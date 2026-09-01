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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xairos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.xairos.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xairos-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xairos-mcp.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xairos/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/xairos2
created: '2026-07-17'
description: Xairos Systems is a Techstars-backed company building quantum time transfer (QTT) technology - a space-based, quantum-resilient global timing and synchronization system positioned as a secure alternative to GPS for positioning, navigation, and timing (PNT). The company targets sub-nanosecond accuracy while mitigating GPS jamming and spoofing, serving critical infrastructure sectors such as transportation, finance, data centers, and power grids. Xairos publishes no first-party developer API, but its site ships an llms.txt and a live Wix Site MCP endpoint for agentic access to public site content.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xairos.png
layout: provider
mcp_servers:
- description: ''
  name: Xairos MCP Server
  slug: xairos-mcp-server
modified: '2026-07-21'
name: Xairos
nav: Providers
network: true
overview: Xairos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quantum, Timing, Synchronization, and PNT.
random_paper: 11
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  provenance:
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Xairos Domain Security
  slug: xairos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xairos
tags:
- Company
- Quantum
- Timing
- Synchronization
- PNT
- GPS Alternative
- Critical Infrastructure
website: https://www.xairos.com/
---
