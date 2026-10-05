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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blacklane/refs/heads/main/security/blacklane-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/blacklane-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blacklane/refs/heads/main/llms/blacklane-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blacklane-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blacklane/refs/heads/main/well-known/blacklane-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blacklane-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blacklane/refs/heads/main/well-known/blacklane-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blacklane-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blacklane/refs/heads/main/well-known/blacklane-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blacklane-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blacklane/refs/heads/main/hosts/blacklane-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blacklane-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blacklane/refs/heads/main/vendors/blacklane-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blacklane-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blacklane.com/en/terms/
- group: operate
  title: ''
  type: Support
  url: https://help.blacklane.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blacklane.com/en/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.blacklane.com/en/press/coverage/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.blacklane.com/en/press/releases/
- group: company
  title: ''
  type: Blog
  url: https://www.blacklane.com/en/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.blacklane.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blacklane
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blacklane/refs/heads/main/security/blacklane-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blacklane-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blacklane/refs/heads/main/security/blacklane-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blacklane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blacklane.com
coverage:
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the API host.
  evidence:
  - status: 404
    url: https://api.blacklane.com/openapi.json
  - status: 404
    url: https://help.blacklane.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: Blacklane is a global chauffeur service offering on‑demand rides, hourly hires, and city‑to‑city journeys in over 64 countries. Founded in 2011, the company provides premium transportation for business travelers, corporate clients, and individuals, emphasizing punctuality, safety, and a seamless booking experience through its web platform and mobile apps. Blacklane’s services include airport transfers, hourly car service, and long‑distance trips, all backed by professional drivers and a commitment to sustainability and customer satisfaction.
layout: provider
modified: '2026-09-29'
name: Blacklane
nav: Providers
network: true
overview: 'Blacklane is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transportation, Ride Hailing, Chauffeur, and Business Travel.


  Blacklane''s developer surface includes support, changelog, engineering blog, documentation, and 14 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.6
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
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blacklane Domain Security
  slug: blacklane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blacklane Vulnerability Disclosure
  slug: blacklane-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: blacklane
tags:
- Company
- Transportation
- Ride Hailing
- Chauffeur
- Business Travel
- Global
website: https://www.blacklane.com
---
