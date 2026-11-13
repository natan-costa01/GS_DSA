from dataclasses import dataclass

@dataclass
class Servico:
    id: int
    titulo: str
    categoria: str
    descricao: str
    requisitos: str
    local: str
