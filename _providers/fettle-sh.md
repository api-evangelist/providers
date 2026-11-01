---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public REST API for Fettle uptime monitoring service
  name: fettle API
  slug: fettle-api
- description: 'fettle.sh Api API: 136 operations.'
  name: fettle.sh Api API
  slug: fettle-sh-api-api
artifact_total: 18
asyncapis:
- description: ''
  name: Fettle Sh Webhooks
  slug: fettle-sh-webhooks
common:
- group: design
  href: https://artifacts.apis.io/fettle-sh/rules/fettle-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/fettle-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/fettle-sh/json-ld/fettle-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fettle-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/fettle-sh/vocabulary/fettle-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fettle-sh-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fettle-sh/conformance/fettle-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fettle-sh-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/fettle-sh/plans/fettle-sh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fettle-sh-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fettle-sh/asyncapi/fettle-sh-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fettle-sh-webhooks.yml
- group: design
  href: https://artifacts.apis.io/fettle-sh/data-model/fettle-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fettle-sh-data-model.yml
- group: auth
  href: https://artifacts.apis.io/fettle-sh/security/fettle-sh-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/fettle-sh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fettle-sh/authentication/fettle-sh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fettle-sh-authentication.yml
- group: design
  href: https://artifacts.apis.io/fettle-sh/errors/fettle-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fettle-sh-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/fettle-sh/llms/fettle-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fettle-sh-llms.txt
- group: auth
  href: https://artifacts.apis.io/fettle-sh/well-known/fettle-sh-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fettle-sh-security.txt
- group: agent
  href: https://artifacts.apis.io/fettle-sh/well-known/fettle-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fettle-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/fettle-sh/hosts/fettle-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fettle-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/fettle-sh/vendors/fettle-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fettle-sh-vendors.yml
- group: build
  href: https://artifacts.apis.io/fettle-sh/packages/fettle-sh-packages.yml
  title: ''
  type: SDKs
  url: packages/fettle-sh-packages.yml
- group: build
  href: https://artifacts.apis.io/fettle-sh/packages/fettle-sh-packages.yml
  title: ''
  type: Packages
  url: packages/fettle-sh-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fettle.sh/fettle-platform
- group: start
  title: ''
  type: Login
  url: https://fettle.sh/login
- group: start
  title: ''
  type: GettingStarted
  url: https://fettle.sh/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/fettle-sh/security/fettle-sh-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fettle-sh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fettle-sh/security/fettle-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fettle-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fettle.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://fettle.sh/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://fettle.sh/pricing
- group: company
  title: ''
  type: Blog
  url: https://fettle.sh/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fettle.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fettle.sh/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://api.fettle.sh/public-api/docs
created: '2026-10-30'
description: Fettle provides hosted uptime monitoring services tailored for developers and their AI agents. It offers HTTP, TCP, ping, DNS, SSL checks across multiple regions, along with cron job heartbeats. The platform includes a public REST API and an MCP server on every plan, enabling integration and automation for monitoring tasks. Paid plans start at $9/month, with a free tier available.
image: https://fettle.sh/og/home?v=sha-0cd041cbeb92
json_schemas:
- name: HeartbeatRead
  property_count: 17
  slug: fettle-sh-heartbeat-read
- name: IncidentRead
  property_count: 14
  slug: fettle-sh-incident-read
- name: MonitorRead
  property_count: 23
  slug: fettle-sh-monitor-read
- name: SslCheckResponse
  property_count: 17
  slug: fettle-sh-ssl-check-response
- name: StatusPagePublicRead
  property_count: 12
  slug: fettle-sh-status-page-public-read
- name: SubscriptionSummary
  property_count: 13
  slug: fettle-sh-subscription-summary
jsonld:
- class_count: 120
  name: Fettle Sh Context
  property_count: 174
  slug: fettle-sh-context
layout: provider
modified: '2026-10-30'
name: fettle-sh
nav: Providers
network: true
overview: 'fettle-sh publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including fettle.sh Api API, and 1 more. Tagged areas include Monitoring, Uptime, Developers, AI Agents, and API.


  The fettle-sh catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  fettle-sh''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, API reference, and 23 more developer resources.'
plans:
- name: Fettle Sh Plans Pricing
  plan_count: 5
  slug: fettle-sh-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Fettle Sh Rate Limits
  slug: fettle-sh-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: fettle-sh API Rules
  rule_count: 12
  severity_counts:
    error: 6
    hint: 0
    info: 2
    warn: 4
  slug: fettle-sh-rules
scopes:
- name: Fettle Sh Scopes
  scope_count: 2
  slug: fettle-sh-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 61.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 80.6
    catalog_earned_first_party: 12.0
    catalog_gap: 34.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 50.0
    discoverability: 57.1
    operational_transparency: 62.6
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Fettle Sh Authentication
  slug: fettle-sh-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fettle Sh Domain Security
  slug: fettle-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fettle Sh Vulnerability Disclosure
  slug: fettle-sh-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: monitor-management
  slug: fettle-sh-monitor-management
slug: fettle-sh
tags:
- Monitoring
- Uptime
- Developers
- AI Agents
- API
website: https://fettle.sh/
---
