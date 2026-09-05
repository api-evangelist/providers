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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/compass-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/compass-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/urbancompass
- group: company
  title: ''
  type: Website
  url: https://www.compass.com
- group: other
  title: ''
  type: Customers
  url: https://www.compass.com/agents/
- group: other
  title: ''
  type: Resources
  url: https://www.compass.com/concierge/
- group: company
  title: ''
  type: Blog
  url: https://www.compass.com/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.compass.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.compass.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/compass-inc-
- group: company
  title: ''
  type: Blog
  url: https://www.compass.com/newsroom/
created: '2026-05-04'
description: Compass is a leading real estate technology company headquartered in New York City that provides a tech-enabled brokerage platform connecting agents, buyers, and sellers across the United States. The company combines residential real estate services with proprietary software for agents, including marketing, client management, and listing tools. Compass does not currently publish a public developer API portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/compass.png
layout: provider
modified: '2026-05-04'
name: Compass
nav: Providers
network: true
overview: 'Compass is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, Brokerage, PropTech, and Fortune 500.


  Compass'' developer surface includes engineering blog and 10 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 19.0
    catalog_earned_first_party: 0.0
    catalog_gap: 96.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 35.2
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.2
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 26.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Compass Domain Security
  slug: compass-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Compass Vulnerability Disclosure
  slug: compass-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: compass
tags:
- Real-Estate
- Brokerage
- PropTech
- Fortune 500
website: https://www.compass.com
---
