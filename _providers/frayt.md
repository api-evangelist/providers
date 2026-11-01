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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 7
  name: Frayt Agentic Access
  operation_count: 8
  slug: frayt-agentic-access
  summary_line: 8 operations · 7 acting · 7 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.frayt.com/api/v2.2/
  baseurl_source: declared
  description: The match estimates API from FRAYT — 2 operation(s) for match estimates.
  name: FRAYT match estimates API
  slug: frayt-match-estimates-api
- baseURL: https://api.frayt.com/api/v2.2/
  baseurl_source: declared
  description: The matches API from FRAYT — 3 operation(s) for matches.
  name: FRAYT Matches API
  slug: frayt-matches-api
- baseURL: https://api.frayt.com/api/v2.2/
  baseurl_source: declared
  description: The oauth API from FRAYT — 1 operation(s) for oauth.
  name: FRAYT OAUTH API
  slug: frayt-oauth-api
artifact_total: 24
asyncapis:
- description: ''
  name: Frayt Match Webhooks
  slug: frayt-match-webhooks
common:
- group: other
  href: https://artifacts.apis.io/frayt/capabilities/frayt-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/frayt-capability-edges.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.frayt.com/
- group: design
  href: https://artifacts.apis.io/frayt/rules/frayt-rules.yml
  title: ''
  type: Spectral
  url: rules/frayt-rules.yml
- group: design
  href: https://artifacts.apis.io/frayt/json-ld/frayt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/frayt-context.jsonld
- group: design
  href: https://artifacts.apis.io/frayt/vocabulary/frayt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/frayt-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/frayt/well-known/frayt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/frayt-well-known.yml
- group: other
  href: https://artifacts.apis.io/frayt/hosts/frayt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/frayt-hosts.yml
- group: build
  href: https://artifacts.apis.io/frayt/integrations/frayt-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/frayt-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/frayt/vendors/frayt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/frayt-vendors.yml
- group: build
  href: https://artifacts.apis.io/frayt/packages/frayt-packages.yml
  title: ''
  type: SDKs
  url: packages/frayt-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.frayt.com/resources/news
- group: other
  title: ''
  type: Leadership
  url: https://www.frayt.com/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.frayt.com
- group: other
  href: https://artifacts.apis.io/frayt/overlays/frayt-matches-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/frayt-matches-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/frayt/agentic-access/frayt-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/frayt-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/frayt/security/frayt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/frayt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.frayt.com/
- group: company
  title: ''
  type: Blog
  url: https://www.frayt.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.frayt.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.frayt.com/platform/faqs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Frayt-Technologies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.frayt.com/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.frayt.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.frayt.app/
- group: agent
  href: https://artifacts.apis.io/frayt/llms/frayt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/frayt-llms.txt
- group: build
  href: https://artifacts.apis.io/frayt/packages/frayt-packages.yml
  title: ''
  type: Packages
  url: packages/frayt-packages.yml
- group: design
  href: https://artifacts.apis.io/frayt/lifecycle/frayt-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/frayt-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/frayt/conformance/frayt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/frayt-conformance.yml
- group: agent
  href: https://artifacts.apis.io/frayt/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/frayt/plans/frayt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/frayt-plans-pricing.yml
created: '2026-08-16'
description: FRAYT (Frayt Technologies, Inc., Cincinnati, Ohio) operates an on-demand and scheduled middle-mile and last-mile delivery marketplace that connects shippers to a vetted nationwide network of owner-operator drivers running everything from cars and midsize vehicles to pickups, cargo vans and box trucks. The FRAYT Client API is a versioned REST API (v2.2) over JSON, secured with OAuth 2.0 client-credentials bearer tokens, that lets a TMS, ERP or storefront price a delivery as an "estimate", authorize it into a "match", track it through the driver lifecycle, tip a driver and cancel it — with webhook callbacks defined in the OpenAPI itself for real-time match and driver-location updates. A full sandbox environment mirrors production.
finops:
- has_sources: true
  method: derived
  name: Frayt Finops
  primary_unit: ''
  service_category: ''
  slug: frayt-finops
  template: true
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
json_schemas:
- name: CancelMatchRequest
  property_count: 1
  slug: frayt-cancel-match-request
- name: MatchRequest
  property_count: 26
  slug: frayt-match-request
- name: MatchResponse
  property_count: 1
  slug: frayt-match-response
- name: MatchStopResponse
  property_count: 37
  slug: frayt-match-stop-response
- name: Oauth Request
  property_count: 3
  slug: frayt-oauth-request
- name: Oauth Response
  property_count: 1
  slug: frayt-oauth-response
- name: RestrictedUpdateMatchRequest
  property_count: 22
  slug: frayt-restricted-update-match-request
- name: UpdateDriverTip
  property_count: 1
  slug: frayt-update-driver-tip
- name: UpdateEstimateRequest
  property_count: 26
  slug: frayt-update-estimate-request
jsonld:
- class_count: 33
  name: Frayt Context
  property_count: 144
  slug: frayt-context
layout: provider
modified: '2026-08-16'
name: FRAYT
nav: Providers
network: true
overview: 'FRAYT publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: match estimates API, Matches API, and OAUTH API. Tagged areas include Company, Last Mile Delivery, Logistics, Couriers, and On-Demand Delivery.


  The FRAYT catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  FRAYT''s developer surface includes documentation, engineering blog, support, signup flow, and 26 more developer resources.'
plans:
- name: Frayt Plans Pricing
  plan_count: 0
  slug: frayt-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Frayt Rate Limits
  slug: frayt-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: FRAYT API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: frayt-rules
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 68.2
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 13.2
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/frayt/frayt-2026-09-02T145540.png
security:
- kind: authentication
  name: Frayt Authentication
  slug: frayt-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Frayt Domain Security
  slug: frayt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: frayt-amend-or-cancel-delivery
  slug: frayt-amend-or-cancel-delivery
- name: frayt-quote-and-book-delivery
  slug: frayt-quote-and-book-delivery
- name: frayt-track-delivery-lifecycle
  slug: frayt-track-delivery-lifecycle
slug: frayt
tags:
- Company
- Last Mile Delivery
- Logistics
- Couriers
- On-Demand Delivery
- Shipping
- Freight
- Supply Chain
- Transportation
- Third Party Logistics
- Delivery Tracking
- Webhook
website: https://www.frayt.com/
---
