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
- group: agent
  href: https://artifacts.apis.io/offdeal/llms/offdeal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/offdeal-llms.txt
- group: other
  href: https://artifacts.apis.io/offdeal/hosts/offdeal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/offdeal-hosts.yml
- group: other
  href: https://artifacts.apis.io/offdeal/vendors/offdeal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/offdeal-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://offdeal.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://offdeal.io/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://offdeal.io/news/offdeal-series-a-funding-radical-ventures-2025
- group: other
  title: ''
  type: Leadership
  url: https://offdeal.io/team
- group: company
  title: ''
  type: Blog
  url: https://offdeal.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OffDeal
- group: auth
  href: https://artifacts.apis.io/offdeal/security/offdeal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/offdeal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://offdeal.io
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.offdeal.io/openapi.json
  - status: 404
    url: https://api.offdeal.io/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: OffDeal is an investment bank focused on helping small businesses sell and exit. The platform offers free valuations, dedicated banker consultations, and matches sellers with qualified buyers to achieve top sale prices. Backed by Radical Ventures, OffDeal provides advisory services, M&A guidance, and a streamlined process for business owners seeking liquidity.
image: https://assets.offdeal.io/landing_og_default_20260918.png
layout: provider
modified: '2026-10-29'
name: OffDeal
nav: Providers
network: true
overview: 'OffDeal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, M&A, InvestmentBank, SmallBusiness, and Advisory.


  OffDeal''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 7
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
    discoverability: 51.8
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Offdeal Domain Security
  slug: offdeal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: offdeal
tags:
- Company
- M&A
- InvestmentBank
- SmallBusiness
- Advisory
website: https://offdeal.io
---
