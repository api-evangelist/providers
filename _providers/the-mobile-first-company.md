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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: Pre-computed call metrics, team performance, and outbound dial funnel
  name: The Mobile First Company Analytics API
  slug: the-mobile-first-company-analytics-api
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: Retrieve and search call records with filtering and pagination. Filter calls by your Allo phone number.
  name: The Mobile First Company Calls API
  slug: the-mobile-first-company-calls-api
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: Search and retrieve contact information with sorting and pagination. Includes engagement level tracking.
  name: The Mobile First Company Contacts API
  slug: the-mobile-first-company-contacts-api
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: The Conversations API from The Mobile First Company — 7 operation(s) for conversations.
  name: The Mobile First Company Conversations API
  slug: the-mobile-first-company-conversations-api
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: Manage people, companies, and deals in your CRM.
  name: The Mobile First Company CRM API
  slug: the-mobile-first-company-crm-api
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: The Partner API from The Mobile First Company — 2 operation(s) for partner.
  name: The Mobile First Company Partner API
  slug: the-mobile-first-company-partner-api
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: Retrieve information about your Allo phone numbers.
  name: The Mobile First Company Phone Numbers API
  slug: the-mobile-first-company-phone-numbers-api
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: The Power Dialer API from The Mobile First Company — 2 operation(s) for power dialer.
  name: The Mobile First Company Power Dialer API
  slug: the-mobile-first-company-power-dialer-api
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: Send SMS messages to phone numbers using your Allo numbers.
  name: The Mobile First Company SMS API
  slug: the-mobile-first-company-sms-api
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: Manage call summary templates that control how AI-generated call summaries are structured for your team.
  name: The Mobile First Company Summary Templates API
  slug: the-mobile-first-company-summary-templates-api
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: The Tags API from The Mobile First Company — 3 operation(s) for tags.
  name: The Mobile First Company Tags API
  slug: the-mobile-first-company-tags-api
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: The Users API from The Mobile First Company — 3 operation(s) for users.
  name: The Mobile First Company Users API
  slug: the-mobile-first-company-users-api
- baseURL: https://api.withallo.com
  baseurl_source: declared
  description: Manage webhook endpoints to receive real-time notifications about events in your Allo account. Each endpoint subscribes to one or more event topics and is verified with a signing secret.
  name: The Mobile First Company Webhooks API
  slug: the-mobile-first-company-webhooks-api
artifact_total: 39
asyncapis:
- description: ''
  name: The Mobile First Company Webhooks
  slug: the-mobile-first-company-webhooks
collections:
- collection_type: open
  name: Allo Analytics API
  slug: open-the-mobile-first-company-analytics-api
- collection_type: open
  name: Allo Analytics Calls API
  slug: open-the-mobile-first-company-calls-api
- collection_type: open
  name: Allo Analytics Contacts API
  slug: open-the-mobile-first-company-contacts-api
- collection_type: open
  name: Allo Analytics Conversations API
  slug: open-the-mobile-first-company-conversations-api
- collection_type: open
  name: Allo Analytics CRM API
  slug: open-the-mobile-first-company-crm-api
- collection_type: open
  name: Allo Analytics Partner API
  slug: open-the-mobile-first-company-partner-api
- collection_type: open
  name: Allo Analytics Phone Numbers API
  slug: open-the-mobile-first-company-phone-numbers-api
- collection_type: open
  name: Allo Analytics Power Dialer API
  slug: open-the-mobile-first-company-power-dialer-api
- collection_type: open
  name: Allo Analytics SMS API
  slug: open-the-mobile-first-company-sms-api
- collection_type: open
  name: Allo Analytics Summary Templates API
  slug: open-the-mobile-first-company-summary-templates-api
- collection_type: open
  name: Allo Analytics Tags API
  slug: open-the-mobile-first-company-tags-api
- collection_type: open
  name: Allo Analytics Users API
  slug: open-the-mobile-first-company-users-api
- collection_type: open
  name: Allo Analytics Webhooks API
  slug: open-the-mobile-first-company-webhooks-api
common:
- group: operate
  href: https://artifacts.apis.io/the-mobile-first-company/rate-limits/the-mobile-first-company-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/the-mobile-first-company-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/the-mobile-first-company/plans/the-mobile-first-company-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/the-mobile-first-company-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/the-mobile-first-company/capabilities/the-mobile-first-company-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/the-mobile-first-company-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/the-mobile-first-company/security/the-mobile-first-company-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-mobile-first-company-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/the-mobile-first-company/authentication/the-mobile-first-company-authentication.yml
  title: ''
  type: Authentication
  url: authentication/the-mobile-first-company-authentication.yml
- group: docs
  href: https://artifacts.apis.io/the-mobile-first-company/openapi/_original/the-mobile-first-company-allo-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/the-mobile-first-company-allo-openapi.json
- group: other
  href: https://artifacts.apis.io/the-mobile-first-company/overlays/the-mobile-first-company-allo-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-mobile-first-company-allo-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/the-mobile-first-company/scopes/the-mobile-first-company-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/the-mobile-first-company-scopes.yml
- group: design
  href: https://artifacts.apis.io/the-mobile-first-company/conventions/the-mobile-first-company-conventions.yml
  title: ''
  type: Conventions
  url: conventions/the-mobile-first-company-conventions.yml
- group: design
  href: https://artifacts.apis.io/the-mobile-first-company/conventions/the-mobile-first-company-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/the-mobile-first-company-conventions.yml
- group: design
  href: https://artifacts.apis.io/the-mobile-first-company/errors/the-mobile-first-company-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/the-mobile-first-company-problem-types.yml
- group: design
  href: https://artifacts.apis.io/the-mobile-first-company/lifecycle/the-mobile-first-company-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/the-mobile-first-company-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.withallo.com
- group: design
  href: https://artifacts.apis.io/the-mobile-first-company/conformance/the-mobile-first-company-conformance.yml
  title: ''
  type: Conformance
  url: conformance/the-mobile-first-company-conformance.yml
- group: design
  href: https://artifacts.apis.io/the-mobile-first-company/data-model/the-mobile-first-company-data-model.yml
  title: ''
  type: DataModel
  url: data-model/the-mobile-first-company-data-model.yml
- group: operate
  href: https://artifacts.apis.io/the-mobile-first-company/changelog/the-mobile-first-company-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/the-mobile-first-company-changelog.yml
- group: design
  href: https://artifacts.apis.io/the-mobile-first-company/asyncapi/the-mobile-first-company-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/the-mobile-first-company-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/the-mobile-first-company/mcp/the-mobile-first-company-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/the-mobile-first-company-mcp.yml
- group: agent
  href: https://artifacts.apis.io/the-mobile-first-company/llms/the-mobile-first-company-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/the-mobile-first-company-llms.txt
- group: agent
  href: https://artifacts.apis.io/the-mobile-first-company/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/the-mobile-first-company/well-known/the-mobile-first-company-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/the-mobile-first-company-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.withallo.com/en/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.withallo.com/en/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://help.withallo.com/en/v2/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://help.withallo.com/en/get-started
- group: company
  title: ''
  type: Website
  url: https://www.withallo.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.withallo.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.withallo.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@withallo.com
- group: start
  title: ''
  type: Login
  url: https://web.withallo.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.withallo.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withallo.com/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: https://www.withallo.com/mcp
created: '2026-07-17'
description: The Mobile-First Company is a French / US (Miami HQ) startup building a suite of mobile-first, AI-powered business apps for small teams under a "one problem, one app" philosophy. Its flagship product, Allo, is an AI phone system used by 5,000+ businesses — an AI receptionist that answers 24/7, call recording with transcription and AI summaries, intelligent routing, spam blocking, SMS, and CRM sync. Allo ships a full REST API (calls, SMS, contacts, CRM, analytics, webhooks), a hosted Model Context Protocol (MCP) server, and OAuth 2.0. Sibling apps Due (invoicing) and Claim (expenses) extend the same approach. The company is backed by Base10 Partners and Lightspeed Venture Partners.
finops:
- has_sources: true
  method: derived
  name: The Mobile First Company Finops
  primary_unit: user
  service_category: ''
  slug: the-mobile-first-company-finops
  template: false
image: https://cdn.prod.website-files.com/678d02bf3966a86060a3c142/6a461aa199bb23ab1e5eb686_Allo_Logo_Allo_0.svg
layout: provider
mcp_servers:
- description: Official hosted (remote) Model Context Protocol server for Allo, the AI phone system by The Mobile-First Company. Exposes Allo's call/SMS/CRM surface to AI agents with the same permissions the connect
  name: Allo MCP Server
  slug: allo-mcp-server
- description: ''
  name: The Mobile First Company MCP Server
  slug: mcp
modified: '2026-07-21'
name: The Mobile First Company
nav: Providers
network: true
overview: 'The Mobile First Company publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Calls API, Contacts API, and 10 more. Tagged areas include Company, Communications, Telephony, Voice, and SMS.


  The The Mobile First Company catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  The Mobile First Company''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, pricing, engineering blog, and 26 more developer resources.'
plans:
- name: The Mobile First Company Plans Pricing
  plan_count: 10
  slug: the-mobile-first-company-plans-pricing
- name: The Mobile First Company Price Estimates
  plan_count: 0
  slug: the-mobile-first-company-price-estimates
random_paper: 23
rate_limits:
- limit_count: 2
  name: The Mobile First Company Rate Limits
  slug: the-mobile-first-company-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: The Mobile First Company API Rules
  rule_count: 66
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 13
  slug: the-mobile-first-company-rules
scopes:
- name: The Mobile First Company Scopes
  scope_count: 22
  slug: the-mobile-first-company-scopes
  summary_line: 22 scopes
score:
  band: strong
  composite: 65.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 31.8
    contract_quality: 62.6
    developer_ergonomics: 58.9
    discoverability: 71.7
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 65.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/the-mobile-first-company/the-mobile-first-company-2026-08-17T082339.png
security:
- kind: authentication
  name: The Mobile First Company Authentication
  slug: the-mobile-first-company-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: The Mobile First Company Domain Security
  slug: the-mobile-first-company-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: send-sms-follow-up
  slug: the-mobile-first-company-send-sms-follow-up
- name: sync-completed-calls-to-crm
  slug: the-mobile-first-company-sync-completed-calls-to-crm
slug: the-mobile-first-company
tags:
- Company
- Communications
- Telephony
- Voice
- SMS
- CRM
- Artificial Intelligence
- MCP
- Webhook
- Small Business
website: https://www.withallo.com
---
