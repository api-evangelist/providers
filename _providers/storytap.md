---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The JSON API behind StoryTap's embeddable video widgets. Brands load a first-party loader script from StoryTap's CDN, and that script POSTs to api.storytap.com/w/* to fetch an embed's configuration an
  name: StoryTap Video Widget API
  slug: storytap-video-widget-api
artifact_total: 8
asyncapis:
- description: ''
  name: Storytap Webhooks
  slug: storytap-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://storytap.com/
- group: other
  title: ''
  type: Enterprise
  url: https://storytap.com/enterprise-video-solution/
- group: company
  title: ''
  type: Blog
  url: https://storytap.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://storytap.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.storytap.com/login
- group: operate
  title: ''
  type: Support
  url: https://storytap.com/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://storytap.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://storytap.com/terms#privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://ohdear.app/status-page/storytap-app-status
- group: auth
  title: ''
  type: Security
  url: https://storytap.com/responsible-disclosure-policy
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/storytap-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/storytap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/storytap-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/storytap-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/storytap-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/storytap-packages.yml
- group: design
  title: ''
  type: Components
  url: components/storytap-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/storytap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/storytap-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/storytap-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/storytap-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/storytap-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/storytap-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/storytap-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/storytap-mcp.yml
- group: operate
  title: ''
  type: Contact
  url: https://storytap.com/contact/
created: '2026-07-17'
description: StoryTap is a patented AI-powered user-generated video (UGC) platform that automates the collection, editing, captioning, and distribution of authentic customer video testimonials and stories. It guides customers through recording on their own devices with no film crew or production stack, auto-edits share-ready clips, and publishes them to websites, social media, and Google Reviews. StoryTap holds six utility patents and is used by brands including TELUS, Samsung, Danone, Canadian Tire, AAA, and UCLA Anderson. A REST API and advanced webhooks are offered on Enterprise plans (not publicly documented). StoryTap is backed by Techstars and the Lazaridis Institute.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/storytap.png
layout: provider
mcp_servers:
- description: ''
  name: storytap-mcp.yml
  slug: storytap-mcpyml
modified: '2026-08-13'
name: StoryTap
nav: Providers
network: true
overview: 'StoryTap publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Testimonials, User Generated Content, and Marketing.


  The StoryTap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  StoryTap''s developer surface includes engineering blog, pricing, support, authentication, and 22 more developer resources.'
plans:
- name: Storytap Plans Pricing
  plan_count: 0
  slug: storytap-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Storytap Rate Limits
  slug: storytap-rate-limits
score:
  band: thin
  composite: 38.5
  delta: -3.7
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 42.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/storytap/refs/heads/main/screenshots/storytap-2026-08-17T082128.png
security:
- kind: authentication
  name: Storytap Authentication
  slug: storytap-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Storytap Domain Security
  slug: storytap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Storytap Vulnerability Disclosure
  slug: storytap-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: storytap
tags:
- Company
- Video
- Testimonials
- User Generated Content
- Marketing
- Reviews
- Video Testimonials
- SaaS
website: https://storytap.com/
---
