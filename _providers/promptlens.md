---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: PromptLens Product API providing prompt retrieval and management via OAuth.
  name: PromptLens API
  slug: promptlens-api
artifact_total: 5
asyncapis:
- description: ''
  name: Promptlens Webhooks
  slug: promptlens-webhooks
common:
- group: other
  href: https://artifacts.apis.io/promptlens/vendors/promptlens-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptlens-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/promptlens/plans/promptlens-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/promptlens-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/promptlens/vocabulary/promptlens-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/promptlens-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/promptlens/asyncapi/promptlens-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/promptlens-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/promptlens/authentication/promptlens-authentication.yml
  title: ''
  type: Authentication
  url: authentication/promptlens-authentication.yml
- group: design
  href: https://artifacts.apis.io/promptlens/conformance/promptlens-conformance.yml
  title: ''
  type: Conformance
  url: conformance/promptlens-conformance.yml
- group: agent
  href: https://artifacts.apis.io/promptlens/llms/promptlens-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/promptlens-llms.txt
- group: agent
  href: https://artifacts.apis.io/promptlens/well-known/promptlens-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/promptlens-well-known.yml
- group: other
  href: https://artifacts.apis.io/promptlens/hosts/promptlens-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptlens-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.promptlens.io/auth/sign-up?redirect_url=/prompts/new
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/promptlens-io
- group: auth
  href: https://artifacts.apis.io/promptlens/security/promptlens-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptlens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptlens.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.promptlens.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.promptlens.io/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.promptlens.io/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://www.promptlens.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.promptlens.io/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.promptlens.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.promptlens.io/terms
- group: docs
  title: ''
  type: Documentation
  url: https://www.promptlens.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.promptlens.io/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.promptlens.io/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://www.promptlens.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.promptlens.io/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.promptlens.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.promptlens.io/terms
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://promptlens.io/openapi.json
  - status: null
    url: https://www.promptlens.io/openapi.json
  - status: 401
    url: https://app.promptlens.io/mcp
  - status: 200
    url: https://promptlens.io/
  reason: partner-login
  state: gated
created: '2026-10-18'
description: PromptLens provides a platform to catch AI regressions before production. It enables engineers to test prompts and model changes against real cases, preventing faulty outputs from reaching users. Features include versioned prompt testing, integration with major LLM providers, and detailed observability of prompt behavior across deployments.
image: https://www.promptlens.io/brand/logo-accent-black.svg
layout: provider
modified: '2026-10-18'
name: PromptLens
nav: Providers
network: true
overview: 'PromptLens is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Monitoring, Testing, and LLM.


  The PromptLens catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PromptLens'' developer surface includes authentication, signup flow, documentation, API reference, getting-started guide, pricing, support, and 20 more developer resources.'
plans:
- name: Promptlens Plans Pricing
  plan_count: 3
  slug: promptlens-plans-pricing
random_paper: 4
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 50.3
    catalog_earned_first_party: 12.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 53.9
    contract_governance: 8.3
    contract_quality: 39.0
    developer_ergonomics: 28.6
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 45.2
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/promptlens/promptlens-2026-11-03T141614.png
security:
- kind: authentication
  name: Promptlens Authentication
  slug: promptlens-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Promptlens Domain Security
  slug: promptlens-domain-security
  summary_line: TLSv1.3 · DMARC
slug: promptlens
tags:
- Company
- Artificial Intelligence
- Monitoring
- Testing
- LLM
- Observability
website: https://promptlens.io/
---
