---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/teamsense/well-known/teamsense-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/teamsense-www-security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://teamsense.com/security
- group: auth
  title: ''
  type: Security
  url: https://www.teamsense.com/security-policy
- group: agent
  href: https://artifacts.apis.io/teamsense/llms/teamsense-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/teamsense-llms.txt
- group: auth
  href: https://artifacts.apis.io/teamsense/well-known/teamsense-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/teamsense-security.txt
- group: agent
  href: https://artifacts.apis.io/teamsense/well-known/teamsense-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/teamsense-well-known.yml
- group: other
  href: https://artifacts.apis.io/teamsense/hosts/teamsense-hosts.yml
  title: ''
  type: Hosts
  url: hosts/teamsense-hosts.yml
- group: other
  href: https://artifacts.apis.io/teamsense/vendors/teamsense-vendors.yml
  title: ''
  type: Vendors
  url: vendors/teamsense-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.teamsense.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teamsense.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://help.teamsense.com/data-needed-for-onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://help.teamsense.com/
- group: auth
  href: https://artifacts.apis.io/teamsense/security/teamsense-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/teamsense-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/teamsense/security/teamsense-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/teamsense-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/teamsense/security/teamsense-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teamsense-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://teamsense.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://app.teamsense.com/api/mcp
  - status: 403
    url: https://help.teamsense.com/mcp
  - status: 403
    url: https://pages.teamsense.com/mcp
  - status: 200
    url: https://teamsense.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: TeamSense provides an all‑in‑one attendance management and employee communication platform for frontline workers. Built for manufacturing, HR, and operations teams, it offers features like attendance tracking, shift start, forms, insights, points‑system calculations, and integrations. The SaaS solution helps reduce turnover, improve visibility, and streamline absence reporting across industries.
image: https://glib-coyote.transforms.svdcdn.com/production/teamsense/TeamSense-SEO-Image-1.png?w=1200&h=630&q=82&auto=format&fit=clip&dm=1664454302&s=a8c678782fc6b12893ed72414546eb71
layout: provider
modified: '2026-10-21'
name: TeamSense
nav: Providers
network: true
overview: 'TeamSense is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Attendance, WorkforceManagement, SaaS, and Frontline.


  TeamSense''s developer surface includes support, getting-started guide, documentation, and 13 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Teamsense Domain Security
  slug: teamsense-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Teamsense Vulnerability Disclosure
  slug: teamsense-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Teamsense Trust Center
  slug: teamsense-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: teamsense
tags:
- Company
- Attendance
- WorkforceManagement
- SaaS
- Frontline
website: https://teamsense.com
---
