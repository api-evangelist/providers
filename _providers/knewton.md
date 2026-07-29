---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The Knewton Enterprise Platform REST API (v0) that partner learning applications integrate with to deliver continuously adaptive learning. Partners create anonymized user accounts, establish learning '
  name: Knewton Enterprise Platform API
  slug: enterprise-platform
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.knewton.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.knewton.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.knewton.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.knewton.com/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.knewton.com/implementation/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://support.knewton.com/s/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.knewton.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://dev.knewton.com/implementation/api-versioning/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wiley.com/en-us/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wiley.com/en-us/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/knewton-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/knewton-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/knewton-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/knewton-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/knewton-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/knewton-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/knewton-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/knewton-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/knewton-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/knewton-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/knewton-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/knewton-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/knewton-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knewton-domain-security.yml
created: '2026-07-17'
description: Knewton is an adaptive learning technology company founded in 2008 in New York City and acquired by John Wiley & Sons in 2019, where it now ships as the Knewton alta courseware line. Its developer-facing product is the Knewton Enterprise Platform API, documented at dev.knewton.com, which lets partner learning applications send learner interaction and performance data to Knewton and receive continuously personalized content recommendations and predictive analytics in return. The platform maps the pedagogical relationships between concepts in a partner catalog into a knowledge graph, then uses it to recommend modules, track goal status and progress, and generate predicted scores. The REST API is versioned at v0, uses OAuth 2.0 client-credentials tokens, and exposes accounts, learning instances, registrations, scoped goals, graded and ungraded student events, recommendations, status-and-progress metrics, and predicted score.
image: https://dev.knewton.com/knewton-theme/assets/images/layout/logo-kw.svg
layout: provider
mcp_servers:
- description: ''
  name: knewton-mcp.yml
  slug: knewton-mcpyml
modified: '2026-07-19'
name: Knewton
nav: Providers
network: true
overview: 'Knewton publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Education, EdTech, and Adaptive Learning.


  Knewton''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 19 more developer resources.'
random_paper: 54
rate_limits:
- limit_count: 0
  name: Knewton Rate Limits
  slug: knewton-rate-limits
scopes:
- name: Knewton Scopes
  scope_count: 0
  slug: knewton-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.4
  delta: -2.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 23.7
  previous_composite: 30.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knewton/refs/heads/main/screenshots/knewton-2026-07-25T223953.png
security:
- kind: authentication
  name: Knewton Authentication
  slug: knewton-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Knewton Domain Security
  slug: knewton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: knewton
tags:
- Company
- Consumer
- Education
- EdTech
- Adaptive Learning
- Learning Analytics
- Machine Learning
- Recommendations
- Courseware
- Higher Education
website: https://www.knewton.com/
---
