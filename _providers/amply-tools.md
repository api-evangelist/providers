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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The Amply SDK reaches the backend over a small, signed HTTPS API. Your app never calls these endpoints itself — the SDK handles the request shape, authentication and retries.
  name: Amply API
  slug: amply-api
- baseURL: https://api.amply.tools
  baseurl_source: declared
  description: 'Amply API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Amply API
  slug: amply-tools-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/amply-tools/rules/amply-tools-rules.yml
  title: ''
  type: Spectral
  url: rules/amply-tools-rules.yml
- group: design
  href: https://artifacts.apis.io/amply-tools/json-ld/amply-tools-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amply-tools-context.jsonld
- group: design
  href: https://artifacts.apis.io/amply-tools/vocabulary/amply-tools-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amply-tools-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/amply-tools/data-model/amply-tools-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amply-tools-data-model.yml
- group: operate
  href: https://artifacts.apis.io/amply-tools/changelog/amply-tools-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/amply-tools-changelog.yml
- group: design
  href: https://artifacts.apis.io/amply-tools/conformance/amply-tools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amply-tools-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amply-tools/llms/amply-tools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amply-tools-llms.txt
- group: agent
  href: https://artifacts.apis.io/amply-tools/well-known/amply-tools-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amply-tools-well-known.yml
- group: other
  href: https://artifacts.apis.io/amply-tools/hosts/amply-tools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amply-tools-hosts.yml
- group: other
  href: https://artifacts.apis.io/amply-tools/vendors/amply-tools-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amply-tools-vendors.yml
- group: build
  href: https://artifacts.apis.io/amply-tools/packages/amply-tools-packages.yml
  title: ''
  type: SDKs
  url: packages/amply-tools-packages.yml
- group: build
  href: https://artifacts.apis.io/amply-tools/packages/amply-tools-packages.yml
  title: ''
  type: Packages
  url: packages/amply-tools-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.amply.tools/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.amply.tools/reference/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.amply.tools/getting-started/what-is-amply
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.amply.tools`
- group: auth
  href: https://artifacts.apis.io/amply-tools/security/amply-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amply-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amply.tools/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amply.tools
- group: company
  title: ''
  type: Blog
  url: https://amply.tools/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://amply.tools/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amply.tools/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amply.tools/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amply-tools
coverage:
  checked: '2026-11-01'
  detail: Docs provide an API reference but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 404
    url: https://api.amply.tools/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Amply provides in-app personalization for mobile apps, allowing each user segment its own paywall, offer, or tip based on behavior. Install the SDK once and no further app releases are needed. Supports iOS, Android, React Native, and Kotlin Multiplatform. The platform lets teams define audiences, triggers, and surfaces via a visual builder, delivering personalized experiences instantly. It integrates with existing analytics tools and offers a free plan with paid tiers up to $299.
image: https://amply.tools/assets/og_image.jpg
json_schemas:
- name: GetV6ApikeyCodesResponse
  property_count: 4
  slug: amply-tools-get-v6-apikey-codes-response
- name: GetV6ApikeyQuotaResponse
  property_count: 7
  slug: amply-tools-get-v6-apikey-quota-response
- name: PostApiV1AttributionRequest
  property_count: 3
  slug: amply-tools-post-api-v1-attribution-request
- name: PostApiV1SessionRequest
  property_count: 3
  slug: amply-tools-post-api-v1-session-request
- name: PostApiV1TmAppleRequest
  property_count: 2
  slug: amply-tools-post-api-v1-tm-apple-request
jsonld:
- class_count: 5
  name: Amply Tools Context
  property_count: 14
  slug: amply-tools-context
layout: provider
modified: '2026-11-01'
name: Amply
nav: Providers
network: true
overview: 'Amply is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Personalization, Mobile, SDK, In-App, and Analytics.


  The Amply catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amply''s developer surface includes changelog, API reference, getting-started guide, documentation, engineering blog, pricing, and 18 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Amply API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: amply-tools-rules
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 15.8
    contract_governance: 19.7
    contract_quality: 26.0
    developer_ergonomics: 27.4
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 35.5
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Amply Tools Authentication
  slug: amply-tools-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Amply Tools Domain Security
  slug: amply-tools-domain-security
  summary_line: TLSv1.3 · DMARC
slug: amply-tools
tags:
- Personalization
- Mobile
- SDK
- In-App
- Analytics
website: https://amply.tools/
---
