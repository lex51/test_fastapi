# test_fastapi


link to doc
http://fastapi.localhost:8008/docs or
http://fastapi.localhost:8008/redoc

link to traefik
http://fastapi.localhost:8081/dashboard/#/


small test
curl -s fastapi.localhost:8008/ping | jq
```json
{
  "ping": "pong!"
}
```

## content of .env in root_dir
```json
COMPOSE_FILE=base.yml

```
