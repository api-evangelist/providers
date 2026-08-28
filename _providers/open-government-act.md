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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Australian Capital Territory Open Data
  name: Open Government, ACT
  slug: open-government-act
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-government-act-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-government-act-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.data.act.gov.au/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Australian Capital Territory Open Data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-government-act.png
layout: provider
modified: '2026-05-28'
name: Open Government, ACT
nav: Providers
network: true
overview: Open Government, ACT publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 18
score:
  band: minimal
  composite: 7.7
  delta: 1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-government-act/refs/heads/main/screenshots/open-government-act-2026-06-20T190748.png
security:
- kind: domain-security
  name: Open Government Act Domain Security
  slug: open-government-act-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Open Government Act Vulnerability Disclosure
  slug: open-government-act-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: open-government-act
tags:
- Government
- Public APIs
website: https://www.data.act.gov.au/
---
