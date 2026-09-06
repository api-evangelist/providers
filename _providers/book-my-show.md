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
- group: company
  title: ''
  type: Website
  url: https://in.bookmyshow.com
- group: operate
  title: ''
  type: Support
  url: https://support.bookmyshow.com/support/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://in.bookmyshow.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://in.bookmyshow.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/book-my-show-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/book-my-show-domain-security.yml
created: '2026-07-17'
description: BookMyShow (Bigtree Entertainment Pvt. Ltd.) is India's premier online entertainment ticketing platform, serving as a centralized hub for discovering and booking movies, live music festivals, comedy, theatre, sports, activities, and Video-on-Demand (VOD) streaming. For enterprise partners and event organizers it also provides venue management software, box-office point-of-sale solutions, corporate vouchers, gift cards, and end-to-end event production capabilities. Added to the API Evangelist network as a portfolio company of Accel; enriched by the enrichment pipeline. No public developer API or portal was found, but BookMyShow publishes an agent-facing llms.txt describing its consumer inventory hubs and B2B services.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/book-my-show.png
layout: provider
modified: '2026-07-18'
name: Book My Show
nav: Providers
network: true
overview: 'Book My Show is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Entertainment, Ticketing, and Movies.


  Book My Show''s developer surface includes support and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
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
  previous_composite: 10.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/book-my-show/refs/heads/main/screenshots/book-my-show-2026-07-25T203606.png
security:
- kind: domain-security
  name: Book My Show Domain Security
  slug: book-my-show-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: book-my-show
tags:
- Company
- Consumer
- Entertainment
- Ticketing
- Movies
- Live Events
- India
website: https://in.bookmyshow.com
---
