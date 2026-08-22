---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for managing email campaigns, subscriber lists, transactional emails, segments, journeys, templates, and campaign performance analytics.
  name: Campaign Monitor API
  slug: campaign-monitor-api
artifact_total: 12
asyncapis:
- description: ''
  name: Campaignmonitor Webhooks
  slug: campaignmonitor-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/campaignmonitor-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/campaignmonitor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/campaignmonitor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.campaignmonitor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.campaignmonitor.com/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/campaignmonitor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/campaign-monitor
- group: company
  title: ''
  type: Blog
  url: https://www.campaignmonitor.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.campaignmonitor.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.campaignmonitor.com/
- group: other
  title: ''
  type: X
  url: https://x.com/campaignmonitor
- group: commercial
  title: ''
  type: Plans
  url: plans/campaignmonitor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/campaignmonitor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/campaignmonitor-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/campaignmonitor-context.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.campaignmonitor.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.campaignmonitor.com/api/v3-3/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://help.campaignmonitor.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.campaignmonitor.com/signup/
- group: start
  title: ''
  type: Login
  url: https://login.createsend.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.campaignmonitor.com/policies/#terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.campaignmonitor.com/policies/#privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/campaignmonitor-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/campaignmonitor-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/campaignmonitor-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/campaignmonitor-security.txt
- group: auth
  title: ''
  type: Security
  url: security/campaignmonitor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/campaignmonitor-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/campaignmonitor-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/campaignmonitor-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/campaignmonitor-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/campaignmonitor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/campaignmonitor-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/campaignmonitor-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/campaignmonitor-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/campaignmonitor-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/campaignmonitor-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/campaignmonitor-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/campaignmonitor-llms.txt
created: '2026-06-13'
description: Campaign Monitor, a Marigold brand, is an email marketing platform for marketers and agencies. Its REST API — served under the original createsend name at api.createsend.com/api/v3.3 — manages clients, subscriber lists, subscribers and custom fields, segments, campaigns, HTML templates, automated journeys, authenticated sending domains and transactional email, and returns per-recipient reporting for opens, clicks, bounces, unsubscribes and spam complaints. Authentication is OAuth 2.0 with twelve coarse permissions, or an API key over HTTP Basic. Per-list webhooks push Subscribe, Update and Deactivate events. Campaign Monitor publishes no OpenAPI, no AsyncAPI and no MCP server; the contract is HTML reference documentation plus seven official client libraries.
finops:
- name: Campaignmonitor Finops
  service_category: ''
  slug: campaignmonitor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/campaignmonitor.png
jsonld:
- class_count: 18
  name: Campaignmonitor Context
  property_count: 1
  slug: campaignmonitor-context
layout: provider
mcp_servers:
- description: ''
  name: campaignmonitor-mcp.yml
  slug: campaignmonitor-mcpyml
modified: '2026-08-13'
name: Campaign Monitor
nav: Providers
network: true
overview: 'Campaign Monitor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email Marketing, Campaigns, Subscribers, Transactional Email, and Segments.


  The Campaign Monitor catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Campaign Monitor''s developer surface includes documentation, engineering blog, pricing, getting-started guide, support, signup flow, authentication, and 33 more developer resources.'
plans:
- name: Campaignmonitor Plans Pricing
  plan_count: 5
  slug: campaignmonitor-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Campaignmonitor Rate Limits
  slug: campaignmonitor-rate-limits
scopes:
- name: Campaignmonitor Scopes
  scope_count: 0
  slug: campaignmonitor-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 72.9
  delta: 3.7
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 56.3
    developer_ergonomics: 57.1
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 69.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/campaignmonitor/refs/heads/main/screenshots/campaignmonitor-2026-06-20T173912.png
security:
- kind: authentication
  name: Campaignmonitor Authentication
  slug: campaignmonitor-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Campaignmonitor Domain Security
  slug: campaignmonitor-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Campaignmonitor Vulnerability Disclosure
  slug: campaignmonitor-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Campaignmonitor Trust Center
  slug: campaignmonitor-trust-center
  summary_line: SOC 2, GDPR
slug: campaignmonitor
tags:
- Email Marketing
- Campaigns
- Subscribers
- Transactional Email
- Segments
- Newsletters
- Automation
- Marketing Automation
- Webhooks
- Email Deliverability
- Marketing
website: https://www.campaignmonitor.com/
---
