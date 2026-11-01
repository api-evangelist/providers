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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Priorlabs Agentic Access
  operation_count: 7
  slug: priorlabs-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.priorlabs.ai
  baseurl_source: declared
  description: The Prediction API from Prior Labs — 3 operation(s) for prediction.
  name: Prior Labs Prediction API
  slug: priorlabs-prediction-api
- baseURL: https://api.priorlabs.ai
  baseurl_source: declared
  description: The Training API from Prior Labs — 4 operation(s) for training.
  name: Prior Labs Training API
  slug: priorlabs-training-api
artifact_total: 12
collections:
- collection_type: open
  name: TabPFN Prediction API
  slug: open-priorlabs-prediction-api
- collection_type: open
  name: TabPFN Prediction Training API
  slug: open-priorlabs-training-api
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://priorlabs.ai/pricing
- group: commercial
  href: https://artifacts.apis.io/priorlabs/plans/priorlabs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/priorlabs-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/priorlabs/capabilities/priorlabs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/priorlabs-capability-edges.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.priorlabs.ai/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.priorlabs.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.priorlabs.ai/api-reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.priorlabs.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://priorlabs.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PriorLabs
- group: start
  title: ''
  type: SignUp
  url: https://ux.priorlabs.ai/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://priorlabs.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://priorlabs.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@priorlabs.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.priorlabs.ai/changelog
- group: docs
  href: https://artifacts.apis.io/priorlabs/openapi/_original/priorlabs-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/priorlabs-openapi-original.json
- group: other
  href: https://artifacts.apis.io/priorlabs/overlays/priorlabs-tabpfn-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/priorlabs-tabpfn-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/priorlabs/mcp/priorlabs-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/priorlabs-mcp.yml
- group: agent
  href: https://artifacts.apis.io/priorlabs/llms/priorlabs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/priorlabs-llms.txt
- group: build
  href: https://artifacts.apis.io/priorlabs/packages/priorlabs-packages.yml
  title: ''
  type: Packages
  url: packages/priorlabs-packages.yml
- group: build
  href: https://artifacts.apis.io/priorlabs/packages/priorlabs-packages.yml
  title: ''
  type: SDKs
  url: packages/priorlabs-packages.yml
- group: agent
  href: https://artifacts.apis.io/priorlabs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/priorlabs/authentication/priorlabs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/priorlabs-authentication.yml
- group: design
  href: https://artifacts.apis.io/priorlabs/conventions/priorlabs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/priorlabs-conventions.yml
- group: design
  href: https://artifacts.apis.io/priorlabs/errors/priorlabs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/priorlabs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/priorlabs/lifecycle/priorlabs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/priorlabs-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/priorlabs/lifecycle/priorlabs-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/priorlabs-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/priorlabs/data-model/priorlabs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/priorlabs-data-model.yml
- group: design
  href: https://artifacts.apis.io/priorlabs/conformance/priorlabs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/priorlabs-conformance.yml
- group: agent
  href: https://artifacts.apis.io/priorlabs/agentic-access/priorlabs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/priorlabs-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/priorlabs/security/priorlabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/priorlabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://priorlabs.ai/
created: '2026-07-17'
description: Prior Labs builds TabPFN, a tabular foundation model that delivers strong predictions on structured/tabular data in seconds — no dataset-specific training, tuning, or ML pipelines required. TabPFN-3 handles classification, regression, time-series forecasting, anomaly detection, synthetic data generation, embeddings, and uncertainty quantification via in-context learning, scaling to 1M rows, 2,000 columns, and 160 classes. Prior Labs exposes TabPFN through a cloud REST API (api.priorlabs.ai), Python and R client SDKs, a Model Context Protocol server for AI agents, and private deployments on AWS SageMaker, Databricks, and Azure AI Foundry. The company was published in Nature and is now part of SAP.
finops:
- has_sources: true
  method: derived
  name: Priorlabs Finops
  primary_unit: ''
  service_category: ''
  slug: priorlabs-finops
  template: true
image: https://priorlabs.ai/pl.svg
layout: provider
mcp_servers:
- description: Remote MCP server at api.priorlabs.ai over HTTP; 5 tools listed.
  name: Prior Labs MCP Server
  slug: tabpfn
modified: '2026-07-20'
name: Prior Labs
nav: Providers
network: true
overview: 'Prior Labs publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Prediction API and Training API. Tagged areas include Company, Machine Learning, Artificial Intelligence, Tabular Data, and Foundation Models.


  Prior Labs'' developer surface includes pricing, documentation, API reference, getting-started guide, engineering blog, signup flow, support, and 24 more developer resources.'
plans:
- name: Priorlabs Plans Pricing
  plan_count: 7
  slug: priorlabs-plans-pricing
random_paper: 14
score:
  band: developing
  composite: 53.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 55.7
    developer_ergonomics: 66.1
    discoverability: 65.0
    operational_transparency: 28.9
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/priorlabs/priorlabs-2026-08-17T081338.png
security:
- kind: authentication
  name: Priorlabs Authentication
  slug: priorlabs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Priorlabs Domain Security
  slug: priorlabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: TabPFN fit and predict
  slug: priorlabs-fit-and-predict
- name: TabPFN predictions via MCP
  slug: priorlabs-mcp-predictions
slug: priorlabs
tags:
- Company
- Machine Learning
- Artificial Intelligence
- Tabular Data
- Foundation Models
- Predictions
- Data Science
- MCP
- SDK
website: https://priorlabs.ai/
---
