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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/9spokes/hosts/9spokes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/9spokes-hosts.yml
- group: other
  href: https://artifacts.apis.io/9spokes/vendors/9spokes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/9spokes-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://9spokes.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://9spokes.com/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://9spokes.com/news
- group: company
  title: ''
  type: Blog
  url: https://9spokes.com/blogs/blog/building-with-banking-vs.-general-ledger-data
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/9spokes
- group: auth
  href: https://artifacts.apis.io/9spokes/security/9spokes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/9spokes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.9spokes.com/
coverage:
  checked: '2026-10-27'
  detail: No public developer documentation or API endpoints were found on the website.
  evidence:
  - status: 200
    url: https://9spokes.com
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: 9Spokes provides a SMB financial insights platform for banks and fintechs, turning SMB banking, cash‑flow, merchant and business‑app data into actionable analytics. The service helps financial institutions gain deeper visibility into small‑business customers, improve credit decisions, and enhance product offerings through data‑driven insights.
image: https://9spokes.com/hubfs/9S.png
layout: provider
modified: '2026-10-26'
name: 9Spokes
nav: Providers
network: true
overview: '9Spokes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, SMB, and DataAnalytics.


  9Spokes'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 11.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 9Spokes Domain Security
  slug: 9spokes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 9spokes
tags:
- Company
- Fintech
- Banking
- SMB
- DataAnalytics
website: https://www.9spokes.com/
---
