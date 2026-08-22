---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.5
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://thinkingmachines.ai
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
  url: https://tinker-docs.thinkingmachines.ai/tinker/api-reference/restclient/
- group: start
  title: ''
  type: GettingStarted
  url: https://tinker-docs.thinkingmachines.ai/cookbook/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://thinkingmachines.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thinking-machines-lab
- group: operate
  title: ''
  type: Support
  url: https://github.com/thinking-machines-lab/tinker-feedback
- group: commercial
  title: ''
  type: Pricing
  url: https://tinker-docs.thinkingmachines.ai/tinker/models/
- group: start
  title: ''
  type: SignUp
  url: https://auth.thinkingmachines.ai/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thinkingmachines.ai/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thinkingmachines.ai/legal/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thinkingmachines.ai
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/thinking-machines-lab-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://tinker-docs.thinkingmachines.ai/tinker/models/
- group: build
  title: ''
  type: Packages
  url: packages/thinking-machines-lab-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/thinking-machines-lab-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thinking-machines-lab-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/thinking-machines-lab-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thinking-machines-lab-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/thinking-machines-lab-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/thinking-machines-lab-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thinking-machines-lab-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thinking-machines-lab-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thinking-machines-lab-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thinking-machines-lab-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thinking-machines-lab-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thinking-machines-lab-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/thinking-machines-lab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://thinkingmachines.ai/security/disclosure-policy/
created: '2026-07-17'
description: 'Thinking Machines Lab is an AI research company (founded by Mira Murati) whose first product is Tinker — a cloud training API for researchers and developers. Tinker gives you full control over your data, algorithms, and models while it manages the GPU infrastructure: you author training loops locally with four primitives (forward_backward, optim_step, sample, save_state) and Tinker runs distributed LoRA fine-tuning across dense and Mixture-of-Experts models from 1B to 1T+ parameters. It supports SFT, reinforcement learning (GRPO, PPO), DPO, and distillation, shipped as an official Python SDK (tinker) plus the tinker-cookbook of recipes, a web console/playground, and OAuth 2.0 / OIDC authentication.'
image: https://thinkingmachines.ai/images/apple-touch-icon.png
layout: provider
modified: '2026-07-21'
name: Thinking Machines Lab
nav: Providers
network: true
overview: 'Thinking Machines Lab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Machine Learning, LLM, and Fine Tuning.


  Thinking Machines Lab''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 23 more developer resources.'
random_paper: 14
scopes:
- name: Thinking Machines Lab Scopes
  scope_count: 4
  slug: thinking-machines-lab-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode
score:
  band: thin
  composite: 36.0
  delta: 0.9
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 35.1
  provenance:
    conformance: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Thinking Machines Lab Authentication
  slug: thinking-machines-lab-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Thinking Machines Lab Domain Security
  slug: thinking-machines-lab-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Thinking Machines Lab Vulnerability Disclosure
  slug: thinking-machines-lab-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: thinking-machines-lab
tags:
- Company
- Ai
- Machine Learning
- LLM
- Fine Tuning
- Model Training
- Developer Tools
- Reinforcement Learning
website: https://thinkingmachines.ai
---
