---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://beyourcover.com
  baseurl_source: declared
  description: Subscription credits and API capability discovery.
  name: BeYourCover Account API
  slug: beyourcover-com-account-api
- baseURL: https://beyourcover.com
  baseurl_source: declared
  description: The Books API from BeYourCover — 3 operation(s) for books.
  name: BeYourCover Books API
  slug: beyourcover-com-books-api
- baseURL: https://beyourcover.com
  baseurl_source: declared
  description: Agency client workspaces, as in the app's client panel.
  name: BeYourCover Clients API
  slug: beyourcover-com-clients-api
- baseURL: https://beyourcover.com
  baseurl_source: declared
  description: The Covers API from BeYourCover — 14 operation(s) for covers.
  name: BeYourCover Covers API
  slug: beyourcover-com-covers-api
- baseURL: https://beyourcover.com
  baseurl_source: declared
  description: The Jobs API from BeYourCover — 2 operation(s) for jobs.
  name: BeYourCover Jobs API
  slug: beyourcover-com-jobs-api
- baseURL: https://beyourcover.com
  baseurl_source: declared
  description: Unauthenticated service discovery and health. Linked from the RFC 9727 API catalog at `/.well-known/api-catalog`.
  name: BeYourCover Service API
  slug: beyourcover-com-service-api
- baseURL: https://beyourcover.com
  baseurl_source: declared
  description: The Templates API from BeYourCover — 1 operation(s) for templates.
  name: BeYourCover Templates API
  slug: beyourcover-com-templates-api
- baseURL: https://beyourcover.com
  baseurl_source: declared
  description: Full print wrap covers (back + spine + front). New wraps are Amazon KDP; a Barnes & Noble design made in the browser wrap editor can be listed, read and re-rendered.
  name: BeYourCover Wraps API
  slug: beyourcover-com-wraps-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/beyourcover-com/plans/beyourcover-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beyourcover-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/beyourcover-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/beyourcover-com/data-model/beyourcover-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beyourcover-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/beyourcover-com/authentication/beyourcover-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beyourcover-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/beyourcover-com/errors/beyourcover-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beyourcover-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/beyourcover-com/llms/beyourcover-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beyourcover-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/beyourcover-com/well-known/beyourcover-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beyourcover-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/beyourcover-com/hosts/beyourcover-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beyourcover-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/beyourcover-com/vendors/beyourcover-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beyourcover-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beyourcover.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beyourcover.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://beyourcover.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://beyourcover.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/beyourcover-com/security/beyourcover-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beyourcover-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beyourcover.com/
- group: docs
  title: ''
  type: Documentation
  url: https://beyourcover.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://beyourcover.com/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://beyourcover.com/#pricing
created: '2026-11-02'
description: BeYourCover is an AI-powered book cover generator designed for authors and publishers. It creates professional, genre‑perfect covers in seconds using smart AI analysis of your book information, simplifying the publishing process and helping you captivate readers with tailored designs.
image: https://beyourcover.com/opengraph-image.png?opengraph-image.2jt8t_upppv6e.png
layout: provider
modified: '2026-11-02'
name: BeYourCover
nav: Providers
network: true
overview: 'BeYourCover publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Books API, Clients API, and 5 more. Tagged areas include Company, Artificial Intelligence, BookCover, Design, and Publishing.


  BeYourCover''s developer surface includes authentication, engineering blog, getting-started guide, documentation, API reference, pricing, and 12 more developer resources.'
plans:
- name: Beyourcover Com Plans Pricing
  plan_count: 1
  slug: beyourcover-com-plans-pricing
random_paper: 9
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 49.8
    developer_ergonomics: 29.2
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Beyourcover Com Authentication
  slug: beyourcover-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Beyourcover Com Domain Security
  slug: beyourcover-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: beyourcover-com-create-and-render-wrap
  slug: beyourcover-com-create-and-render-wrap
- name: beyourcover-com-generate-and-retrieve-cover
  slug: beyourcover-com-generate-and-retrieve-cover
- name: beyourcover-com-manage-client-books
  slug: beyourcover-com-manage-client-books
slug: beyourcover-com
tags:
- Company
- Artificial Intelligence
- BookCover
- Design
- Publishing
website: https://beyourcover.com/
---
