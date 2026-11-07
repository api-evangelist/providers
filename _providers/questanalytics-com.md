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
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides provider data verification and validation APIs for health plans and networks.
  name: BetterDoctor API
  slug: betterdoctor-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/questanalytics-com/well-known/questanalytics-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/questanalytics-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/questanalytics-com/hosts/questanalytics-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/questanalytics-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/questanalytics-com/vendors/questanalytics-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/questanalytics-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://questanalytics.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://questanalytics.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://questanalytics.com/news/
- group: start
  href: https://artifacts.apis.io/questanalytics-com/adequacy-api/quickstart
  title: ''
  type: GettingStarted
  url: /adequacy-api/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developer.questanalytics.com/
- group: auth
  href: https://artifacts.apis.io/questanalytics-com/security/questanalytics-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/questanalytics-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://questanalytics.com/how-we-help/betterdoctor/
coverage:
  checked: '2026-10-29'
  detail: Developer portal requires JavaScript to render API docs, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://developer.questanalytics.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: BetterDoctor, now part of Quest Analytics, provides a comprehensive provider data verification and validation platform for health plans, payers, dental and vision networks, and regulators. Their solution helps ensure accurate provider information, compliance, and network performance through advanced decision apps and analytics, supporting large groups and enterprise solutions across the United States.
image: https://questanalytics.com/wp-content/uploads/2022/11/BetterDoctor-040121-2.png
layout: provider
modified: '2026-10-29'
name: BetterDoctor
nav: Providers
network: true
overview: 'BetterDoctor is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Data Verification, Provider Network, and Analytics.


  BetterDoctor''s developer surface includes getting-started guide, documentation, and 8 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 14.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/questanalytics-com/questanalytics-com-2026-11-03T141827.png
security:
- kind: domain-security
  name: Questanalytics Com Domain Security
  slug: questanalytics-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: questanalytics-com
tags:
- Company
- Healthcare
- Data Verification
- Provider Network
- Analytics
website: https://questanalytics.com/how-we-help/betterdoctor/
---
