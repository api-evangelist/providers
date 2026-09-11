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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/diamondback-energy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/diamondbackenergy
- group: company
  title: ''
  type: Website
  url: https://www.diamondbackenergy.com
- group: company
  title: ''
  type: Blog
  url: https://www.diamondbackenergy.com/investors/press-releases
- group: company
  title: ''
  type: BlogRSS
  url: https://www.diamondbackenergy.com/rss/news-releases.xml
- group: operate
  title: ''
  type: Support
  url: https://www.diamondbackenergy.com/contact-us/overview
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.diamondbackenergy.com/site-info/privacy-policy
coverage:
  checked: '2026-09-06'
  detail: Diamondback is a Permian Basin oil and gas producer whose entire web presence is a Q4/gcs-web investor-relations site with no developer section; owner joint-interest billing and revenue check detail are handed off to the third-party EnergyLink portal, and no api. or developer. subdomain resolves in DNS.
  evidence:
  - status: 200
    url: https://www.diamondbackenergy.com/
  - status: 404
    url: https://www.diamondbackenergy.com/api-docs
  - status: 404
    url: https://www.diamondbackenergy.com/.well-known/api-catalog
  - status: 403
    url: https://www.diamondbackenergy.com/.well-known/agent-card.json
  - status: 403
    url: https://www.diamondbackenergy.com/openapi.json
  - status: 200
    url: https://www.diamondbackenergy.com/owner-relations
  reason: not-a-software-company
  state: none
created: '2026-03-21'
description: Diamondback Energy is an independent oil and natural gas company focused on the acquisition, development, exploration, and exploitation of unconventional, onshore oil and natural gas reserves in the Permian Basin of West Texas. As a Fortune 500 company in the upstream energy sector, Diamondback publishes no developer portal, no API, and no machine-readable contract of any kind; its entire web presence is a Q4/gcs-web investor-relations site, and owner joint-interest billing and revenue check detail are delivered through the third-party EnergyLink portal rather than a first-party interface. The only machine-readable surfaces it serves are three RSS feeds on the IR platform — news releases, events and SEC filings. This repository is maintained as a placeholder for any APIs, developer tools, or machine-readable artifacts that may emerge.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/diamondback-energy.png
layout: provider
modified: '2026-09-06'
name: Diamondback Energy
nav: Providers
network: true
overview: 'Diamondback Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Oil and Gas, Fortune 500, Permian Basin, and Upstream.


  Diamondback Energy''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 10.8
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Diamondback Energy Domain Security
  slug: diamondback-energy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: diamondback-energy
tags:
- Energy
- Oil and Gas
- Fortune 500
- Permian Basin
- Upstream
- Exploration and Production
- Natural Gas
- Investor Relations
website: https://www.diamondbackenergy.com
---
