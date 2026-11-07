---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Instasent Agentic Access
  operation_count: 132
  slug: instasent-agentic-access
  summary_line: 132 operations · 39 acting
api_count: 4
apis:
- baseURL: https://api.instasent.com
  baseurl_source: declared
  description: Account related operations
  name: Instasent Account API
  slug: instasent-account-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: Curated Analytics & Reporting endpoints. A small, bounded, strongly-typed reporting surface over the same engines that power the dashboard. Reports come in two shapes — **values** (aggregate totals ov
  name: Instasent Analytics API
  slug: instasent-analytics-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: 'What has broken, or is about to, for a project and the organization behind it. The counterpart of readiness: readiness answers what is left to configure, this answers what is wrong. One fact has one o'
  name: Instasent Attention API
  slug: instasent-attention-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: Audience contact management, search, and filtering endpoints
  name: Instasent Audience API
  slug: instasent-audience-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: Automation management endpoints for viewing automation details
  name: Instasent Automation API
  slug: instasent-automation-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: Campaign management endpoints for viewing campaign details
  name: Instasent Campaign API
  slug: instasent-campaign-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: The contacts API from Instasent — 2 operation(s) for contacts.
  name: Instasent Contacts API
  slug: instasent-contacts-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: Data source management endpoints for creating and managing data sources
  name: Instasent Datasource API
  slug: instasent-datasource-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: The events API from Instasent — 1 operation(s) for events.
  name: Instasent Events API
  slug: instasent-events-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: 'Flow discovery endpoints (read-only): list flows and their versions to find the ids the flow analytics endpoints take. Flows are built and managed in the dashboard; this surface exists so analytics co'
  name: Instasent Flow API
  slug: instasent-flow-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: General API endpoints for authentication and organization information
  name: Instasent General API
  slug: instasent-general-api
- baseURL: https://api.instasent.com
  baseurl_source: declared
  description: Lookup related operations
  name: Instasent Lookup API
  slug: instasent-lookup-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: 'OAuth 2.1 endpoints — Dynamic Client Registration, the token endpoint, and the discovery metadata that lets a client find them. They exist so a third-party application (or an MCP client) can obtain a '
  name: Instasent OAuth API
  slug: instasent-oauth-api
- baseURL: https://api.instasent.com
  baseurl_source: declared
  description: Price related operations
  name: Instasent Price API
  slug: instasent-price-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: Project management and configuration endpoints
  name: Instasent Project API
  slug: instasent-project-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: RCS sender (agent) management endpoints
  name: Instasent Rcs Sender API
  slug: instasent-rcs-sender-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: Setup readiness endpoints — "what's left to configure" and "what needs attention" for a project or one of its channels, plus the real per-country send capability. Always recomputed from current data (
  name: Instasent Readiness API
  slug: instasent-readiness-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: 'A country''s registration paperwork for one sender: sign a letter, allowlist a verifier, email an operator. Not the setup checklist, which is product configuration and lives under `readiness` — a proje'
  name: Instasent Registration API
  slug: instasent-registration-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: Segment management endpoints for creating and managing audience segments
  name: Instasent Segment API
  slug: instasent-segment-api
- baseURL: https://api.instasent.com
  baseurl_source: declared
  description: Sms related operations
  name: Instasent Sms API
  slug: instasent-sms-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: SMS sender management endpoints
  name: Instasent Sms Sender API
  slug: instasent-sms-sender-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: The specifications API from Instasent — 4 operation(s) for specifications.
  name: Instasent Specifications API
  slug: instasent-specifications-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: Stream endpoints for ingesting contacts and events into data sources
  name: Instasent Stream API
  slug: instasent-stream-api
- baseURL: https://api.instasent.com/v1
  baseurl_source: declared
  description: Other endpoints intendend for external services integration
  name: Instasent Third Party API
  slug: instasent-third-party-api
artifact_total: 37
common:
- group: other
  href: https://artifacts.apis.io/instasent/capabilities/instasent-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/instasent-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/instasent/agentic-access/instasent-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/instasent-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/instasent/rate-limits/instasent-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/instasent-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/instasent/rules/instasent-rules.yml
  title: ''
  type: Spectral
  url: rules/instasent-rules.yml
- group: design
  href: https://artifacts.apis.io/instasent/json-ld/instasent-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/instasent-context.jsonld
- group: design
  href: https://artifacts.apis.io/instasent/vocabulary/instasent-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/instasent-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/instasent/data-model/instasent-data-model.yml
  title: ''
  type: DataModel
  url: data-model/instasent-data-model.yml
- group: design
  href: https://artifacts.apis.io/instasent/errors/instasent-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/instasent-problem-types.yml
- group: design
  href: https://artifacts.apis.io/instasent/conformance/instasent-conformance.yml
  title: ''
  type: Conformance
  url: conformance/instasent-conformance.yml
- group: agent
  href: https://artifacts.apis.io/instasent/llms/instasent-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/instasent-llms.txt
- group: auth
  href: https://artifacts.apis.io/instasent/well-known/instasent-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/instasent-help-security.txt
- group: agent
  href: https://artifacts.apis.io/instasent/well-known/instasent-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/instasent-well-known.yml
- group: other
  href: https://artifacts.apis.io/instasent/hosts/instasent-hosts.yml
  title: ''
  type: Hosts
  url: hosts/instasent-hosts.yml
- group: other
  href: https://artifacts.apis.io/instasent/vendors/instasent-vendors.yml
  title: ''
  type: Vendors
  url: vendors/instasent-vendors.yml
- group: build
  href: https://artifacts.apis.io/instasent/packages/instasent-packages.yml
  title: ''
  type: SDKs
  url: packages/instasent-packages.yml
- group: build
  href: https://artifacts.apis.io/instasent/packages/instasent-packages.yml
  title: ''
  type: Packages
  url: packages/instasent-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.instasent.com/en/legal/terms/
- group: operate
  title: ''
  type: Support
  url: https://help.instasent.com/es/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instasent.com/en/legal/privacy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.instasent.com\\\
- group: auth
  href: https://artifacts.apis.io/instasent/authentication/instasent-authentication.yml
  title: ''
  type: Authentication
  url: authentication/instasent-authentication.yml
- group: auth
  href: https://artifacts.apis.io/instasent/scopes/instasent-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/instasent-scopes.yml
- group: auth
  href: https://artifacts.apis.io/instasent/security/instasent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/instasent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://instasent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.instasent.com/platform/en/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.instasent.com/platform-api/getting-started/choose-your-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.instasent.com/platform-api/getting-started/introduction/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.instasent.com/en/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.instasent.com/en/blog/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.instasent.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instasent
- group: other
  title: ''
  type: Image
  url: https://www.instasent.com/favicon.ico
created: '2026-10-28'
description: Instasent offers a cloud‑based messaging platform that enables businesses to send SMS, RCS and WhatsApp messages. It combines a customer data platform with AI agents that help create segments, draft campaigns and automate flows, while providing a robust API and extensive integrations for developers.
image: https://www.instasent.com/og/en/home.png
json_schemas:
- name: AttributeSpec
  property_count: 21
  slug: instasent-attribute-spec
- name: AudienceContext
  property_count: 7
  slug: instasent-audience-context
- name: CampaignSummary
  property_count: 6
  slug: instasent-campaign-summary
- name: FlowTemplate
  property_count: 23
  slug: instasent-flow-template
- name: ResponseProjectItem
  property_count: 15
  slug: instasent-response-project-item
- name: ResponseSmsItem
  property_count: 23
  slug: instasent-response-sms-item
jsonld:
- class_count: 102
  name: Instasent Context
  property_count: 386
  slug: instasent-context
layout: provider
modified: '2026-10-28'
name: Instasent
nav: Providers
network: true
overview: 'Instasent publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Analytics API, Attention API, and 21 more. Tagged areas include Company, Messaging, SMS, RCS, and WhatsApp.


  The Instasent catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Instasent''s developer surface includes support, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 25 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 3
  name: Instasent Rate Limits
  slug: instasent-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Instasent API Rules
  rule_count: 18
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 8
  slug: instasent-rules
scopes:
- name: Instasent Scopes
  scope_count: 16
  slug: instasent-scopes
  summary_line: 16 scopes · authorizationCode
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 65.2
    developer_ergonomics: 41.7
    discoverability: 78.6
    operational_transparency: 44.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 29.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/instasent/instasent-2026-11-03T133853.png
security:
- kind: authentication
  name: Instasent Authentication
  slug: instasent-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Instasent Domain Security
  slug: instasent-domain-security
  summary_line: TLSv1.3 · DMARC
slug: instasent
tags:
- Company
- Messaging
- SMS
- RCS
- WhatsApp
- Artificial Intelligence
- Marketing
website: https://instasent.com/
---
