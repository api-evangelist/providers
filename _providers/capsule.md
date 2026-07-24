---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Capsule Agentic Access
  operation_count: 32
  slug: capsule-agentic-access
  summary_line: 32 operations · 14 acting
api_count: 4
apis:
- description: The Opportunities API from Capsule — 7 operation(s) for opportunities.
  name: Capsule Opportunities API
  slug: capsule-opportunities-api
- description: The Parties API from Capsule — 5 operation(s) for parties.
  name: Capsule Parties API
  slug: capsule-parties-api
- description: The Projects API from Capsule — 5 operation(s) for projects.
  name: Capsule Projects API
  slug: capsule-projects-api
- description: The Tasks API from Capsule — 2 operation(s) for tasks.
  name: Capsule Tasks API
  slug: capsule-tasks-api
artifact_total: 11
collections:
- collection_type: open
  name: Capsule CRM REST API
  slug: open-capsule
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/capsule-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capsule-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/capsule-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/capsulecrm
- group: company
  title: ''
  type: Website
  url: https://capsulecrm.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.capsulecrm.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://capsulecrm.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://capsulecrm.com/support
- group: company
  title: ''
  type: Blog
  url: https://capsulecrm.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capsulecrm.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capsulecrm.com/terms-of-service
created: '2025-01-01'
description: Capsule is a CRM and project-management platform for small and mid-sized businesses that unifies contacts, sales pipelines, tasks, cases, and projects. The Capsule REST API exposes parties (contacts and companies), opportunities, projects, tasks, cases, entries, tracks, and settings such as tags, pipelines, milestones, stages, and custom fields, with REST Hooks webhooks for event-driven integration.
finops:
- name: Capsule Finops
  service_category: API
  slug: capsule-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/capsule.png
layout: provider
modified: '2026-04-23'
name: Capsule
nav: Providers
network: true
overview: 'Capsule publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Opportunities API, Parties API, Projects API, and 1 more. Tagged areas include Contact Management, CRM, Custom Fields, Opportunities, and Pipelines.


  Capsule''s developer surface includes authentication, documentation, pricing, support, engineering blog, and 6 more developer resources.'
plans:
- name: Capsule Plans Pricing
  plan_count: 3
  slug: capsule-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Capsule Rate Limits
  slug: capsule-rate-limits
score:
  band: thin
  composite: 42.2
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 47.8
    developer_ergonomics: 26.1
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 42.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/capsule/refs/heads/main/screenshots/capsule-2026-06-20T173941.png
security:
- kind: authentication
  name: Capsule Authentication
  slug: capsule-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Capsule Domain Security
  slug: capsule-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: capsule
tags:
- Contact Management
- CRM
- Custom Fields
- Opportunities
- Pipelines
- Project Management
- REST
- Sales
- Tasks
- Webhooks
website: https://capsulecrm.com
---
