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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-17'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.gao.gov/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/government-accountability-office/refs/heads/main/security/government-accountability-office-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/government-accountability-office-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-government
- group: other
  title: ''
  type: Reports
  url: https://www.gao.gov/reports-testimonies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gao.gov/copyright
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gao.gov/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.gao.gov/about/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.gao.gov/blog
- group: company
  title: ''
  type: BlogFeeds
  url: https://www.gao.gov/rss/reports.xml
- group: company
  title: ''
  type: Press
  url: https://www.gao.gov/press-center
- group: other
  title: ''
  type: Podcast
  url: https://www.gao.gov/podcast
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/government-accountability-office/refs/heads/main/llms/government-accountability-office-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/government-accountability-office-llms.txt
coverage:
  checked: '2026-09-12'
  detail: GAO publishes no API and no developer program of any kind — its entire machine-readable public surface is a catalog of ~40 RSS 2.0 feeds, while the Recommendations Database, bid-protest docket and appropriations-law decisions are browser-only search applications whose query strings robots.txt disallows.
  evidence:
  - status: 404
    url: https://www.gao.gov/openapi.json
  - status: 404
    url: https://www.gao.gov/.well-known/api-catalog
  - status: 404
    url: https://www.gao.gov/about/what-gao-does/data-tools
  - status: 200
    url: https://www.gao.gov/rss/reports.xml
  reason: no-developer-program
  state: none
created: '2024-12-25'
description: The Government Accountability Office (GAO) is the United States government's supreme audit institution. It provides Congress with auditing, evaluation, and investigative services, and publishes reports, testimonies, and other products examining federal programs and policies.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/government-accountability-office.png
layout: provider
modified: '2026-09-12'
name: Government Accountability Office
nav: Providers
network: true
overview: 'Government Accountability Office is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Accountability, Auditing, Federal-Government, Government, and United States.


  Government Accountability Office''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 25.9
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/government-accountability-office/refs/heads/main/screenshots/government-accountability-office-2026-06-20T182302.png
security:
- kind: domain-security
  name: Government Accountability Office Domain Security
  slug: government-accountability-office-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: government-accountability-office
tags:
- Accountability
- Auditing
- Federal-Government
- Government
- United States
website: https://www.gao.gov/
---
