---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-24'
api_count: 9
apis:
- description: Comprehensive set of REST APIs for managing conversations across messaging channels, including agent operations, consumer messaging, conversation history, and engagement events.
  name: LivePerson Conversational Cloud API
  slug: conversational-cloud-api
- description: Programmatic access to natural language understanding, intent recognition, and conversation classification capabilities of the LivePerson platform.
  name: LivePerson Intent Manager API
  slug: intent-manager-api
- description: APIs for designing, deploying, and managing chatbots and dialog flows built with LivePerson Conversation Builder.
  name: LivePerson Conversation Builder API
  slug: conversation-builder-api
- description: APIs for managing knowledge bases, articles, and AI-driven knowledge retrieval used by bots and agents in LivePerson conversations.
  name: LivePerson KnowledgeAI API
  slug: knowledgeai-api
- description: Real-time and historical operational metrics for messaging conversations, including queues, agent activity, and SLA performance.
  name: LivePerson Messaging Operations API
  slug: messaging-operations-api
- description: Bulk historical conversation analytics and data export API for offline analysis of LivePerson messaging activity.
  name: LivePerson Data Access API
  slug: data-access-api
- description: API for retrieving historical chat and messaging engagement records, including transcripts, attributes, and survey results.
  name: LivePerson Engagement History API
  slug: engagement-history-api
- description: Authentication API for obtaining bearer tokens for application and user access to the LivePerson Conversational Cloud APIs.
  name: LivePerson Login Service API
  slug: login-service-api
- description: Serverless platform for building, deploying, and invoking custom functions that extend LivePerson conversational workflows.
  name: LivePerson Functions
  slug: functions
artifact_total: 14
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/liveperson-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liveperson-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liveperson
- group: company
  title: ''
  type: Website
  url: https://www.liveperson.com
- group: start
  title: ''
  type: Portal
  url: https://developers.liveperson.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.liveperson.com/getting-started.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.liveperson.com/getting-started-with-liveperson-apis.html
- group: auth
  title: ''
  type: Authentication
  url: https://developers.liveperson.com/login-service-api-overview.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.liveperson.com/
- group: company
  title: ''
  type: Blog
  url: https://www.liveperson.com/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LivePersonInc
created: '2025-01-14'
description: LivePerson is a leading provider of conversational AI and digital customer engagement technology. Their platform enables enterprises to design, deploy, and manage AI-powered messaging, voice, and agent-assisted conversations across web, mobile, and social channels, with a comprehensive suite of REST APIs covering conversation orchestration, contact center management, reporting, messaging, and security.
finops:
- name: Liveperson Finops
  service_category: API
  slug: liveperson-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/liveperson.png
layout: provider
modified: '2026-04-28'
name: LivePerson
nav: Providers
network: true
overview: 'LivePerson publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Conversational AI, Customer Engagement, Messaging, Contact Center, and Bots.


  LivePerson''s developer surface includes developer portal, documentation, getting-started guide, authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Liveperson Plans Pricing
  plan_count: 3
  slug: liveperson-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Liveperson Rate Limits
  slug: liveperson-rate-limits
score:
  band: emerging
  composite: 18.8
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 18.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liveperson/refs/heads/main/screenshots/liveperson-2026-06-20T184616.png
security:
- kind: domain-security
  name: Liveperson Domain Security
  slug: liveperson-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Liveperson Trust Center
  slug: liveperson-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: liveperson
tags:
- Conversational AI
- Customer Engagement
- Messaging
- Contact Center
- Bots
- Chat
website: https://www.liveperson.com
---
