---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The Reporting API uses HTTP API, follows a RESTful design pattern, returns JSON, and enforces a rate limit of 5 requests per second.
  name: Reporting API
  slug: reporting-api
- baseURL: https://dashboard.pubnative.net
  baseurl_source: declared
  description: 'PubNative API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: PubNative API
  slug: pubnative-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/pubnative/rules/pubnative-rules.yml
  title: ''
  type: Spectral
  url: rules/pubnative-rules.yml
- group: design
  href: https://artifacts.apis.io/pubnative/json-ld/pubnative-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pubnative-context.jsonld
- group: design
  href: https://artifacts.apis.io/pubnative/vocabulary/pubnative-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pubnative-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pubnative/data-model/pubnative-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pubnative-data-model.yml
- group: auth
  href: https://artifacts.apis.io/pubnative/security/pubnative-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/pubnative-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/pubnative/conformance/pubnative-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pubnative-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pubnative/llms/pubnative-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pubnative-llms.txt
- group: other
  href: https://artifacts.apis.io/pubnative/hosts/pubnative-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pubnative-hosts.yml
- group: other
  href: https://artifacts.apis.io/pubnative/vendors/pubnative-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pubnative-vendors.yml
- group: build
  href: https://artifacts.apis.io/pubnative/packages/pubnative-packages.yml
  title: ''
  type: SDKs
  url: packages/pubnative-packages.yml
- group: build
  href: https://artifacts.apis.io/pubnative/packages/pubnative-packages.yml
  title: ''
  type: Packages
  url: packages/pubnative-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://verve.com/press/
- group: auth
  href: https://artifacts.apis.io/pubnative/security/pubnative-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pubnative-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pubnative/security/pubnative-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pubnative-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://verve.com/performance-marketplace-for-publishers/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.verve.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.verve.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.verve.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.verve.com/docs/guide-getting-started
- group: operate
  title: ''
  type: Support
  url: https://verve.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://verve.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://verve.com/website-privacy-policy/
coverage:
  checked: '2026-11-01'
  detail: Documentation provides endpoint examples but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://developers.verve.com/reference/reporting-api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: PubNative, now operating as the Performance+ Marketplace within the Verve Group, provides a mobile app monetization platform that connects publishers with premium demand from top brands and performance bidders. Leveraging open-source SDKs, AI-powered on‑device user value prediction, and privacy‑first, ID‑less targeting, PubNative enables publishers to maximize yield across in‑app inventory, offering transparent, customizable ad experiences and robust integration options via SDKs and OpenRTB. The solution is part of Verve’s broader media ecosystem, delivering cross‑channel monetization, audience growth, and data‑driven performance for advertisers and publishers worldwide.
image: https://verve.com/wp-content/uploads/2026/01/p-publishers-homepage-1.png
json_schemas:
- name: GetApiReportsDspResponse
  property_count: 2
  slug: pubnative-get-api-reports-dsp-response
- name: GetApiReportsResponse
  property_count: 10
  slug: pubnative-get-api-reports-response
- name: PostBidV1RequestApptokenAppTokenZoneidYourZoneIdRequest
  property_count: 5
  slug: pubnative-post-bid-v1-request-apptoken-app-token-zoneid-your-zone-id-request
- name: PostBidV1RequestApptokenAppTokenZoneidYourZoneIdResponse
  property_count: 3
  slug: pubnative-post-bid-v1-request-apptoken-app-token-zoneid-your-zone-id-response
- name: PostBidV1RequestRequest
  property_count: 5
  slug: pubnative-post-bid-v1-request-request
jsonld:
- class_count: 5
  name: Pubnative Context
  property_count: 20
  slug: pubnative-context
layout: provider
modified: '2026-11-01'
name: PubNative
nav: Providers
network: true
overview: 'PubNative is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AdTech, Mobile, Monetization, and Publishers.


  The PubNative catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PubNative''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 17 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: PubNative API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: pubnative-rules
scopes:
- name: Pubnative Scopes
  scope_count: 0
  slug: pubnative-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 25.1
    developer_ergonomics: 29.8
    discoverability: 67.0
    operational_transparency: 10.5
  previous_composite: 31.9
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
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pubnative Authentication
  slug: pubnative-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pubnative Domain Security
  slug: pubnative-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pubnative Vulnerability Disclosure
  slug: pubnative-vulnerability-disclosure
  summary_line: no policy recorded
slug: pubnative
tags:
- Company
- AdTech
- Mobile
- Monetization
- Publishers
website: https://verve.com/performance-marketplace-for-publishers/
---
