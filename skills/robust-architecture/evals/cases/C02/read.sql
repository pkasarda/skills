SELECT r.id,r.signed_at,p.team_id AS approving_team
FROM releases r JOIN people p ON p.id=r.actor_id;

