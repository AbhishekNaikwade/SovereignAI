# Router V1 Failure Analysis

## Case: run backup?
Observed: Classified as QUESTION
Expected: COMMAND
Issue: Question mark rule overrides command intent
Fix Idea: Check command keywords before question rule


## Case: ?????
Observed: Classified as QUESTION
Expected: UNKNOWN
Issue: No semantic validation
Fix Idea: Require alphabetic characters for question


## Case: spaces only
Observed: Validation failed
Expected: Correct
Notes: strip() guardrail works


## Case: RUN cleanup
Observed: COMMAND
Expected: Correct
Notes: Case-insensitive logic works


## Case: spaces + run
Observed: COMMAND
Expected: Correct
Notes: Input normalization works

## Guardrail Bug Found

Issue:
Loop returned OK inside pattern loop

Impact:
Only first banned pattern checked

Fix:
Moved return OK outside loop

Lesson:
Early returns can bypass safety checks

