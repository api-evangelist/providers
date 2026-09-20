---
access_model:
  confidence: high
  label: Enterprise · Contact sales for credentials
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - https://api.basis.net/swagger.json
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.3
  scored_at: '2026-09-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Basis Agentic Access
  operation_count: 31
  slug: basis-agentic-access
  summary_line: 31 operations
api_count: 1
apis:
- baseURL: https://api.basis.net
  baseurl_source: declared
  description: The Analytics API from Basis — 31 operation(s) for analytics.
  name: Basis Analytics API
  slug: basis-analytics-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Basis Platform Analytics API
  slug: open-basis-analytics-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/agentic-access/basis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/basis-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/security/basis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/basis-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/authentication/basis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/basis-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://basis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://basis.com/technology/enterprise-api
- group: company
  title: ''
  type: Blog
  url: https://basis.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://basis.com/technology/enterprise-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/basis-technologies
- group: other
  title: ''
  type: X
  url: https://twitter.com/basisglobaltech
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/plans/basis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/basis-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/rate-limits/basis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/basis-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/finops/basis-finops.yml
  title: ''
  type: FinOps
  url: finops/basis-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/scopes/basis-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/basis-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/conventions/basis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/basis-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/errors/basis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/basis-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/lifecycle/basis-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/basis-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/conformance/basis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/basis-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/conformance/basis-conformance.yml
  title: ''
  type: Compliance
  url: conformance/basis-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/data-model/basis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/basis-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/sandbox/basis-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/basis-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/well-known/basis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/basis-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/mcp/basis-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/basis-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/llms/basis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/basis-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/packages/basis-packages.yml
  title: ''
  type: Packages
  url: packages/basis-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/vocabulary/basis-vocabulary.json
  title: ''
  type: Vocabulary
  url: vocabulary/basis-vocabulary.json
- group: start
  title: ''
  type: SignUp
  url: https://platform.basis.net/auth/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.basis.com/
- group: operate
  title: ''
  type: Support
  url: https://basis.com/connect
created: '2026-06-13'
description: Basis is an advertising automation platform providing REST APIs for programmatic DSP campaign management, audience targeting, publisher management, reporting, and omnichannel media buying automation across display, video, audio, native, connected TV, and site-direct channels.
examples:
- key_count: 1
  name: Basis Api Examples
  slug: basis-api-examples
finops:
- name: Basis Finops
  service_category: ''
  slug: basis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/basis.png
json_schemas:
- name: Agency Get
  property_count: 1
  slug: agency-get
- name: Brands Get
  property_count: 2
  slug: brands-get
- name: Campaigns Addons Get
  property_count: 2
  slug: campaigns-addons-get
- name: Campaigns Get
  property_count: 3
  slug: campaigns-get
- name: Campaigns Line_Items Get
  property_count: 3
  slug: campaigns-line_items-get
- name: Clients Get
  property_count: 2
  slug: clients-get
- name: Conversions Get
  property_count: 2
  slug: conversions-get
- name: Creatives Get
  property_count: 2
  slug: creatives-get
- name: Delivery_Sources Get
  property_count: 2
  slug: delivery_sources-get
- name: Groups Get
  property_count: 2
  slug: groups-get
- name: Kpis Get
  property_count: 2
  slug: kpis-get
- name: Me Get
  property_count: 1
  slug: me-get
- name: Properties Get
  property_count: 3
  slug: properties-get
- name: Stats Get
  property_count: 2
  slug: stats-get
- name: Tactics Get
  property_count: 2
  slug: tactics-get
- name: Vendors Get
  property_count: 2
  slug: vendors-get
- name: Verticals Get
  property_count: 2
  slug: verticals-get
jsonld:
- class_count: 18
  name: Basis Context
  property_count: 9
  slug: basis-context
layout: provider
modified: '2026-08-13'
name: Basis
nav: Providers
network: true
overview: 'Basis publishes 1 API on the [APIs.io](https://apis.io/) network: Analytics API. Tagged areas include Programmatic Advertising, DSP, Media Buying, Campaign Management, and Audience Targeting.


  The Basis catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Basis'' developer surface includes authentication, documentation, engineering blog, pricing, sandbox, signup flow, support, and 22 more developer resources.'
plans:
- name: Basis Plans Pricing
  plan_count: 1
  slug: basis-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Basis Rate Limits
  slug: basis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Basis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: basis-jsonschema-spectral-rules
scopes:
- name: Basis Scopes
  scope_count: 0
  slug: basis-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 82.3
    catalog_earned_first_party: 20.0
    catalog_gap: 32.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    contract_governance: 43.2
    contract_quality: 66.0
    developer_ergonomics: 44.6
    discoverability: 68.5
    operational_transparency: 31.6
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/basis/refs/heads/main/screenshots/basis-2026-06-20T173036.png
security:
- kind: authentication
  name: Basis Authentication
  slug: basis-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Basis Domain Security
  slug: basis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: basis
tags:
- Programmatic Advertising
- DSP
- Media Buying
- Campaign Management
- Audience Targeting
- AdTech
website: https://basis.com/
---
