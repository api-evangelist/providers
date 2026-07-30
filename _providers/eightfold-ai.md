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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 9
apis:
- description: Core AI platform that powers candidate matching, skills inference, career-path recommendations, and internal mobility decisions across the Eightfold suite. Customer-facing APIs are made available to e
  name: Eightfold Talent Intelligence Platform
  slug: talent-intelligence
- description: Recruiting product that surfaces candidates by skills, potential, and fit rather than resumes alone, with agentic workflows for sourcing, screening, and pipelining. Integrated with the customer ATS ov
  name: Eightfold Talent Acquisition
  slug: talent-acquisition
- description: Single view of internal talent for retention, skills development, career planning, and succession. Powers manager and employee experiences against the same Talent Intelligence model used for hiring.
  name: Eightfold Talent Management
  slug: talent-management
- description: Internal mobility marketplace that lets employees discover roles, gigs, mentors, and learning paths matched to their skills and aspirations.
  name: Eightfold Workforce Exchange
  slug: workforce-exchange
- description: Project staffing product that matches consultants and employees to billable work using AI-driven skills matching, primarily used by professional services and consulting organisations.
  name: Eightfold Resource Management
  slug: resource-management
- description: Autonomous agentic interviewer that conducts structured candidate interviews end-to-end and returns scored, skills-anchored evaluations. Embedded into customer workflows directly and via partner platf
  name: Eightfold AI Interviewer
  slug: ai-interviewer
- description: Real-time copilot for human-led interviews, providing skills-based prompts, structured note-taking, and consistent evaluation across the interview loop.
  name: Eightfold AI Interview Companion
  slug: ai-interview-companion
- description: Build-it-yourself layer that lets customers compose custom talent applications on top of the Talent Intelligence Platform without long engineering cycles.
  name: Eightfold TalentForge
  slug: talentforge
- description: Marketplace of certified partner and customer-built applications that extend the Eightfold Talent Intelligence Platform.
  name: Eightfold App Marketplace
  slug: app-marketplace
artifact_total: 14
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/eightfold-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eightfold-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eightfold.ai
- group: other
  title: ''
  type: Products
  url: https://eightfold.ai/products/
- group: other
  title: ''
  type: Marketplace
  url: https://app.eightfold.ai/app_marketplace/
- group: operate
  title: ''
  type: Community
  url: https://community.eightfold.ai/
- group: company
  title: ''
  type: Blog
  url: https://eightfold.ai/engineering-blog/
- group: operate
  title: ''
  type: Contact
  url: https://eightfold.ai/company/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eightfold-ai/
- group: agent
  title: ''
  type: LlmsText
  url: https://eightfold.ai/llms.txt
created: '2026-05-23'
description: Eightfold AI is an agentic Talent Intelligence Platform that combines enterprise HR data with insights from more than a billion career profiles to power talent acquisition, talent management, workforce planning, internal mobility, resource management, and AI-driven interviewing. The platform is delivered as enterprise SaaS with sales-led onboarding; APIs and ATS/HRIS integrations are exposed to customers and certified partners (e.g. Oracle Fusion Cloud Recruiting) under contract rather than via a public, self-serve developer portal.
finops:
- name: Eightfold Ai Finops
  service_category: API
  slug: eightfold-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eightfold-ai.png
layout: provider
modified: '2026-05-23'
name: Eightfold AI
nav: Providers
network: true
overview: 'Eightfold AI publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Talent Intelligence, Talent Acquisition, Talent Management, AI Interviewing, and HR Tech.


  Eightfold AI''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Eightfold Ai Plans Pricing
  plan_count: 1
  slug: eightfold-ai-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 2
  name: Eightfold Ai Rate Limits
  slug: eightfold-ai-rate-limits
score:
  band: emerging
  composite: 18.8
  delta: -2.6
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eightfold-ai/refs/heads/main/screenshots/eightfold-ai-2026-06-20T180516.png
security:
- kind: domain-security
  name: Eightfold Ai Domain Security
  slug: eightfold-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Eightfold Ai Trust Center
  slug: eightfold-ai-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017
slug: eightfold-ai
tags:
- Talent Intelligence
- Talent Acquisition
- Talent Management
- AI Interviewing
- HR Tech
- Workforce Planning
- Agentic AI
website: https://eightfold.ai
---
