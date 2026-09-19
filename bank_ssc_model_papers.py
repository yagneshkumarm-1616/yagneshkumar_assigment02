"""Generate exam-oriented prelims papers for SBI Clerk, SSC CGL, and IBPS RRB Clerk.

The blueprints are deliberately separate from the older GSSSB tooling. Questions are
practice questions based on official section structures, syllabus coverage, and
recurring previous-paper topic patterns. They are not claims of exact repetition.
"""

from __future__ import annotations

import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Sequence


ROOT = Path(__file__).resolve().parent
BLUEPRINT_PATH = ROOT / "bank_ssc_exam_blueprints.json"
OUTPUT_DIR = ROOT / "bank_ssc_model_papers"


@dataclass(frozen=True)
class Question:
    number: int
    section: str
    topic: str
    difficulty: str
    prompt: str
    options: List[str]
    answer: str
    explanation: str
    evidence: str = "Syllabus and recurring previous-paper topic"


def q(section: str, topic: str, difficulty: str, prompt: str,
      options: Sequence[str], answer: str, explanation: str) -> Dict:
    return {
        "section": section,
        "topic": topic,
        "difficulty": difficulty,
        "prompt": prompt,
        "options": list(options),
        "answer": answer,
        "explanation": explanation,
    }


def quant_pool(section: str) -> List[Dict]:
    return [
        q(section, "Simplification", "Easy", "25% of 240 + 3/5 of 100 = ?",
          ["100", "120", "140", "160"], "120", "25% of 240 is 60 and 3/5 of 100 is 60; total 120."),
        q(section, "Percentage", "Medium", "A number increased by 20% becomes 360. The original number is:",
          ["280", "300", "320", "340"], "300", "Original = 360/1.20 = 300."),
        q(section, "Profit and Loss", "Medium", "An article bought for Rs. 800 is sold for Rs. 920. Profit percentage is:",
          ["12%", "15%", "18%", "20%"], "15%", "Profit is 120; 120/800 x 100 = 15%."),
        q(section, "Ratio", "Easy", "If A:B = 3:5 and B:C = 10:7, then A:C is:",
          ["3:7", "6:7", "7:6", "5:7"], "6:7", "Make B common: 3:5 = 6:10, hence A:C = 6:7."),
        q(section, "Average", "Easy", "The average of 8, 12, 15, 21 and 24 is:",
          ["14", "16", "18", "20"], "16", "Sum is 80; 80/5 = 16."),
        q(section, "Time and Work", "Medium", "A can finish a task in 12 days and B in 18 days. Together they take:",
          ["6 days", "7 1/5 days", "8 days", "9 days"], "7 1/5 days", "Combined rate is 1/12 + 1/18 = 5/36, so time is 36/5 days."),
        q(section, "Speed, Distance and Time", "Medium", "A train covers 360 km in 4.5 hours. Its speed is:",
          ["72 km/h", "80 km/h", "90 km/h", "96 km/h"], "80 km/h", "Speed = 360/4.5 = 80 km/h."),
        q(section, "Simple Interest", "Medium", "Simple interest on Rs. 5,000 at 8% per annum for 2 years is:",
          ["Rs. 400", "Rs. 600", "Rs. 800", "Rs. 900"], "Rs. 800", "SI = 5000 x 8 x 2 / 100 = 800."),
        q(section, "Number Series", "Medium", "Find the next number: 3, 7, 15, 31, 63, ?",
          ["95", "111", "127", "129"], "127", "Each term is previous term x 2 + 1."),
        q(section, "Data Interpretation", "Medium", "A shop sells 120, 150 and 180 units on three days. The average sale is:",
          ["140", "145", "150", "160"], "150", "Total 450 divided by 3 equals 150."),
        q(section, "Quadratic Equation", "Hard", "The positive root of x^2 - 9x + 20 = 0 is:",
          ["4", "5", "6", "8"], "5", "Factors are (x-4)(x-5); positive roots are 4 and 5, and the requested larger positive root is 5."),
        q(section, "Geometry", "Medium", "The angles of a triangle are in the ratio 2:3:4. The largest angle is:",
          ["60 degrees", "70 degrees", "80 degrees", "90 degrees"], "80 degrees", "Nine parts equal 180 degrees, so one part is 20 and the largest is 80."),
    ]


def reasoning_pool(section: str) -> List[Dict]:
    return [
        q(section, "Syllogism", "Medium", "Statements: All pens are books. Some books are papers. Conclusions: I. Some pens are papers. II. All pens are books.",
          ["Only I follows", "Only II follows", "Both follow", "Neither follows"], "Only II follows", "The first statement directly supports II; overlap of pens and papers is not certain."),
        q(section, "Inequality", "Easy", "If P > Q = R >= S, which is definitely true?",
          ["P < S", "P > S", "Q < S", "R > P"], "P > S", "P is greater than Q and Q is at least S, so P is greater than S."),
        q(section, "Coding-Decoding", "Medium", "If BANK is coded as 2-1-14-11, how is LOAN coded using alphabet positions?",
          ["12-15-1-14", "11-15-1-13", "12-14-1-15", "13-15-2-14"], "12-15-1-14", "Use the alphabet position of each letter."),
        q(section, "Blood Relation", "Easy", "Ravi says, 'She is the daughter of the only son of my grandfather.' The woman is Ravi's:",
          ["Sister", "Mother", "Daughter", "Aunt"], "Sister", "The only son of Ravi's grandfather is Ravi's father; his daughter is Ravi's sister."),
        q(section, "Direction Sense", "Easy", "A person walks 5 km north, then 3 km east, then 5 km south. He is now:",
          ["3 km east of start", "3 km west of start", "5 km south", "8 km east"], "3 km east of start", "North and south movements cancel."),
        q(section, "Series", "Medium", "Find the missing term: B, E, I, N, T, ?",
          ["Y", "Z", "A", "C"], "A", "Letter jumps are +3, +4, +5, +6, then +7 with cyclic alphabet, giving A."),
        q(section, "Order and Ranking", "Easy", "In a class of 40, Meena is 12th from the top. Her rank from the bottom is:",
          ["27th", "28th", "29th", "30th"], "29th", "Bottom rank = 40 - 12 + 1 = 29."),
        q(section, "Seating Arrangement", "Hard", "Five people P, Q, R, S and T sit in a row. P is left of Q, R is right of Q, and S is between P and Q. Who is in the middle?",
          ["P", "Q", "R", "S"], "S", "The order is P-S-Q-R with T at an end; S occupies the central position among the constrained four."),
        q(section, "Analogy", "Easy", "Book : Read :: Food : ?",
          ["Cook", "Eat", "Serve", "Buy"], "Eat", "A book is read; food is eaten."),
        q(section, "Alphabet Test", "Easy", "How many letters are between the 5th letter from the left and the 8th letter from the right?",
          ["12", "13", "14", "15"], "13", "The 8th from right is S; between E and S are 13 letters."),
    ]


def english_pool(section: str) -> List[Dict]:
    return [
        q(section, "Error Spotting", "Easy", "Choose the incorrect part: 'Neither of the answers are correct.'",
          ["Neither", "of the answers", "are", "correct"], "are", "Neither takes a singular verb: 'is'."),
        q(section, "Fillers", "Easy", "The manager insisted ___ punctuality.",
          ["in", "on", "at", "for"], "on", "The correct collocation is 'insisted on'."),
        q(section, "Tenses", "Easy", "By this time tomorrow, she ___ the report.",
          ["completes", "completed", "will have completed", "has completed"], "will have completed", "Future perfect describes an action completed before a future time."),
        q(section, "Active and Passive Voice", "Medium", "Change to passive: 'The committee approved the proposal.'",
          ["The proposal was approved by the committee.", "The proposal is approved by the committee.", "The committee was approved by the proposal.", "The proposal approved the committee."],
          "The proposal was approved by the committee.", "Simple past active changes to was/were + past participle."),
        q(section, "Direct and Indirect Speech", "Medium", "Change to indirect speech: He said, 'I am busy.'",
          ["He said that I am busy.", "He said that he was busy.", "He says he was busy.", "He said he is busy."],
          "He said that he was busy.", "Backshift am to was and change the pronoun I to he."),
        q(section, "Vocabulary", "Easy", "Choose the synonym of 'abundant'.",
          ["scarce", "plentiful", "fragile", "brief"], "plentiful", "Abundant means available in large quantity."),
        q(section, "Vocabulary", "Easy", "Choose the antonym of 'ancient'.",
          ["old", "historic", "modern", "early"], "modern", "Modern is the opposite of ancient."),
        q(section, "Cloze and Usage", "Medium", "The evidence was too weak ___ support the claim.",
          ["for", "to", "with", "by"], "to", "The construction is 'too + adjective + to + verb'."),
        q(section, "Sentence Improvement", "Medium", "Improve: 'She is senior than me.'",
          ["senior to me", "senior from me", "more senior than me", "no improvement"], "senior to me", "Senior is followed by 'to', not 'than'."),
        q(section, "Reading Comprehension", "Medium", "A passage states that regular revision improves retention. The central idea is:",
          ["Revision is unnecessary.", "Revision supports memory.", "Only long study sessions work.", "Memory cannot improve."],
          "Revision supports memory.", "The statement directly supports the benefit of revision."),
    ]


def ga_pool() -> List[Dict]:
    return [
        q("General Awareness", "Indian Polity", "Easy", "Which Article of the Constitution deals with equality before law?",
          ["Article 12", "Article 14", "Article 19", "Article 21"], "Article 14", "Article 14 guarantees equality before law and equal protection of laws."),
        q("General Awareness", "Economy", "Medium", "Repo rate is the rate at which:",
          ["banks lend to customers", "RBI lends to banks", "banks lend to RBI", "government lends to RBI"], "RBI lends to banks", "Repo is the policy rate for RBI lending to commercial banks."),
        q("General Awareness", "History", "Easy", "The Quit India Movement was launched in:",
          ["1930", "1942", "1947", "1950"], "1942", "The movement began in August 1942."),
        q("General Awareness", "Geography", "Easy", "The Tropic of Cancer passes through how many Indian states?",
          ["6", "7", "8", "9"], "8", "It passes through eight Indian states."),
        q("General Awareness", "General Science", "Easy", "The SI unit of electric current is:",
          ["volt", "watt", "ampere", "ohm"], "ampere", "Ampere is the SI unit of current."),
        q("General Awareness", "Banking Awareness", "Medium", "KYC in banking primarily means:",
          ["Keep Your Cash", "Know Your Customer", "Key Yield Calculation", "Know Your Credit"], "Know Your Customer", "KYC verifies the identity and address of a customer."),
        q("General Awareness", "Computer Awareness", "Easy", "Which memory is non-volatile?",
          ["RAM", "Cache", "ROM", "Register"], "ROM", "ROM retains data when power is removed."),
        q("General Awareness", "Static GK", "Easy", "The headquarters of the Reserve Bank of India is in:",
          ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "Mumbai", "RBI headquarters is in Mumbai."),
        q("General Awareness", "Current Affairs Method", "Medium", "For a current-affairs question, the most reliable preparation source is:",
          ["unverified social post", "official release and reputable news", "random guess", "old memory only"],
          "official release and reputable news", "Current facts should be checked against authoritative sources."),
        q("General Awareness", "Financial Awareness", "Medium", "NPA in banking refers to:",
          ["Net Profit Account", "Non-Performing Asset", "New Payment Application", "National Pension Account"],
          "Non-Performing Asset", "An NPA is a loan asset that stops generating income under regulatory rules."),
    ]


def choose_pool(section: str, exam_key: str) -> List[Dict]:
    if section in {"Numerical Ability", "Quantitative Aptitude"}:
        return quant_pool(section)
    if section in {"Reasoning Ability", "Reasoning", "General Intelligence & Reasoning", "Reasoning Ability & Computer Aptitude"}:
        return reasoning_pool(section)
    if section in {"English Language", "General English", "English Comprehension", "English/Hindi Language"}:
        return english_pool(section)
    return ga_pool()


def make_questions(exam_key: str, section: Dict, paper_index: int, start_number: int) -> List[Question]:
    pool = choose_pool(section["name"], exam_key)
    count = section["questions"]
    rng = random.Random(f"{exam_key}:{paper_index}:{section['name']}")
    items = [pool[(i + paper_index * 3) % len(pool)] for i in range(count)]
    rng.shuffle(items)
    return [
        Question(
            number=start_number + i,
            section=item["section"],
            topic=item["topic"],
            difficulty=item["difficulty"],
            prompt=item["prompt"],
            options=item["options"],
            answer=item["answer"],
            explanation=item["explanation"],
        )
        for i, item in enumerate(items)
    ]


def build_paper(exam_key: str, blueprint: Dict, paper_index: int) -> Dict:
    questions: List[Question] = []
    next_number = 1
    for section in blueprint["pattern"]["sections"]:
        generated = make_questions(exam_key, section, paper_index, next_number)
        questions.extend(generated)
        next_number += len(generated)
    return {
        "exam": blueprint["name"],
        "exam_key": exam_key,
        "stage": blueprint["model_stage"],
        "paper_number": paper_index,
        "pattern": blueprint["pattern"],
        "questions": [asdict(item) for item in questions],
        "analysis_note": "Topic weighting follows the official syllabus and recurring previous-paper patterns; it is not a prediction of exact questions.",
    }


def write_text(paper: Dict) -> str:
    lines = [
        f"{paper['exam']} - {paper['stage']} MODEL PAPER {paper['paper_number']}",
        "=" * 84,
        f"Questions: {paper['pattern']['total_questions']} | Marks: {paper['pattern']['total_marks']} | Time: {paper['pattern']['minutes']} minutes",
        f"Negative marking: -{paper['pattern']['negative_mark']} per wrong answer",
        "Use the official notification for the final pattern before the exam.",
        "",
    ]
    for question in paper["questions"]:
        lines.append(f"Q{question['number']}. [{question['section']} | {question['topic']} | {question['difficulty']}]")
        lines.append(question["prompt"])
        for index, option in enumerate(question["options"]):
            lines.append(f"  {chr(65 + index)}) {option}")
        lines.append("")
    lines.append("ANSWER KEY")
    lines.append("-" * 84)
    lines.extend(f"Q{q['number']}: {q['answer']}" for q in paper["questions"])
    lines.append("")
    lines.append("SOLUTIONS")
    lines.append("-" * 84)
    for question in paper["questions"]:
        lines.append(f"Q{question['number']}: {question['answer']} - {question['explanation']}")
    return "\n".join(lines)


def generate_all(output_dir: Path = OUTPUT_DIR, papers_per_exam: int = 10) -> None:
    blueprints = json.loads(BLUEPRINT_PATH.read_text(encoding="utf-8"))
    output_dir.mkdir(exist_ok=True)
    for exam_key, blueprint in blueprints["exams"].items():
        exam_dir = output_dir / exam_key
        exam_dir.mkdir(exist_ok=True)
        for paper_index in range(1, papers_per_exam + 1):
            paper = build_paper(exam_key, blueprint, paper_index)
            (exam_dir / f"paper_{paper_index:02d}.json").write_text(
                json.dumps(paper, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            (exam_dir / f"paper_{paper_index:02d}.txt").write_text(
                write_text(paper), encoding="utf-8"
            )


def main() -> None:
    generate_all()
    print("Generated 10 dedicated prelims model papers for each of:")
    print("- SBI Clerk")
    print("- SSC CGL")
    print("- IBPS RRB Office Assistant (Clerk)")
    print(f"Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
