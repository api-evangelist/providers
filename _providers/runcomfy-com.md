---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: RunComfy provides a cloud platform for ComfyUI with APIs for image generation, workflow automation, and model management. Documentation is at https://docs.runcomfy.com/.
  name: RunComfy API
  slug: runcomfy-api
artifact_total: 5
asyncapis:
- description: ''
  name: Runcomfy Com Webhooks
  slug: runcomfy-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/runcomfy-com/plans/runcomfy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/runcomfy-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/runcomfy-com/asyncapi/runcomfy-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/runcomfy-com-webhooks.yml
- group: build
  href: https://artifacts.apis.io/runcomfy-com/cli/runcomfy-com-cli.yml
  title: ''
  type: CLI
  url: cli/runcomfy-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/runcomfy-com/authentication/runcomfy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/runcomfy-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/runcomfy-com/llms/runcomfy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/runcomfy-com-llms.txt
- group: other
  href: https://artifacts.apis.io/runcomfy-com/a2a/runcomfy-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/runcomfy-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/runcomfy-com/well-known/runcomfy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/runcomfy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/runcomfy-com/hosts/runcomfy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/runcomfy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/runcomfy-com/vendors/runcomfy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/runcomfy-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.runcomfy.net`
- group: auth
  href: https://artifacts.apis.io/runcomfy-com/security/runcomfy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/runcomfy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://runcomfy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runcomfy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.runcomfy.com/comfyui-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.runcomfy.com/serverless/quickstart.md
- group: commercial
  title: ''
  type: Pricing
  url: https://www.runcomfy.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.runcomfy.com/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.runcomfy.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://docs.runcomfy.com/integrations/postman.md
coverage:
  checked: '2026-10-31'
  detail: No public OpenAPI or other machine‑readable contract was found despite documentation pages.
  evidence:
  - status: 404
    url: https://docs.runcomfy.com/openapi.json
  - status: 0
    url: https://api.runcomfy.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: RunComfy provides a cloud platform for ComfyUI, offering fast GPU‑accelerated AI image generation and workflow automation via scalable APIs. Users can run, train, and deploy ComfyUI workflows without setup, leveraging on‑demand GPU resources, model libraries, and a serverless environment. The service targets creators, artists, and developers seeking zero‑ops AI tooling.
layout: provider
modified: '2026-10-31'
name: RunComfy
nav: Providers
network: true
overview: 'RunComfy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Cloud, Image Generation, Workflow Automation, and ComfyUI.


  The RunComfy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  RunComfy''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, pricing, and 13 more developer resources.'
plans:
- name: Runcomfy Com Plans Pricing
  plan_count: 2
  slug: runcomfy-com-plans-pricing
random_paper: 23
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 40.5
    discoverability: 53.6
    operational_transparency: 7.9
  previous_composite: 39.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/runcomfy-com/runcomfy-com-2026-11-03T142531.png
security:
- kind: authentication
  name: Runcomfy Com Authentication
  slug: runcomfy-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Runcomfy Com Domain Security
  slug: runcomfy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: runcomfy-com
tags:
- Artificial Intelligence
- Cloud
- Image Generation
- Workflow Automation
- ComfyUI
website: https://runcomfy.com/
---
