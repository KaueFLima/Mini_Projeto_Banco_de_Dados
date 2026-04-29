from sqlalchemy import text
from decorator_tempo import medir_tempo
from db import engine

def anonimizar_nome(nome: str) -> str:
    partes = nome.split()
    return ' '.join(
        p[0] + '*' * (len(p) - 1) if len(p) > 1 else p
        for p in partes
    )

def anonimizar_cpf(cpf: str) -> str:
    return f"{cpf[:3]}.***.***-**"

def anonimizar_email(email: str) -> str:
    if '@' in email:
        local, dominio = email.split('@', 1)
        return local[0] + '*' * (len(local) - 1) + '@' + dominio
    return email

def anonimizar_telefone(telefone: str) -> str:
    digitos = ''.join(filter(str.isdigit, telefone))
    return digitos[-4:] if len(digitos) >= 4 else digitos


@medir_tempo
def LGPD(row) -> dict:
    d = dict(row._mapping)
    d['nome']     = anonimizar_nome(d['nome'])
    d['cpf']      = anonimizar_cpf(d['cpf'])
    d['email']    = anonimizar_email(d['email'])
    d['telefone'] = anonimizar_telefone(d['telefone'])
    return d

if __name__ == '__main__':
    print("Atividade 1 — Anonimização (primeiros 5 registros):\n")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM usuarios LIMIT 5;"))
        for row in result:
            user = LGPD(row)
            print(user)
