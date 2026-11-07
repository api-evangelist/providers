---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Handlediq Com Agentic Access
  operation_count: 8
  slug: handlediq-com-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- description: API for HandledIQ field service management platform.
  name: HandledIQ API
  slug: handlediq-api
- baseURL: https://app.handlediq.com/agents
  baseurl_source: declared
  description: The Booking Status API from handlediq-com — 1 operation(s) for booking status.
  name: handlediq-com Booking Status API
  slug: handlediq-com-booking-status-api
- baseURL: https://app.handlediq.com/agents
  baseurl_source: declared
  description: The Cancel Booking API from handlediq-com — 1 operation(s) for cancel booking.
  name: handlediq-com Cancel Booking API
  slug: handlediq-com-cancel-booking-api
- baseURL: https://app.handlediq.com/agents
  baseurl_source: declared
  description: The Find Help API from handlediq-com — 1 operation(s) for find help.
  name: handlediq-com Find Help API
  slug: handlediq-com-find-help-api
- baseURL: https://app.handlediq.com/agents
  baseurl_source: declared
  description: The Get Quote API from handlediq-com — 1 operation(s) for get quote.
  name: handlediq-com Get Quote API
  slug: handlediq-com-get-quote-api
- baseURL: https://app.handlediq.com/agents
  baseurl_source: declared
  description: The Hold Time API from handlediq-com — 1 operation(s) for hold time.
  name: handlediq-com Hold Time API
  slug: handlediq-com-hold-time-api
- baseURL: https://app.handlediq.com/agents
  baseurl_source: declared
  description: The Move Booking API from handlediq-com — 1 operation(s) for move booking.
  name: handlediq-com Move Booking API
  slug: handlediq-com-move-booking-api
- baseURL: https://app.handlediq.com/agents
  baseurl_source: declared
  description: The Request Service API from handlediq-com — 1 operation(s) for request service.
  name: handlediq-com Request Service API
  slug: handlediq-com-request-service-api
- baseURL: https://app.handlediq.com/agents
  baseurl_source: declared
  description: The Verify Record API from handlediq-com — 1 operation(s) for verify record.
  name: handlediq-com Verify Record API
  slug: handlediq-com-verify-record-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/handlediq-com/agentic-access/handlediq-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/handlediq-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/handlediq-com/rules/handlediq-com-rules.yml
  title: ''
  type: Spectral
  url: rules/handlediq-com-rules.yml
- group: design
  href: https://artifacts.apis.io/handlediq-com/json-ld/handlediq-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/handlediq-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/handlediq-com/vocabulary/handlediq-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/handlediq-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/handlediq-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/handlediq-com/data-model/handlediq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/handlediq-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/handlediq-com/errors/handlediq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/handlediq-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/handlediq-com/conformance/handlediq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/handlediq-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/handlediq-com/llms/handlediq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/handlediq-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/handlediq-com/mcp/handlediq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/handlediq-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/handlediq-com/well-known/handlediq-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/handlediq-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/handlediq-com/well-known/handlediq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/handlediq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/handlediq-com/hosts/handlediq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/handlediq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/handlediq-com/vendors/handlediq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/handlediq-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.handlediq.com
- group: auth
  href: https://artifacts.apis.io/handlediq-com/security/handlediq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/handlediq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://handlediq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.handlediq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://app.handlediq.com/agents/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://handlediq.com/try.md
- group: operate
  title: ''
  type: Support
  url: https://handlediq.com/contact.md
- group: commercial
  title: ''
  type: Pricing
  url: https://handlediq.com/product.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.handlediq.com/legal/terms.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.handlediq.com/legal/privacy.md
coverage:
  checked: '2026-10-30'
  detail: OpenAPI spec URLs redirect to a login page, indicating the API is behind a partner portal.
  evidence:
  - status: 303
    url: https://app.handlediq.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-30'
description: HandledIQ provides field service management software for home service contractors, offering scheduling, dispatch, estimates, invoicing, payments, payroll, and an AI assistant named Hoss. The platform runs the office, integrates with QuickBooks, Stripe, and other tools, and gives shop owners full data ownership. Shops can book appointments, manage technicians, and automate communications, while developers can access a documented OpenAPI specification for integration.
image: https://handlediq.com/kit/logos/logo-black.svg
jsonld:
- class_count: 1
  name: Handlediq Com Context
  property_count: 2
  slug: handlediq-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.handlediq.com.
  name: handlediq-com MCP Server
  slug: handlediq-com-mcp-yml
modified: '2026-10-30'
name: handlediq-com
nav: Providers
network: true
overview: 'handlediq-com publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Booking Status API, Cancel Booking API, Find Help API, and 6 more. Tagged areas include Field Service Management, Software-as-a-Service, Home Services, Scheduling, and Payments.


  The handlediq-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  handlediq-com''s developer surface includes API reference, getting-started guide, support, pricing, and 20 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: handlediq-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: handlediq-com-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 48.1
    developer_ergonomics: 18.5
    discoverability: 66.7
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/handlediq-com/handlediq-com-2026-11-03T133143.png
security:
- kind: domain-security
  name: Handlediq Com Domain Security
  slug: handlediq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 8
skills:
- name: booking-status
  slug: handlediq-com-booking_status
- name: cancel-booking
  slug: handlediq-com-cancel_booking
- name: find-help
  slug: handlediq-com-find_help
- name: get-quote
  slug: handlediq-com-get_quote
- name: hold-time
  slug: handlediq-com-hold_time
- name: move-booking
  slug: handlediq-com-move_booking
- name: request-service
  slug: handlediq-com-request_service
- name: verify-record
  slug: handlediq-com-verify_record
slug: handlediq-com
tags:
- Field Service Management
- Software-as-a-Service
- Home Services
- Scheduling
- Payments
- Artificial Intelligence
website: https://handlediq.com/
---
