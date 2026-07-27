---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
api_count: 3
apis:
- description: Read calls, meetings, emails and engagement metadata.
  name: Chorus Engagements API
  slug: chorus-engagements-api
- description: Retrieve recordings, transcripts and AI-generated insights.
  name: Chorus Recordings & Transcripts API
  slug: chorus-recordings-transcripts-api
- description: Push and pull contacts, accounts and opportunities for CRM enrichment.
  name: Chorus CRM Sync API
  slug: chorus-crm-sync-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chorus-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chorus.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/chorus-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chorus-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chorus-ai-finops.yml
created: '2026-05-08'
description: Chorus.ai is a conversation intelligence platform (acquired by ZoomInfo) that records, transcribes, and analyzes customer-facing calls and meetings to surface deal insights and coach reps.
finops:
- name: Chorus Ai Finops
  service_category: Sales
  slug: chorus-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chorus-ai.png
layout: provider
modified: '2026-05-08'
name: Chorus.ai
nav: Providers
network: true
overview: Chorus.ai publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sales, Revenue Intelligence, Conversation, Analytics, and ZoomInfo.
plans:
- name: Chorus Ai Plans Pricing
  plan_count: 1
  slug: chorus-ai-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Chorus Ai Rate Limits
  slug: chorus-ai-rate-limits
score:
  band: emerging
  composite: 17.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chorus-ai/refs/heads/main/screenshots/chorus-ai-2026-06-20T174336.png
security:
- kind: domain-security
  name: Chorus Ai Domain Security
  slug: chorus-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chorus-ai
tags:
- Sales
- Revenue Intelligence
- Conversation
- Analytics
- ZoomInfo
website: https://www.chorus.ai/
---
