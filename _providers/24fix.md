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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://24x.co.th/
- group: company
  title: ''
  type: Blog
  url: https://fix.24x.co.th/blog
- group: operate
  title: ''
  type: Support
  url: https://24x.co.th/th/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://24x.co.th/th/term-condition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://24x.co.th/th/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/24fix-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/24fix-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/24fix-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/24fix-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 24 FIX is a Bangkok home-maintenance services operator whose only software is a consumer booking app; the words "API", "SDK", "developer" and "webhook" appear nowhere in the served HTML of any 24X property, every named /.well-known/ and spec path 404s on all seven operated hosts, and the single /api/ tree that exists is the fix.24x.co.th Next.js app's own internal routes, which its robots.txt disallows.
  evidence:
  - status: 404
    url: https://24x.co.th/openapi.json
  - status: 404
    url: https://fix.24x.co.th/openapi.json
  - status: 404
    url: https://24x.co.th/.well-known/api-catalog
  - status: 404
    url: https://fix.24x.co.th/.well-known/agent-card.json
  - status: 404
    url: https://24x.co.th/llms.txt
  - status: 404
    url: https://24x.co.th/apis.json
  - status: 200
    url: https://fix.24x.co.th/robots.txt
  - status: 200
    url: https://24fix.co/
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '24 FIX is the flagship consumer home-maintenance brand of 24 Solution Group (Thailand) Co., Ltd., founded in Bangkok in 2018 by six co-founders and now operating under the 24X umbrella brand. It runs an end-to-end property maintenance and home-solutions service rather than a matchmaking marketplace: air-conditioner cleaning and repair, washing-machine and appliance service, electrical and plumbing work, painting, cleaning, renovation and construction, delivered through an in-house managed ecosystem of more than 500 fixer teams and material vendor stores across Bangkok and the surrounding provinces, with expansion into Phuket and Singapore. The group fields four business lines — 24 FIX (consumer), 24 FIX for Business (commercial and facility maintenance, 500+ corporate customers), 24 House Solution, and 24 Projects (renovation and construction) — supported by an internal computerized maintenance management system that dispatches, tracks and quality-controls technician jobs.
  It raised a seed round in 2020, a pre-Series A from ECG Venture Capital in 2021, a 150 million THB Series A from Krungsri Finnovate, ECG Venture Capital and BCH Ventures in 2022, and a USD 5 million Series B from Wavemaker and Krungsri Finnovate in 2023. 24 FIX is a consumer and B2B services operator, not a software vendor: it publishes no developer portal, no API documentation, no SDKs and no machine-readable API contract, and the only /api/ path on its booking application is an internal Next.js route tree its own robots.txt disallows.'
image: https://24x.co.th/24fix/img/logo.svg
layout: provider
modified: '2026-09-05'
name: 24 FIX
nav: Providers
network: true
overview: '24 FIX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Services, Property Maintenance, Facility Management, and Field Service.


  24 FIX''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 24Fix Domain Security
  slug: 24fix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 24fix
tags:
- Company
- Home Services
- Property Maintenance
- Facility Management
- Field Service
- Marketplace
- Construction
- Renovation
- Consumer Services
- Thailand
- Southeast Asia
website: https://24x.co.th/
---
