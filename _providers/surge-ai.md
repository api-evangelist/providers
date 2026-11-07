---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Surge Ai Agentic Access
  operation_count: 18
  slug: surge-ai-agentic-access
  summary_line: 18 operations · 10 acting
api_count: 1
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
- baseURL: https://app.surgehq.ai/api
  baseurl_source: declared
  description: The Projects API from Surge AI — 9 operation(s) for projects.
  name: Surge AI Projects API
  slug: surge-ai-projects-api
- baseURL: https://app.surgehq.ai/api
  baseurl_source: declared
  description: The Tasks API from Surge AI — 5 operation(s) for tasks.
  name: Surge AI Tasks API
  slug: surge-ai-tasks-api
- baseURL: https://app.surgehq.ai/api
  baseurl_source: declared
  description: The Teams API from Surge AI — 1 operation(s) for teams.
  name: Surge AI Teams API
  slug: surge-ai-teams-api
artifact_total: 55
collections:
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
- group: other
  href: https://artifacts.apis.io/surge-ai/capabilities/surge-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/surge-ai-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/surge-ai/rules/surge-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/surge-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/surge-ai/json-ld/surge-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/surge-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/surge-ai/vocabulary/surge-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/surge-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/surge-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/surge-ai/data-model/surge-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/surge-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/surge-ai/conventions/surge-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/surge-ai-conventions.yml
- group: operate
  href: https://artifacts.apis.io/surge-ai/lifecycle/surge-ai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/surge-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/surge-ai/lifecycle/surge-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/surge-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/surge-ai/conformance/surge-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/surge-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/surge-ai/overlays/surge-ai-projects-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/surge-ai-projects-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/surge-ai/hosts/surge-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/surge-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/surge-ai/vendors/surge-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/surge-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/surge-ai/packages/surge-ai-packages.yml
  title: ''
  type: Packages
  url: packages/surge-ai-packages.yml
- group: commercial
  href: https://artifacts.apis.io/surge-ai/finops/surge-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/surge-ai-finops.yml
- group: company
  title: ''
  type: Website
  url: https://surgehq.ai/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/surge-ai/surge-python/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/surge-ai/surge-python/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/surge-ai/agentic-access/surge-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/surge-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/surge-ai/security/surge-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/surge-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/surge-ai/authentication/surge-ai-authentication.yml
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
  url: https://surgehq.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://surgehq.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://surgehq.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.surgehq.ai/
- group: docs
  title: ''
  type: Guides
  url: https://surgehq.ai/guides
- group: start
  title: ''
  type: Login
  url: https://app.surgehq.ai/customers/sign_in
- group: company
  title: ''
  type: Careers
  url: https://surgehq.ai/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/surge-ai/
- group: other
  title: ''
  type: X
  url: https://x.com/HelloSurgeAI
coverage:
  checked: '2026-10-27'
  detail: Surge's API reference at app.surgehq.ai/docs/api redirects to app.surgehq.ai/customers/sign_in, so the only public description of the API is the open-source surge-python SDK.
  evidence:
  - status: 200
    url: https://app.surgehq.ai/docs/api
  - status: 404
    url: https://app.surgehq.ai/openapi.json
  - status: 404
    url: https://app.surgehq.ai/api/openapi.json
  reason: customer-only-docs
  state: gated
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
- has_sources: false
  method: generated
  name: Surge Ai Finops
  primary_unit: ''
  service_category: API
  slug: surge-ai-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surge-ai.png
integrations:
- description: Programmatic integration via the official surge-python SDK.
  name: Python SDK
- description: Standard API-key auth (SURGE_API_KEY env var or programmatic configuration).
  name: API Key Authentication
- description: Use Surge blueprints as templates for new labeling projects.
  name: Custom Project Blueprints
json_schemas:
- name: ProjectCreate
  property_count: 4
  slug: surge-ai-project-create
- name: Project
  property_count: 4
  slug: surge-ai-project
- name: ProjectUpdate
  property_count: 3
  slug: surge-ai-project-update
- name: TaskCreate
  property_count: 1
  slug: surge-ai-task-create
- name: Task
  property_count: 4
  slug: surge-ai-task
- name: Team
  property_count: 2
  slug: surge-ai-team
jsonld:
- class_count: 6
  name: Surge Ai Context
  property_count: 10
  slug: surge-ai-context
layout: provider
modified: '2026-10-27'
name: Surge AI
nav: Providers
network: true
overview: 'Surge AI publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Projects API, Tasks API, Teams API, and 11 more. Tagged areas include Human Data, RLHF, SFT, Rubrics, and Verifiers.


  The Surge AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Surge AI''s developer surface includes authentication, developer portal, documentation, API reference, signup flow, developer console, engineering blog, and 34 more developer resources.'
plans:
- name: Surge Ai Plans Pricing
  plan_count: 0
  slug: surge-ai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Surge Ai Rate Limits
  slug: surge-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Surge AI API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: surge-ai-rules
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 58.9
    developer_ergonomics: 58.9
    discoverability: 57.1
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 0.0
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/surge-ai/surge-ai-2026-06-20T194733.png
security:
- kind: authentication
  name: Surge Ai Authentication
  slug: surge-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Surge Ai Domain Security
  slug: surge-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: collect-task-responses
  slug: surge-ai-collect-task-responses
- name: create-and-launch-a-labeling-project
  slug: surge-ai-create-and-launch-a-labeling-project
- name: manage-project-lifecycle
  slug: surge-ai-manage-project-lifecycle
- name: seed-gold-standards
  slug: surge-ai-seed-gold-standards
slug: surge-ai
tags:
- Human Data
- RLHF
- SFT
- Rubrics
- Verifiers
- RL Environments
- Multi-Modal
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
website: https://surgehq.ai/
---
