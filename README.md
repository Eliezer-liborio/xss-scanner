# XSS Scanner v2

Ferramenta avançada para detecção de vulnerabilidades Cross-Site Scripting (XSS) com multithreading e lista de payloads customizável.

## 🌟 Features

- Teste massivo de payloads XSS pré-definidos
- Paralelismo com ThreadPoolExecutor (até 20 threads)
- Barra de progresso visual com tqdm
- Suporte opcional a proxy Tor
- Detecção baseada em regex para múltiplos padrões XSS
- Geração de relatório automático
- Configuração modular via variáveis

## 🛠️ Tecnologias

- Python 3
- Bibliotecas:
  - `requests` (requisições HTTP)
  - `concurrent.futures` (paralelismo)
  - `tqdm` (barra de progresso)
  - `re` (detecção por regex)

## ⚙️ Instalação

```bash
pip install requests tqdm


🚀 Uso Básico
Configure a URL alvo e caminho do payload no script

Execute:

bash
python3 xssv2.py


⚡ Exemplo de Saída
Executando ataque XSS: 100%|████████████| 6613/6613 [02:46<00:00, 39.81it/s]
✅ Ataque finalizado em 166.23s. 12 payloads positivos. Resultados em 'xss_report.txt'


📂 Estrutura do Projeto
/xss-scanner/
├── xssv2.py                # Script principal
├── xss_report.txt          # Relatório de vulnerabilidades
├── payloads/               # Diretório de payloads
│   └── xss-payload-list.txt # Lista de payloads
└── README.md               # Documentação
