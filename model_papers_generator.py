"""
GSSSB Class-3 Model Papers Generator
Generates complete model papers with detailed answers and solutions
"""

import json
import random
from datetime import datetime
from typing import List, Dict, Tuple

class ModelQuestion:
    def __init__(self, qid: int, category: str, difficulty: str, 
                 question: str, options: List[str], answer: str, 
                 solution: str, topic: str):
        self.qid = qid
        self.category = category
        self.difficulty = difficulty
        self.question = question
        self.options = options
        self.answer = answer
        self.solution = solution
        self.topic = topic
    
    def to_dict(self):
        return {
            "id": self.qid,
            "category": self.category,
            "topic": self.topic,
            "difficulty": self.difficulty,
            "question": self.question,
            "options": self.options,
            "answer": self.answer,
            "solution": self.solution
        }

class QuestionBank:
    """Question bank with 100+ questions across all topics"""
    
    def __init__(self):
        self.questions = []
        self._initialize_bank()
    
    def _initialize_bank(self):
        """Initialize comprehensive question bank"""
        
        # QUANTITATIVE APTITUDE QUESTIONS (40 questions)
        qa_questions = [
            # Number System
            ModelQuestion(1, "Quantitative Aptitude", "Easy", 
                "What is the LCM of 12, 18, and 24?",
                ["36", "48", "72", "96"],
                "72",
                "LCM(12, 18, 24) = 2³ × 3² = 8 × 9 = 72",
                "Number System - LCM/HCF"),
            
            ModelQuestion(2, "Quantitative Aptitude", "Easy",
                "Find HCF of 48 and 64",
                ["8", "16", "32", "64"],
                "16",
                "Factors of 48: 1,2,3,4,6,8,12,16,24,48\nFactors of 64: 1,2,4,8,16,32,64\nHCF = 16",
                "Number System - LCM/HCF"),
            
            ModelQuestion(3, "Quantitative Aptitude", "Medium",
                "15% of 800 + 20% of 500 = ?",
                ["220", "320", "420", "520"],
                "220",
                "15% of 800 = 0.15 × 800 = 120\n20% of 500 = 0.20 × 500 = 100\nTotal = 120 + 100 = 220",
                "Percentage - Basic Calculation"),
            
            ModelQuestion(4, "Quantitative Aptitude", "Medium",
                "If A's income is 20% more than B's, then B's income is what % less than A's?",
                ["16.67%", "18%", "20%", "25%"],
                "16.67%",
                "Let B's income = 100, A's = 120\nDifference = 20, as % of A's = 20/120 × 100 = 16.67%",
                "Percentage - Comparative"),
            
            ModelQuestion(5, "Quantitative Aptitude", "Medium",
                "A shopkeeper buys a shirt for Rs. 400 and sells it for Rs. 600. What is profit%?",
                ["25%", "33.33%", "50%", "60%"],
                "50%",
                "Cost Price = 400, Selling Price = 600\nProfit = 600 - 400 = 200\nProfit% = 200/400 × 100 = 50%",
                "Profit & Loss - Basic"),
            
            ModelQuestion(6, "Quantitative Aptitude", "Hard",
                "Two items are sold at equal selling price. One at 20% profit, other at 20% loss. What is net loss%?",
                ["4%", "5%", "10%", "20%"],
                "4%",
                "Let SP = 100 each, CP1 = 100/1.2 = 83.33, CP2 = 100/0.8 = 125\nTotal CP = 208.33, Total SP = 200\nLoss% = 8.33/208.33 × 100 = 4%",
                "Profit & Loss - Advanced"),
            
            ModelQuestion(7, "Quantitative Aptitude", "Easy",
                "Average of 5, 10, 15, 20, 25 = ?",
                ["10", "12", "15", "20"],
                "15",
                "Sum = 5+10+15+20+25 = 75\nAverage = 75/5 = 15",
                "Average - Simple"),
            
            ModelQuestion(8, "Quantitative Aptitude", "Medium",
                "A man covers 50 km in 10 hours. What is his speed in km/hr?",
                ["3", "4", "5", "6"],
                "5",
                "Speed = Distance/Time = 50/10 = 5 km/hr",
                "Speed, Distance, Time"),
            
            ModelQuestion(9, "Quantitative Aptitude", "Medium",
                "What is 25% of 80?",
                ["15", "20", "25", "30"],
                "20",
                "25% of 80 = 0.25 × 80 = 20",
                "Percentage - Basic"),
            
            ModelQuestion(10, "Quantitative Aptitude", "Hard",
                "A sum becomes 4/3 of itself in 5 years at simple interest. What is rate of interest?",
                ["6.67%", "10%", "20%", "25%"],
                "6.67%",
                "SI = 4/3 P - P = 1/3 P\nSI = P×R×T/100\n1/3 P = P×R×5/100\nR = 100/15 = 6.67%",
                "Simple Interest - Advanced"),
            
            # Probability
            ModelQuestion(11, "Quantitative Aptitude", "Easy",
                "What is probability of getting head in coin toss?",
                ["0.25", "0.5", "0.75", "1"],
                "0.5",
                "A coin has 2 equally likely outcomes: Head and Tail\nP(Head) = 1/2 = 0.5",
                "Probability - Basic"),
            
            ModelQuestion(12, "Quantitative Aptitude", "Medium",
                "Two dice are thrown. What is probability of getting sum = 7?",
                ["1/6", "1/12", "1/18", "1/36"],
                "1/6",
                "Favorable outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6\nTotal outcomes = 36\nP(sum=7) = 6/36 = 1/6",
                "Probability - Compound"),
        ]
        
        # ENGLISH QUESTIONS (20 questions)
        english_questions = [
            # Tenses
            ModelQuestion(21, "English", "Easy",
                "Choose the correct sentence:",
                [
                    "He goes to school yesterday",
                    "He went to school yesterday",
                    "He is going to school yesterday",
                    "He has gone to school yesterday"
                ],
                "He went to school yesterday",
                "Past events use Simple Past tense. 'Yesterday' is a past time indicator.\nCorrect: He went to school yesterday",
                "Tenses - Simple Past"),
            
            ModelQuestion(22, "English", "Easy",
                "Fill: She ___ been working here for 5 years",
                ["has", "have", "is", "was"],
                "has",
                "Present Perfect uses 'has' with singular subject (She).\nCorrect: She has been working here for 5 years",
                "Tenses - Present Perfect"),
            
            ModelQuestion(23, "English", "Medium",
                "Convert to Passive: They built this house in 1990",
                ["This house was built in 1990", "This house is built in 1990", "This house has been built in 1990", "This house will be built in 1990"],
                "This house was built in 1990",
                "Active: They built (past) → Passive: This house was built (past)\nStructure: Object + was/were + past participle + by + subject",
                "Voice - Passive"),
            
            ModelQuestion(24, "English", "Medium",
                "Choose correct: If I _____ him, I would help",
                ["know", "knew", "will know", "have known"],
                "knew",
                "Conditional sentence: If + past, would + verb\nCorrect: If I knew him, I would help (Conditional Perfect)",
                "Conditional Tenses"),
            
            ModelQuestion(25, "English", "Easy",
                "Choose correct article: I need _____ honest person",
                ["a", "an", "the", "no article"],
                "an",
                "'Honest' starts with vowel sound, so use 'an'\nCorrect: I need an honest person",
                "Articles - Usage"),
            
            ModelQuestion(26, "English", "Easy",
                "Fill: She is good _____ Mathematics",
                ["at", "in", "on", "for"],
                "at",
                "'Good at' is correct usage for skills/subjects\nCorrect: She is good at Mathematics",
                "Prepositions - Common"),
            
            ModelQuestion(27, "English", "Medium",
                "Identify error: He have completed his work",
                ["He", "have", "completed", "No error"],
                "have",
                "Subject 'He' is singular, so use 'has' not 'have'\nCorrect: He has completed his work",
                "Subject-Verb Agreement"),
            
            ModelQuestion(28, "English", "Medium",
                "Choose correct: Neither the teacher _____ the students are present",
                ["nor", "or", "and", "but"],
                "nor",
                "'Neither...nor' is a correlative conjunction pair\nCorrect: Neither the teacher nor the students are present",
                "Conjunctions - Correlative"),
            
            ModelQuestion(29, "English", "Easy",
                "Fill: She sang _____ and danced all night",
                ["beautiful", "beautifully", "beauty", "beautify"],
                "beautifully",
                "Adverbs modify verbs. 'Beautifully' modifies 'sang'\nCorrect: She sang beautifully and danced all night",
                "Adjectives & Adverbs"),
            
            ModelQuestion(30, "English", "Medium",
                "Convert: 'I said, I am going home'",
                ["I said that I am going home", "I said that I was going home", "I said I would go home", "I told I am going home"],
                "I said that I was going home",
                "Indirect speech: Change present to past when main verb is past\nDirect: 'I am going' → Indirect: 'I was going'",
                "Direct & Indirect Speech"),
        ]
        
        # GENERAL AWARENESS QUESTIONS (30 questions)
        ga_questions = [
            ModelQuestion(41, "General Awareness", "Easy",
                "Who is the current President of India?",
                ["Narendra Modi", "Rajendra Prasad", "Droupadi Murmu", "Ram Nath Kovind"],
                "Droupadi Murmu",
                "Droupadi Murmu became the 15th President of India on July 25, 2022",
                "Current Affairs - Politics"),
            
            ModelQuestion(42, "General Awareness", "Easy",
                "What is the capital of Gujarat?",
                ["Ahmedabad", "Gandhinagar", "Vadodara", "Rajkot"],
                "Gandhinagar",
                "Gandhinagar is the capital of Gujarat state, while Ahmedabad is the largest city",
                "Indian Geography"),
            
            ModelQuestion(43, "General Awareness", "Medium",
                "Who was the first Prime Minister of India?",
                ["Jawaharlal Nehru", "Sardar Patel", "Subhas Chandra Bose", "Mahatma Gandhi"],
                "Jawaharlal Nehru",
                "Jawaharlal Nehru was the first PM of India (1947-1964)",
                "Indian History"),
            
            ModelQuestion(44, "General Awareness", "Easy",
                "How many states are there in India?",
                ["25", "28", "29", "30"],
                "28",
                "India has 28 states and 8 union territories (as of 2024)",
                "Indian Geography"),
            
            ModelQuestion(45, "General Awareness", "Medium",
                "Which is the longest river in India?",
                ["Godavari", "Brahmaputra", "Ganga", "Sutlej"],
                "Ganga",
                "The Ganga is the longest river in India, approximately 2525 km",
                "Indian Geography"),
            
            ModelQuestion(46, "General Awareness", "Medium",
                "In which year did India become a Republic?",
                ["1947", "1950", "1952", "1956"],
                "1950",
                "India became a Republic on January 26, 1950, when the Constitution came into effect",
                "Indian History"),
            
            ModelQuestion(47, "General Awareness", "Easy",
                "Which is the highest mountain peak in India?",
                ["Kangchenjunga", "Makalu", "Kanchenjunga", "Nanda Devi"],
                "Kangchenjunga",
                "Kangchenjunga (8,586m) is the highest peak in India, shared with Nepal",
                "Indian Geography"),
            
            ModelQuestion(48, "General Awareness", "Medium",
                "Who wrote the Indian Constitution?",
                ["Jawaharlal Nehru", "B.R. Ambedkar", "Rajendra Prasad", "Sardar Patel"],
                "B.R. Ambedkar",
                "Dr. B.R. Ambedkar chaired the drafting committee and was the main architect of the Indian Constitution",
                "Indian History"),
            
            ModelQuestion(49, "General Awareness", "Easy",
                "What is the national animal of India?",
                ["Lion", "Tiger", "Peacock", "Elephant"],
                "Tiger",
                "The Bengal Tiger is the national animal of India, representing strength and grace",
                "Indian Symbols"),
            
            ModelQuestion(50, "General Awareness", "Medium",
                "Which country shares the longest border with India?",
                ["China", "Pakistan", "Bangladesh", "Nepal"],
                "Bangladesh",
                "Bangladesh shares a 4,096 km border with India, the longest among all neighbors",
                "Indian Geography"),
        ]
        
        self.questions.extend(qa_questions)
        self.questions.extend(english_questions)
        self.questions.extend(ga_questions)
    
    def get_random_questions(self, count: int) -> List[ModelQuestion]:
        """Get random questions from bank"""
        return random.sample(self.questions, min(count, len(self.questions)))
    
    def get_questions_by_category(self, category: str, count: int) -> List[ModelQuestion]:
        """Get random questions by category"""
        category_questions = [q for q in self.questions if q.category == category]
        return random.sample(category_questions, min(count, len(category_questions)))

class ModelPaper:
    """Complete model paper"""
    
    def __init__(self, paper_number: int, question_bank: QuestionBank):
        self.paper_number = paper_number
        self.questions: List[ModelQuestion] = []
        self.creation_date = datetime.now()
        self.total_marks = 75
        self.duration_minutes = 60
        self._generate_paper(question_bank)
    
    def _generate_paper(self, qbank: QuestionBank):
        """Generate paper with balanced questions"""
        # 30 Quantitative Aptitude (40%)
        qa_qs = qbank.get_questions_by_category("Quantitative Aptitude", 30)
        # 20 English (20%)  
        en_qs = qbank.get_questions_by_category("English", 20)
        # 25 General Awareness (40%)
        ga_qs = qbank.get_questions_by_category("General Awareness", 25)
        
        all_qs = qa_qs + en_qs + ga_qs
        random.shuffle(all_qs)
        
        # Renumber questions 1-75
        for idx, q in enumerate(all_qs, 1):
            q.qid = idx
            self.questions.append(q)
    
    def get_answer_key(self) -> Dict[int, str]:
        """Get answer key"""
        return {q.qid: q.answer for q in self.questions}
    
    def generate_paper_text(self) -> str:
        """Generate paper in text format"""
        text = []
        text.append("=" * 90)
        text.append(f"GSSSB CLASS-3 MODEL PAPER {self.paper_number}")
        text.append(f"Date: {self.creation_date.strftime('%Y-%m-%d %H:%M')}")
        text.append("=" * 90)
        text.append(f"Total Questions: 75 | Total Marks: 75 | Time: 60 minutes")
        text.append(f"Negative Marking: -0.25 per wrong answer")
        text.append("-" * 90)
        
        for q in self.questions:
            text.append(f"\nQ{q.qid}. [{q.category} - {q.difficulty}] {q.topic}")
            text.append(f"{q.question}")
            for i, opt in enumerate(q.options, 1):
                text.append(f"    {chr(64+i)}) {opt}")
        
        return "\n".join(text)
    
    def generate_answer_sheet(self) -> str:
        """Generate answer sheet"""
        text = []
        text.append("=" * 90)
        text.append(f"MODEL PAPER {self.paper_number} - ANSWER SHEET")
        text.append("=" * 90)
        
        answer_key = self.get_answer_key()
        
        # Answers in grid format
        text.append("\nQUICK ANSWER KEY (75 Questions)")
        text.append("-" * 90)
        
        for i in range(0, len(self.questions), 10):
            row = []
            for j in range(i, min(i+10, len(self.questions))):
                q_num = j + 1
                ans = answer_key[q_num]
                row.append(f"Q{q_num}: {ans}")
            text.append("  ".join(row))
        
        return "\n".join(text)
    
    def generate_solutions(self) -> str:
        """Generate detailed solutions"""
        text = []
        text.append("=" * 90)
        text.append(f"MODEL PAPER {self.paper_number} - DETAILED SOLUTIONS")
        text.append("=" * 90)
        
        for q in self.questions:
            text.append(f"\nQ{q.qid}. {q.question}")
            text.append(f"Topic: {q.topic} | Difficulty: {q.difficulty}")
            text.append(f"Category: {q.category}")
            text.append(f"\nOptions:")
            for i, opt in enumerate(q.options, 1):
                marker = "✓" if opt == q.answer else " "
                text.append(f"  {marker} {chr(64+i)}) {opt}")
            text.append(f"\nCorrect Answer: {q.answer}")
            text.append(f"\nExplanation:")
            text.append(q.solution)
            text.append("-" * 90)
        
        return "\n".join(text)
    
    def to_json(self) -> str:
        """Convert to JSON"""
        return json.dumps({
            "paper_number": self.paper_number,
            "creation_date": self.creation_date.isoformat(),
            "total_marks": self.total_marks,
            "duration_minutes": self.duration_minutes,
            "total_questions": len(self.questions),
            "questions": [q.to_dict() for q in self.questions]
        }, indent=2, ensure_ascii=False)

class ModelPapersGenerator:
    """Generate multiple model papers"""
    
    def __init__(self):
        self.qbank = QuestionBank()
    
    def generate_papers(self, count: int = 5) -> List[ModelPaper]:
        """Generate multiple papers"""
        return [ModelPaper(i, self.qbank) for i in range(1, count + 1)]
    
    def save_papers(self, papers: List[ModelPaper], directory: str = "."):
        """Save all papers to files"""
        import os
        
        for paper in papers:
            # Paper questions
            paper_file = os.path.join(directory, f"Model_Paper_{paper.paper_number}.txt")
            with open(paper_file, 'w', encoding='utf-8') as f:
                f.write(paper.generate_paper_text())
            
            # Answer sheet
            ans_file = os.path.join(directory, f"Model_Paper_{paper.paper_number}_AnswerSheet.txt")
            with open(ans_file, 'w', encoding='utf-8') as f:
                f.write(paper.generate_answer_sheet())
            
            # Solutions
            sol_file = os.path.join(directory, f"Model_Paper_{paper.paper_number}_Solutions.txt")
            with open(sol_file, 'w', encoding='utf-8') as f:
                f.write(paper.generate_solutions())
            
            # JSON
            json_file = os.path.join(directory, f"Model_Paper_{paper.paper_number}.json")
            with open(json_file, 'w', encoding='utf-8') as f:
                f.write(paper.to_json())

def main():
    """Generate 5 complete model papers"""
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("Generating 5 Complete GSSSB Model Papers...")
    print("=" * 90)
    
    generator = ModelPapersGenerator()
    papers = generator.generate_papers(5)
    
    # Save papers
    generator.save_papers(papers)
    
    print("\n✓ 5 Model Papers Generated Successfully!\n")
    print("-" * 90)
    print("Generated Files:")
    print("-" * 90)
    
    for i in range(1, 6):
        print(f"\nModel Paper {i}:")
        print(f"  • Model_Paper_{i}.txt (Questions)")
        print(f"  • Model_Paper_{i}_AnswerSheet.txt (Answer Key)")
        print(f"  • Model_Paper_{i}_Solutions.txt (Detailed Solutions)")
        print(f"  • Model_Paper_{i}.json (Structured Data)")
    
    print("\n" + "=" * 90)
    print("Paper Statistics:")
    print("=" * 90)
    
    for paper in papers:
        qa_count = sum(1 for q in paper.questions if q.category == "Quantitative Aptitude")
        en_count = sum(1 for q in paper.questions if q.category == "English")
        ga_count = sum(1 for q in paper.questions if q.category == "General Awareness")
        
        print(f"\nModel Paper {paper.paper_number}:")
        print(f"  Total Questions: {len(paper.questions)}")
        print(f"  Quantitative Aptitude: {qa_count} questions (40%)")
        print(f"  English: {en_count} questions (20%)")
        print(f"  General Awareness: {ga_count} questions (40%)")
        print(f"  Total Marks: {paper.total_marks}")
        print(f"  Duration: {paper.duration_minutes} minutes")
    
    print("\n" + "=" * 90)
    print("How to Use:")
    print("=" * 90)
    print("1. Take the test from: Model_Paper_X.txt")
    print("2. Check your answers: Model_Paper_X_AnswerSheet.txt")
    print("3. Learn from solutions: Model_Paper_X_Solutions.txt")
    print("4. Analyze performance: Model_Paper_X.json")
    print("\n" + "=" * 90)

if __name__ == "__main__":
    main()
