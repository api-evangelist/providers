---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Autocontent Api Agentic Access
  operation_count: 51
  slug: autocontent-api-agentic-access
  summary_line: 51 operations · 25 acting
api_count: 1
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
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The Content API from AutoContent API — 24 operation(s) for content.
  name: AutoContent API Content API
  slug: autocontent-api-content-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The Dedicated Account API from AutoContent API — 4 operation(s) for dedicated account.
  name: AutoContent API Dedicated Account API
  slug: autocontent-api-dedicated-account-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The Podcast API from AutoContent API — 3 operation(s) for podcast.
  name: AutoContent API Podcast API
  slug: autocontent-api-podcast-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The Share API from AutoContent API — 5 operation(s) for share.
  name: AutoContent API Share API
  slug: autocontent-api-share-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The Video API from AutoContent API — 12 operation(s) for video.
  name: AutoContent API Video API
  slug: autocontent-api-video-api
- baseURL: https://api.autocontentapi.com/v1
  baseurl_source: declared
  description: 'The current AutoContent product: a Project-centred, scope-based REST API that turns a website, reusable Knowledge or a bounded topic into first-class content Assets — articles, lead magnets, ebooks, s'
  name: AutoContent Platform API v1
  slug: platform-api-v1
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The original AutoContent surface, served unversioned at https://api.autocontentapi.com with its own JWT credentials and monthly credit plans. 106 operations across 99 paths covering podcasts, explaine
  name: AutoContent legacy Content API
  slug: legacy-content-api
artifact_total: 43
asyncapis:
- description: ''
  name: Autocontent Api Webhooks
  slug: autocontent-api-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AutoContent Content API
  slug: open-autocontent-api-content-api
- collection_type: open
  name: AutoContent Content Dedicated Account API
  slug: open-autocontent-api-dedicated-account-api
- collection_type: open
  name: AutoContent Content Podcast API
  slug: open-autocontent-api-podcast-api
- collection_type: open
  name: AutoContent Content Share API
  slug: open-autocontent-api-share-api
- collection_type: open
  name: AutoContent Content Video API
  slug: open-autocontent-api-video-api
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
  url: https://docs.autocontentapi.com/
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
  type: LLMsTxt
  url: https://autocontentapi.com/llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://autocontentapi.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://autocontentapi.com/developers/api
- group: start
  title: ''
  type: GettingStarted
  url: https://autocontentapi.com/developers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autocontentapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autocontentapi.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/autocontent-api-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/autocontent-api-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/autocontent-api-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/autocontent-api-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/autocontent-api-tool-crosswalk.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/autocontent-api-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/autocontent-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/autocontent-api-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/autocontent-api-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/autocontent-api-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/autocontent-api-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/autocontent-api-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/autocontent-api-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/autocontent-api-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/autocontent-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/autocontent-api-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
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
mcp_servers:
- description: 'AutoContent API runs TWO distinct hosted MCP services on mcp.autocontentapi.com. The Platform MCP at /v1 is the current one: Streamable HTTP, OAuth-only, sharing the Platform REST API''s audience and s'
  name: AutoContent API MCP Server
  slug: autocontent-api-mcp-server
modified: '2026-09-04'
name: AutoContent API
nav: Providers
network: true
overview: 'AutoContent API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Content API, Dedicated Account API, Podcast API, and 4 more. Tagged areas include Artificial Intelligence, Audio, Content Generation, Podcasts, and Video.


  The AutoContent API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AutoContent API''s developer surface includes authentication, engineering blog, documentation, signup flow, pricing, API reference, getting-started guide, and 24 more developer resources.'
plans:
- name: Autocontent Api Plans Pricing
  plan_count: 4
  slug: autocontent-api-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 9
  name: Autocontent Api Rate Limits
  slug: autocontent-api-rate-limits
scopes:
- name: Autocontent Api Scopes
  scope_count: 0
  slug: autocontent-api-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 22.7
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 8.5
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 20.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/autocontent-api/refs/heads/main/screenshots/autocontent-api-2026-06-20T172653.png
security:
- kind: authentication
  name: Autocontent Api Authentication
  slug: autocontent-api-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Autocontent Api Domain Security
  slug: autocontent-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autocontent-api
tags:
- Artificial Intelligence
- Audio
- Content Generation
- Podcasts
- Video
- Generative AI
- Text-to-Speech
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
