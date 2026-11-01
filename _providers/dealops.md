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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 3
apis:
- description: Dealops API provides programmatic access to catalog, quotes, deals, and approvals. Base URL is https://api.dealops.com/external/v1 as documented.
  name: Dealops API
  slug: dealops-api
- baseURL: https://api.dealops.com
  baseurl_source: declared
  description: 'Dealops api API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Dealops api API
  slug: api-api
- baseURL: https://api.dealops.com
  baseurl_source: declared
  description: 'Dealops core API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Dealops core API
  slug: core-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/dealops/rate-limits/dealops-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dealops-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/dealops/rules/dealops-rules.yml
  title: ''
  type: Spectral
  url: rules/dealops-rules.yml
- group: design
  href: https://artifacts.apis.io/dealops/json-ld/dealops-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dealops-context.jsonld
- group: design
  href: https://artifacts.apis.io/dealops/vocabulary/dealops-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dealops-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dealops/data-model/dealops-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dealops-data-model.yml
- group: design
  href: https://artifacts.apis.io/dealops/conventions/dealops-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dealops-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dealops/authentication/dealops-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dealops-authentication.yml
- group: design
  href: https://artifacts.apis.io/dealops/conformance/dealops-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dealops-conformance.yml
- group: auth
  href: https://artifacts.apis.io/dealops/well-known/dealops-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dealops-app-security.txt
- group: agent
  href: https://artifacts.apis.io/dealops/well-known/dealops-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dealops-well-known.yml
- group: other
  href: https://artifacts.apis.io/dealops/hosts/dealops-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dealops-hosts.yml
- group: other
  href: https://artifacts.apis.io/dealops/vendors/dealops-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dealops-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dealops.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dealops.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dealops.com/docs/category/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dealops.com/
- group: auth
  href: https://artifacts.apis.io/dealops/security/dealops-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dealops-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dealops.com/
coverage:
  checked: '2026-10-22'
  detail: Documentation provides base URL and authentication details but no OpenAPI or other machine‑readable contract is publicly available.
  evidence:
  - status: 200
    url: https://docs.dealops.com/docs/api/api-overview
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Dealops provides an AI‑native CPQ (Configure‑Price‑Quote) and revenue optimization platform that automates complex pricing strategies. It enables businesses to set up a CPQ instance in hours, supports tiered, usage‑based, and subscription pricing, and integrates with CRM and ERP systems. Dealops targets AI product companies and enterprises seeking to turn quoting into a revenue advantage, offering features like dynamic pricing, revenue forecasting, and a developer portal for custom integrations.
image: https://cdn.prod.website-files.com/6932e33700f5127296776d2b/6a55d49146c94fcfbe15e472_0cf2eb436ddae1922beaa5d3753362ed_OpenGraph.jpg
json_schemas:
- name: GetApprovalGroupsResponse
  property_count: 1
  slug: dealops-get-approval-groups-response
- name: GetApprovalRuleGroupsResponse
  property_count: 1
  slug: dealops-get-approval-rule-groups-response
- name: GetApprovalRulesResponse
  property_count: 1
  slug: dealops-get-approval-rules-response
- name: GetApprovalsResponse
  property_count: 1
  slug: dealops-get-approvals-response
- name: GetPricingQuotesResponse
  property_count: 1
  slug: dealops-get-pricing-quotes-response
- name: GetProductsResponse
  property_count: 1
  slug: dealops-get-products-response
- name: PostExternalV1WebhookConfigsRequest
  property_count: 3
  slug: dealops-post-external-v1-webhook-configs-request
jsonld:
- class_count: 10
  name: Dealops Context
  property_count: 4
  slug: dealops-context
layout: provider
modified: '2026-10-22'
name: Dealops
nav: Providers
network: true
overview: 'Dealops is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including api API, core API, and 1 more. Tagged areas include Company, CPQ, Pricing, Artificial Intelligence, and Software-as-a-Service.


  The Dealops catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dealops'' developer surface includes authentication, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 1
  name: Dealops Rate Limits
  slug: dealops-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Dealops API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: dealops-rules
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 23.7
    developer_ergonomics: 33.3
    discoverability: 71.4
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 15
      marker_coverage: 100.0
      total: 15
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dealops Authentication
  slug: dealops-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dealops Domain Security
  slug: dealops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dealops
tags:
- Company
- CPQ
- Pricing
- Artificial Intelligence
- Software-as-a-Service
- Revenue-Optimization
website: https://dealops.com/
---
