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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/studeo/hosts/studeo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/studeo-hosts.yml
- group: other
  href: https://artifacts.apis.io/studeo/vendors/studeo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/studeo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://studeo.app/legal/terms-and-conditions
- group: auth
  href: https://artifacts.apis.io/studeo/security/studeo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/studeo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://studeo.app
- group: company
  title: ''
  type: Blog
  url: https://studeo.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://studeo.app/upgrade
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider’s API host or documentation pages.
  evidence:
  - status: error
    url: https://api.studeo.app/openapi.json
  - status: 404
    url: https://studeo.app/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Studeo is an AI‑powered educational platform that helps students boost their grades in subjects like Maths, Sciences, English, French, and SES. Leveraging generative avatar professors, the app offers personalized tutoring, interactive lessons, and adaptive learning paths, aiming to make studying more engaging and effective for learners worldwide.
image: https://studeo.app/api/og
layout: provider
modified: '2026-10-29'
name: Studeo
nav: Providers
network: true
overview: 'Studeo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, AI, Tutoring, PersonalizedLearning, and SaaS.


  Studeo''s developer surface includes engineering blog, pricing, and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Studeo Domain Security
  slug: studeo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: studeo
tags:
- Education
- AI
- Tutoring
- PersonalizedLearning
- SaaS
- Company
website: https://studeo.app
---
