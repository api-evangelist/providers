---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: API for integrating strategy management, signal submission, and white‑label solutions.
  name: Collective2 API
  slug: collective2-api-2
- baseURL: https://api4-general.collective2.com
  baseurl_source: declared
  description: The Autotrade API from Collective2 — 1 operation(s) for autotrade.
  name: Collective2 Autotrade API
  slug: collective2-autotrade-api
- baseURL: https://api4-general.collective2.com
  baseurl_source: declared
  description: The General API from Collective2 — 2 operation(s) for general.
  name: Collective2 General API
  slug: collective2-general-api
- baseURL: https://api4-general.collective2.com
  baseurl_source: declared
  description: The Strategies API from Collective2 — 2 operation(s) for strategies.
  name: Collective2 Strategies API
  slug: collective2-strategies-api
artifact_total: 16
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/rate-limits/collective2-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/collective2-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/rules/collective2-rules.yml
  title: ''
  type: Spectral
  url: rules/collective2-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/json-ld/collective2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/collective2-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/vocabulary/collective2-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/collective2-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/data-model/collective2-data-model.yml
  title: ''
  type: DataModel
  url: data-model/collective2-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/conventions/collective2-conventions.yml
  title: ''
  type: Conventions
  url: conventions/collective2-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/authentication/collective2-authentication.yml
  title: ''
  type: Authentication
  url: authentication/collective2-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/conformance/collective2-conformance.yml
  title: ''
  type: Conformance
  url: conformance/collective2-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/llms/collective2-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/collective2-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/well-known/collective2-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/collective2-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/hosts/collective2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/collective2-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/vendors/collective2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/collective2-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/collective2
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/collective2/refs/heads/main/security/collective2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/collective2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://collective2.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://trade.collective2.com
- group: docs
  title: ''
  type: Documentation
  url: https://trade.collective2.com/c2-api.html
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.collective2.com/apis/general/swagger/general
- group: start
  title: ''
  type: GettingStarted
  url: https://trade.collective2.com/pricing.html
- group: operate
  title: ''
  type: Support
  url: https://support.collective2.com/
- group: company
  title: ''
  type: Blog
  url: https://trade.collective2.com/blog.html
- group: commercial
  title: ''
  type: Pricing
  url: https://trade.collective2.com/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://collective2.com/securesignup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://collective2.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://collective2.com/privacy-policy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://api-docs.collective2.com/mcp
  - status: 401
    url: https://support.collective2.com/mcp
  - status: 200
    url: https://collective2.com
  - status: 403
    url: https://equityzen.com/company/collective2
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Collective2 provides a marketplace for manager‑led trading strategies, allowing investors to follow and automate signals from professional strategy managers directly within their brokerage accounts. The platform offers API4 for developers to integrate strategy management, signal submission, and white‑label solutions, supporting multiple brokers and providing detailed documentation, pricing, and support resources.
image: https://trade.collective2.com/og-cover.png
json_schemas:
- name: DeleteAutotradeAutotradeidResponse
  property_count: 2
  slug: collective2-delete-autotrade-autotradeid-response
- name: GetAutotradeAutotradeidResponse
  property_count: 2
  slug: collective2-get-autotrade-autotradeid-response
- name: PostAutotradeAutotradeidRequest
  property_count: 3
  slug: collective2-post-autotrade-autotradeid-request
- name: PostAutotradeAutotradeidResponse
  property_count: 2
  slug: collective2-post-autotrade-autotradeid-response
- name: PutAutotradeAutotradeidRequest
  property_count: 4
  slug: collective2-put-autotrade-autotradeid-request
- name: PutAutotradeAutotradeidResponse
  property_count: 2
  slug: collective2-put-autotrade-autotradeid-response
jsonld:
- class_count: 6
  name: Collective2 Context
  property_count: 7
  slug: collective2-context
layout: provider
modified: '2026-10-09'
name: Collective2
nav: Providers
network: true
overview: 'Collective2 is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Autotrade API, General API, Strategies API, and 1 more. Tagged areas include Finance, Trading, Marketplace, and Investment.


  The Collective2 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Collective2''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Collective2 Plans Pricing
  plan_count: 0
  slug: collective2-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Collective2 Rate Limits
  slug: collective2-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Collective2 API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: collective2-rules
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 23.6
    developer_ergonomics: 57.1
    discoverability: 60.7
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Collective2 Authentication
  slug: collective2-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Collective2 Domain Security
  slug: collective2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: collective2
tags:
- Finance
- Trading
- Marketplace
- Investment
website: https://collective2.com
---
