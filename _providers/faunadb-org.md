---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: build
  href: https://artifacts.apis.io/faunadb-org/cli/faunadb-org-cli.yml
  title: ''
  type: CLI
  url: cli/faunadb-org-cli.yml
- group: operate
  href: https://artifacts.apis.io/faunadb-org/changelog/faunadb-org-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/faunadb-org-changelog.yml
- group: design
  href: https://artifacts.apis.io/faunadb-org/conventions/faunadb-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/faunadb-org-conventions.yml
- group: auth
  href: https://artifacts.apis.io/faunadb-org/authentication/faunadb-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/faunadb-org-authentication.yml
- group: operate
  href: https://artifacts.apis.io/faunadb-org/lifecycle/faunadb-org-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/faunadb-org-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/faunadb-org/lifecycle/faunadb-org-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/faunadb-org-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/faunadb-org/conformance/faunadb-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/faunadb-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/faunadb-org/llms/faunadb-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/faunadb-org-llms.txt
- group: other
  href: https://artifacts.apis.io/faunadb-org/hosts/faunadb-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/faunadb-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/faunadb-org/vendors/faunadb-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/faunadb-org-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fauna/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.faunadb.org/fauna/current/reference/fql/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.faunadb.org/fauna/current/get-started/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.faunadb.org/
- group: auth
  href: https://artifacts.apis.io/faunadb-org/security/faunadb-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/faunadb-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://faunadb.org/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://faunadb.org/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Fauna is a serverless cloud database platform that provides a globally distributed, transactional NoSQL database with built‑in security, authentication, and a powerful query language called FQL. It enables developers to build modern applications without managing infrastructure, offering features such as multi‑region replication, ACID transactions, and flexible data models. Fauna’s platform is designed for high scalability, low latency, and seamless integration with serverless functions and APIs, making it ideal for building real‑time, data‑intensive applications.
layout: provider
modified: '2026-10-22'
name: Fauna
nav: Providers
network: true
overview: 'Fauna is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Database, Serverless, NoSQL, and Cloud.


  Fauna''s developer surface includes CLI, changelog, authentication, API reference, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 51.8
    operational_transparency: 26.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.9
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/faunadb-org/faunadb-org-2026-11-03T131909.png
security:
- kind: authentication
  name: Faunadb Org Authentication
  slug: faunadb-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Faunadb Org Domain Security
  slug: faunadb-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: faunadb-org
tags:
- Company
- Database
- Serverless
- NoSQL
- Cloud
website: https://faunadb.org/
---
