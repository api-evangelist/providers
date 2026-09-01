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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tractive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://tractive.com/en/l/vulnerability-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tractive-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tractive-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tractive-security.txt
- group: company
  title: ''
  type: Website
  url: https://tractive.com/
- group: company
  title: ''
  type: Blog
  url: https://tractive.com/blog/en
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tractive
- group: build
  title: ''
  type: Packages
  url: packages/tractive-packages.yml
created: '2026-07-17'
description: Tractive is an Austrian pet-technology company, founded in October 2012 in Pasching, Austria and led by CEO Michael Hurnaus, that builds GPS location and health-monitoring trackers for dogs and cats. Its collar-attached devices (such as the DOG and CAT GPS trackers) pair with a subscription mobile app to deliver real-time worldwide location, virtual fences, activity, sleep and, more recently, resting heart-rate and respiratory-rate health intelligence to more than 1.4 million active subscribers. Tractive was acquired by Italy's Bending Spoons in 2026. Tractive does NOT publish a public developer API, SDK, or developer portal — its backend HTTP API (api.tractive.com) is private to its own apps; the only clients are unofficial, community reverse-engineered libraries. This profile enriches the company's identity for the API Evangelist network; there is no official API surface to catalog.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tractive.png
layout: provider
modified: '2026-07-21'
name: Tractive
nav: Providers
network: true
overview: 'Tractive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pet Technology, GPS Tracking, IoT, and Location.


  Tractive''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 6.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Tractive Domain Security
  slug: tractive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tractive Vulnerability Disclosure
  slug: tractive-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tractive
tags:
- Company
- Pet Technology
- GPS Tracking
- IoT
- Location
- Wearables
- Consumer Hardware
- Health Monitoring
website: https://tractive.com/
---
