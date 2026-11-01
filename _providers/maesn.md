---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 60
  human_in_the_loop: 0
  name: Maesn Agentic Access
  operation_count: 145
  slug: maesn-agentic-access
  summary_line: 145 operations · 60 acting
api_count: 1
apis:
- baseURL: https://api.maesn.dev
  baseurl_source: declared
  description: The accounting API from Maesn — 91 operation(s) for accounting.
  name: Maesn Accounting API
  slug: maesn-accounting-api
- baseURL: https://api.maesn.dev
  baseurl_source: declared
  description: The auth API from Maesn — 4 operation(s) for auth.
  name: Maesn Auth API
  slug: maesn-auth-api
- baseURL: https://api.maesn.dev
  baseurl_source: declared
  description: The tenants API from Maesn — 6 operation(s) for tenants.
  name: Maesn Tenants API
  slug: maesn-tenants-api
- baseURL: https://api.maesn.dev
  baseurl_source: declared
  description: The user API from Maesn — 1 operation(s) for user.
  name: Maesn User API
  slug: maesn-user-api
- baseURL: https://api.maesn.dev
  baseurl_source: declared
  description: The webhook API from Maesn — 2 operation(s) for webhook.
  name: Maesn Webhook API
  slug: maesn-webhook-api
artifact_total: 20
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.maesn.com/guides/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.maesn.com/
- group: agent
  href: https://artifacts.apis.io/maesn/agentic-access/maesn-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/maesn-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/maesn/rate-limits/maesn-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/maesn-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/maesn/rules/maesn-rules.yml
  title: ''
  type: Spectral
  url: rules/maesn-rules.yml
- group: design
  href: https://artifacts.apis.io/maesn/json-ld/maesn-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/maesn-context.jsonld
- group: design
  href: https://artifacts.apis.io/maesn/vocabulary/maesn-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/maesn-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/maesn/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/maesn/data-model/maesn-data-model.yml
  title: ''
  type: DataModel
  url: data-model/maesn-data-model.yml
- group: operate
  href: https://artifacts.apis.io/maesn/changelog/maesn-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/maesn-changelog.yml
- group: design
  href: https://artifacts.apis.io/maesn/conventions/maesn-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/maesn-conventions.yml
- group: design
  href: https://artifacts.apis.io/maesn/conventions/maesn-conventions.yml
  title: ''
  type: Conventions
  url: conventions/maesn-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.maesn.com/security/
- group: auth
  href: https://artifacts.apis.io/maesn/authentication/maesn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/maesn-authentication.yml
- group: design
  href: https://artifacts.apis.io/maesn/conformance/maesn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/maesn-conformance.yml
- group: agent
  href: https://artifacts.apis.io/maesn/llms/maesn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/maesn-llms.txt
- group: other
  href: https://artifacts.apis.io/maesn/a2a/maesn-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/maesn-a2a.yml
- group: agent
  href: https://artifacts.apis.io/maesn/well-known/maesn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/maesn-well-known.yml
- group: other
  href: https://artifacts.apis.io/maesn/hosts/maesn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/maesn-hosts.yml
- group: other
  href: https://artifacts.apis.io/maesn/vendors/maesn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/maesn-vendors.yml
- group: build
  href: https://artifacts.apis.io/maesn/packages/maesn-packages.yml
  title: ''
  type: SDKs
  url: packages/maesn-packages.yml
- group: build
  href: https://artifacts.apis.io/maesn/packages/maesn-packages.yml
  title: ''
  type: Packages
  url: packages/maesn-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.maesn.com/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://www.maesn.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.maesn.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maesndev
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.maesn.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.maesn.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/maesn/security/maesn-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/maesn-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/maesn/security/maesn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maesn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.maesn.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.maesn.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.maesn.com/blog/
created: '2026-10-20'
description: Maesn provides a unified REST API that connects to major ERP and accounting systems such as DATEV, Sage, and Exact Online. It offers normalized data, authentication, and webhook support, enabling developers to integrate multiple financial platforms through a single endpoint.
image: https://www.maesn.com/images/brand/maesn-logo.svg
json_schemas:
- name: BillResponseDto
  property_count: 32
  slug: maesn-bill-response-dto
- name: CreateBillRequestDto
  property_count: 29
  slug: maesn-create-bill-request-dto
- name: CreateVendorCreditRequestDto
  property_count: 29
  slug: maesn-create-vendor-credit-request-dto
- name: InvoiceResponseDto
  property_count: 30
  slug: maesn-invoice-response-dto
- name: UpdateBillRequestDto
  property_count: 29
  slug: maesn-update-bill-request-dto
- name: VendorCreditResponseDto
  property_count: 32
  slug: maesn-vendor-credit-response-dto
jsonld:
- class_count: 120
  name: Maesn Context
  property_count: 265
  slug: maesn-context
layout: provider
modified: '2026-10-20'
name: Maesn
nav: Providers
network: true
overview: 'Maesn publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounting API, Auth API, Tenants API, and 2 more. Tagged areas include ERP, Accounting, Integration, and Software-as-a-Service.


  The Maesn catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Maesn''s developer surface includes getting-started guide, documentation, changelog, authentication, API reference, pricing, engineering blog, and 26 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 9
  name: Maesn Rate Limits
  slug: maesn-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Maesn API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 3
  slug: maesn-rules
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 52.5
    developer_ergonomics: 51.8
    discoverability: 57.1
    operational_transparency: 63.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Maesn Authentication
  slug: maesn-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Maesn Domain Security
  slug: maesn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Maesn Trust Center
  slug: maesn-trust-center
  summary_line: ISO 27001, GDPR
skill_count: 2
skills:
- name: maesn-setup-tenant
  slug: maesn-setup-tenant
- name: maesn-webhook-management
  slug: maesn-webhook-management
slug: maesn
tags:
- ERP
- Accounting
- Integration
- Software-as-a-Service
website: https://www.maesn.com/
---
