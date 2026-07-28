from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Hokai MCP", stateless_http=True, json_response=True)

@mcp.tool()
def get_tools_tree() -> dict:
    """
    Fetch Hokai tools-tree JSON.
    """
    r = requests.get("https://hokai.io/api/tools-tree", timeout=30)
    r.raise_for_status()
    return {"status": "ok", "data": r.json()}

@mcp.tool()
def scanner_status() -> dict:
    """
    Simple health check for the MCP server.
    """
    return {"status": "ok", "message": "MCP server running"}

if __name__ == "__main__":
    # Streamable HTTP transport for remote MCP
    mcp.run(transport="streamable-http")
