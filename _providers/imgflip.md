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
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
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
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Imgflip Meme Generator AI API
  slug: open-imgflip-ai-api
- collection_type: open
  name: Imgflip Meme Generator AI Memes API
  slug: open-imgflip-memes-api
- collection_type: open
  name: Imgflip Meme Generator AI Premium API
  slug: open-imgflip-premium-api
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
random_paper: 148
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Imgflip API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: imgflip-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.6
  delta: -7.6
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 9.8
    contract_quality: 51.0
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 0.0
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
