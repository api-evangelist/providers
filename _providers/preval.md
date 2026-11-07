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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/preval/hosts/preval-hosts.yml
  title: ''
  type: Hosts
  url: hosts/preval-hosts.yml
- group: other
  href: https://artifacts.apis.io/preval/vendors/preval-vendors.yml
  title: ''
  type: Vendors
  url: vendors/preval-vendors.yml
- group: build
  href: https://artifacts.apis.io/preval/packages/preval-packages.yml
  title: ''
  type: SDKs
  url: packages/preval-packages.yml
- group: build
  href: https://artifacts.apis.io/preval/packages/preval-packages.yml
  title: ''
  type: Packages
  url: packages/preval-packages.yml
- group: auth
  href: https://artifacts.apis.io/preval/security/preval-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/preval-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://preval.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://preval.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://preval.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://preval.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://preval.dev/privacy
- group: start
  title: ''
  type: SignUp
  url: https://preval.dev/login
coverage:
  checked: '2026-10-18'
  detail: The developer portal and documentation URLs (https://preval.dev/ and https://docs.preval.dev) return 404, indicating no accessible API program.
  evidence:
  - status: 404
    url: https://docs.preval.dev
  reason: no-developer-program
  state: none
created: '2026-10-18'
description: Preval provides AI agent observability platform that traces, evaluates, and optimizes large language model agents in production. It captures LLM calls, voice transcriptions, tool executions, and offers automated metrics, PII detection, prompt optimization, and a unified playground. Users can monitor agents across regions, get real‑time insights, and improve reliability before release.
layout: provider
modified: '2026-10-18'
name: Preval
nav: Providers
network: true
overview: 'Preval is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Observability, Monitoring, and LLM.


  Preval''s developer surface includes pricing, signup flow, and 9 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 16.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/preval/preval-2026-11-03T141511.png
security:
- kind: domain-security
  name: Preval Domain Security
  slug: preval-domain-security
  summary_line: TLSv1.3 · HSTS
slug: preval
tags:
- Company
- Artificial Intelligence
- Observability
- Monitoring
- LLM
website: https://preval.dev/
---
