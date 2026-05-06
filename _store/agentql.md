---
aid: agentql
name: AgentQL
description: AgentQL connects LLMs and AI agents to the entire web through a specialized query language, REST API, and Python/JavaScript SDKs. It enables web scraping, data extraction, and browser automation using natural language queries that are self-healing — adapting automatically to page layout changes. AgentQL supports structured data extraction from web pages, PDF documents, and images, and integrates with LangChain, LlamaIndex, MCP, Zapier, and Google ADK.
url: https://raw.githubusercontent.com/api-evangelist/agentql/refs/heads/main/apis.yml
humanURL: https://www.agentql.com/
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consumer
tags:
  - Agents
  - Artificial Intelligence
  - Web Scraping
  - Data Extraction
  - Browser Automation
  - REST API
created: '2025-08-19'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: agentql:query-data-api
    name: AgentQL Query Data API
    description: Extract structured JSON data from web pages using AgentQL query language or natural language prompts. Supports URL-based and raw HTML input, configurable browser behavior, proxy settings, and screenshot capture.
    humanURL: https://docs.agentql.com/rest-api/api-reference
    baseURL: https://api.agentql.com
    tags:
      - Data Extraction
      - Web Scraping
      - REST API
      - AI
    properties:
      - type: Documentation
        url: https://docs.agentql.com/rest-api/api-reference
      - type: GettingStarted
        url: https://docs.agentql.com/quick-start
      - type: Authentication
        url: https://docs.agentql.com/rest-api/authentication
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/agentql/refs/heads/main/openapi/agentql-openapi.yaml
  - aid: agentql:remote-browser-api
    name: AgentQL Remote Browser Sessions API
    description: Create and manage remote Chrome browser sessions with Chrome DevTools Protocol (CDP) access for authenticated web automation, stealth browsing, and complex multi-step interactions.
    humanURL: https://docs.agentql.com/rest-api/api-reference
    baseURL: https://api.agentql.com
    tags:
      - Browser Automation
      - Remote Browser
      - CDP
      - Web Automation
    properties:
      - type: Documentation
        url: https://docs.agentql.com/rest-api/api-reference
  - aid: agentql:query-document-api
    name: AgentQL Query Document API
    description: Extract structured data from PDF documents and images (JPEG, PNG) using AgentQL query language or natural language prompts. Useful for processing invoices, reports, and other document formats.
    humanURL: https://docs.agentql.com/rest-api/api-reference
    baseURL: https://api.agentql.com
    tags:
      - Document Parsing
      - PDF
      - Data Extraction
      - AI
    properties:
      - type: Documentation
        url: https://docs.agentql.com/rest-api/api-reference
common:
  - type: Portal
    url: https://www.agentql.com/
  - type: Documentation
    url: https://docs.agentql.com/home
  - type: GettingStarted
    url: https://docs.agentql.com/quick-start
  - type: Pricing
    url: https://www.agentql.com/pricing
  - type: Blog
    url: https://www.agentql.com/blog
  - type: Support
    url: https://docs.agentql.com/support
  - type: Console
    url: https://dev.agentql.com/playground
  - type: SDK
    url: https://pypi.org/project/agentql/
    title: Python SDK
  - type: SDK
    url: https://www.npmjs.com/package/agentql
    title: JavaScript SDK
  - type: CLI
    url: https://docs.agentql.com/cli
  - type: GitHubOrganization
    url: https://github.com/tinyfish-io
  - type: Features
    data:
      - name: Natural Language Query Language
        description: A specialized query language that uses natural language to locate and extract web elements without requiring XPath, CSS selectors, or regex.
      - name: Self-Healing Queries
        description: AI-powered queries automatically adapt to page layout changes, eliminating brittle scrapers that break on site updates.
      - name: REST API
        description: Browserless data extraction from public URLs via a REST API requiring only an API key and query parameters.
      - name: PDF and Image Parsing
        description: Extract structured data from PDF documents, JPEG, and PNG images using the same query language as web extraction.
      - name: Remote Browser Sessions
        description: Managed Chrome browser sessions with CDP access for authenticated browsing, stealth mode, and complex multi-step web automation.
      - name: Playwright Integration
        description: Python and JavaScript SDKs extend Playwright with AgentQL query capabilities for AI-powered browser automation.
      - name: Browser Debugger Extension
        description: Chrome extension for real-time query testing and optimization during development.
  - type: UseCases
    data:
      - name: E-Commerce Price Monitoring
        description: Extract product names, prices, and availability from e-commerce sites for competitive intelligence and price tracking.
      - name: Job Board Aggregation
        description: Collect job listings, requirements, and company information from multiple job boards into a unified dataset.
      - name: Social Media Content Harvesting
        description: Extract posts, metrics, and profile data from social media platforms for analysis and reporting.
      - name: Document Data Extraction
        description: Parse invoices, contracts, and reports in PDF format to extract structured data for downstream processing.
      - name: AI Agent Web Access
        description: Enable AI agents to access and extract data from any website as part of automated research and task completion workflows.
      - name: Lead Generation
        description: Automate the collection of contact information, company data, and other business intelligence from public web sources.
  - type: Integrations
    data:
      - name: LangChain
        description: Integrate AgentQL web extraction into LangChain agent and chain workflows.
      - name: LlamaIndex
        description: Use AgentQL as a data ingestion source for LlamaIndex-powered RAG and agent applications.
      - name: MCP (Model Context Protocol)
        description: Expose AgentQL capabilities as MCP tools accessible to any MCP-compatible AI agent.
      - name: Zapier
        description: Connect AgentQL web extraction to thousands of apps via Zapier automation workflows.
      - name: Google ADK
        description: Integrate AgentQL with Google Agent Development Kit for Gemini-based agent web access.
      - name: Langflow
        description: Use AgentQL in Langflow visual AI workflow pipelines for web data extraction.
      - name: Playwright
        description: Extend Playwright browser automation with AgentQL AI-powered element querying and data extraction.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
