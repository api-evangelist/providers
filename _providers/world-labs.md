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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.worldlabs.ai
  baseurl_source: spec
  description: The credits API from World Labs — 1 operation(s) for credits.
  name: World Labs credits API
  slug: world-labs-credits-api
- baseURL: https://api.worldlabs.ai
  baseurl_source: spec
  description: The Marble API from World Labs — 8 operation(s) for marble.
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
  composite: 22.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 93.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 54.5
    developer_ergonomics: 19.0
    discoverability: 48.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 22.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
