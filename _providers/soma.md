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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.somainsure.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.somainsure.com/terms
created: '2026-07-17'
description: Soma (Soma Insurance Services) is a commercial insurance brokerage that positions itself as the fastest brokerage for complex businesses, placing customized commercial-lines coverage across industries including retail, trucking, hospitality, healthcare, finance, technology, manufacturing, and construction. Coverage lines include general liability, commercial auto, cyber liability, professional liability, and builder's risk. Backed by Accel and Cowboy Ventures in the insurance-tech sector. As of this enrichment pass Soma publishes no public API, developer portal, or documentation surface; this profile captures its public web presence and domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soma.png
layout: provider
modified: '2026-07-21'
name: Soma
nav: Providers
network: true
overview: Soma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance Tech, Insurance, Commercial Insurance, and Insurance Brokerage.
random_paper: 12
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Soma Domain Security
  slug: soma-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: soma
tags:
- Company
- Insurance Tech
- Insurance
- Commercial Insurance
- Insurance Brokerage
- Cyber Liability
- Fintech
website: https://www.somainsure.com/
---
