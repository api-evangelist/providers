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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-21'
api_count: 1
apis:
- description: 'The public Esri ArcGIS Online feature-service catalog Hawaiian Electric serves under tenant gfBpz2hbsVDgru6D. Twenty-three FeatureServers are shared publicly and answer anonymous queries: the External'
  name: Hawaiian Electric Grid Data (ArcGIS REST Feature Services)
  slug: hawaiian-electric-grid-data-arcgis-rest-feature-services
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hawaiian-electric-industries/refs/heads/main/security/hawaiian-electric-industries-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hawaiian-electric-industries-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hawaiianelectricindustries
- group: company
  title: ''
  type: Website
  url: https://www.hei.com/
- group: other
  title: ''
  type: Subsidiary
  url: https://www.hawaiianelectric.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.hei.com/investor-relations/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.hei.com/news/
- group: other
  title: ''
  type: Sustainability
  url: https://www.hei.com/sustainability/
- group: other
  title: ''
  type: Subsidiary
  url: https://pacificcurrenthawaii.com/
- group: other
  title: ''
  type: SECFilings
  url: https://www.hei.com/investor-relations/reports-and-filings/default.aspx
- group: operate
  title: ''
  type: ContactUs
  url: https://www.hei.com/investor-relations/contact-us/default.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hawaiianelectric.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hawaiianelectric.com/privacy-notice/customer-information-privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.hawaiianelectric.com/about-us/newsroom
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hawaiian-electric-industries/refs/heads/main/llms/hawaiian-electric-industries-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hawaiian-electric-industries-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hawaiian-electric-industries/refs/heads/main/packages/hawaiian-electric-industries-packages.yml
  title: ''
  type: Packages
  url: packages/hawaiian-electric-industries-packages.yml
created: '2026-03-24'
description: 'Hawaiian Electric Industries (HEI) is a Honolulu-based holding company whose principal subsidiary, Hawaiian Electric, delivers electricity to roughly 95% of Hawaii''s residents through three operating utilities — Hawaiian Electric (Oahu), Hawaii Electric Light (Hawaii Island) and Maui Electric (Maui County) — alongside Pacific Current, its clean-energy and sustainability investment arm. HEI runs no developer program and publishes no OpenAPI, SDK or MCP server. It does serve one real, anonymously callable machine-readable surface: a public Esri ArcGIS REST feature-service catalog carrying the Locational Value Maps, published grid needs and EV charging locations that its own hawaiianelectric.com map applications consume.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hawaiian-electric-industries.png
layout: provider
modified: '2026-09-13'
name: Hawaiian Electric Industries
nav: Providers
network: true
overview: 'Hawaiian Electric Industries publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Utilities, Electricity, Grid, and Holding Company.


  Hawaiian Electric Industries'' developer surface includes engineering blog and 14 more developer resources.'
plans:
- name: Hawaiian Electric Industries Plans Pricing
  plan_count: 0
  slug: hawaiian-electric-industries-plans-pricing
press:
- date: ''
  title: Hawaiian Electric Industries Inc. has sold over 90% of its ...
  url: https://www.facebook.com/staradvertiser/posts/hawaiian-electric-industries-inc-has-sold-over-90-of-its-subsidiary-american-sav/977490881142703/
- date: ''
  title: Hawaiian Electric Industries, Inc. (HE) Q3 2025 Earnings ...
  url: https://seekingalpha.com/article/4840645-hawaiian-electric-industries-inc-he-q3-2025-earnings-call-transcript
- date: ''
  title: Hawaiian Electric Industries (NYSE:HE) - Stock Analysis
  url: https://simplywall.st/stocks/us/utilities/nyse-he/hawaiian-electric-industries
- date: ''
  title: Hawaiian Electric Continues to Advance Wildfire Safety ...
  url: https://www.hei.com/investor-relations/news-and-events/news/news-details/2024/Hawaiian-Electric-Continues-to-Advance-Wildfire-Safety-Efforts/default.aspx
- date: ''
  title: 'Wall Street Recap: Can Hawaiian Electric Industries Inc. (HWI) stock ...'
  url: https://www.fitnessatfive.com/ati-del/258/Can-Hawaiian-Electric-Industries-Inc.-(HWI)-stock-sustain-institutional-flows
random_paper: 5
rate_limits:
- limit_count: 3
  name: Hawaiian Electric Industries Rate Limits
  slug: hawaiian-electric-industries-rate-limits
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 75.9
    operational_transparency: 31.6
  previous_composite: 26.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/hawaiian-electric-industries/refs/heads/main/screenshots/hawaiian-electric-industries-2026-06-20T182541.png
security:
- kind: authentication
  name: Hawaiian Electric Industries Authentication
  slug: hawaiian-electric-industries-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Hawaiian Electric Industries Domain Security
  slug: hawaiian-electric-industries-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hawaiian-electric-industries
tags:
- Energy
- Utilities
- Electricity
- Grid
- Holding Company
- Hawaii
- Fortune 1000
- Geospatial
- ArcGIS
- Open Data
- Locational Value Map
- EV Charging
website: https://www.hei.com/
---
