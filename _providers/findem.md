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
api_count: 11
apis:
- description: Assistive AI product that searches Findem's enriched people graph using natural-language attribute queries, returning ranked candidate lists with contact data and outreach workflows.
  name: Findem Talent Sourcing
  slug: talent-sourcing
- description: Outreach and nurture product that automates multi-channel campaigns against Findem-sourced and customer-imported talent pools.
  name: Findem Talent Marketing
  slug: talent-marketing
- description: Specialised sourcing experience focused on senior and executive talent, with longitudinal attribute search across the career graph.
  name: Findem Executive Search
  slug: executive-search
- description: Talent analytics product covering pipeline, diversity, and hiring funnel metrics built on Findem's people graph and customer ATS data.
  name: Findem Analytics
  slug: analytics
- description: Labour market and competitive talent intelligence module surfacing supply, compensation, and movement signals against Findem's enriched datasets.
  name: Findem Market Intelligence
  slug: market-intelligence
- description: Agentic AI worker that drafts, optimises, and distributes job posts based on role requirements and historical performance.
  name: Findem Intelligent Job Post Agent
  slug: intelligent-job-post
- description: Agentic worker that re-engages and converts inbound applicants through personalised outreach and scheduling.
  name: Findem Application Boost Agent
  slug: application-boost
- description: Agentic worker that screens applicants against role criteria, performs structured assessments, and advances qualified candidates.
  name: Findem Screening Agent
  slug: screening-agent
- description: Agentic worker that coordinates interview scheduling across candidate and interviewer calendars.
  name: Findem Scheduling Agent
  slug: scheduling-agent
- description: '"Build AI" service that labels and structures HR data so customers and partners can train and operate their own talent models.'
  name: Findem Data Labeling Engine
  slug: data-labeling-engine
- description: Embedded AI building blocks - including the AI Job Board, Sourcing Copilot, Labeling Engine, agents, and an MCP surface - that partners use to ship Findem-powered talent experiences inside their own p
  name: Findem Embedded AI (AI Job Board, Sourcing Copilot, Agents, MCP)
  slug: embedded-ai
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/findem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.findem.ai
- group: operate
  title: ''
  type: Contact
  url: https://www.findem.ai/contact-us
- group: company
  title: ''
  type: Partnerships
  url: https://www.findem.ai/partnerships
- group: start
  title: ''
  type: Demo
  url: https://www.findem.ai/request-demo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/findemai/
created: '2026-05-23'
description: Findem is an AI Talent Intelligence platform that blends assistive AI for sourcing, marketing, executive search, and analytics with agentic AI workers for intelligent job posting, application boost, screening, and scheduling. The company also exposes Embedded AI building blocks (AI Job Board, Sourcing Copilot, Labeling Engine, Agents, and MCP) for partners to ship branded AI hiring experiences. Findem is sold enterprise-direct; ATS, HRIS, and partner integrations are gated rather than offered through a public self-serve developer portal.
finops:
- name: Findem Finops
  service_category: API
  slug: findem-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/findem.png
layout: provider
modified: '2026-05-23'
name: Findem
nav: Providers
network: true
overview: Findem publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Talent Intelligence, AI Sourcing, Talent Analytics, Agentic AI, and Embedded AI.
plans:
- name: Findem Plans Pricing
  plan_count: 1
  slug: findem-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Findem Rate Limits
  slug: findem-rate-limits
score:
  band: emerging
  composite: 15.9
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/findem/refs/heads/main/screenshots/findem-2026-06-20T181216.png
security:
- kind: domain-security
  name: Findem Domain Security
  slug: findem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: findem
tags:
- Talent Intelligence
- AI Sourcing
- Talent Analytics
- Agentic AI
- Embedded AI
- HR Tech
website: https://www.findem.ai
---
