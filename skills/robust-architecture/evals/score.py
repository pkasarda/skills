"""Validate blind-judge evidence and aggregate it; this does not grade semantics."""
from pathlib import Path
from collections import Counter
import json


def validate_response(grade, answer, criteria):
    rows = grade['criteria']
    ids = [row['id'].replace('-', '.') for row in rows]
    assert len(ids) == len(set(ids)) and set(ids) == set(criteria), ids
    for row, cid in zip(rows, ids):
        assert type(row['pass']) is bool
        assert isinstance(row['reason'], str) and row['reason'].strip()
        quote = row['evidence_quote']
        if row['pass']:
            assert quote and quote in answer, (cid, quote)
        elif quote:
            assert quote in answer, (cid, quote)
    return rows


def aggregate(root):
    rubric = json.loads((root/'rubric.json').read_text())
    expected = {row['id']: {c['id']: c for c in row['criteria']} for row in rubric}
    grades = json.loads((root/'results/isolated/blind-grades.json').read_text())
    key = json.loads((root/'operator/isolated-blind-key.json').read_text())
    assert len(grades['cases']) == len(expected) == len({x['id'] for x in grades['cases']})
    totals = {'A': Counter(), 'B': Counter()}
    per_case = []; failures = []
    for case in grades['cases']:
        cid = case['id']; assert set(case['responses']) == {'X', 'Y'}
        assert set(key[cid].values()) == {'A', 'B'}
        case_scores = {}
        for variant, grade in case['responses'].items():
            condition = key[cid][variant]
            raw = json.loads((root/'answers/isolated'/f'{cid}-{condition}.json').read_text())
            assert raw['id'] == cid
            rows = validate_response(grade, raw['answer'], expected[cid])
            case_scores[condition] = sum(row['pass'] for row in rows)
            for row in rows:
                criterion = expected[cid][row['id'].replace('-', '.')]
                stats = totals[condition]
                stats['total'] += 1; stats['passed'] += row['pass']
                if criterion['critical']:
                    stats['critical_total'] += 1; stats['critical_passed'] += row['pass']
                if not row['pass']:
                    failures.append({'case': cid, 'condition': condition, 'criterion': criterion['id'], 'critical': criterion['critical'], 'reason': row['reason']})
        per_case.append({'id': cid, 'baseline': case_scores['A'], 'with_skill': case_scores['B'], 'maximum': len(expected[cid])})
    candidate = totals['B']
    return {'dataset': 'structured-paired-v1', 'candidate_instruction_hash': json.loads((root/'operator/conditions.json').read_text())['skill_hash'], 'current_version_results': 'revision2/results/aggregate.json', 'cases': per_case, 'totals': {('baseline' if k == 'A' else 'with_skill'): dict(v) for k,v in totals.items()}, 'failures': failures, 'rubric_issues': grades.get('rubric_issues', []), 'candidate_critical_gate': candidate['critical_passed'] == candidate['critical_total'] and not grades.get('rubric_issues'), 'scope': 'Synthetic design proposals, one fresh model context per case/condition; not implementation/runtime proof or a universal guarantee.'}


def self_check():
    criteria = {'T.1': {'critical': True}}
    good = {'criteria': [{'id': 'T.1', 'pass': True, 'evidence_quote': 'bounded', 'reason': 'Visible bounded contract'}]}
    validate_response(good, 'Use a bounded buffer.', criteria)
    bad = {'criteria': [{'id': 'T.1', 'pass': True, 'evidence_quote': 'never present', 'reason': 'Fabricated evidence'}]}
    try:
        validate_response(bad, 'Use a bounded buffer.', criteria)
    except AssertionError:
        pass
    else:
        raise AssertionError('Fabricated passing evidence was accepted')


if __name__ == '__main__':
    self_check()
    root = Path(__file__).resolve().parent
    result = aggregate(root)
    (root/'results/aggregate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))
    if not result['candidate_critical_gate']:
        raise SystemExit(2)
