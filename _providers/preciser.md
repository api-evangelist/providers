---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The Chart Data API from Preciser — 1 operation(s) for chart data.
  name: Preciser Chart Data API
  slug: preciser-chart-data-api
- description: The Opp Team Data API from Preciser — 1 operation(s) for opp team data.
  name: Preciser Opp Team Data API
  slug: preciser-opp-team-data-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://preciser.io
- group: docs
  title: ''
  type: APIReference
  url: https://api.preciser.io/
- group: company
  title: ''
  type: Blog
  url: https://preciser.io/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.preciser.io
- group: start
  title: ''
  type: Login
  url: https://app.preciser.io
- group: operate
  title: ''
  type: Support
  url: https://preciser.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://preciser.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://preciser.io/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/preciserai/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/preciserai
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/precisersports/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/preciser-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/preciser-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/preciser-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/preciser-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/preciser-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/preciser-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/preciser-domain-security.yml
created: '2026-07-17'
description: Preciser is an AI and computer-vision sports analytics platform that automatically converts basketball and baseball game footage into statistics, trends, and player insights, removing the traditionally manual work of video tagging. Its three-part product covers Capture (InstaStats converts video to stats), Analyze (a Data Management System that generates statistics and insights), and Monetize (APIs that expose live stats feeds and widgets). The Preciser API advertises game chart-data and opponent-team-data endpoints under https://plg-api.preciser.io/v1. The company reports roughly 85% average accuracy, a two-hour average turnaround per game, and 10x faster analysis than manual tagging. Preciser is backed by 500 Global and the NVIDIA Inception Program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/preciser.png
layout: provider
mcp_servers:
- description: ''
  name: preciser-mcp.yml
  slug: preciser-mcpyml
modified: '2026-07-20'
name: Preciser
nav: Providers
network: true
overview: 'Preciser publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chart Data API and Opp Team Data API. Tagged areas include Company, Sports, Sports Analytics, Computer Vision, and Artificial Intelligence.


  Preciser''s developer surface includes API reference, engineering blog, signup flow, support, and 14 more developer resources.'
random_paper: 71
score:
  band: thin
  composite: 32.0
  delta: -1.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 52.5
    developer_ergonomics: 15.2
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 33.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Preciser Domain Security
  slug: preciser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: preciser
tags:
- Company
- Sports
- Sports Analytics
- Computer Vision
- Artificial Intelligence
- Video Analysis
- Statistics
- Basketball
- Baseball
- Data
website: https://preciser.io
---
