---
agent_readiness:
  band: agent-ready
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: The FirmLedger MCP API provides programmatic access to ledger data, including company profiles, verification scores, and data export. Documentation is available at the API reference page.
  name: FirmLedger MCP API
  slug: firmledger-mcp-api
- baseURL: https://mcp.firmledger.co.ke
  baseurl_source: declared
  description: 'FirmLedger API as documented publicly: 36 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: FirmLedger API
  slug: firmledger-co-ke-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/firmledger-co-ke/plans/firmledger-co-ke-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/firmledger-co-ke-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/firmledger-co-ke/rules/firmledger-co-ke-rules.yml
  title: ''
  type: Spectral
  url: rules/firmledger-co-ke-rules.yml
- group: design
  href: https://artifacts.apis.io/firmledger-co-ke/json-ld/firmledger-co-ke-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/firmledger-co-ke-context.jsonld
- group: design
  href: https://artifacts.apis.io/firmledger-co-ke/vocabulary/firmledger-co-ke-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/firmledger-co-ke-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/firmledger-co-ke/data-model/firmledger-co-ke-data-model.yml
  title: ''
  type: DataModel
  url: data-model/firmledger-co-ke-data-model.yml
- group: auth
  href: https://artifacts.apis.io/firmledger-co-ke/authentication/firmledger-co-ke-authentication.yml
  title: ''
  type: Authentication
  url: authentication/firmledger-co-ke-authentication.yml
- group: design
  href: https://artifacts.apis.io/firmledger-co-ke/conformance/firmledger-co-ke-conformance.yml
  title: ''
  type: Conformance
  url: conformance/firmledger-co-ke-conformance.yml
- group: agent
  href: https://artifacts.apis.io/firmledger-co-ke/well-known/firmledger-co-ke-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/firmledger-co-ke-well-known.yml
- group: other
  href: https://artifacts.apis.io/firmledger-co-ke/hosts/firmledger-co-ke-hosts.yml
  title: ''
  type: Hosts
  url: hosts/firmledger-co-ke-hosts.yml
- group: other
  href: https://artifacts.apis.io/firmledger-co-ke/vendors/firmledger-co-ke-vendors.yml
  title: ''
  type: Vendors
  url: vendors/firmledger-co-ke-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://firmledger.co.ke/status
- group: start
  title: ''
  type: Sandbox
  url: https://firmledger.co.ke/login?next=/dashboard/api/playground
- group: auth
  href: https://artifacts.apis.io/firmledger-co-ke/security/firmledger-co-ke-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/firmledger-co-ke-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://firmledger.co.ke
- group: start
  title: ''
  type: DeveloperPortal
  url: https://firmledger.co.ke/docs
- group: docs
  title: ''
  type: Documentation
  url: https://firmledger.co.ke/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://firmledger.co.ke/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://firmledger.co.ke/api/docs
- group: operate
  title: ''
  type: Support
  url: https://firmledger.co.ke/help
- group: company
  title: ''
  type: Blog
  url: https://firmledger.co.ke/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://firmledger.co.ke/pricing
- group: start
  title: ''
  type: SignUp
  url: https://firmledger.co.ke/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://firmledger.co.ke/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://firmledger.co.ke/privacy
created: '2026-10-28'
description: FirmLedger provides a public web application that indexes and verifies business records for companies, startups, agencies, and other entities. It aggregates open-source data into canonical profiles with provenance, confidence scores, and ownership verification. Users can browse listings without sign‑in, while a Pro API offers programmatic access to the ledger, complete with keys, documentation, and a playground for developers.
image: https://firmledger.co.ke/assets/og-card.png
json_schemas:
- name: PostApiV1ListingsRequest
  property_count: 17
  slug: firmledger-co-ke-post-api-v1-listings-request
- name: PostApiV1Webhooks7RotateSecretResponse
  property_count: 2
  slug: firmledger-co-ke-post-api-v1-webhooks7-rotate-secret-response
- name: PostApiV1Webhooks7TestResponse
  property_count: 2
  slug: firmledger-co-ke-post-api-v1-webhooks7-test-response
- name: PostMcpRequest
  property_count: 4
  slug: firmledger-co-ke-post-mcp-request
- name: PostMcpResponse
  property_count: 4
  slug: firmledger-co-ke-post-mcp-response
- name: PostOauthRegisterRequest
  property_count: 3
  slug: firmledger-co-ke-post-oauth-register-request
jsonld:
- class_count: 13
  name: Firmledger Co Ke Context
  property_count: 40
  slug: firmledger-co-ke-context
layout: provider
modified: '2026-10-28'
name: FirmLedger
nav: Providers
network: true
overview: 'FirmLedger is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including MCP API, and 1 more. Tagged areas include Company, Directory, Business-Intelligence, Kenya, and API.


  The FirmLedger catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FirmLedger''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 17 more developer resources.'
plans:
- name: Firmledger Co Ke Plans Pricing
  plan_count: 3
  slug: firmledger-co-ke-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: FirmLedger API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: firmledger-co-ke-rules
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 64.3
    discoverability: 57.1
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - kenya
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 18
      marker_coverage: 100.0
      total: 18
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Firmledger Co Ke Authentication
  slug: firmledger-co-ke-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Firmledger Co Ke Domain Security
  slug: firmledger-co-ke-domain-security
  summary_line: TLSv1.3 · DMARC
slug: firmledger-co-ke
tags:
- Company
- Directory
- Business-Intelligence
- Kenya
- API
website: https://firmledger.co.ke
---
