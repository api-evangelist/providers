---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Spark Hire Agentic Access
  operation_count: 44
  slug: spark-hire-agentic-access
  summary_line: 44 operations · 25 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.sparkhire.com/v1.0
  baseurl_source: declared
  description: Authenticated user, plan, and company context.
  name: Spark Hire Account API
  slug: spark-hire-account-api
- baseURL: https://api.sparkhire.com/v1.0
  baseurl_source: declared
  description: Questions within an interview and reusable question sets.
  name: Spark Hire Interview Questions API
  slug: spark-hire-interview-questions-api
- baseURL: https://api.sparkhire.com/v1.0
  baseurl_source: declared
  description: One-way and live video interviews.
  name: Spark Hire Interviews API
  slug: spark-hire-interviews-api
- baseURL: https://api.sparkhire.com/v1.0
  baseurl_source: declared
  description: Jobs (requisitions) that interviews are organized under.
  name: Spark Hire Jobs API
  slug: spark-hire-jobs-api
- baseURL: https://api.sparkhire.com/v1.0
  baseurl_source: declared
  description: Basic and advanced share links for reviewing interviews.
  name: Spark Hire Share Links API
  slug: spark-hire-share-links-api
- baseURL: https://api.sparkhire.com/v1.0
  baseurl_source: declared
  description: Company users (evaluators) and their integration API keys.
  name: Spark Hire Users API
  slug: spark-hire-users-api
- baseURL: https://api.sparkhire.com/v1.0
  baseurl_source: declared
  description: Event subscriptions for interview and job lifecycle changes.
  name: Spark Hire Webhooks API
  slug: spark-hire-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spark Hire Account API
  slug: open-spark-hire-account-api
- collection_type: open
  name: Spark Hire Account Interview Questions API
  slug: open-spark-hire-interview-questions-api
- collection_type: open
  name: Spark Hire Account Interviews API
  slug: open-spark-hire-interviews-api
- collection_type: open
  name: Spark Hire Account Jobs API
  slug: open-spark-hire-jobs-api
- collection_type: open
  name: Spark Hire Account Share Links API
  slug: open-spark-hire-share-links-api
- collection_type: open
  name: Spark Hire Account Users API
  slug: open-spark-hire-users-api
- collection_type: open
  name: Spark Hire Account Webhooks API
  slug: open-spark-hire-webhooks-api
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
random_paper: 6
rate_limits:
- limit_count: 2
  name: Spark Hire Rate Limits
  slug: spark-hire-rate-limits
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 3.4
    developer_ergonomics: 13.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spark-hire/refs/heads/main/screenshots/spark-hire-2026-09-02T160328.png
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
