import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

MCP_URL = "https://api.fabric.microsoft.com/v1/mcp/powerbi"


async def main():
    print("Conectando al servidor MCP de Power BI...")

    async with streamable_http_client(MCP_URL) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            print("Inicializando sesión MCP...")
            await session.initialize()

            print("Listando herramientas disponibles...")
            tools = await session.list_tools()

            print("\nHerramientas encontradas:")
            for tool in tools.tools:
                print(f"- {tool.name}")


if __name__ == "__main__":
    asyncio.run(main())