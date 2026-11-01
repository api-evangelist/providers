---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/diigo/authentication/diigo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/diigo-authentication.yml
- group: other
  href: https://artifacts.apis.io/diigo/hosts/diigo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diigo-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.diigo.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.diigo.com/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.diigo.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.diigo.com/press
- group: company
  title: ''
  type: Blog
  url: http://blog.diigo.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.diigo.com/educator-accounts/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.diigo.com/
- group: auth
  href: https://artifacts.apis.io/diigo/security/diigo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diigo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diigo.com/
coverage:
  checked: '2026-10-26'
  detail: Homepage returns a 200 but no machine‑readable API spec is published.
  evidence:
  - status: 403
    url: https://diigo.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: 'Diigo is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-26'
name: Diigo
nav: Providers
network: true
overview: 'Diigo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Diigo''s developer surface includes authentication, signup flow, engineering blog, getting-started guide, documentation, and 6 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 28.6
    operational_transparency: 0.0
  provenance:
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
  name: Diigo Authentication
  slug: diigo-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Diigo Domain Security
  slug: diigo-domain-security
  summary_line: TLSv1.3
slug: diigo
tags:
- Company
website: https://diigo.com/
---
