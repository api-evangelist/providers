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
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.flixbus.com/
- group: company
  title: ''
  type: About
  url: https://corporate.flix.com/
- group: operate
  title: ''
  type: Support
  url: https://support.flixbus.com/global/en
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flix-tech
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/flix-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flix-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://global.flixbus.com/responsible-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flix-domain-security.yml
created: '2026-07-17'
description: Flix SE is a Munich-based global travel-tech company founded in 2013 that operates an asset-light, platform-based long-distance mobility network across more than 40 countries and 8,000+ destinations. Under the Flix umbrella it runs four consumer brands — FlixBus (green intercity coaches across Europe, North and South America, and Asia), FlixTrain (long-distance rail in Germany and Sweden), Greyhound (North America), and Kâmil Koç (Turkey) — having carried more than 500 million travelers. Flix pairs a technology and data-analytics platform with partner bus operators who run the physical fleet, selling and servicing trips through its consumer apps and website. Flix does not currently publish a public developer API or partner developer portal; its public technical surface is limited to a coordinated vulnerability-disclosure program (security.txt) and the flix-tech open-source GitHub organization. This profile was surfaced as an HV Capital portfolio company and enriched by the API
  Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flix.png
layout: provider
modified: '2026-07-19'
name: Flix
nav: Providers
network: true
overview: 'Flix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Transportation, Mobility, and Travel.


  Flix''s developer surface includes support and 8 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 7.7
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 7.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flix/refs/heads/main/screenshots/flix-2026-07-25T214807.png
security:
- kind: domain-security
  name: Flix Domain Security
  slug: flix-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Flix Vulnerability Disclosure
  slug: flix-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: flix
tags:
- Company
- Consumer
- Transportation
- Mobility
- Travel
- Bus
- Train
- Ground Transportation
website: https://www.flixbus.com/
---
