---
agent_readiness:
  band: agent-ready
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Unified API aggregating property data from multiple PMS connectors.
  name: Propexo Unified API
  slug: propexo-unified-api
- baseURL: https://api.propexo.com
  baseurl_source: declared
  description: 'Propexo API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Propexo API
  slug: propexo-api
artifact_total: 14
asyncapis:
- description: ''
  name: Propexo Webhooks
  slug: propexo-webhooks
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.propexo.com/how-it-works/getting-started/introduction
- group: operate
  href: https://artifacts.apis.io/propexo/rate-limits/propexo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/propexo-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/propexo/rules/propexo-rules.yml
  title: ''
  type: Spectral
  url: rules/propexo-rules.yml
- group: design
  href: https://artifacts.apis.io/propexo/json-ld/propexo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/propexo-context.jsonld
- group: design
  href: https://artifacts.apis.io/propexo/vocabulary/propexo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/propexo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/propexo/asyncapi/propexo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/propexo-webhooks.yml
- group: design
  href: https://artifacts.apis.io/propexo/data-model/propexo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/propexo-data-model.yml
- group: operate
  href: https://artifacts.apis.io/propexo/changelog/propexo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/propexo-changelog.yml
- group: design
  href: https://artifacts.apis.io/propexo/conventions/propexo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/propexo-conventions.yml
- group: start
  href: https://artifacts.apis.io/propexo/sandbox/propexo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/propexo-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/propexo/authentication/propexo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/propexo-authentication.yml
- group: design
  href: https://artifacts.apis.io/propexo/conformance/propexo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/propexo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/propexo/llms/propexo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/propexo-llms.txt
- group: agent
  href: https://artifacts.apis.io/propexo/well-known/propexo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/propexo-well-known.yml
- group: other
  href: https://artifacts.apis.io/propexo/hosts/propexo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/propexo-hosts.yml
- group: other
  href: https://artifacts.apis.io/propexo/vendors/propexo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/propexo-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.propexo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://propexo.com/legal/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.propexo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://propexo.com/legal/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://propexo.com/company/press/
- group: start
  title: ''
  type: Login
  url: https://app.propexo.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.propexo.com/release-notes/release-notes/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/propexo
- group: auth
  href: https://artifacts.apis.io/propexo/security/propexo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/propexo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://propexo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.propexo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://propexo.com/unified-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://propexo.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://propexo.com/blog/
coverage:
  checked: '2026-10-18'
  detail: Documentation pages are HTML rendered via JavaScript, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://docs.propexo.com/api-reference/overview
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Propexo provides a Property Data Platform for multifamily real‑estate operators, offering a no‑code data movement solution called Connect and a Unified API that aggregates data from over 126 property management system connectors into data warehouses such as Snowflake, BigQuery, or Databricks. The platform enables operators, IT/analytics teams, and proptech developers to access, synchronize, and analyze property data across systems, reducing integration effort and accelerating insights.
image: https://propexo.com/img/og-image.svg
json_schemas:
- name: GetV1LeadsMriResponse
  property_count: 3
  slug: propexo-get-v1-leads-mri-response
- name: GetV1OwnersResponse
  property_count: 2
  slug: propexo-get-v1-owners-response
- name: PostV1LeadsMriRequest
  property_count: 22
  slug: propexo-post-v1-leads-mri-request
- name: PostV1LeadsMriResponse
  property_count: 2
  slug: propexo-post-v1-leads-mri-response
- name: PutV1LeadsMriLeadidRequest
  property_count: 20
  slug: propexo-put-v1-leads-mri-leadid-request
- name: PutV1LeadsMriLeadidResponse
  property_count: 2
  slug: propexo-put-v1-leads-mri-leadid-response
jsonld:
- class_count: 6
  name: Propexo Context
  property_count: 24
  slug: propexo-context
layout: provider
modified: '2026-10-18'
name: Propexo
nav: Providers
network: true
overview: 'Propexo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Data Platform, Integration, and PropTech.


  The Propexo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Propexo''s developer surface includes getting-started guide, changelog, sandbox, authentication, documentation, API reference, pricing, and 23 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 1
  name: Propexo Rate Limits
  slug: propexo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Propexo API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: propexo-rules
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 33.1
    developer_ergonomics: 50.0
    discoverability: 58.9
    operational_transparency: 65.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
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
  name: Propexo Authentication
  slug: propexo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Propexo Domain Security
  slug: propexo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: propexo
tags:
- Company
- Real Estate
- Data Platform
- Integration
- PropTech
website: https://propexo.com/
---
