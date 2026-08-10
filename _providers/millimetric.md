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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 63.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Millimetric Agentic Access
  operation_count: 7
  slug: millimetric-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 3
apis:
- description: Link anonymous visitors to known users and honor deletion requests.
  name: Millimetric Identity API
  slug: millimetric-identity-api
- description: Write events into a project.
  name: Millimetric Ingest API
  slug: millimetric-ingest-api
- description: Query raw events and aggregated stats and attribution.
  name: Millimetric Read API
  slug: millimetric-read-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Track anonymously, identify on login, tag subsequent events, then read the user's history.
  name: Stitch an anonymous visitor to a known user
  slug: millimetric-anonymous-to-known
- description: Emit an event, then pull aggregate stats and the paid-vs-social attribution split.
  name: Capture an event and analyze traffic sources
  slug: millimetric-capture-and-analyze
- description: Confirm a user's events, then permanently delete them with a secret key.
  name: GDPR right-to-be-forgotten
  slug: millimetric-gdpr-delete
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://millimetric.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.millimetric.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.millimetric.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.millimetric.ai/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.millimetric.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:hello@millimetric.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://millimetric.ai/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://millimetric.ai/signup
- group: start
  title: ''
  type: Login
  url: https://millimetric.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://millimetric.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://millimetric.ai/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.millimetric.ai
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/millimetric-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/millimetric-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/millimetric-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/millimetric-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/millimetric-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/millimetric-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/millimetric-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/millimetric-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/millimetric-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/millimetric-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/millimetric-plans.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/millimetric-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/millimetric-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/millimetric-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/millimetric-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://millimetric.ai/legal/dpa
- group: design
  title: ''
  type: DataModel
  url: data-model/millimetric-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/millimetric-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/millimetric-capture-and-analyze.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/millimetric-anonymous-to-known.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/millimetric-gdpr-delete.yml
created: '2026-07-17'
description: Millimetric is API-first, privacy-respecting web and product analytics for developers, indie startups ("vibe coders"), and AI agents. It captures events over a simple REST API (/v1/track, /v1/batch, /v1/identify, /v1/query, /v1/stats, /v1/sources), a ~1.8 KB browser SDK, and a zero-dependency Node SDK, with a built-in attribution classifier that splits paid versus organic social traffic (the Facebook social-vs-paid split). It stores no cookies and no raw IPs — GDPR/CCPA compliant, with a /v1/forget right-to-be-forgotten endpoint — and ships a first-class hosted Model Context Protocol (MCP) server so AI agents emit and query analytics natively. Backed by Seedcamp.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/millimetric.png
layout: provider
mcp_servers:
- description: ''
  name: millimetric-mcp.yml
  slug: millimetric-mcpyml
modified: '2026-07-20'
name: Millimetric
nav: Providers
network: true
overview: 'Millimetric publishes 3 APIs on the [APIs.io](https://apis.io/) network: Identity API, Ingest API, and Read API. Tagged areas include Company, Analytics, Web Analytics, Product Analytics, and Attribution.


  Millimetric''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Millimetric Plans
  plan_count: 3
  slug: millimetric-plans
random_paper: 19
rate_limits:
- limit_count: 2
  name: Millimetric Rate Limits
  slug: millimetric-rate-limits
score:
  band: strong
  composite: 62.6
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 67.9
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 62.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/millimetric/refs/heads/main/screenshots/millimetric-2026-08-07T172916.png
security:
- kind: authentication
  name: Millimetric Authentication
  slug: millimetric-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Millimetric Domain Security
  slug: millimetric-domain-security
  summary_line: TLSv1.3 · HSTS
slug: millimetric
tags:
- Company
- Analytics
- Web Analytics
- Product Analytics
- Attribution
- Privacy
- MCP
- AI Agents
- Events
- Developer Tools
website: https://millimetric.ai
---
