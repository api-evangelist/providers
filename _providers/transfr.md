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
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transfr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://transfrinc.com/
- group: company
  title: ''
  type: Blog
  url: https://transfrinc.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://transfrinc.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/transfr-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transfrinc.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://transfrinc.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.transfrinc.com/
- group: start
  title: ''
  type: Login
  url: https://dashboard.transfrinc.com/login
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/transfr-llms.txt
coverage:
  checked: '2026-08-30'
  detail: Transfr ships VR training only as an end-user product — its full sitemap contains no developer, API or integration page, its dashboard SPA bundle references no API host, and rostering/SSO is delegated to Clever, ClassLink and Canvas rather than to a Transfr API.
  evidence:
  - status: 200
    url: https://transfrinc.com/sitemap.xml
  - status: 404
    url: https://transfrinc.com/openapi.json
  - status: 404
    url: https://transfrinc.com/llms.txt
  - status: 404
    url: https://transfrinc.com/.well-known/api-catalog
  - status: 0
    url: https://api.transfrinc.com/
  reason: no-developer-program
  state: none
created: '2026-08-30'
description: Transfr Inc. is a New York City based workforce-education company that builds immersive virtual-reality job-training simulations for schools, colleges, workforce development boards, non-profits and justice-impacted programs. Its two products are Transfr Trek, a career-exploration program covering more than 150 occupations, and Transfr Train, hands-on VR skills training across sectors including manufacturing, healthcare, construction, automotive, aviation, diesel technology, electrical construction and hospitality. Learner and classroom data is administered through the Transfr dashboard, with rostering and single sign-on delivered through third-party education platforms (Clever, ClassLink, Canvas) rather than through a Transfr-published API. As of this profiling pass Transfr publishes no public developer program, API reference or machine-readable contract.
image: https://cdn.prod.website-files.com/695eb16b152dcf308e340d64/6983d1ad02da087c55e14cda_Favicon.svg
layout: provider
modified: '2026-08-30'
name: Transfr
nav: Providers
network: true
overview: 'Transfr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Workforce Development, Virtual Reality, and Training.


  Transfr''s developer surface includes engineering blog, pricing, support, and 7 more developer resources.'
plans:
- name: Transfr Plans Pricing
  plan_count: 3
  slug: transfr-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 5
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Transfr Domain Security
  slug: transfr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: transfr
tags:
- Company
- Education
- Workforce Development
- Virtual Reality
- Training
- Career Exploration
- EdTech
- Simulation
website: https://transfrinc.com/
---
