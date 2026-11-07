---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DoDomain API for managing domains and webhooks
  name: DoDomain API
  slug: dodomain-api
- baseURL: https://app.dodomain.io
  baseurl_source: declared
  description: The `/api/v1` surface integrators call to create domain-connect sessions, drive detection and DNS verification, and manage the resulting connections.
  name: DoDomain API API
  slug: dodomain-api-api
artifact_total: 16
asyncapis:
- description: ''
  name: Dodomain Io Webhooks
  slug: dodomain-io-webhooks
common:
- group: design
  href: https://artifacts.apis.io/dodomain-io/rules/dodomain-io-rules.yml
  title: ''
  type: Spectral
  url: rules/dodomain-io-rules.yml
- group: design
  href: https://artifacts.apis.io/dodomain-io/json-ld/dodomain-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dodomain-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/dodomain-io/vocabulary/dodomain-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dodomain-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dodomain-io/conformance/dodomain-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dodomain-io-conformance.yml
- group: operate
  href: https://artifacts.apis.io/dodomain-io/rate-limits/dodomain-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dodomain-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dodomain-io/plans/dodomain-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dodomain-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dodomain-io/asyncapi/dodomain-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dodomain-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dodomain-io/data-model/dodomain-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dodomain-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dodomain-io/changelog/dodomain-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dodomain-io-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://dodomain.io/terms
- group: auth
  href: https://artifacts.apis.io/dodomain-io/authentication/dodomain-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dodomain-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/dodomain-io/errors/dodomain-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dodomain-io-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/dodomain-io/llms/dodomain-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dodomain-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/dodomain-io/well-known/dodomain-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dodomain-io-security.txt
- group: auth
  href: https://artifacts.apis.io/dodomain-io/well-known/dodomain-io-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dodomain-io-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/dodomain-io/well-known/dodomain-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dodomain-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/dodomain-io/hosts/dodomain-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dodomain-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dodomain-io/vendors/dodomain-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dodomain-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.dodomain.io/signin
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.dodomain.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://dodomain.io/changelog
- group: auth
  href: https://artifacts.apis.io/dodomain-io/security/dodomain-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dodomain-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dodomain-io/security/dodomain-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dodomain-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dodomain.io/
- group: docs
  title: ''
  type: Documentation
  url: https://dodomain.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dodomain.io/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://dodomain.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dodomain.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dodomain.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dodomain.io
- group: operate
  title: ''
  type: Support
  url: https://app.dodomain.io/support
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://dodomain.io/openapi.json
  - status: null
    url: https://dev.dodomain.io/openapi.json
  - status: 401
    url: https://app.dodomain.io/api/mcp
  - status: 401
    url: https://dev-app.dodomain.io/api/mcp
  - status: 200
    url: https://dodomain.io/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: DoDomain provides a platform for SaaS companies to offer custom domains to their customers, handling DNS provider detection, one‑click Cloudflare integration, guided setup for other providers, and webhook verification. The service includes a REST API for managing sessions, domains, connections, and webhooks, with SDKs for Node, Python, and React, and supports secure secret‑key, public‑key, OAuth, and session‑token authentication.
image: https://dodomain.io/opengraph-image?7251290ad44223a0
json_schemas:
- name: CheckDomainResponse
  property_count: 11
  slug: dodomain-io-check-domain-response
- name: ConnectionSummary
  property_count: 12
  slug: dodomain-io-connection-summary
- name: IntegratorSession
  property_count: 13
  slug: dodomain-io-integrator-session
- name: ListAppsResponse
  property_count: 1
  slug: dodomain-io-list-apps-response
- name: ListConnectionsResponse
  property_count: 2
  slug: dodomain-io-list-connections-response
- name: PublicSession
  property_count: 9
  slug: dodomain-io-public-session
jsonld:
- class_count: 24
  name: Dodomain Io Context
  property_count: 64
  slug: dodomain-io-context
layout: provider
modified: '2026-11-05'
name: DoDomain
nav: Providers
network: true
overview: 'DoDomain publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Software-as-a-Service, DNS, CustomDomain, and Integration.


  The DoDomain catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DoDomain''s developer surface includes changelog, authentication, documentation, API reference, pricing, support, and 25 more developer resources.'
plans:
- name: Dodomain Io Plans Pricing
  plan_count: 3
  slug: dodomain-io-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Dodomain Io Rate Limits
  slug: dodomain-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: DoDomain API Rules
  rule_count: 63
  severity_counts:
    error: 57
    hint: 0
    info: 2
    warn: 4
  slug: dodomain-io-rules
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 81.6
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dodomain Io Authentication
  slug: dodomain-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dodomain Io Domain Security
  slug: dodomain-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dodomain Io Vulnerability Disclosure
  slug: dodomain-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dodomain-io
tags:
- Software-as-a-Service
- DNS
- CustomDomain
- Integration
website: https://dodomain.io/
---
