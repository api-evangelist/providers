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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Restheart Webhooks
  slug: restheart-webhooks
common:
- group: design
  href: https://artifacts.apis.io/restheart/asyncapi/restheart-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/restheart-webhooks.yml
- group: design
  href: https://artifacts.apis.io/restheart/conventions/restheart-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/restheart-conventions.yml
- group: design
  href: https://artifacts.apis.io/restheart/conventions/restheart-conventions.yml
  title: ''
  type: Conventions
  url: conventions/restheart-conventions.yml
- group: auth
  href: https://artifacts.apis.io/restheart/authentication/restheart-authentication.yml
  title: ''
  type: Authentication
  url: authentication/restheart-authentication.yml
- group: other
  href: https://artifacts.apis.io/restheart/hosts/restheart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/restheart-hosts.yml
- group: other
  href: https://artifacts.apis.io/restheart/vendors/restheart-vendors.yml
  title: ''
  type: Vendors
  url: vendors/restheart-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://restheart.org/docs/stripe/plans-and-seats
- group: docs
  title: ''
  type: APIReference
  url: https://restheart.org/docs/reference/blog-posts
- group: start
  title: ''
  type: GettingStarted
  url: https://restheart.org/docs/foundations/quick-start
- group: auth
  href: https://artifacts.apis.io/restheart/security/restheart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/restheart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://restheart.org/
- group: docs
  title: ''
  type: Documentation
  url: https://restheart.org/docs
- group: company
  title: ''
  type: Blog
  url: https://restheart.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SoftInstigate
- group: operate
  title: ''
  type: Support
  url: https://restheart.org/community
- group: start
  title: ''
  type: SignUp
  url: https://ulabase.com/signup?utm_source=restheart.org&utm_medium=home&utm_content=home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.softinstigate.com/en/privacy
coverage:
  checked: '2026-10-21'
  detail: Documentation is available but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found.
  evidence:
  - status: 200
    url: https://restheart.org/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: SoftInstigate, operating under the brand RestHeart, provides a high-performance, open-source, NoSQL database server built on MongoDB wire protocol. It enables developers to quickly deploy scalable, schema-less data stores with built-in REST, GraphQL, and WebSocket interfaces. The platform focuses on simplicity, performance, and extensibility, offering features such as authentication, role-based access control, and data validation. SoftInstigate aims to empower modern applications with flexible data management while reducing operational overhead.
image: https://restheart.org/images/restheart_social_preview_1200x630.png
layout: provider
modified: '2026-10-21'
name: SoftInstigate
nav: Providers
network: true
overview: 'SoftInstigate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Open Source, NoSQL, REST, and GraphQL.


  The SoftInstigate catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SoftInstigate''s developer surface includes authentication, pricing, API reference, getting-started guide, documentation, engineering blog, support, and 10 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 29.8
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 32.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/restheart/restheart-2026-11-03T142218.png
security:
- kind: authentication
  name: Restheart Authentication
  slug: restheart-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Restheart Domain Security
  slug: restheart-domain-security
  summary_line: TLSv1.3 · DMARC
slug: restheart
tags:
- Database
- Open Source
- NoSQL
- REST
- GraphQL
website: https://restheart.org/
---
