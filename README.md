# TareFaz

#### Sistema de gerenciamento de tarefas

# API Doc

## Login:

**POST** /api/v1/auth/login/

```json
{
  "username": "usuario",
  "password": "senha"
}
```

#### Response

```json
{
  "token": "token"
}
```

## Tarefas:

### Lista as tarefas cadastradas

**GET** /api/v1/tarefas/

```json
[
  {
    "id": 9,
    "descricao": "Altera tarefa do Fábio",
    "feita": true,
    "data_add": "2021-01-30T21:50:45.301097-03:00",
    "usuario": 2
  },
  {
    "id": 10,
    "descrição": "Tarefa 2",
    "feita": true,
    "data_add": "2020-01-01T12:00:00",
    "usuario": 2
  }
]
```

### Cria uma nova tarefa

**POST** /api/v1/tarefas/

```json
{
  "descrição": "Task Test",
  "usuario": "user_id"
}
```

### Recupera uma tarefa pelo ID

**GET** /api/v1/tarefas/{id}/

```json
{
  "id": 9,
  "descricao": "Altera tarefa do Fábio",
  "feita": true,
  "data_add": "2021-01-30T21:50:45.301097-03:00",
  "usuario": 2
}
```

### Atualiza uma tarefa pelo ID

**PUT** /api/v1/tarefas/{id}/

```json
{
  "descrição": "Atualiza tarefa",
  "feita": true,
  "usuario": "usuario_id"
}
```

### Remove uma tarefa

**DELETE** /api/v1/tarefas/{id}/
