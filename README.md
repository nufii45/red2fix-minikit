# minikit (Red2Fix demo)

A tiny Python library with three seeded bugs (see the issues). Every pull request is reviewed by
[Red2Fix](https://github.com/nufii45/red2fix): it writes a test from the linked issue without seeing the diff,
proves it fails on `main` and passes on the PR, runs the existing tests on both, and reviews the diff. The
verdict is the required `red2fix/verdict` status; GitHub auto-merge merges only proven PRs.
