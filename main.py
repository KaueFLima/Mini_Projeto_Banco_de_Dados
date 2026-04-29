from sqlalchemy import text
from db import engine
from atividade1 import LGPD
from atividade2 import atividade2
from atividade3 import atividade3

print("=" * 55)

print("\nAtividade 1 — Anonimização (primeiros 5 registros):")
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM usuarios LIMIT 5;"))
    for row in result:
        print(LGPD(row))

print("\nAtividade 2 — Arquivos por ano de nascimento:")
atividade2()

print("\nAtividade 3 — todos.xlsx (sem anonimização):")
atividade3()

print("\nConcluído. Log gravado em lgpd_log.txt")
print("=" * 55)
