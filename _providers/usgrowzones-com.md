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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Free JSON API for USDA plant hardiness zones, temperature ranges, and frost dates by U.S. ZIP code.
  name: US Grow Zones Hardiness API
  slug: hardiness-api
- description: 'US Grow Zones API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: US Grow Zones API
  slug: usgrowzones-com-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/usgrowzones-com/rules/usgrowzones-com-rules.yml
  title: ''
  type: Spectral
  url: rules/usgrowzones-com-rules.yml
- group: design
  href: https://artifacts.apis.io/usgrowzones-com/json-ld/usgrowzones-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usgrowzones-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/usgrowzones-com/vocabulary/usgrowzones-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usgrowzones-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/usgrowzones-com/data-model/usgrowzones-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usgrowzones-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/usgrowzones-com/conformance/usgrowzones-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usgrowzones-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/usgrowzones-com/hosts/usgrowzones-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usgrowzones-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/usgrowzones-com/vendors/usgrowzones-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usgrowzones-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/usgrowzones-com/security/usgrowzones-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usgrowzones-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usgrowzones.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://usgrowzones.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://usgrowzones.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://usgrowzones.com/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://usgrowzones.com/developers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usgrowzones.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://usgrowzones.com/contact/
coverage:
  checked: '2026-10-29'
  detail: The developer portal documents the API but provides no machine‑readable OpenAPI or other spec.
  evidence:
  - status: 200
    url: https://usgrowzones.com/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: US Grow Zones provides a free, keyless JSON API that returns USDA plant hardiness zones, temperature ranges, and frost dates for any U.S. ZIP code. The service also offers a web interface to look up zones, first and last frost dates, and planting calendars for over 500 U.S. cities. No authentication is required and CORS is open, making it suitable for apps, blogs, and research.
image: https://usgrowzones.com/assets/og/developers.png
json_schemas:
- name: GetDataZw10JsonResponse
  property_count: 2
  slug: usgrowzones-com-get-data-zw10-json-response
jsonld:
- class_count: 1
  name: Usgrowzones Com Context
  property_count: 2
  slug: usgrowzones-com-context
layout: provider
modified: '2026-10-29'
name: US Grow Zones
nav: Providers
network: true
overview: 'US Grow Zones is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Weather, Plants, Geolocation, and Free.


  The US Grow Zones catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  US Grow Zones'' developer surface includes documentation, API reference, getting-started guide, support, and 11 more developer resources.'
plans:
- name: Usgrowzones Com Plans Pricing
  plan_count: 0
  slug: usgrowzones-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Usgrowzones Com Rate Limits
  slug: usgrowzones-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: US Grow Zones API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: usgrowzones-com-rules
scopes:
- name: Usgrowzones Com Scopes
  scope_count: 0
  slug: usgrowzones-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 16.4
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.5
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
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/usgrowzones-com/usgrowzones-com-2026-11-03T145544.png
security:
- kind: authentication
  name: Usgrowzones Com Authentication
  slug: usgrowzones-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Usgrowzones Com Domain Security
  slug: usgrowzones-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: usgrowzones-com
tags:
- Agriculture
- Weather
- Plants
- Geolocation
- Free
website: https://usgrowzones.com
---
