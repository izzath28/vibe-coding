import time

def get_number(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val < 0 or val > 100:
                print("❌ Please enter a mark between 0 and 100.")
            else:
                return val
        except ValueError:
            print("❌ Invalid input. Please enter a numerical value.")

def main():
    print("🎓 --- STUDENT GRADE CALCULATOR --- 🎓")
    print("Welcome! Let's see how you're doing in your studies.")
    
    name = input("👋 What's your name? ").strip()
    if not name:
        name = "Student"
    
    print(f"\nOkay {name}, let's record your marks for 3 subjects!")
    
    marks = []
    subjects = ["Subject 1", "Subject 2", "Subject 3"]
    
    for sub in subjects:
        mark = get_number(f"📝 Enter marks for {sub}: ")
        marks.append(mark)
        
    average = sum(marks) / len(marks)
    
    # Grading Logic
    if average >= 75:
        grade = "A"
        emoji = "🌟"
        message = "EXCELLENT! You're a superstar! 🚀"
    elif average >= 60:
        grade = "B"
        emoji = "✨"
        message = "GREAT JOB! Keep it up! 👍"
    elif average >= 40:
        grade = "C"
        emoji = "✅"
        message = "GOOD! You've passed. Keep improving! 📚"
    else:
        grade = "FAIL"
        emoji = "😔"
        message = "Don't give up, practice makes perfect! 💪"

    print("\n" + "="*40)
    print(f"📊 Analyzing results for {name}...")
    time.sleep(1)
    
    print(f"{emoji} {message}")
    
    # Requested clean formatted output
    print("-" * 30)
    print(f"Name   : {name}")
    print(f"Average: {average:.1f}")
    print(f"Grade  : {grade}")
    print("-" * 30)
    print("="*40)

if __name__ == "__main__":
    main()
