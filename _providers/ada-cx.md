---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: The Ada REST API is the unified v2 interface to the Ada AI customer service platform. It covers knowledge sources and articles, end users, conversations, integrations (Actions), data export, data comp
  name: Ada REST API
  slug: ada-rest-api
- description: Manage knowledge sources, articles, and tags that Ada's AI Agent uses to ground answers to customer questions.
  name: Ada Knowledge API
  slug: ada-knowledge-api
- description: Read and manage conversations handled by the Ada AI Agent across all supported channels.
  name: Ada Conversations API
  slug: ada-conversations-api
- description: Create, look up, and update end users (customers) along with their metadata for use by Ada's AI Agent and Actions.
  name: Ada End Users API
  slug: ada-end-users-api
- description: Configure and invoke Actions, the integration layer that lets the Ada AI Agent call external systems and APIs during a conversation.
  name: Ada Integrations (Actions) API
  slug: ada-integrations-api
- description: Export conversation, message, and analytics data from Ada to data warehouses and BI tooling.
  name: Ada Data Export API
  slug: ada-data-export-api
- description: Run data subject access requests, data deletion, and other compliance operations across the Ada platform.
  name: Ada Data Compliance API
  slug: ada-data-compliance-api
- description: Configure and consume webhooks that notify external systems of conversation lifecycle events and other platform activity.
  name: Ada Webhooks API
  slug: ada-webhooks-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ada-cx-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ada-cx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ada-cx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ada.cx/
- group: other
  title: ''
  type: Developer
  url: https://docs.ada.cx/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ada.cx/reference/introduction/overview
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.ada.cx/openapi.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.ada.cx/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ada.cx/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ada.support/
- group: operate
  title: ''
  type: Support
  url: https://www.ada.cx/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ada.cx/policy/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ada.cx/policy/terms-of-service/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ada-support/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ada.cx/changelog
created: '2026-05-23'
description: Ada (formerly Ada Support) is an AI customer service automation platform that resolves customer questions across chat, email, voice, and social channels using a generative AI agent grounded in a customer's knowledge sources. Ada exposes REST APIs for managing conversations, end users, knowledge sources and articles, integrations (Actions), data export, data compliance, and webhooks.
finops:
- name: Ada Cx Finops
  service_category: API
  slug: ada-cx-finops
graphqls:
- description: Ada CX is an AI agent platform for customer experience automation. The API covers AI agent configuration, conversation flows, knowledge sources, integrations, analytics, and voice/chat/email channel m
  name: Ada CX GraphQL API
  slug: ada-cx-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ada-cx.png
layout: provider
modified: '2026-05-23'
name: Ada
nav: Providers
network: true
overview: 'Ada publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include AI Agent, Automation, Chatbots, Conversational AI, and Customer Service.


  Ada''s developer surface includes documentation, engineering blog, pricing, support, changelog, and 10 more developer resources.'
plans:
- name: Ada Cx Plans Pricing
  plan_count: 1
  slug: ada-cx-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Ada Cx Rate Limits
  slug: ada-cx-rate-limits
score:
  band: thin
  composite: 40.7
  delta: -2.3
  facets:
    commercial_clarity: 68.4
    contract_quality: 43.2
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 43.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ada-cx/refs/heads/main/screenshots/ada-cx-2026-06-20T164455.png
security:
- kind: domain-security
  name: Ada Cx Domain Security
  slug: ada-cx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ada Cx Vulnerability Disclosure
  slug: ada-cx-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ada Cx Trust Center
  slug: ada-cx-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: ada-cx
tags:
- AI Agent
- Automation
- Chatbots
- Conversational AI
- Customer Service
- Customer Support
- CX
- Generative AI
- Knowledge
- Messaging
website: https://www.ada.cx/
---
