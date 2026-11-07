---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 5
apis:
- description: Auto‑generated API for a Gadget app, allowing GraphQL, JavaScript, or React calls to backend actions.
  name: Example App API
  slug: example-app-api
- description: 'Gadget actions API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Gadget actions API
  slug: actions-api
- description: 'Gadget core API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Gadget core API
  slug: core-api
- description: 'Gadget http routes API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Gadget http routes API
  slug: http-routes-api
- description: 'Gadget plugins API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Gadget plugins API
  slug: plugins-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/gadget/rules/gadget-rules.yml
  title: ''
  type: Spectral
  url: rules/gadget-rules.yml
- group: design
  href: https://artifacts.apis.io/gadget/json-ld/gadget-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gadget-context.jsonld
- group: design
  href: https://artifacts.apis.io/gadget/vocabulary/gadget-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gadget-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gadget/data-model/gadget-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gadget-data-model.yml
- group: design
  href: https://artifacts.apis.io/gadget/conformance/gadget-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gadget-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gadget/llms/gadget-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gadget-llms.txt
- group: other
  href: https://artifacts.apis.io/gadget/hosts/gadget-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gadget-hosts.yml
- group: other
  href: https://artifacts.apis.io/gadget/vendors/gadget-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gadget-vendors.yml
- group: build
  href: https://artifacts.apis.io/gadget/packages/gadget-packages.yml
  title: ''
  type: SDKs
  url: packages/gadget-packages.yml
- group: build
  href: https://artifacts.apis.io/gadget/packages/gadget-packages.yml
  title: ''
  type: Packages
  url: packages/gadget-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://gadget.dev/press
- group: start
  title: ''
  type: Login
  url: https://app.gadget.dev/auth/login
- group: other
  title: ''
  type: Leadership
  url: https://app.gadget.dev/auth/team/create-app?type=ShopifyApp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gadget-inc
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gadget.dev/guides/plugins/shopify/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.gadget.dev/guides/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gadget.dev/reference
- group: auth
  href: https://artifacts.apis.io/gadget/security/gadget-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gadget-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gadget.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gadget.dev/
- group: operate
  title: ''
  type: Support
  url: https://gadget.dev/support
- group: company
  title: ''
  type: Blog
  url: https://gadget.dev/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gadget.dev/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gadget.dev/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://gadget.dev/pricing
coverage:
  checked: '2026-10-29'
  detail: Docs describe the API but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract is published.
  evidence:
  - status: 200
    url: https://docs.gadget.dev/api/example-app/development/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Gadget is an integrated development platform that provides everything needed to build, run, and scale full‑stack web applications. Offering a unified environment, Gadget stitches together tools for frontend, backend, data storage, and deployment, enabling developers to accelerate product delivery. Backed by Sequoia Capital, the company focuses on simplifying app development with a rich API ecosystem, extensive documentation, and developer‑friendly resources.
image: https://cdn.prod.website-files.com/60673aeb6d3163e7fda75a76/671a7a6d161e79cbbaad33a4_gadget-shopify-og-image.avif
json_schemas:
- name: GetAskResponse
  property_count: 3
  slug: gadget-get-ask-response
- name: GetInventorySkuResponse
  property_count: 1
  slug: gadget-get-inventory-sku-response
- name: PostAdminApi202604GraphqlJsonRequest
  property_count: 1
  slug: gadget-post-admin-api202604-graphql-json-request
- name: PostAdminApi202604GraphqlJsonResponse
  property_count: 1
  slug: gadget-post-admin-api202604-graphql-json-response
- name: PostApiGraphqlRequest
  property_count: 1
  slug: gadget-post-api-graphql-request
- name: PostApiRequest
  property_count: 1
  slug: gadget-post-api-request
- name: PostDataResponse
  property_count: 2
  slug: gadget-post-data-response
jsonld:
- class_count: 7
  name: Gadget Context
  property_count: 9
  slug: gadget-context
layout: provider
modified: '2026-10-28'
name: Gadget
nav: Providers
network: true
overview: 'Gadget is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including actions API, core API, http routes API, and 2 more. Tagged areas include Platform, Software-as-a-Service, Development, and Full-Stack.


  The Gadget catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gadget''s developer surface includes getting-started guide, changelog, API reference, documentation, support, engineering blog, pricing, and 18 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Gadget API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: gadget-rules
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 22.4
    contract_governance: 19.7
    contract_quality: 21.1
    developer_ergonomics: 25.0
    discoverability: 62.5
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gadget/gadget-2026-11-03T132446.png
security:
- kind: domain-security
  name: Gadget Domain Security
  slug: gadget-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gadget
tags:
- Platform
- Software-as-a-Service
- Development
- Full-Stack
website: https://gadget.dev/
---
