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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ftx-exchange-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claims.ftx.com/
created: '2026-07-17'
description: 'FTX Exchange was a cryptocurrency exchange (ftx.com / ftx.us) that collapsed in November 2022 and filed for Chapter 11 bankruptcy. As of the 2026-07-19 enrichment probe, all FTX web and docs domains (ftx.com, ftx.us, docs.ftx.com, docs.ftx.us) return 301 redirects to the FTX bankruptcy claims portal at claims.ftx.com; the former developer/API surface no longer exists. This profile was surfaced as a portfolio company of insight-partners and added to the API Evangelist network as a web3 stub. It is DEFUNCT: there is no live exchange, developer portal, documentation, OpenAPI, or API to enrich. The enrichment pipeline verified this and captured only real, probeable domain-security DNS/TLS data.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ftx-exchange.png
layout: provider
modified: '2026-07-19'
name: FTX Exchange
nav: Providers
network: true
overview: FTX Exchange is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company and Web3.
random_paper: 0
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 2
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ftx-exchange/refs/heads/main/screenshots/ftx-exchange-2026-07-25T215245.png
security:
- kind: domain-security
  name: Ftx Exchange Domain Security
  slug: ftx-exchange-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ftx-exchange
tags:
- Company
- Web3
website: https://claims.ftx.com/
---
