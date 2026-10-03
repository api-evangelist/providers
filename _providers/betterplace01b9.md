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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Betterplace provides a learning platform API (details not publicly documented).
  name: Betterplace API
  slug: betterplace-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/betterplace01b9/refs/heads/main/plans/betterplace01b9-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/betterplace01b9-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betterplace01b9/refs/heads/main/hosts/betterplace01b9-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betterplace01b9-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.betterplace.com/terms-of-service/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.betterplace.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://www.betterplace.com/login/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/betterplace01b9/refs/heads/main/security/betterplace01b9-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betterplace01b9-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.betterplace.com
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI or other machine‑readable contract found on api.betterplace.com or documentation pages.
  evidence:
  - status: dns_error
    url: https://api.betterplace.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Betterplace01b9 is a learning platform that provides AI‑powered tools for educators to create, deliver, and experience courses. It offers a suite of services including instant course generation, adaptive learning, and a marketplace for instructors. The platform aims to make education more accessible, scalable, and personalized for learners worldwide.
layout: provider
modified: '2026-09-28'
name: Betterplace01b9
nav: Providers
network: true
overview: 'Betterplace01b9 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Artificial Intelligence, Learning Platform, Courses, and Technology.


  Betterplace01b9''s developer surface includes pricing and 6 more developer resources.'
plans:
- name: Betterplace01B9 Plans Pricing
  plan_count: 3
  slug: betterplace01b9-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Betterplace01B9 Domain Security
  slug: betterplace01b9-domain-security
  summary_line: TLSv1.2
slug: betterplace01b9
tags:
- Education
- Artificial Intelligence
- Learning Platform
- Courses
- Technology
- Company
website: https://www.betterplace.com
---
