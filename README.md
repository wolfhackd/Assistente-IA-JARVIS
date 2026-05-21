# 🤖 Assistente IA - JARVIS

Um assistente de inteligência artificial multimodal que integra reconhecimento de voz, processamento de linguagem natural e síntese de voz para criar uma experiência conversacional completa.

## 🌟 Características

- **🎤 Reconhecimento de Voz (STT)** - Converte áudio em texto usando Google Speech Recognition
- **🧠 Processamento de Linguagem Natural (NLT)** - Gera respostas inteligentes usando Google Gemini 3.5 Flash
- **🔊 Síntese de Voz (TTS)** - Converte texto em fala usando PyTTSx3
- **🇧🇷 Suporte em Português Brasileiro** - Interface totalmente em português

## 📋 Pré-requisitos

- Python 3.8+
- Microfone conectado ao computador
- Chave de API do Google Gemini
- Conexão com a internet

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/wolfhackd/Assistente-IA-JARVIS.git
cd Assistente-IA-JARVIS
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv

# No Windows:
venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GOOGLE_API_KEY=sua_chave_de_api_aqui
```

> 📌 **Como obter a chave de API:** Acesse [Google AI Studio](https://aistudio.google.com/app/apikey) e gere uma nova chave de API.

## 📦 Dependências

| Pacote | Versão | Propósito |
|--------|--------|----------|
| `google-genai` | - | API do Google Gemini |
| `SpeechRecognition` | - | Reconhecimento de voz |
| `pyttsx3` | - | Síntese de voz |
| `python-dotenv` | - | Gerenciamento de variáveis de ambiente |

## 💻 Uso

### Execução Padrão

```bash
python main.py
```

O programa irá:
1. Aguardar por entrada de voz
2. Reconhecer o texto dito
3. Processar com IA Gemini
4. Reproduzir a resposta em voz

### Teste Individual de Componentes

#### Testar STT (Fala → Texto)

```bash
python testes.py
```

#### Testar TTS (Texto → Fala)

```bash
python -c "from src.engine.tts import TTS; t = TTS(); t.speak('Olá, mundo!')"
```

## 🏗️ Estrutura do Projeto

```
Assistente-IA-JARVIS/
├── main.py                 # Ponto de entrada principal
├── testes.py              # Scripts de teste
├── .env                   # Variáveis de ambiente (não versionado)
├── .gitignore             # Arquivos ignorados pelo Git
├── README.md              # Este arquivo
│
├── config/                # Configurações do projeto
│   └── __init__.py
│
├── src/                   # Código-fonte
│   ├── __init__.py
│   ├── engine/            # Motores principais
│   │   ├── __init__.py
│   │   ├── nlt.py         # Natural Language (Gemini)
│   │   ├── stt.py         # Speech to Text
│   │   └── tts.py         # Text to Speech
│   │
│   └── skills/            # Habilidades customizáveis
│       └── __init__.py
│
├── tests/                 # Testes automatizados
└── venv/                  # Ambiente virtual
```

## 🔧 Componentes Principais

### STT (Speech to Text)
Converte áudio do microfone em texto usando Google Speech Recognition.

```python
from src.engine.stt import STT

stt = STT()
audio = stt.listen()
texto = stt.recognize(audio)
print(texto)
```

### NLT (Natural Language)
Processa texto com a API Gemini para gerar respostas inteligentes.

```python
from src.engine.nlt import NLT
import os

nlt = NLT(api_key=os.getenv("GOOGLE_API_KEY"))
resposta = nlt.generate_text("Olá, como você está?")
print(resposta)
```

### TTS (Text to Speech)
Converte texto em fala sintetizada.

```python
from src.engine.tts import TTS

tts = TTS()
tts.speak("Olá, tudo bem?")
```

## 🎯 Fluxo de Funcionamento

```
┌─────────────┐
│  Usuário    │
│   Fala      │
└──────┬──────┘
       │
       ▼
┌──────────────┐
│ STT Engine   │  Reconhecer fala
│ (Microfone)  │
└──────┬───────┘
       │ Texto
       ▼
┌──────────────┐
│ NLT Engine   │  Processar com IA
│ (Gemini)     │
└──────┬───────┘
       │ Resposta
       ▼
┌──────────────┐
│ TTS Engine   │  Sintetizar voz
│ (pyttsx3)    │
└──────┬───────┘
       │
       ▼
┌─────────────┐
│  Usuário    │
│   Ouve      │
└─────────────┘
```

## 🐛 Troubleshooting

| Problema | Solução |
|----------|---------|
| "Could not request results" | Verifique sua conexão com a internet |
| Microfone não detectado | Verifique se o microfone está conectado e ativo |
| Erro de API Key | Confirme que a chave está corretamente definida no `.env` |
| Voz "robótica" | É um comportamento normal do pyttsx3; melhorias futuras estão planejadas |

## 📝 Próximas Melhorias

- [ ] Melhorar qualidade da síntese de voz
- [ ] Adicionar suporte a mais idiomas
- [ ] Implementar sistema de skills customizáveis
- [ ] Adicionar logging detalhado
- [ ] Criar testes automatizados
- [ ] Suporte a diferentes modelos de IA

## 📄 Licença

Este projeto é mantido por [wolfhackd](https://github.com/wolfhackd).

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor, abra uma issue ou pull request.

## 📞 Contato

- GitHub: [@wolfhackd](https://github.com/wolfhackd)
- Repositório: [Assistente-IA-JARVIS](https://github.com/wolfhackd/Assistente-IA-JARVIS)

---

**Desenvolvido com ❤️ usando Python e IA**
