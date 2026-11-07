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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Purple Dot pre‑order platform.
  name: Purple Dot API
  slug: purple-dot-api-2
- baseURL: https://www.purpledotprice.com
  baseurl_source: declared
  description: 'Purple Dot API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Purple Dot API
  slug: purple-dot-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/purple-dot/rules/purple-dot-rules.yml
  title: ''
  type: Spectral
  url: rules/purple-dot-rules.yml
- group: design
  href: https://artifacts.apis.io/purple-dot/json-ld/purple-dot-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/purple-dot-context.jsonld
- group: design
  href: https://artifacts.apis.io/purple-dot/vocabulary/purple-dot-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/purple-dot-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/purple-dot/data-model/purple-dot-data-model.yml
  title: ''
  type: DataModel
  url: data-model/purple-dot-data-model.yml
- group: design
  href: https://artifacts.apis.io/purple-dot/conformance/purple-dot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/purple-dot-conformance.yml
- group: agent
  href: https://artifacts.apis.io/purple-dot/llms/purple-dot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/purple-dot-llms.txt
- group: agent
  href: https://artifacts.apis.io/purple-dot/well-known/purple-dot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/purple-dot-well-known.yml
- group: other
  href: https://artifacts.apis.io/purple-dot/hosts/purple-dot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/purple-dot-hosts.yml
- group: other
  href: https://artifacts.apis.io/purple-dot/vendors/purple-dot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/purple-dot-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getpurpledot.com/docs
- group: auth
  href: https://artifacts.apis.io/purple-dot/security/purple-dot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/purple-dot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.purpledotprice.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getpurpledot.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getpurpledot.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.getpurpledot.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getpurpledot.com/information/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Documentation provides markdown pages but no OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://docs.getpurpledot.com/docs/purple-dot-apis/public-api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Purple Dot provides a premium pre‑order platform enabling brands to sell products before they arrive in inventory. The service automates pre‑order sales, reduces inventory risk, and integrates with existing e‑commerce systems. It offers AI‑driven order management, flexible commerce tools, and a merchant portal for real‑time insights, helping modern brands capture demand and launch products efficiently.
image: https://cdn.prod.website-files.com/63f4871215420df736d2cc24/63f4871215420d9a12d2cc77_Purple-dot-coffee-p-1600.jpg
json_schemas:
- name: GetAdminApiV1PreOrdersResponse
  property_count: 21
  slug: purple-dot-get-admin-api-v1-pre-orders-response
- name: GetAdminApiV1WaitlistsResponse
  property_count: 8
  slug: purple-dot-get-admin-api-v1-waitlists-response
- name: GetApiV1PreOrdersResponse
  property_count: 3
  slug: purple-dot-get-api-v1-pre-orders-response
- name: PostAdminApiV1RefundRequest
  property_count: 4
  slug: purple-dot-post-admin-api-v1-refund-request
jsonld:
- class_count: 4
  name: Purple Dot Context
  property_count: 32
  slug: purple-dot-context
layout: provider
modified: '2026-10-29'
name: Purple Dot
nav: Providers
network: true
overview: 'Purple Dot is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pre-Order, E-Commerce, Software-as-a-Service, and Artificial Intelligence.


  The Purple Dot catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Purple Dot''s developer surface includes documentation, getting-started guide, engineering blog, and 13 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Purple Dot API Rules
  rule_count: 40
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 2
  slug: purple-dot-rules
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 22.4
    developer_ergonomics: 16.7
    discoverability: 64.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/purple-dot/purple-dot-2026-11-03T141720.png
security:
- kind: domain-security
  name: Purple Dot Domain Security
  slug: purple-dot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: purple-dot
tags:
- Company
- Pre-Order
- E-Commerce
- Software-as-a-Service
- Artificial Intelligence
website: https://www.purpledotprice.com/
---
