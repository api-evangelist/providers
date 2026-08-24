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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.0
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: The credits API from World Labs — 1 operation(s) for credits.
  name: World Labs credits API
  slug: world-labs-credits-api
- description: The Marble API from World Labs — 8 operation(s) for marble.
  name: World Labs Marble API
  slug: world-labs-marble-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Marble Public API v1 credits API
  slug: open-world-labs-credits-api
- collection_type: open
  name: Public API v1 credits Marble API
  slug: open-world-labs-marble-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/world-labs-marble-developer-api.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/world-labs-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/world-labs-marble-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/world-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/world-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/world-labs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://worldlabs.ai
created: '2026-07-17'
description: 'World Labs is a company surfaced as a portfolio company of sv-angel and added to the API Evangelist network as a stub for enrichment. Sector: ai. This profile is a lead awaiting the enrichment pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/world-labs.png
layout: provider
mcp_servers:
- description: World Labs publishes no official MCP server as of this pass (none referenced in docs.worldlabs.ai, the worldlabsai GitHub org, or the official marble-developer-api-skill — the skill targets coding age
  name: World Labs MCP Server
  slug: world-labs-mcp-server
modified: '2026-07-17'
name: World Labs
nav: Providers
network: true
overview: 'World Labs publishes 2 APIs on the [APIs.io](https://apis.io/) network: credits API and Marble API. Tagged areas include Company and Artificial Intelligence.


  World Labs'' developer surface includes authentication and 6 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 24.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 56.1
    developer_ergonomics: 19.0
    discoverability: 48.1
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 24.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: World Labs Authentication
  slug: world-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: World Labs Domain Security
  slug: world-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: World Labs Vulnerability Disclosure
  slug: world-labs-vulnerability-disclosure
  summary_line: disclosure policy published
slug: world-labs
tags:
- Company
- Artificial Intelligence
website: https://worldlabs.ai
---
