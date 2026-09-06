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
  url: security/tripoto-travel-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tripoto-travel-llms.txt
- group: company
  title: ''
  type: Website
  url: https://tripoto.com
created: '2026-07-17'
description: Tripoto is a travel community and trip-planning platform where travelers discover destinations, read and publish first-person travel itineraries and stories, and browse and book curated trips, tours, and experiences. Content is largely user-generated, with travel guides organized by destination, theme, and season. Tripoto was surfaced as a portfolio company of 500 Global and is tracked in the API Evangelist network. At the time of this profile no public developer API, OpenAPI specification, or developer portal was discoverable; an api.tripoto.com host exists but serves the consumer application backend.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tripoto-travel.png
layout: provider
modified: '2026-07-21'
name: Tripoto Travel
nav: Providers
network: true
overview: Tripoto Travel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Trip Planning, Tourism, and Travel Community.
random_paper: 14
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tripoto-travel/refs/heads/main/screenshots/tripoto-travel-2026-09-02T164249.png
security:
- kind: domain-security
  name: Tripoto Travel Domain Security
  slug: tripoto-travel-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tripoto-travel
tags:
- Company
- Travel
- Trip Planning
- Tourism
- Travel Community
- Itineraries
- User Generated Content
- India
website: https://tripoto.com
---
