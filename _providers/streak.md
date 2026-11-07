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
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-11-06'
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
- baseURL: https://api.streak.com/api
  baseurl_source: declared
  description: The News Feed API from Streak — 1 operation(s) for news feed.
  name: Streak News Feed API
  slug: streak-news-feed-api
artifact_total: 22
collections:
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
- group: other
  href: https://artifacts.apis.io/streak/capabilities/streak-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/streak-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/streak/agentic-access/streak-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/streak-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/streak/security/streak-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/streak-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/streak/security/streak-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/streak-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/streak/authentication/streak-authentication.yml
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
mcp_servers:
- description: Remote MCP server at api.streak.com over HTTP.
  name: Streak MCP Server
  slug: streak
modified: '2026-05-11'
name: Streak
nav: Providers
network: true
overview: 'Streak publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Boxes API, Fields API, Pipelines API, and 5 more. Tagged areas include CRM, Sales, Gmail, Pipeline Management, and Email Tracking.


  The Streak catalog on APIs.io includes 1 Spectral governance ruleset.


  Streak''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Streak API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: streak-rules
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.2
  facets:
    access_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 48.7
    developer_ergonomics: 40.5
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/streak/streak-2026-06-20T194620.png
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
