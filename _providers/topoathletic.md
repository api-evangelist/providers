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
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/topoathletic-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/topoathletic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://topoathletic.com
created: '2026-07-17'
description: Topo Athletic is a performance footwear brand offering road running, trail running, hiking, and recovery shoes plus apparel and accessories (Topo Gear). Its shoes are known for a roomy toe box, secure midfoot and heel fit, low heel-to-toe drop, and the ZipFoam midsole, designed to promote natural movement and foot health. Surfaced as a portfolio company of Norwest Venture Partners and added to the API Evangelist network. Topo Athletic operates a direct-to-consumer e-commerce site at topoathletic.com; as of this enrichment pass it publishes no public developer API, developer portal, or API documentation. It does publish a machine-readable /llms.txt describing its catalog and support surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/topoathletic.png
layout: provider
modified: '2026-07-21'
name: Topo Athletic
nav: Providers
network: true
overview: Topo Athletic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Footwear, Running, Trail Running, and Hiking.
random_paper: 15
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
screenshot: https://raw.githubusercontent.com/api-evangelist/topoathletic/refs/heads/main/screenshots/topoathletic-2026-09-02T163924.png
security:
- kind: domain-security
  name: Topoathletic Domain Security
  slug: topoathletic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: topoathletic
tags:
- Company
- Footwear
- Running
- Trail Running
- Hiking
- Apparel
- Retail
- E-Commerce
- Consumer
- Sportswear
website: https://topoathletic.com
---
