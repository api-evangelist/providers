---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The HTTP server started by `furiosa-llm serve <ARTIFACT_PATH>`. It hosts a single model on RNGD NPUs and exposes an OpenAI-compatible surface - /v1/completions, /v1/chat/completions, /v1/responses (Op
  name: Furiosa-LLM OpenAI-Compatible Server
  slug: furiosa-llm-openai-server
- baseURL: http://{furiosa_llm_host}:8000/v1
  baseurl_source: declared
  description: The Health API from FuriosaAI — 2 operation(s) for health.
  name: FuriosaAI Health API
  slug: furiosa-health-api
- baseURL: http://{furiosa_llm_host}:8000/v1
  baseurl_source: declared
  description: The Models API from FuriosaAI — 3 operation(s) for models.
  name: FuriosaAI Models API
  slug: furiosa-models-api
- baseURL: http://{furiosa_llm_host}:8000/v1
  baseurl_source: declared
  description: The Predict API API from FuriosaAI — 1 operation(s) for predict api.
  name: FuriosaAI Predict API
  slug: furiosa-predict-api-api
- baseURL: http://{furiosa_llm_host}:8000/v1
  baseurl_source: declared
  description: The Repository API from FuriosaAI — 3 operation(s) for repository.
  name: FuriosaAI Repository API
  slug: furiosa-repository-api
artifact_total: 14
common:
- group: other
  href: https://artifacts.apis.io/furiosa/capabilities/furiosa-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/furiosa-capability-edges.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/furiosa-ai/furiosa-sdk/blob/main/LICENSE
- group: other
  href: https://artifacts.apis.io/furiosa/overlays/furiosa-predict-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/furiosa-predict-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/furiosa/overlays/furiosa-model-repository-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/furiosa-model-repository-v2-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://furiosa.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.furiosa.ai/latest/en/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.furiosa.ai/latest/en/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.furiosa.ai/latest/en/furiosa_llm/reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.furiosa.ai/latest/en/get_started/furiosa_llm.html
- group: operate
  title: ''
  type: Support
  url: https://furiosa-ai.atlassian.net/servicedesk/customer/portals
- group: operate
  title: ''
  type: Community
  url: https://forums.furiosa.ai/
- group: company
  title: ''
  type: Blog
  url: https://furiosa.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/furiosa-ai
- group: operate
  title: ''
  type: Roadmap
  url: https://developer.furiosa.ai/latest/en/overview/roadmap.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.furiosa.ai/latest/en/whatsnew/index.html
- group: start
  title: ''
  type: SignUp
  url: https://lp.furiosa.ai/furiosa-access-program
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://furiosa.ai/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://furiosa.ai/contact
- group: build
  href: https://artifacts.apis.io/furiosa/packages/furiosa-packages.yml
  title: ''
  type: Packages
  url: packages/furiosa-packages.yml
- group: build
  href: https://artifacts.apis.io/furiosa/packages/furiosa-packages.yml
  title: ''
  type: SDKs
  url: packages/furiosa-packages.yml
- group: build
  href: https://artifacts.apis.io/furiosa/cli/furiosa-cli.yml
  title: ''
  type: CLI
  url: cli/furiosa-cli.yml
- group: start
  href: https://artifacts.apis.io/furiosa/sandbox/furiosa-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/furiosa-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/furiosa/authentication/furiosa-authentication.yml
  title: ''
  type: Authentication
  url: authentication/furiosa-authentication.yml
- group: design
  href: https://artifacts.apis.io/furiosa/conventions/furiosa-conventions.yml
  title: ''
  type: Conventions
  url: conventions/furiosa-conventions.yml
- group: design
  href: https://artifacts.apis.io/furiosa/errors/furiosa-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/furiosa-problem-types.yml
- group: design
  href: https://artifacts.apis.io/furiosa/lifecycle/furiosa-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/furiosa-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/furiosa/lifecycle/furiosa-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/furiosa-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/furiosa/conformance/furiosa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/furiosa-conformance.yml
- group: design
  href: https://artifacts.apis.io/furiosa/data-model/furiosa-data-model.yml
  title: ''
  type: DataModel
  url: data-model/furiosa-data-model.yml
- group: auth
  href: https://artifacts.apis.io/furiosa/security/furiosa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/furiosa-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/furiosa/llms/furiosa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/furiosa-llms.txt
- group: agent
  href: https://artifacts.apis.io/furiosa/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/furiosa/plans/furiosa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/furiosa-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/furiosa/rate-limits/furiosa-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/furiosa-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/furiosa/changelog/furiosa-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/furiosa-changelog.yml
created: '2026-08-16'
description: 'FuriosaAI is a South Korean semiconductor company that designs data-center AI inference chips and the software stack that runs on them. Its second-generation NPU, RNGD, implements a Tensor Contraction Processor architecture on TSMC 5nm and targets LLM, multi-modal and vision inference. The developer surface is software you run yourself rather than a hosted API: Furiosa-LLM ships an OpenAI-compatible server exposing chat, completions, responses, embeddings, score, rerank, models, tokenizer and Prometheus metrics endpoints, and the earlier Furiosa Model Server implements the KServe v2 Predict Protocol and the Triton Model Repository extension over REST and gRPC. Around that sit Python, Go and Rust packages, a furiosa-smi device CLI, container images, an APT/RPM package repository, and a Kubernetes cloud-native toolkit (device plugin, DRA driver, feature discovery, metrics exporter, NPU operator).'
finops:
- has_sources: true
  method: derived
  name: Furiosa Finops
  primary_unit: ''
  service_category: ''
  slug: furiosa-finops
  template: true
image: https://furiosa.ai/favicon.ico
layout: provider
modified: '2026-08-16'
name: FuriosaAI
nav: Providers
network: true
overview: 'FuriosaAI publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Models API, Predict API, and 2 more. Tagged areas include Artificial Intelligence, Machine Learning, Inference, Semiconductors, and NPU.


  The FuriosaAI catalog on APIs.io includes 1 Spectral governance ruleset.


  FuriosaAI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, signup flow, and 28 more developer resources.'
plans:
- name: Furiosa Plans Pricing
  plan_count: 0
  slug: furiosa-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Furiosa Rate Limits
  slug: furiosa-rate-limits
rules:
- authorship: generated
  effective_rule_count: 70
  extends:
  - spectral:oas
  name: FuriosaAI API Rules
  rule_count: 29
  severity_counts:
    error: 26
    hint: 0
    info: 2
    warn: 1
  slug: furiosa-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 31.8
    contract_quality: 36.3
    developer_ergonomics: 80.4
    discoverability: 73.2
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 45.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/furiosa/furiosa-2026-08-17T080944.png
security:
- kind: authentication
  name: Furiosa Authentication
  slug: furiosa-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Furiosa Domain Security
  slug: furiosa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: furiosa-llm-openai-client
  slug: furiosa-llm-openai-client
- name: furiosa-run-inference
  slug: furiosa-run-inference
- name: furiosa-serve-a-model
  slug: furiosa-serve-a-model
slug: furiosa
tags:
- Artificial Intelligence
- Machine Learning
- Inference
- Semiconductors
- NPU
- Hardware
- LLM
- Model Serving
- Kubernetes
- Developer Tools
- Compute
- Infrastructure
website: https://furiosa.ai/
---
