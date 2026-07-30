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
api_count: 11
apis:
- description: Gem's public REST API (v0) for customer and partner integrations against the Gem recruiting platform. Reference documentation is published at api.gem.com/v0/reference; access is provisioned for Gem cu
  name: Gem REST API (v0)
  slug: rest-api
- description: Next-generation, AI-native applicant tracking system that unifies pipeline management, application review, and interviewer workflows.
  name: Gem ATS
  slug: ats
- description: Talent CRM for sourcing, nurturing, and re-engaging passive and past candidates with multi-step outreach sequences and analytics.
  name: Gem Recruiting CRM
  slug: recruiting-crm
- description: Agentic sourcing product that finds and reaches out to candidates across sourcing sites and proprietary signals.
  name: Gem AI Outbound Sourcing
  slug: ai-outbound-sourcing
- description: Interview scheduling product that coordinates candidate and interviewer calendars and integrates with CodeSignal and other assessment partners.
  name: Gem Scheduling
  slug: scheduling
- description: Recruiting analytics product covering top-of-funnel sourcing through hire, with team, pipeline, source, and DEI reporting.
  name: Gem Full-Funnel Analytics
  slug: full-funnel-analytics
- description: Talent marketing module for landing pages, recruiting events, and candidate nurture campaigns.
  name: Gem Talent Marketing
  slug: talent-marketing
- description: Agentic AI worker that screens inbound applications against job criteria and routes qualified candidates into the hiring pipeline.
  name: Gem AI Application Review
  slug: ai-application-review
- description: Agentic AI worker that re-surfaces past applicants and silver-medalists against open requisitions.
  name: Gem AI Talent Rediscovery
  slug: ai-talent-rediscovery
- description: Browser extension that lets recruiters source candidates from LinkedIn and other sites, capture contact data, and push prospects into Gem sequences and the Gem CRM.
  name: Gem Chrome Extension
  slug: chrome-extension
- description: Integrations directory covering ATS, sourcing sites, productivity, HRIS & onboarding, scheduling, background checks, candidate assessments, job advertising, job boards & distribution, and interviewing
  name: Gem Integrations Marketplace
  slug: integrations-marketplace
artifact_total: 17
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/gem-com-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gem-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gem-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gem.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.gem.com/v0/reference
- group: operate
  title: ''
  type: Help
  url: https://help.gem.com
- group: learn
  title: ''
  type: Academy
  url: https://academy.gem.com/
- group: operate
  title: ''
  type: Status
  url: https://status.gem.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gem-software/
created: '2026-05-23'
description: Gem is an AI-first recruiting platform that bundles a next-generation ATS, recruiting CRM, AI outbound sourcing, scheduling, talent marketing, application review, and talent rediscovery into a single agentic AI hiring system used by more than 1,200 talent acquisition teams. Gem ships a Chrome extension for sourcing, a public REST API (v0) documented at api.gem.com/v0/reference, an integrations marketplace at integrations.gem.com/gem covering ATS, HRIS, scheduling, assessments, background checks, and job distribution, plus a status page and academy.
finops:
- name: Gem Com Finops
  service_category: API
  slug: gem-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gem-com.png
layout: provider
modified: '2026-05-23'
name: Gem
nav: Providers
network: true
overview: 'Gem publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Recruiting CRM, ATS, Sourcing, Talent Marketing, and Agentic AI.


  Gem''s developer surface includes documentation, academy / training, status page, and 6 more developer resources.'
plans:
- name: Gem Com Plans Pricing
  plan_count: 1
  slug: gem-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Gem Com Rate Limits
  slug: gem-com-rate-limits
score:
  band: emerging
  composite: 19.3
  delta: -2.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gem-com/refs/heads/main/screenshots/gem-com-2026-06-20T181713.png
security:
- kind: domain-security
  name: Gem Com Domain Security
  slug: gem-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gem Com Vulnerability Disclosure
  slug: gem-com-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Gem Com Trust Center
  slug: gem-com-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR
slug: gem-com
tags:
- Recruiting CRM
- ATS
- Sourcing
- Talent Marketing
- Agentic AI
- HR Tech
website: https://www.gem.com
---
