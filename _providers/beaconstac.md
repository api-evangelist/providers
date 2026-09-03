---
access_model:
  confidence: high
  label: Self-serve signup, 14-day trial, API from the Pro plan up
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - authentication
  - plans
  - rate-limits
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: REST API (v2.0) to programmatically create static and dynamic QR Codes across 20+ campaign types, apply design templates, generate codes in bulk from CSV/XLSX, manage Digital Business Cards, leads and
  name: Uniqode QR Code API
  slug: uniqode-qr-code-api
artifact_total: 9
asyncapis:
- description: ''
  name: Beaconstac Webhooks
  slug: beaconstac-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.uniqode.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.uniqode.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.uniqode.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.uniqode.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.uniqode.com/en/articles/6064771-getting-started-with-static-and-dynamic-qr-code-api
- group: build
  title: ''
  type: Postman
  url: https://apidocs.uniqode.com/
- group: build
  title: ''
  type: PostmanCollection
  url: collections/beaconstac-uniqode-api.postman_collection.json
- group: company
  title: ''
  type: Blog
  url: https://www.uniqode.com/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.uniqode.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.uniqode.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.uniqode.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/beaconstac-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.uniqode.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.uniqode.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uniqode.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uniqode.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mobstac
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uniqode.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/beaconstac-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.uniqode.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/beaconstac-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beaconstac-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beaconstac-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beaconstac-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/beaconstac-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.uniqode.com/.well-known/openid-configuration
- group: agent
  title: ''
  type: MCPServer
  url: mcp/beaconstac-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beaconstac-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/beaconstac-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/beaconstac-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/beaconstac-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/beaconstac-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/beaconstac-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/beaconstac-packages.yml
- group: design
  title: ''
  type: Components
  url: components/beaconstac-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beaconstac-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beaconstac-llms.txt
created: '2026-07-17'
description: Beaconstac (now Uniqode) is a B2B SaaS platform for creating, customizing, and tracking dynamic QR Codes and Digital Business Cards at scale, connecting physical touchpoints to measurable digital experiences for 50,000+ brands. Its REST API (v2.0) covers QR Codes and templates, bulk CSV generation, Digital Business Cards, leads, wallet passes, feedback forms, tags, places, media, organizations, users and webhooks, plus a separate RPC reporting endpoint for scan analytics; the contract is published as a 96-request Postman collection rather than an OpenAPI. REST auth is a dashboard-issued token in the Authorization header plus an Organization ID, gated to the Pro plan and above at 10-100 requests/second by tier. Uniqode also runs a hosted, OAuth-protected MCP server at mcp.uniqode.com for QR management and analytics from Claude. SOC 2 Type II, ISO 27001:2022, HIPAA and GDPR compliant. Formerly MobStac / Beaconstac; backed by Accel.
image: https://cdn.prod.website-files.com/6669ecc72092c5122374cf32/6731094d55afbe708065f595_uniqode-opengraph.png
layout: provider
mcp_servers:
- description: ''
  name: Beaconstac MCP Server
  slug: beaconstac-mcp-server
modified: '2026-08-13'
name: Beaconstac
nav: Providers
network: true
overview: 'Beaconstac publishes 1 API on the [APIs.io](https://apis.io/) network: Uniqode QR Code API. Tagged areas include Company, Big Data, QR Codes, Digital Business Cards, and Marketing.


  The Beaconstac catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Beaconstac''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Beaconstac Plans Pricing
  plan_count: 0
  slug: beaconstac-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Beaconstac Rate Limits
  slug: beaconstac-rate-limits
scopes:
- name: Beaconstac Scopes
  scope_count: 6
  slug: beaconstac-scopes
  summary_line: 6 scopes
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 57.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beaconstac/refs/heads/main/screenshots/beaconstac-2026-07-25T202531.png
security:
- kind: authentication
  name: Beaconstac Authentication
  slug: beaconstac-authentication
  summary_line: apiKey/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Beaconstac Domain Security
  slug: beaconstac-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Beaconstac Trust Center
  slug: beaconstac-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, ISO 27001:2022, HIPAA, GDPR, UK GDPR
slug: beaconstac
tags:
- Company
- Big Data
- QR Codes
- Digital Business Cards
- Marketing
- Analytics
- Software-as-a-Service
- Proximity
- Webhook
- MCP
website: https://www.uniqode.com
---
