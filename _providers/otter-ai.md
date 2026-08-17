---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Otter.ai REST API enables Enterprise customers to programmatically upload audio and video files for transcription, retrieve speaker-identified transcripts, receive webhook notifications when speec
  name: Otter.ai API
  slug: otter-ai-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/otter-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/otter-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://otter.ai
- group: docs
  title: ''
  type: Documentation
  url: https://otter.ai/api/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/otter-framework
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/otter-ai
- group: company
  title: ''
  type: Blog
  url: https://otter.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://otter.ai/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.otter.ai/
- group: other
  title: ''
  type: X
  url: https://x.com/otter_ai
- group: commercial
  title: ''
  type: Plans
  url: plans/otter-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/otter-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/otter-ai-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: https://raw.githubusercontent.com/api-evangelist/otter-ai/refs/heads/main/blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/otter-ai/refs/heads/main/json-ld/otter-ai-context.jsonld
created: '2026-06-13'
description: Otter.ai is an AI-powered meeting transcription and conversational intelligence platform that automatically records, transcribes, and summarizes meetings across Zoom, Google Meet, Microsoft Teams, and other video conferencing services. The platform provides a REST API for Enterprise customers to programmatically retrieve speech-to-text transcripts, speaker-identified conversation segments, and AI-generated meeting summaries. Developers can upload audio files, retrieve processed transcripts via webhooks, and integrate meeting intelligence into their own applications using bearer token authentication. Otter.ai also offers an MCP Server integration enabling AI assistants like Claude and ChatGPT to query meeting knowledge directly.
finops:
- name: Otter Ai Finops
  service_category: ''
  slug: otter-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/otter-ai.png
jsonld:
- class_count: 14
  name: Otter Ai Context
  property_count: 0
  slug: otter-ai-context
layout: provider
modified: '2026-06-13'
name: Otter.ai
nav: Providers
network: true
overview: 'Otter.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Transcription, Meeting Notes, Speech-to-Text, and Speaker Identification.


  The Otter.ai catalog on APIs.io includes 1 JSON-LD context.


  Otter.ai''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Otter Ai Plans Pricing
  plan_count: 4
  slug: otter-ai-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 9
  name: Otter Ai Rate Limits
  slug: otter-ai-rate-limits
score:
  band: thin
  composite: 30.7
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 30.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/otter-ai/refs/heads/main/screenshots/otter-ai-2026-06-20T191223.png
security:
- kind: domain-security
  name: Otter Ai Domain Security
  slug: otter-ai-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Otter Ai Trust Center
  slug: otter-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: otter-ai
tags:
- AI
- Transcription
- Meeting Notes
- Speech-to-Text
- Speaker Identification
- Meeting Intelligence
- Summaries
website: https://otter.ai
---
