# Parcel inspection
A single-depot Python service records parcel inspections. A worker processes queued inspection requests; an operator can revise parcel contents before a worker finishes. SQLite supports transactions. The scanner is external and can finish late. Run python -m unittest discover -s tests.
