"""
CCE Gujarat Government Exam Model Paper Generator
Generates comprehensive model papers with answers, analysis, and predictions
"""

import json
import random
from datetime import datetime
from typing import List, Dict, Tuple

# Exam Configuration
EXAM_CONFIG = {
    "exam_name": "CCE Gujarat Government Exam",
    "total_marks": 100,
    "total_questions": 100,
    "duration_minutes": 60,
    "marking_scheme": {
        "correct": 1,
        "negative": -0.25
    },
    "subjects": [
        "Reasoning Ability",
        "Quantitative Aptitude",
        "English Language",
        "Gujarati Language"
    ],
    "questions_per_subject": 25
}

class ExamQuestion:
    def __init__(self, qid: int, subject: str, question_text: str, 
                 options: List[str], correct_answer: str, difficulty: str):
        self.qid = qid
        self.subject = subject
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty
        self.frequency = 0  # Times this question appeared in past exams
        
    def to_dict(self):
        return {
            "id": self.qid,
            "subject": self.subject,
            "question": self.question_text,
            "options": self.options,
            "correct_answer": self.correct_answer,
            "difficulty": self.difficulty,
            "historical_frequency": self.frequency
        }


class ModelPaper:
    def __init__(self, paper_number: int):
        self.paper_number = paper_number
        self.questions: List[ExamQuestion] = []
        self.creation_date = datetime.now()
        self.total_marks = EXAM_CONFIG["total_marks"]
        self.total_questions = EXAM_CONFIG["total_questions"]
        
    def add_question(self, question: ExamQuestion):
        self.questions.append(question)
        
    def get_answer_key(self) -> Dict[int, str]:
        return {q.qid: q.correct_answer for q in self.questions}
    
    def calculate_statistics(self) -> Dict:
        """Calculate statistics for the model paper"""
        if not self.questions:
            return {}
        
        subjects_count = {}
        difficulty_count = {"Easy": 0, "Medium": 0, "Hard": 0}
        
        for q in self.questions:
            subjects_count[q.subject] = subjects_count.get(q.subject, 0) + 1
            difficulty_count[q.difficulty] = difficulty_count.get(q.difficulty, 0) + 1
        
        return {
            "total_questions": len(self.questions),
            "subjects_distribution": subjects_count,
            "difficulty_distribution": difficulty_count,
            "average_difficulty": sum({"Easy": 1, "Medium": 2, "Hard": 3}.get(d, 0) 
                                      for d in [q.difficulty for q in self.questions]) / len(self.questions)
        }
    
    def to_json(self) -> str:
        return json.dumps({
            "paper_number": self.paper_number,
            "creation_date": self.creation_date.isoformat(),
            "exam_config": EXAM_CONFIG,
            "questions": [q.to_dict() for q in self.questions],
            "statistics": self.calculate_statistics()
        }, indent=2)


class RepeatingPatternAnalyzer:
    """Analyzes and predicts repeating question patterns"""
    
    def __init__(self):
        self.question_frequency = {}
        self.topic_patterns = {}
        self.difficulty_trends = {}
    
    def analyze_pattern(self, questions: List[ExamQuestion]) -> Dict:
        """Analyze question patterns for repeat predictions"""
        patterns = {
            "high_frequency_topics": [],
            "likely_repeating_questions": [],
            "difficulty_prediction": {},
            "confidence_score": 0
        }
        
        # Analyze subject frequencies
        subject_freq = {}
        for q in questions:
            subject_freq[q.subject] = subject_freq.get(q.subject, 0) + q.frequency
        
        patterns["high_frequency_topics"] = sorted(
            subject_freq.items(), key=lambda x: x[1], reverse=True
        )[:3]
        
        # Predict likely repeating questions (high frequency + medium difficulty)
        likely_repeat = [q for q in questions if q.frequency > 0 and q.difficulty != "Hard"]
        patterns["likely_repeating_questions"] = [
            {
                "question": q.question_text,
                "frequency": q.frequency,
                "confidence": min(q.frequency * 20, 95)
            }
            for q in sorted(likely_repeat, key=lambda x: x.frequency, reverse=True)[:10]
        ]
        
        patterns["confidence_score"] = min(len([q for q in questions if q.frequency > 0]) * 10, 85)
        
        return patterns
    
    def generate_prediction_report(self, analysis: Dict) -> str:
        """Generate human-readable prediction report"""
        report = []
        report.append("=" * 80)
        report.append("CCE EXAM PREDICTION ANALYSIS REPORT")
        report.append("=" * 80)
        report.append("")
        
        report.append("HIGH FREQUENCY TOPICS (Most likely to appear):")
        report.append("-" * 80)
        for topic, freq in analysis["high_frequency_topics"]:
            report.append(f"  • {topic}: {freq} occurrences (High Priority)")
        report.append("")
        
        report.append("LIKELY REPEATING QUESTIONS:")
        report.append("-" * 80)
        for idx, item in enumerate(analysis["likely_repeating_questions"][:5], 1):
            report.append(f"{idx}. Q: {item['question'][:80]}...")
            report.append(f"   Confidence: {item['confidence']}% | Frequency: {item['frequency']} times")
        report.append("")
        
        report.append(f"OVERALL PREDICTION CONFIDENCE: {analysis['confidence_score']}%")
        report.append("=" * 80)
        
        return "\n".join(report)


class ModelPaperGenerator:
    """Main generator class for creating model papers"""
    
    def __init__(self):
        self.question_bank = self._initialize_question_bank()
        self.analyzer = RepeatingPatternAnalyzer()
    
    def _initialize_question_bank(self) -> List[ExamQuestion]:
        """Initialize question bank with sample questions"""
        questions = []
        
        # Sample question templates
        reasoning_q = [
            ExamQuestion(1, "Reasoning Ability", 
                        "If SCHOOL is coded as 12345567, then BOOK is coded as?",
                        ["1334", "2338", "2344", "2345"], "2344", "Easy"),
            ExamQuestion(2, "Reasoning Ability",
                        "Find the odd one out: 2, 3, 5, 7, 11, 13, 17, 21",
                        ["7", "13", "17", "21"], "21", "Medium"),
            ExamQuestion(3, "Reasoning Ability",
                        "A is B's brother. B is C's sister. D is C's mother. How is A related to D?",
                        ["Son", "Grandson", "Brother", "Cousin"], "Grandson", "Hard"),
        ]
        
        quant_q = [
            ExamQuestion(4, "Quantitative Aptitude",
                        "What is 15% of 800?",
                        ["120", "100", "80", "110"], "120", "Easy"),
            ExamQuestion(5, "Quantitative Aptitude",
                        "If x² + 2x + 1 = 0, then x = ?",
                        ["-1", "1", "2", "-2"], "-1", "Medium"),
            ExamQuestion(6, "Quantitative Aptitude",
                        "Find the value of 1/2 + 1/3 + 1/4 = ?",
                        ["13/12", "11/12", "15/12", "10/12"], "13/12", "Medium"),
        ]
        
        english_q = [
            ExamQuestion(7, "English Language",
                        "Choose the correct spelling:",
                        ["Accomodate", "Accommodate", "Acommodate", "Accomodit"], 
                        "Accommodate", "Easy"),
            ExamQuestion(8, "English Language",
                        "Fill in the blank: The weather was ____ to cancel the match.",
                        ["too bad", "so bad", "very bad", "bad enough"],
                        "too bad", "Medium"),
            ExamQuestion(9, "English Language",
                        "Identify the error: I have seen him yesterday.",
                        ["have", "seen", "him", "No error"],
                        "have", "Hard"),
        ]
        
        gujarati_q = [
            ExamQuestion(10, "Gujarati Language",
                        "નીચે આપેલ શબ્દમાંથી તમાટ શોધો:",
                        ["આ", "એ", "ઇ", "ઊ"],
                        "આ", "Easy"),
            ExamQuestion(11, "Gujarati Language",
                        "સાચો ગુણાણ પસંદ કરો:",
                        ["પ્રેમ", "પ્રમ", "પ્રેમો", "પ્રામ"],
                        "પ્રેમ", "Medium"),
        ]
        
        questions.extend(reasoning_q)
        questions.extend(quant_q)
        questions.extend(english_q)
        questions.extend(gujarati_q)
        
        return questions
    
    def generate_model_paper(self, paper_num: int, 
                           include_high_freq: bool = True) -> ModelPaper:
        """Generate a complete model paper"""
        paper = ModelPaper(paper_num)
        
        # Select questions from question bank
        selected = random.sample(self.question_bank, min(len(self.question_bank), 
                                                         EXAM_CONFIG["total_questions"]))
        
        for q in selected:
            paper.add_question(q)
        
        return paper
    
    def generate_with_analysis(self, num_papers: int = 3) -> List[Tuple[ModelPaper, Dict]]:
        """Generate multiple papers with pattern analysis"""
        papers_with_analysis = []
        
        for i in range(1, num_papers + 1):
            paper = self.generate_model_paper(i)
            analysis = self.analyzer.analyze_pattern(paper.questions)
            papers_with_analysis.append((paper, analysis))
        
        return papers_with_analysis


def main():
    """Main function to generate exam model papers"""
    print("CCE Gujarat Government Exam - Model Paper Generator")
    print("=" * 80)
    
    generator = ModelPaperGenerator()
    
    # Generate 3 sample model papers
    print("\nGenerating 3 model papers with analysis...\n")
    
    papers_with_analysis = generator.generate_with_analysis(num_papers=3)
    
    for paper, analysis in papers_with_analysis:
        print(f"\n{'=' * 80}")
        print(f"MODEL PAPER {paper.paper_number}")
        print(f"{'=' * 80}")
        print(f"Created: {paper.creation_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Questions: {paper.total_questions}")
        print(f"Total Marks: {paper.total_marks}")
        print(f"Duration: {EXAM_CONFIG['duration_minutes']} minutes")
        
        # Print statistics
        stats = paper.calculate_statistics()
        print(f"\nQuestion Distribution:")
        for subject, count in stats.get("subjects_distribution", {}).items():
            print(f"  • {subject}: {count} questions")
        
        print(f"\nDifficulty Distribution:")
        for diff, count in stats.get("difficulty_distribution", {}).items():
            print(f"  • {diff}: {count} questions")
        
        # Print prediction analysis
        print("\n" + generator.analyzer.generate_prediction_report(analysis))
        
        # Print answer key (first 5 for demo)
        answer_key = paper.get_answer_key()
        print("\nSAMPLE ANSWER KEY (First 10):")
        print("-" * 80)
        for qid, ans in list(answer_key.items())[:10]:
            print(f"Q{qid}: {ans}")
        
        # Save to file
        filename = f"cce_model_paper_{paper.paper_number}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(paper.to_json())
        print(f"\n✓ Paper saved to: {filename}")


if __name__ == "__main__":
    main()
