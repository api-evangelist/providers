---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 30
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering customer support, help desk, ticketing, knowledge base, and live chat APIs. Customer support platforms power the interfaces and back-office systems that companies use to receive, route, resolve, and learn from customer inquiries across email, chat, phone, social, and self-service channels. This collection includes traditional help desk and ticketing suites like Zendesk, Freshdesk, and Help Scout, conversational customer support platforms like Intercom and Front, enterprise service clouds from Salesforce, ServiceNow, and Microsoft, knowledge base and self-service systems, live chat and messaging platforms like Crisp, LiveChat, and Olark, and modern API-first support tools like Plain and Chatwoot.
examples:
- key_count: 14
  name: Support Kb Article Example
  slug: support-kb-article-example
- key_count: 13
  name: Support Ticket Example
  slug: support-ticket-example
features:
- description: Support APIs expose create, read, update, and resolve operations on tickets, cases, or conversations representing each customer inquiry, with status, priority, and assignment workflows.
  name: Ticket and Case Management
- description: Modern support platforms unify email, chat, social, SMS, and voice into a single conversation thread per customer, exposed through APIs that abstract the underlying channel.
  name: Omnichannel Conversation Threads
- description: Knowledge base APIs let teams publish, version, and search help articles that power customer self-service portals, in-product help, and AI deflection agents.
  name: Knowledge Base and Self-Service
- description: Service-level agreements, business hours, queues, and skills-based routing rules are exposed as configurable API resources that drive how tickets flow through support teams.
  name: SLA and Routing Policies
- description: Support APIs maintain customer contact and organization records that link conversations, ticket history, custom attributes, and integrations to CRM systems.
  name: Contact and Organization Records
- description: Reusable macros, event-driven triggers, and workflow automations are exposed as APIs so teams can codify common responses and resolution patterns.
  name: Macros, Triggers, and Automations
- description: Live chat APIs power real-time conversations between customers and agents through web, mobile, and messaging channel widgets with presence, typing, and file sharing primitives.
  name: Live Chat and Messaging
- description: Reporting APIs expose ticket volume, response and resolution times, agent productivity, and customer satisfaction (CSAT) scores for dashboards and warehouse export.
  name: Reporting and CSAT
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Market-leading customer support and ticketing suite with deep APIs for tickets, users, organizations, macros, triggers, and help center articles.
  name: Zendesk
- description: Conversational customer engagement platform with APIs for conversations, contacts, articles, and AI-powered Fin support automation.
  name: Intercom
- description: Freshworks' omnichannel customer support and ticketing platform with APIs for tickets, contacts, agents, and knowledge base solutions.
  name: Freshdesk
- description: Shared inbox and help desk platform designed for small and mid-market teams, with APIs for conversations, customers, mailboxes, and Docs articles.
  name: Help Scout
- description: Enterprise customer service platform built on the Salesforce CRM, with REST and SOAP APIs for cases, knowledge articles, entitlements, and omnichannel routing.
  name: Salesforce Service Cloud
- description: Enterprise service management platform with APIs covering customer service management, incident, problem, change, and knowledge management.
  name: ServiceNow
- description: Shared inbox and customer operations platform with APIs for conversations, contacts, comments, and team collaboration on customer email.
  name: Front
- description: Atlassian's incident communication platform with APIs to publish component status, incidents, scheduled maintenance, and subscriber notifications.
  name: Statuspage
json_schemas:
- name: SupportKnowledgeBaseArticle
  property_count: 14
  slug: support-kb-article
- name: SupportTicket
  property_count: 13
  slug: support-ticket
json_structures:
- name: Support Kb Article Structure
  property_count: 14
  slug: support-kb-article-structure
- name: Support Ticket Structure
  property_count: 13
  slug: support-ticket-structure
jsonld:
- class_count: 12
  name: Support Context
  property_count: 15
  slug: support-context
layout: provider
modified: '2026-05-19'
name: Support
nav: Providers
network: true
overview: 'Support is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Support, Help Desk, Ticketing, Knowledge Base, and Live Chat.


  The Support catalog on APIs.io includes 1 JSON-LD context.


  Support''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: support
tags:
- Customer Support
- Help Desk
- Ticketing
- Knowledge Base
- Live Chat
- Customer Service
use_cases:
- description: Companies use platforms like Zendesk, Freshdesk, and Help Scout to route customer email, chat, and social inquiries into a single ticket queue worked by a shared support team.
  name: Omnichannel Help Desk
- description: Platforms like Intercom and Crisp embed conversational support widgets directly in web and mobile products, blending live chat, chatbots, and help articles.
  name: In-Product Messaging and Customer Support
- description: Salesforce Service Cloud, ServiceNow, and Microsoft Dynamics 365 Customer Service handle enterprise-scale case management, integrated with CRM, field service, and back-office systems.
  name: Enterprise Customer Service
- description: Atlassian Statuspage and similar tools publish service status, incident timelines, and scheduled maintenance through APIs and customer-facing status pages.
  name: Status Communication and Incident Updates
- description: Document360, Archbee, and DeveloperHub power public and private help centers, customer documentation portals, and AI-searchable knowledge bases.
  name: Self-Service Knowledge Bases
- description: Gorgias, Kustomer, and Zendesk integrate deeply with Shopify, Stripe, and other commerce platforms so support agents see orders, refunds, and subscription state alongside each ticket.
  name: E-commerce and Subscription Support
- description: ServiceDesk Plus, SysAid, TOPdesk, and Spiceworks deliver IT service management (ITSM) workflows for employees raising IT, HR, and facilities requests.
  name: Internal IT Service Desk
website: https://apievangelist.com
---
