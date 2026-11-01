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
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/alden-tech/hosts/alden-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alden-tech-hosts.yml
- group: auth
  href: https://artifacts.apis.io/alden-tech/security/alden-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alden-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alden.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://www.alden.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.alden.tech/web/login
- group: operate
  title: ''
  type: Support
  url: https://www.alden.tech/helpdesk/member-support-1
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alden.tech/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alden.tech/privacy
coverage:
  checked: '2026-10-29'
  detail: The public website does not provide any machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.alden.tech/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Alden provides next‑generation microbe testing solutions that deliver accurate diagnostic results within 8–24 hours, helping laboratories and food‑safety operations streamline workflows, lower costs, and reduce disease risk. Their platform offers fast, accurate, and easy‑to‑use testing for pathogens, mycotoxins, and viruses, supporting rapid decision‑making in food safety and public health.
image: https://www.alden.tech/web/image/9568-a1676a5f/Alden-2024-06.png
layout: provider
modified: '2026-10-29'
name: Smart Diagnostics Systems
nav: Providers
network: true
overview: 'Smart Diagnostics Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diagnostics, Microbiology, Food Safety, and Healthcare.


  Smart Diagnostics Systems'' developer surface includes documentation, support, and 6 more developer resources.'
random_paper: 21
scopes:
- name: Alden Tech Scopes
  scope_count: 0
  slug: alden-tech-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 24.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alden Tech Authentication
  slug: alden-tech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Alden Tech Domain Security
  slug: alden-tech-domain-security
  summary_line: DMARC
slug: alden-tech
tags:
- Company
- Diagnostics
- Microbiology
- Food Safety
- Healthcare
- API
website: https://alden.tech/
---
