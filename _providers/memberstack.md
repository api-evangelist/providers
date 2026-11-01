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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Server-side Memberstack Admin REST API for managing members, verifying tokens, and other administrative tasks.
  name: Admin REST API
  slug: admin-rest-api
- baseURL: https://admin.memberstack.com
  baseurl_source: declared
  description: 'Memberstack API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Memberstack API
  slug: memberstack-api
artifact_total: 19
common:
- group: operate
  href: https://artifacts.apis.io/memberstack/rate-limits/memberstack-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/memberstack-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/memberstack/plans/memberstack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/memberstack-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/memberstack/rules/memberstack-rules.yml
  title: ''
  type: Spectral
  url: rules/memberstack-rules.yml
- group: design
  href: https://artifacts.apis.io/memberstack/json-ld/memberstack-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/memberstack-context.jsonld
- group: design
  href: https://artifacts.apis.io/memberstack/vocabulary/memberstack-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/memberstack-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/memberstack/data-model/memberstack-data-model.yml
  title: ''
  type: DataModel
  url: data-model/memberstack-data-model.yml
- group: operate
  href: https://artifacts.apis.io/memberstack/changelog/memberstack-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/memberstack-changelog.yml
- group: auth
  href: https://artifacts.apis.io/memberstack/authentication/memberstack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/memberstack-authentication.yml
- group: design
  href: https://artifacts.apis.io/memberstack/conformance/memberstack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/memberstack-conformance.yml
- group: agent
  href: https://artifacts.apis.io/memberstack/llms/memberstack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/memberstack-llms.txt
- group: other
  href: https://artifacts.apis.io/memberstack/hosts/memberstack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/memberstack-hosts.yml
- group: other
  href: https://artifacts.apis.io/memberstack/vendors/memberstack-vendors.yml
  title: ''
  type: Vendors
  url: vendors/memberstack-vendors.yml
- group: build
  href: https://artifacts.apis.io/memberstack/packages/memberstack-packages.yml
  title: ''
  type: SDKs
  url: packages/memberstack-packages.yml
- group: build
  href: https://artifacts.apis.io/memberstack/packages/memberstack-packages.yml
  title: ''
  type: Packages
  url: packages/memberstack-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.memberstack.com/features/webhooks
- group: operate
  title: ''
  type: Support
  url: https://www.memberstack.com/features/help-center
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.memberstack.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.memberstack.com/dom-package/quick-start
- group: auth
  href: https://artifacts.apis.io/memberstack/security/memberstack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/memberstack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://memberstack.com/
- group: company
  title: ''
  type: Blog
  url: https://www.memberstack.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.memberstack.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.memberstack.com/signup
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.memberstack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.memberstack.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Memberstack
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found; attempts to fetch common spec URLs returned HTML pages.
  evidence:
  - status: 200
    url: https://app.memberstack.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Memberstack provides a membership and authentication platform for Webflow, WordPress, and custom sites, enabling user sign‑ups, social logins, gated content, and Stripe payment integration, with no hidden fees and scalable pricing as businesses grow.
image: https://www.memberstack.com/brand/memberstack-logo-full-light.png
json_schemas:
- name: GetMembersExample40TestComResponse
  property_count: 1
  slug: memberstack-get-members-example40-test-com-response
- name: GetMembersMemAbc123Response
  property_count: 1
  slug: memberstack-get-members-mem-abc123-response
- name: GetV1DataTablesTablekeyResponse
  property_count: 7
  slug: memberstack-get-v1-data-tables-tablekey-response
- name: GetV2DataTablesProductsResponse
  property_count: 1
  slug: memberstack-get-v2-data-tables-products-response
- name: GetV2DataTablesResponse
  property_count: 10
  slug: memberstack-get-v2-data-tables-response
- name: PatchMembersIdRequest
  property_count: 7
  slug: memberstack-patch-members-id-request
- name: PatchMembersMemAbc123Response
  property_count: 1
  slug: memberstack-patch-members-mem-abc123-response
- name: PostMembersRequest
  property_count: 7
  slug: memberstack-post-members-request
- name: PostMembersResponse
  property_count: 13
  slug: memberstack-post-members-response
- name: PostV1DataRecordsQueryRequest
  property_count: 7
  slug: memberstack-post-v1-data-records-query-request
jsonld:
- class_count: 26
  name: Memberstack Context
  property_count: 44
  slug: memberstack-context
layout: provider
modified: '2026-10-28'
name: Memberstack
nav: Providers
network: true
overview: 'Memberstack is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Membership, Webflow, SaaS, Authentication, and Payments.


  The Memberstack catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Memberstack''s developer surface includes changelog, authentication, support, getting-started guide, engineering blog, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Memberstack Plans Pricing
  plan_count: 2
  slug: memberstack-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Memberstack Rate Limits
  slug: memberstack-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Memberstack API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: memberstack-rules
scopes:
- name: Memberstack Scopes
  scope_count: 0
  slug: memberstack-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 25.8
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 50.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Memberstack Authentication
  slug: memberstack-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Memberstack Domain Security
  slug: memberstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: memberstack
tags:
- Membership
- Webflow
- SaaS
- Authentication
- Payments
website: https://memberstack.com/
---
