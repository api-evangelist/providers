---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: Programmatic entry points into the Guided Selling managed package for completing participant actions, skipping (deferring) participant actions, and creating sequence-independent quick actions. These a
  name: RingDNA Guided Selling API
  slug: guided-selling-api
- description: A live, remotely hosted Model Context Protocol server operated by Revenue.io at https://app.ringdna.com/mcp. An MCP client can POST to it today with no local install. It is protected by OAuth 2.1 with
  name: RingDNA MCP Server
  slug: mcp-server
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ringdna-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ringdna-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.revenue.io
- group: docs
  title: ''
  type: Documentation
  url: https://support.revenue.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ringdna
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revenueio
- group: company
  title: ''
  type: Blog
  url: https://www.revenue.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.revenue.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.revenue.io
- group: other
  title: ''
  type: X
  url: https://twitter.com/revenue_io
- group: commercial
  title: ''
  type: Plans
  url: plans/ringdna-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ringdna-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ringdna-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ringdna-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ringdna-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ringdna-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ringdna-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ringdna-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/ringdna-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ringdna-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.revenue.io/security
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ringdna-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ringdna-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ringdna-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ringdna-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ringdna-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ringdna-sandbox.yml
- group: docs
  title: ''
  type: APIReference
  url: https://support.revenue.io/guided-selling/salesforce-administration/api-endpoints/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.revenue.io/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://support.revenue.io
- group: start
  title: ''
  type: SignUp
  url: https://app.revenue.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.revenue.io/msa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.revenue.io/privacy-policy
created: '2026-06-13'
description: RingDNA (now Revenue.io) is an intelligent revenue platform providing REST APIs for sales dialing, call recording, conversation analytics, real-time coaching, and CRM integration. The platform is 100% Salesforce-native and serves revenue teams with AI-driven sales engagement, guided selling cadences, conversation intelligence, and revenue orchestration capabilities including the RingDNA Dialer, Moments real-time guidance, and Guided Selling API endpoints.
finops:
- name: Ringdna Finops
  service_category: ''
  slug: ringdna-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ringdna.png
layout: provider
mcp_servers:
- description: 'Revenue.io (formerly RingDNA) operates a live, remotely-hosted Model Context Protocol server at https://app.ringdna.com/mcp. It is a real agent surface: an MCP client can POST to it today without any '
  name: RingDNA / Revenue.io MCP Server
  slug: ringdna-revenueio-mcp-server
modified: '2026-08-14'
name: RingDNA
nav: Providers
network: true
overview: 'RingDNA publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Engagement, Conversation Intelligence, Sales Dialing, Call Recording, and Revenue Orchestration.


  RingDNA''s developer surface includes documentation, engineering blog, pricing, authentication, changelog, sandbox, API reference, and 26 more developer resources.'
plans:
- name: Ringdna Plans Pricing
  plan_count: 3
  slug: ringdna-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Ringdna Rate Limits
  slug: ringdna-rate-limits
scopes:
- name: Ringdna Scopes
  scope_count: 4
  slug: ringdna-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 38.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ringdna/refs/heads/main/screenshots/ringdna-2026-06-20T193122.png
security:
- kind: authentication
  name: Ringdna Authentication
  slug: ringdna-authentication
  summary_line: oauth2/apiKey · 3 schemes
- kind: domain-security
  name: Ringdna Domain Security
  slug: ringdna-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Ringdna Trust Center
  slug: ringdna-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: ringdna
tags:
- Sales Engagement
- Conversation Intelligence
- Sales Dialing
- Call Recording
- Revenue Orchestration
- CRM Integration
- Salesforce
- AI Coaching
- Sales Automation
website: https://www.revenue.io
---
