---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/heycanopy-com/hosts/heycanopy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/heycanopy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/heycanopy-com/vendors/heycanopy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/heycanopy-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.heycanopy.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://help.heycanopy.com/en_US/account-setup/can-i-invest-on-canopy-as-a-non-us-investor
- group: docs
  title: ''
  type: Documentation
  url: https://help.heycanopy.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HeyCanopy
- group: auth
  href: https://artifacts.apis.io/heycanopy-com/security/heycanopy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heycanopy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://heycanopy.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://help.heycanopy.com/mcp
  - status: 200
    url: https://heycanopy.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Canopy provides investment fund infrastructure solutions, offering tools and services for fund managers to streamline operations, reporting, and compliance. The platform focuses on modernizing the financial services workflow with APIs that enable data integration, portfolio management, and investor communications. It aims to serve both emerging and established funds, enhancing efficiency and transparency across the investment lifecycle.
image: https://cdn.prod.website-files.com/61c1c0b4e368108c5ab02f30/62385d67c46d9a32873c39aa_canopy_dark.png
layout: provider
modified: '2026-10-25'
name: Canopy
nav: Providers
network: true
overview: 'Canopy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Investment Fund Infrastructure, Private Equity, Fundraising Software, and Capital Deployment.


  Canopy''s developer surface includes getting-started guide, documentation, and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 39.3
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Heycanopy Com Domain Security
  slug: heycanopy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: heycanopy-com
tags:
- Investment Fund Infrastructure
- Private Equity
- Fundraising Software
- Capital Deployment
website: https://heycanopy.com
---
