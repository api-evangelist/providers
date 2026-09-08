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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.adastec.com/
- group: company
  title: ''
  type: Blog
  url: https://www.adastec.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.adastec.com/company-contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adastec
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/600ad06ae00a6210fd3a2752/6508bba82a8174f84bc7f9ed_Website%20Privacy%20and%20Cookie%20Policy.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adastec/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/adasteccorp
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adastec-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adastec-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/adastec-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adastec-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adastec-llms.txt
coverage:
  checked: '2026-09-07'
  detail: ADASTEC markets an "Open API" as a component of flowride Cloud on its product page, but publishes no developer portal, API reference or contract of any kind — /developers, /api and /docs all 404 on adastec.com, there is no api. or docs. subdomain, the GitHub organization has zero public repositories, and the contact form is the only route to the platform.
  evidence:
  - status: 200
    url: https://www.adastec.com/flowride-ai
  - status: 404
    url: https://www.adastec.com/developers
  - status: 404
    url: https://www.adastec.com/api
  - status: 404
    url: https://www.adastec.com/.well-known/api-catalog
  reason: sales-gate
  state: gated
created: '2026-09-07'
description: ADASTEC Corp. is an automated-driving software company headquartered in East Lansing, Michigan, with offices in Helmond, Netherlands and Istanbul, Turkey. It develops flowride.ai, an SAE Level-4 automated driving software and sensor platform for full-size commercial vehicles — factory-fitted electric buses and minibuses operated on pre-mapped public-road routes. The platform is organized as flowride Drive (the on-vehicle automation stack and HMI connector), flowride Cloud (central control, data storage, data sharing and what the company markets as an Open API) and flowride Apps (remote management, command and control, a passenger application and analytics). Deployments run with transit operators and bus OEM partners including Karsan, Beep and Applied Autonomy across the United States, Sweden, Norway, Finland, Germany, Switzerland, the Netherlands, Romania and Turkey. ADASTEC is a premium member of the Autoware Foundation. No public developer portal, API reference or machine-readable
  contract is published for the flowride Cloud API.
image: https://cdn.prod.website-files.com/600ad06ae00a6210fd3a2752/60215786b6466708c00a9abf_Adastec_Logo_onlyA256X256.png
layout: provider
modified: '2026-09-07'
name: Adastec
nav: Providers
network: true
overview: 'Adastec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Autonomous Vehicles, Automated Driving, Public Transit, and Transportation.


  Adastec''s developer surface includes engineering blog, support, and 10 more developer resources.'
plans:
- name: Adastec Plans Pricing
  plan_count: 0
  slug: adastec-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  provenance:
    conformance: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adastec Domain Security
  slug: adastec-domain-security
  summary_line: TLSv1.3 · HSTS
slug: adastec
tags:
- Company
- Autonomous Vehicles
- Automated Driving
- Public Transit
- Transportation
- Mobility
- Fleet Management
- Automotive
- Robotics
website: https://www.adastec.com/
---
