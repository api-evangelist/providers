---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Managed training/fine-tuning and sampling API for open-weight language models, consumed through the official Tinker Python SDK and CLI. Supports SFT, RL, and distillation workflows, checkpoint managem
  name: Tinker API
  slug: tinker-api
artifact_total: 4
common:
- group: auth
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
  title: ''
  type: SDKs
  url: packages/thinking-machines-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/thinking-machines-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/thinking-machines-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thinking-machines-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thinking-machines-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thinking-machines-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thinking-machines-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thinking-machines-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/thinking-machines-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://tinker-docs.thinkingmachines.ai/changelog/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thinking-machines-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://tinker-docs.thinkingmachines.ai/tinker/model-deprecations/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thinking-machines-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thinking-machines-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/thinking-machines-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/thinking-machines-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/thinking-machines-vulnerability-disclosure.yml
created: '2026-07-17'
description: Thinking Machines Lab is an artificial intelligence research and product company building tools to make AI systems more widely understood, customizable, and generally capable. Its flagship developer product is Tinker, a managed API with an official Python SDK and CLI for fine-tuning and sampling open-weight language models (supervised fine-tuning, reinforcement learning, and distillation), alongside Inkling, an open-weights model. The Tinker platform exposes ServiceClient, TrainingClient, SamplingClient, and RestClient interfaces plus OpenAI- and Anthropic-compatible inference endpoints, governed by a project-scoped permission model.
image: https://thinkingmachines.ai/images/home.png
layout: provider
modified: '2026-07-21'
name: Thinking Machines
nav: Providers
network: true
overview: 'Thinking Machines publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Fine-Tuning, and LLM.


  Thinking Machines'' developer surface includes documentation, API reference, quickstart, signup flow, support, engineering blog, CLI, and 22 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 34.7
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thinking-machines/refs/heads/main/screenshots/thinking-machines-2026-09-02T163529.png
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
- Machine-Learning
- Fine-Tuning
- LLM
- Model Training
- Developer Tools
website: https://thinkingmachines.ai/
---
