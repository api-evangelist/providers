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
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: BrandMov REST API providing ad intelligence endpoints such as authentication, account, ad-copy, meta publishing, and watchlists.
  name: BrandMov API
  slug: brandmov-api
- baseURL: https://api.brandmov.com
  baseurl_source: declared
  description: 'BrandMov API as documented publicly: 47 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: BrandMov API
  slug: brandmov-com-api
artifact_total: 14
asyncapis:
- description: ''
  name: Brandmov Com Webhooks
  slug: brandmov-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/brandmov-com/rules/brandmov-com-rules.yml
  title: ''
  type: Spectral
  url: rules/brandmov-com-rules.yml
- group: design
  href: https://artifacts.apis.io/brandmov-com/json-ld/brandmov-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/brandmov-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/brandmov-com/vocabulary/brandmov-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brandmov-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/brandmov-com/asyncapi/brandmov-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/brandmov-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/brandmov-com/data-model/brandmov-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brandmov-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/brandmov-com/changelog/brandmov-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/brandmov-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/brandmov-com/authentication/brandmov-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brandmov-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/brandmov-com/conformance/brandmov-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brandmov-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brandmov-com/well-known/brandmov-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brandmov-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/brandmov-com/hosts/brandmov-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brandmov-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/brandmov-com/vendors/brandmov-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brandmov-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brandmov.com/terms
- group: auth
  title: ''
  type: Security
  url: https://brandmov.com/security
- group: operate
  title: ''
  type: Roadmap
  url: https://brandmov.com/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brandmov.com/privacy
- group: start
  title: ''
  type: Login
  url: https://brandmov.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://brandmov.com/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://brandmov.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://brandmov.com/blog
- group: auth
  href: https://artifacts.apis.io/brandmov-com/security/brandmov-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brandmov-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/brandmov-com/security/brandmov-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brandmov-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandmov.com/
created: '2026-11-02'
description: BrandMov provides competitor ad intelligence for agencies, offering watchlists for Meta and Google, a curated library of over 56,000 DTC and local ads, and tools to clone winning ads as paused drafts. The platform enables teams to collaborate on ad research, share insights, and streamline creative strategy without requiring direct account access.
image: https://brandmov.com/og-image.jpg
json_schemas:
- name: GetMetaConnectionResponse
  property_count: 9
  slug: brandmov-com-get-meta-connection-response
- name: PostApiV1MetaAdsetsRequest
  property_count: 8
  slug: brandmov-com-post-api-v1-meta-adsets-request
- name: PostApiV1MetaCampaignsRequest
  property_count: 6
  slug: brandmov-com-post-api-v1-meta-campaigns-request
- name: PostApiV1MetaCreativesRequest
  property_count: 10
  slug: brandmov-com-post-api-v1-meta-creatives-request
- name: PostMetaAdsetsRequest
  property_count: 8
  slug: brandmov-com-post-meta-adsets-request
- name: PostMetaCreativesRequest
  property_count: 9
  slug: brandmov-com-post-meta-creatives-request
jsonld:
- class_count: 54
  name: Brandmov Com Context
  property_count: 92
  slug: brandmov-com-context
layout: provider
modified: '2026-11-02'
name: BrandMov
nav: Providers
network: true
overview: 'BrandMov is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Marketing, Competitive Intelligence, Software-as-a-Service, and BrandMov.


  The BrandMov catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BrandMov''s developer surface includes changelog, authentication, documentation, engineering blog, and 18 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: BrandMov API Rules
  rule_count: 45
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 4
  slug: brandmov-com-rules
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 36.1
    developer_ergonomics: 17.9
    discoverability: 66.1
    operational_transparency: 23.7
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Brandmov Com Authentication
  slug: brandmov-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Brandmov Com Domain Security
  slug: brandmov-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Brandmov Com Vulnerability Disclosure
  slug: brandmov-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: brandmov-com
tags:
- Advertising
- Marketing
- Competitive Intelligence
- Software-as-a-Service
- BrandMov
website: https://brandmov.com/
---
