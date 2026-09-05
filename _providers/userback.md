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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Userback Agentic Access
  operation_count: 8
  slug: userback-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- description: REST API for managing Userback feedback items, projects, users, tags, and account resources. Uses Bearer token authentication; partner integrations use an X-Partner-Code header.
  name: Userback REST API
  slug: rest-api
- baseURL: https://rest.userback.io/1.0
  baseurl_source: declared
  description: Feedback items captured by Userback widgets.
  name: Userback Feedback API
  slug: userback-feedback-api
- baseURL: https://rest.userback.io/1.0
  baseurl_source: declared
  description: Comments attached to feedback items.
  name: Userback Feedback Comments API
  slug: userback-feedback-comments-api
- baseURL: https://rest.userback.io/1.0
  baseurl_source: declared
  description: Userback projects (workspaces grouping feedback widgets).
  name: Userback Projects API
  slug: userback-projects-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Userback REST Feedback API
  slug: open-userback-feedback-api
- collection_type: open
  name: Userback REST Feedback Feedback Comments API
  slug: open-userback-feedback-comments-api
- collection_type: open
  name: Userback REST Feedback Projects API
  slug: open-userback-projects-api
- collection_type: open
  name: Userback REST API
  slug: open-userback
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/userback-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/userback-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/userback-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/userback
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/userback
- group: company
  title: ''
  type: Website
  url: https://www.userback.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.userback.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.userback.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.userback.io/signup
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.userback.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.userback.io/blog
created: '2026-05-11'
description: Userback is a customer feedback platform that captures visual feedback, screenshots, screen recordings, and bug reports directly from in-product widgets installed on websites and web applications. The platform offers feedback boards, session replays, and integrations with project management and developer tools to streamline customer-driven product development. Userback's REST API uses Bearer token authentication for managing feedback, projects, users, and account data.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/userback.png
layout: provider
modified: '2026-05-11'
name: Userback
nav: Providers
network: true
overview: 'Userback publishes 3 APIs on the [APIs.io](https://apis.io/) network: Feedback API, Feedback Comments API, and Projects API. Tagged areas include Customer Feedback, Bug Reporting, Visual Feedback, Session Replay, and Product Management.


  Userback''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 6 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 30.4
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
    contract_quality: 60.5
    developer_ergonomics: 13.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/userback/refs/heads/main/screenshots/userback-2026-06-20T200723.png
security:
- kind: authentication
  name: Userback Authentication
  slug: userback-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Userback Domain Security
  slug: userback-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: userback
tags:
- Customer Feedback
- Bug Reporting
- Visual Feedback
- Session Replay
- Product Management
- Software-as-a-Service
website: https://www.userback.io
---
