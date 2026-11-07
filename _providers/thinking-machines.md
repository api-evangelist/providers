---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Managed training/fine-tuning and sampling API for open-weight language models, consumed through the official Tinker Python SDK and CLI. Supports SFT, RL, and distillation workflows, checkpoint managem
  name: Tinker API
  slug: tinker-api
artifact_total: 6
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://tinker-docs.thinkingmachines.ai/tinker/models/models_and_pricing/
- group: commercial
  href: https://artifacts.apis.io/thinking-machines/plans/thinking-machines-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thinking-machines-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://thinkingmachines.ai/blog/index.xml
- group: auth
  href: https://artifacts.apis.io/thinking-machines/security/thinking-machines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thinking-machines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thinkingmachines.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tinker-docs.thinkingmachines.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://tinker-docs.thinkingmachines.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://tinker-docs.thinkingmachines.ai/tinker/api-reference/
- group: start
  title: ''
  type: Quickstart
  url: https://tinker-docs.thinkingmachines.ai/tinker/quickstart/
- group: start
  title: ''
  type: SignUp
  url: https://tinker.thinkingmachines.ai/
- group: operate
  title: ''
  type: Support
  url: https://tinker-docs.thinkingmachines.ai/support/
- group: company
  title: ''
  type: Blog
  url: https://thinkingmachines.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thinking-machines-lab
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thinkingmachines.ai/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thinkingmachines.ai/legal/privacy/
- group: build
  href: https://artifacts.apis.io/thinking-machines/packages/thinking-machines-packages.yml
  title: ''
  type: SDKs
  url: packages/thinking-machines-packages.yml
- group: build
  href: https://artifacts.apis.io/thinking-machines/packages/thinking-machines-packages.yml
  title: ''
  type: Packages
  url: packages/thinking-machines-packages.yml
- group: build
  href: https://artifacts.apis.io/thinking-machines/cli/thinking-machines-cli.yml
  title: ''
  type: CLI
  url: cli/thinking-machines-cli.yml
- group: auth
  href: https://artifacts.apis.io/thinking-machines/authentication/thinking-machines-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thinking-machines-authentication.yml
- group: design
  href: https://artifacts.apis.io/thinking-machines/conventions/thinking-machines-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thinking-machines-conventions.yml
- group: design
  href: https://artifacts.apis.io/thinking-machines/data-model/thinking-machines-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thinking-machines-data-model.yml
- group: design
  href: https://artifacts.apis.io/thinking-machines/errors/thinking-machines-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thinking-machines-problem-types.yml
- group: design
  href: https://artifacts.apis.io/thinking-machines/conformance/thinking-machines-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thinking-machines-conformance.yml
- group: operate
  href: https://artifacts.apis.io/thinking-machines/changelog/thinking-machines-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/thinking-machines-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://tinker-docs.thinkingmachines.ai/changelog/
- group: design
  href: https://artifacts.apis.io/thinking-machines/lifecycle/thinking-machines-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thinking-machines-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://tinker-docs.thinkingmachines.ai/tinker/model-deprecations/
- group: agent
  href: https://artifacts.apis.io/thinking-machines/llms/thinking-machines-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thinking-machines-llms.txt
- group: agent
  href: https://artifacts.apis.io/thinking-machines/well-known/thinking-machines-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thinking-machines-well-known.yml
- group: auth
  href: https://artifacts.apis.io/thinking-machines/well-known/thinking-machines-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thinking-machines-security.txt
- group: auth
  href: https://artifacts.apis.io/thinking-machines/security/thinking-machines-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/thinking-machines-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/thinking-machines/security/thinking-machines-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/thinking-machines-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: APIReference
  url: https://tinker-docs.thinkingmachines.ai/tinker/api-reference/restclient/
created: '2026-07-17'
description: Thinking Machines Lab is an artificial intelligence research and product company building tools to make AI systems more widely understood, customizable, and generally capable. Its flagship developer product is Tinker, a managed API with an official Python SDK and CLI for fine-tuning and sampling open-weight language models (supervised fine-tuning, reinforcement learning, and distillation), alongside Inkling, an open-weights model. The Tinker platform exposes ServiceClient, TrainingClient, SamplingClient, and RestClient interfaces plus OpenAI- and Anthropic-compatible inference endpoints, governed by a project-scoped permission model.
finops:
- has_sources: true
  method: derived
  name: Thinking Machines Finops
  primary_unit: million tokens (sample)
  service_category: ''
  slug: thinking-machines-finops
  template: false
image: https://thinkingmachines.ai/images/home.png
layout: provider
modified: '2026-10-06'
name: Thinking Machines
nav: Providers
network: true
overview: 'Thinking Machines is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, Fine-Tuning, and LLM.


  Thinking Machines'' developer surface includes pricing, documentation, API reference, quickstart, signup flow, support, engineering blog, and 26 more developer resources.'
plans:
- name: Thinking Machines Plans Pricing
  plan_count: 11
  slug: thinking-machines-plans-pricing
random_paper: 17
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 73.2
    operational_transparency: 36.8
  previous_composite: 43.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/thinking-machines/thinking-machines-2026-09-02T163529.png
security:
- kind: authentication
  name: Thinking Machines Authentication
  slug: thinking-machines-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Thinking Machines Domain Security
  slug: thinking-machines-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Thinking Machines Vulnerability Disclosure
  slug: thinking-machines-vulnerability-disclosure
  summary_line: contact published
slug: thinking-machines
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Fine-Tuning
- LLM
- Model Training
- Developer Tools
- Foundation Models
- Reinforcement Learning
website: https://thinkingmachines.ai/
---
