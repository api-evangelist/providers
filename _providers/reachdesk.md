---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Reachdesk operates a first-party remote Model Context Protocol server at https://app.reachdesk.com/mcp, on the same host as its REST API. It is a hosted HTTP endpoint an MCP client POSTs to directly —
  name: Reachdesk MCP Server
  slug: reachdesk-mcp
- baseURL: https://app.reachdesk.com/api/v2
  baseurl_source: declared
  description: The Bulk Sends API from Reachdesk — 1 operation(s) for bulk sends.
  name: Reachdesk Bulk Sends API
  slug: reachdesk-bulk-sends-api
- baseURL: https://app.reachdesk.com/api/v2
  baseurl_source: declared
  description: The Campaigns API from Reachdesk — 1 operation(s) for campaigns.
  name: Reachdesk Campaigns API
  slug: reachdesk-campaigns-api
- baseURL: https://app.reachdesk.com/api/v2
  baseurl_source: declared
  description: The Contacts API from Reachdesk — 1 operation(s) for contacts.
  name: Reachdesk Contacts API
  slug: reachdesk-contacts-api
- baseURL: https://app.reachdesk.com/api/v2
  baseurl_source: declared
  description: The Gdpr API from Reachdesk — 2 operation(s) for gdpr.
  name: Reachdesk Gdpr API
  slug: reachdesk-gdpr-api
- baseURL: https://app.reachdesk.com/api/v2
  baseurl_source: declared
  description: The Organization API from Reachdesk — 1 operation(s) for organization.
  name: Reachdesk Organization API
  slug: reachdesk-organization-api
- baseURL: https://app.reachdesk.com/api/v2
  baseurl_source: declared
  description: The Sends API from Reachdesk — 1 operation(s) for sends.
  name: Reachdesk Sends API
  slug: reachdesk-sends-api
- baseURL: https://app.reachdesk.com/api/v2
  baseurl_source: declared
  description: The Transactions API from Reachdesk — 1 operation(s) for transactions.
  name: Reachdesk Transactions API
  slug: reachdesk-transactions-api
artifact_total: 25
asyncapis:
- description: ''
  name: Reachdesk Webhooks
  slug: reachdesk-webhooks
collections:
- collection_type: open
  name: Reachdesk API
  slug: open-reachdesk-api
common:
- group: other
  href: https://artifacts.apis.io/reachdesk/capabilities/reachdesk-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/reachdesk-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/reachdesk/authentication/reachdesk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/reachdesk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/reachdesk/security/reachdesk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reachdesk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reachdesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.reachdesk.com/hc/en-gb/categories/4404901379473-Integrations-API
- group: operate
  title: ''
  type: Support
  url: https://support.reachdesk.com/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://www.reachdesk.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reachdesk.com/pricing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reachdesk
- group: other
  title: ''
  type: X
  url: https://x.com/ReachdeskHQ
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/reachdesk
- group: commercial
  href: https://artifacts.apis.io/reachdesk/plans/reachdesk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reachdesk-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/reachdesk/rate-limits/reachdesk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reachdesk-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/reachdesk/finops/reachdesk-finops.yml
  title: ''
  type: FinOps
  url: finops/reachdesk-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://reachdesk.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://reachdesk.readme.io/reference/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://support.reachdesk.com/hc/en-gb/articles/29669486204305-Send-gifts-with-the-Reachdesk-Trigger-Campaign-API
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reachdesk.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reachdesk.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.reachdesk.com/users/sign_in
- group: agent
  href: https://artifacts.apis.io/reachdesk/well-known/reachdesk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/reachdesk-well-known.yml
- group: agent
  href: https://artifacts.apis.io/reachdesk/mcp/reachdesk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/reachdesk-mcp.yml
- group: build
  href: https://artifacts.apis.io/reachdesk/mcp/reachdesk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/reachdesk-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/reachdesk/scopes/reachdesk-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/reachdesk-scopes.yml
- group: design
  href: https://artifacts.apis.io/reachdesk/conventions/reachdesk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/reachdesk-conventions.yml
- group: design
  href: https://artifacts.apis.io/reachdesk/errors/reachdesk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/reachdesk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/reachdesk/data-model/reachdesk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reachdesk-data-model.yml
- group: design
  href: https://artifacts.apis.io/reachdesk/lifecycle/reachdesk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reachdesk-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/reachdesk/changelog/reachdesk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/reachdesk-changelog.yml
- group: design
  href: https://artifacts.apis.io/reachdesk/conformance/reachdesk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reachdesk-conformance.yml
- group: auth
  href: https://artifacts.apis.io/reachdesk/security/reachdesk-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/reachdesk-trust-center.yml
- group: design
  href: https://artifacts.apis.io/reachdesk/asyncapi/reachdesk-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/reachdesk-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/reachdesk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/reachdesk/packages/reachdesk-packages.yml
  title: ''
  type: Packages
  url: packages/reachdesk-packages.yml
- group: agent
  href: https://artifacts.apis.io/reachdesk/llms/reachdesk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reachdesk-llms.txt
- group: other
  href: https://artifacts.apis.io/reachdesk/overlays/reachdesk-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/reachdesk-api-overlay.yaml
created: '2026-06-13'
description: Reachdesk is a global B2B corporate gifting and direct mail platform that enables sales, marketing, and customer success teams to send physical gifts, branded merchandise, and digital rewards at scale. The Reachdesk REST API allows programmatic triggering of gift campaigns, integration with CRM and marketing automation tools, and management of sending workflows across 180+ countries. API tokens are generated via the platform settings and used to authenticate requests for campaign triggering and gift delivery operations.
finops:
- has_sources: true
  method: derived
  name: Reachdesk Finops
  primary_unit: order
  service_category: ''
  slug: reachdesk-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reachdesk.png
jsonld:
- class_count: 10
  name: Reachdesk Context
  property_count: 24
  slug: reachdesk-context
layout: provider
mcp_servers:
- description: 'Reachdesk operates a first-party remote MCP server on its own API host. It is a hosted HTTP endpoint an MCP client POSTs to directly — there is no npx/stdio package to install. Access is OAuth 2.1: th'
  name: Reachdesk MCP Server
  slug: reachdesk
modified: '2026-08-13'
name: Reachdesk
nav: Providers
network: true
overview: 'Reachdesk publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bulk Sends API, Campaigns API, Contacts API, and 5 more. Tagged areas include Corporate Gifting, Direct Mail, Swag, B2B, and Sales Enablement.


  The Reachdesk catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Reachdesk''s developer surface includes authentication, documentation, support, engineering blog, pricing, API reference, getting-started guide, and 29 more developer resources.'
plans:
- name: Reachdesk Plans Pricing
  plan_count: 5
  slug: reachdesk-plans-pricing
- name: Reachdesk Price Estimates
  plan_count: 0
  slug: reachdesk-price-estimates
random_paper: 2
rate_limits:
- limit_count: 0
  name: Reachdesk Rate Limits
  slug: reachdesk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Reachdesk API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 1
  slug: reachdesk-rules
scopes:
- name: Reachdesk Scopes
  scope_count: 2
  slug: reachdesk-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 61.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 67.5
    catalog_earned_first_party: 12.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.7
  facets:
    access_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 65.5
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 28.9
  previous_composite: 59.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/reachdesk/reachdesk-2026-06-20T192631.png
security:
- kind: authentication
  name: Reachdesk Authentication
  slug: reachdesk-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Reachdesk Domain Security
  slug: reachdesk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Reachdesk Trust Center
  slug: reachdesk-trust-center
  summary_line: verified, claimed, note
skill_count: 4
skills:
- name: reachdesk-bulk-send
  slug: reachdesk-bulk-send
- name: reachdesk-gdpr-request
  slug: reachdesk-gdpr-request
- name: reachdesk-reconcile-spend
  slug: reachdesk-reconcile-spend
- name: reachdesk-send-a-gift
  slug: reachdesk-send-a-gift
slug: reachdesk
tags:
- Corporate Gifting
- Direct Mail
- Swag
- B2B
- Sales Enablement
- Customer Success
- Marketing Automation
- Gifting Platform
- Rewards
- MCP
- AI Agents
- OpenAPI
website: https://www.reachdesk.com/
---
