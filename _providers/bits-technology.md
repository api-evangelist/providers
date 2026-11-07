---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://api.bits.bi
  baseurl_source: spec
  description: API for Bits Technology compliance platform, documented at https://docs.bits.bi/api-reference
  name: Bits Technology API
  slug: bits-technology-api
- baseURL: https://api.bits.bi
  baseurl_source: declared
  description: The Applications API from Bits Technology — 2 operation(s) for applications.
  name: Bits Technology Applications API
  slug: bits-technology-applications-api
- baseURL: https://api.bits.bi
  baseurl_source: declared
  description: The Oauth2 API from Bits Technology — 2 operation(s) for oauth2.
  name: Bits Technology Oauth2 API
  slug: bits-technology-oauth2-api
artifact_total: 12
common:
- group: other
  href: https://artifacts.apis.io/bits-technology/vendors/bits-technology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bits-technology-vendors.yml
- group: design
  href: https://artifacts.apis.io/bits-technology/rules/bits-technology-rules.yml
  title: ''
  type: Spectral
  url: rules/bits-technology-rules.yml
- group: design
  href: https://artifacts.apis.io/bits-technology/json-ld/bits-technology-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bits-technology-context.jsonld
- group: design
  href: https://artifacts.apis.io/bits-technology/vocabulary/bits-technology-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bits-technology-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bits-technology/data-model/bits-technology-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bits-technology-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bits-technology/changelog/bits-technology-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bits-technology-changelog.yml
- group: start
  href: https://artifacts.apis.io/bits-technology/sandbox/bits-technology-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bits-technology-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/bits-technology/security/bits-technology-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bits-technology-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bits-technology/authentication/bits-technology-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bits-technology-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.bits.bi/api-reference/versioning
- group: design
  href: https://artifacts.apis.io/bits-technology/lifecycle/bits-technology-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bits-technology-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bits-technology/conformance/bits-technology-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bits-technology-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bits-technology/llms/bits-technology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bits-technology-llms.txt
- group: auth
  href: https://artifacts.apis.io/bits-technology/well-known/bits-technology-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bits-technology-security.txt
- group: auth
  href: https://artifacts.apis.io/bits-technology/well-known/bits-technology-bits-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bits-technology-bits-security.txt
- group: agent
  href: https://artifacts.apis.io/bits-technology/well-known/bits-technology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bits-technology-well-known.yml
- group: other
  href: https://artifacts.apis.io/bits-technology/hosts/bits-technology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bits-technology-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.bits.bi/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bits.bi/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bits.bi/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bits.bi/use-cases/onboarding
- group: auth
  href: https://artifacts.apis.io/bits-technology/security/bits-technology-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bits-technology-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bits-technology/security/bits-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bits-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bits.bi/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bits.bi/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.bits.bi/developers
- group: company
  title: ''
  type: Blog
  url: https://www.bits.bi/resources/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bits.bi/resources/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bits.bi/resources/legal
coverage:
  checked: '2026-10-15'
  detail: API reference page is a JavaScript‑rendered Next.js site with no static OpenAPI spec
  evidence:
  - status: 200
    url: https://docs.bits.bi/api-reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Bits Technology provides a compliance platform for the AMLR era, helping regulated financial companies streamline onboarding, transaction monitoring, AML risk scoring, and ongoing due diligence. Based in Europe, Bits unifies anti‑money‑laundering processes for fintechs, offering automated compliance operations, case management, and measurable growth. The platform supports integrations, APIs, and a developer portal for building compliant financial services.
image: https://framerusercontent.com/images/NpU8G6c75uZqE07Xv48CXn7fuQ.jpg
json_schemas:
- name: GetOauth2UserinfoResponse
  property_count: 1
  slug: bits-technology-get-oauth2-userinfo-response
- name: PostApplicationsBankaccountsListRequest
  property_count: 1
  slug: bits-technology-post-applications-bankaccounts-list-request
- name: PostApplicationsCreateRequest
  property_count: 3
  slug: bits-technology-post-applications-create-request
- name: PostApplicationsCreateResponse
  property_count: 2
  slug: bits-technology-post-applications-create-response
jsonld:
- class_count: 4
  name: Bits Technology Context
  property_count: 7
  slug: bits-technology-context
layout: provider
modified: '2026-10-15'
name: Bits Technology
nav: Providers
network: true
overview: 'Bits Technology is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Oauth2 API, and 1 more. Tagged areas include Company, AML, Compliance, Fintech, and Europe.


  The Bits Technology catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bits Technology''s developer surface includes changelog, sandbox, authentication, API reference, getting-started guide, documentation, engineering blog, and 22 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Bits Technology API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: bits-technology-rules
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 21.4
    developer_ergonomics: 39.3
    discoverability: 70.5
    operational_transparency: 22.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 38.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bits-technology/bits-technology-2026-11-03T121804.png
security:
- kind: authentication
  name: Bits Technology Authentication
  slug: bits-technology-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bits Technology Domain Security
  slug: bits-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bits Technology Vulnerability Disclosure
  slug: bits-technology-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bits-technology
tags:
- Company
- AML
- Compliance
- Fintech
- Europe
website: https://bits.bi/
---
