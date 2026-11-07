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
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://chrome-stats.com
  baseurl_source: declared
  description: Chrome-Stats API provides endpoints for extension and app analytics.
  name: Chrome-Stats API
  slug: chrome-stats-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/chrome-stats-com/plans/chrome-stats-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chrome-stats-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/chrome-stats-com/security/chrome-stats-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/chrome-stats-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/chrome-stats-com/conformance/chrome-stats-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chrome-stats-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/chrome-stats-com/well-known/chrome-stats-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chrome-stats-com-security.txt
- group: agent
  href: https://artifacts.apis.io/chrome-stats-com/well-known/chrome-stats-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chrome-stats-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/chrome-stats-com/hosts/chrome-stats-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chrome-stats-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/chrome-stats-com/vendors/chrome-stats-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chrome-stats-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/chrome-stats-com/security/chrome-stats-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chrome-stats-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chrome-stats-com/security/chrome-stats-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chrome-stats-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chrome-stats.com/
- group: docs
  title: ''
  type: Documentation
  url: https://chrome-stats.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://chrome-stats.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://chrome-stats.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chrome-stats.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chrome-stats.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://chrome-stats.com/blog
created: '2026-11-03'
description: Chrome-Stats provides comprehensive analytics and historical data for browser extensions and mobile apps across major marketplaces. It aggregates public store metrics, permissions, rankings, and download counts, offering CSV exports, API access, and webhook notifications for developers, security teams, and researchers. Launched in 2020, the service expanded to cover Edge, Firefox, Android, and Apple app stores, delivering insights for growth, risk assessment, and market research.
layout: provider
modified: '2026-11-03'
name: Chrome-Stats
nav: Providers
network: true
overview: 'Chrome-Stats is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Extensions, Mobile App, and Data.


  Chrome-Stats'' developer surface includes documentation, API reference, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Chrome Stats Com Plans Pricing
  plan_count: 1
  slug: chrome-stats-com-plans-pricing
random_paper: 22
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 32.9
    developer_ergonomics: 9.5
    discoverability: 62.5
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chrome Stats Com Domain Security
  slug: chrome-stats-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chrome Stats Com Vulnerability Disclosure
  slug: chrome-stats-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chrome-stats-com
tags:
- Company
- Analytics
- Extensions
- Mobile App
- Data
website: https://chrome-stats.com/
---
