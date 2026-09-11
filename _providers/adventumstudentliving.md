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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://adventumstudentliving.com/
- group: company
  title: ''
  type: Blog
  url: https://uniacco.com/blog
- group: operate
  title: ''
  type: Support
  url: https://adventumstudentliving.com/company/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adventumstudentliving.com/company/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adventumstudentliving.com/company/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uniacco-tech
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adventumstudentliving-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adventumstudentliving-domain-security.yml
coverage:
  checked: '2026-09-09'
  detail: 'Adventum Student Living ships only consumer web products (UniAcco, UniCreds, UniScholars, UniFlx, UniEssential) and an invite-only partner dashboard at partner.uniacco.com whose backing host crm.uniacco.com is an internal CRM SPA serving robots.txt "Disallow: /" — there is no developer portal, API reference, or machine-readable contract on any of the seven company hosts probed.'
  evidence:
  - status: 404
    url: https://uniacco.com/openapi.json
  - status: 404
    url: https://adventumstudentliving.com/.well-known/api-catalog
  - status: 0
    url: https://api.uniacco.com/
  - status: 200
    url: https://uniacco.com/llms.txt
  - status: 200
    url: https://crm.uniacco.com/robots.txt
  reason: no-developer-program
  state: none
created: '2026-09-09'
description: 'Adventum Student Living Private Limited (ASL) is a Mumbai-headquartered study-abroad and student accommodation group founded in 2019 by Amit Singh, Anupam Gupta and Sayantan Biswas. It operates a family of consumer brands for internationally mobile students: UniAcco (a global purpose-built student accommodation marketplace covering the UK, Ireland, the United States, Canada, Australia and continental Europe), UniCreds (an education-loan marketplace), UniScholars (study-abroad counselling and admissions guidance), UniFlx (short-stay 1-12 week student housing) and UniEssential (arrival services such as airport transfers, guarantors, insurance and student bank accounts). ASL publishes consumer web properties and an invite-only partner dashboard for property owners, but as of this profile it publishes no public developer program, API reference or machine-readable contract.'
image: https://adventumstudentliving.com/favicon.ico
layout: provider
modified: '2026-09-09'
name: Adventum Student Living
nav: Providers
network: true
overview: 'Adventum Student Living is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Student Housing, Study Abroad, and Real Estate.


  Adventum Student Living''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: Adventumstudentliving Plans Pricing
  plan_count: 0
  slug: adventumstudentliving-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Adventumstudentliving Rate Limits
  slug: adventumstudentliving-rate-limits
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 6
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
    operational_transparency: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adventumstudentliving Domain Security
  slug: adventumstudentliving-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adventumstudentliving
tags:
- Company
- Education
- Student Housing
- Study Abroad
- Real Estate
- Marketplace
- Lending
- Travel
- India
- Consumer
website: https://adventumstudentliving.com/
---
