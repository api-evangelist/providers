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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sekra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sekra.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sekra-llms.txt
created: '2026-07-17'
description: Sekra is a residential and community development company building spaces designed around human connection — its tagline is "the future of home is Human," with an emphasis on community, culture, and longevity. Sekra partners with property owners, developers, and investors globally to create residential communities, and is expanding to new cities. Surfaced in the API Evangelist network as a portfolio company of Fifth Wall (proptech). As of enrichment, Sekra publishes no public API, developer portal, SDKs, or technical integration surface — this profile captures its identity and a probed domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sekra.png
layout: provider
modified: '2026-07-21'
name: Sekra
nav: Providers
network: true
overview: Sekra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PropTech, Real-Estate, Community, and Residential.
random_paper: 9
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sekra/refs/heads/main/screenshots/sekra-2026-09-02T154815.png
security:
- kind: domain-security
  name: Sekra Domain Security
  slug: sekra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sekra
tags:
- Company
- PropTech
- Real-Estate
- Community
- Residential
- Housing
- Property Development
website: https://www.sekra.com/
---
