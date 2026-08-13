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
  scored_at: '2026-08-12'
api_count: 7
apis:
- description: Creates, manages, and retrieves on-demand and live video interviews, including structured interview guides, candidate invitations, and recorded responses. Exposed to customers and certified ATS partne
  name: HireVue Video Interviewing API
  slug: video-interviewing
- description: Provisions and scores HireVue assessments including skill validation, assessment builder, virtual job tryouts, game-based assessments, technical coding assessments, and language proficiency tests.
  name: HireVue Assessments API
  slug: assessments
- description: Automated interview scheduling and coordination across candidate and interviewer calendars. Supports self-scheduling links, panel scheduling, and rescheduling flows.
  name: HireVue Coordinate (Scheduling) API
  slug: coordinate-scheduling
- description: Agentic AI surface that engages candidates conversationally, conducts structured screening, and routes qualified applicants into interview and assessment workflows.
  name: HireVue AI Hiring Agent
  slug: ai-hiring-agent
- description: SMS and chat-based candidate engagement, text recruiting, and Match and Apply flows that move candidates from interest to application.
  name: HireVue Text Recruiting / Match and Apply
  slug: text-automation
- description: Analytics product that aggregates interview, assessment, and pipeline data into reporting and hiring science insights.
  name: HireVue Interview Insights
  slug: interview-insights
- description: Server-to-server event delivery covering interview lifecycle, assessment completion, scheduling events, and candidate status changes.
  name: HireVue Webhooks
  slug: webhooks
artifact_total: 12
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/hirevue-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hirevue-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hirevue.com/blog
- group: company
  title: ''
  type: Website
  url: https://www.hirevue.com
- group: other
  title: ''
  type: Platform
  url: https://www.hirevue.com/platform
- group: other
  title: ''
  type: Developer
  url: https://developer.hirevue.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hirevue/
created: '2026-05-23'
description: HireVue is an AI-driven hiring platform built around video interviewing, conversational AI, structured assessments, automated scheduling, and an AI Hiring Agent. The platform plugs into the major ATS systems (Workday, SAP SuccessFactors, Oracle/Taleo, iCIMS, Greenhouse, SmartRecruiters, PageUp, Cornerstone, Avature, Oleeo, BrassRing) and exposes REST APIs and webhooks to customers and certified partners via the HireVue developer portal at developer.hirevue.com. At the time of this profile the public developer portal was not responding to crawl, so APIs are listed at the product/capability level and the developer portal URL is captured as the canonical reference.
finops:
- name: Hirevue Finops
  service_category: API
  slug: hirevue-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hirevue.png
layout: provider
modified: '2026-05-23'
name: HireVue
nav: Providers
network: true
overview: 'HireVue publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Video Interviewing, Assessments, AI Hiring, Scheduling, and Conversational AI.


  HireVue''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Hirevue Plans Pricing
  plan_count: 1
  slug: hirevue-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 2
  name: Hirevue Rate Limits
  slug: hirevue-rate-limits
score:
  band: emerging
  composite: 18.0
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hirevue/refs/heads/main/screenshots/hirevue-2026-06-20T182756.png
security:
- kind: domain-security
  name: Hirevue Domain Security
  slug: hirevue-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Hirevue Trust Center
  slug: hirevue-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: hirevue
tags:
- Video Interviewing
- Assessments
- AI Hiring
- Scheduling
- Conversational AI
- HR Tech
website: https://www.hirevue.com
---
