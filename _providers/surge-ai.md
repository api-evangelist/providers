---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Surge Ai Agentic Access
  operation_count: 18
  slug: surge-ai-agentic-access
  summary_line: 18 operations · 10 acting
api_count: 14
apis:
- description: Surge's REST API for managing labeling projects, tasks, and results. Endpoints cover projects (list, retrieve, create, download results, save reports in multiple formats), tasks (create, list, retriev
  name: Surge API
  slug: surge-api
- description: Official Python SDK (surge-api on PyPI) wrapping the Surge API. Requires Python 3.10+, MIT-licensed, and last updated May 2026. Configured via surge.api_key or the SURGE_API_KEY environment variable.
  name: Surge Python SDK
  slug: surge-python-sdk
- description: Surge's product surface for delivering complex reinforcement-learning environments and agents that challenge and evaluate agentic models.
  name: Surge RL Environments and Agents
  slug: surge-rl-environments
- description: Scoring rubrics and automated verifiers for grading AI outputs across domains.
  name: Surge Rubrics and Verifiers
  slug: surge-rubrics-verifiers
- description: Preference and reward data for reinforcement learning from human feedback.
  name: Surge RLHF
  slug: surge-rlhf
- description: Foundational-skill demonstration data for supervised fine-tuning.
  name: Surge SFT
  slug: surge-sft
- description: Quality assessment of AI outputs by Surge's expert workforce.
  name: Surge Human Evaluation
  slug: surge-human-evaluation
- description: Image, audio, and video data collection and labeling.
  name: Surge Multimodal Data
  slug: surge-multimodal
- description: Multilingual data across 70+ languages for localization, translation, and multilingual model evaluation.
  name: Surge Internationalization
  slug: surge-internationalization
- description: Pre-built datasets ready for licensing and download.
  name: Surge Off-The-Shelf Data
  slug: surge-off-the-shelf-data
- description: The world's largest open social-media toxicity dataset, published under MIT license.
  name: Surge Toxicity Dataset
  slug: surge-toxicity-dataset
- description: The Projects API from Surge AI — 9 operation(s) for projects.
  name: Surge AI Projects API
  slug: surge-ai-projects-api
- description: The Tasks API from Surge AI — 5 operation(s) for tasks.
  name: Surge AI Tasks API
  slug: surge-ai-tasks-api
- description: The Teams API from Surge AI — 1 operation(s) for teams.
  name: Surge AI Teams API
  slug: surge-ai-teams-api
artifact_total: 44
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Surge AI Projects API
  slug: open-surge-ai-projects-api
- collection_type: open
  name: Surge AI Projects Tasks API
  slug: open-surge-ai-tasks-api
- collection_type: open
  name: Surge AI Projects Teams API
  slug: open-surge-ai-teams-api
- collection_type: open
  name: Surge AI API
  slug: open-surge-ai
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/surge-ai/surge-python/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/surge-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/surge-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/surge-ai-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.surgehq.ai
- group: docs
  title: ''
  type: Documentation
  url: https://app.surgehq.ai/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://app.surgehq.ai/docs/api
- group: auth
  title: ''
  type: Authentication
  url: https://app.surgehq.ai/docs/api
- group: start
  title: ''
  type: Signup
  url: https://app.surgehq.ai/customers/sign_in
- group: start
  title: ''
  type: Console
  url: https://app.surgehq.ai
- group: build
  title: ''
  type: SDKs
  url: https://github.com/surge-ai/surge-python
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/surge-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/surge-ai
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/surge-ai/toxicity
- group: company
  title: ''
  type: Blog
  url: https://www.surgehq.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.surgehq.ai
- group: other
  title: ''
  type: X
  url: https://x.com/HelloSurgeAI
created: '2026-05-23'
description: Surge AI is a human-data company that provides large-scale, expert-quality labeled data for training and evaluating frontier AI models. The product surface spans RL environments and agents (rich, complex environments that challenge agentic models), rubrics and verifiers (scoring systems for AI outputs), RLHF (preference and reward data), SFT (foundational skill demonstrations), human evaluation, expert professional domains, internationalization across 70+ languages, multimodal (image, audio, video) data, and off-the-shelf datasets. Surge ships an official Python SDK (surge-python) wrapping the Surge API, with API-key authentication, and exposes the dashboard and API reference at app.surgehq.ai. Public datasets published by Surge include the toxicity dataset (the world's largest social-media toxicity dataset).
features:
- description: Endpoints for projects, tasks, and blueprints, with API-key authentication.
  name: Surge REST API
- description: Official surge-python SDK on PyPI, MIT-licensed, Python 3.10+.
  name: Python SDK
- description: Complex environments that challenge agentic models.
  name: RL Environments and Agents
- description: Scoring systems for AI outputs across domains.
  name: Rubrics and Verifiers
- description: Preference, reward, and demonstration data for foundation-model training.
  name: RLHF and SFT
- description: Expert workforce grades AI output quality.
  name: Human Evaluation
- description: Specialized expertise across finance, law, medicine, and more.
  name: Expert Professional Domains
- description: Internationalization coverage spanning more than 70 languages.
  name: 70+ Languages
- description: Image, audio, and video collection and labeling.
  name: Multimodal Data
- description: Pre-built datasets available for licensing.
  name: Off-The-Shelf Datasets
- description: Public releases including the world's largest social-media toxicity dataset.
  name: Open Datasets
finops:
- name: Surge Ai Finops
  service_category: API
  slug: surge-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surge-ai.png
integrations:
- description: Programmatic integration via the official surge-python SDK.
  name: Python SDK
- description: Standard API-key auth (SURGE_API_KEY env var or programmatic configuration).
  name: API Key Authentication
- description: Use Surge blueprints as templates for new labeling projects.
  name: Custom Project Blueprints
layout: provider
modified: '2026-05-23'
name: Surge AI
nav: Providers
network: true
overview: 'Surge AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Projects API, Tasks API, and Teams API. Tagged areas include Human Data, RLHF, SFT, Rubrics, and Verifiers.


  Surge AI''s developer surface includes authentication, developer portal, documentation, API reference, signup flow, developer console, engineering blog, and 10 more developer resources.'
plans:
- name: Surge Ai Plans Pricing
  plan_count: 1
  slug: surge-ai-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 2
  name: Surge Ai Rate Limits
  slug: surge-ai-rate-limits
score:
  band: developing
  composite: 42.8
  delta: -0.2
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 59.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/surge-ai/refs/heads/main/screenshots/surge-ai-2026-06-20T194733.png
security:
- kind: authentication
  name: Surge Ai Authentication
  slug: surge-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Surge Ai Domain Security
  slug: surge-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: surge-ai
tags:
- Human Data
- RLHF
- SFT
- Rubrics
- Verifiers
- RL Environments
- Multimodal
- Internationalization
- Labeling
use_cases:
- description: Preference and reward data for reinforcement learning from human feedback.
  name: Frontier Model RLHF
- description: Demonstration data for SFT across professional domains.
  name: Supervised Fine-Tuning
- description: Benchmark agents in complex RL environments with structured rubrics.
  name: Agentic Evals
- description: Evaluate model quality across 70+ languages.
  name: Multilingual Model Evaluation
- description: Use the toxicity dataset and human evaluation pipelines for trust and safety work.
  name: Trust and Safety Research
website: https://www.surgehq.ai
---
