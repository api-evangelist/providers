---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-17'
api_count: 0
artifact_total: 4
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clean-energy-fuels/refs/heads/main/security/clean-energy-fuels-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clean-energy-fuels-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clean-energy-fuels-corp
- group: company
  title: ''
  type: Blog
  url: https://cleanenergyfuels.com/feed
- group: company
  title: ''
  type: Website
  url: https://cleanenergyfuels.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clean-energy-fuels/refs/heads/main/llms/clean-energy-fuels-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clean-energy-fuels-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://cleanenergyfuels.com/customer-service
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cleanenergyfuels.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleanenergyfuels.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://cleanenergyfuels.com/about-us/newsroom
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.cleanenergyfuels.com/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ce_renewables
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/CENatGas
coverage:
  checked: '2026-09-17'
  detail: Clean Energy Fuels is a renewable-natural-gas producer and fueling-station operator whose public surface is a WordPress marketing site, a Q4 investor site and a React station locator; the api.cleanenergyfuels.com and developer.cleanenergyfuels.com hosts the prior scaffolded record named do not resolve in DNS (NXDOMAIN), every /openapi.json, /graphql, /.well-known/* and agent-card path on cleanenergyfuels.com, www and investors 404s (negative control 404s too), stations.cleanenergyfuels.com answers 500 for every non-root path, no GitHub org or npm/PyPI package exists, and the station locator reads its data from a static allstations.json in a contractor's (KMicro-Tech) GitHub repo rather than a company-served API. The customer fuel-card portal named in llms.txt has no public link or docs.
  evidence:
  - note: NXDOMAIN
    status: 0
    url: https://api.cleanenergyfuels.com/
  - note: NXDOMAIN
    status: 0
    url: https://developer.cleanenergyfuels.com/docs
  - status: 404
    url: https://cleanenergyfuels.com/openapi.json
  - status: 404
    url: https://cleanenergyfuels.com/.well-known/agent-card.json
  - status: 404
    url: https://cleanenergyfuels.com/.well-known/clean-energy-fuels-negative-control-9c1f2a7e.json
  - status: 500
    url: https://stations.cleanenergyfuels.com/openapi.json
  - status: 200
    url: https://cleanenergyfuels.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/cleanenergyfuels
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Clean Energy Fuels Corp. (Nasdaq: CLNE) is North America''s largest provider of renewable natural gas (RNG) for the transportation industry. It produces RNG at dairy-farm and landfill facilities and delivers it as CNG or LNG through a network of more than 600 fueling stations across the United States and Canada, alongside hydrogen fueling, bulk LNG and turnkey fleet services. The company publishes no developer program, public API, SDK or machine-readable contract; its only machine-readable surface is an llms.txt at the apex domain and a React station locator that reads static JSON from a contractor''s GitHub repository.'
finops:
- name: Clean Energy Fuels Finops
  service_category: Energy / Fueling
  slug: clean-energy-fuels-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clean-energy-fuels.png
layout: provider
modified: '2026-09-17'
name: Clean Energy Fuels
nav: Providers
network: true
overview: 'Clean Energy Fuels is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Natural Gas, Renewables, Transportation, Renewable Natural Gas, and Hydrogen.


  Clean Energy Fuels'' developer surface includes engineering blog, support, YouTube channel, and 9 more developer resources.'
plans:
- name: Clean Energy Fuels Plans Pricing
  plan_count: 1
  slug: clean-energy-fuels-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Clean Energy Fuels Rate Limits
  slug: clean-energy-fuels-rate-limits
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.7
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 5.3
  previous_composite: 9.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/clean-energy-fuels/refs/heads/main/screenshots/clean-energy-fuels-2026-06-20T174450.png
security:
- kind: domain-security
  name: Clean Energy Fuels Domain Security
  slug: clean-energy-fuels-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clean-energy-fuels
tags:
- Natural Gas
- Renewables
- Transportation
- Renewable Natural Gas
- Hydrogen
- Fleet Fueling
- LNG
- Energy
website: https://cleanenergyfuels.com
---
