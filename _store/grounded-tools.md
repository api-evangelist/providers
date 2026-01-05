---
aid: grounded-tools
url: >-
  https://raw.githubusercontent.com/api-evangelist/grounded-tools/refs/heads/main/apis.yml
apis:
  - aid: grounded-tools:grounded-tools
    name: grounded.tools
    tags:
      - Experience
      - Documentation
      - Developer Tools
      - Developers
    humanURL: ' https://grounded.tools/'
    properties:
      - url: ' https://grounded.tools/'
        type: Documentation
    description: >-
      Index 3rd party documentation from websites, GitHub, npm, PyPI, and local
      files. Provide your AI with version-aware search tools via the Model
      Context Protocol. 
name: grounded.tools
tags:
  - Experience
  - Documentation
  - Developer Tools
  - Developers
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://grounded.tools/
    name: Docs MCP Server | grounded.tools
    type: Website
    description: 'null'
  - url: https://grounded.tools/#features
    name: Docs MCP Server | grounded.tools
    type: Features
    description: 'null'
created: '2026-01-02'
modified: '2026-01-04'
position: Consuming
description: >-
  Grounded.tools (Grounded Docs MCP Server) is an open-source, privacy-first
  documentation indexing tool that keeps AI assistants informed with up-to-date,
  version-specific documentation from multiple sources. The tool addresses
  common issues like stale LLM knowledge, hallucinated code, and version
  ambiguity by indexing documentation from websites, GitHub repositories, npm,
  PyPI, and local files, then providing AI assistants with version-aware search
  capabilities via the Model Context Protocol (MCP). Unlike generic web
  scrapers, Grounded.tools uses structure-aware RAG (Retrieval-Augmented
  Generation) that parses documents as hierarchies and intelligently handles
  code blocks while preserving API signatures and proper formatting. The system
  runs entirely locally on your machine for privacy, offers semantic search with
  relevance ranking, supports OAuth security, and provides tools like
  search_docs for querying indexed documentation and fetch_url for grabbing
  pages on the fly. Compatible with popular AI development tools including
  Cursor, Claude Desktop, VS Code, GitHub Copilot, and any MCP-compatible
  assistant, Grounded.tools serves as an open-source alternative to Context7,
  Nia, and Ref.Tools, enabling faster AI code assistance while reducing API
  costs through condensed, highly-relevant context delivery.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---