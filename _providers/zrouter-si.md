---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Unified AI model gateway API as documented.
  name: ZRouter API
  slug: zrouter-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/zrouter-si/plans/zrouter-si-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zrouter-si-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/zrouter-si/cli/zrouter-si-cli.yml
  title: ''
  type: CLI
  url: cli/zrouter-si-cli.yml
- group: auth
  href: https://artifacts.apis.io/zrouter-si/authentication/zrouter-si-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zrouter-si-authentication.yml
- group: agent
  href: https://artifacts.apis.io/zrouter-si/llms/zrouter-si-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zrouter-si-llms.txt
- group: agent
  href: https://artifacts.apis.io/zrouter-si/well-known/zrouter-si-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zrouter-si-well-known.yml
- group: other
  href: https://artifacts.apis.io/zrouter-si/hosts/zrouter-si-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zrouter-si-hosts.yml
- group: other
  href: https://artifacts.apis.io/zrouter-si/vendors/zrouter-si-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zrouter-si-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://zrouter.si/status
- group: auth
  href: https://artifacts.apis.io/zrouter-si/security/zrouter-si-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zrouter-si-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zrouter.si/
- group: docs
  title: ''
  type: Documentation
  url: https://zrouter.si/docs
- group: docs
  title: ''
  type: APIReference
  url: https://zrouter.si/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://zrouter.si/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://zrouter.si/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://zrouter.si/pricing
- group: start
  title: ''
  type: SignUp
  url: https://zrouter.si/login?mode=signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zrouter.si/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zrouter.si/privacy
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite probing known locations.
  evidence:
  - status: 200
    url: https://api.zrouter.si/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: ZRouter provides a unified API gateway for AI models, allowing developers to access chat, image, audio, and video capabilities through a single OpenAI‑compatible endpoint. It routes requests to multiple providers such as OpenAI, Anthropic, Gemini, DeepSeek, and Mistral, offering flexible model selection, budgeting, and usage monitoring. The platform includes tools for key management, BYOK, and detailed analytics, targeting developers building AI‑enhanced applications.
image: https://zrouter.si/website/assets/zrouter-social-card.jpg?v=c60067cc3ea2
layout: provider
modified: '2026-10-31'
name: zrouter-si
nav: Providers
network: true
overview: 'zrouter-si is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, API Gateway, OpenAI-Compatible, and Multi-Model.


  zrouter-si''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, pricing, and 11 more developer resources.'
plans:
- name: Zrouter Si Plans Pricing
  plan_count: 2
  slug: zrouter-si-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 31.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zrouter Si Authentication
  slug: zrouter-si-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Zrouter Si Domain Security
  slug: zrouter-si-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zrouter-si
tags:
- Company
- Artificial Intelligence
- API Gateway
- OpenAI-Compatible
- Multi-Model
website: https://zrouter.si/
---
