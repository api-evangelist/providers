---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Alto API as documented publicly: 31 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Alto API
  slug: alto-video-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/alto-video/plans/alto-video-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alto-video-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/alto-video/rules/alto-video-rules.yml
  title: ''
  type: Spectral
  url: rules/alto-video-rules.yml
- group: design
  href: https://artifacts.apis.io/alto-video/json-ld/alto-video-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/alto-video-context.jsonld
- group: design
  href: https://artifacts.apis.io/alto-video/vocabulary/alto-video-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alto-video-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/alto-video/data-model/alto-video-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alto-video-data-model.yml
- group: auth
  href: https://artifacts.apis.io/alto-video/authentication/alto-video-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alto-video-authentication.yml
- group: design
  href: https://artifacts.apis.io/alto-video/conformance/alto-video-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alto-video-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alto-video/llms/alto-video-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alto-video-llms.txt
- group: auth
  href: https://artifacts.apis.io/alto-video/well-known/alto-video-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alto-video-security.txt
- group: agent
  href: https://artifacts.apis.io/alto-video/well-known/alto-video-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alto-video-well-known.yml
- group: other
  href: https://artifacts.apis.io/alto-video/hosts/alto-video-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alto-video-hosts.yml
- group: other
  href: https://artifacts.apis.io/alto-video/vendors/alto-video-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alto-video-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://alto.video/status
- group: auth
  title: ''
  type: Security
  url: https://alto.video/security
- group: start
  title: ''
  type: Login
  url: https://alto.video/signin
- group: auth
  href: https://artifacts.apis.io/alto-video/security/alto-video-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/alto-video-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/alto-video/security/alto-video-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alto-video-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alto.video/
- group: docs
  title: ''
  type: Documentation
  url: https://alto.video/docs
- group: docs
  title: ''
  type: APIReference
  url: https://alto.video/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://alto.video/docs/cli-and-mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://alto.video/pricing
- group: operate
  title: ''
  type: Support
  url: https://alto.video/support
- group: company
  title: ''
  type: Blog
  url: https://alto.video/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alto.video/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alto.video/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://alto.video/mcp
  - status: 200
    url: https://alto.video/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Alto provides a video hosting platform tailored for sales demos, allowing agents to upload, share, and track demo videos with detailed viewer analytics. The service emphasizes privacy, easy integration, and tools for agents to personalize demo experiences. Alto aims to replace traditional file sharing and public video platforms for business demo workflows, offering features like viewer heatmaps, engagement metrics, and secure video delivery.
image: https://alto.video/og/home.png
json_schemas:
- name: GetApiConnectCodeResponse
  property_count: 4
  slug: alto-video-get-api-connect-code-response
- name: GetApiLinksResponse
  property_count: 1
  slug: alto-video-get-api-links-response
- name: GetApiVideosIdResponse
  property_count: 6
  slug: alto-video-get-api-videos-id-response
- name: GetApiVideosIdStatusResponse
  property_count: 2
  slug: alto-video-get-api-videos-id-status-response
- name: PatchApiVideosIdRequest
  property_count: 6
  slug: alto-video-patch-api-videos-id-request
- name: PostApiVideosIdLinksRequest
  property_count: 3
  slug: alto-video-post-api-videos-id-links-request
jsonld:
- class_count: 33
  name: Alto Video Context
  property_count: 37
  slug: alto-video-context
layout: provider
modified: '2026-11-01'
name: Alto
nav: Providers
network: true
overview: 'Alto is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video Hosting, Sales Enablement, Demo Analytics, Privacy, and Software-as-a-Service.


  The Alto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Alto''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, engineering blog, and 19 more developer resources.'
plans:
- name: Alto Video Plans Pricing
  plan_count: 4
  slug: alto-video-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Alto API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: alto-video-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 53.9
    contract_governance: 19.7
    contract_quality: 24.7
    developer_ergonomics: 29.8
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 44.7
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
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alto Video Authentication
  slug: alto-video-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Alto Video Domain Security
  slug: alto-video-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Alto Video Vulnerability Disclosure
  slug: alto-video-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: alto-video
tags:
- Video Hosting
- Sales Enablement
- Demo Analytics
- Privacy
- Software-as-a-Service
website: https://alto.video/
---
