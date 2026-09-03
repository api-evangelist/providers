---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Evidently Agentic Access
  operation_count: 26
  slug: evidently-agentic-access
  summary_line: 26 operations · 10 acting
api_count: 1
apis:
- baseURL: https://app.evidently.cloud
  baseurl_source: declared
  description: Manage project monitoring dashboards
  name: Evidently AI Dashboards API
  slug: evidently-dashboards-api
- baseURL: https://app.evidently.cloud
  baseurl_source: declared
  description: Manage Evidently projects — create, list, update, delete
  name: Evidently AI Projects API
  slug: evidently-projects-api
- baseURL: https://app.evidently.cloud
  baseurl_source: declared
  description: Service metadata and version information
  name: Evidently AI Service API
  slug: evidently-service-api
- baseURL: https://app.evidently.cloud
  baseurl_source: declared
  description: Upload and query evaluation snapshots (reports and test suites)
  name: Evidently AI Snapshots API
  slug: evidently-snapshots-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Evidently Platform REST Dashboards API
  slug: open-evidently-dashboards-api
- collection_type: open
  name: Evidently Platform REST Dashboards Projects API
  slug: open-evidently-projects-api
- collection_type: open
  name: Evidently Platform REST Dashboards Service API
  slug: open-evidently-service-api
- collection_type: open
  name: Evidently Platform REST Dashboards Snapshots API
  slug: open-evidently-snapshots-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/evidentlyai/evidently/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/evidentlyai/evidently/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/evidentlyai/evidently/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/evidentlyai/evidently/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/evidently-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evidently-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/evidently-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.evidentlyai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evidentlyai.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/evidentlyai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/evidently-ai/
- group: company
  title: ''
  type: Blog
  url: https://www.evidentlyai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.evidentlyai.com/pricing
- group: other
  title: ''
  type: X
  url: https://twitter.com/EvidentlyAI
- group: commercial
  title: ''
  type: Plans
  url: plans/evidently-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/evidently-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/evidently-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/evidently-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/evidently-context.jsonld
created: '2026-06-13'
description: Evidently AI is an open-source ML and LLM observability framework licensed under Apache 2.0 that enables teams to evaluate, test, and monitor AI-powered systems and data pipelines in production. The platform provides over 100 built-in metrics for tracking data drift, data quality, and model performance across both tabular data and generative AI workloads. Developers can integrate evaluations programmatically via the Python SDK or through the Evidently Platform REST API, which exposes endpoints for managing projects, uploading traces, running evaluations, and storing results. Evidently supports self-hosted deployments and previously offered Evidently Cloud (now discontinued as SaaS) so teams can run the full platform within their own infrastructure.
finops:
- name: Evidently Finops
  service_category: ''
  slug: evidently-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/evidently.png
jsonld:
- class_count: 0
  name: Evidently Context
  property_count: 35
  slug: evidently-context
layout: provider
modified: '2026-06-13'
name: Evidently AI
nav: Providers
network: true
overview: 'Evidently AI publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Dashboards API, Projects API, Service API, and 1 more. Tagged areas include ML Monitoring, LLM Observability, Data Drift, Model Performance, and AI Evaluation.


  The Evidently AI catalog on APIs.io includes 1 JSON-LD context.


  Evidently AI''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Evidently Plans Pricing
  plan_count: 3
  slug: evidently-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Evidently Rate Limits
  slug: evidently-rate-limits
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 12
    catalog_gap: 50.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 15.2
    contract_quality: 59.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 15.2
    operational_transparency: 21.1
  open_source:
    applies: true
    score: 50.0
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evidently/refs/heads/main/screenshots/evidently-2026-06-20T180913.png
security:
- kind: authentication
  name: Evidently Authentication
  slug: evidently-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Evidently Domain Security
  slug: evidently-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: evidently
tags:
- ML Monitoring
- LLM Observability
- Data Drift
- Model Performance
- AI Evaluation
- Data Quality
- Open-Source
- MLOps
- LLMOps
- Generative AI
website: https://www.evidentlyai.com/
---
