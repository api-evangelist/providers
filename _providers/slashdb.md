---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/slashdb/plans/slashdb-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/slashdb-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/slashdb/conventions/slashdb-conventions.yml
  title: ''
  type: Conventions
  url: conventions/slashdb-conventions.yml
- group: auth
  href: https://artifacts.apis.io/slashdb/authentication/slashdb-authentication.yml
  title: ''
  type: Authentication
  url: authentication/slashdb-authentication.yml
- group: other
  href: https://artifacts.apis.io/slashdb/hosts/slashdb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/slashdb-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.slashdb.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.slashdb.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.slashdb.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.slashdb.com/category/press/
- group: other
  title: ''
  type: Leadership
  url: https://www.slashdb.com/team/victor-olex/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SlashDB
- group: docs
  title: ''
  type: Documentation
  url: https://docs.slashdb.com/
- group: auth
  href: https://artifacts.apis.io/slashdb/security/slashdb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/slashdb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://slashdb.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://slashdb.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: VT Enterprise provides SlashDB, a tool that generates REST APIs for reading and writing to databases. It is offered to developers, enterprises, data scientists, data vendors, and systems integrators who need to connect databases to web and mobile applications, modernize legacy systems, and share data securely with clients and partners.
image: https://www.slashdb.com/wp-content/uploads/2015/08/slashdb-how-it-works.png
layout: provider
modified: '2026-10-21'
name: VT Enterprise
nav: Providers
network: true
overview: 'VT Enterprise is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include API, Data Integration, Low Code, Enterprise Software, and Database APIs.


  VT Enterprise''s developer surface includes authentication, pricing, documentation, and 10 more developer resources.'
plans:
- name: Slashdb Plans Pricing
  plan_count: 4
  slug: slashdb-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 51.8
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Slashdb Authentication
  slug: slashdb-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Slashdb Domain Security
  slug: slashdb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: slashdb
tags:
- API
- Data Integration
- Low Code
- Enterprise Software
- Database APIs
website: https://slashdb.com/
---
