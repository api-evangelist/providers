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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.xing.com
  baseurl_source: declared
  description: 'XING API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: XING API
  slug: xing-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/xing/rules/xing-rules.yml
  title: ''
  type: Spectral
  url: rules/xing-rules.yml
- group: design
  href: https://artifacts.apis.io/xing/json-ld/xing-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/xing-context.jsonld
- group: design
  href: https://artifacts.apis.io/xing/vocabulary/xing-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/xing-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/xing/data-model/xing-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xing-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://privacy.xing.com/en/your-security
- group: auth
  title: ''
  type: Security
  url: https://www.new-work.se/.well-known/rfc-2350.txt
- group: design
  href: https://artifacts.apis.io/xing/conformance/xing-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xing-conformance.yml
- group: agent
  href: https://artifacts.apis.io/xing/llms/xing-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xing-llms.txt
- group: auth
  href: https://artifacts.apis.io/xing/well-known/xing-xing-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xing-xing-security.txt
- group: auth
  href: https://artifacts.apis.io/xing/well-known/xing-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xing-security.txt
- group: auth
  href: https://artifacts.apis.io/xing/well-known/xing-corporate-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xing-corporate-security.txt
- group: agent
  href: https://artifacts.apis.io/xing/well-known/xing-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xing-well-known.yml
- group: other
  href: https://artifacts.apis.io/xing/hosts/xing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xing-hosts.yml
- group: other
  href: https://artifacts.apis.io/xing/vendors/xing-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xing-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.xing.com/hc/de?segment=b2c
- group: start
  title: ''
  type: SignUp
  url: https://www.xing.com/start/signup
- group: company
  title: ''
  type: Newsroom
  url: https://corporate.xing.com/de/Newsroom/pressekontakt/pressemitteilungen
- group: auth
  href: https://artifacts.apis.io/xing/security/xing-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/xing-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/xing/security/xing-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/xing-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/xing/security/xing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xing.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.xing.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.xing.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.xing.com/api/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/xing-engineering
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dev.xing.com/api/terms_and_conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xing.com/privacy
coverage:
  checked: '2026-10-28'
  detail: Developer portal pages render HTML without machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://dev.xing.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: XING is a professional networking platform based in Germany that connects professionals, helps them find jobs, and enables recruiters to discover talent. The service offers job listings, company profiles, and networking tools for career development, serving over a million job seekers and thousands of recruiters across Europe.
image: https://static.xingcdn.com/og-cover-image.png
json_schemas:
- name: GetVendorJobsOrdersJsonResponse
  property_count: 4
  slug: xing-get-vendor-jobs-orders-json-response
- name: GetVendorJobsPostingsJsonResponse
  property_count: 4
  slug: xing-get-vendor-jobs-postings-json-response
- name: GetVendorJobsPostingsStatusJsonResponse
  property_count: 4
  slug: xing-get-vendor-jobs-postings-status-json-response
- name: PostVendorJobsPostingsJsonRequest
  property_count: 20
  slug: xing-post-vendor-jobs-postings-json-request
- name: PostVendorJobsPostingsJsonResponse
  property_count: 2
  slug: xing-post-vendor-jobs-postings-json-response
jsonld:
- class_count: 5
  name: Xing Context
  property_count: 26
  slug: xing-context
layout: provider
modified: '2026-10-28'
name: XING
nav: Providers
network: true
overview: 'XING is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, Job, Recruiters, and Europe.


  The XING catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  XING''s developer surface includes support, signup flow, documentation, API reference, engineering blog, and 22 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: XING API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: xing-rules
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 25.1
    developer_ergonomics: 16.7
    discoverability: 74.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 36.8
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
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/xing/xing-2026-11-03T150301.png
security:
- kind: domain-security
  name: Xing Domain Security
  slug: xing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Xing Vulnerability Disclosure
  slug: xing-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Xing Trust Center
  slug: xing-trust-center
  summary_line: PCI DSS, GDPR
slug: xing
tags:
- Company
- Networking
- Job
- Recruiters
- Europe
website: https://xing.com/
---
