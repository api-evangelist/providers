---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: negotiable
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://console.fyber.com
  baseurl_source: declared
  description: 'Digital Turbine (Fyber) API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Digital Turbine (Fyber) API
  slug: digital-turbine-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/digital-turbine/rules/digital-turbine-rules.yml
  title: ''
  type: Spectral
  url: rules/digital-turbine-rules.yml
- group: design
  href: https://artifacts.apis.io/digital-turbine/json-ld/digital-turbine-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/digital-turbine-context.jsonld
- group: design
  href: https://artifacts.apis.io/digital-turbine/vocabulary/digital-turbine-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/digital-turbine-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/digital-turbine/data-model/digital-turbine-data-model.yml
  title: ''
  type: DataModel
  url: data-model/digital-turbine-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.digitalturbine.com/
- group: auth
  href: https://artifacts.apis.io/digital-turbine/authentication/digital-turbine-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digital-turbine-authentication.yml
- group: design
  href: https://artifacts.apis.io/digital-turbine/conformance/digital-turbine-conformance.yml
  title: ''
  type: Conformance
  url: conformance/digital-turbine-conformance.yml
- group: agent
  href: https://artifacts.apis.io/digital-turbine/llms/digital-turbine-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digital-turbine-llms.txt
- group: agent
  href: https://artifacts.apis.io/digital-turbine/well-known/digital-turbine-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/digital-turbine-well-known.yml
- group: other
  href: https://artifacts.apis.io/digital-turbine/hosts/digital-turbine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digital-turbine-hosts.yml
- group: other
  href: https://artifacts.apis.io/digital-turbine/vendors/digital-turbine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digital-turbine-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digitalturbine.com/legal/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.digitalturbine.com/dt-exchange/getting-started-with-dt-exchange
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DigitalTurbine
- group: auth
  href: https://artifacts.apis.io/digital-turbine/security/digital-turbine-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/digital-turbine-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/digital-turbine/security/digital-turbine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digital-turbine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digitalturbine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digitalturbine.com/
- group: company
  title: ''
  type: Blog
  url: https://www.digitalturbine.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.fyber.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.digitalturbine.com/legal/terms-of-use
coverage:
  checked: '2026-10-26'
  detail: Documentation is provided as markdown pages without a published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.digitalturbine.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Digital Turbine provides a mobile growth and monetization platform connecting advertisers, app developers, and device partners. It offers solutions like DT Launchpad for app acquisition, DT Ads for advertising, DT Ignite for device engagement, and a suite of SDKs and APIs enabling app distribution, ad monetization, and data-driven optimization across billions of devices.
image: https://cdn.prod.website-files.com/69f832754e7f6f5bd3314f06/69f9ed601191c74d6a307f36_Digital-Turbine-OG-Image.png
json_schemas:
- name: GetApiManagementV1AppResponse
  property_count: 13
  slug: digital-turbine-get-api-management-v1-app-response
- name: GetApiManagementV1InstanceResponse
  property_count: 11
  slug: digital-turbine-get-api-management-v1-instance-response
- name: PostApiManagementV1AppResponse
  property_count: 12
  slug: digital-turbine-post-api-management-v1-app-response
- name: PostApiManagementV1InstanceRequest
  property_count: 10
  slug: digital-turbine-post-api-management-v1-instance-request
- name: PostApiManagementV1InstanceResponse
  property_count: 10
  slug: digital-turbine-post-api-management-v1-instance-response
- name: PutApiManagementV1InstanceResponse
  property_count: 10
  slug: digital-turbine-put-api-management-v1-instance-response
jsonld:
- class_count: 14
  name: Digital Turbine Context
  property_count: 34
  slug: digital-turbine-context
layout: provider
modified: '2026-10-26'
name: Digital Turbine (Fyber)
nav: Providers
network: true
overview: 'Digital Turbine (Fyber) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile, Advertising, Monetization, and SDK.


  The Digital Turbine (Fyber) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Digital Turbine (Fyber)''s developer surface includes authentication, getting-started guide, documentation, engineering blog, pricing, and 16 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Digital Turbine (Fyber) API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: digital-turbine-rules
scopes:
- name: Digital Turbine Scopes
  scope_count: 0
  slug: digital-turbine-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 27.6
    contract_governance: 33.3
    contract_quality: 28.7
    developer_ergonomics: 28.6
    discoverability: 73.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
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
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/digital-turbine/digital-turbine-2026-11-03T130708.png
security:
- kind: authentication
  name: Digital Turbine Authentication
  slug: digital-turbine-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Digital Turbine Domain Security
  slug: digital-turbine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Digital Turbine Trust Center
  slug: digital-turbine-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: digital-turbine
tags:
- Company
- Mobile
- Advertising
- Monetization
- SDK
website: https://www.digitalturbine.com/
---
