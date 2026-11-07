---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Life360 Agentic Access
  operation_count: 4
  slug: life360-agentic-access
  summary_line: 4 operations
api_count: 2
apis:
- baseURL: https://www.life360.com
  baseurl_source: declared
  description: Life360's public, unauthenticated product-catalog API ("Life360 WEB API" v0.1), advertised by the agent-facing manifest at https://www.life360.com/.well-known/ai-plugin.json — 4 GET operations under /
  name: Life360 Product API
  slug: life360-product-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/life360/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/life360/agentic-access/life360-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/life360-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/life360/plans/life360-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/life360-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/life360/rules/life360-rules.yml
  title: ''
  type: Spectral
  url: rules/life360-rules.yml
- group: design
  href: https://artifacts.apis.io/life360/json-ld/life360-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/life360-context.jsonld
- group: design
  href: https://artifacts.apis.io/life360/vocabulary/life360-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/life360-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/life360/data-model/life360-data-model.yml
  title: ''
  type: DataModel
  url: data-model/life360-data-model.yml
- group: design
  href: https://artifacts.apis.io/life360/conventions/life360-conventions.yml
  title: ''
  type: Conventions
  url: conventions/life360-conventions.yml
- group: design
  href: https://artifacts.apis.io/life360/errors/life360-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/life360-problem-types.yml
- group: other
  href: https://artifacts.apis.io/life360/overlays/life360-catalog-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/life360-catalog-overlay.yaml
- group: other
  href: https://artifacts.apis.io/life360/hosts/life360-hosts.yml
  title: ''
  type: Hosts
  url: hosts/life360-hosts.yml
- group: other
  href: https://artifacts.apis.io/life360/vendors/life360-vendors.yml
  title: ''
  type: Vendors
  url: vendors/life360-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://www.life360.com/
- group: agent
  href: https://artifacts.apis.io/life360/well-known/life360-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/life360-well-known.yml
- group: auth
  href: https://artifacts.apis.io/life360/well-known/life360-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/life360-security.txt
- group: other
  href: https://artifacts.apis.io/life360/well-known/life360-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/life360-robots.txt
- group: agent
  href: https://artifacts.apis.io/life360/llms/life360-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/life360-llms.txt
- group: auth
  href: https://artifacts.apis.io/life360/security/life360-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/life360-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/life360/security/life360-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/life360-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.life360.com/security
- group: design
  href: https://artifacts.apis.io/life360/conformance/life360-conformance.yml
  title: ''
  type: Conformance
  url: conformance/life360-conformance.yml
- group: design
  href: https://artifacts.apis.io/life360/lifecycle/life360-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/life360-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.life360.com/
- group: operate
  title: ''
  type: Support
  url: https://support.life360.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.life360.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.life360.com/plans-pricing
- group: start
  title: ''
  type: Login
  url: https://app.life360.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.life360.com/sign-up?web_loc=plans&period=month&plan=free
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.corp.life360.com/hc/en-us/articles/16124856472471-Life360-Terms-of-Service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.corp.life360.com/hc/en-us/articles/16038777217175-Life360-Privacy-Policy
- group: company
  title: ''
  type: Press
  url: https://www.life360.com/press
- group: other
  title: ''
  type: Leadership
  url: https://www.life360.com/leadership
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/life360
created: '2026-07-17'
description: Life360 is a family safety platform built around a location-sharing mobile app for iOS and Android, offering real-time member location, Place Alerts, location history, driving safety scores and trip history, crash detection, SOS alerts and emergency dispatch, plus digital safety features such as identity theft protection and dark web monitoring. Its hardware line, following the acquisitions of Tile and Jiobit, spans Tile Mate, Pro, Slim and Sticker Bluetooth item trackers and a cellular GPS pet tracker, sold direct and through Amazon, Best Buy, Target and Walmart. The service is sold as Free, Silver, Gold and Platinum membership tiers. Life360 publishes no developer portal, no SDKs and no partner/location API — its only machine-readable surface is an agent-facing one (llms.txt, an ai-plugin manifest whose advertised OpenAPI (a 4-operation product-catalog spec at www.life360.com/openapi-spec.json) resolves, and Content-Signal directives in robots.txt). This profile is maintained
  in the API Evangelist network for company discovery and monitoring.
image: https://www.life360.com/svgs/life360-logo-dark.svg
json_schemas:
- name: Product
  property_count: 19
  slug: life360-product
jsonld:
- class_count: 11
  name: Life360 Context
  property_count: 54
  slug: life360-context
layout: provider
modified: '2026-10-20'
name: Life360
nav: Providers
network: true
overview: 'Life360 publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Product API. Tagged areas include Company, Consumer, Family Safety, Location, and GPS Tracking.


  The Life360 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Life360''s developer surface includes support, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Life360 Plans Pricing
  plan_count: 4
  slug: life360-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Life360 Rate Limits
  slug: life360-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Life360 API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: life360-rules
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 70.4
    catalog_earned_first_party: 12.0
    catalog_gap: 44.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 69.7
    contract_governance: 33.3
    contract_quality: 51.6
    developer_ergonomics: 8.9
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/life360/life360-2026-07-25T225034.png
security:
- kind: authentication
  name: Life360 Authentication
  slug: life360-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Life360 Domain Security
  slug: life360-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Life360 Vulnerability Disclosure
  slug: life360-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 2
skills:
- name: life360-explore-product-variants
  slug: life360-explore-product-variants
- name: life360-find-and-check-a-product
  slug: life360-find-and-check-a-product
slug: life360
tags:
- Company
- Consumer
- Family Safety
- Location
- GPS Tracking
- Bluetooth Trackers
- Mobile App
- Driving Safety
- Wearables
- Subscription
website: https://www.life360.com/
---
