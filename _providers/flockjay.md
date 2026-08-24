---
access_model:
  confidence: high
  label: Demo request only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://flockjay.com/request-demo
  - plans/flockjay-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.1
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: Django REST Framework API behind the Flockjay platform. The API root at https://api.flockjay.com/api/ is anonymously readable and enumerates 20 collections across an unversioned v1 tree (events, quest
  name: Flockjay API
  slug: flockjay-api
- description: Hosted, first-party Model Context Protocol server that gives AI assistants read access to a customer's enablement data — rep certification and learning progress, coaching scorecards and call scores, a
  name: Flockjay MCP Server
  slug: flockjay-mcp-server
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://flockjay.com
- group: start
  title: ''
  type: Login
  url: https://flockjay.com/login
- group: company
  title: ''
  type: Blog
  url: https://flockjay.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://flockjay.com/resources/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flockjay
- group: auth
  title: ''
  type: TrustCenter
  url: https://flockjay.com/product/trust-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flockjay.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flockjay.com/legal/terms-and-conditions
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flockjay-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flockjay-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flockjay-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flockjay-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flockjay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flockjay-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flockjay-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flockjay-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flockjay-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flockjay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flockjay-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/flockjay-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flockjay-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flockjay-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flockjay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/flockjay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/flockjay-trust-center.yml
created: '2026-07-17'
description: 'Flockjay is a sales enablement platform that helps revenue teams capture, organize, and scale their best practices. It combines a learning management system, a content and knowledge management system, and AI-powered coaching — including semantic search across sales content, real-time deal and rep coaching, call scoring, and pitch grading — so sales leaders, revenue operations, and enablement professionals can onboard reps faster and reinforce winning behaviors. Flockjay advertises 50+ integrations with tools such as Gong, Chorus, Clari Copilot, Slack, Microsoft Teams, Zoom, Salesforce and Okta, and is backed by Lightspeed Venture Partners, e.ventures and Salesforce Ventures. Flockjay runs a Django REST Framework API at api.flockjay.com whose root anonymously enumerates 20 collections across two version trees, and a hosted, OAuth 2.1-protected Model Context Protocol server at api.flockjay.com/mcp that it announced on its own blog. Neither is documented: there is no developer
  portal, no API reference, no OpenAPI, no SDK and no pricing page anywhere on flockjay.com.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flockjay.png
json_schemas:
- name: Flockjay Events Options Metadata
  property_count: 0
  slug: flockjay-events-options-metadata
layout: provider
mcp_servers:
- description: Flockjay operates a first-party, hosted Model Context Protocol server that gives AI assistants read access to a customer's enablement data — rep certification and learning progress, coaching scorecard
  name: Flockjay MCP Server
  slug: flockjay-mcp-server
- description: ''
  name: Flockjay MCP Server
  slug: flockjay-mcp-server-2
modified: '2026-08-14'
name: Flockjay
nav: Providers
network: true
overview: 'Flockjay publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales Enablement, Sales Training, Learning Management, and Revenue Operations.


  Flockjay''s developer surface includes engineering blog, support, authentication, and 22 more developer resources.'
plans:
- name: Flockjay Plans Pricing
  plan_count: 0
  slug: flockjay-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Flockjay Rate Limits
  slug: flockjay-rate-limits
scopes:
- name: Flockjay Scopes
  scope_count: 0
  slug: flockjay-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.2
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 8.5
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 33.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 85.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flockjay/refs/heads/main/screenshots/flockjay-2026-07-25T214813.png
security:
- kind: authentication
  name: Flockjay Authentication
  slug: flockjay-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Flockjay Domain Security
  slug: flockjay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flockjay Vulnerability Disclosure
  slug: flockjay-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Flockjay Trust Center
  slug: flockjay-trust-center
  summary_line: trust center published
slug: flockjay
tags:
- Company
- Sales Enablement
- Sales Training
- Learning Management
- Revenue Operations
- AI Coaching
- Content Management
- Software-as-a-Service
- MCP
- agent-native
- Authentication
website: https://flockjay.com
---
