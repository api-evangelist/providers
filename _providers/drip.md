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
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Drip Agentic Access
  operation_count: 22
  slug: drip-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 1
apis:
- description: 'REST API for Drip exposing subscribers, tags, custom fields, broadcasts, email campaigns, events, conversions, workflows, shopper activity (orders, carts, products), purchases, and webhooks. Supports '
  name: Drip REST API
  slug: drip-api
- baseURL: https://api.getdrip.com/v2
  baseurl_source: declared
  description: The Accounts API from Drip — 2 operation(s) for accounts.
  name: Drip Accounts API
  slug: drip-accounts-api
- baseURL: https://api.getdrip.com/v2
  baseurl_source: declared
  description: The Broadcasts API from Drip — 2 operation(s) for broadcasts.
  name: Drip Broadcasts API
  slug: drip-broadcasts-api
- baseURL: https://api.getdrip.com/v2
  baseurl_source: declared
  description: The Campaigns API from Drip — 5 operation(s) for campaigns.
  name: Drip Campaigns API
  slug: drip-campaigns-api
- baseURL: https://api.getdrip.com/v2
  baseurl_source: declared
  description: The Conversions API from Drip — 1 operation(s) for conversions.
  name: Drip Conversions API
  slug: drip-conversions-api
- baseURL: https://api.getdrip.com/v2
  baseurl_source: declared
  description: The Custom Fields API from Drip — 1 operation(s) for custom fields.
  name: Drip Custom Fields API
  slug: drip-custom-fields-api
- baseURL: https://api.getdrip.com/v2
  baseurl_source: declared
  description: The Events API from Drip — 3 operation(s) for events.
  name: Drip Events API
  slug: drip-events-api
- baseURL: https://api.getdrip.com/v2
  baseurl_source: declared
  description: The Forms API from Drip — 1 operation(s) for forms.
  name: Drip Forms API
  slug: drip-forms-api
- baseURL: https://api.getdrip.com/v2
  baseurl_source: declared
  description: The Orders API from Drip — 1 operation(s) for orders.
  name: Drip Orders API
  slug: drip-orders-api
- baseURL: https://api.getdrip.com/v2
  baseurl_source: declared
  description: The Shopper Activity API from Drip — 3 operation(s) for shopper activity.
  name: Drip Shopper Activity API
  slug: drip-shopper-activity-api
- baseURL: https://api.getdrip.com/v2
  baseurl_source: declared
  description: The Subscribers API from Drip — 2 operation(s) for subscribers.
  name: Drip Subscribers API
  slug: drip-subscribers-api
- description: Drip operates a remote Model Context Protocol server at https://api.getdrip.com/mcp, protected by its OAuth 2.0 authorization server and discoverable through RFC 9728 protected-resource metadata. Prob
  name: Drip MCP Server
  slug: drip-mcp
artifact_total: 39
asyncapis:
- description: ''
  name: Drip Webhooks
  slug: drip-webhooks
collections:
- collection_type: open
  name: Drip REST Accounts API
  slug: open-drip-accounts-api
- collection_type: open
  name: Drip REST Accounts Broadcasts API
  slug: open-drip-broadcasts-api
- collection_type: open
  name: Drip REST Accounts Campaigns API
  slug: open-drip-campaigns-api
- collection_type: open
  name: Drip REST Accounts Conversions API
  slug: open-drip-conversions-api
- collection_type: open
  name: Drip REST Accounts Custom Fields API
  slug: open-drip-custom-fields-api
- collection_type: open
  name: Drip REST Accounts Events API
  slug: open-drip-events-api
- collection_type: open
  name: Drip REST Accounts Forms API
  slug: open-drip-forms-api
- collection_type: open
  name: Drip REST Accounts Orders API
  slug: open-drip-orders-api
- collection_type: open
  name: Drip REST Accounts Shopper Activity API
  slug: open-drip-shopper-activity-api
- collection_type: open
  name: Drip REST Accounts Subscribers API
  slug: open-drip-subscribers-api
- collection_type: open
  name: Drip REST API
  slug: open-drip
common:
- group: other
  href: https://artifacts.apis.io/drip/capabilities/drip-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/drip-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/drip/agentic-access/drip-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/drip-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/drip/security/drip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drip-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/drip/authentication/drip-authentication.yml
  title: ''
  type: Authentication
  url: authentication/drip-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getdrip
- group: company
  title: ''
  type: Website
  url: https://www.drip.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.drip.com/
- group: start
  title: ''
  type: Signup
  url: https://www.drip.com/forms/79091116/submissions/new
- group: commercial
  title: ''
  type: Pricing
  url: https://www.drip.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.getdrip.com/login
- group: operate
  title: ''
  type: Support
  url: https://help.drip.com/
- group: company
  title: ''
  type: Blog
  url: https://www.drip.com/learn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DripEmail
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.drip.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.drip.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.drip.com/#introduction
- group: operate
  title: ''
  type: StatusPage
  url: https://status.drip.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.drip.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.drip.com/privacy
- group: build
  href: https://artifacts.apis.io/drip/packages/drip-packages.yml
  title: ''
  type: Packages
  url: packages/drip-packages.yml
- group: build
  href: https://artifacts.apis.io/drip/packages/drip-packages.yml
  title: ''
  type: SDKs
  url: packages/drip-packages.yml
- group: agent
  href: https://artifacts.apis.io/drip/well-known/drip-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drip-well-known.yml
- group: auth
  href: https://artifacts.apis.io/drip/well-known/drip-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/drip-security.txt
- group: auth
  href: https://artifacts.apis.io/drip/security/drip-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/drip-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/drip/security/drip-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/drip-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/drip/scopes/drip-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/drip-scopes.yml
- group: design
  href: https://artifacts.apis.io/drip/conventions/drip-conventions.yml
  title: ''
  type: Conventions
  url: conventions/drip-conventions.yml
- group: design
  href: https://artifacts.apis.io/drip/errors/drip-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/drip-problem-types.yml
- group: design
  href: https://artifacts.apis.io/drip/lifecycle/drip-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/drip-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/drip/conformance/drip-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drip-conformance.yml
- group: design
  href: https://artifacts.apis.io/drip/data-model/drip-data-model.yml
  title: ''
  type: DataModel
  url: data-model/drip-data-model.yml
- group: design
  href: https://artifacts.apis.io/drip/components/drip-components.yml
  title: ''
  type: Components
  url: components/drip-components.yml
- group: design
  href: https://artifacts.apis.io/drip/asyncapi/drip-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/drip-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/drip/rate-limits/drip-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/drip-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/drip/plans/drip-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/drip-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/drip/llms/drip-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drip-llms.txt
- group: agent
  href: https://artifacts.apis.io/drip/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-05-11'
description: Drip is an email marketing and marketing automation platform built for ecommerce brands that combines subscriber management, segmentation, email campaigns, automation workflows, and shopper activity tracking. The Drip REST API gives programmatic access to subscribers, campaigns, events, workflows, broadcasts, orders, carts, and webhooks using either API token Basic authentication or OAuth 2.0.
finops:
- has_sources: true
  method: derived
  name: Drip Finops
  primary_unit: month for 1-2,500 people
  service_category: ''
  slug: drip-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drip.png
layout: provider
mcp_servers:
- description: 'Drip operates a real, reachable remote MCP server at https://api.getdrip.com/mcp. It is discoverable the standards-compliant way: the API host publishes RFC 9728 OAuth protected-resource metadata nami'
  name: Drip MCP Server
  slug: drip
modified: '2026-08-13'
name: Drip
nav: Providers
network: true
overview: 'Drip publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Broadcasts API, Campaigns API, and 9 more. Tagged areas include Email Marketing, Marketing Automation, E-Commerce, Customer Engagement, and Campaigns.


  The Drip catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Drip''s developer surface includes authentication, documentation, signup flow, pricing, support, engineering blog, API reference, and 30 more developer resources.'
plans:
- name: Drip Plans Pricing
  plan_count: 1
  slug: drip-plans-pricing
- name: Drip Price Estimates
  plan_count: 0
  slug: drip-price-estimates
random_paper: 23
rate_limits:
- limit_count: 6
  name: Drip Rate Limits
  slug: drip-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Drip API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: drip-rules
scopes:
- name: Drip Scopes
  scope_count: 2
  slug: drip-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 62.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 67.1
    contract_governance: 31.8
    contract_quality: 52.8
    developer_ergonomics: 54.2
    discoverability: 75.0
    operational_transparency: 68.4
  previous_composite: 62.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/drip/drip-2026-06-20T180233.png
security:
- kind: authentication
  name: Drip Authentication
  slug: drip-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Drip Domain Security
  slug: drip-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Drip Vulnerability Disclosure
  slug: drip-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 4
skills:
- name: Enroll a subscriber in an email series campaign
  slug: drip-enroll-in-campaign
- name: Bulk import subscribers into Drip
  slug: drip-import-subscribers
- name: Record subscriber events in Drip
  slug: drip-record-events
- name: Sync ecommerce shopper activity to Drip
  slug: drip-sync-shopper-activity
slug: drip
tags:
- Email Marketing
- Marketing Automation
- E-Commerce
- Customer Engagement
- Campaigns
- Workflows
website: https://www.drip.com
---
