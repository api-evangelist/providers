---
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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.aegfuels.com/
- group: company
  title: ''
  type: About
  url: https://www.aegfuels.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.aegfuels.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.aegfuels.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.aegfuels.com/enroll
- group: start
  title: ''
  type: Login
  url: https://app.aegfuels.com/toolbox/Login.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aegfuels.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.prod.website-files.com/67a659f9b80c35040b4d08ae/6813f3821e59ec07be1c4e8f_AEG%20General%20Terms%20and%20Conditions%20-%20May%202025.pdf
- group: company
  title: ''
  type: Careers
  url: https://www.aegfuels.com/careers
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aegfuels-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/aegfuels-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aegfuels-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aegfuels-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aegfuels-llms.txt
coverage:
  checked: '2026-09-09'
  detail: AEG Fuels ships end-user software only - the MILO client portal at app.aegfuels.com and the iOS/Android AEG Fuels Mobile apps for quoting and ordering fuel - and publishes no developer portal, API reference or machine-readable contract on any host, including the subdomains found in certificate transparency (paygateway, uplift, aegis/SAP, ai, dev).
  evidence:
  - status: 404
    url: https://www.aegfuels.com/openapi.json
  - status: 404
    url: https://www.aegfuels.com/developers
  - status: 404
    url: https://app.aegfuels.com/swagger/v1/swagger.json
  - status: 404
    url: https://www.aegfuels.com/.well-known/api-catalog
  - status: 500
    url: https://paygateway.aegfuels.com/swagger/v1/swagger.json
  - status: 404
    url: https://api.github.com/users/aegfuels
  reason: no-developer-program
  state: none
created: '2026-09-09'
description: 'AEG Fuels (Associated Energy Group, LLC) is a Miami, Florida-based global aviation fuel supply, logistics and trip-support company that has served commercial air carriers, business and general aviation operators, FBOs and government aircraft since 1988. It arranges jet fuel uplifts at more than 3,000 locations across 197 countries and layers ancillary services on top of supply: flight support (flight planning, ground handling, overflight and landing permits, on-site supervision, coordination of third-party services), fuel management for airlines, tax recovery and VAT exemption, a Sustainable Aviation Fuel (SAF) program, marine fuel and land fuel, the Carnet fuel card, the AEG Rewards loyalty program, and the AEG Connect network for FBOs and bulk fuel distribution. Customers transact through the company''s own MILO ordering platform - a browser client portal at app.aegfuels.com and iOS/Android apps for quoting, ordering, authorizing and reviewing fuel transactions. As of this
  profile AEG Fuels publishes no public developer program, API reference or machine-readable contract; the digital surface is an end-user product, not a platform.'
image: https://cdn.prod.website-files.com/67a659f9b80c35040b4d08ae/67a659f9b80c35040b4d0c34_662674c090a942af1f6146b7_logo_header.svg
layout: provider
modified: '2026-09-09'
name: AEG Fuels
nav: Providers
network: true
overview: 'AEG Fuels is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aviation, Aviation Fuel, Fuel, and Energy.


  AEG Fuels'' developer surface includes engineering blog, support, signup flow, and 11 more developer resources.'
plans:
- name: Aegfuels Plans Pricing
  plan_count: 0
  slug: aegfuels-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Aegfuels Rate Limits
  slug: aegfuels-rate-limits
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aegfuels Domain Security
  slug: aegfuels-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aegfuels
tags:
- Company
- Aviation
- Aviation Fuel
- Fuel
- Energy
- Logistics
- Supply Chain
- Flight Support
- Sustainable Aviation Fuel
- Marine Fuel
- Transportation
- Business Aviation
website: https://www.aegfuels.com/
---
