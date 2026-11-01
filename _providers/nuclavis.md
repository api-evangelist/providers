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
- group: operate
  href: https://artifacts.apis.io/nuclavis/changelog/nuclavis-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nuclavis-changelog.yml
- group: other
  href: https://artifacts.apis.io/nuclavis/hosts/nuclavis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nuclavis-hosts.yml
- group: other
  href: https://artifacts.apis.io/nuclavis/vendors/nuclavis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nuclavis-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://nuclavis.com/sign-up
- group: operate
  title: ''
  type: ChangeLog
  url: https://nuclavis.com/release-notes/
- group: auth
  href: https://artifacts.apis.io/nuclavis/security/nuclavis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nuclavis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nuclavis.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://nuclavis.com/sign-up/
- group: operate
  title: ''
  type: Support
  url: http://support.nuclavis.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nuclavis.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nuclavis
coverage:
  checked: '2026-10-28'
  detail: No public developer program or API documentation is provided on the company's website.
  evidence:
  - status: 200
    url: https://nuclavis.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Nuclavis provides mobile‑first peer‑to‑peer fundraising solutions for nonprofit organizations. Its platform delivers branded mobile apps, messaging tools, QR code integration, and analytics to help fundraisers recruit, engage, and raise more money. The company integrates with major P2P fundraising platforms and offers white‑glove support throughout deployment.
image: https://nuclavis.com/wp-content/uploads/2024/12/nuclavis-logo-2024-1.svg
layout: provider
modified: '2026-10-28'
name: Nuclavis
nav: Providers
network: true
overview: 'Nuclavis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fundraising, Mobile, Nonprofit, P2P, and Messaging.


  Nuclavis'' developer surface includes changelog, signup flow, getting-started guide, support, and 7 more developer resources.'
random_paper: 5
scopes:
- name: Nuclavis Scopes
  scope_count: 0
  slug: nuclavis-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 21.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Nuclavis Authentication
  slug: nuclavis-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Nuclavis Domain Security
  slug: nuclavis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nuclavis
tags:
- Fundraising
- Mobile
- Nonprofit
- P2P
- Messaging
website: https://nuclavis.com/
---
