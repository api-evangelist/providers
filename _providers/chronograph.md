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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Chronograph provides a developer API for portfolio monitoring and data management.
  name: Chronograph API
  slug: chronograph-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Blog
  url: https://www.chronograph.pe/category/blog/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.chronograph.pe/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chronograph/refs/heads/main/well-known/chronograph-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chronograph-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chronograph/refs/heads/main/well-known/chronograph-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chronograph-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chronograph/refs/heads/main/hosts/chronograph-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chronograph-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chronograph/refs/heads/main/vendors/chronograph-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chronograph-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chronograph.pe/
- group: company
  title: ''
  type: Newsroom
  url: https://www.chronograph.pe/category/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chronograph/refs/heads/main/security/chronograph-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/chronograph-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chronograph/refs/heads/main/security/chronograph-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chronograph-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chronograph.pe/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chronograph
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chronograph.pe/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/chronograph/workspace
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.chronograph.pe/
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Chronograph provides cloud‑based portfolio monitoring, analytics, data management and reporting solutions for private equity and other private capital investors. Their platform automates data collection, valuation, ESG tracking and API connectivity, enabling limited and general partners to streamline portfolio oversight and investor communications.
image: https://www.chronograph.pe/wp-content/uploads/2022/09/fahrul-azmi-XZc4f2XZc84-unsplash-1.jpg
layout: provider
modified: '2026-10-08'
name: Chronograph
nav: Providers
network: true
overview: 'Chronograph is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Private Equity, Portfolio-Monitoring, Analytics, and Data-Management.


  Chronograph''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chronograph Domain Security
  slug: chronograph-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Chronograph Trust Center
  slug: chronograph-trust-center
  summary_line: SOC 2
slug: chronograph
tags:
- Company
- Private Equity
- Portfolio-Monitoring
- Analytics
- Data-Management
website: https://www.chronograph.pe/
---
