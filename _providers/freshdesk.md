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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Freshdesk Agentic Access
  operation_count: 82
  slug: freshdesk-agentic-access
  summary_line: 82 operations · 44 acting
api_count: 17
apis:
- description: The Freshdesk Webhook API enables real-time communication between Freshdesk and external systems by sending HTTP POST requests when specific events occur within the helpdesk. Webhooks can be triggered
  name: Freshdesk Webhook API
  slug: webhook-api
- description: 'The Freshdesk App SDK allows developers to build custom applications that extend the functionality of the Freshdesk helpdesk platform. Backed by a Platform-as-a-Service infrastructure that includes a '
  name: Freshdesk App SDK
  slug: app-sdk
- description: Manage support agents and their properties.
  name: freshdesk Agents API
  slug: freshdesk-agents-api
- description: Manage business hour schedules used in SLA calculations.
  name: freshdesk Business Hours API
  slug: freshdesk-business-hours-api
- description: Manage companies (organizations) associated with contacts.
  name: freshdesk Companies API
  slug: freshdesk-companies-api
- description: Manage contacts (end users) who submit support tickets.
  name: freshdesk Contacts API
  slug: freshdesk-contacts-api
- description: Manage replies, notes, and conversation threads on tickets.
  name: freshdesk Conversations API
  slug: freshdesk-conversations-api
- description: Manage email mailbox configurations for the helpdesk.
  name: freshdesk Email Configs API
  slug: freshdesk-email-configs-api
- description: Manage agent groups for ticket assignment and routing.
  name: freshdesk Groups API
  slug: freshdesk-groups-api
- description: Manage products to categorize tickets by product line.
  name: freshdesk Products API
  slug: freshdesk-products-api
- description: Manage roles that define agent permissions.
  name: freshdesk Roles API
  slug: freshdesk-roles-api
- description: View customer satisfaction survey ratings on tickets.
  name: freshdesk Satisfaction Ratings API
  slug: freshdesk-satisfaction-ratings-api
- description: Search across tickets, contacts, and companies using query syntax.
  name: freshdesk Search API
  slug: freshdesk-search-api
- description: Manage service level agreement policies for ticket response and resolution times.
  name: freshdesk SLA Policies API
  slug: freshdesk-sla-policies-api
- description: Manage knowledge base solution categories, folders, and articles.
  name: freshdesk Solutions API
  slug: freshdesk-solutions-api
- description: Manage support tickets including creation, updates, bulk operations, merging, and lifecycle management.
  name: freshdesk Tickets API
  slug: freshdesk-tickets-api
- description: Track time spent on tickets by agents.
  name: freshdesk Time Entries API
  slug: freshdesk-time-entries-api
artifact_total: 30
asyncapis:
- description: The Freshdesk Webhook API enables real-time communication between Freshdesk and external systems by sending HTTP POST requests when specific events occur within the helpdesk. Webhooks can be triggered
  name: Freshdesk Webhook Events
  slug: freshdesk-webhook-api-asyncapi
collections:
- collection_type: open
  name: Freshdesk REST API
  slug: open-freshdesk-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freshdesk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freshdesk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freshdesk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freshdesk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/freshdesk
- group: design
  title: ''
  type: JSONLD
  url: json-ld/freshdesk-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/freshdesk-ticket-schema.json
description: Freshdesk API.
finops:
- name: Freshdesk Finops
  service_category: Customer Support SaaS
  slug: freshdesk-finops
graphqls:
- description: Freshdesk is a customer support and helpdesk platform developed by Freshworks. It provides a REST API (v2) as its primary programmatic interface. Freshdesk does not offer a native public GraphQL endpo
  name: Freshdesk GraphQL API
  slug: freshdesk-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freshdesk.png
json_schemas:
- name: Freshdesk Ticket
  property_count: 29
  slug: freshdesk-ticket
jsonld:
- class_count: 0
  name: Freshdesk Context
  property_count: 8
  slug: freshdesk-context
layout: provider
modified: '2026-05-19'
name: freshdesk
nav: Providers
network: true
overview: 'freshdesk publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Webhook API, Agents API, Business Hours API, and 13 more.


  The freshdesk catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  freshdesk''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Freshdesk Plans Pricing
  plan_count: 5
  slug: freshdesk-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 7
  name: Freshdesk Rate Limits
  slug: freshdesk-rate-limits
rules:
- name: freshdesk API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: freshdesk-asyncapi-spectral-rules
- name: freshdesk API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: freshdesk-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.6
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 75.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freshdesk/refs/heads/main/screenshots/freshdesk-2026-06-20T181554.png
security:
- kind: authentication
  name: Freshdesk Authentication
  slug: freshdesk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Freshdesk Domain Security
  slug: freshdesk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freshdesk
---
