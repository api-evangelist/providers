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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gps-insight/refs/heads/main/changelog/gps-insight-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gps-insight-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.gpsinsight.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gps-insight/refs/heads/main/llms/gps-insight-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gps-insight-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gps-insight/refs/heads/main/well-known/gps-insight-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gps-insight-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gps-insight/refs/heads/main/well-known/gps-insight-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gps-insight-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gps-insight/refs/heads/main/hosts/gps-insight-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gps-insight-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gps-insight/refs/heads/main/vendors/gps-insight-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gps-insight-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gpsinsight.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://help.gpsinsight.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gpsinsight.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gpsinsight.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.gpsinsight.com/resources/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.gpsinsight.com/resources/leadership/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.gpsinsight.com
- group: company
  title: ''
  type: Blog
  url: https://www.gpsinsight.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.gpsinsight.com/feature/getting-started/?product=gpsportal
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gps-insight/refs/heads/main/security/gps-insight-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gps-insight-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gps-insight/refs/heads/main/security/gps-insight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gps-insight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gpsinsight.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.gpsinsight.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.gpsinsight.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: GPS Insight provides fleet management and GPS tracking solutions for businesses across industries such as construction, energy, government, and transportation. Their platform offers real-time vehicle tracking, driver behavior analytics, smart dash cameras, field service management, and compliance tools, helping companies improve safety, efficiency, and accountability while reducing operational costs.
layout: provider
modified: '2026-10-13'
name: GPS Insight
nav: Providers
network: true
overview: 'GPS Insight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fleet Management, GPS Tracking, Telematics, and Software-as-a-Service.


  GPS Insight''s developer surface includes changelog, support, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 55.4
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gps Insight Domain Security
  slug: gps-insight-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Gps Insight Trust Center
  slug: gps-insight-trust-center
  summary_line: SOC 2, GDPR
slug: gps-insight
tags:
- Company
- Fleet Management
- GPS Tracking
- Telematics
- Software-as-a-Service
website: https://www.gpsinsight.com
---
