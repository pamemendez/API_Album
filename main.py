from fastapi import FastAPI, HTTPException, status, Depends
from typing import Optional, Any
from model import AlbumLanaDelRey

app = FastAPI(title="API de Álbuns da Lana Del Rey", version="1.0.0", description="Albuns da cantora Lana Del Rey")

albuns_lana_del_rey = {
    1: {
        "nome": "Born to Die",
        "ano_lancamento": 2012,
        "capa_url": "https://upload.wikimedia.org/wikipedia/pt/thumb/d/d0/Lana_Del_Rey_-_Born_to_Die.png/220px-Lana_Del_Rey_-_Born_to_Die.png",
        "descricao": "Primeiro álbum de estúdio de Lana Del Rey."
    },
    2: {
        "nome": "Ultraviolence",
        "ano_lancamento": 2014,
        "capa_url": "https://upload.wikimedia.org/wikipedia/pt/thumb/5/59/Lana_Del_Rey_-_Ultraviolence.png/220px-Lana_Del_Rey_-_Ultraviolence.png",
        "descricao": "Álbum que explora temas de amor tóxico e violência."
    },
    3: {
        "nome": "Lust for Life",
        "ano_lancamento": 2017,
        "capa_url": "https://upload.wikimedia.org/wikipedia/pt/thumb/3/33/Lana_Del_Rey_-_Lust_for_Life.png/220px-Lana_Del_Rey_-_Lust_for_Life.png",
        "descricao": "Álbum que reflete uma sonoridade mais otimista e colaborativa."
    },
     4: {
        "nome": "Norman Fucking Rockwell!",
        "ano_lancamento": 2019,
        "capa_url": "https://upload.wikimedia.org/wikipedia/pt/thumb/1/17/Lana_Del_Rey_-_Norman_Fucking_Rockwell.png/220px-Lana_Del_Rey_-_Norman_Fucking_Rockwell.png",
        "descricao": "Álbum aclamado pela crítica, com letras introspectivas e emotivas."
    },
    5: {
        "nome": "Chemtrails over the Country Club",
        "ano_lancamento": 2021,
        "capa_url": "https://upload.wikimedia.org/wikipedia/pt/thumb/2/2b/Chemtrails_Over_the_Country_Club_-_Lana_del_Rey.png/220px-Chemtrails_Over_the_Country_Club_-_Lana_del_Rey.png",
        "descricao": "Álbum introspectivo que combina temas de nostalgia com uma produção mais suave."
    },
}

def fake_db():
    try:
        print("Conectando com o banco de dados...")
    finally:
        print("Fechando a conexão com o banco de dados...")

@app.get("/albuns", description="Retorna todos os álbuns da Lana Del Rey")
async def get_albuns(db: Any = Depends(fake_db)):
    return albuns_lana_del_rey

@app.get("/albuns/{album_id}", description="Retorna detalhes de um álbum específico")
async def get_album(album_id: int):
    try:
        album = albuns_lana_del_rey[album_id]
        return album
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Álbum não encontrado")

@app.post("/albuns", status_code=status.HTTP_201_CREATED, description="Adiciona um novo álbum")
async def post_album(album: AlbumLanaDelRey):
    next_id = len(albuns_lana_del_rey) + 1
    albuns_lana_del_rey[next_id] = album.dict()
    albuns_lana_del_rey[next_id].pop("id", None)
    return albuns_lana_del_rey[next_id]

@app.put("/albuns/{album_id}", status_code=status.HTTP_202_ACCEPTED, description="Atualiza um álbum existente")
async def put_album(album_id: int, album: AlbumLanaDelRey):
    if album_id in albuns_lana_del_rey:
        albuns_lana_del_rey[album_id] = album.dict()
        return albuns_lana_del_rey[album_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Álbum com ID {album_id} não encontrado")

@app.delete("/albuns/{album_id}", status_code=status.HTTP_204_NO_CONTENT, description="Deleta um álbum")
async def delete_album(album_id: int):
    if album_id in albuns_lana_del_rey:
        del albuns_lana_del_rey[album_id]
        return {"message": "Álbum deletado com sucesso!"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Álbum com ID {album_id} não encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
