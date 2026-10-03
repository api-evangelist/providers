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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.8
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Bayzat provides a cloud‑based HR, payroll, benefits and spend‑management platform with an API (access gated).
  name: Bayzat API
  slug: bayzat-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.bayzat.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bayzat/refs/heads/main/well-known/bayzat-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bayzat-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bayzat/refs/heads/main/well-known/bayzat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bayzat-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bayzat/refs/heads/main/hosts/bayzat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bayzat-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bayzat.com/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://www.bayzat.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bayzat.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.bayzat.com/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bayzat
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bayzat/refs/heads/main/security/bayzat-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bayzat-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bayzat/refs/heads/main/security/bayzat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bayzat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bayzat.com
- group: company
  title: ''
  type: Blog
  url: https://www.bayzat.com/blog
coverage:
  checked: '2026-09-27'
  detail: API spec at https://api.bayzat.com/openapi.json returns 401 Unauthorized, indicating access is gated behind authentication.
  evidence:
  - status: 401
    url: https://api.bayzat.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-09-27'
description: Bayzat provides a cloud‑based HR, payroll, benefits and spend‑management platform for companies in the UAE, KSA and GCC. Their solution automates core HR processes, payroll processing, employee benefits administration, corporate card spend, and integrates AI‑driven analytics to streamline workforce management and finance operations. Serving over 4,000 enterprises, Bayzat emphasizes compliance with regional regulations and offers a unified employee experience across hiring, onboarding, performance, and off‑boarding.
layout: provider
modified: '2026-09-27'
name: Bayzat
nav: Providers
network: true
overview: 'Bayzat publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Human Resources, Payroll, Benefits, Software-as-a-Service, and GCC.


  Bayzat''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bayzat Domain Security
  slug: bayzat-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Bayzat Trust Center
  slug: bayzat-trust-center
  summary_line: SOC 2, ISO 27001
slug: bayzat
tags:
- Human Resources
- Payroll
- Benefits
- Software-as-a-Service
- GCC
website: https://www.bayzat.com
---
