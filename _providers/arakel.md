---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.4
  scored_at: '2026-09-15'
api_count: 1
apis:
- description: REST API providing machine-readable evidence checks against official U.S. government sources, with free preflight routes and x402/HTTP-402 payment-gated paid routes. Also exposes an MCP server, llms.t
  name: ARAKEL Machine Evidence Network API
  slug: arakel-machine-evidence-network-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://proof.arakelproof.space
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arakel/refs/heads/main/security/arakel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arakel-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arakel/refs/heads/main/well-known/arakel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arakel-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arakel/refs/heads/main/conformance/arakel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arakel-conformance.yml
created: '2026-09-13'
description: Pay-per-call, machine-readable evidence checked against enabled official U.S. government sources (OFAC, FDA, USAspending, Federal Register), sold to autonomous agents via the x402 payment protocol. Identity-free, payment-gated using USDC on Base.
layout: provider
mcp_servers:
- description: ''
  name: ARAKEL Machine Evidence Network MCP Server
  slug: arakel-machine-evidence-network-mcp-server
- description: ''
  name: ARAKEL Machine Evidence Network
  slug: arakel-machine-evidence-network
modified: '2026-09-13'
name: ARAKEL Machine Evidence Network
nav: Providers
network: true
overview: ARAKEL Machine Evidence Network publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include machine-evidence, Compliance, Sanctions Screening, OFAC, and Regulatory Monitoring.
plans:
- name: Arakel Plans Pricing
  plan_count: 0
  slug: arakel-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Arakel Rate Limits
  slug: arakel-rate-limits
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 33.3
    developer_ergonomics: 28.6
    discoverability: 72.2
    operational_transparency: 0.0
  previous_composite: 29.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Arakel Authentication
  slug: arakel-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Arakel Domain Security
  slug: arakel-domain-security
  summary_line: TLSv1.3
slug: arakel
tags:
- machine-evidence
- Compliance
- Sanctions Screening
- OFAC
- Regulatory Monitoring
- Government Data
- FDA-recalls
- Federal Spending
- Federal Register
- counterparty-due-diligence
- agent-native
- x402
- pay-per-call
- MCP
- A2A
website: https://proof.arakelproof.space
---
