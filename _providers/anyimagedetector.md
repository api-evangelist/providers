---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.4
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: REST API with a single endpoint (POST /v1/image/detect) that detects whether an image is AI-generated. Accepts a multipart file upload (JPG, PNG or WebP, up to 8 MB) or a JSON body with a public image
  name: AI Image Detector API
  slug: ai-image-detector-api
artifact_total: 7
collections:
- collection_type: open
  name: AI Image Detector API
  slug: open-anyimagedetector-ai-image-detector
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anyimagedetector-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anyimagedetector-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://imagedetector.online/api
- group: docs
  title: ''
  type: Documentation
  url: https://imagedetector.online/docs
- group: docs
  title: ''
  type: APIReference
  url: https://imagedetector.online/docs
- group: operate
  title: ''
  type: Support
  url: mailto:support@imagedetector.online
- group: company
  title: ''
  type: Blog
  url: https://imagedetector.online/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://imagedetector.online/pricing
- group: start
  title: ''
  type: SignUp
  url: https://imagedetector.online/sign-up
- group: start
  title: ''
  type: Login
  url: https://imagedetector.online/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://imagedetector.online/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://imagedetector.online/privacy-policy
- group: other
  title: ''
  type: Methodology
  url: https://imagedetector.online/methodology
- group: other
  title: ''
  type: Limitations
  url: https://imagedetector.online/accuracy-and-limitations
- group: company
  title: ''
  type: About
  url: https://imagedetector.online/about
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anyimagedetector-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/anyimagedetector-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anyimagedetector-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anyimagedetector-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/anyimagedetector-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anyimagedetector-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anyimagedetector-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anyimagedetector-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/anyimagedetector-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-11'
description: AnyImageDetector (imagedetector.online) is a single-purpose AI-image-detection service for individuals, trust-and-safety reviewers, journalists and developers. Its AI Image Detector API exposes one REST endpoint, POST /v1/image/detect, that accepts a JPG/PNG/WebP file up to 8 MB or a public image URL and returns a verdict (likely_ai, likely_human or uncertain), an ai_score from 0 to 1, a confidence label, and a source_breakdown array reserved for future per-generator scores. The provider publishes the exact score bands that map ai_score to verdict and confidence, and deliberately declines to publish a single accuracy percentage, stating that one number would hide differences between generators, image styles, resolutions and editing conditions. Authentication is a static sk_ API key sent as a Bearer token or an x-api-key header; API access requires a paid plan and each successful detection consumes one credit from the same balance as the web tool. Requests are limited to one
  per second per key, with Retry-After returned on 429.
image: https://imagedetector.online/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: anyimagedetector-mcp.yml
  slug: anyimagedetector-mcpyml
modified: '2026-08-11'
name: AnyImageDetector
nav: Providers
network: true
overview: 'AnyImageDetector publishes 1 API on the [APIs.io](https://apis.io/) network: AI Image Detector API. Tagged areas include AI image detection, image analysis, computer vision, content moderation, and trust & safety.


  AnyImageDetector''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
plans:
- name: Anyimagedetector Plans Pricing
  plan_count: 5
  slug: anyimagedetector-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 1
  name: Anyimagedetector Rate Limits
  slug: anyimagedetector-rate-limits
score:
  band: developing
  composite: 53.9
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 61.9
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 53.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Anyimagedetector Authentication
  slug: anyimagedetector-authentication
  summary_line: http-bearer/apiKey · 2 schemes
- kind: domain-security
  name: Anyimagedetector Domain Security
  slug: anyimagedetector-domain-security
  summary_line: TLSv1.3 · DMARC
slug: anyimagedetector
tags:
- AI image detection
- image analysis
- computer vision
- content moderation
- trust & safety
- fact-checking
- media verification
- developer tools
- synthetic media
- fraud prevention
website: https://imagedetector.online/api
---
