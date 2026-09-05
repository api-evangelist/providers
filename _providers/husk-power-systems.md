---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/husk-power-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.huskpowersystems.com/
- group: company
  title: ''
  type: About
  url: https://www.huskpowersystems.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.huskpowersystems.com/News-and-Insights
- group: operate
  title: ''
  type: Support
  url: https://www.huskpowersystems.com/Contact-Us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.huskpowersystems.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.huskpowersystems.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HuskPowerSystems
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/husk-power-systems/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/huskpowersystem
- group: company
  title: ''
  type: Careers
  url: https://www.huskpowersystems.com/Careers
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.huskpowersystems.com/Investor-Relations
- group: other
  title: ''
  type: Listing
  url: https://forgeglobal.com/husk-power-systems_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/husk-power-systems-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Husk ships software only as end-user and operator products (the HUSKify customer app and the Husk Neuron operations dashboard); the corporate site has no developer, API or docs section anywhere in its sitemap, and every contract-discovery path on huskpowersystems.com returns 404.
  evidence:
  - status: 404
    url: https://www.huskpowersystems.com/openapi.json
  - status: 404
    url: https://www.huskpowersystems.com/llms.txt
  - status: 404
    url: https://www.huskpowersystems.com/api-docs
  - status: 404
    url: https://www.huskpowersystems.com/.well-known/agent-card.json
  - status: 200
    url: https://www.huskpowersystems.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Husk Power Systems is an energy technology company, founded in 2008 and headquartered in Fort Collins, Colorado with operating hubs in Patna, Mumbai and Pune (India) and Abuja (Nigeria), that builds, owns and operates AI-enabled distributed renewable energy systems — community solar minigrids, commercial and industrial solar, and residential rooftop — for unserved and underserved communities, businesses and households across Africa and Asia. Husk operates one of the largest minigrid fleets in the world and pairs it with pay-as-you-go smart metering, a customer mobile app (HUSKify) and an internal operations platform (Husk Neuron). Its software is delivered as end-user and operator products; Husk publishes no public developer program, API documentation, SDKs or machine-readable API specifications.
image: https://framerusercontent.com/images/KsxpwZXwI91nHN7Wq2bl2MvoGeU.png
layout: provider
modified: '2026-08-22'
name: Husk Power Systems
nav: Providers
network: true
overview: 'Husk Power Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Renewable Energy, Solar, and Distributed Energy Resources.


  Husk Power Systems'' developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/husk-power-systems/refs/heads/main/screenshots/husk-power-systems-2026-09-02T145801.png
security:
- kind: domain-security
  name: Husk Power Systems Domain Security
  slug: husk-power-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: husk-power-systems
tags:
- Company
- Energy
- Renewable Energy
- Solar
- Distributed Energy Resources
- Minigrids
- Electrification
- Smart Metering
- Africa
- India
- Nigeria
- Climate Tech
website: https://www.huskpowersystems.com/
---
