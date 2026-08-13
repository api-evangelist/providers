---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Agentql Agentic Access
  operation_count: 3
  slug: agentql-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 5
apis:
- description: Create and manage remote Chrome browser sessions with Chrome DevTools Protocol (CDP) access for authenticated web automation, stealth browsing, and complex multi-step interactions.
  name: AgentQL Remote Browser Sessions API
  slug: remote-browser-api
- description: Extract structured data from PDF documents and images (JPEG, PNG) using AgentQL query language or natural language prompts. Useful for processing invoices, reports, and other document formats.
  name: AgentQL Query Document API
  slug: query-document-api
- description: Extract structured data from web pages using AgentQL queries
  name: AgentQL Query Data API
  slug: agentql-query-data-api
- description: Extract structured data from PDF and image documents
  name: AgentQL Query Document API
  slug: agentql-query-document-api
- description: Manage remote Chrome browser sessions with CDP access
  name: AgentQL Remote Browser API
  slug: agentql-remote-browser-api
artifact_total: 46
collections:
- collection_type: postman
  name: AgentQL Query Data API
  slug: postman-agentql-query-data-api
- collection_type: postman
  name: AgentQL Query Data Query Document API
  slug: postman-agentql-query-document-api
- collection_type: postman
  name: AgentQL Query Data Remote Browser API
  slug: postman-agentql-remote-browser-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/agentql/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agentql-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agentql-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agentql-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.agentql.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentql.com/home
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentql.com/quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agentql.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.agentql.com/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.agentql.com/support
- group: start
  title: ''
  type: Console
  url: https://dev.agentql.com/playground
- group: build
  title: Python SDK
  type: SDKs
  url: https://pypi.org/project/agentql/
- group: build
  title: JavaScript SDK
  type: SDKs
  url: https://www.npmjs.com/package/agentql
- group: build
  title: ''
  type: CLI
  url: https://docs.agentql.com/cli
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tinyfish-io
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/tinyfish-io/agentql-mcp
created: '2025-08-19'
description: AgentQL connects LLMs and AI agents to the entire web through a specialized query language, REST API, and Python/JavaScript SDKs. It enables web scraping, data extraction, and browser automation using natural language queries that are self-healing — adapting automatically to page layout changes. AgentQL supports structured data extraction from web pages, PDF documents, and images, and integrates with LangChain, LlamaIndex, MCP, Zapier, and Google ADK.
examples:
- key_count: 3
  name: Agentql Create Session Response Example
  slug: agentql-create-session-response-example
- key_count: 3
  name: Agentql Query Data Request Example
  slug: agentql-query-data-request-example
features:
- description: A specialized query language that uses natural language to locate and extract web elements without requiring XPath, CSS selectors, or regex.
  name: Natural Language Query Language
- description: AI-powered queries automatically adapt to page layout changes, eliminating brittle scrapers that break on site updates.
  name: Self-Healing Queries
- description: Browserless data extraction from public URLs via a REST API requiring only an API key and query parameters.
  name: REST API
- description: Extract structured data from PDF documents, JPEG, and PNG images using the same query language as web extraction.
  name: PDF and Image Parsing
- description: Managed Chrome browser sessions with CDP access for authenticated browsing, stealth mode, and complex multi-step web automation.
  name: Remote Browser Sessions
- description: Python and JavaScript SDKs extend Playwright with AgentQL query capabilities for AI-powered browser automation.
  name: Playwright Integration
- description: Chrome extension for real-time query testing and optimization during development.
  name: Browser Debugger Extension
finops:
- name: Agentql Finops
  service_category: API
  slug: agentql-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agentql.png
json_schemas:
- name: CreateSessionRequest
  property_count: 4
  slug: agentql-create-session-request
- name: CreateSessionResponse
  property_count: 3
  slug: agentql-create-session-response
- name: QueryDataRequest
  property_count: 5
  slug: agentql-query-data-request
- name: QueryDataResponse
  property_count: 2
  slug: agentql-query-data-response
- name: QueryDocumentRequest
  property_count: 3
  slug: agentql-query-document-request
- name: QueryParams
  property_count: 5
  slug: agentql-query-params
- name: ResponseMetadata
  property_count: 2
  slug: agentql-response-metadata
json_structures:
- name: Agentql Create Session Request Structure
  property_count: 4
  slug: agentql-create-session-request-structure
- name: Agentql Create Session Response Structure
  property_count: 3
  slug: agentql-create-session-response-structure
- name: Agentql Query Data Request Structure
  property_count: 5
  slug: agentql-query-data-request-structure
- name: Agentql Query Data Response Structure
  property_count: 2
  slug: agentql-query-data-response-structure
- name: Agentql Query Document Request Structure
  property_count: 3
  slug: agentql-query-document-request-structure
- name: Agentql Query Params Structure
  property_count: 5
  slug: agentql-query-params-structure
- name: Agentql Response Metadata Structure
  property_count: 2
  slug: agentql-response-metadata-structure
jsonld:
- class_count: 5
  name: Agentql Context
  property_count: 16
  slug: agentql-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: AgentQL
nav: Providers
network: true
overview: 'AgentQL publishes 3 APIs on the [APIs.io](https://apis.io/) network: Query Data API, Query Document API, and Remote Browser API. Tagged areas include Agents, Artificial Intelligence, Web Scraping, Data Extraction, and Browser Automation.


  The AgentQL catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentQL''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, support, and 9 more developer resources.'
plans:
- name: Agentql Plans Pricing
  plan_count: 4
  slug: agentql-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 5
  name: Agentql Rate Limits
  slug: agentql-rate-limits
rules:
- name: AgentQL API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agentql-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.9
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 23.5
    developer_ergonomics: 78.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agentql/refs/heads/main/screenshots/agentql-2026-06-20T170057.png
security:
- kind: authentication
  name: Agentql Authentication
  slug: agentql-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Agentql Domain Security
  slug: agentql-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: agentql
tags:
- Agents
- Artificial Intelligence
- Web Scraping
- Data Extraction
- Browser Automation
- REST API
use_cases:
- description: Extract product names, prices, and availability from e-commerce sites for competitive intelligence and price tracking.
  name: E-Commerce Price Monitoring
- description: Collect job listings, requirements, and company information from multiple job boards into a unified dataset.
  name: Job Board Aggregation
- description: Extract posts, metrics, and profile data from social media platforms for analysis and reporting.
  name: Social Media Content Harvesting
- description: Parse invoices, contracts, and reports in PDF format to extract structured data for downstream processing.
  name: Document Data Extraction
- description: Enable AI agents to access and extract data from any website as part of automated research and task completion workflows.
  name: AI Agent Web Access
- description: Automate the collection of contact information, company data, and other business intelligence from public web sources.
  name: Lead Generation
website: https://www.agentql.com/
---
