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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Qred API provides loan application and management endpoints as documented in the developer portal.
  name: Qred API
  slug: qred-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qred/refs/heads/main/hosts/qred-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qred-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qred/refs/heads/main/vendors/qred-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qred-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.qred.com/test/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qred.com/info/privacy-be
- group: company
  title: ''
  type: Newsroom
  url: https://www.qred.com/en-dk/press
- group: company
  title: ''
  type: Blog
  url: https://www.qred.com/en-dk/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://qred.com/docs/widget/getting_started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.qred.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qred
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qred/refs/heads/main/security/qred-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qred-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qred.com/
coverage:
  checked: '2026-10-15'
  detail: Developer portal pages are rendered by Docusaurus JavaScript and no OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://developers.qred.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Qred provides small business loans across multiple European markets, offering fast and flexible financing solutions for entrepreneurs. The platform operates under different brand names in various countries, such as Qeld in the Netherlands, and maintains a network of local sites like qred.se, qred.dk, qred.be, and others. Their services aim to simplify access to credit, supporting growth and development for small enterprises.
layout: provider
modified: '2026-10-15'
name: Qred
nav: Providers
network: true
overview: 'Qred is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Loans, SmallBusiness, and Europe.


  Qred''s developer surface includes support, engineering blog, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 55.4
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Qred Domain Security
  slug: qred-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: qred
tags:
- Company
- Finance
- Loans
- SmallBusiness
- Europe
website: https://qred.com/
---
