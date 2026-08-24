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
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.6
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lydia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://lydia-app.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/lydia-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lydia-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lydia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lydia-app.com/
- group: company
  title: ''
  type: Website
  url: https://sumeria.eu/
created: '2026-07-17'
description: Lydia is a French fintech, founded in 2013, that built one of Europe's most popular mobile peer-to-peer payments apps, letting users send money, split bills, and pay merchants from their phone. Backed by Accel, Tencent and others, the company evolved into a full mobile banking and financial services provider. In 2024 it split its consumer banking product into a new brand, Sumeria (sumeria.eu), while the Lydia name continues for the P2P payments experience. Lydia publishes a security.txt bug-bounty contact but no longer exposes a public developer API or portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lydia.png
layout: provider
modified: '2026-07-20'
name: Lydia
nav: Providers
network: true
overview: Lydia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, Mobile Payments, and Peer-to-Peer.
random_paper: 6
score:
  band: minimal
  composite: 4.4
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 4.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lydia/refs/heads/main/screenshots/lydia-2026-07-25T225745.png
security:
- kind: domain-security
  name: Lydia Domain Security
  slug: lydia-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Lydia Vulnerability Disclosure
  slug: lydia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lydia
tags:
- Company
- Payments
- Fintech
- Mobile Payments
- Peer-to-Peer
- Banking
- Neobank
- France
website: https://lydia-app.com/
---
