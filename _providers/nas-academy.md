---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nas Academy Agentic Access
  operation_count: 36
  slug: nas-academy-agentic-access
  summary_line: 36 operations
api_count: 1
apis:
- baseURL: https://nas.com
  baseurl_source: spec
  description: Public machine-readable resources for AI assistants, crawlers, and agents.
  name: Nas Academy AI discovery API
  slug: nas-academy-ai-discovery-api
- baseURL: https://nas.com
  baseurl_source: spec
  description: Public developer and integration guidance without private API contracts.
  name: Nas Academy Developer discovery API
  slug: nas-academy-developer-discovery-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nas.com Public Discovery AI discovery API
  slug: open-nas-academy-ai-discovery-api
- collection_type: open
  name: Nas.com Public Discovery AI discovery Developer discovery API
  slug: open-nas-academy-developer-discovery-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/nas-academy-discovery-skill.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nas-academy-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nas-academy-discovery-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://nasdaily.com
created: '2026-07-17'
description: Nas Academy is a company surfaced as a portfolio company of 500-global and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: Official authenticated hosted MCP server for Nas.com business, member, product, and order context.
  name: Nas Academy MCP Server
  slug: nas-academy-mcp-server
modified: '2026-07-17'
name: Nas Academy
nav: Providers
network: true
overview: 'Nas Academy publishes 2 APIs on the [APIs.io](https://apis.io/) network: AI discovery API and Developer discovery API. Tagged areas include Company.'
random_paper: 20
scopes:
- name: Nas Academy Scopes
  scope_count: 6
  slug: nas-academy-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 85.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 45.7
    developer_ergonomics: 7.1
    discoverability: 35.2
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 18.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nas-academy/refs/heads/main/screenshots/nas-academy-2026-08-07T184637.png
security:
- kind: authentication
  name: Nas Academy Authentication
  slug: nas-academy-authentication
  summary_line: none/oauth2 · 2 schemes
- kind: domain-security
  name: Nas Academy Domain Security
  slug: nas-academy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nas-academy
tags:
- Company
website: https://nasdaily.com
---
