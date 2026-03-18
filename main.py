#importa o fastapi e o HTTPException para lidar com erros
from fastapi import FastAPI, HTTPException

#define o formato dos dados de entrada
from pydantic import BaseModel

#ajudar na tipagem de dados
from typing import List, Optional

app = FastAPI(
    title="API de Gerenciamento de Tarefas",
    description="Uma API simples para gerenciar tarefas, permitindo criar, ler, atualizar e excluir tarefas.",
    version="1.0.0"
)

class Tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    concluida: bool = False

#banco em memoria
db_tarefas = []