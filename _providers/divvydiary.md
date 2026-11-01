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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/divvydiary/plans/divvydiary-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/divvydiary-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/divvydiary/hosts/divvydiary-hosts.yml
  title: ''
  type: Hosts
  url: hosts/divvydiary-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://divvydiary.com/help
- group: company
  title: ''
  type: Newsroom
  url: https://divvydiary.com/press
- group: start
  title: ''
  type: Login
  url: https://divvydiary.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/divvydiary
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.divvydiary.com/de/
- group: auth
  href: https://artifacts.apis.io/divvydiary/security/divvydiary-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/divvydiary-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://divvydiary.com/
- group: docs
  title: ''
  type: Documentation
  url: https://divvydiary.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://divvydiary.com/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://divvydiary.com/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://divvydiary.com/en/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://divvydiary.com/en/privacy
coverage:
  checked: '2026-10-27'
  detail: All probed spec URLs on api, dev, and research hosts returned redirects or 404, and no OpenAPI/AsyncAPI/GraphQL files were found.
  evidence:
  - status: 404
    url: https://api.divvydiary.com/openapi.json
  - status: 302
    url: https://dev.divvydiary.com/openapi.json
  - status: 301
    url: https://research.divvydiary.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: DivvyDiary provides a personal dividend calendar platform that helps investors track current and future dividend payments across global stocks and ETFs. Users can create portfolios, receive notifications, and visualize cash flow, while the service offers extensive data on dividend dates, amounts, and yields. The platform includes features such as calendar export, mobile alerts, and integration with financial tools, aiming to strengthen shareholder culture through transparent dividend tracking.
image: https://divvydiary.com/social.png
layout: provider
modified: '2026-10-27'
name: DivvyDiary
nav: Providers
network: true
overview: 'DivvyDiary is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Investment, Dividend, and Portfolio.


  DivvyDiary''s developer surface includes support, documentation, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Divvydiary Plans Pricing
  plan_count: 2
  slug: divvydiary-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 5.3
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
  name: Divvydiary Domain Security
  slug: divvydiary-domain-security
  summary_line: TLSv1.3 · DMARC
slug: divvydiary
tags:
- Company
- Finance
- Investment
- Dividend
- Portfolio
website: https://divvydiary.com/
---
