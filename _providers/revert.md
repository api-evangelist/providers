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
- acting_count: 25
  human_in_the_loop: 0
  name: Revert Agentic Access
  operation_count: 51
  slug: revert-agentic-access
  summary_line: 51 operations · 25 acting
api_count: 13
apis:
- description: Unified accounting operations across Xero and QuickBooks
  name: Revert Accounting API
  slug: revert-accounting-api
- description: Unified chat operations across Slack, Microsoft Teams, and Discord
  name: Revert Chat API
  slug: revert-chat-api
- description: Manage third-party OAuth connections and webhooks
  name: Revert Connections API
  slug: revert-connections-api
- description: Unified CRM company/account operations
  name: Revert CRM Companies API
  slug: revert-crm-companies-api
- description: Unified CRM contact operations across Salesforce, HubSpot, Zoho, Pipedrive, and Close
  name: Revert CRM Contacts API
  slug: revert-crm-contacts-api
- description: Unified CRM deal/opportunity operations
  name: Revert CRM Deals API
  slug: revert-crm-deals-api
- description: Unified CRM event/activity operations
  name: Revert CRM Events API
  slug: revert-crm-events-api
- description: Unified CRM lead operations
  name: Revert CRM Leads API
  slug: revert-crm-leads-api
- description: Unified CRM note operations
  name: Revert CRM Notes API
  slug: revert-crm-notes-api
- description: Unified CRM custom property operations
  name: Revert CRM Properties API
  slug: revert-crm-properties-api
- description: Unified CRM task operations
  name: Revert CRM Tasks API
  slug: revert-crm-tasks-api
- description: Unified CRM user operations
  name: Revert CRM Users API
  slug: revert-crm-users-api
- description: Unified ticketing operations across Jira and Asana
  name: Revert Tickets API
  slug: revert-tickets-api
artifact_total: 27
collections:
- collection_type: open
  name: Revert Unified API
  slug: open-revert-unified-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revert-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revert-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.revert.dev/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/revertinc/revert
- group: docs
  title: ''
  type: Documentation
  url: https://docs.revert.dev
- group: auth
  title: ''
  type: Authentication
  url: https://docs.revert.dev
created: '2026-03-16'
description: Revert is an open-source unified API platform that makes it easy to build product integrations 10x faster. It provides a single standardized API to integrate with CRMs (Salesforce, HubSpot, Zoho CRM, Pipedrive, Close CRM), ticketing systems (Jira, Asana), accounting (Xero, QuickBooks), chat (Slack, Microsoft Teams, Discord), and more, with built-in OAuth management, token refresh, and retry logic.
examples:
- key_count: 2
  name: Revert Create Deal Example
  slug: revert-create-deal-example
- key_count: 2
  name: Revert Get Contacts Example
  slug: revert-get-contacts-example
finops:
- name: Revert Finops
  service_category: API
  slug: revert-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revert.png
json_schemas:
- name: Revert Unified CRM Contact
  property_count: 11
  slug: revert-contact
- name: Revert Unified CRM Deal
  property_count: 14
  slug: revert-deal
json_structures:
- name: Revert Contact Structure
  property_count: 0
  slug: revert-contact-structure
jsonld:
- class_count: 44
  name: Revert Context
  property_count: 0
  slug: revert-context
layout: provider
modified: '2026-05-19'
name: Revert
nav: Providers
network: true
overview: 'Revert publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Chat API, Connections API, and 10 more. Tagged areas include Integrations, CRM, Unified API, and Open Source.


  The Revert catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Revert''s developer surface includes authentication, GitHub presence, documentation, and 3 more developer resources.'
plans:
- name: Revert Plans Pricing
  plan_count: 3
  slug: revert-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Revert Rate Limits
  slug: revert-rate-limits
rules:
- name: Revert API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: revert-jsonschema-spectral-rules
- name: Revert API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 6
  slug: revert-rules
score:
  band: developing
  composite: 47.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 65.5
    developer_ergonomics: 19.6
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 47.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Revert Authentication
  slug: revert-authentication
  summary_line: apiKey · 1 scheme
slug: revert
tags:
- Integrations
- CRM
- Unified API
- Open Source
website: https://www.revert.dev/
---
