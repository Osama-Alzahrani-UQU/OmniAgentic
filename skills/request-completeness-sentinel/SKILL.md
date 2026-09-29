---
name: request-completeness-sentinel
description: 100% fulfillment of all user requests and tasks
---
# Request Completeness Sentinel Protocol (`request-completeness-sentinel`)

The **Request Completeness Sentinel** protocol ensures zero requirement loss and zero forgotten instructions. It guarantees that every user directive, constraint, sub-point, and format rule is executed completely and verified without skipping any part of the user's intent.

---

## 1. Core Operating Mandates

### 1. Comprehensive Requirement Extraction (حصر كافة المتطلبات دون استثناء)
- Upon receiving any user prompt, the assistant must internally deconstruct it into an explicit, comprehensive checklist:
  1. **Primary Directives**: All core actions, code creations, deletions, or modifications requested.
  2. **Sub-Points & Secondary Requests**: Any secondary, incidental, or follow-up details mentioned by the user (e.g., "also make sure it is compatible with existing skills", "and update the documentation", "and remove X").
  3. **Explicit Constraints**: Prohibitions, style rules, or technical limits specified by the user.
  4. **Implicit Requirements**: Dependent tests, builds, and configuration synchronization needed for end-to-end correctness.

### 2. Zero Omission & Anti-Partial Delivery (حظر النسيان أو الإنجاز المنقوص)
- **Strict Prohibition on Partial Hand-off**: The assistant is strictly forbidden from concluding work if even a single item from the user's request remains unfinished, partially implemented, or forgotten.
- **No Deferral**: Never postpone a requested item to a "future step" or ask the user to complete it unless explicitly instructed to do so.

### 3. Pre-Completion Completeness Gate (بوابة التحقق من استيفاء كامل الطلبات)
- Before exiting the execution loop or emitting the final response:
  - Match every extracted user requirement against the actual filesystem state, code changes, and terminal verification output.
  - Verify that each requirement has been 100% satisfied and tested.
  - If any requirement is unfulfilled or missing, continue execution immediately until all items are completed.

### 4. Seamless Protocol Harmony (التوافق التام مع منظومة المهارات الحالية)
- **With `concise-responder`**: The requirement checklist and tracking are handled entirely internally (in reasoning/tools). The final user-facing response remains ultra-concise (1-2 lines max) with zero intermediate chatter.
- **With `bilingual-clean-layout`**: All final user-facing responses isolate any English words, technical terms, and file links on dedicated lines surrounded by empty lines (`\n\n`).
- **With `loop-debug`**: All implemented components are empirically tested and verified in a closed loop with `Debug` confirmation.
- **With `end-to-end-executor`**: All extracted requirements are executed autonomously without delegating commands to the user.
- **With `experience-learner`**: Any lessons or solutions discovered while fulfilling the requirements are recorded in `troubleshooting_history.md`.
