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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Decagon AI Agents Studio is the enterprise platform for authoring, deploying, testing, and operating AI agents using Agent Operating Procedures (AOPs) - natural-language workflows that drive agent beh
  name: Decagon AI Agents Studio
  slug: ai-agents-studio
artifact_total: 16
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/decagon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/decagon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decagon.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.decagon.ai
- group: company
  title: ''
  type: Blog
  url: https://decagon.ai/blog
- group: other
  title: ''
  type: Customers
  url: https://decagon.ai/customers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://decagon.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://decagon.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://decagon.ai/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/decagon-ai
- group: learn
  title: ''
  type: Training
  url: https://decagon.ai/university
- group: other
  title: ''
  type: Resources
  url: https://decagon.ai/resources
- group: docs
  title: ''
  type: Reference
  url: https://decagon.ai/glossary
- group: other
  title: ''
  type: Customers
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://decagon.ai/llms.txt
created: '2026-05-23'
description: Decagon is an enterprise AI customer service platform that builds and operates voice, chat, and email AI agents on top of natural-language Agent Operating Procedures (AOPs). The platform includes the AI Agents Studio for authoring agents, Watchtower for continuous quality assurance, Voice of the Customer analytics, A/B testing and simulations, and tool connectors for back-office integrations. Decagon is enterprise sales-led; its developer documentation is gated behind an access code and no self-serve public API is published.
features:
- description: Natural-language workflows that define agent behavior without complex configuration languages.
  name: Agent Operating Procedures (AOPs)
- description: Build, deploy, test, and optimize AI agents across voice, chat, and email channels.
  name: AI Agents Studio
- description: Natural-dialogue voice agents with brand customization.
  name: Voice AI Agents
- description: Continuous quality assurance for live agent conversations.
  name: Watchtower
- description: Analytics suite extracting insights from customer conversations.
  name: Voice of the Customer
- description: Testing and optimization tooling including multivariate testing and conversation simulations.
  name: A/B Testing & Simulations
- description: Integrations to back-office systems and knowledge bases for agent grounding.
  name: Tool Connectors
finops:
- name: Decagon Finops
  service_category: API
  slug: decagon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/decagon.png
layout: provider
modified: '2026-05-23'
name: Decagon
nav: Providers
network: true
overview: 'Decagon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, AI, Chat, Conversational AI, and Customer Experience.


  Decagon''s developer surface includes documentation, engineering blog, support, training material, and 10 more developer resources.'
plans:
- name: Decagon Plans Pricing
  plan_count: 1
  slug: decagon-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 2
  name: Decagon Rate Limits
  slug: decagon-rate-limits
score:
  band: emerging
  composite: 23.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 27.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/decagon/refs/heads/main/screenshots/decagon-2026-06-20T175849.png
security:
- kind: domain-security
  name: Decagon Domain Security
  slug: decagon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Decagon Vulnerability Disclosure
  slug: decagon-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: decagon
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
- description: Resolve customer support inquiries autonomously across voice, chat, and email.
  name: Customer Service Automation
- description: Replace traditional IVR with natural conversational voice agents.
  name: Voice IVR Replacement
- description: Surface customer insights and operational issues from conversation data.
  name: Conversation Intelligence
website: https://decagon.ai
---
