---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Bettermenu Agentic Access
  operation_count: 82
  slug: bettermenu-agentic-access
  summary_line: 82 operations · 42 acting
api_count: 1
apis:
- baseURL: https://api.bettermenu.live
  baseurl_source: declared
  description: The Conversions API from BetterMenu — 1 operation(s) for conversions.
  name: BetterMenu Conversions API
  slug: bettermenu-conversions-api
- baseURL: https://api.bettermenu.live
  baseurl_source: declared
  description: Account entitlement and plan status.
  name: BetterMenu Entitlements API
  slug: bettermenu-entitlements-api
- baseURL: https://api.bettermenu.live
  baseurl_source: declared
  description: Organization-level capabilities spanning multiple resource types (e.g. search).
  name: BetterMenu Org API
  slug: bettermenu-org-api
- baseURL: https://api.bettermenu.live
  baseurl_source: declared
  description: 'Recipe authoring: create and manage recipes, servings, ingredient resolution, nutrition computation and analysis, labels, and version history.'
  name: BetterMenu Studio API
  slug: bettermenu-studio-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/bettermenu/agentic-access/bettermenu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bettermenu-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bettermenu/rules/bettermenu-rules.yml
  title: ''
  type: Spectral
  url: rules/bettermenu-rules.yml
- group: design
  href: https://artifacts.apis.io/bettermenu/json-ld/bettermenu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bettermenu-context.jsonld
- group: design
  href: https://artifacts.apis.io/bettermenu/vocabulary/bettermenu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bettermenu-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bettermenu/conformance/bettermenu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bettermenu-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/bettermenu/plans/bettermenu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bettermenu-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bettermenu/data-model/bettermenu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bettermenu-data-model.yml
- group: design
  href: https://artifacts.apis.io/bettermenu/errors/bettermenu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bettermenu-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/bettermenu/llms/bettermenu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bettermenu-llms.txt
- group: agent
  href: https://artifacts.apis.io/bettermenu/well-known/bettermenu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bettermenu-well-known.yml
- group: other
  href: https://artifacts.apis.io/bettermenu/hosts/bettermenu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bettermenu-hosts.yml
- group: other
  href: https://artifacts.apis.io/bettermenu/vendors/bettermenu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bettermenu-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://bettermenu.live/changelog/
- group: auth
  href: https://artifacts.apis.io/bettermenu/security/bettermenu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bettermenu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bettermenu.live/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bettermenu.live/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bettermenu.live/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://bettermenu.live/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bettermenu.live/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bettermenu.live/privacy/
- group: operate
  title: ''
  type: Support
  url: https://bettermenu.live/support/
- group: company
  title: ''
  type: Blog
  url: https://bettermenu.live/blog/
coverage:
  checked: '2026-10-21'
  detail: The provider's documentation at https://docs.bettermenu.live/docs/api is HTML with no machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://docs.bettermenu.live/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: BetterMenu provides a cloud‑based recipe formulation platform for food manufacturers, enabling rapid product development with built‑in FDA‑compliant nutrition labeling. Users can input ingredient lists and instantly generate nutrition facts panels, streamline formulation, and accelerate time‑to‑market while ensuring regulatory compliance. The service offers a web‑based interface, pricing plans, and integrates FDA guidelines to help bring food products to market faster.
image: https://bettermenu.live/images/og-image.png
json_schemas:
- name: CheckoutRequest
  property_count: 3
  slug: bettermenu-checkout-request
- name: ComputeConversionsRequest
  property_count: 3
  slug: bettermenu-compute-conversions-request
- name: CreateCustomIngredientRequest
  property_count: 8
  slug: bettermenu-create-custom-ingredient-request
- name: CreateSearchTokenRequest
  property_count: 1
  slug: bettermenu-create-search-token-request
- name: EntitlementStatusResponse
  property_count: 12
  slug: bettermenu-entitlement-status-response
- name: GetIngredientResponse
  property_count: 16
  slug: bettermenu-get-ingredient-response
- name: PatchAddedSugarsReportRowRequest
  property_count: 5
  slug: bettermenu-patch-added-sugars-report-row-request
- name: PlansResponse
  property_count: 1
  slug: bettermenu-plans-response
- name: PortalRequest
  property_count: 1
  slug: bettermenu-portal-request
- name: PortalResponse
  property_count: 1
  slug: bettermenu-portal-response
- name: RecordReferenceFoodViewRequest
  property_count: 11
  slug: bettermenu-record-reference-food-view-request
- name: ReferenceFood
  property_count: 12
  slug: bettermenu-reference-food
- name: ReferenceServingSize
  property_count: 12
  slug: bettermenu-reference-serving-size
- name: SearchTokenResponse
  property_count: 5
  slug: bettermenu-search-token-response
- name: UpdateOrgSettingsRequest
  property_count: 2
  slug: bettermenu-update-org-settings-request
- name: UpdateOrgSettingsResponse
  property_count: 2
  slug: bettermenu-update-org-settings-response
- name: UsageResponse
  property_count: 8
  slug: bettermenu-usage-response
jsonld:
- class_count: 120
  name: Bettermenu Context
  property_count: 293
  slug: bettermenu-context
layout: provider
modified: '2026-10-21'
name: BetterMenu
nav: Providers
network: true
overview: 'BetterMenu publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Conversions API, Entitlements API, Org API, and 1 more. Tagged areas include Food Tech, RecipeFormulation, FDA Compliance, Software-as-a-Service, and Cloud.


  The BetterMenu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BetterMenu''s developer surface includes changelog, documentation, API reference, pricing, support, engineering blog, and 16 more developer resources.'
plans:
- name: Bettermenu Plans Pricing
  plan_count: 1
  slug: bettermenu-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: BetterMenu API Rules
  rule_count: 47
  severity_counts:
    error: 37
    hint: 0
    info: 3
    warn: 7
  slug: bettermenu-rules
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 47.8
    developer_ergonomics: 11.9
    discoverability: 73.2
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 25.0
      total: 4
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/bettermenu/bettermenu-2026-11-03T121700.png
security:
- kind: domain-security
  name: Bettermenu Domain Security
  slug: bettermenu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bettermenu
tags:
- Food Tech
- RecipeFormulation
- FDA Compliance
- Software-as-a-Service
- Cloud
website: https://bettermenu.live/
---
