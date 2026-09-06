---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.evolvtechnology.com/'', ''status'': 301, ''note'': ''declared website redirects to https://evolv.com/ — a different registrable domain (evolvtechnology.com -> evolv.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/evolv-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.evolvtechnology.com/
created: '2026-07-17'
description: 'Evolv Technologies Holdings, Inc. (NASDAQ: EVLV), headquartered in Waltham, Massachusetts, builds AI-based touchless security screening systems used to detect concealed weapons at venues, schools, hospitals, workplaces, and stadiums. Its flagship Evolv Express walk-through system uses sensor fusion and machine learning to screen people at high throughput without requiring them to stop, empty pockets, or remove bags, and the companion Evolv Insights analytics product reports on screening volume, alert rates, and operational performance. Evolv Technology is a portfolio company of DCVC and was added to the API Evangelist network as a company profile. As of this enrichment pass the company publishes no public developer API, OpenAPI/Swagger definition, SDK, MCP server, or open developer portal; its public web presence is served behind bot protection and its status surface is gated behind SSO.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/evolv-technology.png
layout: provider
modified: '2026-07-19'
name: Evolv Technology
nav: Providers
network: true
overview: Evolv Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Physical Security, Weapons Detection, and Screening.
random_paper: 5
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evolv-technology/refs/heads/main/screenshots/evolv-technology-2026-07-25T213811.png
security:
- kind: domain-security
  name: Evolv Technology Domain Security
  slug: evolv-technology-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: evolv-technology
tags:
- Company
- Security
- Physical Security
- Weapons Detection
- Screening
- Artificial Intelligence
- Sensor Fusion
- Public Safety
website: https://www.evolvtechnology.com/
---
