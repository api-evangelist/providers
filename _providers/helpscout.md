---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Helpscout Agentic Access
  operation_count: 17
  slug: helpscout-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 25
apis:
- description: Append customer replies, agent replies, internal notes, phone, chat, and forwards to an existing conversation as new threads.
  name: Help Scout Threads API
  slug: helpscout-threads-api
- description: Manage customer profiles including addresses, emails, phone numbers, chat handles, social profiles, websites, and properties.
  name: Help Scout Customers API
  slug: helpscout-customers-api
- description: Read mailbox / inbox configuration including routing settings, saved replies, custom fields, and folders.
  name: Help Scout Mailboxes API
  slug: helpscout-mailboxes-api
- description: Retrieve Help Scout user accounts (agents) including roles, permissions, and online/offline status.
  name: Help Scout Users API
  slug: helpscout-users-api
- description: Manage teams that group users for routing and assignment within shared inboxes.
  name: Help Scout Teams API
  slug: helpscout-teams-api
- description: List, create, and apply tags to conversations for categorization, automation, and reporting.
  name: Help Scout Tags API
  slug: helpscout-tags-api
- description: List automation workflows and trigger them manually against a conversation.
  name: Help Scout Workflows API
  slug: helpscout-workflows-api
- description: Read custom field definitions on inboxes and read / update custom field values on conversations.
  name: Help Scout Custom Fields API
  slug: helpscout-custom-fields-api
- description: Upload and download attachment data for conversation threads.
  name: Help Scout Attachments API
  slug: helpscout-attachments-api
- description: Read customer satisfaction ratings (great / okay / not good) attached to conversation threads.
  name: Help Scout Ratings API
  slug: helpscout-ratings-api
- description: Aggregated reports across company performance, conversations, happiness ratings, productivity, and user/team statistics.
  name: Help Scout Reports API
  slug: helpscout-reports-api
- description: Subscribe to Help Scout events (convo.created, convo.assigned, convo.tag, customer.created, rating.received) for downstream automation. Webhooks include HMAC signatures for verification.
  name: Help Scout Webhooks API
  slug: helpscout-webhooks-api
- description: Manage knowledge-base sites, collections, categories, articles, and search/related content for Help Scout Docs.
  name: Help Scout Docs API
  slug: helpscout-docs-api
- description: Embed Beacon (live chat, help docs, customer portal) into web and mobile applications and pre-fill or update Beacon context via the Beacon JS API.
  name: Help Scout Beacon API
  slug: helpscout-beacon-api
- description: Read and write live chat conversations and messages alongside the email Mailbox API for unified ticketing.
  name: Help Scout Chat API
  slug: helpscout-chat-api
- description: Build sidebar applications that render custom content within the Help Scout Inbox UI for partner integrations.
  name: Help Scout Apps API
  slug: helpscout-apps-api
- description: The Conversations API from Help Scout — 2 operation(s) for conversations.
  name: Help Scout Conversations API
  slug: helpscout-conversations-api
- description: The Customers API from Help Scout — 2 operation(s) for customers.
  name: Help Scout Customers API
  slug: helpscout-customers-api
- description: The Mailboxes API from Help Scout — 1 operation(s) for mailboxes.
  name: Help Scout Mailboxes API
  slug: helpscout-mailboxes-api
- description: The Tags API from Help Scout — 1 operation(s) for tags.
  name: Help Scout Tags API
  slug: helpscout-tags-api
- description: The Teams API from Help Scout — 1 operation(s) for teams.
  name: Help Scout Teams API
  slug: helpscout-teams-api
- description: The Threads API from Help Scout — 1 operation(s) for threads.
  name: Help Scout Threads API
  slug: helpscout-threads-api
- description: The Users API from Help Scout — 1 operation(s) for users.
  name: Help Scout Users API
  slug: helpscout-users-api
- description: The Webhooks API from Help Scout — 1 operation(s) for webhooks.
  name: Help Scout Webhooks API
  slug: helpscout-webhooks-api
- description: The Workflows API from Help Scout — 1 operation(s) for workflows.
  name: Help Scout Workflows API
  slug: helpscout-workflows-api
artifact_total: 66
asyncapis:
- description: 'Help Scout publishes webhook events from the Mailbox, Beacon, Docs, and organization surfaces to subscriber-configured URLs. Each delivery is an HTTP POST containing a JSON body, an X-HelpScout-Event '
  name: Help Scout Webhooks
  slug: helpscout-webhooks-asyncapi
collections:
- collection_type: postman
  name: Help Scout Mailbox Conversations API
  slug: postman-helpscout-conversations-api
- collection_type: postman
  name: Help Scout Mailbox Conversations Customers API
  slug: postman-helpscout-customers-api
- collection_type: postman
  name: Help Scout Mailbox Conversations Mailboxes API
  slug: postman-helpscout-mailboxes-api
- collection_type: postman
  name: Help Scout Mailbox Conversations Tags API
  slug: postman-helpscout-tags-api
- collection_type: postman
  name: Help Scout Mailbox Conversations Teams API
  slug: postman-helpscout-teams-api
- collection_type: postman
  name: Help Scout Mailbox Conversations Threads API
  slug: postman-helpscout-threads-api
- collection_type: postman
  name: Help Scout Mailbox Conversations Users API
  slug: postman-helpscout-users-api
- collection_type: postman
  name: Help Scout Mailbox Conversations Webhooks API
  slug: postman-helpscout-webhooks-api
- collection_type: postman
  name: Help Scout Mailbox Conversations Workflows API
  slug: postman-helpscout-workflows-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Help Scout Mailbox Conversations API
  slug: open-helpscout-conversations-api
- collection_type: open
  name: Help Scout Mailbox Conversations Customers API
  slug: open-helpscout-customers-api
- collection_type: open
  name: Help Scout Mailbox Conversations Mailboxes API
  slug: open-helpscout-mailboxes-api
- collection_type: open
  name: Help Scout Mailbox Conversations Tags API
  slug: open-helpscout-tags-api
- collection_type: open
  name: Help Scout Mailbox Conversations Teams API
  slug: open-helpscout-teams-api
- collection_type: open
  name: Help Scout Mailbox Conversations Threads API
  slug: open-helpscout-threads-api
- collection_type: open
  name: Help Scout Mailbox Conversations Users API
  slug: open-helpscout-users-api
- collection_type: open
  name: Help Scout Mailbox Conversations Webhooks API
  slug: open-helpscout-webhooks-api
- collection_type: open
  name: Help Scout Mailbox Conversations Workflows API
  slug: open-helpscout-workflows-api
- collection_type: open
  name: Help Scout Mailbox API
  slug: open-helpscout
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/help-scout/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/helpscout-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/helpscout-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helpscout-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/helpscout-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/helpscout-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/help-scout
- group: company
  title: ''
  type: Website
  url: https://www.helpscout.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.helpscout.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.helpscout.com/mailbox-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.helpscout.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://secure.helpscout.net/login/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.helpscout.com/
- group: company
  title: ''
  type: Blog
  url: https://www.helpscout.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.helpscout.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helpscout
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.helpscout.com/company/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.helpscout.com/company/legal/terms-of-service/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.helpscout.com/mailbox-api/overview/authentication/
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.helpscout.com/mailbox-api/overview/rate-limiting/
- group: design
  title: ''
  type: Webhooks
  url: https://developer.helpscout.com/webhooks/
- group: commercial
  title: ''
  type: Plans
  url: plans/helpscout-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/helpscout-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/helpscout-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.helpscout.com/llms.txt
created: '2026-05-08'
description: Help Scout is an email-first help desk platform with shared inboxes, live chat, knowledge bases, and a customer portal. The Help Scout APIs expose conversations, customers, inboxes, users, workflows, ratings, reports, Docs (knowledge base), Beacon (in-app messaging), and webhooks.
features:
- REST API at https://api.helpscout.net/v2 with OAuth 2 authentication
- JSON-only request/response format with HATEOAS resource links
- Free plan up to 5 users, 1 inbox, 1 Docs site
- Standard $25/user/mo, Plus $45/user/mo, Pro $75/user/mo (16% off annual)
- AI Answers add-on at $0.75 per resolution
- Additional inbox $10/month, additional Docs site $20/month
- Account-shared rate limit; write requests count double
- X-RateLimit-Limit-Minute / Remaining-Minute / Retry-After headers
- Webhooks with HMAC signatures
- PHP SDK and Laravel/Lumen adapter
finops:
- name: Helpscout Finops
  service_category: Customer Support
  slug: helpscout-finops
graphqls:
- description: This conceptual GraphQL schema models the Help Scout customer support and help desk platform. It covers the full surface of the Help Scout Mailbox API v2, Docs API, Beacon API, and webhooks. The schem
  name: Help Scout GraphQL Schema
  slug: helpscout-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/helpscout.png
layout: provider
modified: '2026-05-30'
name: Help Scout
nav: Providers
network: true
overview: 'Help Scout publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Threads API, Customers API, Mailboxes API, and 14 more. Tagged areas include Customer Support, Help Desk, Email, Live Chat, and Knowledge Base.


  The Help Scout catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Help Scout''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, and 19 more developer resources.'
plans:
- name: Helpscout Plans Pricing
  plan_count: 7
  slug: helpscout-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 3
  name: Helpscout Rate Limits
  slug: helpscout-rate-limits
rules:
- name: Help Scout API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: helpscout-asyncapi-spectral-rules
scopes:
- name: Helpscout Scopes
  scope_count: 0
  slug: helpscout-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.4
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 66.0
    developer_ergonomics: 37.0
    discoverability: 63.0
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/helpscout/refs/heads/main/screenshots/helpscout-2026-06-20T182635.png
security:
- kind: authentication
  name: Helpscout Authentication
  slug: helpscout-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Helpscout Domain Security
  slug: helpscout-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Helpscout Trust Center
  slug: helpscout-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: helpscout
tags:
- Customer Support
- Help Desk
- Email
- Live Chat
- Knowledge Base
- SaaS
website: https://www.helpscout.com/
---
