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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation for Wevo automotive components and services.
  name: Wevo API
  slug: wevo-api-2
- description: 'Wevo API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Wevo API
  slug: wevo-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/wevo/rules/wevo-rules.yml
  title: ''
  type: Spectral
  url: rules/wevo-rules.yml
- group: design
  href: https://artifacts.apis.io/wevo/json-ld/wevo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wevo-context.jsonld
- group: design
  href: https://artifacts.apis.io/wevo/vocabulary/wevo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wevo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/wevo/data-model/wevo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wevo-data-model.yml
- group: build
  href: https://artifacts.apis.io/wevo/cli/wevo-cli.yml
  title: ''
  type: CLI
  url: cli/wevo-cli.yml
- group: design
  href: https://artifacts.apis.io/wevo/conventions/wevo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wevo-conventions.yml
- group: auth
  href: https://artifacts.apis.io/wevo/authentication/wevo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wevo-authentication.yml
- group: design
  href: https://artifacts.apis.io/wevo/conformance/wevo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wevo-conformance.yml
- group: other
  href: https://artifacts.apis.io/wevo/hosts/wevo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wevo-hosts.yml
- group: other
  href: https://artifacts.apis.io/wevo/vendors/wevo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wevo-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.jitterbit.com:443/resources/type/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jitterbit.com/api-manager/quickstart-guide/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jitterbit.com/
- group: auth
  href: https://artifacts.apis.io/wevo/security/wevo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wevo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wevo.com.br/
coverage:
  checked: '2026-10-21'
  detail: Homepage is a static HTML page with no machine‑readable API spec discovered
  evidence:
  - status: 404
    url: https://wevo.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Wevo (Windrush Evolutions Inc.) is a California‑based company specializing in design, testing, development and implementation of automotive components, primarily for Porsche vehicles. They offer a range of over 100 WEVO products covering model series from 1965 to 2008, provide motorsports engineering services, and partner with global Porsche specialists. The firm manufactures domestically, outsources drawing‑to‑part production, and supports racing teams across club to advanced sportscar categories.
image: https://www.jitterbit.com/wp-content/uploads/jitterbit-social-banner.jpg
json_schemas:
- name: GetRestV1VinylDeployMetadataResponse
  property_count: 6
  slug: wevo-get-rest-v1-vinyl-deploy-metadata-response
- name: GetRestV1VinylDeployReleaseQueueReleaseidResponse
  property_count: 11
  slug: wevo-get-rest-v1-vinyl-deploy-release-queue-releaseid-response
- name: GetRestV1VinylDeployReleaseReleaseidResponse
  property_count: 13
  slug: wevo-get-rest-v1-vinyl-deploy-release-releaseid-response
- name: PostRestV1VinylDeployReleaseQueueResponse
  property_count: 11
  slug: wevo-post-rest-v1-vinyl-deploy-release-queue-response
- name: PostRestV1VinylDeployReleaseResponse
  property_count: 13
  slug: wevo-post-rest-v1-vinyl-deploy-release-response
- name: PutJitterbitCloudRestfulServiceUserLoginResponse
  property_count: 8
  slug: wevo-put-jitterbit-cloud-restful-service-user-login-response
jsonld:
- class_count: 15
  name: Wevo Context
  property_count: 40
  slug: wevo-context
layout: provider
modified: '2026-10-21'
name: Wevo
nav: Providers
network: true
overview: 'Wevo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, Automation, iPaaS, API Management, and Low-Code.


  The Wevo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wevo''s developer surface includes CLI, authentication, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Wevo API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: wevo-rules
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 0.0
    contract_governance: 35.6
    contract_quality: 24.7
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.0
  provenance:
    conformance: first-party
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
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/wevo/wevo-2026-11-03T150135.png
security:
- kind: authentication
  name: Wevo Authentication
  slug: wevo-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Wevo Domain Security
  slug: wevo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: wevo
tags:
- Integration
- Automation
- iPaaS
- API Management
- Low-Code
- Artificial Intelligence
- EDI
website: https://wevo.com.br/
---
