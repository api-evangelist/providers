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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/finazon/plans/finazon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/finazon-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/finazon/lifecycle/finazon-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/finazon-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/finazon/lifecycle/finazon-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/finazon-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/finazon/llms/finazon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/finazon-llms.txt
- group: auth
  href: https://artifacts.apis.io/finazon/well-known/finazon-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/finazon-www-security.txt
- group: auth
  href: https://artifacts.apis.io/finazon/well-known/finazon-ws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/finazon-ws-security.txt
- group: auth
  href: https://artifacts.apis.io/finazon/well-known/finazon-webservices-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/finazon-webservices-security.txt
- group: auth
  href: https://artifacts.apis.io/finazon/well-known/finazon-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/finazon-support-security.txt
- group: auth
  href: https://artifacts.apis.io/finazon/well-known/finazon-finazon-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/finazon-finazon-security.txt
- group: auth
  href: https://artifacts.apis.io/finazon/well-known/finazon-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/finazon-api-security.txt
- group: agent
  href: https://artifacts.apis.io/finazon/well-known/finazon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/finazon-well-known.yml
- group: other
  href: https://artifacts.apis.io/finazon/hosts/finazon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finazon-hosts.yml
- group: other
  href: https://artifacts.apis.io/finazon/vendors/finazon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/finazon-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://finazon.io/libraries
- group: operate
  title: ''
  type: ChangeLog
  url: https://finazon.io/docs/changelog
- group: auth
  href: https://artifacts.apis.io/finazon/security/finazon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finazon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finazon.io/
- group: docs
  title: ''
  type: Documentation
  url: https://finazon.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://finazon.io/docs/api/latest
- group: start
  title: ''
  type: GettingStarted
  url: https://finazon.io/docs/guides
- group: operate
  title: ''
  type: Support
  url: https://support.finazon.io/en/
- group: company
  title: ''
  type: Blog
  url: https://finazon.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/finazon-io
- group: commercial
  title: ''
  type: Pricing
  url: https://finazon.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://finazon.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finazon.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finazon.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://finazon.statuspage.io/
coverage:
  checked: '2026-10-20'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 301
    url: https://finazon.io/docs/api/latest
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Finazon is a marketplace for global financial data APIs, offering datasets covering stock prices, cryptocurrency, and more. It provides REST and WebSocket APIs, libraries, and add‑ons for developers to integrate financial data into applications. Finazon aims to simplify access to worldwide financial datasets through a unified platform, supporting various use cases from analytics to trading.
image: https://finazon.io/assets/images/default/default-meta-image.jpg
layout: provider
modified: '2026-10-20'
name: Finazon
nav: Providers
network: true
overview: 'Finazon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Data, Marketplace, and Datasets.


  Finazon''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Finazon Plans Pricing
  plan_count: 6
  slug: finazon-plans-pricing
random_paper: 13
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 39.3
    operational_transparency: 55.3
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
  name: Finazon Domain Security
  slug: finazon-domain-security
  summary_line: TLSv1.3 · DMARC
slug: finazon
tags:
- Company
- Financial Data
- Marketplace
- Datasets
website: https://finazon.io/
---
