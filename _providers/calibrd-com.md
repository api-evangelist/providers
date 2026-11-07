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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/calibrd-com/llms/calibrd-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calibrd-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/calibrd-com/well-known/calibrd-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calibrd-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/calibrd-com/hosts/calibrd-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calibrd-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/calibrd-com/vendors/calibrd-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calibrd-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.calibrd.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.calibrd.com/sign-up?redirect_url=%2Fworkspace
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.calibrd.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://www.calibrd.com/interview-prep/leadership
- group: auth
  href: https://artifacts.apis.io/calibrd-com/security/calibrd-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calibrd-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calibrd.com/
coverage:
  checked: '2026-11-03'
  detail: Provider's documentation is served as HTML pages without machine‑readable OpenAPI or other specs.
  evidence:
  - status: 200
    url: https://www.calibrd.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Calibrd provides a private AI interview coach for tech professionals, offering resume scoring, predicted interview questions, voice mock interviews, ATS checks, and compensation benchmarks. Users can compare up to three job postings against their resume for free, receive personalized feedback, and practice with realistic interview simulations. The platform emphasizes data privacy, encrypting user data at rest and allowing full deletion at any time. Founded by Xiaochen Guo, an ex‑Director of Engineering at King and Microsoft Gaming, Calibrd leverages a decade of hiring experience to help candidates prepare effectively for technical interviews.
image: https://www.calibrd.com/opengraph-image.png?67070a176e2eecde
layout: provider
modified: '2026-11-03'
name: Calibrd
nav: Providers
network: true
overview: 'Calibrd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Interview Coaching, Resume, and Hiring.


  Calibrd''s developer surface includes signup flow and 9 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calibrd Com Domain Security
  slug: calibrd-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: calibrd-com
tags:
- Company
- Artificial Intelligence
- Interview Coaching
- Resume
- Hiring
website: https://calibrd.com/
---
