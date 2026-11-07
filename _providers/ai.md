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
api_count: 1
apis:
- description: AI Worker platform API providing access to automation of IT tasks.
  name: AI Worker
  slug: ai-worker
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/ai/hosts/ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ai/security/ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai.work/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ai.work/
- group: docs
  title: ''
  type: APIReference
  url: https://www.ai.work/ai-worker
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ai.work/request-access
- group: operate
  title: ''
  type: Support
  url: https://www.ai.work/support
- group: company
  title: ''
  type: Blog
  url: https://www.ai.work/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ai.work/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ai.work/policies/privacy-policy
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at any discovered host.
  evidence:
  - status: 404
    url: https://api.ai.work/openapi.json
  - status: 404
    url: https://api.ai.work/openapi.yaml
  - status: 404
    url: https://api.ai.work/swagger.json
  - status: 404
    url: https://api.ai.work/v1/openapi.json
  - status: 308
    url: https://ai.work/openapi.json
  - status: 308
    url: https://ai.work/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: ai.work provides an AI‑powered worker platform that automates repetitive IT tasks, integrates with enterprise tools like ServiceNow, Okta, Slack, and HubSpot, and accelerates service delivery. The solution enables teams to delegate routine processes to a digital assistant, improving speed, accuracy, and cost efficiency across IT operations and HR workflows.
image: https://framerusercontent.com/images/YHK2n3fdCoURo2Mp4NLbthuK8M.png
layout: provider
modified: '2026-10-19'
name: ai.work
nav: Providers
network: true
overview: 'ai.work is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, IT, and Enterprise.


  ai.work''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 5 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 16.7
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
screenshot: https://apis.io/screenshots/ai/ai-2026-11-03T120638.png
security:
- kind: domain-security
  name: Ai Domain Security
  slug: ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ai
tags:
- Company
- Artificial Intelligence
- Automation
- IT
- Enterprise
website: https://ai.work/
---
