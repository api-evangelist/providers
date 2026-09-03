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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Groove Agentic Access
  operation_count: 24
  slug: groove-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 1
apis:
- description: GraphQL API exposing conversations, messages, agents, contacts, mailboxes, tags, and knowledge base data through a single endpoint. Authentication uses a Bearer API key retrieved from Groove account s
  name: Groove GraphQL API v2
  slug: graphql-api
- description: Legacy REST API for managing customers, conversations, messages, mailboxes, agents, tags, and webhooks in Groove. Authentication uses a Bearer API key. The REST API is no longer actively developed; ne
  name: Groove REST API v1
  slug: rest-api-v1
- description: Groove's webhook surface delivered through the legacy REST API webhook subscription endpoint. Customers register destination URLs and event types via POST /v1/webhooks; Groove then POSTs JSON payloads
  name: Groove Webhooks
  slug: webhooks
- baseURL: https://api.groovehq.com/graphql
  baseurl_source: declared
  description: The Agents API from Groove — 2 operation(s) for agents.
  name: Groove Agents API
  slug: groove-agents-api
- baseURL: https://api.groovehq.com/graphql
  baseurl_source: declared
  description: The Attachments API from Groove — 1 operation(s) for attachments.
  name: Groove Attachments API
  slug: groove-attachments-api
- baseURL: https://api.groovehq.com/graphql
  baseurl_source: declared
  description: The Customers API from Groove — 2 operation(s) for customers.
  name: Groove Customers API
  slug: groove-customers-api
- baseURL: https://api.groovehq.com/graphql
  baseurl_source: declared
  description: The Folders API from Groove — 1 operation(s) for folders.
  name: Groove Folders API
  slug: groove-folders-api
- baseURL: https://api.groovehq.com/graphql
  baseurl_source: declared
  description: The Groups API from Groove — 2 operation(s) for groups.
  name: Groove Groups API
  slug: groove-groups-api
- baseURL: https://api.groovehq.com/graphql
  baseurl_source: declared
  description: The Mailboxes API from Groove — 1 operation(s) for mailboxes.
  name: Groove Mailboxes API
  slug: groove-mailboxes-api
- baseURL: https://api.groovehq.com/graphql
  baseurl_source: declared
  description: The Messages API from Groove — 2 operation(s) for messages.
  name: Groove Messages API
  slug: groove-messages-api
- baseURL: https://api.groovehq.com/graphql
  baseurl_source: declared
  description: The Tickets API from Groove — 4 operation(s) for tickets.
  name: Groove Tickets API
  slug: groove-tickets-api
- baseURL: https://api.groovehq.com/graphql
  baseurl_source: declared
  description: The Webhooks API from Groove — 2 operation(s) for webhooks.
  name: Groove Webhooks API
  slug: groove-webhooks-api
artifact_total: 29
asyncapis:
- description: AsyncAPI 2.6 description of Groove's webhook surface as documented for the legacy Groove REST API v1. Groove enables customers to register webhook subscriptions through `POST https://api.groovehq.com/
  name: Groove Webhooks
  slug: groove-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Groove REST API v1 Agents API
  slug: open-groove-agents-api
- collection_type: open
  name: Groove REST API v1 Agents Attachments API
  slug: open-groove-attachments-api
- collection_type: open
  name: Groove REST API v1 Agents Customers API
  slug: open-groove-customers-api
- collection_type: open
  name: Groove REST API v1 Agents Folders API
  slug: open-groove-folders-api
- collection_type: open
  name: Groove REST API v1 Agents Groups API
  slug: open-groove-groups-api
- collection_type: open
  name: Groove REST API v1 Agents Mailboxes API
  slug: open-groove-mailboxes-api
- collection_type: open
  name: Groove REST API v1 Agents Messages API
  slug: open-groove-messages-api
- collection_type: open
  name: Groove REST API v1 Agents Tickets API
  slug: open-groove-tickets-api
- collection_type: open
  name: Groove REST API v1 Agents Webhooks API
  slug: open-groove-webhooks-api
- collection_type: open
  name: Groove REST API v1
  slug: open-groove
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/groove-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/groove-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/groove-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.groovehq.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.groovehq.com
- group: docs
  title: ''
  type: Documentation
  url: https://doc.groovehq.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.groovehq.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.groovehq.com/signup
- group: company
  title: ''
  type: Blog
  url: https://www.groovehq.com/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/GrooveHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/groovehq
created: '2026-05-11'
description: Groove is a customer support helpdesk and shared inbox platform for small and midsize businesses that consolidates email, live chat, social, and knowledge base content into a single agent workspace with automations, collision detection, reporting, and SLAs. Groove also provides customer- facing knowledge bases and self-service portals. Developers can integrate via the v2 GraphQL API or the legacy v1 REST API, both authenticated with an API key obtained from account settings.
graphqls:
- description: GraphQL API exposing conversations, messages, agents, contacts, mailboxes, tags, and knowledge base data through a single endpoint. Authentication uses a Bearer API key retrieved from Groove account s
  name: Groove GraphQL API
  slug: groove-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groove.png
layout: provider
modified: '2026-05-30'
name: Groove
nav: Providers
network: true
overview: 'Groove publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Agents API, Attachments API, and 7 more. Tagged areas include Customer-Support, Help Desk, Shared Inbox, Knowledge Base, and Conversations.


  The Groove catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Groove''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, GitHub presence, and 5 more developer resources.'
random_paper: 7
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Groove API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: groove-asyncapi-spectral-rules
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 11.4
    contract_quality: 56.6
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 5.3
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/groove/refs/heads/main/screenshots/groove-2026-06-20T182412.png
security:
- kind: authentication
  name: Groove Authentication
  slug: groove-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Groove Domain Security
  slug: groove-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: groove
tags:
- Customer-Support
- Help Desk
- Shared Inbox
- Knowledge Base
- Conversations
- Live Chat
website: https://www.groovehq.com
---
