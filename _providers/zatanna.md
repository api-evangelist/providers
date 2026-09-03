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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Zatanna's hosted, remote Model Context Protocol (MCP) server — the agent-facing surface of its reverse-engineered portal integrations. Live at https://api.zatanna.ai/mcp over Streamable HTTP (JSON-RPC
  name: Zatanna MCP Server
  slug: zatanna-mcp-server
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.zatanna.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zatanna.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zatanna.ai/privacy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zatanna-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zatanna-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zatanna-domain-security.yml
created: '2026-07-17'
description: Zatanna is a Y Combinator (W2026) startup based in San Francisco that creates APIs for software that doesn't have any. It reverse-engineers the back ends of web-based cloud and on-prem software — ERPs (SAP), PMS/POS systems, insurance portals, and marketplaces — by observing real workflows, reconstructing the underlying request sequences, and hosting them as clean, callable APIs. Rather than relying on slow browser automation or computer-use agents, Zatanna gives AI agents faster, cheaper, and more reliable integrations, with a reliability layer that handles session management, authentication, and change detection. The agent-facing surface is a hosted, OAuth-protected Model Context Protocol (MCP) server at api.zatanna.ai.
image: https://raw.githubusercontent.com/api-evangelist/zatanna/refs/heads/main/apis.yml
layout: provider
mcp_servers:
- description: 'Zatanna operates a hosted, remote MCP server at https://api.zatanna.ai/mcp. The endpoint is live: an unauthenticated POST returns HTTP 401 with a WWW-Authenticate Bearer challenge pointing at the RFC '
  name: Zatanna MCP Server
  slug: zatanna-mcp-server
modified: '2026-07-21'
name: Zatanna
nav: Providers
network: true
overview: Zatanna publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, AI Agents, Integration, and Reverse Engineering.
random_paper: 14
scopes:
- name: Zatanna Scopes
  scope_count: 4
  slug: zatanna-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 16.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zatanna/refs/heads/main/screenshots/zatanna-2026-09-02T171456.png
security:
- kind: authentication
  name: Zatanna Authentication
  slug: zatanna-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Zatanna Domain Security
  slug: zatanna-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zatanna
tags:
- Company
- MCP
- AI Agents
- Integration
- Reverse Engineering
- Automation
- Authentication
- Y Combinator
website: https://www.zatanna.ai/
---
