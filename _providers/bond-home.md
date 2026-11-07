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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Bond (fan / shade bridge) API as documented publicly: 23 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Bond (fan / shade bridge) API
  slug: bond-home-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/bond-home/rules/bond-home-rules.yml
  title: ''
  type: Spectral
  url: rules/bond-home-rules.yml
- group: design
  href: https://artifacts.apis.io/bond-home/json-ld/bond-home-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bond-home-context.jsonld
- group: design
  href: https://artifacts.apis.io/bond-home/vocabulary/bond-home-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bond-home-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bond-home/data-model/bond-home-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bond-home-data-model.yml
- group: design
  href: https://artifacts.apis.io/bond-home/conformance/bond-home-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bond-home-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bond-home/llms/bond-home-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bond-home-llms.txt
- group: other
  href: https://artifacts.apis.io/bond-home/hosts/bond-home-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bond-home-hosts.yml
- group: other
  href: https://artifacts.apis.io/bond-home/vendors/bond-home-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bond-home-vendors.yml
- group: build
  href: https://artifacts.apis.io/bond-home/packages/bond-home-packages.yml
  title: ''
  type: SDKs
  url: packages/bond-home-packages.yml
- group: build
  href: https://artifacts.apis.io/bond-home/packages/bond-home-packages.yml
  title: ''
  type: Packages
  url: packages/bond-home-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://bondhome.io/register/
- group: operate
  title: ''
  type: ChangeLog
  url: https://bondhome.io/whats-new/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.zendesk.com/documentation/developer-tools/getting-started/getting-a-trial-or-sponsored-account-for-development/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bondhome
- group: auth
  href: https://artifacts.apis.io/bond-home/security/bond-home-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bond-home-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bondhome.io/
- group: docs
  title: ''
  type: Documentation
  url: https://olibra.zendesk.com/hc/en-us/articles/360055398992--APP-Setting-up-your-device-with-the-Bond-Home-application
- group: operate
  title: ''
  type: Support
  url: https://olibra.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Newsroom
  url: https://bondhome.io/newsroom/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bondhome.io/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bondhome.io/terms-and-conditions/
coverage:
  checked: '2026-10-28'
  detail: Documentation is provided via Zendesk articles without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://olibra.zendesk.com/hc/en-us/articles/360055398992--APP-Setting-up-your-device-with-the-Bond-Home-application
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Bond, powered by Olibra, creates smart‑home solutions that connect often‑overlooked appliances such as ceiling fans, fireplaces, and window shades. Their platform lets users control these devices via voice assistants, mobile apps, and automation routines, aiming to make home environments more meaningful, durable, and energy‑efficient. The company focuses on intuitive design, reliable hardware integration, and expanding the ecosystem of connected home products.
image: https://bondhome.io/wp-content/uploads/2020/04/bond-fb.png
json_schemas:
- name: GetApiSunshineObjectsRecordsResourceidRelationshipsRelations
  property_count: 7
  slug: bond-home-get-api-sunshine-objects-records-resourceid-relationships-relations
- name: GetApiV2UserProfilesResponse
  property_count: 1
  slug: bond-home-get-api-v2-user-profiles-response
- name: PostApiSunshineObjectsRecordsRequest
  property_count: 6
  slug: bond-home-post-api-sunshine-objects-records-request
- name: PostApiSunshineObjectsTypesRequest
  property_count: 11
  slug: bond-home-post-api-sunshine-objects-types-request
- name: PostApiV2UserProfilesEventsRequest
  property_count: 12
  slug: bond-home-post-api-v2-user-profiles-events-request
- name: PostApiV2UsersUseridEventsRequest
  property_count: 11
  slug: bond-home-post-api-v2-users-userid-events-request
jsonld:
- class_count: 28
  name: Bond Home Context
  property_count: 45
  slug: bond-home-context
layout: provider
modified: '2026-10-28'
name: Bond (fan / shade bridge)
nav: Providers
network: true
overview: 'Bond (fan / shade bridge) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Home, IoT, Home Automation, and Connectivity.


  The Bond (fan / shade bridge) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bond (fan / shade bridge)''s developer surface includes signup flow, changelog, getting-started guide, documentation, support, and 16 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Bond (fan / shade bridge) API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: bond-home-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 25.2
    developer_ergonomics: 20.2
    discoverability: 65.2
    operational_transparency: 10.5
  previous_composite: 33.2
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bond-home/bond-home-2026-11-03T122200.png
security:
- kind: domain-security
  name: Bond Home Domain Security
  slug: bond-home-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bond-home
tags:
- Company
- Smart Home
- IoT
- Home Automation
- Connectivity
website: https://bondhome.io/
---
