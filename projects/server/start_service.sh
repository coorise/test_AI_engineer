curl  -X POST http://localhost:8000/api/chat  -H "Authorization: Bearer 1234" -H "Content-Type: application/json" -d '{
  "model": "auto",
  "messages": [
    {"role": "user", "content": "Quels sont les avantages Ollama ?"}
  ]
}'