---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
  human_in_the_loop: 0
  name: Autocontent Api Agentic Access
  operation_count: 51
  slug: autocontent-api-agentic-access
  summary_line: 51 operations · 25 acting
api_count: 9
apis:
- description: Generate AI-powered podcast episodes from URLs, PDFs, YouTube videos, plain text, or social media feeds. Produces MP3 audio with metadata using NotebookLM-style AI with support for standard voices and
  name: Podcast Generation API
  slug: podcast-generation
- description: Programmatically produce explainer videos and short-form vertical video content (9:16 format) from text, URLs, and other source content. Explainer videos consume 50 credits; video shorts consume 400 c
  name: Video Generation API
  slug: video-generation
- description: Performs multi-step AI reasoning that browses the live web, reads reputable sources, and synthesizes comprehensive research reports. Supports output as structured JSON, HTML blog posts, and study guid
  name: Deep Research API
  slug: deep-research
- description: Transform source content into visual infographics and interactive quiz formats. Consumes 10-30 credits per asset. Supports diverse input types and produces structured HTML and visual media output.
  name: Infographics and Quizzes API
  slug: infographics-quizzes
- description: The Content API from AutoContent API — 24 operation(s) for content.
  name: AutoContent API Content API
  slug: autocontent-api-content-api
- description: The Dedicated Account API from AutoContent API — 4 operation(s) for dedicated account.
  name: AutoContent API Dedicated Account API
  slug: autocontent-api-dedicated-account-api
- description: The Podcast API from AutoContent API — 3 operation(s) for podcast.
  name: AutoContent API Podcast API
  slug: autocontent-api-podcast-api
- description: The Share API from AutoContent API — 5 operation(s) for share.
  name: AutoContent API Share API
  slug: autocontent-api-share-api
- description: The Video API from AutoContent API — 12 operation(s) for video.
  name: AutoContent API Video API
  slug: autocontent-api-video-api
artifact_total: 32
collections:
- collection_type: open
  name: AutoContent API
  slug: open-autocontent-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/autocontent-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autocontent-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/autocontent-api-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://autocontentapi.com/blog
- group: company
  title: ''
  type: Website
  url: https://autocontentapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://autocontentapi.com/docs
- group: start
  title: ''
  type: Signup
  url: https://autocontentapi.com
- group: commercial
  title: ''
  type: Pricing
  url: https://autocontentapi.com/pricing
- group: operate
  title: ''
  type: RateLimits
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://autocontentapi.com/llms.txt
created: '2025-05-02'
description: AutoContent API is an AI-powered content generation platform that enables developers and content teams to programmatically produce podcasts, explainer videos, video shorts, deep research reports, infographics, and quizzes from diverse input sources including URLs, PDFs, YouTube videos, plain text, and social data feeds. Built on NotebookLM-style AI technology, it provides REST API endpoints with a credit-based pricing model and integrations with Make.com, Zapier, and WordPress.
features:
- description: Generate audio podcast episodes from URLs, PDFs, YouTube videos, plain text, and social feeds using NotebookLM-style AI with natural-sounding voices.
  name: AI Podcast Generation
- description: Programmatically produce explainer videos and short-form vertical video content suitable for social media platforms.
  name: Video Content Production
- description: Multi-step AI reasoning that browses the live web and synthesizes comprehensive research reports from reputable sources.
  name: Deep Research Synthesis
- description: Transform text and data sources into visual infographic formats for presentations, reports, and marketing materials.
  name: Infographic Generation
- description: Automatically generate interactive quizzes from educational content, PDFs, and URLs for e-learning and assessment purposes.
  name: Quiz Creation
- description: Create custom voice replicas for personalized podcast and audio content generation that matches a specific speaker's voice profile.
  name: Voice Cloning
- description: Accept diverse input formats including URLs, PDF files, YouTube videos, plain text, X/Twitter streams, and Reddit data feeds.
  name: Multi-Source Input
- description: Flexible credit-based consumption model where different content types consume different credit amounts based on complexity and output quality.
  name: Credit-Based Pricing
finops:
- name: Autocontent Api Finops
  service_category: API
  slug: autocontent-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autocontent-api.png
integrations:
- description: Native Make.com (formerly Integromat) integration for no-code workflow automation connecting AutoContent API with hundreds of other services.
  name: Make.com
- description: Zapier integration enabling automated content generation workflows triggered by events in thousands of connected applications.
  name: Zapier
- description: WordPress plugin or REST API integration for automatically publishing AI-generated content directly to WordPress sites.
  name: WordPress
layout: provider
modified: '2026-04-19'
name: AutoContent API
nav: Providers
network: true
overview: 'AutoContent API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Content API, Dedicated Account API, Podcast API, and 2 more. Tagged areas include AI, Audio, Content Generation, Podcasts, and Video.


  AutoContent API''s developer surface includes authentication, engineering blog, documentation, signup flow, pricing, and 4 more developer resources.'
plans:
- name: Autocontent Api Plans Pricing
  plan_count: 3
  slug: autocontent-api-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 5
  name: Autocontent Api Rate Limits
  slug: autocontent-api-rate-limits
score:
  band: thin
  composite: 39.2
  delta: -2.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 53.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autocontent-api/refs/heads/main/screenshots/autocontent-api-2026-06-20T172653.png
security:
- kind: authentication
  name: Autocontent Api Authentication
  slug: autocontent-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Autocontent Api Domain Security
  slug: autocontent-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autocontent-api
tags:
- AI
- Audio
- Content Generation
- Podcasts
- Video
- Generative AI
- Text to Speech
- Automation
use_cases:
- description: Content creators and media teams automating production of podcast episodes, videos, and written content from research materials at scale.
  name: Content Creator Automation
- description: Educators and e-learning platforms generating AI-powered audio lessons, explainer videos, and interactive quizzes from course materials.
  name: Educational Content Production
- description: Marketing teams programmatically producing diverse content formats from campaign briefs, product data, and market research for multi-channel distribution.
  name: Marketing Content at Scale
- description: Media organizations and research firms automating synthesis of news coverage, competitive intelligence, and industry reports.
  name: News and Research Automation
- description: Developers embedding AI content generation capabilities into applications, CMS platforms, and automated publishing workflows via REST API.
  name: Developer Integration
website: https://autocontentapi.com
---
