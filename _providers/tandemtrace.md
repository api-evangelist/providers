---
agent_readiness:
  band: human-only
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://tandemtrace.ai/contact
- group: agent
  href: https://artifacts.apis.io/tandemtrace/llms/tandemtrace-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tandemtrace-llms.txt
- group: auth
  href: https://artifacts.apis.io/tandemtrace/well-known/tandemtrace-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tandemtrace-www-security.txt
- group: auth
  href: https://artifacts.apis.io/tandemtrace/well-known/tandemtrace-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tandemtrace-security.txt
- group: agent
  href: https://artifacts.apis.io/tandemtrace/well-known/tandemtrace-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tandemtrace-well-known.yml
- group: other
  href: https://artifacts.apis.io/tandemtrace/hosts/tandemtrace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tandemtrace-hosts.yml
- group: other
  href: https://artifacts.apis.io/tandemtrace/vendors/tandemtrace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tandemtrace-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tandemtrace.ai/privacy/
- group: company
  title: ''
  type: Blog
  url: https://www.tandemtrace.ai/blog/
- group: auth
  href: https://artifacts.apis.io/tandemtrace/security/tandemtrace-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tandemtrace-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tandemtrace/security/tandemtrace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tandemtrace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tandemtrace.ai
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://signal.tandemtrace.ai/api/mcp
  - status: 200
    url: https://tandemtrace.ai
  reason: partner-login
  state: gated
created: '2026-10-25'
description: TandemTrace provides an autonomous AI-driven security operations layer that reads telemetry from SIEM, EDR, identity and cloud sources via read‑only APIs. It triages alerts at machine speed, enriches them with threat intel, and presents actionable verdicts to SOC analysts. The platform emphasizes human judgment, offering no‑agent, read‑only integration, and aims to reduce noise by up to 99% while maintaining full coverage across major cloud and security tools.
image: https://www.tandemtrace.ai/og-tandemtrace.png
layout: provider
modified: '2026-10-25'
name: TandemTrace
nav: Providers
network: true
overview: 'TandemTrace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, AI, SOC, and Automation.


  TandemTrace''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tandemtrace Domain Security
  slug: tandemtrace-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Tandemtrace Vulnerability Disclosure
  slug: tandemtrace-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tandemtrace
tags:
- Company
- Security
- AI
- SOC
- Automation
website: https://tandemtrace.ai
---
