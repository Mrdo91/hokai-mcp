# HokAI MCP Server

An [MCP](https://modelcontextprotocol.io) server that exposes the
[HokAI](https://hokai.io) catalogue of AI tools, agents, models, companies and
infrastructure services to any MCP-compatible client.

Listed in the official MCP Registry as **`io.hokai/hokai`**.

## Hosted endpoint (no install)

The server is hosted, so you do not need to run anything locally:

```
https://hokai.io/mcp
```

Transport: Streamable HTTP. No authentication required — the catalogue is public.

### Claude Desktop / Claude Code

```json
{
  "mcpServers": {
    "hokai": {
      "type": "http",
      "url": "https://hokai.io/mcp"
    }
  }
}
```

## Tools

| Tool | Description |
|---|---|
| `get_tools_tree` | Returns the full HokAI catalogue tree — AI tools, agents, models, companies and services, with categories. |
| `get_listing_info` | How an AI product gets listed on HokAI: today's one-time price, what a listing includes, and the free badge route. |
| `submit_listing` | Starts a listing for an AI tool, model, agent, MCP server or service. Returns a payment link that a person completes; nothing is charged by the call. Submissions are reviewed by a person, and paying never affects rankings. |
| `scanner_status` | Health check. Returns `ok` when the server is running. |

## Run it yourself

```bash
pip install "mcp[cli]" requests
python server.py
```

Serves Streamable HTTP on `127.0.0.1:8000/mcp`.

## About HokAI

[HokAI](https://hokai.io) is an AI tool discovery platform. It catalogues AI tools,
agents, models, companies and infrastructure providers with structured pricing,
capability and comparison data — and Smart Match, which recommends tools from a
plain-language description of what you are trying to do.

## License

MIT
