---
aid: context7
url: https://raw.githubusercontent.com/api-evangelist/context7/refs/heads/main/apis.yml
name: Context7
description: Context7 is an Upstash service providing up-to-date, version-specific documentation and code examples for libraries and frameworks, exposed as both a REST API and a Model Context Protocol (MCP) server so AI coding assistants can fetch authoritative reference material at prompt time.
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Context
  - Documentation
  - LLM
  - MCP
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: context7:rest-api
    name: Context7 REST API
    tags:
      - Documentation
      - LLM
      - REST
      - Search
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://context7.com/api
    humanURL: https://context7.com/docs/api-guide
    properties:
      - url: https://context7.com/docs/api-guide
        type: Documentation
      - url: https://context7.com/docs/llms.txt
        type: LLMsTxt
    description: The Context7 REST API exposes endpoints for searching libraries, retrieving documentation context for LLMs, refreshing indexed sources, and submitting new sources (GitHub repositories, OpenAPI specs, llms.txt files, websites, and Confluence spaces). Endpoints span v1 and v2 paths under https://context7.com/api and use Bearer token authentication with keys issued from the Context7 dashboard.
  - aid: context7:mcp-server
    name: Context7 MCP Server
    tags:
      - AI
      - Context
      - LLM
      - MCP
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://mcp.context7.com/mcp
    humanURL: https://github.com/upstash/context7
    properties:
      - url: https://github.com/upstash/context7
        type: Documentation
      - url: https://github.com/upstash/context7
        type: GitHubRepository
    description: The Context7 MCP Server implements the Model Context Protocol so AI coding assistants such as Cursor, Claude, and Windsurf can call Context7 tools directly from a developer's editor. It exposes resolve-library-id (mapping a library name to a Context7-compatible identifier) and query-docs (returning documentation snippets for a given library and query) and is hosted at https://mcp.context7.com/mcp with API key authentication.
  - aid: context7:cli
    name: Context7 CLI
    tags:
      - CLI
      - Documentation
      - Tooling
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/upstash/context7
    properties:
      - url: https://github.com/upstash/context7
        type: Documentation
      - url: https://github.com/upstash/context7
        type: GitHubRepository
    description: The Context7 CLI (ctx7) is a command-line tool for querying the Context7 index from the terminal. It provides ctx7 library for searching the catalog by library name and ctx7 docs for retrieving documentation using a Context7-compatible library ID, useful for scripting and local developer workflows.
common:
  - type: Website
    url: https://context7.com/
  - type: Documentation
    url: https://context7.com/docs
  - type: Dashboard
    url: https://context7.com/dashboard
  - type: GitHub Organization
    url: https://github.com/upstash
  - type: GitHubRepository
    url: https://github.com/upstash/context7
  - type: Pricing
    url: https://context7.com/pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
