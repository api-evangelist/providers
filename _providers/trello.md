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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 53
  human_in_the_loop: 0
  name: Trello Agentic Access
  operation_count: 101
  slug: trello-agentic-access
  summary_line: 101 operations · 53 acting
api_count: 16
apis:
- description: The Trello Webhooks API allows developers to receive real-time notifications when changes occur on Trello models such as boards, lists, and cards. Rather than polling the REST API for updates, webhook
  name: Trello Webhooks API
  slug: webhooks-api
- description: Trello Power-Ups are a framework for extending and integrating with the Trello platform. Power-Ups allow developers to add custom functionality to Trello boards, including custom fields, board buttons
  name: Trello Power-Ups
  slug: power-ups
- description: Operations for retrieving and managing actions, which represent activity events that occur on Trello objects such as boards, lists, and cards.
  name: trello Actions API
  slug: trello-actions-api
- description: Operations for creating, retrieving, updating, and deleting boards, as well as managing board memberships, lists, cards, labels, and other board-level resources.
  name: trello Boards API
  slug: trello-boards-api
- description: Operations for creating, retrieving, updating, and deleting cards, including managing card attachments, checklists, comments, labels, members, and stickers.
  name: trello Cards API
  slug: trello-cards-api
- description: Operations for creating, retrieving, updating, and deleting checklists and their check items on cards.
  name: trello Checklists API
  slug: trello-checklists-api
- description: Operations for creating, retrieving, updating, and deleting custom field definitions and their values on boards and cards.
  name: trello CustomFields API
  slug: trello-customfields-api
- description: Operations for creating, retrieving, updating, and deleting labels on boards and cards.
  name: trello Labels API
  slug: trello-labels-api
- description: Operations for creating, retrieving, updating, and archiving lists on boards.
  name: trello Lists API
  slug: trello-lists-api
- description: Operations for retrieving and updating member profiles, boards, organizations, and notification settings.
  name: trello Members API
  slug: trello-members-api
- description: Operations for retrieving and managing member notifications about activity on boards, cards, and other Trello objects.
  name: trello Notifications API
  slug: trello-notifications-api
- description: Operations for creating, retrieving, updating, and deleting Trello workspaces (organizations), including managing workspace members and settings.
  name: trello Organizations API
  slug: trello-organizations-api
- description: Operations for managing Power-Up plugins, including listing, updating, and creating plugin marketplace listings.
  name: trello Plugins API
  slug: trello-plugins-api
- description: Operations for searching across Trello boards, cards, members, and organizations using query strings.
  name: trello Search API
  slug: trello-search-api
- description: Operations for retrieving and deleting API tokens and their associated webhooks.
  name: trello Tokens API
  slug: trello-tokens-api
- description: Operations for creating, retrieving, updating, and deleting webhooks that deliver real-time notifications when Trello models change.
  name: trello Webhooks API
  slug: trello-webhooks-api
artifact_total: 52
asyncapis:
- description: The Trello Webhooks API delivers real-time notifications when changes occur on Trello models such as boards, lists, cards, and members. Rather than polling the REST API for updates, webhooks push even
  name: Trello Webhooks Events
  slug: trello-webhooks-asyncapi
collections:
- collection_type: open
  name: Trello REST API
  slug: open-trello-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trello-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trello-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trello-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trello-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trello-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trello
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atlassian
- group: design
  title: ''
  type: JSONLD
  url: json-ld/trello-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trello-board-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trello-card-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trello-webhook-payload-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/trello-board-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/trello-card-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/trello-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trello-vocabulary.yml
description: Trello is a web-based, kanban-style, list-making application that allows users to organize tasks, projects, and workflows using boards, lists, and cards.
features:
- 'Free: up to 10 boards per workspace, unlimited cards'
- 'Standard at $5/user/mo: unlimited boards, AI quick capture, custom fields'
- 'Premium at $10/user/mo: AI, multiple views (Timeline/Calendar/Table)'
- 'Enterprise at $17.50/user/mo: org-wide permissions, SSO via Atlassian Guard'
- REST API at api.trello.com/1
- 'Per API key: 300 req/10s'
- 'Per token: 100 req/10s'
- 'Search: 50 req/min'
- 'Webhook deliveries: 600 events/min'
- Power-Ups for board extensions
- Butler automation (rules, buttons, scheduled commands)
- Card mirroring (Standard+)
- OAuth 1.0a + API key/token
- Webhooks for board, list, card, member events
- Atlassian-owned (Confluence/Jira ecosystem)
- iOS, Android, desktop apps
finops:
- name: Trello Finops
  service_category: Kanban / Project Management
  slug: trello-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Trello API. Trello exposes a REST API at `https://api.trello.com/1/` with key/token authentication. This GraphQL schema maps the core Trello
  name: Trello GraphQL Schema
  slug: trello-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trello.png
json_schemas:
- name: Trello Board
  property_count: 17
  slug: trello-board
- name: Trello Card
  property_count: 24
  slug: trello-card
- name: Trello Webhook Payload
  property_count: 2
  slug: trello-webhook-payload
json_structures:
- name: Trello Board Structure
  property_count: 0
  slug: trello-board-structure
- name: Trello Card Structure
  property_count: 0
  slug: trello-card-structure
jsonld:
- class_count: 0
  name: Trello Context
  property_count: 13
  slug: trello-context
layout: provider
modified: '2026-05-19'
name: trello
nav: Providers
network: true
overview: 'trello publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Actions API, Boards API, and 12 more.


  The trello catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  trello''s developer surface includes authentication and 14 more developer resources.'
plans:
- name: Trello Plans Pricing
  plan_count: 4
  slug: trello-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 4
  name: Trello Rate Limits
  slug: trello-rate-limits
rules:
- name: trello API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: trello-asyncapi-spectral-rules
- name: trello API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: trello-jsonschema-spectral-rules
- name: trello API Rules
  rule_count: 20
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 14
  slug: trello-spectral-rules
score:
  band: thin
  composite: 39.1
  delta: -8.3
  facets:
    commercial_clarity: 23.7
    contract_quality: 76.7
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 52.1
    operational_transparency: 13.2
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/trello/refs/heads/main/screenshots/trello-2026-06-20T195704.png
security:
- kind: authentication
  name: Trello Authentication
  slug: trello-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Trello Domain Security
  slug: trello-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Trello Vulnerability Disclosure
  slug: trello-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Trello Trust Center
  slug: trello-trust-center
  summary_line: FedRAMP
slug: trello
---
