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
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Mozilla's unified authentication and user profile service.
  name: Firefox Accounts API
  slug: firefox-accounts-api
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/mozilla-accounts/well-known/mozilla-accounts-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mozilla-accounts-www-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.mozilla.org/en-US/security/bug-bounty/
- group: agent
  href: https://artifacts.apis.io/mozilla-accounts/well-known/mozilla-accounts-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mozilla-accounts-well-known.yml
- group: other
  href: https://artifacts.apis.io/mozilla-accounts/hosts/mozilla-accounts-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mozilla-accounts-hosts.yml
- group: other
  href: https://artifacts.apis.io/mozilla-accounts/vendors/mozilla-accounts-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mozilla-accounts-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mozilla-accounts/security/mozilla-accounts-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mozilla-accounts-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mozilla-accounts/security/mozilla-accounts-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mozilla-accounts-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accounts.firefox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/mozilla/fxa
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/mozilla/fxa/tree/main/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/mozilla/fxa#readme
- group: operate
  title: ''
  type: Support
  url: https://support.mozilla.org/en-US/products/firefox/accounts
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://accounts.firefox.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Mozilla Accounts (formerly Firefox Accounts) is Mozilla’s unified authentication and user profile service that powers Firefox Sync, Pocket, and other Mozilla products. It provides secure sign‑in, account recovery, and profile management via a set of public APIs. The service is open‑source, with its code hosted on GitHub, and its documentation is available in the repository and on Mozilla’s developer site.
layout: provider
modified: '2026-10-27'
name: Mozilla accounts
nav: Providers
network: true
overview: 'Mozilla accounts is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Authentication, Identity, Mozilla, and OpenSource.


  Mozilla accounts'' developer surface includes documentation, getting-started guide, support, and 9 more developer resources.'
random_paper: 13
scopes:
- name: Mozilla Accounts Scopes
  scope_count: 16
  slug: mozilla-accounts-scopes
  summary_line: 16 scopes
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 62.5
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mozilla Accounts Authentication
  slug: mozilla-accounts-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Mozilla Accounts Domain Security
  slug: mozilla-accounts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mozilla Accounts Vulnerability Disclosure
  slug: mozilla-accounts-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mozilla-accounts
tags:
- Company
- Authentication
- Identity
- Mozilla
- OpenSource
website: https://accounts.firefox.com/
---
