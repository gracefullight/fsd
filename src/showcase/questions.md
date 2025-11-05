# FSD Project Showcase

> As you prepare for your Showcase presentation (Part 3), please review this Sample Question List.
> These are the kinds of questions I may ask about your design, logic, testing, and teamwork.
> You don’t need to memorise answers — just be ready to explain your own code and what you learned.

## By now, each group should demonstrate

- Technical fluency: Writing functional, modular code in Java or Python.
- Data handling: Reading/writing to local files (students.data), serialization, and validation.
- Design understanding: Applying Model–View–Controller (MVC) logic, separating UI logic from backend data handling.
- Regex validation: Implementing correct email and password rules.
- Error handling: Managing edge cases (duplicate student, invalid input, subject limit, etc.).
- Testing & debugging: Matching outputs to given sample I/O.
- Collaboration: Integrating each member’s work into one consistent system.

## Concept & Design (5 examples)

- How does your implementation follow the MVC structure?
- What data structures did you use to store subjects and students, and why?
- Explain how your program handles persistence — what happens when the system restarts?
- How did you ensure the system remains scalable if more features were added?
- Describe one key difference between your CLI and GUI implementation.

## Coding & Logic (Python variants)

- How did you validate emails and passwords using regex?
- What method generates unique IDs for students and subjects?
- Can you explain how marks and grades are calculated?
- How does your code prevent enrolment beyond four subjects?
- If the students.data file doesn’t exist, what happens?

### Optional follow-ups for each language

- Python: How did you use pickle / json, and how did you handle exceptions with try–except?

## Error Handling & Testing

- What exceptions or input errors did you anticipate and handle?
- How did you test your system to confirm all menus and file operations worked?
- What happens if an admin removes a student currently enrolled in subjects?
- How did you verify data integrity after write/read operations?

## GUI

- How does your GUI interact with the backend data file?
- How do you manage window transitions (Login → Enrolment → Subject list)?
- Which GUI framework did you use (Tkinter), and why?
- How did you handle empty input or invalid login attempts in the GUI?

## Reflection & Teamwork

- What was your biggest coding or integration challenge, and how did you solve it?
- How did your group divide and merge tasks effectively?
- What new skills or tools did you learn through this project?
- If you could redesign one feature, what would it be and why?
- How does this project prepare you for real software development roles?
