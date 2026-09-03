---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Streak Agentic Access
  operation_count: 18
  slug: streak-agentic-access
  summary_line: 18 operations · 9 acting
api_count: 1
apis:
- description: RESTful API exposing CRUD access to pipelines, boxes (records), stages, custom fields, threads, tasks, files, comments, users, and teams in the Streak CRM. Authentication uses HTTP Basic Auth with the
  name: Streak REST API
  slug: rest-api
- baseURL: https://api.streak.com/api
  baseurl_source: declared
  description: The Boxes API from Streak — 2 operation(s) for boxes.
  name: Streak Boxes API
  slug: streak-boxes-api
- baseURL: https://api.streak.com/api
  baseurl_source: declared
  description: The Fields API from Streak — 1 operation(s) for fields.
  name: Streak Fields API
  slug: streak-fields-api
- baseURL: https://api.streak.com/api
  baseurl_source: declared
  description: The Newsfeed API from Streak — 1 operation(s) for newsfeed.
  name: Streak Newsfeed API
  slug: streak-newsfeed-api
- baseURL: https://api.streak.com/api
  baseurl_source: declared
  description: The Pipelines API from Streak — 2 operation(s) for pipelines.
  name: Streak Pipelines API
  slug: streak-pipelines-api
- baseURL: https://api.streak.com/api
  baseurl_source: declared
  description: The Stages API from Streak — 1 operation(s) for stages.
  name: Streak Stages API
  slug: streak-stages-api
- baseURL: https://api.streak.com/api
  baseurl_source: declared
  description: The Users API from Streak — 1 operation(s) for users.
  name: Streak Users API
  slug: streak-users-api
- baseURL: https://api.streak.com/api
  baseurl_source: declared
  description: The Webhooks API from Streak — 1 operation(s) for webhooks.
  name: Streak Webhooks API
  slug: streak-webhooks-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Streak REST Boxes API
  slug: open-streak-boxes-api
- collection_type: open
  name: Streak REST Boxes Fields API
  slug: open-streak-fields-api
- collection_type: open
  name: Streak REST Boxes Newsfeed API
  slug: open-streak-newsfeed-api
- collection_type: open
  name: Streak REST Boxes Pipelines API
  slug: open-streak-pipelines-api
- collection_type: open
  name: Streak REST Boxes Stages API
  slug: open-streak-stages-api
- collection_type: open
  name: Streak REST Boxes Users API
  slug: open-streak-users-api
- collection_type: open
  name: Streak REST Boxes Webhooks API
  slug: open-streak-webhooks-api
- collection_type: open
  name: Streak REST API
  slug: open-streak
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/streak-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/streak-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/streak-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/streak-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/streak-com
- group: company
  title: ''
  type: Website
  url: https://www.streak.com
- group: docs
  title: ''
  type: Documentation
  url: https://streak.readme.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.streak.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.streak.com/sign-up
- group: operate
  title: ''
  type: Support
  url: https://support.streak.com
- group: build
  title: ''
  type: Chrome Extension
  url: https://chromewebstore.google.com/detail/streak-crm-for-gmail/pnnfemgpilpdaojpnkjdgfgbnnjojfik
- group: agent
  title: ''
  type: LlmsText
  url: https://api.streak.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/streak-developer-blog
created: '2026-05-11'
description: Streak is a CRM that lives inside Gmail, turning the inbox into a pipeline management workspace for sales, hiring, support, fundraising, deal flow, and project tracking using pipelines, boxes, stages, and email tracking. The Streak API provides programmatic REST access to the core CRM data models including pipelines, boxes, stages, fields, threads, tasks, and teams. Authentication uses HTTP Basic Auth with the API key as the username.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/streak.png
layout: provider
modified: '2026-05-11'
name: Streak
nav: Providers
network: true
overview: 'Streak publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Boxes API, Fields API, Newsfeed API, and 4 more. Tagged areas include CRM, Sales, Gmail, Pipeline Management, and Email Tracking.


  Streak''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 7 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 29.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/streak/refs/heads/main/screenshots/streak-2026-06-20T194620.png
security:
- kind: authentication
  name: Streak Authentication
  slug: streak-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Streak Domain Security
  slug: streak-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Streak Vulnerability Disclosure
  slug: streak-vulnerability-disclosure
  summary_line: Hackerone
slug: streak
tags:
- CRM
- Sales
- Gmail
- Pipeline Management
- Email Tracking
- Productivity
- Small Business
- Workflows
website: https://www.streak.com
---
