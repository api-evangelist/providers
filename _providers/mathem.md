---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mathem-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/mathem-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mathem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mathem.se
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/mathem-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mathem-well-known.yml
created: '2026-07-17'
description: Mathem is Sweden's largest pure-play online grocery retailer, delivering fresh food, household goods and pantry staples directly to consumers' homes across Sweden. Customers browse and order the full assortment of a physical supermarket through the mathem.se website and native iOS/Android apps, and receive scheduled home delivery. Mathem merged with the Norwegian online grocer Oda to form one of the Nordics' largest online grocery groups, and its security and careers functions are now operated under the shared Oda organization. Payments are handled through Klarna and the major card networks. Mathem operates a consumer e-commerce storefront and mobile apps; it does not publish a public developer API, SDKs, or a developer portal. This API Evangelist profile was created as a SoftBank Vision Fund portfolio lead and enriched via the enrichment pipeline; the substantive public technical surface found is an RFC 9116 security.txt and an invite-only YesWeHack bug-bounty program run through
  Oda.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mathem.png
layout: provider
modified: '2026-07-20'
name: Mathem
nav: Providers
network: true
overview: Mathem is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Grocery, E-Commerce, and Retail.
random_paper: 6
score:
  band: minimal
  composite: 6.4
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 6.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mathem/refs/heads/main/screenshots/mathem-2026-07-25T230409.png
security:
- kind: domain-security
  name: Mathem Domain Security
  slug: mathem-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mathem Vulnerability Disclosure
  slug: mathem-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mathem
tags:
- Company
- Consumer
- Grocery
- E-Commerce
- Retail
- Food Delivery
- Sweden
- Nordics
website: https://www.mathem.se
---
