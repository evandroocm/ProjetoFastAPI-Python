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

#rota para listar tarefas
@app.get("/tarefas", response_model=List[Tarefa])
async def listar_tarefas():
    return db_tarefas

#rota para criar tarefa
@app.post("/tarefas", response_model=Tarefa, status_code=201)
async def criar_tarefa(tarefa: Tarefa):
    tarefa.id = len(db_tarefas) + 1
    db_tarefas.append(tarefa)
    return tarefa

#buscar tarefa por id
@app.get("/tarefas/{tarefa_id}", response_model=Tarefa)
async def obter_tarefa(tarefa_id: int):
    for t in db_tarefas:
        if t.id == tarefa_id:
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

#rota para alterar tarefa
@app.put("/tarefas/{tarefa_id}", response_model=Tarefa)
async def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa):
    for index, t in enumerate(db_tarefas):
        if t.id == tarefa_id:
            tarefa_atualizada.id = tarefa_id
            db_tarefas[index] = tarefa_atualizada
            return tarefa_atualizada
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

#rota para deletar tarefa
@app.delete("/tarefas/{tarefa_id}", status_code=204)
async def deletar_tarefa(tarefa_id: int):
    for t in db_tarefas:
        if t.id == tarefa_id:
            db_tarefas.remove(t)
            return
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")