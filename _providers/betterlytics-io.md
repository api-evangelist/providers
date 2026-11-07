---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Betterlytics provides cookieless web analytics, session replay, error tracking, Core Web Vitals, and uptime monitoring via its platform.
  name: Betterlytics API
  slug: betterlytics-api
- description: 'Betterlytics API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Betterlytics API
  slug: betterlytics-io-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/betterlytics-io/plans/betterlytics-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/betterlytics-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/betterlytics-io/rules/betterlytics-io-rules.yml
  title: ''
  type: Spectral
  url: rules/betterlytics-io-rules.yml
- group: design
  href: https://artifacts.apis.io/betterlytics-io/json-ld/betterlytics-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/betterlytics-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/betterlytics-io/vocabulary/betterlytics-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/betterlytics-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/betterlytics-io/data-model/betterlytics-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/betterlytics-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/betterlytics-io/changelog/betterlytics-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/betterlytics-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/betterlytics-io/conformance/betterlytics-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/betterlytics-io-conformance.yml
- group: auth
  href: https://artifacts.apis.io/betterlytics-io/well-known/betterlytics-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/betterlytics-io-security.txt
- group: auth
  href: https://artifacts.apis.io/betterlytics-io/well-known/betterlytics-io-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/betterlytics-io-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/betterlytics-io/well-known/betterlytics-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/betterlytics-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/betterlytics-io/hosts/betterlytics-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betterlytics-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/betterlytics-io/packages/betterlytics-io-packages.yml
  title: ''
  type: SDKs
  url: packages/betterlytics-io-packages.yml
- group: build
  href: https://artifacts.apis.io/betterlytics-io/packages/betterlytics-io-packages.yml
  title: ''
  type: Packages
  url: packages/betterlytics-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betterlytics.io/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.betterlytics.io
- group: auth
  title: ''
  type: Security
  url: https://github.com/betterlytics/betterlytics/security/policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betterlytics.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://betterlytics.io/pricing
- group: start
  title: ''
  type: Login
  url: https://betterlytics.io/signin
- group: operate
  title: ''
  type: ChangeLog
  url: https://betterlytics.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://betterlytics.io/docs/installation/cloud-hosting
- group: docs
  title: ''
  type: Documentation
  url: https://dev.betterlytics.io/
- group: auth
  href: https://artifacts.apis.io/betterlytics-io/security/betterlytics-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/betterlytics-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/betterlytics-io/security/betterlytics-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betterlytics-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betterlytics.io/
coverage:
  checked: '2026-11-02'
  detail: Docs are rendered via JavaScript, no machine‑readable OpenAPI spec found.
  evidence:
  - status: 200
    url: https://betterlytics.io/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Betterlytics provides cookieless web analytics, session replay, error tracking, Core Web Vitals, and uptime monitoring in a single open‑source dashboard. Hosted in the EU, it offers a free plan and aims to give developers privacy‑first insight into website performance and user behavior.
image: https://betterlytics.io/og_image.jpg
json_schemas:
- name: PostRequest
  property_count: 2
  slug: betterlytics-io-post-request
jsonld:
- class_count: 1
  name: Betterlytics Io Context
  property_count: 2
  slug: betterlytics-io-context
layout: provider
modified: '2026-11-02'
name: Betterlytics
nav: Providers
network: true
overview: 'Betterlytics is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Session Replay, Error Tracking, Core Web Vitals, and Uptime Monitoring.


  The Betterlytics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Betterlytics'' developer surface includes changelog, pricing, getting-started guide, documentation, and 21 more developer resources.'
plans:
- name: Betterlytics Io Plans Pricing
  plan_count: 3
  slug: betterlytics-io-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Betterlytics Io Rate Limits
  slug: betterlytics-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: Betterlytics API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: betterlytics-io-rules
scopes:
- name: Betterlytics Io Scopes
  scope_count: 0
  slug: betterlytics-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 16.4
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 21.1
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
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Betterlytics Io Authentication
  slug: betterlytics-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Betterlytics Io Domain Security
  slug: betterlytics-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Betterlytics Io Vulnerability Disclosure
  slug: betterlytics-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: betterlytics-io
tags:
- Analytics
- Session Replay
- Error Tracking
- Core Web Vitals
- Uptime Monitoring
- Open Source
website: https://betterlytics.io/
---
