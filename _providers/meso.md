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
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://meso.network
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meso-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/meso-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meso-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://meso.network/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meso-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meso-llms.txt
created: '2026-07-17'
description: Meso is payment infrastructure designed for crypto. Backed by Ribbit Capital, the company is positioned as a payments-rails provider for the cryptocurrency sector. As of this enrichment pass its public web presence is a single-page marketing site at meso.network with no publicly documented developer portal, API reference, or OpenAPI definition surfaced yet. The one machine-readable artifact the company publishes is a PGP-signed RFC 9116 security.txt at /.well-known/security.txt declaring a security contact and disclosure policy. This profile was added to the API Evangelist network as a Ribbit Capital portfolio lead and is tracked for future API surface as the product launches.
image: https://meso.network/assets/img/open-meta.png
layout: provider
modified: '2026-07-20'
name: Meso
nav: Providers
network: true
overview: Meso is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Payments, Payment Infrastructure, and Cryptocurrency.
random_paper: 16
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 3
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
    operational_transparency: 10.5
  previous_composite: 5.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Meso Domain Security
  slug: meso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Meso Vulnerability Disclosure
  slug: meso-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: meso
tags:
- Company
- Crypto
- Payments
- Payment Infrastructure
- Cryptocurrency
- Fintech
- Blockchain
website: https://meso.network
---
