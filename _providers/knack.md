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
    agentic_access: derived
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Knack Agentic Access
  operation_count: 6
  slug: knack-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- description: Resource-oriented REST API for managing records in Knack applications. Supports create, retrieve, update, and delete operations against specific objects or page views. All requests and responses use J
  name: Knack REST API
  slug: rest-api
- baseURL: https://api.knack.com/v1
  baseurl_source: declared
  description: CRUD operations on records via object endpoints
  name: Knack Object Records API
  slug: knack-object-records-api
- baseURL: https://api.knack.com/v1
  baseurl_source: declared
  description: Operations on records via page view endpoints
  name: Knack View Records API
  slug: knack-view-records-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Knack REST Object Records API
  slug: open-knack-object-records-api
- collection_type: open
  name: Knack REST Object Records View Records API
  slug: open-knack-view-records-api
- collection_type: open
  name: Knack REST API
  slug: open-knack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/knack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/knack-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knackhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/knackhq
- group: company
  title: ''
  type: Website
  url: https://www.knack.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knack.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.knack.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://dashboard.knack.com/sign-up
- group: operate
  title: ''
  type: Support
  url: https://support.knack.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.knack.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.knack.com/blog/feed/
created: '2026-05-11'
description: Knack is a no-code database and application platform that lets users build custom web applications from structured data without writing code. The platform combines a relational database, forms, search, charts, and user access controls with embeddable pages. Knack offers a resource-oriented REST API with predictable URLs for creating, retrieving, updating, and deleting records, authenticated via an Application ID and REST API key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/knack.png
layout: provider
modified: '2026-05-11'
name: Knack
nav: Providers
network: true
overview: 'Knack publishes 2 APIs on the [APIs.io](https://apis.io/) network: Object Records API and View Records API. Tagged areas include No-Code, Database, Application Builder, Low-Code, and Web Applications.


  Knack''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 6 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 58.2
    developer_ergonomics: 29.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knack/refs/heads/main/screenshots/knack-2026-06-20T184106.png
security:
- kind: authentication
  name: Knack Authentication
  slug: knack-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Knack Domain Security
  slug: knack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: knack
tags:
- No-Code
- Database
- Application Builder
- Low-Code
- Web Applications
website: https://www.knack.com
---
