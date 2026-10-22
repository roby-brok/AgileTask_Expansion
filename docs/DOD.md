# Definition of Done (DoD)

We agreed this list as a whole team in Sprint Zero, before writing any user story. A backlog item is **Done** only when all 5 points are true. If even one is missing, the item goes back to "In Progress". For us there is no "almost done".

1. **All unit tests pass.**
   New or changed code has unit tests, and the full suite (`python -m unittest discover -s tests -v`) is green. No skipped tests and no tests commented out.

2. **Acceptance criteria shown to the PO.**
   We show every acceptance criterion of the story working to Adrian, our Product Owner, and the PO accepts the story.

3. **Code is refactored (Boy Scout Rule applied).**
   We leave every file we touch cleaner than we found it: clear names, no duplicated code, no dead code, small methods that do one thing.

4. **Peer reviewed and merged.**
   At least one other team member reviewed the change, all comments are fixed, and it is merged into `main`. After the merge `main` still runs and all tests still pass.

5. **Rationale document updated.**
   Any design decision or trade-off goes in `docs/RATIONALE.md`, so later we still know why the code is like this.
