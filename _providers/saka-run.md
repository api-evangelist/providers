---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Saka Run provides a prospecting API for local business data, documented at the developer portal.
  name: Saka Run API
  slug: saka-run-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/saka-run/llms/saka-run-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/saka-run-llms.txt
- group: auth
  href: https://artifacts.apis.io/saka-run/well-known/saka-run-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/saka-run-help-security.txt
- group: agent
  href: https://artifacts.apis.io/saka-run/well-known/saka-run-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/saka-run-well-known.yml
- group: other
  href: https://artifacts.apis.io/saka-run/hosts/saka-run-hosts.yml
  title: ''
  type: Hosts
  url: hosts/saka-run-hosts.yml
- group: other
  href: https://artifacts.apis.io/saka-run/vendors/saka-run-vendors.yml
  title: ''
  type: Vendors
  url: vendors/saka-run-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://saka.run/sandbox
- group: auth
  href: https://artifacts.apis.io/saka-run/security/saka-run-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/saka-run-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://saka.run/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://saka.run/developers
- group: docs
  title: ''
  type: Documentation
  url: https://saka.run/docs
- group: docs
  title: ''
  type: APIReference
  url: https://saka.run/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://saka.run/about
- group: operate
  title: ''
  type: Support
  url: https://saka.run/support
- group: company
  title: ''
  type: Blog
  url: https://saka.run/blog/build-an-ai-sdr
- group: commercial
  title: ''
  type: Pricing
  url: https://saka.run/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://saka.run/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://saka.run/privacy
- group: start
  title: ''
  type: SignUp
  url: https://sire-run-inc.getrewardful.com/signup
coverage:
  checked: '2026-10-30'
  detail: Provider documentation is HTML only and no OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://saka.run/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Saka-run provides local business prospect lists with source references, enabling agencies and freelancers to build targeted outreach lists. The platform offers industry and location based searches, preview of business details, and paid export of records with contact information. It emphasizes data quality, transparent sourcing, and flexible pricing for various business needs, positioning itself as a comprehensive solution for local market intelligence and prospecting.
image: https://saka.run/assets/business-records.png
layout: provider
modified: '2026-10-30'
name: saka-run
nav: Providers
network: true
overview: 'saka-run publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Prospecting, Marketing, and SaaS.


  saka-run''s developer surface includes sandbox, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 11 more developer resources.'
random_paper: 10
scopes:
- name: Saka Run Scopes
  scope_count: 0
  slug: saka-run-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 57.1
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Saka Run Authentication
  slug: saka-run-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Saka Run Domain Security
  slug: saka-run-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: balance
  slug: saka-run-balance
- name: purchase
  slug: saka-run-purchase
- name: quote
  slug: saka-run-quote
slug: saka-run
tags:
- Company
- Data
- Prospecting
- Marketing
- SaaS
website: https://saka.run/
---
