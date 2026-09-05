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
  url: https://xocean.com/
- group: company
  title: ''
  type: About
  url: https://xocean.com/company/
- group: other
  title: ''
  type: Services
  url: https://xocean.com/data-as-a-service/
- group: company
  title: ''
  type: Careers
  url: https://xocean.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://xocean.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://xocean.com/contact/
- group: operate
  title: ''
  type: ContactUs
  url: https://xocean.com/imprint/
- group: company
  title: ''
  type: BlogFeed
  url: https://xocean.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xocean.com/terms-and-conditions/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://xocean.com/disclaimer/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xocean.com/privacy-statement-eu-2/
- group: commercial
  title: ''
  type: Privacy
  url: https://xocean.com/cookie-policy-eu-2/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://xocean.com/supplier-code-of-conduct/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xocean/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/xoceansocial
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/xoceansocial/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xocean-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/xocean-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xocean-llms.txt
coverage:
  checked: '2026-09-04'
  detail: XOCEAN sells ocean survey data as contracted project deliverables rather than as a programmable product — xocean.com is a 22-page WordPress marketing site with no /developers, /api or /docs section, api./docs./developer.xocean.com do not exist in DNS, there is no xocean GitHub organization, and the only machine-readable surface on the domain is the CMS's own stock /wp-json/ REST root; the CyberDeck cloud platform named on the technology page is the internal console XOCEAN's own pilots use to fly the USVs, not a customer-facing API.
  evidence:
  - status: 404
    url: https://xocean.com/openapi.json
  - status: 404
    url: https://xocean.com/llms.txt
  - status: 404
    url: https://xocean.com/.well-known/agent-card.json
  - status: 404
    url: https://xocean.com/.well-known/api-catalog
  - status: 404
    url: https://api.github.com/orgs/xocean
  - status: 200
    url: https://xocean.com/wp-json/
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: XOCEAN is an Irish ocean-data company, founded in 2017 and headquartered at the Rathcor Technical Centre in Co. Louth, Ireland, with offices in the UK, US, Canada, Norway and Australia and over 240 staff. It collects turnkey marine data using a fleet of low-carbon Uncrewed Surface Vessels (USVs) piloted over satellite from onshore operations centres, carrying multibeam echosounder, sub-bottom profiler, side-scan sonar, magnetometer and USBL payloads for seabed mapping, geophysical survey and environmental monitoring. Its customers are offshore wind developers, subsea cable operators, national hydrographic offices, oil and gas operators and carbon capture and storage projects, and its proprietary CyberDeck cloud environment monitors and controls the fleet in real time. XOCEAN sells survey data as a service — project deliverables, not a programmable product — and publishes no public API, developer portal, SDK or machine-readable contract of any kind.
image: https://xocean.com/wp-content/uploads/2023/01/icon.png
layout: provider
modified: '2026-09-04'
name: XOCEAN
nav: Providers
network: true
overview: 'XOCEAN is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ocean Data, Marine Survey, Hydrography, and Uncrewed Surface Vessels.


  XOCEAN''s developer surface includes support, privacy policy, and 17 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: domain-security
  name: Xocean Domain Security
  slug: xocean-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xocean
tags:
- Company
- Ocean Data
- Marine Survey
- Hydrography
- Uncrewed Surface Vessels
- Marine Robotics
- Offshore Wind
- Seabed Mapping
- Bathymetry
- Geospatial
- Environmental Monitoring
- Subsea Cables
- Carbon Capture and Storage
- Blue Economy
- Ireland
website: https://xocean.com/
---
