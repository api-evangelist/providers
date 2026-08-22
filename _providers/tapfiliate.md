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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 41
  human_in_the_loop: 0
  name: Tapfiliate Agentic Access
  operation_count: 77
  slug: tapfiliate-agentic-access
  summary_line: 77 operations · 41 acting
api_count: 11
apis:
- description: Manage affiliate groups
  name: Tapfiliate Affiliate Groups API
  slug: tapfiliate-affiliate-groups-api
- description: Manage affiliate prospects (pending applicants)
  name: Tapfiliate Affiliate Prospects API
  slug: tapfiliate-affiliate-prospects-api
- description: Manage affiliates, their groups, notes, and payout methods
  name: Tapfiliate Affiliates API
  slug: tapfiliate-affiliates-api
- description: View affiliate balances
  name: Tapfiliate Balances API
  slug: tapfiliate-balances-api
- description: Track and manage clicks
  name: Tapfiliate Clicks API
  slug: tapfiliate-clicks-api
- description: Manage individual commissions
  name: Tapfiliate Commissions API
  slug: tapfiliate-commissions-api
- description: Track and manage conversions and commissions
  name: Tapfiliate Conversions API
  slug: tapfiliate-conversions-api
- description: Manage customers and their metadata
  name: Tapfiliate Customers API
  slug: tapfiliate-customers-api
- description: Manage affiliate payments
  name: Tapfiliate Payments API
  slug: tapfiliate-payments-api
- description: Manage affiliate programs and program affiliates
  name: Tapfiliate Programs API
  slug: tapfiliate-programs-api
- description: Official remote Model Context Protocol server for Tapfiliate, announced 2026-08-07. A read-only analytics surface over live account data — clicks, conversions, customers, revenue, commissions, payouts
  name: Tapfiliate MCP Server
  slug: tapfiliate-mcp-server
artifact_total: 40
asyncapis:
- description: ''
  name: Tapfiliate Webhooks
  slug: tapfiliate-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tapfiliate REST Affiliate Groups API
  slug: open-tapfiliate-affiliate-groups-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Affiliate Prospects API
  slug: open-tapfiliate-affiliate-prospects-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Affiliates API
  slug: open-tapfiliate-affiliates-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Balances API
  slug: open-tapfiliate-balances-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Clicks API
  slug: open-tapfiliate-clicks-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Commissions API
  slug: open-tapfiliate-commissions-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Conversions API
  slug: open-tapfiliate-conversions-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Customers API
  slug: open-tapfiliate-customers-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Payments API
  slug: open-tapfiliate-payments-api
- collection_type: open
  name: Tapfiliate REST Affiliate Groups Programs API
  slug: open-tapfiliate-programs-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tapfiliate-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tapfiliate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tapfiliate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tapfiliate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tapfiliate.com
- group: docs
  title: ''
  type: Documentation
  url: https://tapfiliate.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Tapfiliate
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tapfiliate/
- group: company
  title: ''
  type: Blog
  url: https://tapfiliate.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://tapfiliate.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tapfiliate.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/tapfiliate
- group: commercial
  title: ''
  type: Plans
  url: plans/tapfiliate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tapfiliate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tapfiliate-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tapfiliate-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/tapfiliate-context.jsonld
- group: build
  title: ''
  type: Packages
  url: packages/tapfiliate-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tapfiliate-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tapfiliate-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tapfiliate-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tapfiliate-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tapfiliate-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tapfiliate-security.txt
- group: auth
  title: ''
  type: Security
  url: security/tapfiliate-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tapfiliate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tapfiliate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tapfiliate-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tapfiliate-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tapfiliate-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tapfiliate-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tapfiliate-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tapfiliate-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tapfiliate.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://tapfiliate.com/docs/rest/
- group: start
  title: ''
  type: GettingStarted
  url: https://tapfiliate.com/docs/integrations/rest-api/
- group: operate
  title: ''
  type: Support
  url: https://support.tapfiliate.com/
- group: start
  title: ''
  type: SignUp
  url: https://tapfiliate.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tapfiliate.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tapfiliate.com/privacy/
created: 2026-06-13
description: Tapfiliate is an affiliate tracking and management platform with a REST API for creating affiliate programs, managing affiliates, tracking conversions, and handling commission payouts. The API is versioned at V1.6 and uses API key authentication via the X-Api-Key header.
examples:
- key_count: 4
  name: Tapfiliate Create Affiliate Example
  slug: tapfiliate-create-affiliate-example
- key_count: 4
  name: Tapfiliate Create Conversion Example
  slug: tapfiliate-create-conversion-example
finops:
- name: Tapfiliate Finops
  service_category: ''
  slug: tapfiliate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tapfiliate.png
json_schemas:
- name: Affiliate
  property_count: 10
  slug: tapfiliate-affiliate
- name: Commission
  property_count: 7
  slug: tapfiliate-commission
- name: Conversion
  property_count: 8
  slug: tapfiliate-conversion
- name: Customer
  property_count: 6
  slug: tapfiliate-customer
jsonld:
- class_count: 54
  name: Tapfiliate Context
  property_count: 0
  slug: tapfiliate-context
layout: provider
mcp_servers:
- description: ''
  name: tapfiliate-mcp.yml
  slug: tapfiliate-mcpyml
modified: 2026-08-13
name: Tapfiliate
nav: Providers
network: true
overview: 'Tapfiliate publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Affiliate Groups API, Affiliate Prospects API, Affiliates API, and 7 more. Tagged areas include Affiliate Marketing, Affiliate Tracking, Commission Management, Conversion Tracking, and Partner Programs.


  The Tapfiliate catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Tapfiliate''s developer surface includes authentication, documentation, engineering blog, pricing, sandbox, API reference, getting-started guide, and 34 more developer resources.'
plans:
- name: Tapfiliate Plans Pricing
  plan_count: 3
  slug: tapfiliate-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Tapfiliate Rate Limits
  slug: tapfiliate-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tapfiliate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tapfiliate-jsonschema-spectral-rules
scopes:
- name: Tapfiliate Scopes
  scope_count: 4
  slug: tapfiliate-scopes
  summary_line: 4 scopes
score:
  band: exemplar
  composite: 69.6
  delta: -7.5
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 41.7
    contract_quality: 75.0
    developer_ergonomics: 73.2
    discoverability: 92.6
    governance: 41.7
    operational_transparency: 39.5
  previous_composite: 77.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/screenshots/tapfiliate-2026-06-20T194920.png
security:
- kind: authentication
  name: Tapfiliate Authentication
  slug: tapfiliate-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Tapfiliate Domain Security
  slug: tapfiliate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tapfiliate Vulnerability Disclosure
  slug: tapfiliate-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tapfiliate
tags:
- Affiliate Marketing
- Affiliate Tracking
- Commission Management
- Conversion Tracking
- Partner Programs
- Referral Programs
- Influencer Marketing
website: https://tapfiliate.com
---
