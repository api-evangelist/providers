---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
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
  score: 24.2
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: REST API for accessing iSpot.tv TV and video ad measurement data — airing occurrence, estimated spend, household and person-level impressions, attention metrics, OTT/streaming impressions, TV conversi
  name: iSpot REST API v4
  slug: ispot-rest-api-v4
- description: Server-side and client-side measurement ingest endpoints. A 1x1 GIF pixel accepts OTT/CTV/digital impression events (pi.ispot.tv) and TV conversion events (pt.ispot.tv) keyed by a client-specific trac
  name: iSpot Impression & TV Conversion Pixel API v2
  slug: ispot-impression-tv-conversion-pixel-api-v2
- baseURL: https://api.ispot.tv
  baseurl_source: declared
  description: 'iSpot.tv API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: iSpot.tv API
  slug: ispottv-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/ispottv/rules/ispottv-rules.yml
  title: ''
  type: Spectral
  url: rules/ispottv-rules.yml
- group: design
  href: https://artifacts.apis.io/ispottv/vocabulary/ispottv-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ispottv-vocabulary.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ispot.tv/
- group: auth
  href: https://artifacts.apis.io/ispottv/security/ispottv-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ispottv-trust-center.yml
- group: operate
  href: https://artifacts.apis.io/ispottv/lifecycle/ispottv-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ispottv-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/ispottv/hosts/ispottv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ispottv-hosts.yml
- group: build
  href: https://artifacts.apis.io/ispottv/integrations/ispottv-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/ispottv-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/ispottv/vendors/ispottv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ispottv-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ispot.tv:443/hub/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ispot.tv/hub/feed/
- group: company
  title: ''
  type: Website
  url: http://www.ispot.tv/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ispot.tv/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ispot.tv/documentation/api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ispot.tv/api/v4
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ispot.tv/quickstarts/api
- group: start
  title: ''
  type: Login
  url: https://login.ispot.tv/
- group: operate
  title: ''
  type: Support
  url: https://www.ispot.tv/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ispot-tv
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ispot.tv/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.ispot.tv/hub/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ispot.tv/hub/agreements/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ispot.tv/hub/agreements/privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ispot.tv/
- group: auth
  href: https://artifacts.apis.io/ispottv/security/ispottv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ispottv-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ispot.tv
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.ispot.tv/releases/api/v4/notes
- group: operate
  href: https://artifacts.apis.io/ispottv/changelog/ispottv-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ispottv-changelog.yml
- group: auth
  href: https://artifacts.apis.io/ispottv/authentication/ispottv-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ispottv-authentication.yml
- group: design
  href: https://artifacts.apis.io/ispottv/conventions/ispottv-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ispottv-conventions.yml
- group: operate
  href: https://artifacts.apis.io/ispottv/rate-limits/ispottv-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ispottv-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/ispottv/lifecycle/ispottv-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ispottv-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/ispottv/plans/ispottv-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ispottv-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ispottv/conformance/ispottv-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ispottv-conformance.yml
- group: design
  href: https://artifacts.apis.io/ispottv/data-model/ispottv-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ispottv-data-model.yml
- group: design
  href: https://artifacts.apis.io/ispottv/components/ispottv-components.yml
  title: ''
  type: Components
  url: components/ispottv-components.yml
- group: start
  href: https://artifacts.apis.io/ispottv/sandbox/ispottv-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ispottv-sandbox.yml
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: http://www.ispot.tv/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: iSpot.tv is a TV and video advertising measurement company that provides end-to-end measurement unifying creative assessment, audience measurement, and outcome attribution across linear TV and streaming. Its platform draws on data from tens of millions of smart TVs and set-top boxes to track ad occurrences, impressions, share of voice, creative effectiveness, and return on ad spend for advertisers, agencies, and networks. iSpot exposes its data programmatically through the iSpot REST API (v4), documented at a dedicated developer portal with quickstarts, an API reference, a Python sample, an interactive API demo tool, and release notes. iSpot.tv is backed by Insight Partners and was added to the API Evangelist network from that portfolio.
finops:
- has_sources: true
  method: derived
  name: Ispottv Finops
  primary_unit: ''
  service_category: ''
  slug: ispottv-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ispottv.png
layout: provider
modified: '2026-10-06'
name: iSpot.tv
nav: Providers
network: true
overview: 'iSpot.tv is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, TV Advertising, Advertising Measurement, Analytics, and Attribution.


  The iSpot.tv catalog on APIs.io includes 1 Spectral governance ruleset.


  iSpot.tv''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, changelog, and 29 more developer resources.'
plans:
- name: Ispottv Plans Pricing
  plan_count: 0
  slug: ispottv-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 21
  name: Ispottv Rate Limits
  slug: ispottv-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: iSpot.tv API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: ispottv-rules
scopes:
- name: Ispottv Scopes
  scope_count: 0
  slug: ispottv-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 57.8
    catalog_earned_first_party: 12.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 11.2
    developer_ergonomics: 60.7
    discoverability: 78.6
    operational_transparency: 73.7
  previous_composite: 51.0
  provenance:
    conformance: first-party
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
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/ispottv/ispottv-2026-07-25T222949.png
security:
- kind: authentication
  name: Ispottv Authentication
  slug: ispottv-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ispottv Domain Security
  slug: ispottv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ispottv Trust Center
  slug: ispottv-trust-center
  summary_line: SOC 2, ISO 27001
slug: ispottv
tags:
- Company
- TV Advertising
- Advertising Measurement
- Analytics
- Attribution
- Media
- Marketing
- Streaming
website: http://www.ispot.tv/
---
