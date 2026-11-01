---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Noerrands Com Agentic Access
  operation_count: 76
  slug: noerrands-com-agentic-access
  summary_line: 76 operations · 42 acting
api_count: 8
apis:
- baseURL: https://api.noerrands.com/c/booking
  baseurl_source: declared
  description: Appointments
  name: noerrands-com Booking API
  slug: noerrands-com-booking-api
- baseURL: https://api.noerrands.com/c/cards
  baseurl_source: declared
  description: Greeting cards
  name: noerrands-com Cards API
  slug: noerrands-com-cards-api
- baseURL: https://api.noerrands.com/c/fax
  baseurl_source: declared
  description: Faxing
  name: noerrands-com Fax API
  slug: noerrands-com-fax-api
- baseURL: https://api.noerrands.com/c/mail
  baseurl_source: declared
  description: Physical mail
  name: noerrands-com Mail API
  slug: noerrands-com-mail-api
- baseURL: https://api.noerrands.com/c/prints
  baseurl_source: declared
  description: Photo prints, canvas, custom T-shirts and mugs
  name: noerrands-com Prints API
  slug: noerrands-com-prints-api
- baseURL: https://api.noerrands.com/c/ship
  baseurl_source: declared
  description: Shipping labels, pickups and tracking
  name: noerrands-com Ship API
  slug: noerrands-com-ship-api
- baseURL: https://api.noerrands.com/c/sign
  baseurl_source: declared
  description: Electronic signature envelopes
  name: noerrands-com Sign API
  slug: noerrands-com-sign-api
- baseURL: https://api.noerrands.com/c/tables
  baseurl_source: declared
  description: Restaurant table requests
  name: noerrands-com Tables API
  slug: noerrands-com-tables-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/noerrands-com/agentic-access/noerrands-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/noerrands-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/noerrands-com/rate-limits/noerrands-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/noerrands-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/noerrands-com/rules/noerrands-com-rules.yml
  title: ''
  type: Spectral
  url: rules/noerrands-com-rules.yml
- group: design
  href: https://artifacts.apis.io/noerrands-com/json-ld/noerrands-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/noerrands-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/noerrands-com/vocabulary/noerrands-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/noerrands-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/noerrands-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/noerrands-com/data-model/noerrands-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/noerrands-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/noerrands-com/conventions/noerrands-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/noerrands-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/noerrands-com/conventions/noerrands-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/noerrands-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/noerrands-com/authentication/noerrands-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/noerrands-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/noerrands-com/scopes/noerrands-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/noerrands-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/noerrands-com/errors/noerrands-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/noerrands-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/noerrands-com/conformance/noerrands-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/noerrands-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/noerrands-com/llms/noerrands-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/noerrands-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/noerrands-com/mcp/noerrands-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/noerrands-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/noerrands-com/well-known/noerrands-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/noerrands-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/noerrands-com/hosts/noerrands-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/noerrands-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/noerrands-com/vendors/noerrands-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/noerrands-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/noerrands-com/security/noerrands-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/noerrands-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://noerrands.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://noerrands.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://noerrands.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://noerrands.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://noerrands.com/get-key/
- group: operate
  title: ''
  type: Support
  url: https://noerrands.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://noerrands.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://noerrands.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://noerrands.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://noerrands.com/get-key/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.noerrands.com/mcp
  - status: 200
    url: https://noerrands.com/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: No Errands offers an AI‑driven service platform that lets developers programmatically request real‑world tasks such as mailing letters or postcards, sending faxes, booking appointments, reserving restaurant tables, creating shipping or return labels, printing and posting photos, sending greeting cards, arranging same‑day courier deliveries, and obtaining document signatures. Users obtain an API key, embed a single prompt into their AI agent, and the platform handles the logistics, providing a seamless bridge between digital assistants and physical services. This unified API abstracts complex physical workflows into simple programmable calls, empowering AI‑enabled applications to act in the real world without manual handling.
image: https://noerrands.com/og.png
jsonld:
- class_count: 7
  name: Noerrands Com Context
  property_count: 17
  slug: noerrands-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.noerrands.com.
  name: noerrands-com MCP Server
  slug: noerrands-com-mcp-yml
modified: '2026-10-29'
name: noerrands-com
nav: Providers
network: true
overview: 'noerrands-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Booking API, Cards API, Fax API, and 5 more. Tagged areas include Company, AI, Automation, Productivity, and Messaging.


  The noerrands-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  noerrands-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Noerrands Com Plans Pricing
  plan_count: 0
  slug: noerrands-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Noerrands Com Rate Limits
  slug: noerrands-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: noerrands-com API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: noerrands-com-rules
scopes:
- name: Noerrands Com Scopes
  scope_count: 0
  slug: noerrands-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 58.9
    developer_ergonomics: 61.2
    discoverability: 70.0
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Noerrands Com Authentication
  slug: noerrands-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Noerrands Com Domain Security
  slug: noerrands-com-domain-security
  summary_line: TLSv1.3
skill_count: 8
skills:
- name: noerrands-com-booking-skill
  slug: noerrands-com-booking-skill
- name: noerrands-com-cards-skill
  slug: noerrands-com-cards-skill
- name: noerrands-com-fax-skill
  slug: noerrands-com-fax-skill
- name: noerrands-com-mail-skill
  slug: noerrands-com-mail-skill
- name: noerrands-com-prints-skill
  slug: noerrands-com-prints-skill
- name: noerrands-com-ship-skill
  slug: noerrands-com-ship-skill
- name: noerrands-com-sign-skill
  slug: noerrands-com-sign-skill
- name: noerrands-com-tables-skill
  slug: noerrands-com-tables-skill
slug: noerrands-com
tags:
- Company
- AI
- Automation
- Productivity
- Messaging
website: https://noerrands.com/
---
