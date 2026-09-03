---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.bdai.superb-ai.com
  baseurl_source: declared
  description: Multi-tenant REST backend for the Superb Platform. 164 operations across tenants, workspaces, image datasets and assets, projects and labeling workflow, annotations, comments, auto-label runs, model t
  name: Superb AI MLOps Platform API
  slug: superb-ai-mlops-platform-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://superb-ai.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.superb-ai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.superb-ai.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bdai.superb-ai.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.superb-ai.com/docs/welcome
- group: operate
  title: ''
  type: Support
  url: https://superb-ai.com/en/company/contact
- group: company
  title: ''
  type: Blog
  url: https://superb-ai.com/en/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Superb-AI-Suite
- group: commercial
  title: ''
  type: Pricing
  url: https://superb-ai.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.superb-ai.com/auth/sign_up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://superbai.notion.site/Terms-of-Use-a20d09ccfc28469987e61552eee3e3c4?pvs=4
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://superbai.notion.site/Privacy-Policy-880523efa01649708e64696332d1ca60
- group: auth
  title: ''
  type: TrustCenter
  url: security/superb-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superb-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/superb-ai-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/superb-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/superb-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/superb-ai-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/superb-ai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/superb-ai-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/superb-ai-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/superb-ai-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/superb-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/superb-ai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/superb-ai-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/superb-ai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/superb-ai-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/superb-ai-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/superb-ai-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/superb-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/superb-ai-conformance.yml
created: '2026-08-29'
description: Superb AI (Superb AI Inc.) is a vision-intelligence company that turns industrial visual data into models enterprises can deploy. Its Superb Platform covers the data-centric computer-vision lifecycle end to end — dataset and image-asset management, human and automated annotation (Superb Label), dataset curation and embedding search (Superb Curate), model training, diagnosis and hosted inference endpoints (Superb Model), plus the ZERO vision foundation model for open-vocabulary detection. The platform is used by manufacturing, logistics, mobility and physical-security teams, and is delivered as cloud, private-cloud and air-gapped on-premise deployments. Developers reach it through a multi-tenant REST API, a first-party Python SDK family and the spb command-line interface.
image: https://superb-ai.com/logo/superb-logo-circle.png
layout: provider
mcp_servers:
- description: ''
  name: Superb AI Documentation MCP Server
  slug: superb-ai-documentation-mcp-server
modified: '2026-08-29'
name: Superb AI
nav: Providers
network: true
overview: 'Superb AI publishes 1 API on the [APIs.io](https://apis.io/) network: MLOps Platform API. Tagged areas include Artificial Intelligence, Machine-Learning, Computer-Vision, Data Labeling, and Annotation.


  Superb AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Superb Ai Plans Pricing
  plan_count: 0
  slug: superb-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Superb Ai Rate Limits
  slug: superb-ai-rate-limits
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 46.9
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 42.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/superb-ai/refs/heads/main/screenshots/superb-ai-2026-09-02T161212.png
security:
- kind: authentication
  name: Superb Ai Authentication
  slug: superb-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Superb Ai Domain Security
  slug: superb-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Superb Ai Trust Center
  slug: superb-ai-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: superb-ai
tags:
- Artificial Intelligence
- Machine-Learning
- Computer-Vision
- Data Labeling
- Annotation
- MLOps
- Training Data
- Model Training
- Inference
- Datasets
website: https://superb-ai.com/en
---
