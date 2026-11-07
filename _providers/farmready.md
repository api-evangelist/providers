---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The FarmReady REST API gives external systems programmatic access to your farm data.
  name: FarmReady API
  slug: farmready-api-2
- description: 'FarmReady (Bolt, Cart, Shed) API as documented publicly: 23 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: FarmReady (Bolt, Cart, Shed) API
  slug: farmready-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/farmready/rate-limits/farmready-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/farmready-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/farmready/rules/farmready-rules.yml
  title: ''
  type: Spectral
  url: rules/farmready-rules.yml
- group: design
  href: https://artifacts.apis.io/farmready/json-ld/farmready-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/farmready-context.jsonld
- group: design
  href: https://artifacts.apis.io/farmready/vocabulary/farmready-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/farmready-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/farmready/data-model/farmready-data-model.yml
  title: ''
  type: DataModel
  url: data-model/farmready-data-model.yml
- group: design
  href: https://artifacts.apis.io/farmready/conventions/farmready-conventions.yml
  title: ''
  type: Conventions
  url: conventions/farmready-conventions.yml
- group: auth
  href: https://artifacts.apis.io/farmready/authentication/farmready-authentication.yml
  title: ''
  type: Authentication
  url: authentication/farmready-authentication.yml
- group: design
  href: https://artifacts.apis.io/farmready/lifecycle/farmready-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/farmready-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/farmready/conformance/farmready-conformance.yml
  title: ''
  type: Conformance
  url: conformance/farmready-conformance.yml
- group: other
  href: https://artifacts.apis.io/farmready/hosts/farmready-hosts.yml
  title: ''
  type: Hosts
  url: hosts/farmready-hosts.yml
- group: other
  href: https://artifacts.apis.io/farmready/vendors/farmready-vendors.yml
  title: ''
  type: Vendors
  url: vendors/farmready-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/farmready
- group: auth
  href: https://artifacts.apis.io/farmready/security/farmready-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/farmready-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.farmready.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.farmready.io/help
- group: company
  title: ''
  type: Blog
  url: https://www.farmready.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.farmready.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.farmready.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.farmready.io/account/register
- group: operate
  title: ''
  type: Support
  url: https://www.farmready.io/help
coverage:
  checked: '2026-10-28'
  detail: Documentation is publicly accessible HTML but provides no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://www.farmready.io/developer/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: FarmReady provides a suite of farm management applications—including Shed for inventory, Bolt for equipment, Cart for grain contracts, and Crew for safety—to help farms digitize operations, track assets, manage grain logistics, and improve workplace safety. The platform offers a free beta for farms, with tools accessible via web and mobile interfaces, aiming to streamline farm workflows and data visibility.
image: https://www.farmready.io/images/icons-d7f19a4be1dc8d3253364f846fca164c.svg?vsn=d
json_schemas:
- name: GetApiShedOrganisationsOrgidProductsResponse
  property_count: 20
  slug: farmready-get-api-shed-organisations-orgid-products-response
- name: GetApiShedProductsIdResponse
  property_count: 14
  slug: farmready-get-api-shed-products-id-response
- name: GetApiShedReceiptsIdResponse
  property_count: 13
  slug: farmready-get-api-shed-receipts-id-response
- name: GetApiShedReturnsIdResponse
  property_count: 14
  slug: farmready-get-api-shed-returns-id-response
- name: PatchApiShedOrganisationsOrgidReturnsIdResponse
  property_count: 13
  slug: farmready-patch-api-shed-organisations-orgid-returns-id-response
- name: PostApiShedOrganisationsOrgidReturnsRequest
  property_count: 8
  slug: farmready-post-api-shed-organisations-orgid-returns-request
jsonld:
- class_count: 24
  name: Farmready Context
  property_count: 38
  slug: farmready-context
layout: provider
modified: '2026-10-28'
name: FarmReady (Bolt, Cart, Shed)
nav: Providers
network: true
overview: 'FarmReady (Bolt, Cart, Shed) is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Farm Management, Inventory, and Equipment.


  The FarmReady (Bolt, Cart, Shed) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FarmReady (Bolt, Cart, Shed)''s developer surface includes authentication, documentation, engineering blog, signup flow, support, and 15 more developer resources.'
plans:
- name: Farmready Plans Pricing
  plan_count: 0
  slug: farmready-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Farmready Rate Limits
  slug: farmready-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: FarmReady (Bolt, Cart, Shed) API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: farmready-rules
scopes:
- name: Farmready Scopes
  scope_count: 0
  slug: farmready-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 20.2
    discoverability: 57.1
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/farmready/farmready-2026-11-03T131851.png
security:
- kind: authentication
  name: Farmready Authentication
  slug: farmready-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Farmready Domain Security
  slug: farmready-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: farmready
tags:
- Company
- Agriculture
- Farm Management
- Inventory
- Equipment
- Safety
website: https://www.farmready.io/
---
