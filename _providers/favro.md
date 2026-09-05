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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Public REST API for the Favro planning and collaboration platform: manage organizations, collections, widgets, columns, cards, tasks, tasklists, comments, tags, custom fields, groups, users, and webho'
  name: Favro API
  slug: favro-api
artifact_total: 5
asyncapis:
- description: ''
  name: Favro Webhooks
  slug: favro-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/favro-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.favro.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://favro.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://favro.com/developer
- group: company
  title: ''
  type: Blog
  url: https://www.favro.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.favro.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://favro.com/signup
- group: operate
  title: ''
  type: Support
  url: https://help.favro.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.favro.com/en/articles/1024895-favro-s-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.favro.com/en/articles/1019861-favro-s-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.favro.com
- group: auth
  title: ''
  type: Security
  url: https://www.favro.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.favro.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/favro-domain-security.yml
created: '2026-07-17'
description: Favro is a cloud planning and collaboration platform for agile teams, combining planning boards, backlogs, sprint/kanban widgets, roadmaps, and OKR/portfolio management in a single organization-scoped workspace. Its public REST API (https://favro.com/api/v1) exposes organizations, collections, widgets, columns, cards, tasks, tasklists, comments, tags, custom fields, groups, users, and webhooks, authenticated with HTTP Basic auth using an email plus a revocable API token. The API supports request-id cursor pagination, per-plan token-bucket rate limiting with X-RateLimit-* headers, backend-affinity routing via the X-Favro-Backend-Identifier header, outbound webhooks for card and comment events, and SCIM 1.1/2.0 user and group provisioning. Favro is SaaS, backed by Creandum.
image: https://cdn.prod.website-files.com/5eb8d3f3c300199312debf24/6036cf2c15bbbca169cec61a_meta2.png
layout: provider
modified: '2026-07-19'
name: Favro
nav: Providers
network: true
overview: 'Favro publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Project Management, Collaboration, and Agile.


  The Favro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Favro''s developer surface includes documentation, engineering blog, pricing, signup flow, support, and 9 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 45.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/favro/refs/heads/main/screenshots/favro-2026-07-25T214254.png
security:
- kind: authentication
  name: Favro Authentication
  slug: favro-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Favro Domain Security
  slug: favro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Favro Trust Center
  slug: favro-trust-center
  summary_line: ISO 27001, PCI DSS
slug: favro
tags:
- Company
- Software-as-a-Service
- Project Management
- Collaboration
- Agile
- Planning
- Task Management
- Kanban
- Productivity
website: https://www.favro.com/
---
