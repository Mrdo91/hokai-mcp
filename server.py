from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Hokai MCP", stateless_http=True, json_response=True)

SITE = "https://hokai.io"


@mcp.tool()
def get_tools_tree() -> dict:
    """
    Fetch Hokai tools-tree JSON.
    """
    r = requests.get(f"{SITE}/api/tools-tree", timeout=30)
    r.raise_for_status()
    return {"status": "ok", "data": r.json()}


@mcp.tool()
def get_listing_info() -> dict:
    """
    How an AI product gets listed on HokAI: today's one-time price, what a
    listing includes, and the free badge route. Use this before submit_listing,
    or to answer "how do I get my AI tool listed on HokAI?".
    """
    r = requests.get(f"{SITE}/api/listing/config", timeout=30)
    r.raise_for_status()
    cfg = r.json()
    cfg.pop("mode", None)
    return {
        "status": "ok",
        "listing": cfg,
        "facts_markdown": f"{SITE}/for-vendors.md",
        "submit_page": f"{SITE}/business/vendors#get-listed",
    }


@mcp.tool()
def submit_listing(tool_url: str, email: str, company: str = "", note: str = "") -> dict:
    """
    Start a HokAI directory listing for an AI tool, model, agent, MCP server,
    skill or AI service. Returns a payment link: a PERSON must open it and pay
    the one-time fee. Nothing is charged by this call, and the submission is
    reviewed by a human (full refund if the product is not a fit). Paying never
    affects rankings.

    Only call this when the product's owner or their team asked for it, and
    use their real work email: HokAI emails it when the page goes live.

    Args:
        tool_url: the product's own website, e.g. https://example.com
        email: a work email for the vendor
        company: company name (optional)
        note: anything the editors should know (optional)
    """
    payload = {
        "tool_url": tool_url,
        "email": email,
        "company": company or None,
        "note": ("[via MCP] " + note).strip()[:1000],
    }
    r = requests.post(f"{SITE}/api/listing/checkout", json=payload, timeout=30)
    try:
        data = r.json()
    except ValueError:
        data = {}
    if r.ok and data.get("url"):
        return {
            "status": "ok",
            "payment_url": data["url"],
            "next_step": "Give this link to the person who will pay. The listing is "
                         "submitted for review once payment completes.",
            "free_alternative": f"{SITE}/business/vendors#get-listed (place the "
                                "'Listed on HokAI' badge instead of paying)",
        }
    return {
        "status": "error",
        "http_status": r.status_code,
        "error": data.get("error") or "Submission failed.",
        "code": data.get("code"),
        "fallback": "Email adminhokai@gmail.com with the product URL, or use "
                    f"{SITE}/business/vendors#get-listed",
    }


@mcp.tool()
def scanner_status() -> dict:
    """
    Simple health check for the MCP server.
    """
    return {"status": "ok", "message": "MCP server running"}


if __name__ == "__main__":
    # Streamable HTTP transport for remote MCP
    mcp.run(transport="streamable-http")
