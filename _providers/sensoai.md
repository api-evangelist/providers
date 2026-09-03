---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'Key-authenticated REST API to ingest content into a knowledge base, run semantic search with AI-generated answers, and generate verified content. Authenticated with an X-API-Key header (keys prefixed '
  name: Senso Org API
  slug: senso-org-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://senso.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.senso.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.senso.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.senso.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.senso.ai/docs/hello-world
- group: company
  title: ''
  type: Blog
  url: https://blog.senso.ai/
- group: operate
  title: ''
  type: Support
  url: https://faqs.senso.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AI-Template-SDK
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sensoai-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/sensoai-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/sensoai-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sensoai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sensoai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sensoai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sensoai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sensoai-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sensoai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sensoai-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Senso.ai is a verified-context layer for the agentic web that keeps AI agents aligned with an organization's ground truth. Teams ingest raw sources into a knowledge base, run semantic search that returns an AI-generated answer plus the source chunks, and generate verified, on-brand content from that knowledge. Senso also tracks how AI assistants (OpenAI, Gemini, Amazon Nova) answer questions about a brand and remediates incorrect answers (generative engine optimization). The Senso Org API is a key-authenticated REST API at https://apiv2.senso.ai/api/v1, with an official CLI and a Model Context Protocol (MCP) server so agents like Claude can ingest, search, and generate against a knowledge base directly.
image: https://docs.senso.ai/senso-logo.png
layout: provider
mcp_servers:
- description: Official Model Context Protocol server for the Senso API, published by Senso (GitHub org AI-Template-SDK). Lets Claude Desktop (and other MCP clients) add raw content, search, and generate against a S
  name: Senso.ai MCP Server
  slug: sensoai-mcp-server
modified: '2026-07-21'
name: Senso.ai
nav: Providers
network: true
overview: 'Senso.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Knowledge Base, AI Agents, Content Generation, and Semantic Search.


  Senso.ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, authentication, and 12 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 55.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 19.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sensoai/refs/heads/main/screenshots/sensoai-2026-09-02T154912.png
security:
- kind: authentication
  name: Sensoai Authentication
  slug: sensoai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sensoai Domain Security
  slug: sensoai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sensoai
tags:
- Company
- Knowledge Base
- AI Agents
- Content Generation
- Semantic Search
- Generative Engine Optimization
- Verified Context
- Agentic Web
- MCP
website: https://senso.ai/
---
