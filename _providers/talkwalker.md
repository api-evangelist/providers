---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: Search and export a subset of documents from a Talkwalker project, including brand mentions and social data across supported channels. Results are metered at 1 credit per result plus a minimum of 10 c
  name: Talkwalker Search API
  slug: search-api
- description: Real-time streaming API (v3) for monitoring keyword-based streams and project or topic-level data feeds. Charged at 1 credit per streamed result with no per-call minimum.
  name: Talkwalker Streaming API
  slug: streaming-api
- description: Reproduce Talkwalker dashboard widgets programmatically by fetching histogram data. Charged at 10 credits per call.
  name: Talkwalker Histogram API
  slug: histogram-api
- description: Manage and retrieve project resources including topics, filters, pages, events, panels, and datasets. Also exposes tag and view (dashboard, report, alert) management endpoints. Free to call — no credi
  name: Talkwalker Resources API
  slug: resources-api
- description: Import custom documents and modify existing documents within Talkwalker projects. Supports custom metrics creation for imported content. Document imports are free — no credit cost.
  name: Talkwalker Document API
  slug: document-api
- description: Detect features and entities within images using Talkwalker's image detection capabilities, enabling logo detection and visual content analytics.
  name: Talkwalker Image API
  slug: image-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/talkwalker-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/talkwalker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.talkwalker.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.talkwalker.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/talkwalker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/talkwalker
- group: company
  title: ''
  type: Blog
  url: https://www.talkwalker.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.talkwalker.com/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/Talkwalker
- group: commercial
  title: ''
  type: Plans
  url: plans/talkwalker-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/talkwalker-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/talkwalker-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.talkwalker.com/api/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.talkwalker.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.talkwalker.com/docs/getting-started/access-token
- group: operate
  title: ''
  type: Support
  url: https://www.talkwalker.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.talkwalker.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.talkwalker.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.talkwalker.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/talkwalker-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/talkwalker-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/talkwalker-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/talkwalker-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/talkwalker-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/talkwalker-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/talkwalker-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/talkwalker-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/talkwalker-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-06-13'
description: Talkwalker is a social media analytics and listening platform that provides REST APIs for tracking brand mentions, analyzing sentiment, measuring campaign performance, and monitoring competitors across 150 million websites and 10+ social networks. The API suite covers search, streaming, histograms, document management, image detection, topic management, and custom metrics.
finops:
- name: Talkwalker Finops
  service_category: ''
  slug: talkwalker-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/talkwalker.png
layout: provider
mcp_servers:
- description: ''
  name: talkwalker-mcp.yml
  slug: talkwalker-mcpyml
modified: '2026-08-13'
name: Talkwalker
nav: Providers
network: true
overview: 'Talkwalker publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Search API, Streaming API, Histogram API, and 3 more. Tagged areas include Social Media Analytics, Social Listening, Brand Monitoring, Sentiment Analysis, and Media Monitoring.


  Talkwalker''s developer surface includes authentication, documentation, engineering blog, pricing, API reference, getting-started guide, support, and 22 more developer resources.'
plans:
- name: Talkwalker Plans Pricing
  plan_count: 3
  slug: talkwalker-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 9
  name: Talkwalker Rate Limits
  slug: talkwalker-rate-limits
score:
  band: developing
  composite: 53.9
  delta: -4.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 16.7
    contract_quality: 46.2
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 57.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/talkwalker/refs/heads/main/screenshots/talkwalker-2026-06-20T194908.png
security:
- kind: authentication
  name: Talkwalker Authentication
  slug: talkwalker-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Talkwalker Domain Security
  slug: talkwalker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: talkwalker
tags:
- Social Media Analytics
- Social Listening
- Brand Monitoring
- Sentiment Analysis
- Media Monitoring
- Campaign Analytics
website: https://www.talkwalker.com/
---
