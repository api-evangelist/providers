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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Sierra Agent OS is the enterprise platform for building, deploying, and operating customer-facing AI agents. It includes Agent Studio, Ghostwriter, Insights, the Agent Data Platform, Voice Agents, and
  name: Sierra Agent OS
  slug: agent-os
artifact_total: 21
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sierra-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sierra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sierra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sierra.ai
- group: company
  title: ''
  type: Blog
  url: https://sierra.ai/blog
- group: other
  title: ''
  type: Customers
  url: https://sierra.ai/customers
- group: commercial
  title: ''
  type: Pricing
  url: https://sierra.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sierra.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sierra.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://sierra.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sierra-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sierra-ai
- group: start
  title: ''
  type: Login
  url: https://app.sierra.ai
- group: other
  title: ''
  type: Customers
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-23'
description: Sierra is an enterprise conversational AI platform co-founded by Bret Taylor that builds and operates customer-facing AI agents across chat, SMS, WhatsApp, email, voice, and ChatGPT. Its Agent OS includes Agent Studio for building agents, Ghostwriter for agent generation from SOPs and transcripts, Insights for analytics, an Agent Data Platform for personalization, Voice Agents, and Live Assist for human handoff. Sierra is enterprise sales-led with no self-serve public developer API; integrations and Agent SDK access are provisioned through customer engagements.
features:
- description: Dashboard for building, configuring, optimizing, and managing customer-facing AI agents.
  name: Agent Studio
- description: Agent-building agent that generates production-ready agents from SOPs, transcripts, or plain English descriptions.
  name: Ghostwriter
- description: Analytics suite covering conversation Explorer, proactive Monitors, multivariate Experiments, and tool-call Observability.
  name: Insights
- description: Integrates customer context, conversation history, and data warehouses for personalization.
  name: Agent Data Platform
- description: AI agents deployable across voice, chat, SMS, WhatsApp, email, and ChatGPT channels.
  name: Voice Agents
- description: Seamless escalation and human-in-the-loop handoff from AI agents to live customer service reps.
  name: Live Assist
finops:
- name: Sierra Finops
  service_category: API
  slug: sierra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sierra.png
integrations:
- description: Data connectivity and infrastructure partner.
  name: Google Cloud
- description: Data warehouse and ML platform connector for agent context.
  name: Databricks
- description: Data warehouse connector for the Agent Data Platform.
  name: Snowflake
- description: Real-time data and cache integration.
  name: Redis
- description: Cloud infrastructure and data connector.
  name: AWS
layout: provider
modified: '2026-05-23'
name: Sierra
nav: Providers
network: true
overview: 'Sierra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, AI, Chat, Conversational AI, and Customer Experience.


  Sierra''s developer surface includes engineering blog, pricing, support, and 10 more developer resources.'
plans:
- name: Sierra Plans Pricing
  plan_count: 1
  slug: sierra-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 2
  name: Sierra Rate Limits
  slug: sierra-rate-limits
score:
  band: thin
  composite: 30.6
  delta: 0.0
  facets:
    commercial_clarity: 89.5
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 30.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sierra/refs/heads/main/screenshots/sierra-2026-06-20T193900.png
security:
- kind: domain-security
  name: Sierra Domain Security
  slug: sierra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sierra Vulnerability Disclosure
  slug: sierra-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Sierra Trust Center
  slug: sierra-trust-center
  summary_line: PCI DSS, HIPAA
slug: sierra
tags:
- Agents
- AI
- Chat
- Conversational AI
- Customer Experience
- Customer Service
- Enterprise
- Voice
use_cases:
- description: Resolve customer support inquiries autonomously across channels.
  name: Customer Service Automation
- description: Replace traditional IVR with natural conversational voice agents.
  name: Voice IVR Replacement
- description: Reduce subscription cancellations through proactive agent engagement.
  name: Subscription Retention
website: https://sierra.ai
---
