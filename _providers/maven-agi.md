---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Maven Agi Agentic Access
  operation_count: 59
  slug: maven-agi-agentic-access
  summary_line: 59 operations · 46 acting
api_count: 9
apis:
- description: The Actions API from Maven AGI — 3 operation(s) for actions.
  name: Maven AGI Actions API
  slug: maven-agi-actions-api
- description: The Agents API from Maven AGI — 3 operation(s) for agents.
  name: Maven AGI Agents API
  slug: maven-agi-agents-api
- description: The Analytics API from Maven AGI — 4 operation(s) for analytics.
  name: Maven AGI Analytics API
  slug: maven-agi-analytics-api
- description: The App Settings API from Maven AGI — 2 operation(s) for app settings.
  name: Maven AGI App Settings API
  slug: maven-agi-app-settings-api
- description: The Conversations API from Maven AGI — 12 operation(s) for conversations.
  name: Maven AGI Conversations API
  slug: maven-agi-conversations-api
- description: The Events API from Maven AGI — 4 operation(s) for events.
  name: Maven AGI Events API
  slug: maven-agi-events-api
- description: The Knowledge API from Maven AGI — 12 operation(s) for knowledge.
  name: Maven AGI Knowledge API
  slug: maven-agi-knowledge-api
- description: The Triggers API from Maven AGI — 2 operation(s) for triggers.
  name: Maven AGI Triggers API
  slug: maven-agi-triggers-api
- description: The Users API from Maven AGI — 4 operation(s) for users.
  name: Maven AGI Users API
  slug: maven-agi-users-api
artifact_total: 17
collections:
- collection_type: open
  name: Maven AGI Platform API
  slug: open-maven-agi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/maven-agi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/maven-agi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maven-agi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maven-agi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mavenagi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mavenagi
- group: company
  title: ''
  type: Website
  url: https://www.mavenagi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mavenagi.com
- group: commercial
  title: ''
  type: Plans
  url: plans/maven-agi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/maven-agi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/maven-agi-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://mavenagi.com/resources
created: '2026-07-01'
description: Maven AGI is an enterprise AI agent platform for customer experience. Its AI agents answer questions, take actions, and improve with every interaction across chat, email, voice, and SMS. The Maven Platform API lets developers build apps that manage conversations, knowledge, actions, users, events, and triggers, authenticated with an App ID and App Secret scoped to an organization and agent.
finops:
- name: Maven Agi Finops
  service_category: AI and Machine Learning
  slug: maven-agi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maven-agi.png
layout: provider
modified: '2026-07-01'
name: Maven AGI
nav: Providers
network: true
overview: 'Maven AGI publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Agents API, Analytics API, and 6 more. Tagged areas include AI, Agents, Customer Support, Customer Experience, and Conversational AI.


  Maven AGI''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Maven Agi Plans Pricing
  plan_count: 2
  slug: maven-agi-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 3
  name: Maven Agi Rate Limits
  slug: maven-agi-rate-limits
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 55.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maven-agi/refs/heads/main/screenshots/maven-agi-2026-07-25T230432.png
security:
- kind: authentication
  name: Maven Agi Authentication
  slug: maven-agi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Maven Agi Domain Security
  slug: maven-agi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Maven Agi Trust Center
  slug: maven-agi-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR
slug: maven-agi
tags:
- AI
- Agents
- Customer Support
- Customer Experience
- Conversational AI
- Knowledge
website: https://www.mavenagi.com
---
