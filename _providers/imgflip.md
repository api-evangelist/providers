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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Imgflip Agentic Access
  operation_count: 7
  slug: imgflip-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 3
apis:
- description: AI-powered meme generation endpoints
  name: Imgflip AI API
  slug: imgflip-ai-api
- description: Meme template retrieval and captioning operations
  name: Imgflip Memes API
  slug: imgflip-memes-api
- description: Endpoints requiring a premium Imgflip account
  name: Imgflip Premium API
  slug: imgflip-premium-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/imgflip-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imgflip-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://imgflip.com/terms
- group: operate
  title: ''
  type: Contact
  url: https://imgflip.com/contact
- group: start
  title: ''
  type: Login
  url: https://imgflip.com/login
- group: start
  title: ''
  type: Signup
  url: https://imgflip.com/signup
- group: commercial
  title: ''
  type: Plans
  url: https://imgflip.com/api
created: '2026-06-13'
description: Imgflip is a meme generator platform providing a REST API for captioning popular meme templates, searching over one million meme formats, auto-generating memes from text input, and creating original AI-powered meme images. Free endpoints cover getting popular templates and captioning images; premium endpoints unlock GIF captioning, meme search, automeme, and AI meme generation.
examples:
- key_count: 2
  name: Ai Meme Response
  slug: ai-meme-response
- key_count: 7
  name: Caption Image Request
  slug: caption-image-request
- key_count: 2
  name: Caption Image Response
  slug: caption-image-response
- key_count: 2
  name: Get Memes Response
  slug: get-memes-response
- key_count: 2
  name: Search Memes Response
  slug: search-memes-response
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imgflip.png
json_schemas:
- name: AiMemeResponse
  property_count: 2
  slug: ai-meme-response
- name: CaptionResponse
  property_count: 2
  slug: caption-response
- name: MemeTemplate
  property_count: 7
  slug: meme-template
- name: TextBox
  property_count: 7
  slug: text-box
layout: provider
modified: '2026-06-13'
name: Imgflip
nav: Providers
network: true
overview: 'Imgflip publishes 3 APIs on the [APIs.io](https://apis.io/) network: AI API, Memes API, and Premium API. Tagged areas include Memes, Images, GIFs, Entertainment, and AI.


  The Imgflip catalog on APIs.io includes 1 Spectral governance ruleset.


  Imgflip''s developer surface includes signup flow and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 64
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Imgflip API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: imgflip-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.5
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 48.7
    developer_ergonomics: 0.0
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 41.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imgflip/refs/heads/main/screenshots/imgflip-2026-06-20T183250.png
security:
- kind: domain-security
  name: Imgflip Domain Security
  slug: imgflip-domain-security
  summary_line: TLSv1.3 · DMARC
slug: imgflip
tags:
- Memes
- Images
- GIFs
- Entertainment
- AI
- Image Generation
---
