---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The Recall.ai REST API provides programmatic access to meeting bot management, recording retrieval, transcript extraction, calendar integration, and real-time media streaming across Zoom, Google Meet,
  name: Recall.ai REST API
  slug: recallai-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recall-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.recall.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.recall.ai/docs/getting-started
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/recallai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recall-ai
- group: company
  title: ''
  type: Blog
  url: https://www.recall.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.recall.ai/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://statusgator.com/services/recallai
- group: other
  title: ''
  type: X
  url: https://twitter.com/recall_ai
- group: commercial
  title: ''
  type: Plans
  url: plans/recall-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/recall-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/recall-ai-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/recall-ai-context.jsonld
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-12'
description: Recall.ai provides meeting bot infrastructure through a REST API that enables developers to programmatically join Zoom, Microsoft Teams, Google Meet, Webex, Slack Huddles, and other video conferencing platforms. The API delivers real-time and asynchronous access to meeting recordings, AI-powered transcription, participant metadata, and structured meeting data. Developers can deploy bots that stream audio and video, trigger calendar-driven automations, and extract actionable insights from meetings at scale. Recall.ai supports multi-region deployments across US West, US East, EU, and Asia-Pacific, with per-second usage billing and no monthly platform fee.
finops:
- name: Recall Ai Finops
  service_category: ''
  slug: recall-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recall-ai.png
jsonld:
- class_count: 7
  name: Recall Ai Context
  property_count: 16
  slug: recall-ai-context
layout: provider
modified: '2026-06-12'
name: Recall.ai
nav: Providers
network: true
overview: 'Recall.ai publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Meeting Bots, Recording, Transcription, Video Conferencing, and Zoom.


  The Recall.ai catalog on APIs.io includes 1 JSON-LD context.


  Recall.ai''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Recall Ai Plans Pricing
  plan_count: 3
  slug: recall-ai-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 7
  name: Recall Ai Rate Limits
  slug: recall-ai-rate-limits
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 38.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recall-ai/refs/heads/main/screenshots/recall-ai-2026-06-20T192655.png
security:
- kind: domain-security
  name: Recall Ai Domain Security
  slug: recall-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: recall-ai
tags:
- Meeting Bots
- Recording
- Transcription
- Video Conferencing
- Zoom
- Google Meet
- Microsoft Teams
- Real-Time
- AI
- Infrastructure
website: https://www.recall.ai/
---
