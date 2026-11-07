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
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/teslafi/security/teslafi-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/teslafi-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/teslafi/well-known/teslafi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/teslafi-well-known.yml
- group: other
  href: https://artifacts.apis.io/teslafi/hosts/teslafi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/teslafi-hosts.yml
- group: other
  href: https://artifacts.apis.io/teslafi/vendors/teslafi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/teslafi-vendors.yml
- group: auth
  href: https://artifacts.apis.io/teslafi/security/teslafi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/teslafi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/teslafi/security/teslafi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teslafi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://teslafi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://teslafi.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://teslafi.com/signup.php
- group: operate
  title: ''
  type: Support
  url: https://help.teslafi.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://teslafi.com/terms.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://teslafi.com/privacy.php
coverage:
  checked: '2026-10-28'
  detail: Access to API documentation redirects to a login page (302 to /userlogin.php)
  evidence:
  - status: 302
    url: https://teslafi.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-28'
description: TeslaFi provides a cloud-based data logger and analytics platform for Tesla vehicle owners. It automatically records drives, charges, and parked time, offering detailed maps, charts, cost analysis, and alerts. Users can view drive logs, energy efficiency, and generate reports, with features like auto-tagged locations, trip summaries, and sharing via public links. The service includes a 14‑day free trial without requiring payment information and supports integration with Alexa and other tools.
layout: provider
modified: '2026-10-28'
name: TeslaFi
nav: Providers
network: true
overview: 'TeslaFi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tesla, Data-Logger, and Vehicle-Analytics.


  TeslaFi''s developer surface includes documentation, getting-started guide, support, and 9 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 35.7
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/teslafi/teslafi-2026-11-03T144452.png
security:
- kind: domain-security
  name: Teslafi Domain Security
  slug: teslafi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Teslafi Vulnerability Disclosure
  slug: teslafi-vulnerability-disclosure
  summary_line: no policy recorded
slug: teslafi
tags:
- Company
- Tesla
- Data-Logger
- Vehicle-Analytics
website: https://teslafi.com/
---
