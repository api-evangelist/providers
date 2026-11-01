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
- group: auth
  href: https://artifacts.apis.io/openlegacy-com/well-known/openlegacy-com-customer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/openlegacy-com-customer-security.txt
- group: agent
  href: https://artifacts.apis.io/openlegacy-com/well-known/openlegacy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/openlegacy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/openlegacy-com/hosts/openlegacy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openlegacy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/openlegacy-com/vendors/openlegacy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openlegacy-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openlegacy.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.openlegacy.com/company/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openlegacy.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.openlegacy.com/blog/plans-to-support-legacy-systems
- group: company
  title: ''
  type: Newsroom
  url: https://www.openlegacy.com/company/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.openlegacy.com/ja/company/management
- group: company
  title: ''
  type: Blog
  url: https://www.openlegacy.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openlegacy
- group: auth
  href: https://artifacts.apis.io/openlegacy-com/security/openlegacy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openlegacy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openlegacy.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://openlegacy.com/mcp
  - status: 200
    url: https://openlegacy.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: OpenLegacy provides an AI‑driven legacy modernization platform that enables enterprises to modernize, expose, and integrate legacy systems without rewriting code. Using low‑code tools, automated API generation, and cloud‑ready deployment, OpenLegacy helps organizations create secure, scalable APIs over mainframes, COBOL, and other legacy applications, accelerating digital transformation while preserving existing investments.
layout: provider
modified: '2026-10-21'
name: OpenLegacy
nav: Providers
network: true
overview: 'OpenLegacy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legacy Modernization, API Generation, Low-Code, and Cloud Integration.


  OpenLegacy''s developer surface includes support, pricing, engineering blog, and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Openlegacy Com Domain Security
  slug: openlegacy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openlegacy-com
tags:
- Company
- Legacy Modernization
- API Generation
- Low-Code
- Cloud Integration
website: https://openlegacy.com/
---
