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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Sierra Agent OS is the enterprise platform for building, deploying, and operating customer-facing AI agents. It includes Agent Studio, Ghostwriter, Insights, the Agent Data Platform, Voice Agents, and
  name: Sierra Agent OS
  slug: agent-os
artifact_total: 28
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
- group: start
  title: ''
  type: Portal
  url: https://sierra.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sierra.ai
- group: other
  title: ''
  type: Resources
  url: https://sierra.ai/resources
- group: company
  title: ''
  type: Careers
  url: https://sierra.ai/careers
- group: operate
  title: ''
  type: Contact
  url: https://sierra.ai/contact
- group: other
  title: ''
  type: Events
  url: https://sierra.ai/summit
- group: other
  title: ''
  type: X
  url: https://twitter.com/sierraplatform
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
modified: '2026-08-08'
name: Sierra
nav: Providers
network: true
overview: 'Sierra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, AI, Chat, Conversational AI, and Customer Experience.


  Sierra''s developer surface includes engineering blog, pricing, support, developer portal, documentation, and 15 more developer resources.'
plans:
- name: Sierra Plans Pricing
  plan_count: 1
  slug: sierra-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 2
  name: Sierra Rate Limits
  slug: sierra-rate-limits
score:
  band: emerging
  composite: 23.6
  delta: -8.4
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 32.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sierra/refs/heads/main/screenshots/sierra-2026-06-20T193901.png
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
solutions:
- description: Vertical solution for banks, fintechs, and lenders with compliance tooling and case templates.
  name: Financial Services
- description: HIPAA-aligned deployments for payers, providers, and digital health.
  name: Healthcare
- description: Carrier-grade agents for plan changes, troubleshooting, and retention.
  name: Telecommunications
- description: Subscription lifecycle and content support.
  name: Media and Subscriptions
- description: Booking, itinerary changes, and concierge experiences (Woodside Collection).
  name: Travel and Hospitality
- description: Pre-purchase, post-purchase, and loyalty agents.
  name: Retail
- description: Developer tools and SaaS support workflows.
  name: Technology
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
