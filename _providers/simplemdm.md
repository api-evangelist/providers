---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
api_count: 2
apis:
- description: See how simple Apple device management can be. Setting up a SimpleMDM account is easy and only takes a few minutes. Get started today.
  name: SimpleMDM API
  slug: simplemdm-api-2
- baseURL: https://a.simplemdm.com
  baseurl_source: declared
  description: 'SimpleMDM API as documented publicly: 71 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: SimpleMDM API
  slug: simplemdm-api
artifact_total: 12
common:
- group: auth
  href: https://artifacts.apis.io/simplemdm/well-known/simplemdm-pdq-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/simplemdm-pdq-security.txt
- group: commercial
  href: https://artifacts.apis.io/simplemdm/plans/simplemdm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/simplemdm-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/simplemdm/rules/simplemdm-rules.yml
  title: ''
  type: Spectral
  url: rules/simplemdm-rules.yml
- group: design
  href: https://artifacts.apis.io/simplemdm/json-ld/simplemdm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/simplemdm-context.jsonld
- group: design
  href: https://artifacts.apis.io/simplemdm/vocabulary/simplemdm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/simplemdm-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/simplemdm/data-model/simplemdm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/simplemdm-data-model.yml
- group: design
  href: https://artifacts.apis.io/simplemdm/conformance/simplemdm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/simplemdm-conformance.yml
- group: agent
  href: https://artifacts.apis.io/simplemdm/well-known/simplemdm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/simplemdm-well-known.yml
- group: other
  href: https://artifacts.apis.io/simplemdm/hosts/simplemdm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/simplemdm-hosts.yml
- group: other
  href: https://artifacts.apis.io/simplemdm/vendors/simplemdm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/simplemdm-vendors.yml
- group: build
  href: https://artifacts.apis.io/simplemdm/packages/simplemdm-packages.yml
  title: ''
  type: SDKs
  url: packages/simplemdm-packages.yml
- group: build
  href: https://artifacts.apis.io/simplemdm/packages/simplemdm-packages.yml
  title: ''
  type: Packages
  url: packages/simplemdm-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simplemdm.com/terms-conditions/
- group: operate
  title: ''
  type: StatusPage
  url: https://pdq.statuspage.io/
- group: auth
  title: ''
  type: Security
  url: https://simplemdm.com/blog/categories/security/1/
- group: start
  title: ''
  type: GettingStarted
  url: https://simplemdm.com/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SimpleMDM
- group: auth
  href: https://artifacts.apis.io/simplemdm/security/simplemdm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simplemdm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simplemdm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.simplemdm.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://simplemdm.com/pricing/
- group: operate
  title: ''
  type: Roadmap
  url: https://simplemdm.com/roadmap/
- group: company
  title: ''
  type: Blog
  url: https://simplemdm.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://simplemdm.pdq.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simplemdm.com/privacy/
coverage:
  checked: '2026-10-28'
  detail: Docs site redirects to a help center and provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://docs.simplemdm.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: SimpleMDM provides an intuitive and powerful Apple Mobile Device Management (MDM) solution for businesses, offering easy-to-use enrollment, configuration profiles, device actions, and advanced enterprise features. The platform enables seamless management of Apple fleets, supporting both macOS and iOS devices with robust security, compliance, and automation capabilities.
image: https://images.ctfassets.net/wijwqldy5f7q/6wTF9wXH0AGM8zA6Jov9vc/47227c73384989bd81462c302a9d0df4/SimpleMDM_logo.svg
json_schemas:
- name: PatchApiV1CustomConfigurationProfilesProfileidRequest
  property_count: 12
  slug: simplemdm-patch-api-v1-custom-configuration-profiles-profileid-request
- name: PatchApiV1CustomDeclarationsProfileidRequest
  property_count: 7
  slug: simplemdm-patch-api-v1-custom-declarations-profileid-request
- name: PostApiV1AppsRequest
  property_count: 4
  slug: simplemdm-post-api-v1-apps-request
- name: PostApiV1AppsResponse
  property_count: 6
  slug: simplemdm-post-api-v1-apps-response
- name: PostApiV1CustomConfigurationProfilesRequest
  property_count: 12
  slug: simplemdm-post-api-v1-custom-configuration-profiles-request
- name: PostApiV1CustomDeclarationsRequest
  property_count: 7
  slug: simplemdm-post-api-v1-custom-declarations-request
jsonld:
- class_count: 37
  name: Simplemdm Context
  property_count: 36
  slug: simplemdm-context
layout: provider
modified: '2026-10-28'
name: SimpleMDM
nav: Providers
network: true
overview: 'SimpleMDM is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Mobile Device Management, Apple, MDM, Enterprise, and Software-as-a-Service.


  The SimpleMDM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SimpleMDM''s developer surface includes getting-started guide, documentation, pricing, engineering blog, support, and 20 more developer resources.'
plans:
- name: Simplemdm Plans Pricing
  plan_count: 3
  slug: simplemdm-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: SimpleMDM API Rules
  rule_count: 38
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 3
  slug: simplemdm-rules
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 30.7
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 41.3
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/simplemdm/simplemdm-2026-11-03T143220.png
security:
- kind: domain-security
  name: Simplemdm Domain Security
  slug: simplemdm-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: simplemdm
tags:
- Mobile Device Management
- Apple
- MDM
- Enterprise
- Software-as-a-Service
- Company
website: https://simplemdm.com/
---
