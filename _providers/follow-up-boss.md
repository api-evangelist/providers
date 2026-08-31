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
  score: 21.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Follow Up Boss Agentic Access
  operation_count: 37
  slug: follow-up-boss-agentic-access
  summary_line: 37 operations · 20 acting
api_count: 1
apis:
- description: REST API for managing real estate leads, contacts, deals, notes, tasks, calls, text messages, events, and webhooks in Follow Up Boss. Authenticated with HTTP Basic using an API key issued from the Fol
  name: Follow Up Boss API
  slug: rest-api
- description: The Calls API from Follow Up Boss — 2 operation(s) for calls.
  name: Follow Up Boss Calls API
  slug: follow-up-boss-calls-api
- description: The Deals API from Follow Up Boss — 2 operation(s) for deals.
  name: Follow Up Boss Deals API
  slug: follow-up-boss-deals-api
- description: The Events API from Follow Up Boss — 2 operation(s) for events.
  name: Follow Up Boss Events API
  slug: follow-up-boss-events-api
- description: The Notes API from Follow Up Boss — 2 operation(s) for notes.
  name: Follow Up Boss Notes API
  slug: follow-up-boss-notes-api
- description: The People API from Follow Up Boss — 5 operation(s) for people.
  name: Follow Up Boss People API
  slug: follow-up-boss-people-api
- description: The Tasks API from Follow Up Boss — 2 operation(s) for tasks.
  name: Follow Up Boss Tasks API
  slug: follow-up-boss-tasks-api
- description: The TextMessages API from Follow Up Boss — 2 operation(s) for textmessages.
  name: Follow Up Boss TextMessages API
  slug: follow-up-boss-textmessages-api
- description: The Webhooks API from Follow Up Boss — 2 operation(s) for webhooks.
  name: Follow Up Boss Webhooks API
  slug: follow-up-boss-webhooks-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Follow Up Boss Calls API
  slug: open-follow-up-boss-calls-api
- collection_type: open
  name: Follow Up Boss Calls Deals API
  slug: open-follow-up-boss-deals-api
- collection_type: open
  name: Follow Up Boss Calls Events API
  slug: open-follow-up-boss-events-api
- collection_type: open
  name: Follow Up Boss Calls Notes API
  slug: open-follow-up-boss-notes-api
- collection_type: open
  name: Follow Up Boss Calls People API
  slug: open-follow-up-boss-people-api
- collection_type: open
  name: Follow Up Boss Calls Tasks API
  slug: open-follow-up-boss-tasks-api
- collection_type: open
  name: Follow Up Boss Calls TextMessages API
  slug: open-follow-up-boss-textmessages-api
- collection_type: open
  name: Follow Up Boss Calls Webhooks API
  slug: open-follow-up-boss-webhooks-api
- collection_type: open
  name: Follow Up Boss API
  slug: open-follow-up-boss
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/follow-up-boss-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/follow-up-boss-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/follow-up-boss-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/follow-up-boss-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FollowUpBoss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/follow-up-boss
- group: company
  title: ''
  type: Website
  url: https://www.followupboss.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.followupboss.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.followupboss.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.followupboss.com/free-trial
- group: operate
  title: ''
  type: Support
  url: https://help.followupboss.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.followupboss.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.followupboss.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.followupboss.com/blog
created: '2026-05-11'
description: Follow Up Boss is a real estate CRM and lead management platform helping agents and teams capture leads from any source, automate follow-up via texts, emails, and calls, manage pipelines and deals, and track team performance. The Follow Up Boss REST API exposes resources such as people, notes, tasks, deals, calls, text messages, events, and webhooks, secured with HTTP Basic authentication using an API key obtained from the application's admin settings.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/follow-up-boss.png
layout: provider
modified: '2026-05-11'
name: Follow Up Boss
nav: Providers
network: true
overview: 'Follow Up Boss publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Deals API, Events API, and 5 more. Tagged areas include Real-Estate, CRM, Lead Management, Sales Automation, and Follow Up.


  Follow Up Boss'' developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 15.3
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 22.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/follow-up-boss/refs/heads/main/screenshots/follow-up-boss-2026-06-20T181354.png
security:
- kind: authentication
  name: Follow Up Boss Authentication
  slug: follow-up-boss-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Follow Up Boss Domain Security
  slug: follow-up-boss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Follow Up Boss Vulnerability Disclosure
  slug: follow-up-boss-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: follow-up-boss
tags:
- Real-Estate
- CRM
- Lead Management
- Sales Automation
- Follow Up
- Pipeline Management
website: https://www.followupboss.com
---
