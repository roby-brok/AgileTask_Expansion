# Sprint Zero Reflection

**Team:** Adrian (Product Owner), Blagoy (Scrum Master), Roberto Cassano Brocato (Developer)

Here we answer the review questions about our Sprint Zero for the AgileTask expansion.

---

## 1. How does the "Decreasing Resolution" of the plan (planning detail for 2 weeks vs. 3 months) help our team respond to change instead of following a rigid plan?

Our backlog already shows decreasing resolution. US-01, US-02 and US-03 are the work for the next two weeks, so they have full acceptance criteria and story points. US-04 is further away, so it only has draft criteria and a rough number. Ideas for the next three months are not even written as stories yet, they are just topics we talked about.

US-04 shows why this works. If at the start we had planned three months in detail, we would have put a guess for notifications in the plan, and that guess would be wrong, because we didn't know how rigid `complete_task()` was. One day of spike changed what we knew. Because only the next two weeks are detailed, a new request from the customer, like the real-time notifications, doesn't break anything. It goes into the backlog, Adrian reorders it at the next Sprint Planning, and we lose very little work. With a rigid long-term plan we would have two bad choices: ignore the customer, or throw away a lot of planning. In our opinion detail is only useful when the work is close, because that is when we know enough to plan it well.

## 2. Why is "face-to-face conversation" the most efficient method for our team to reconcile the PO's priorities with the Developers' estimates?

Adrian knows the value of each story and the Developers know the cost. A good backlog needs both views to meet. For example, if Adrian sees that US-03 is 5 points and wonders why, Adrian can ask straight away. The Developer can explain that it needs US-01 first and that the two filters must work together. Then Adrian can decide on the spot to keep the order, or to make the story smaller, for example filtering by category first and by status later. Face to face this takes a few minutes. By email or chat it can take days of messages back and forth, and doubts and tone get lost on the way.

When we talk in the same room we see when someone is confused, we can draw on the whiteboard, and we agree together, so the whole team owns the estimate and the order. This is why the Agile Manifesto puts individuals and interactions over processes and tools. A user story card is only a reminder of a conversation. The real understanding comes from talking, and the acceptance criteria are where we write down what we agreed. We are a small team of three, so meeting face to face is easy for us and it is the quickest way to agree.

## 3. How does our team's DoD prevent the accumulation of Fragility and Opacity in the AgileTask code base?

**Fragility** is when a change in one place breaks something in another place. **Opacity** is when the code is hard to read and understand. Both grow slowly, a little bit every sprint, if nothing stops them. Our DoD stops them because every item must pass it before it is Done.

**Against Fragility:**
- "All unit tests pass" means every change comes with tests, and the full suite must be green. In SP-01 we found a real example. The 3 baseline tests didn't check the `[LOG]` and `[EMAIL]` output at all, so someone could break it and nobody would notice. In the spike we added `test_old_log_and_email_output_is_preserved`. Now if anybody breaks that output, the suite goes red and the story can't be Done.
- "Peer reviewed and merged" means a second person checks the change, and `main` must still pass all the tests after the merge.
- The spike also removed one cause of fragility in the design itself. A new channel is now a new `Notifier` class, so adding one can't break `TaskManager`, because we don't touch it (RD-003).

**Against Opacity:**
- "Code is refactored (Boy Scout Rule applied)" made us clean the code in the same commit as the spike: docstrings, type hints, private fields, f-strings, `mark_complete()`, and `TaskNotFoundError` with a clear message instead of a bare `KeyError`.
- "Rationale document updated" made us write RD-003. The code shows **what** the `Notifier` interface does, but only RD-003 explains **why** it is there and what the trade-off is (`TaskManager()` alone prints nothing now). Without it, a new developer could think the interface is too complicated and put the prints back, and the rigidity would come back.

Spike code is often quick and messy. Because our DoD covers everything we merge, the spike had to pass the same bar as a normal story: tests, refactoring and the rationale. So the spike didn't leave a mess behind. It left the code cleaner than the baseline. The DoD fixes these problems in small pieces in every sprint, instead of letting them pile up until the only option is a big rewrite.
