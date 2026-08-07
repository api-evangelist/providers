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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Gptzero Agentic Access
  operation_count: 7
  slug: gptzero-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 3
apis:
- description: Batch processing
  name: GPTZero Batch API
  slug: gptzero-batch-api
- description: AI content detection
  name: GPTZero Detection API
  slug: gptzero-detection-api
- description: Document analysis
  name: GPTZero Documents API
  slug: gptzero-documents-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://gptzero.me
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gptzero.me/developers
- group: docs
  title: ''
  type: Documentation
  url: https://gptzero.stoplight.io/
- group: docs
  title: ''
  type: APIReference
  url: https://gptzero.stoplight.io/docs/gptzero-api/5bf295g49gwxp-gpt-zero-api
- group: start
  title: ''
  type: GettingStarted
  url: https://support.gptzero.me/hc/en-us/articles/15525014408215-How-can-I-get-the-API-and-request-code-samples
- group: operate
  title: ''
  type: Support
  url: https://support.gptzero.me
- group: company
  title: ''
  type: Blog
  url: https://gptzero.me/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GPTZero
- group: commercial
  title: ''
  type: Pricing
  url: https://gptzero.me/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.gptzero.me/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gptzero.me/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gptzero.me/privacy-policy.html
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/gptzero-openapi-original.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/gptzero-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/gptzero-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gptzero-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gptzero-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/gptzero-detect-ai-text.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/gptzero-batch-analysis.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gptzero-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/gptzero-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/gptzero-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gptzero-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gptzero-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gptzero-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gptzero-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gptzero-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gptzero-plans.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gptzero-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gptzero-agentic-access.yml
created: '2026-07-17'
description: GPTZero is an AI content detection company whose v2 API analyzes text and uploaded documents to determine whether content was written by a human, by AI, or is a mix of both. The API returns document-, paragraph-, and sentence-level probabilities along with supporting perplexity and burstiness signals, plus asynchronous batch analysis and aggregate reporting. Authentication is via an X-API-Key header, requests are rate limited to 30,000 per hour, and API access is bundled with the Professional plan. GPTZero was surfaced as a portfolio company of Uncork Capital and has been enriched into the API Evangelist network from its public developer surface.
image: https://gptzero.me/logo.png
layout: provider
mcp_servers:
- description: ''
  name: gptzero-mcp.yml
  slug: gptzero-mcpyml
modified: '2026-07-19'
name: GPTZero
nav: Providers
network: true
overview: 'GPTZero publishes 3 APIs on the [APIs.io](https://apis.io/) network: Batch API, Detection API, and Documents API. Tagged areas include Company, Ai, AI Detection, Content Moderation, and Machine Learning.


  GPTZero''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Gptzero Plans
  plan_count: 4
  slug: gptzero-plans
random_paper: 101
rate_limits:
- limit_count: 1
  name: Gptzero Rate Limits
  slug: gptzero-rate-limits
score:
  band: strong
  composite: 58.2
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 57.4
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 42.1
  previous_composite: 58.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gptzero/refs/heads/main/screenshots/gptzero-2026-07-25T220147.png
security:
- kind: authentication
  name: Gptzero Authentication
  slug: gptzero-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gptzero Domain Security
  slug: gptzero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gptzero
tags:
- Company
- Ai
- AI Detection
- Content Moderation
- Machine Learning
- Text Analysis
- Natural Language Processing
- Education
website: https://gptzero.me
---
