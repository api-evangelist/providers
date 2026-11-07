---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://stg-id.uaepass.ae
  baseurl_source: declared
  description: 'UAE PASS API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: UAE PASS API
  slug: uae-pass-api
artifact_total: 10
common:
- group: other
  href: https://artifacts.apis.io/uae-pass/vendors/uae-pass-vendors.yml
  title: ''
  type: Vendors
  url: vendors/uae-pass-vendors.yml
- group: design
  href: https://artifacts.apis.io/uae-pass/rules/uae-pass-rules.yml
  title: ''
  type: Spectral
  url: rules/uae-pass-rules.yml
- group: design
  href: https://artifacts.apis.io/uae-pass/json-ld/uae-pass-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/uae-pass-context.jsonld
- group: design
  href: https://artifacts.apis.io/uae-pass/vocabulary/uae-pass-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/uae-pass-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/uae-pass/data-model/uae-pass-data-model.yml
  title: ''
  type: DataModel
  url: data-model/uae-pass-data-model.yml
- group: operate
  href: https://artifacts.apis.io/uae-pass/changelog/uae-pass-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/uae-pass-changelog.yml
- group: design
  href: https://artifacts.apis.io/uae-pass/conformance/uae-pass-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uae-pass-conformance.yml
- group: agent
  href: https://artifacts.apis.io/uae-pass/llms/uae-pass-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uae-pass-llms.txt
- group: agent
  href: https://artifacts.apis.io/uae-pass/well-known/uae-pass-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/uae-pass-well-known.yml
- group: other
  href: https://artifacts.apis.io/uae-pass/hosts/uae-pass-hosts.yml
  title: ''
  type: Hosts
  url: hosts/uae-pass-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.uaepass.ae/getting-onboarded-with-uae-pass/onboarding-process-for-uae-pass-service-providers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.uaepass.ae/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UAEPASS
- group: auth
  href: https://artifacts.apis.io/uae-pass/security/uae-pass-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uae-pass-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uaepass.ae/
coverage:
  checked: '2026-10-26'
  detail: The UAE PASS developer portal at https://uaepass.ae/developer loads via a Nuxt.js SPA and provides no downloadable OpenAPI, GraphQL, or other spec files.
  evidence:
  - status: 200
    url: https://uaepass.ae/developer
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: UAE PASS is the United Arab Emirates’ national digital identity platform that enables citizens, residents and businesses to securely access government and private sector services online. It provides a unified authentication and electronic signature solution, supporting mobile apps, web portals and APIs for identity verification, consent management, and transaction signing across a wide range of public and private services.
json_schemas:
- name: GetIdshubUserinfoResponse
  property_count: 9
  slug: uae-pass-get-idshub-userinfo-response
- name: PostApiV1ConsentTransactionCallbackRequest
  property_count: 3
  slug: uae-pass-post-api-v1-consent-transaction-callback-request
- name: PostApiV1ConsentTransactionSendRequest
  property_count: 23
  slug: uae-pass-post-api-v1-consent-transaction-send-request
- name: PostApiV1ConsentTransactionSendResponse
  property_count: 3
  slug: uae-pass-post-api-v1-consent-transaction-send-response
- name: PostIdshubIntrospectResponse
  property_count: 11
  slug: uae-pass-post-idshub-introspect-response
- name: PostIdshubTokenResponse
  property_count: 4
  slug: uae-pass-post-idshub-token-response
jsonld:
- class_count: 6
  name: Uae Pass Context
  property_count: 48
  slug: uae-pass-context
layout: provider
modified: '2026-10-26'
name: UAE PASS
nav: Providers
network: true
overview: 'UAE PASS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Authentication, United Arab Emirates, and Digital.


  The UAE PASS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  UAE PASS''s developer surface includes changelog, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: UAE PASS API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: uae-pass-rules
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 10.7
    discoverability: 69.6
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-arab-emirates
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.8
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
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/uae-pass/uae-pass-2026-11-03T145341.png
security:
- kind: domain-security
  name: Uae Pass Domain Security
  slug: uae-pass-domain-security
  summary_line: TLSv1.2 · DMARC
slug: uae-pass
tags:
- Company
- Identity
- Authentication
- United Arab Emirates
- Digital
website: https://uaepass.ae/
---
