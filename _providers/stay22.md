---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Stay22 provides an affiliate link API, interactive maps, and a reporting API for transaction data.
  name: Stay22 API
  slug: stay22-api-2
- baseURL: https://api.stay22.com
  baseurl_source: declared
  description: 'Stay22 API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Stay22 API
  slug: stay22-api
artifact_total: 14
asyncapis:
- description: ''
  name: Stay22 Webhooks
  slug: stay22-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/stay22/well-known/stay22-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stay22-www-security.txt
- group: operate
  href: https://artifacts.apis.io/stay22/rate-limits/stay22-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stay22-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/stay22/rules/stay22-rules.yml
  title: ''
  type: Spectral
  url: rules/stay22-rules.yml
- group: design
  href: https://artifacts.apis.io/stay22/json-ld/stay22-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stay22-context.jsonld
- group: design
  href: https://artifacts.apis.io/stay22/vocabulary/stay22-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stay22-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/stay22/data-model/stay22-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stay22-data-model.yml
- group: design
  href: https://artifacts.apis.io/stay22/conventions/stay22-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stay22-conventions.yml
- group: start
  href: https://artifacts.apis.io/stay22/sandbox/stay22-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/stay22-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://stay22.com/bugbounty
- group: auth
  href: https://artifacts.apis.io/stay22/authentication/stay22-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stay22-authentication.yml
- group: design
  href: https://artifacts.apis.io/stay22/lifecycle/stay22-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stay22-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/stay22/conformance/stay22-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stay22-conformance.yml
- group: agent
  href: https://artifacts.apis.io/stay22/llms/stay22-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stay22-llms.txt
- group: auth
  href: https://artifacts.apis.io/stay22/well-known/stay22-stay22-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stay22-stay22-security.txt
- group: auth
  href: https://artifacts.apis.io/stay22/well-known/stay22-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stay22-status-security.txt
- group: auth
  href: https://artifacts.apis.io/stay22/well-known/stay22-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stay22-security.txt
- group: auth
  href: https://artifacts.apis.io/stay22/well-known/stay22-lando-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stay22-lando-security.txt
- group: agent
  href: https://artifacts.apis.io/stay22/well-known/stay22-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stay22-well-known.yml
- group: other
  href: https://artifacts.apis.io/stay22/hosts/stay22-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stay22-hosts.yml
- group: other
  href: https://artifacts.apis.io/stay22/vendors/stay22-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stay22-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stay22.com/
- group: start
  title: ''
  type: SignUp
  url: https://hub.stay22.com/signup
- group: company
  title: ''
  type: Newsroom
  url: https://www.stay22.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stay22
- group: auth
  href: https://artifacts.apis.io/stay22/security/stay22-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stay22-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/stay22/security/stay22-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stay22-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stay22.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.stay22.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://dev.stay22.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.stay22.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.stay22.com/docs/api/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.stay22.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://blog.stay22.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stay22.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stay22.com/privacy
coverage:
  checked: '2026-10-28'
  detail: The public documentation at dev.stay22.com/docs provides human‑readable API information, but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 404
    url: https://dev.stay22.com/docs/api/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Stay22 is a travel‑tech platform that helps publishers, event organizers, and transportation services monetize travel intent by providing affiliate links, interactive maps, and a direct travel API. It offers products such as Allez affiliate links, interactive maps, Nova and Spark recommendation widgets, and a reporting API for transaction data. The company originated from a need to simplify hotel discovery for e‑sports events and now serves a global audience across media and travel industries.
image: https://lando.stay22.com/hubfs/glyph%20blue.png
json_schemas:
- name: GetV1ReportingTransactionsResponse
  property_count: 5
  slug: stay22-get-v1-reporting-transactions-response
- name: GetV2AccommodationsResponse
  property_count: 9
  slug: stay22-get-v2-accommodations-response
- name: GetV3AccommodationsResponse
  property_count: 5
  slug: stay22-get-v3-accommodations-response
jsonld:
- class_count: 3
  name: Stay22 Context
  property_count: 19
  slug: stay22-context
layout: provider
modified: '2026-10-28'
name: Stay22
nav: Providers
network: true
overview: 'Stay22 is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include TravelTech, AffiliateMarketing, SaaS, Events, and Maps.


  The Stay22 catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Stay22''s developer surface includes sandbox, authentication, signup flow, documentation, API reference, getting-started guide, support, and 28 more developer resources.'
plans:
- name: Stay22 Plans Pricing
  plan_count: 0
  slug: stay22-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Stay22 Rate Limits
  slug: stay22-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Stay22 API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: stay22-rules
scopes:
- name: Stay22 Scopes
  scope_count: 0
  slug: stay22-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 31.9
    developer_ergonomics: 64.3
    discoverability: 67.9
    operational_transparency: 63.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
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
  name: Stay22 Authentication
  slug: stay22-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stay22 Domain Security
  slug: stay22-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stay22 Vulnerability Disclosure
  slug: stay22-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: stay22
tags:
- TravelTech
- AffiliateMarketing
- SaaS
- Events
- Maps
website: https://stay22.com/
---
