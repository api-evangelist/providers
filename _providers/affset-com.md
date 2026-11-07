---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Affset provides an affiliate tracking platform with public documentation at https://affset.com/docs.
  name: Affset API
  slug: affset-api
- baseURL: https://api.affset.com
  baseurl_source: declared
  description: 'Affset API as documented publicly: 76 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: Affset API
  slug: affset-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/affset-com/plans/affset-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/affset-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/affset-com/rules/affset-com-rules.yml
  title: ''
  type: Spectral
  url: rules/affset-com-rules.yml
- group: design
  href: https://artifacts.apis.io/affset-com/json-ld/affset-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/affset-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/affset-com/vocabulary/affset-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/affset-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/affset-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/affset-com/data-model/affset-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/affset-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/affset-com/conformance/affset-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/affset-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/affset-com/llms/affset-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/affset-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/affset-com/well-known/affset-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/affset-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/affset-com/hosts/affset-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/affset-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/affset-com/vendors/affset-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/affset-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.affset.com/login
- group: auth
  href: https://artifacts.apis.io/affset-com/security/affset-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/affset-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://affset.com/
- group: docs
  title: ''
  type: Documentation
  url: https://affset.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://affset.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://affset.com/demo
- group: commercial
  title: ''
  type: Pricing
  url: https://affset.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://affset.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://affset.com/privacy
coverage:
  checked: '2026-10-31'
  detail: OpenAPI file at https://affset.com/openapi.json is for a different product (Affitor) and does not describe Affset's API.
  evidence:
  - status: 200
    url: https://affset.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Affset provides an affiliate tracking platform with a built‑in MCP server, enabling media buyers, affiliate teams, and CPA networks to monitor clicks, conversions, and postbacks in real time. The service offers a free forever plan, white‑label options, and integrations with AI assistants like Claude and Cursor. It includes detailed documentation, pricing, demo, and support resources, positioning itself as a comprehensive solution for performance marketing and affiliate management.
image: https://affset.com/og-image.png
json_schemas:
- name: GetApiPayoutRequestsPayoutrequestidResponse
  property_count: 11
  slug: affset-com-get-api-payout-requests-payoutrequestid-response
- name: GetApiTrafficSourcesB3E1E6B02F2A4A3E9C8E1C9A2F6D4B22BlocksPu
  property_count: 8
  slug: affset-com-get-api-traffic-sources-b3-e1-e6-b02-f2-a4-a3-e9-c8-e1-c9-a2-f6-d4-b22-blocks-pu
- name: PostApiOffersRequest
  property_count: 16
  slug: affset-com-post-api-offers-request
- name: PostApiTrafficSourcesRequest
  property_count: 6
  slug: affset-com-post-api-traffic-sources-request
- name: PutApiOffersOfferidRequest
  property_count: 16
  slug: affset-com-put-api-offers-offerid-request
- name: PutApiTrafficSourcesTrafficsourceidRequest
  property_count: 6
  slug: affset-com-put-api-traffic-sources-trafficsourceid-request
jsonld:
- class_count: 91
  name: Affset Com Context
  property_count: 129
  slug: affset-com-context
layout: provider
modified: '2026-10-31'
name: Affset
nav: Providers
network: true
overview: 'Affset is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Affiliate Tracking, Media Buying, CPA Networks, Postback, and White Label.


  The Affset catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Affset''s developer surface includes documentation, API reference, getting-started guide, pricing, and 16 more developer resources.'
plans:
- name: Affset Com Plans Pricing
  plan_count: 5
  slug: affset-com-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Affset API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: affset-com-rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 20.7
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 38.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
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
- kind: domain-security
  name: Affset Com Domain Security
  slug: affset-com-domain-security
  summary_line: TLSv1.3
slug: affset-com
tags:
- Affiliate Tracking
- Media Buying
- CPA Networks
- Postback
- White Label
- Pricing
website: https://affset.com/
---
