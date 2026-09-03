---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: 'SilverStripe''s GraphQL API provides a content API layer for getting data in and out of the CMS. It supports schema generation from DataObject models, custom types and queries, and extensible schemas. '
  name: SilverStripe GraphQL API
  slug: graphql-api
- description: SilverStripe provides REST API capabilities via the restfulserver module, allowing CRUD operations on DataObject models over HTTP. Authentication supports API token headers (x-api-token) and session-b
  name: SilverStripe REST API
  slug: rest-api
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/silverstripe/silverstripe-restfulserver/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/silverstripe/silverstripe-restfulserver/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/silverstripe/silverstripe-restfulserver/blob/3/code-of-conduct.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/silverstripe/.github/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/silverstripe/silverstripe-restfulserver/blob/3/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silverstripe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.silverstripe.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.silverstripe.org/
- group: docs
  title: ''
  type: APIReference
  url: https://api.silverstripe.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/silverstripe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/silverstripe/
- group: company
  title: ''
  type: Blog
  url: https://www.silverstripe.org/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.silverstripe.org/software/
- group: operate
  title: ''
  type: StatusPage
  url: https://github.com/silverstripe/platform-status-page
- group: other
  title: ''
  type: X
  url: https://twitter.com/silverstripe
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.silverstripe.org/en/6/changelogs/
- group: commercial
  title: ''
  type: Plans
  url: plans/silverstripe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/silverstripe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/silverstripe-finops.yml
created: '2026-06-13'
description: SilverStripe is an open-source PHP content management system and framework with a GraphQL and REST API for managing pages, assets, versioning, and custom data objects. It powers 50,000+ live sites and provides a flexible, extensible platform for developers to build content-driven web applications with enterprise-level security and an intuitive editing experience.
finops:
- name: Silverstripe Finops
  service_category: ''
  slug: silverstripe-finops
graphqls:
- description: SilverStripe CMS provides a GraphQL API via the optional `silverstripe/graphql` module. The schema is code-generated at build time from DataObject models configured in YAML. Types, queries, and mutati
  name: SilverStripe GraphQL API
  slug: silverstripe-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/silverstripe.png
layout: provider
modified: '2026-06-13'
name: SilverStripe
nav: Providers
network: true
overview: 'SilverStripe publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CMS, Content Management, GraphQL, REST API, and PHP.


  SilverStripe''s developer surface includes documentation, API reference, engineering blog, pricing, changelog, and 14 more developer resources.'
plans:
- name: Silverstripe Plans Pricing
  plan_count: 2
  slug: silverstripe-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Silverstripe Rate Limits
  slug: silverstripe-rate-limits
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 68.4
  open_source:
    applies: true
    score: 65.0
  previous_composite: 40.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/silverstripe/refs/heads/main/screenshots/silverstripe-2026-06-20T193925.png
security:
- kind: domain-security
  name: Silverstripe Domain Security
  slug: silverstripe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: silverstripe
tags:
- CMS
- Content Management
- GraphQL
- REST API
- PHP
- Open-Source
- Framework
- Pages
- Assets
- Versioning
website: https://www.silverstripe.org/
---
