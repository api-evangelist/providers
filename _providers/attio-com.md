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
- acting_count: 30
  human_in_the_loop: 0
  name: Attio Com Agentic Access
  operation_count: 54
  slug: attio-com-agentic-access
  summary_line: 54 operations · 30 acting
api_count: 12
apis:
- description: Typed fields defined on objects and lists, plus select options and statuses.
  name: Attio Attributes API
  slug: attio-com-attributes-api
- description: Comments within threads on records and list entries.
  name: Attio Comments API
  slug: attio-com-comments-api
- description: Entries within a list, referencing a parent record.
  name: Attio List Entries API
  slug: attio-com-list-entries-api
- description: Collections that model a process by referencing records.
  name: Attio Lists API
  slug: attio-com-lists-api
- description: Access token identification and introspection.
  name: Attio Meta API
  slug: attio-com-meta-api
- description: Free-form notes attached to records.
  name: Attio Notes API
  slug: attio-com-notes-api
- description: Top-level data model - people, companies, deals, and custom objects.
  name: Attio Objects API
  slug: attio-com-objects-api
- description: Individual records within an object, with CRUD, query, and upsert.
  name: Attio Records API
  slug: attio-com-records-api
- description: Actionable to-dos with deadlines and assignees.
  name: Attio Tasks API
  slug: attio-com-tasks-api
- description: Threads of comments on records and list entries.
  name: Attio Threads API
  slug: attio-com-threads-api
- description: Webhook subscriptions delivering signed HTTP callbacks on changes.
  name: Attio Webhooks API
  slug: attio-com-webhooks-api
- description: Human users belonging to the workspace.
  name: Attio Workspace Members API
  slug: attio-com-workspace-members-api
artifact_total: 19
collections:
- collection_type: open
  name: Attio REST API
  slug: open-attio-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/attio-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/attio-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/attio-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/attio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/attio
- group: company
  title: ''
  type: Website
  url: https://attio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.attio.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/attio-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/attio-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/attio-com-finops.yml
created: '2026-07-02'
description: Attio is an AI-native customer relationship management (CRM) platform built on a flexible object/attribute/record data model. The Attio REST API (base https://api.attio.com/v2) exposes that data model programmatically - objects, records, attributes, lists, list entries, notes, tasks, comments, threads, workspace members, and webhooks - letting teams sync data, build workflows, and extend the CRM.
finops:
- name: Attio Com Finops
  service_category: Business Applications
  slug: attio-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/attio-com.png
layout: provider
modified: '2026-07-02'
name: Attio
nav: Providers
network: true
overview: 'Attio publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Attributes API, Comments API, List Entries API, and 9 more. Tagged areas include CRM, Customer Relationship Management, AI, Sales, and Data Model.


  Attio''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Attio Com Plans Pricing
  plan_count: 4
  slug: attio-com-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 3
  name: Attio Com Rate Limits
  slug: attio-com-rate-limits
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.5
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Attio Com Authentication
  slug: attio-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Attio Com Domain Security
  slug: attio-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: attio-com
tags:
- CRM
- Customer Relationship Management
- AI
- Sales
- Data Model
- Objects and Records
website: https://attio.com/
---
