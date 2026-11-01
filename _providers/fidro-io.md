---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Fraud detection API offering email, IP, VPN, and domain risk checks.
  name: Fidro API
  slug: fidro-api
- description: 'fidro-io API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: fidro-io API
  slug: fidro-io-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/fidro-io/rate-limits/fidro-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fidro-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fidro-io/plans/fidro-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fidro-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fidro-io/rules/fidro-io-rules.yml
  title: ''
  type: Spectral
  url: rules/fidro-io-rules.yml
- group: design
  href: https://artifacts.apis.io/fidro-io/json-ld/fidro-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fidro-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/fidro-io/vocabulary/fidro-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fidro-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fidro-io/data-model/fidro-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fidro-io-data-model.yml
- group: start
  href: https://artifacts.apis.io/fidro-io/sandbox/fidro-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/fidro-io-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/fidro-io/authentication/fidro-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fidro-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/fidro-io/errors/fidro-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fidro-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fidro-io/conformance/fidro-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fidro-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fidro-io/llms/fidro-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fidro-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/fidro-io/well-known/fidro-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fidro-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/fidro-io/hosts/fidro-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fidro-io-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://fidro.io/login
- group: auth
  href: https://artifacts.apis.io/fidro-io/security/fidro-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fidro-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fidro.io/
- group: docs
  title: ''
  type: Documentation
  url: https://fidro.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://fidro.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://fidro.io/docs#getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://fidro.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://fidro.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fidro.io/
coverage:
  checked: '2026-10-30'
  detail: Documentation is publicly available but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://fidro.io/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Fidro provides a fraud detection API that evaluates email addresses, IPs, VPNs, proxies, and domain risk in a single call. It returns a risk score with recommendations to allow, challenge, or block, and includes features like signup and login monitoring, chargeback prevention, and Stripe transaction scoring. The service offers a free tier with sub‑200 ms response times and paid plans for higher volume.
image: https://fidro.io/og/title.png?eyebrow=Fidro&subtitle=One%20API%20call%20scores%20the%20email%2C%20IP%20and%20network%2C%20remembers%20repeat%20signups%20and%20odd%20logins%2C%20then%20tells%20you%20to%20allow%2C%20challenge%20or%20block.%20Free%20plan%2C%20under%20200ms.&title=Fraud%20Detection%20API%20for%20Fake%20Signups%20and%20Stolen%20Cards&signature=9a5926bdc24452cd01d9cf3c0e790d18dce7a8dfee44e31512a6f33842c5d5ec
json_schemas:
- name: GetApiBlocklistResponse
  property_count: 7
  slug: fidro-io-get-api-blocklist-response
- name: GetApiStatusResponse
  property_count: 3
  slug: fidro-io-get-api-status-response
- name: PostApiBlocklistRequest
  property_count: 5
  slug: fidro-io-post-api-blocklist-request
- name: PostApiBlocklistResponse
  property_count: 7
  slug: fidro-io-post-api-blocklist-response
- name: PostApiDomainLookupRequest
  property_count: 1
  slug: fidro-io-post-api-domain-lookup-request
- name: PostApiValidateRequest
  property_count: 1
  slug: fidro-io-post-api-validate-request
jsonld:
- class_count: 6
  name: Fidro Io Context
  property_count: 12
  slug: fidro-io-context
layout: provider
modified: '2026-10-30'
name: fidro-io
nav: Providers
network: true
overview: 'fidro-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FraudDetection, API, RiskAnalysis, and Payments.


  The fidro-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  fidro-io''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Fidro Io Plans Pricing
  plan_count: 4
  slug: fidro-io-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Fidro Io Rate Limits
  slug: fidro-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: fidro-io API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: fidro-io-rules
scopes:
- name: Fidro Io Scopes
  scope_count: 0
  slug: fidro-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 94.3
    catalog_earned_first_party: 0.0
    catalog_gap: 20.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 62.6
    contract_governance: 79.1
    contract_quality: 53.4
    developer_ergonomics: 50.0
    discoverability: 57.1
    operational_transparency: 28.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Fidro Io Authentication
  slug: fidro-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fidro Io Domain Security
  slug: fidro-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fidro-io
tags:
- Company
- FraudDetection
- API
- RiskAnalysis
- Payments
website: https://fidro.io/
---
