---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Spark Hire Agentic Access
  operation_count: 44
  slug: spark-hire-agentic-access
  summary_line: 44 operations · 25 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Authenticated user, plan, and company context.
  name: Spark Hire Account API
  slug: spark-hire-account-api
- description: Questions within an interview and reusable question sets.
  name: Spark Hire Interview Questions API
  slug: spark-hire-interview-questions-api
- description: One-way and live video interviews.
  name: Spark Hire Interviews API
  slug: spark-hire-interviews-api
- description: Jobs (requisitions) that interviews are organized under.
  name: Spark Hire Jobs API
  slug: spark-hire-jobs-api
- description: Basic and advanced share links for reviewing interviews.
  name: Spark Hire Share Links API
  slug: spark-hire-share-links-api
- description: Company users (evaluators) and their integration API keys.
  name: Spark Hire Users API
  slug: spark-hire-users-api
- description: Event subscriptions for interview and job lifecycle changes.
  name: Spark Hire Webhooks API
  slug: spark-hire-webhooks-api
artifact_total: 14
collections:
- collection_type: open
  name: Spark Hire API
  slug: open-spark-hire
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spark-hire-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spark-hire-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spark-hire-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spark-hire
- group: company
  title: ''
  type: Website
  url: https://www.sparkhire.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sparkhire.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/spark-hire-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spark-hire-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spark-hire-finops.yml
created: '2026-07-10'
description: Spark Hire is a video interviewing and talent assessment platform that lets recruiters screen, interview, and evaluate candidates asynchronously and live. The Spark Hire REST API embeds video interviewing into an applicant tracking system or custom hiring app - programmatically managing jobs, one-way and live interviews, interview questions and question sets, company users (evaluators), candidate share links, and webhook subscriptions for interview and job lifecycle events. Responses are JSON over HTTPS under https://api.sparkhire.com/v1.0, authenticated with a per-user API key via HTTP Basic. API access is not self-serve - it must be enabled on your account by Spark Hire - but the API reference is fully public.
finops:
- name: Spark Hire Finops
  service_category: Human Resources and Recruiting Software
  slug: spark-hire-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spark-hire.png
layout: provider
modified: '2026-07-10'
name: Spark Hire
nav: Providers
network: true
overview: 'Spark Hire publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Interview Questions API, Interviews API, and 4 more. Tagged areas include Video Interviewing, Recruiting, Hiring, HR Tech, and Talent Assessment.


  Spark Hire''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Spark Hire Plans Pricing
  plan_count: 4
  slug: spark-hire-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 2
  name: Spark Hire Rate Limits
  slug: spark-hire-rate-limits
score:
  band: thin
  composite: 35.4
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Spark Hire Authentication
  slug: spark-hire-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spark Hire Domain Security
  slug: spark-hire-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: spark-hire
tags:
- Video Interviewing
- Recruiting
- Hiring
- HR Tech
- Talent Assessment
- ATS
website: https://www.sparkhire.com
---
