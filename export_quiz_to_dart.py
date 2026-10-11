# -*- coding: utf-8 -*-
import json

with open('public/data/nestedQuizBank.json', 'r', encoding='utf-8') as f:
    nested = json.load(f)

# Extract defaultQuizBank from existing quiz_bank.dart
with open('lib/features/class/quiz_bank.dart', 'r', encoding='utf-8') as f:
    content = f.read()

default_part = content[content.find('final Map<String, List<Map<String, dynamic>>> defaultQuizBank ='):]

def escape_str(s):
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('$', '\\$').replace('\n', ' ')

out = []
out.append("final Map<String, Map<String, Map<String, List<Map<String, dynamic>>>>>\n nestedQuizBank = {\n")

for cls_name, subjects in nested.items():
    out.append(f"  '{cls_name}': {{\n")
    for subj_name, lessons in subjects.items():
        out.append(f"    '{subj_name}': {{\n")
        for lesson_name, questions in lessons.items():
            safe_lesson = escape_str(lesson_name)
            out.append(f"      '{safe_lesson}': [\n")
            for q in questions:
                out.append("        {\n")
                out.append(f"          'id': {q['id']},\n")
                safe_q = escape_str(q['question'])
                out.append(f"          'question': '{safe_q}',\n")
                options_str = ", ".join(f"'{escape_str(opt)}'" for opt in q['options'])
                out.append(f"          'options': [{options_str}],\n")
                out.append(f"          'answer': {q['answer']},\n")
                out.append("        },\n")
            out.append("      ],\n")
        out.append("    },\n")
    out.append("  },\n")

out.append("};\n\n")
out.append(default_part)

with open('lib/features/class/quiz_bank.dart', 'w', encoding='utf-8') as f:
    f.write("".join(out))

print("Successfully exported all 6 classes to lib/features/class/quiz_bank.dart!")
