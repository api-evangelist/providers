---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.3
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emmi-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://emmi.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://noether-docs.emmi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://noether-docs.emmi.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://noether-docs.emmi.ai/autoapi/noether/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://noether-docs.emmi.ai/tutorials/getting_started_install_and_verify.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Emmi-AI
- group: company
  title: ''
  type: Blog
  url: https://emmi.ai/news
- group: operate
  title: ''
  type: Support
  url: https://emmi.ai/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emmi.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emmi.ai/imprint
- group: build
  title: ''
  type: Packages
  url: packages/emmi-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/emmi-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/emmi-ai-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/emmi-ai-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/emmi-ai-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/emmi-ai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://emmi.ai/security-compliance
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/emmi-ai-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/emmi-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/emmi-ai-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/emmi-ai-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/emmi-ai-robots.txt
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Emmi-AI/noether
- group: commercial
  title: ''
  type: License
  url: https://raw.githubusercontent.com/Emmi-AI/noether/main/LICENSE.txt
coverage:
  checked: '2026-08-17'
  detail: 'Emmi AI ships an open-source Python framework (emmiai-noether) and a CLI that run on the customer''s own CPU/GPU/SLURM hardware - there is no hosted service and no API: no api./app./platform./console./mcp. host resolves under emmi.ai, and every contract-discovery probe (openapi.json, agent-card.json, agent.json, every /.well-known/ path on both emmi.ai and noether-docs.emmi.ai) returned 404 or NXDOMAIN.'
  evidence:
  - status: 404
    url: https://emmi.ai/openapi.json
  - status: 404
    url: https://emmi.ai/.well-known/agent-card.json
  - status: 404
    url: https://noether-docs.emmi.ai/.well-known/agent.json
  - status: 404
    url: https://emmi.ai/api
  - status: 200
    url: https://pypi.org/pypi/emmiai-noether/json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Emmi AI is an Austrian engineering-AI company building Large Engineering Models (LEMs) - pre-trained, physics-accurate neural networks that replace traditional CAE/CFD solvers to deliver real-time, GPU-accelerated simulation and design validation for manufacturing, aerospace, semiconductor, and energy engineering. Its flagship open-source Noether framework (the emmiai-noether PyTorch package) provides transformer building blocks, a model/dataset/recipe zoo, and a command-line toolchain for training, fine-tuning, and deploying industrial physics models, alongside vertical products such as NeuralWing (aircraft wing validation), NeuralMould (injection moulding), and NeuralDEM (particulate flows). Emmi AI was acquired by Mistral AI in May 2026 to build an industrial AI stack.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emmi-ai.png
layout: provider
modified: '2026-08-17'
name: Emmi Ai
nav: Providers
network: true
overview: 'Emmi Ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Engineering AI, Physics Simulation, Machine-Learning, and Deep Learning.


  Emmi Ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, changelog, and 19 more developer resources.'
plans:
- name: Emmi Ai Plans Pricing
  plan_count: 0
  slug: emmi-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Emmi Ai Rate Limits
  slug: emmi-ai-rate-limits
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 31.0
  provenance:
    conformance: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emmi-ai/refs/heads/main/screenshots/emmi-ai-2026-07-25T213243.png
security:
- kind: domain-security
  name: Emmi Ai Domain Security
  slug: emmi-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Emmi Ai Trust Center
  slug: emmi-ai-trust-center
  summary_line: SOC 2 Type 2
slug: emmi-ai
tags:
- Company
- Engineering AI
- Physics Simulation
- Machine-Learning
- Deep Learning
- Scientific Computing
- CAE
- CFD
- Manufacturing
- Open-Source
website: https://emmi.ai
---
