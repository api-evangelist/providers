---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
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
overview: 'TeslaFi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tesla, Data-Logger, Vehicle-Analytics, and API.


  TeslaFi''s developer surface includes documentation, getting-started guide, support, and 9 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- API
website: https://teslafi.com/
---
