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
- group: company
  title: ''
  type: Website
  url: https://www.bloxbuilt.com/
- group: company
  title: ''
  type: About
  url: https://www.bloxbuilt.com/about
- group: other
  title: ''
  type: Products
  url: https://www.bloxbuilt.com/products
- group: company
  title: ''
  type: News
  url: https://www.bloxbuilt.com/news
- group: company
  title: ''
  type: Careers
  url: https://www.bloxbuilt.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.bloxbuilt.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloxbuilt.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloxbuilt.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BLOXBuilt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blox-domain-security.yml
coverage:
  checked: '2026-08-07'
  detail: BLOX manufactures prefabricated healthcare buildings — its product ships on a truck, and bloxbuilt.com has no /developers, /docs or /api path at all (the site's own 404 handler answers each one), while the BLOXBuilt GitHub org's five public repos are internal 2016 Revit/portal projects, four of them empty.
  evidence:
  - status: 404
    url: https://www.bloxbuilt.com/developers
  - status: 404
    url: https://www.bloxbuilt.com/openapi.json
  - status: 404
    url: https://www.bloxbuilt.com/llms.txt
  - status: 404
    url: https://www.bloxbuilt.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/BLOXBuilt/repos
  reason: not-a-software-company
  state: none
created: '2026-08-07'
description: BLOX is a Bessemer, Alabama design-manufacture-construct (DMC) company that describes itself as the largest manufacturer of healthcare buildings in the United States. Founded in 2010-2011 as a spinoff of Giattina Aycock Architecture Studio by Chris Giattina, BLOX designs, prefabricates and installs modular medical buildings and building components — freestanding emergency departments, acute-care patient-room modules, primary-care clinics and full hospitals — from a former Pullman Standard railcar plant in the Interstate Industrial Park. Customers include HCA Healthcare, Encompass Health, Universal Health Services and Walmart Health. The company is privately held and its shares appear on secondary-market venues such as Forge Global. BLOX publishes no developer program, no public API, and no machine-readable specification; its software work is internal tooling for the DMC delivery system rather than a product.
image: https://avatars.githubusercontent.com/u/22823827?v=4
layout: provider
modified: '2026-08-07'
name: Blox
nav: Providers
network: true
overview: 'Blox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Modular Construction, Prefabrication, and Manufacturing.


  Blox''s developer surface includes product news and 9 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blox/refs/heads/main/screenshots/blox-2026-08-07T162639.png
security:
- kind: domain-security
  name: Blox Domain Security
  slug: blox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blox
tags:
- Company
- Construction
- Modular Construction
- Prefabrication
- Manufacturing
- Healthcare Facilities
- Architecture
- Building Technology
website: https://www.bloxbuilt.com/
---
