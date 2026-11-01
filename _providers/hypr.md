---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-10-31'
api_count: 6
apis:
- baseURL: https://{tenant}.hypr.com
  baseurl_source: declared
  description: The Analytics API from HYPR — 14 operation(s) for analytics.
  name: HYPR Analytics API
  slug: hypr-analytics-api
- baseURL: https://{tenant}.hypr.com
  baseurl_source: declared
  description: The Control Center API from HYPR — 77 operation(s) for control center.
  name: HYPR Control Center API
  slug: hypr-control-center-api
- baseURL: https://{tenant}.hypr.com
  baseurl_source: declared
  description: The FIDO API API from HYPR — 3 operation(s) for fido api.
  name: HYPR FIDO API
  slug: hypr-fido-api-api
- baseURL: https://{tenant}.hypr.com
  baseurl_source: declared
  description: The FIDO2 RP API API from HYPR — 13 operation(s) for fido2 rp api.
  name: HYPR FIDO2 RP API
  slug: hypr-fido2-rp-api-api
- baseURL: https://{tenant}.hypr.com
  baseurl_source: declared
  description: The RADIUS API from HYPR — 9 operation(s) for radius.
  name: HYPR RADIUS API
  slug: hypr-radius-api
- baseURL: https://{tenant}.hypr.com
  baseurl_source: declared
  description: The RP Applications API from HYPR — 111 operation(s) for rp applications.
  name: HYPR RP Applications API
  slug: hypr-rp-applications-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/hypr/plans/hypr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hypr-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hypr/rules/hypr-rules.yml
  title: ''
  type: Spectral
  url: rules/hypr-rules.yml
- group: auth
  href: https://artifacts.apis.io/hypr/security/hypr-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/hypr-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/hypr/errors/hypr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hypr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hypr/conformance/hypr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hypr-conformance.yml
- group: auth
  href: https://artifacts.apis.io/hypr/well-known/hypr-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hypr-status-security.txt
- group: agent
  href: https://artifacts.apis.io/hypr/well-known/hypr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hypr-well-known.yml
- group: other
  href: https://artifacts.apis.io/hypr/hosts/hypr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hypr-hosts.yml
- group: other
  href: https://artifacts.apis.io/hypr/vendors/hypr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hypr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/hypr/security/hypr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hypr-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hypr/security/hypr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hypr-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hypr/security/hypr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hypr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hypr.com
- group: build
  title: ''
  type: Postman
  url: https://apidocs.hypr.com
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.hypr.com
- group: company
  title: ''
  type: Blog
  url: https://www.hypr.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.hypr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hypr.com
- group: start
  title: ''
  type: GettingStarted
  url: https://get.hypr.com/getting-started
- group: company
  title: ''
  type: Newsroom
  url: https://www.hypr.com/company/newsroom
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hypr.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hypr.com/privacy-policy/
- group: build
  title: ''
  type: SDKs
  url: https://www.hypr.com/platform/sdk
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hypr.com
- group: operate
  title: ''
  type: Support
  url: https://support.hypr.com/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hypr.com/trust-center/terms-of-service
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.hypr.com/mcp
  - status: 403
    url: https://get.hypr.com/mcp
  - status: 200
    url: https://www.hypr.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: HYPR is a passwordless identity assurance company. Its Passwordless REST APIs, served from each customer's own HYPR Server, cover device registration, authentication, user management, RP application configuration, audit trail and administration.
finops:
- has_sources: true
  method: derived
  name: Hypr Finops
  primary_unit: user
  service_category: ''
  slug: hypr-finops
  template: false
image: https://www.hypr.com/hubfs/Company/HYPR-general-tile.jpg
layout: provider
modified: '2026-10-13'
name: HYPR
nav: Providers
network: true
overview: 'HYPR is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Control Center API, FIDO API, and 3 more. Tagged areas include Company, Identity, Passwordless, Authentication, and FIDO.


  The HYPR catalog on APIs.io includes 1 Spectral governance ruleset.


  HYPR''s developer surface includes API reference, engineering blog, documentation, getting-started guide, pricing, support, and 20 more developer resources.'
plans:
- name: Hypr Plans Pricing
  plan_count: 7
  slug: hypr-plans-pricing
- name: Hypr Price Estimates
  plan_count: 0
  slug: hypr-price-estimates
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: HYPR API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: hypr-rules
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 11.1
    developer_ergonomics: 57.1
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 38.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hypr Domain Security
  slug: hypr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hypr Vulnerability Disclosure
  slug: hypr-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Hypr Trust Center
  slug: hypr-trust-center
  summary_line: trust center published
slug: hypr
tags:
- Company
- Identity
- Passwordless
- Authentication
- FIDO
- Security
website: https://www.hypr.com
---
