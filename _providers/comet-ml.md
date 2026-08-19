---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: 'The Comet REST API exposes read endpoints (workspace, project, experiment data), write endpoints (data submission), and Model Production Monitoring (MPM) endpoints. Authentication uses an API key via '
  name: Comet REST API
  slug: comet-rest-api
- description: Opik is Comet's open-source GenAI observability product. It provides spans-based tracing, evaluations, prompt management, and dataset features over an HTTP API and Python SDK. Self-hostable.
  name: Opik (GenAI Observability)
  slug: opik
artifact_total: 10
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/comet-ml/opik/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/comet-ml/opik/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/comet-ml/opik/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/comet-ml/opik/blob/main/LICENSE
- group: auth
  title: ''
  type: TrustCenter
  url: security/comet-ml-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/comet-ml-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/comet-ml
- group: company
  title: ''
  type: Website
  url: https://www.comet.com/
- group: start
  title: ''
  type: Portal
  url: https://www.comet.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.comet.com/site/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/comet-ml
- group: commercial
  title: ''
  type: Plans
  url: plans/comet-ml-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/comet-ml-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/comet-ml-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/comet-ml/opik-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/comet-ml/opik-skills
- group: company
  title: ''
  type: Blog
  url: https://www.comet.com/site/blog/feed/
created: '2026-05-08'
description: Comet is an MLOps and GenAI observability platform. It exposes a REST API (read, write, and Model Production Monitoring endpoints) plus a Python SDK. Opik is the GenAI observability product line; MLOps is the classical experiment-tracking line.
finops:
- name: Comet Ml Finops
  service_category: ML
  slug: comet-ml-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/comet-ml.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Comet
nav: Providers
network: true
overview: 'Comet publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ML, MLOps, GenAI, Experiment Tracking, and Model Monitoring.


  Comet''s developer surface includes developer portal, pricing, engineering blog, and 14 more developer resources.'
plans:
- name: Comet Ml Plans Pricing
  plan_count: 1
  slug: comet-ml-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 1
  name: Comet Ml Rate Limits
  slug: comet-ml-rate-limits
score:
  band: emerging
  composite: 20.1
  delta: -1.7
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 21.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/comet-ml/refs/heads/main/screenshots/comet-ml-2026-06-20T174806.png
security:
- kind: domain-security
  name: Comet Ml Domain Security
  slug: comet-ml-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Comet Ml Trust Center
  slug: comet-ml-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 2
skills:
- name: instrument
  slug: instrument
- name: opik
  slug: opik
slug: comet-ml
tags:
- ML
- MLOps
- GenAI
- Experiment Tracking
- Model Monitoring
website: https://www.comet.com/
---
