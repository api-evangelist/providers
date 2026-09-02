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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bizzycar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bizzycar.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bizzycar.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.bizzycar.com/support
- group: start
  title: ''
  type: Login
  url: https://www.portal.bizzycar.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bizzycar.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bizzycar.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bizzycar
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bizzycar-llms.txt
coverage:
  checked: '2026-08-07'
  detail: api.bizzycar.com is live but is BizzyCar's own application backend, not a product — every contract path (/openapi.json, /swagger.json, /api-docs, /graphql) returns the app's Rails JSON 404 envelope, none of the 238 URLs in the sitemap is a developer, docs or API page, and there is no bizzycar GitHub org or package on any registry; BizzyCar sells the DMS connectors it consumes, not an API it exposes.
  evidence:
  - status: 404
    url: https://api.bizzycar.com/openapi.json
  - status: 404
    url: https://api.bizzycar.com/graphql
  - status: 200
    url: https://www.bizzycar.com/sitemap.xml
  - status: 404
    url: https://api.github.com/orgs/bizzycar
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: 'BizzyCar is a B2B SaaS platform for automotive dealerships that automates service recall management, customer outreach and mobile service. Founded in 2018 and headquartered in Saint Peters, Missouri, the company ingests VIN-level open-recall data from OEM partners, matches it against a dealer''s market area and DMS records, then uses AI-driven outreach (SMS, email, voice) to book service appointments and dispatch mobile service vans. Products include Recall Outreach, Recall Scout, Recall Radar, Service Engine, Mobile Service and Fleet IQ. BizzyCar is primarily an API *consumer* rather than an API producer: it ships pre-built connectors into dealer management systems (Dealertrack, DMS Plus, Open/Mate, Asbury, PBS, Tekion, Fortellis, Reynolds & Reynolds) and service schedulers (Xtime, TCC, DealerFX, Affinitiv, Update Promise), but publishes no public developer program, API reference or machine-readable contract of its own.'
image: https://www.bizzycar.com/hubfs/1.%201200x630.png
layout: provider
modified: '2026-08-07'
name: BizzyCar
nav: Providers
network: true
overview: 'BizzyCar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Recall Management, Dealerships, and Mobile Service.


  BizzyCar''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bizzycar/refs/heads/main/screenshots/bizzycar-2026-08-07T162605.png
security:
- kind: domain-security
  name: Bizzycar Domain Security
  slug: bizzycar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bizzycar
tags:
- Company
- Automotive
- Recall Management
- Dealerships
- Mobile Service
- Vehicle Service
- Fleet Management
- Scheduling
- Software-as-a-Service
website: https://www.bizzycar.com/
---
