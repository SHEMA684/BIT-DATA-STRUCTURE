"""
STACK QUESTIONS - COMPLETE SOLUTIONS
Following instructions: Practical tasks with screenshots, Challenge with algorithm, Reflection theoretical only
"""

# =============================================================================
# PRACTICAL TASK 1: MoMo Transaction
# Complete code with screenshot-style output format
# =============================================================================

print("=" * 60)
print("PRACTICAL TASK 1: MoMo TRANSACTION")
print("=" * 60)

# Complete code implementation
momo_stack = []

# Push all transaction steps
momo_stack.append("Enter Number")
momo_stack.append("Enter Amount") 
momo_stack.append("Confirm")

print("SCREENSHOT-STYLE OUTPUT:")
print("-" * 25)
print("Step 1: Push operations")
print("Stack after all pushes: ['Enter Number', 'Enter Amount', 'Confirm']")
print("Visual representation:")
print("  |   'Confirm'    | <- TOP (most recent)")
print("  | 'Enter Amount' |")
print("  | 'Enter Number' | <- BOTTOM (first added)")
print()

# Undo one operation
undone = momo_stack.pop()

print("Step 2: Undo operation (pop)")
print(f"Removed: {undone}")
print(f"Stack after undo: {momo_stack}")
print("Visual representation:")
print("  | 'Enter Amount' | <- TOP (remaining)")
print("  | 'Enter Number' | <- BOTTOM")
print()

print("FINAL ANSWER:")
print(f"Step that remains at top: '{momo_stack[-1]}'")
print()

# Complete output display
print("COMPLETE EXECUTION OUTPUT:")
print("Initial stack: []")
print("After push 'Enter Number': ['Enter Number']")
print("After push 'Enter Amount': ['Enter Number', 'Enter Amount']") 
print("After push 'Confirm': ['Enter Number', 'Enter Amount', 'Confirm']")
print(f"After pop(): {momo_stack} (removed: {undone})")
print(f"Remaining top element: {momo_stack[-1]}")

print("\n" + "=" * 60)

# =============================================================================
# PRACTICAL TASK 2: UR Student Assignments  
# Complete code with screenshot-style output format
# =============================================================================

print("PRACTICAL TASK 2: UR STUDENT ASSIGNMENTS")
print("=" * 60)

# Complete code implementation
ur_stack = []

# Push all assignments
ur_stack.append("Assignment1")
ur_stack.append("Assignment2")
ur_stack.append("Assignment3")

print("SCREENSHOT-STYLE OUTPUT:")
print("-" * 25)
print("Step 1: Push all assignments")
print("Stack after all pushes: ['Assignment1', 'Assignment2', 'Assignment3']")
print("Visual representation:")
print("  | 'Assignment3' | <- TOP (most recent)")
print("  | 'Assignment2' |")
print("  | 'Assignment1' | <- BOTTOM (first added)")
print()

# Pop two assignments
first_pop = ur_stack.pop()   # Removes Assignment3
second_pop = ur_stack.pop()  # Removes Assignment2

print("Step 2: Pop two assignments")
print(f"First pop removed: {first_pop}")
print(f"Second pop removed: {second_pop}")
print(f"Stack after two pops: {ur_stack}")
print("Visual representation:")
print("  | 'Assignment1' | <- Only remaining assignment")
print()

print("FINAL ANSWER:")
print(f"Assignment left: '{ur_stack[0]}'")
print()

# Complete output display
print("COMPLETE EXECUTION OUTPUT:")
print("Initial stack: []")
print("After push 'Assignment1': ['Assignment1']")
print("After push 'Assignment2': ['Assignment1', 'Assignment2']")
print("After push 'Assignment3': ['Assignment1', 'Assignment2', 'Assignment3']")
print(f"After first pop(): {['Assignment1', 'Assignment2']} (removed: Assignment3)")
print(f"After second pop(): {ur_stack} (removed: Assignment2)")
print(f"Final remaining: {ur_stack[0]}")

print("\n" + "=" * 60)

# =============================================================================
# CHALLENGE: Reverse "KIGALI" using Stack
# Clear algorithmic sequence with step-by-step explanation
# =============================================================================

print("CHALLENGE: REVERSE 'KIGALI' USING STACK")
print("=" * 60)

print("ALGORITHMIC SEQUENCE:")
print("-" * 20)

# Algorithm Step 1: Initialize
print("STEP 1: Initialize")
word = "KIGALI"
char_stack = []
reversed_word = ""
print(f"  - Input word: '{word}'")
print(f"  - Empty stack: {char_stack}")
print(f"  - Result string: '{reversed_word}'")

# Algorithm Step 2: Push Phase
print("\nSTEP 2: Push each character onto stack (LIFO preparation)")
for i, char in enumerate(word):
    char_stack.append(char)
    print(f"  2.{i+1}: Push '{char}' -> Stack: {char_stack}")

print(f"  Final stack after all pushes: {char_stack}")
print("  Stack visualization (bottom to top): K-I-G-A-L-I")

# Algorithm Step 3: Pop Phase  
print("\nSTEP 3: Pop each character to build reversed string")
step_counter = 1
original_stack = char_stack.copy()  # Keep copy for display

while char_stack:
    popped_char = char_stack.pop()
    reversed_word += popped_char
    print(f"  3.{step_counter}: Pop '{popped_char}' -> Add to result: '{reversed_word}' -> Stack: {char_stack}")
    step_counter += 1

# Algorithm Step 4: Result
print(f"\nSTEP 4: Final Result")
print(f"  - Original: '{word}'")
print(f"  - Reversed: '{reversed_word}'")
print(f"  - Verification: Each character popped in reverse order due to LIFO")

# Code implementation with line-by-line explanation
print("\nCORRESPONDING CODE LINES:")
print("-" * 25)
print("word = 'KIGALI'              # Step 1: Initialize input")
print("char_stack = []              # Step 1: Create empty stack") 
print("reversed_word = ''           # Step 1: Initialize result")
print()
print("for char in word:            # Step 2: Iterate through characters")
print("    char_stack.append(char)  # Step 2: Push each character")
print()
print("while char_stack:            # Step 3: While stack not empty")
print("    popped = char_stack.pop() # Step 3: Remove from top (LIFO)")
print("    reversed_word += popped   # Step 3: Build reversed string")
print()
print("print(reversed_word)         # Step 4: Display result")

print(f"\nALGORITHM OUTPUT: '{word}' -> '{reversed_word}'")

print("\n" + "=" * 60)

# =============================================================================
# REFLECTION: Why stack helpful for reversing words but not serving people?
# Theoretical discussion only - no code required per instructions
# =============================================================================

print("REFLECTION: THEORETICAL ANALYSIS")
print("=" * 60)

print("QUESTION: Why is stack helpful for reversing words but not for serving people?")
print()

print("THEORETICAL DISCUSSION:")
print("-" * 22)

print("\n1. NATURE OF DATA vs HUMANS:")
print("   • Words/characters are passive data with no expectations")
print("   • Humans have social expectations and concepts of fairness")
print("   • Data doesn't care about processing order")
print("   • People expect fair treatment based on arrival order")

print("\n2. STACK CHARACTERISTICS (LIFO - Last In, First Out):")
print("   • Naturally reverses input order")
print("   • Most recent item processed first") 
print("   • Efficient for 'undo' type operations")
print("   • Perfect mechanical reversal mechanism")

print("\n3. WHY STACK WORKS FOR WORD REVERSAL:")
print("   • Desired outcome IS reversal of character order")
print("   • No ethical implications in data manipulation")
print("   • LIFO property directly achieves the goal")
print("   • Efficient single-pass algorithm")

print("\n4. WHY STACK FAILS FOR SERVING PEOPLE:")
print("   • Violates 'First Come, First Served' principle")
print("   • Creates perceived unfairness and potential conflict")
print("   • Last person in line gets served first (counterintuitive)")
print("   • Conflicts with social norms and expectations")

print("\n5. APPROPRIATE DATA STRUCTURE FOR PEOPLE:")
print("   • Queue (FIFO - First In, First Out)")
print("   • Maintains arrival order")
print("   • Aligns with fairness expectations")
print("   • Prevents social conflicts")

print("\n6. CORE PRINCIPLE:")
print("   • Technical efficiency ≠ Social appropriateness")
print("   • Data structures must match problem context")
print("   • Consider human factors, not just algorithmic efficiency")
print("   • Same tool can be perfect for one use, terrible for another")

print("\nCONCLUSION:")
print("Stack's LIFO property makes it ideal for reversing operations")
print("but inappropriate for fair human service scenarios where")
print("order preservation and social fairness are paramount.")

print("\n" + "=" * 60)
print("END OF SOLUTIONS")
print("=" * 60)