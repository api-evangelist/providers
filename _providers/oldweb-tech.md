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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/oldweb-tech/hosts/oldweb-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oldweb-tech-hosts.yml
- group: auth
  href: https://artifacts.apis.io/oldweb-tech/security/oldweb-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oldweb-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oldweb.tech/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oldweb.tech/privacy.html
coverage:
  checked: '2026-10-29'
  detail: The site offers only offline browser utilities and no developer program or public API.
  evidence:
  - status: 200
    url: https://oldweb.tech/
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: OldWeb LLC operates the website oldweb.tech, offering a collection of fast, cookie‑free browser utilities that run entirely offline. The tools include a subnet calculator, CIDR converter, regex tester, JWT decoder, hash generators, paycheck and loan calculators, PDF utilities, and more. All processing happens in the user’s browser with no cookies or data storage, providing privacy‑focused network and developer utilities.
image: https://oldweb.tech/logo/og-image.png
layout: provider
modified: '2026-10-29'
name: oldweb-tech
nav: Providers
network: true
overview: oldweb-tech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Network, Utilities, Offline, Privacy, and Tools.
random_paper: 22
rate_limits:
- limit_count: 0
  name: Oldweb Tech Rate Limits
  slug: oldweb-tech-rate-limits
scopes:
- name: Oldweb Tech Scopes
  scope_count: 0
  slug: oldweb-tech-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 22.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Oldweb Tech Authentication
  slug: oldweb-tech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Oldweb Tech Domain Security
  slug: oldweb-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oldweb-tech
tags:
- Network
- Utilities
- Offline
- Privacy
- Tools
website: https://oldweb.tech/
---
