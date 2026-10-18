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
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-10-17'
api_count: 3
apis:
- baseURL: https://api.cnaught.com
  baseurl_source: declared
  description: The CNaught API API from CNaught — 2 operation(s) for cnaught api.
  name: CNaught CNaught API
  slug: cnaught-cnaught-api-api
- baseURL: https://api.cnaught.com
  baseurl_source: declared
  description: The Orders API from CNaught — 2 operation(s) for orders.
  name: CNaught Orders API
  slug: cnaught-orders-api
- baseURL: https://api.cnaught.com
  baseurl_source: declared
  description: The Subaccounts API from CNaught — 1 operation(s) for subaccounts.
  name: CNaught Subaccounts API
  slug: cnaught-subaccounts-api
artifact_total: 14
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/plans/cnaught-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cnaught-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/rules/cnaught-rules.yml
  title: ''
  type: Spectral
  url: rules/cnaught-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/json-ld/cnaught-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cnaught-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/vocabulary/cnaught-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cnaught-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/data-model/cnaught-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cnaught-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/changelog/cnaught-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cnaught-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/conventions/cnaught-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cnaught-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/conventions/cnaught-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cnaught-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/authentication/cnaught-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cnaught-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/conformance/cnaught-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cnaught-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/llms/cnaught-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cnaught-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/hosts/cnaught-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cnaught-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/vendors/cnaught-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cnaught-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/packages/cnaught-packages.yml
  title: ''
  type: SDKs
  url: packages/cnaught-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/packages/cnaught-packages.yml
  title: ''
  type: Packages
  url: packages/cnaught-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cnaught.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cnaught.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cnaught.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cnaught-inc
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cnaught.com/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cnaught/refs/heads/main/security/cnaught-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cnaught-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cnaught.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cnaught.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cnaught.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cnaught.com/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.cnaught.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cnaught.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.cnaught.com/contact-sales
created: '2026-10-09'
description: CNaught provides a science‑backed platform that helps businesses purchase, manage and retire high‑integrity carbon credits. Their API enables integration of carbon‑credit portfolios, access to Energy Attribute Certificates, and tools for emissions calculations, aiming to simplify climate impact for companies of any size.
image: https://www.cnaught.com/api/og?title=Carbon credits you can trust
json_schemas:
- name: DeleteV1SubaccountsIdResponse
  property_count: 2
  slug: cnaught-delete-v1-subaccounts-id-response
- name: GetV1V1IdIdResponse
  property_count: 2
  slug: cnaught-get-v1-v1-id-id-response
- name: GetV1V1IdResponse
  property_count: 2
  slug: cnaught-get-v1-v1-id-response
- name: PostV1OrdersIdCancelResponse
  property_count: 6
  slug: cnaught-post-v1-orders-id-cancel-response
- name: PostV1OrdersIdResponse
  property_count: 2
  slug: cnaught-post-v1-orders-id-response
- name: PostV1V1IdRequest
  property_count: 4
  slug: cnaught-post-v1-v1-id-request
jsonld:
- class_count: 7
  name: Cnaught Context
  property_count: 9
  slug: cnaught-context
layout: provider
modified: '2026-10-09'
name: CNaught
nav: Providers
network: true
overview: 'CNaught is listed with 3 APIs on the [APIs.io](https://apis.io/) network: CNaught API, Orders API, and Subaccounts API. Tagged areas include Company, Climate, CarbonCredits, and Sustainability.


  The CNaught catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CNaught''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Cnaught Plans Pricing
  plan_count: 3
  slug: cnaught-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: CNaught API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: cnaught-rules
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 23.8
    developer_ergonomics: 54.8
    discoverability: 69.6
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cnaught Authentication
  slug: cnaught-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cnaught Domain Security
  slug: cnaught-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cnaught
tags:
- Company
- Climate
- CarbonCredits
- Sustainability
website: https://www.cnaught.com/
---
