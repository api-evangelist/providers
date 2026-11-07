---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/citus-data/plans/citus-data-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/citus-data-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/citus-data/changelog/citus-data-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/citus-data-changelog.yml
- group: auth
  href: https://artifacts.apis.io/citus-data/well-known/citus-data-apis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citus-data-apis-security.txt
- group: agent
  href: https://artifacts.apis.io/citus-data/well-known/citus-data-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citus-data-well-known.yml
- group: other
  href: https://artifacts.apis.io/citus-data/hosts/citus-data-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citus-data-hosts.yml
- group: build
  href: https://artifacts.apis.io/citus-data/integrations/citus-data-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/citus-data-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/citus-data/vendors/citus-data-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citus-data-vendors.yml
- group: build
  href: https://artifacts.apis.io/citus-data/packages/citus-data-packages.yml
  title: ''
  type: SDKs
  url: packages/citus-data-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.citusdata.com/blog/tags/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.citusdata.com/newsroom/press/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.citusdata.com/en/v13.0/reference/common_errors.html
- group: company
  title: ''
  type: BlogRSS
  url: https://www.citusdata.com/feed.xml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/microsoft/
- group: auth
  href: https://artifacts.apis.io/citus-data/security/citus-data-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citus-data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.citusdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/postgresql/citus/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.citusdata.com/product/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.citusdata.com/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/citusdata
- group: company
  title: ''
  type: Blog
  url: https://www.citusdata.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.citusdata.com/support
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/citusdata/citus/blob/main/CHANGELOG.md
- group: other
  title: ''
  type: Download
  url: https://www.citusdata.com/download/
- group: build
  href: https://artifacts.apis.io/citus-data/packages/citus-data-packages.yml
  title: ''
  type: Packages
  url: packages/citus-data-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.citusdata.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.citusdata.com/privacy
- group: operate
  title: ''
  type: FAQ
  url: https://www.citusdata.com/faq
coverage:
  checked: '2026-11-05'
  detail: Citus is a PostgreSQL extension consumed over the Postgres wire protocol and SQL; citusdata.com and docs.citusdata.com publish no HTTP API, OpenAPI, llms.txt or MCP surface.
  evidence:
  - status: 200
    url: https://www.citusdata.com/
  - status: 404
    url: https://www.citusdata.com/llms.txt
  - status: 404
    url: https://docs.citusdata.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Citus Data is the company behind Citus, an open source extension that turns PostgreSQL into a distributed database. Rather than forking Postgres, Citus adds sharding, distributed tables, reference tables, and a distributed query planner so applications can scale out across many nodes while keeping full SQL, ACID transactions, and the entire Postgres ecosystem. It is used for multi-tenant SaaS applications, real-time analytics dashboards, and microservices architectures. Founded in San Francisco and acquired by Microsoft in 2019, Citus is developed in the open on GitHub and is also offered as a managed cloud service (Azure Cosmos DB for PostgreSQL); its reference documentation is hosted on Microsoft Learn. Citus is consumed over the standard PostgreSQL wire protocol and SQL, so it exposes no REST/HTTP API, no OAuth surface, and no language SDKs of its own.
image: https://avatars.githubusercontent.com/u/2545424?s=200&v=4
layout: provider
modified: '2026-11-05'
name: Citus Data
nav: Providers
network: true
overview: 'Citus Data is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PostgreSQL, Database, Distributed Database, and Sharding.


  Citus Data''s developer surface includes changelog, API reference, documentation, getting-started guide, engineering blog, support, pricing, and 20 more developer resources.'
plans:
- name: Citus Data Plans Pricing
  plan_count: 2
  slug: citus-data-plans-pricing
random_paper: 23
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.2
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 50.0
    operational_transparency: 28.9
  previous_composite: 13.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/citus-data/citus-data-2026-07-25T205430.png
security:
- kind: domain-security
  name: Citus Data Domain Security
  slug: citus-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citus-data
tags:
- Company
- PostgreSQL
- Database
- Distributed Database
- Sharding
- Open Source
- Scalability
- Analytics
- Microsoft
website: https://www.citusdata.com/
---
