---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Revenue.io's programmable surface for guided selling, call analytics, rep performance data, conversation insights, and CRM activity synchronization. Exposed as RDNACadence Apex classes and Flow invoca
  name: Revenue.io API
  slug: revenue-io-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/revenue-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revenue-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.revenue.io/
- group: docs
  title: ''
  type: Documentation
  url: https://support.revenue.io/
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
  url: https://status.revenue.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revenueio
- group: other
  title: ''
  type: X
  url: https://twitter.com/revenue_io
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/revenue-io/refs/heads/main/plans/revenue-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/revenue-io/refs/heads/main/rate-limits/revenue-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/revenue-io/refs/heads/main/finops/revenue-io-finops.yml
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
  url: https://support.revenue.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ringdna
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.revenue.io/msa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.revenue.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.revenue.io/
- group: auth
  title: ''
  type: Compliance
  url: https://www.revenue.io/security
- group: operate
  title: ''
  type: Deprecation
  url: https://support.revenue.io/guided-selling/release-notes/guided-selling-winter-2025-release-v12/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.revenue.io/guided-selling/release-notes/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/revenue-io-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/revenue-io-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/revenue-io-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revenue-io-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/revenue-io-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revenue-io-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/revenue-io-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/revenue-io-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/revenue-io-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/revenue-io-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/revenue-io-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/revenue-io-data-model.yml
created: '2026-06-13'
description: Revenue.io is a Salesforce-native revenue orchestration platform offering real-time guidance, call analytics, rep performance tracking, conversation insights, and CRM activity synchronization. Formerly known as RingDNA, it powers RevOps, Sales Engagement, and Conversation Intelligence for inside sales teams using Salesforce. It publishes no public REST API or OpenAPI; its documented programmable surface is a set of Apex classes and Flow invocable actions in the RDNACadence managed-package namespace, plus an OAuth-gated remote MCP server at https://app.ringdna.com/mcp discovered from RFC 9728 protected-resource metadata on api.revenue.io.
finops:
- name: Revenue Io Finops
  service_category: ''
  slug: revenue-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revenue-io.png
layout: provider
mcp_servers:
- description: Revenue.io operates a live, remote Model Context Protocol server at https://app.ringdna.com/mcp. It was discovered from the RFC 9728 protected-resource metadata served at https://api.revenue.io/.well-
  name: Revenue.io (ringDNA) MCP Server
  slug: revenueio-ringdna-mcp-server
modified: '2026-08-13'
name: Revenue.io
nav: Providers
network: true
overview: 'Revenue.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Revenue Intelligence, Sales Engagement, Conversation Intelligence, Revenue Operations, and Call Analytics.


  Revenue.io''s developer surface includes documentation, engineering blog, pricing, API reference, getting-started guide, support, changelog, and 27 more developer resources.'
plans:
- name: Revenue Io Plans Pricing
  plan_count: 3
  slug: revenue-io-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Revenue Io Rate Limits
  slug: revenue-io-rate-limits
scopes:
- name: Revenue Io Scopes
  scope_count: 1
  slug: revenue-io-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 32.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revenue-io/refs/heads/main/screenshots/revenue-io-2026-06-20T193047.png
security:
- kind: authentication
  name: Revenue Io Authentication
  slug: revenue-io-authentication
  summary_line: oauth2/apiKey · 3 schemes
- kind: domain-security
  name: Revenue Io Domain Security
  slug: revenue-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Revenue Io Trust Center
  slug: revenue-io-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: revenue-io
tags:
- Revenue Intelligence
- Sales Engagement
- Conversation Intelligence
- Revenue Operations
- Call Analytics
- Real-Time Guidance
- CRM Integration
- Salesforce
website: https://www.revenue.io/
---
