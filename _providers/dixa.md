---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 66
  human_in_the_loop: 0
  name: Dixa Agentic Access
  operation_count: 123
  slug: dixa-agentic-access
  summary_line: 123 operations · 66 acting
api_count: 20
apis:
- description: The Agents API from Dixa — 7 operation(s) for agents.
  name: Dixa Agents API
  slug: dixa-agents-api
- description: The Analytics API from Dixa — 5 operation(s) for analytics.
  name: Dixa Analytics API
  slug: dixa-analytics-api
- description: The Anonymization API from Dixa — 5 operation(s) for anonymization.
  name: Dixa Anonymization API
  slug: dixa-anonymization-api
- description: The Business Hours API from Dixa — 4 operation(s) for business hours.
  name: Dixa Business Hours API
  slug: dixa-business-hours-api
- description: The Chatbots API from Dixa — 13 operation(s) for chatbots.
  name: Dixa Chatbots API
  slug: dixa-chatbots-api
- description: The Contact Endpoints API from Dixa — 2 operation(s) for contact endpoints.
  name: Dixa Contact Endpoints API
  slug: dixa-contact-endpoints-api
- description: The Conversations API from Dixa — 27 operation(s) for conversations.
  name: Dixa Conversations API
  slug: dixa-conversations-api
- description: The Custom Attributes API from Dixa — 4 operation(s) for custom attributes.
  name: Dixa Custom Attributes API
  slug: dixa-custom-attributes-api
- description: The End Users API from Dixa — 6 operation(s) for end users.
  name: Dixa End Users API
  slug: dixa-end-users-api
- description: The Internal Notes API from Dixa — 2 operation(s) for internal notes.
  name: Dixa Internal Notes API
  slug: dixa-internal-notes-api
- description: The Knowledge API from Dixa — 16 operation(s) for knowledge.
  name: Dixa Knowledge API
  slug: dixa-knowledge-api
- description: The Messages API from Dixa — 2 operation(s) for messages.
  name: Dixa Messages API
  slug: dixa-messages-api
- description: The Organization API from Dixa — 1 operation(s) for organization.
  name: Dixa Organization API
  slug: dixa-organization-api
- description: The Queues API from Dixa — 5 operation(s) for queues.
  name: Dixa Queues API
  slug: dixa-queues-api
- description: The Ratings API from Dixa — 4 operation(s) for ratings.
  name: Dixa Ratings API
  slug: dixa-ratings-api
- description: The Search API from Dixa — 1 operation(s) for search.
  name: Dixa Search API
  slug: dixa-search-api
- description: The Tags API from Dixa — 7 operation(s) for tags.
  name: Dixa Tags API
  slug: dixa-tags-api
- description: The Teams API from Dixa — 4 operation(s) for teams.
  name: Dixa Teams API
  slug: dixa-teams-api
- description: The Templates API from Dixa — 2 operation(s) for templates.
  name: Dixa Templates API
  slug: dixa-templates-api
- description: The Webhooks API from Dixa — 4 operation(s) for webhooks.
  name: Dixa Webhooks API
  slug: dixa-webhooks-api
artifact_total: 43
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dixa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dixa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dixa-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.dixa.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dixa.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/dixa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dixa
- group: company
  title: ''
  type: Blog
  url: https://www.dixa.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dixa.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dixa.io
- group: other
  title: ''
  type: X
  url: https://twitter.com/dixaapp
- group: operate
  title: ''
  type: ChangeLog
  url: https://releases.dixa.help/en
- group: commercial
  title: ''
  type: Plans
  url: plans/dixa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dixa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dixa-finops.yml
created: '2026-06-13'
description: Dixa is a conversational customer service platform with a REST API for managing conversations, queues, agents, routing, knowledge base articles, and customer satisfaction data. The API enables developers to build automated workflows, integrate external data into routing logic, export conversations and activity logs, manage users and teams, and access omnichannel messaging across phone, email, chat, and social channels.
examples:
- key_count: 7
  name: Getagents
  slug: getAgents
- key_count: 7
  name: Getagentsagentid
  slug: getAgentsAgentid
- key_count: 7
  name: Getconversationsconversationid
  slug: getConversationsConversationid
- key_count: 7
  name: Getqueues
  slug: getQueues
- key_count: 7
  name: Gettags
  slug: getTags
- key_count: 7
  name: Getteams
  slug: getTeams
finops:
- name: Dixa Finops
  service_category: ''
  slug: dixa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dixa.png
json_schemas:
- name: Agent
  property_count: 12
  slug: agent
- name: Article
  property_count: 14
  slug: article
- name: Conversation
  property_count: 0
  slug: conversation
- name: EndUser
  property_count: 13
  slug: enduser
- name: Message
  property_count: 5
  slug: message
- name: Queue
  property_count: 2
  slug: queue
- name: Tag
  property_count: 4
  slug: tag
- name: Team
  property_count: 1
  slug: team
- name: WebhookSubscription
  property_count: 12
  slug: webhooksubscription
jsonld:
- class_count: 18
  name: Dixa Context
  property_count: 0
  slug: dixa-context
layout: provider
modified: '2026-06-13'
name: Dixa
nav: Providers
network: true
overview: 'Dixa publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Analytics API, Anonymization API, and 17 more. Tagged areas include Customer Service, Conversational, Omnichannel, CX, and Help Desk.


  The Dixa catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dixa''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 10 more developer resources.'
plans:
- name: Dixa Plans Pricing
  plan_count: 3
  slug: dixa-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 3
  name: Dixa Rate Limits
  slug: dixa-rate-limits
rules:
- name: Dixa API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dixa-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dixa/refs/heads/main/screenshots/dixa-2026-06-20T180054.png
security:
- kind: authentication
  name: Dixa Authentication
  slug: dixa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dixa Domain Security
  slug: dixa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dixa
tags:
- Customer Service
- Conversational
- Omnichannel
- CX
- Help Desk
- Chat
- Knowledge Base
website: https://www.dixa.com
---
