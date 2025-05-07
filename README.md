# 📚 Wiki MCP Server

An MCP (Model Context Protocol) Server implementation for managing Confluence wiki pages.

Supports:
- Creating new wiki pages
- Updating existing wiki pages
- Deleting wiki pages
- Searching wiki pages by keyword
- Auto-selecting correct Confluence knowledge base (`alm`, `wpb`, etc.) based on user query

Built with **FastAPI**, following **MCP Server Best Practices**, and ready for production deployment.

---

## 🚀 Tech Stack

- Python 3.10+
- FastAPI
- MCP SDK
- Requests (for Confluence API interaction)
- ContextVars (for session management)

---

## 📦 Project Structure

```plaintext
wiki_mcp_server/
├── src/wiki_mcp_server/
│   ├── server.py          # MCP server entry point
│   ├── service.py         # Business logic (Confluence API interactions)
│   ├── tools.py           # MCP tool definitions
│   ├── prompts.py         # MCP prompt definitions
│   ├── resources.py       # MCP resource definitions
│   ├── utils.py           # Helper functions (wiki_type inference etc.)
│   ├── utils/session_context.py  # Session context manager
│   └── middleware.py      # Authentication and session initialization middleware
├── Dockerfile             # Container configuration
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── smithery.yaml          # Smithery integration config (optional)
└── pyproject.toml         # Python project metadata
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://your-repo-url/wiki_mcp_server.git
cd wiki_mcp_server
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Configure your environment variables if needed.

---

## 🛠 Running Locally

Run the server:

```bash
cd src
uvicorn wiki_mcp_server.server:app --host 0.0.0.0 --port 9999 --reload
```

After startup, you can visit:

- OpenAPI docs (Swagger UI): [http://localhost:9999/docs](http://localhost:9999/docs)
- ReDoc docs: [http://localhost:9999/redoc](http://localhost:9999/redoc)

---

## 🧪 Example Request

### Headers Required:

| Key | Example Value |
|:---|:---|
| user_name | john.doe@domain.com |
| alm_confluence_base_url | https://your-confluence-site/wiki/rest/api |
| alm_confluence_api_token | your-api-token |
| wpb_confluence_base_url | (optional if available) |
| wpb_confluence_api_token | (optional if available) |

> ⚠️ If headers are missing or invalid, server will return HTTP 400 error.

---

### Example: Create Page

**POST** `/create_page`

```json
{
  "space_key": "TEST",
  "title": "Test Page Created by MCP Server",
  "content": "<p>Hello, World!</p>",
  "user_query": "Please create a page in GSNA knowledge base."
}
```

**Behavior**:
- Server will infer `wiki_type=alm` from user_query.
- Create the page in Confluence and return page metadata.

---

## 🧠 Auto Inference Logic

- If the query mentions `gsna`, `global`, `alm-confluence` → **alm**
- If the query mentions `wpb`, `wealth` → **wpb**
- Otherwise default to **alm**

(You can also manually specify `wiki_type` in input)

---

## 🐳 Docker (Optional)

Build and run containerized server:

```bash
docker build -t wiki-mcp-server .
docker run -d -p 9999:9999 --name wiki-mcp-server wiki-mcp-server
```

---

## 📜 License

MIT License.

---

## 📞 Contact

For issues or collaboration requests, please contact:

- Developer: **Shawn**
- Email: gsqasxb@gmail.com
- Project maintained by internal MCP Working Group

---# wiki_mcp_server
