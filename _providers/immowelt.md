---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Immowelt Agentic Access
  operation_count: 14
  slug: immowelt-agentic-access
  summary_line: 14 operations · 9 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Immowelt provides RESTful APIs for real‑estate listings, import/export of listings, and seeker leads, as described in the developer portal.
  name: Immowelt API
  slug: immowelt-api
artifact_total: 29
common:
- group: auth
  href: https://artifacts.apis.io/immowelt/security/immowelt-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/immowelt-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/immowelt/authentication/immowelt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/immowelt-authentication.yml
- group: agent
  href: https://artifacts.apis.io/immowelt/llms/immowelt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/immowelt-llms.txt
- group: auth
  href: https://artifacts.apis.io/immowelt/well-known/immowelt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/immowelt-security.txt
- group: agent
  href: https://artifacts.apis.io/immowelt/well-known/immowelt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/immowelt-well-known.yml
- group: other
  href: https://artifacts.apis.io/immowelt/hosts/immowelt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/immowelt-hosts.yml
- group: other
  href: https://artifacts.apis.io/immowelt/vendors/immowelt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/immowelt-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.immowelt.de/
- group: auth
  href: https://artifacts.apis.io/immowelt/security/immowelt-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/immowelt-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/immowelt/security/immowelt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/immowelt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://immowelt.de/
coverage:
  checked: '2026-10-28'
  detail: The Immowelt developer portal provides documentation but the API base URL https://apim.immowelt.de/ returns HTTP 403 and no OpenAPI spec is publicly available.
  evidence:
  - status: 403
    url: https://apim.immowelt.de/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Immowelt is a leading German online real‑estate marketplace that connects property seekers with landlords, real‑estate agents and developers. The platform offers listings for apartments, houses, and commercial spaces across Germany and Austria, providing tools for searching, filtering, and contacting sellers. Immowelt also supplies market data, price trends, and a range of services for both private users and professional partners, positioning itself as a central hub in the European property market.
json_schemas:
- name: apiRequest
  property_count: 4
  slug: immowelt-api-request
- name: createLeadRequest
  property_count: 9
  slug: immowelt-create-lead-request
- name: GetExportStatusResponse
  property_count: 3
  slug: immowelt-get-export-status-response
- name: listingResponse
  property_count: 1
  slug: immowelt-listing-response
- name: mediaPresignedUrlRequest
  property_count: 2
  slug: immowelt-media-presigned-url-request
- name: mediaPresignedUrlResponse
  property_count: 2
  slug: immowelt-media-presigned-url-response
- name: passHealthResponse
  property_count: 2
  slug: immowelt-pass-health-response
- name: projectResponse
  property_count: 5
  slug: immowelt-project-response
- name: RequestListingsExportRequest
  property_count: 1
  slug: immowelt-request-listings-export-request
- name: RequestListingsExportResponse
  property_count: 1
  slug: immowelt-request-listings-export-response
- name: webhookAuditResponse
  property_count: 7
  slug: immowelt-webhook-audit-response
- name: webhookSubscriptionAddRequest
  property_count: 3
  slug: immowelt-webhook-subscription-add-request
- name: webhookSubscriptionListResponse
  property_count: 2
  slug: immowelt-webhook-subscription-list-response
- name: webhookSubscriptionResponse
  property_count: 5
  slug: immowelt-webhook-subscription-response
- name: webhookSubscriptionUpdateRequest
  property_count: 2
  slug: immowelt-webhook-subscription-update-request
jsonld:
- class_count: 40
  name: Immowelt Context
  property_count: 257
  slug: immowelt-context
layout: provider
modified: '2026-10-28'
name: Immowelt
nav: Providers
network: true
overview: 'Immowelt publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Marketplace, Germany, Austria, and Property Listings.


  The Immowelt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Immowelt''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Immowelt Plans Pricing
  plan_count: 0
  slug: immowelt-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Immowelt Rate Limits
  slug: immowelt-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Immowelt API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 2
  slug: immowelt-rules
scopes:
- name: Immowelt Scopes
  scope_count: 15
  slug: immowelt-scopes
  summary_line: 15 scopes
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 31
    catalog_earned: 53.5
    catalog_earned_first_party: 0.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 27.3
    developer_ergonomics: 16.7
    discoverability: 75.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - austria
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/immowelt/immowelt-2026-11-03T133721.png
security:
- kind: authentication
  name: Immowelt Authentication
  slug: immowelt-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Immowelt Domain Security
  slug: immowelt-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Immowelt Vulnerability Disclosure
  slug: immowelt-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: immowelt-export-listings
  slug: immowelt-export-listings
- name: immowelt-import-listings
  slug: immowelt-import-listings
- name: immowelt-ingest-lead
  slug: immowelt-ingest-lead
- name: immowelt-seeker-leads
  slug: immowelt-seeker-leads
slug: immowelt
tags:
- Real Estate
- Marketplace
- Germany
- Austria
- Property Listings
website: https://immowelt.de/
---
