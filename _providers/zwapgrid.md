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
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://apione.zwapgrid.com
  baseurl_source: declared
  description: 'Zwapgrid API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Zwapgrid API
  slug: zwapgrid-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/zwapgrid/plans/zwapgrid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zwapgrid-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/zwapgrid/rules/zwapgrid-rules.yml
  title: ''
  type: Spectral
  url: rules/zwapgrid-rules.yml
- group: design
  href: https://artifacts.apis.io/zwapgrid/json-ld/zwapgrid-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zwapgrid-context.jsonld
- group: design
  href: https://artifacts.apis.io/zwapgrid/vocabulary/zwapgrid-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zwapgrid-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/zwapgrid/data-model/zwapgrid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zwapgrid-data-model.yml
- group: operate
  href: https://artifacts.apis.io/zwapgrid/changelog/zwapgrid-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zwapgrid-changelog.yml
- group: auth
  href: https://artifacts.apis.io/zwapgrid/authentication/zwapgrid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zwapgrid-authentication.yml
- group: design
  href: https://artifacts.apis.io/zwapgrid/conformance/zwapgrid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zwapgrid-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zwapgrid/llms/zwapgrid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zwapgrid-llms.txt
- group: agent
  href: https://artifacts.apis.io/zwapgrid/well-known/zwapgrid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zwapgrid-well-known.yml
- group: other
  href: https://artifacts.apis.io/zwapgrid/hosts/zwapgrid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zwapgrid-hosts.yml
- group: other
  href: https://artifacts.apis.io/zwapgrid/vendors/zwapgrid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zwapgrid-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.zwapgrid.com/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.zwapgrid.com/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Zwapgrid
- group: auth
  href: https://artifacts.apis.io/zwapgrid/security/zwapgrid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zwapgrid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zwapgrid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zwapgrid.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zwapgrid.com/api.1/api.1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zwapgrid.com/get-started/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zwapgrid.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zwapgrid.com/terms-and-conditions
- group: company
  title: ''
  type: Blog
  url: https://www.zwapgrid.com/blog
- group: operate
  title: ''
  type: Support
  url: https://trust.zwapgrid.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zwapgrid.com/
created: '2026-10-19'
description: Zwapgrid provides a unified accounting API platform connecting multiple ERP and bookkeeping systems. It offers API.1, Accounting API, AI‑powered invoice parsing, and raw data onboarding, enabling seamless integration for fintechs, SaaS, and enterprises. The service includes extensive documentation, sandbox environments, and compliance resources, supporting integrations with Fortnox, Visma, Microsoft Business Central, Xero, QuickBooks, and more.
image: https://cdn.prod.website-files.com/675c8c13f8f72ad23526a4f7/6792458c3bce8483d0ee8463_zwapgrid%20og.jpg
json_schemas:
- name: GetConsentsApiV1ConsentsConsentidResponse
  property_count: 8
  slug: zwapgrid-get-consents-api-v1-consents-consentid-response
- name: GetConsentsApiV1ConsentsResponse
  property_count: 2
  slug: zwapgrid-get-consents-api-v1-consents-response
- name: PatchConsentsApiV1ConsentsConsentidRequest
  property_count: 2
  slug: zwapgrid-patch-consents-api-v1-consents-consentid-request
- name: PostConsentsApiV1ConsentsConsentidOtcResponse
  property_count: 1
  slug: zwapgrid-post-consents-api-v1-consents-consentid-otc-response
- name: PostConsentsApiV1ConsentsRequest
  property_count: 2
  slug: zwapgrid-post-consents-api-v1-consents-request
jsonld:
- class_count: 5
  name: Zwapgrid Context
  property_count: 12
  slug: zwapgrid-context
layout: provider
modified: '2026-10-19'
name: Zwapgrid
nav: Providers
network: true
overview: 'Zwapgrid is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Fintech, Integration, and Software-as-a-Service.


  The Zwapgrid catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zwapgrid''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Zwapgrid Plans Pricing
  plan_count: 3
  slug: zwapgrid-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Zwapgrid API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: zwapgrid-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 33.3
    contract_quality: 26.0
    developer_ergonomics: 47.6
    discoverability: 58.9
    operational_transparency: 36.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zwapgrid Authentication
  slug: zwapgrid-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Zwapgrid Domain Security
  slug: zwapgrid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zwapgrid
tags:
- Accounting
- Fintech
- Integration
- Software-as-a-Service
website: https://zwapgrid.com/
---
