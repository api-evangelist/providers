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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The Endurain API is documented at https://docs.endurain.com and provides endpoints for activities, authentication, gear, health data, and integrations. The documentation lists reference pages but no m
  name: Endurain API
  slug: endurain-api-2
- description: 'Endurain API as documented publicly: 23 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Endurain API
  slug: endurain-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/endurain/rate-limits/endurain-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/endurain-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/endurain/rules/endurain-rules.yml
  title: ''
  type: Spectral
  url: rules/endurain-rules.yml
- group: design
  href: https://artifacts.apis.io/endurain/json-ld/endurain-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/endurain-context.jsonld
- group: design
  href: https://artifacts.apis.io/endurain/vocabulary/endurain-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/endurain-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/endurain/data-model/endurain-data-model.yml
  title: ''
  type: DataModel
  url: data-model/endurain-data-model.yml
- group: auth
  href: https://artifacts.apis.io/endurain/authentication/endurain-authentication.yml
  title: ''
  type: Authentication
  url: authentication/endurain-authentication.yml
- group: design
  href: https://artifacts.apis.io/endurain/conformance/endurain-conformance.yml
  title: ''
  type: Conformance
  url: conformance/endurain-conformance.yml
- group: other
  href: https://artifacts.apis.io/endurain/hosts/endurain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/endurain-hosts.yml
- group: other
  href: https://artifacts.apis.io/endurain/vendors/endurain-vendors.yml
  title: ''
  type: Vendors
  url: vendors/endurain-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ThreeCO
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/endurain-project/endurain/releases
- group: docs
  title: ''
  type: APIReference
  url: https://docs.endurain.com/reference/gears/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.endurain.com/getting-started/quick-start/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.endurain.com/
- group: auth
  href: https://artifacts.apis.io/endurain/security/endurain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/endurain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://endurain.com
coverage:
  checked: '2026-10-28'
  detail: Documentation at https://docs.endurain.com lists reference pages but no OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL files were found.
  evidence:
  - status: 404
    url: https://docs.endurain.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Endurain provides a self‑hosted, privacy‑first fitness tracking platform that lets users store and analyze their activity, gear, and health data on their own infrastructure. The service offers a web dashboard, mobile apps, and integrations with Strava and Garmin, all under an AGPL‑3.0 license. Endurain emphasizes data ownership, no lock‑in, and community‑driven development, with documentation, a live demo, and open‑source code available.
image: https://endurain.com/assets/img/screenshots/screenshot_home.jpg
json_schemas:
- name: GetProfileApiKeysResponse
  property_count: 9
  slug: endurain-get-profile-api-keys-response
- name: PostApiV1AuthMfaVerifyResponse
  property_count: 7
  slug: endurain-post-api-v1-auth-mfa-verify-response
- name: PostApiV1ProfileApiKeysRequest
  property_count: 5
  slug: endurain-post-api-v1-profile-api-keys-request
- name: PostApiV1ProfileApiKeysResponse
  property_count: 10
  slug: endurain-post-api-v1-profile-api-keys-response
- name: PostApiV1PublicIdpSessionSessionidTokensResponse
  property_count: 6
  slug: endurain-post-api-v1-public-idp-session-sessionid-tokens-response
- name: PostProfileIdpIdpidLinkTokenRequest
  property_count: 2
  slug: endurain-post-profile-idp-idpid-link-token-request
jsonld:
- class_count: 22
  name: Endurain Context
  property_count: 26
  slug: endurain-context
layout: provider
modified: '2026-10-28'
name: Endurain
nav: Providers
network: true
overview: 'Endurain is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fitness, Self-Hosted, Open Source, and Privacy.


  The Endurain catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Endurain''s developer surface includes authentication, changelog, API reference, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 5
  name: Endurain Rate Limits
  slug: endurain-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Endurain API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: endurain-rules
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 42.1
  previous_composite: 29.0
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
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/endurain/endurain-2026-11-03T131513.png
security:
- kind: authentication
  name: Endurain Authentication
  slug: endurain-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Endurain Domain Security
  slug: endurain-domain-security
  summary_line: TLSv1.3 · DMARC
slug: endurain
tags:
- Company
- Fitness
- Self-Hosted
- Open Source
- Privacy
website: https://endurain.com
---
