---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: OAuth 2.0 protected REST API for managing CRM records, modules, users, workflows, notes, attachments, tags, and bulk data operations across the Zoho CRM platform.
  name: Zoho CRM REST API v8
  slug: rest-api-v8
- description: 'Instant Notifications API for Zoho CRM. Subscribers register a channel via POST /crm/v2/actions/watch with a notify_url and a list of module/operation events (for example Leads.create, Contacts.edit, '
  name: Zoho CRM Notifications API v2
  slug: notifications-api-v2
artifact_total: 7
asyncapis:
- description: AsyncAPI 2.6 specification for the Zoho CRM Notifications (Instant Notifications) API surface. Subscribers register a notify_url (channel) with Zoho CRM via the REST "actions/watch" endpoint and recei
  name: Zoho CRM Notifications API
  slug: zoho-crm-notifications-asyncapi
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-crm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-crm-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/zohocrm
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/crm/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/crm/developer/docs/api/v8/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zoho.com/crm/developer/
- group: start
  title: ''
  type: Signup
  url: https://www.zoho.com/crm/signup.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/crm/zohocrm-pricing.html
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/zohocrmdevelopers/zoho-crm-developers/overview
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/crm/blog/feed/
created: '2026-05-11'
description: Zoho CRM is an AI-powered sales and customer relationship management platform from Zoho that helps businesses manage leads, contacts, accounts, deals, and customer engagement across multiple channels. The Zoho CRM REST API (currently at v8) uses OAuth 2.0 authorization-code flow and provides programmatic access to records, modules, users, workflows, analytics, and bulk data operations, with an OpenAPI specification published for the API.
graphqls:
- description: This is a conceptual GraphQL schema for Zoho CRM, derived from the Zoho CRM REST API v8. Zoho CRM is an AI-powered sales and customer relationship management platform that helps businesses manage lead
  name: Zoho CRM GraphQL Schema
  slug: zoho-crm-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-crm.png
layout: provider
modified: '2026-05-30'
name: Zoho CRM
nav: Providers
network: true
overview: 'Zoho CRM publishes 2 APIs on the [APIs.io](https://apis.io/) network: REST API v8 and Notifications API v2. Tagged areas include CRM, Sales, Customer Relationship Management, Marketing Automation, and Lead Management.


  The Zoho CRM catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Zoho CRM''s developer surface includes documentation, signup flow, pricing, engineering blog, and 7 more developer resources.'
random_paper: 15
rules:
- name: Zoho CRM API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: zoho-crm-asyncapi-spectral-rules
score:
  band: thin
  composite: 35.5
  delta: -2.7
  facets:
    commercial_clarity: 10.5
    contract_quality: 64.2
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 41.7
    operational_transparency: 5.3
  previous_composite: 38.2
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-crm/refs/heads/main/screenshots/zoho-crm-2026-06-20T201938.png
security:
- kind: domain-security
  name: Zoho Crm Domain Security
  slug: zoho-crm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Crm Vulnerability Disclosure
  slug: zoho-crm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-crm
tags:
- CRM
- Sales
- Customer Relationship Management
- Marketing Automation
- Lead Management
- Customer Engagement
website: https://www.zoho.com/crm/
---
