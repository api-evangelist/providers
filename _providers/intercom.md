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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Intercom Agentic Access
  operation_count: 18
  slug: intercom-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 9
apis:
- description: Workspace teammates and admin information.
  name: Intercom Admins API
  slug: intercom-admins-api
- description: Manage Help Center articles.
  name: Intercom Articles API
  slug: intercom-articles-api
- description: Manage company records associated with contacts.
  name: Intercom Companies API
  slug: intercom-companies-api
- description: Manage users and leads in your Intercom workspace.
  name: Intercom Contacts API
  slug: intercom-contacts-api
- description: Manage conversations between contacts and admins.
  name: Intercom Conversations API
  slug: intercom-conversations-api
- description: Submit and retrieve user activity events.
  name: Intercom Data Events API
  slug: intercom-data-events-api
- description: Send outbound messages from Intercom to contacts.
  name: Intercom Messages API
  slug: intercom-messages-api
- description: Manage news items in the Help Desk.
  name: Intercom News API
  slug: intercom-news-api
- description: Access user and company segments.
  name: Intercom Segments API
  slug: intercom-segments-api
artifact_total: 57
asyncapis:
- description: AsyncAPI description of Intercom's outbound webhook surface. Intercom delivers workspace events to a single subscriber URL configured per app under the Developer Hub > Webhooks settings. Each delivery
  name: Intercom Webhooks
  slug: intercom-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Intercom Admins API
  slug: open-intercom-admins-api
- collection_type: open
  name: Intercom Admins Articles API
  slug: open-intercom-articles-api
- collection_type: open
  name: Intercom Admins Companies API
  slug: open-intercom-companies-api
- collection_type: open
  name: Intercom Admins Contacts API
  slug: open-intercom-contacts-api
- collection_type: open
  name: Intercom Admins Conversations API
  slug: open-intercom-conversations-api
- collection_type: open
  name: Intercom Admins Data Events API
  slug: open-intercom-data-events-api
- collection_type: open
  name: Intercom Admins Messages API
  slug: open-intercom-messages-api
- collection_type: open
  name: Intercom Admins News API
  slug: open-intercom-news-api
- collection_type: open
  name: Intercom Admins Segments API
  slug: open-intercom-segments-api
- collection_type: open
  name: Intercom API
  slug: open-intercom
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/intercom-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/intercom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intercom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/intercom-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intercom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/intercom
- group: start
  title: ''
  type: Portal
  url: https://developers.intercom.com/
- group: company
  title: ''
  type: Website
  url: https://www.intercom.com/
- group: company
  title: ''
  type: Blog
  url: https://www.intercom.com/blog/feed/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.intercom.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://www.intercom.com/help/
- group: start
  title: ''
  type: Signup
  url: https://app.intercom.com/a/signup/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.intercom.com/llms.txt
created: '2024-07-02'
description: Intercom is an AI-powered customer service platform that enables businesses to build seamless customized experiences through its Help Desk and Messenger. The Intercom API allows developers to integrate with the Intercom platform using RESTful APIs and SDKs.
features:
- Essential at $29/seat/mo with Fin Customer Agent and Messenger
- Advanced at $85/seat/mo with workflows automation and 20 free Lite seats
- Expert at $132/seat/mo with SSO, HIPAA, SLAs, multibrand
- Fin AI Agent standalone at $0.99 per resolved outcome
- Pro AI add-on at $99/mo (CX Score, Topics, Custom Scorecards)
- Copilot AI add-on at $29/agent/mo
- Proactive Support Plus add-on at $99/mo
- REST API at ~166 req/10s (1000/min) standard, 33/10s search, 16/10s bulk
- Conversations, Contacts, Companies, Tickets, Articles APIs
- Webhooks for real-time event delivery
- Outbound messaging via Posts, Surveys, Tours
- SMS and WhatsApp campaigns (usage-based)
- Phone Plus voice support (usage-based)
- Knowledge base and AI-powered help center
- OAuth 2.0 and personal access tokens
- Apps Framework for marketplace and embedded apps
finops:
- name: Intercom Finops
  service_category: Customer Support
  slug: intercom-finops
graphqls:
- description: Intercom does not publish a public GraphQL API. Its developer platform is built entirely on REST. The GraphQL schema in this directory is a conceptual data model derived from the official Intercom RES
  name: Intercom GraphQL
  slug: intercom-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intercom.png
json_schemas:
- name: Admin
  property_count: 6
  slug: intercom-admin
- name: Article
  property_count: 9
  slug: intercom-article
- name: Company
  property_count: 8
  slug: intercom-company
- name: CompanyList
  property_count: 2
  slug: intercom-companylist
- name: Contact
  property_count: 9
  slug: intercom-contact
- name: ContactList
  property_count: 3
  slug: intercom-contactlist
- name: Conversation
  property_count: 8
  slug: intercom-conversation
- name: ConversationList
  property_count: 3
  slug: intercom-conversationlist
- name: Segment
  property_count: 6
  slug: intercom-segment
json_structures:
- name: Intercom Structure
  property_count: 0
  slug: intercom-structure
layout: provider
modified: '2026-05-30'
name: Intercom
nav: Providers
network: true
overview: 'Intercom publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Admins API, Articles API, Companies API, and 6 more. Tagged areas include AI, Customer Service, Customer Support, and Messaging.


  The Intercom catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Intercom''s developer surface includes authentication, developer portal, engineering blog, documentation, support, signup flow, and 7 more developer resources.'
plans:
- name: Intercom Plans Pricing
  plan_count: 4
  slug: intercom-plans-pricing
random_paper: 120
rate_limits:
- limit_count: 3
  name: Intercom Rate Limits
  slug: intercom-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Intercom API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: intercom-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Intercom API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: intercom-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.0
  delta: -4.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 11.4
    contract_quality: 66.5
    developer_ergonomics: 38.1
    discoverability: 72.2
    governance: 11.4
    operational_transparency: 10.5
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intercom/refs/heads/main/screenshots/intercom-2026-06-20T183440.png
security:
- kind: authentication
  name: Intercom Authentication
  slug: intercom-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Intercom Domain Security
  slug: intercom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Intercom Vulnerability Disclosure
  slug: intercom-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: intercom
tags:
- AI
- Customer Service
- Customer Support
- Messaging
website: https://www.intercom.com/
---
