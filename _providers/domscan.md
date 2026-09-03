---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST domain-intelligence API (40+ endpoints under /v1) for availability, DNS, WHOIS/RDAP, SSL/TLS, email auth, valuation, security, and OSINT, with API-key authentication.
  name: DomScan API
  slug: domscan-api
artifact_total: 2
created: '2026-07-12'
description: Domain intelligence API for domain availability, DNS, WHOIS/RDAP, valuation, security checks, email posture, social handle checks, and monitoring workflows. Offers REST API, machine-readable contracts, a hosted MCP server, and llms.txt.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/domscan.png
layout: provider
mcp_servers:
- description: ''
  name: DomScan MCP Server
  slug: domscan-mcp-server
modified: '2026-07-12'
name: DomScan
nav: Providers
network: true
overview: DomScan publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Domains, DNS, WHOIS, rdap, and SSL/TLS.
random_paper: 6
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 1
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 14.3
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 15.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/domscan/refs/heads/main/screenshots/domscan-2026-07-25T212249.png
slug: domscan
tags:
- Domains
- DNS
- WHOIS
- rdap
- SSL/TLS
- Email Security
- domain-valuation
- Brand Protection
- OSINT
- Threat Intelligence
- MCP
- agent-native
---
