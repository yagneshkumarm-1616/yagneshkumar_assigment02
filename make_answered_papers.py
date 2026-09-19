"""Create question-by-question answer versions from generated JSON papers."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent / "bank_ssc_model_papers"


def render(paper):
    pattern = paper["pattern"]
    lines = [
        f"{paper['exam']} - {paper['stage']} MODEL PAPER {paper['paper_number']} (ANSWERED)",
        "=" * 88,
        f"Questions: {pattern['total_questions']} | Marks: {pattern['total_marks']} | "
        f"Time: {pattern['minutes']} minutes",
        f"Negative marking: -{pattern['negative_mark']} per wrong answer",
        "Each question is followed by its answer and explanation.",
        "",
    ]
    for item in paper["questions"]:
        lines.append(
            f"Q{item['number']}. [{item['section']} | {item['topic']} | {item['difficulty']}]"
        )
        lines.append(item["prompt"])
        for index, option in enumerate(item["options"]):
            marker = " [CORRECT]" if option == item["answer"] else ""
            lines.append(f"  {chr(65 + index)}) {option}{marker}")
        lines.append(f"Answer: {item['answer']}")
        lines.append(f"Explanation: {item['explanation']}")
        lines.append("-" * 88)
    return "\n".join(lines) + "\n"


def main():
    generated = 0
    for json_path in sorted(ROOT.glob("*/*.json")):
        paper = json.loads(json_path.read_text(encoding="utf-8"))
        output_path = json_path.with_name(json_path.stem + "_answered.txt")
        output_path.write_text(render(paper), encoding="utf-8")
        generated += 1
    print(f"Created {generated} question-by-question answered papers.")


if __name__ == "__main__":
    main()
