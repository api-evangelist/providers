---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 66.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 78
  human_in_the_loop: 5
  name: Autocontent Api Agentic Access
  operation_count: 165
  slug: autocontent-api-agentic-access
  summary_line: 165 operations · 78 acting · 5 human-in-the-loop
api_count: 3
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
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The account API from AutoContent API — 1 operation(s) for account.
  name: AutoContent API Account API
  slug: autocontent-api-account-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The api-keys API from AutoContent API — 2 operation(s) for api-keys.
  name: AutoContent API API Keys API
  slug: autocontent-api-api-keys-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The asset-types API from AutoContent API — 1 operation(s) for asset-types.
  name: AutoContent API Asset Types API
  slug: autocontent-api-asset-types-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The assets API from AutoContent API — 3 operation(s) for assets.
  name: AutoContent API Assets API
  slug: autocontent-api-assets-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The avatars API from AutoContent API — 2 operation(s) for avatars.
  name: AutoContent API Avatars API
  slug: autocontent-api-avatars-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: Billing and invoices operations
  name: AutoContent API Billing API
  slug: autocontent-api-billing-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The collections API from AutoContent API — 1 operation(s) for collections.
  name: AutoContent API Collections API
  slug: autocontent-api-collections-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The content-loop-runs API from AutoContent API — 2 operation(s) for content-loop-runs.
  name: AutoContent API Content Loop Runs API
  slug: autocontent-api-content-loop-runs-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The content-loops API from AutoContent API — 4 operation(s) for content-loops.
  name: AutoContent API Content Loops API
  slug: autocontent-api-content-loops-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: Data table assets generated per token
  name: AutoContent API Data Tables API
  slug: autocontent-api-data-tables-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: Advanced research operations
  name: AutoContent API Deep Research API
  slug: autocontent-api-deep-research-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: Briefing document assets generated per token
  name: AutoContent API Documents API
  slug: autocontent-api-documents-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: Social media feed management operations
  name: AutoContent API Feeds API
  slug: autocontent-api-feeds-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: Upload and manage private files for resources
  name: AutoContent API Files API
  slug: autocontent-api-files-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The generations API from AutoContent API — 6 operation(s) for generations.
  name: AutoContent API Generations API
  slug: autocontent-api-generations-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: Infographic assets generated per token
  name: AutoContent API Infographics API
  slug: autocontent-api-infographics-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The models API from AutoContent API — 1 operation(s) for models.
  name: AutoContent API Models API
  slug: autocontent-api-models-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: Project context management for content generation
  name: AutoContent API Projects API
  slug: autocontent-api-projects-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The Public API from AutoContent API — 4 operation(s) for public.
  name: AutoContent API Public API
  slug: autocontent-api-public-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: Quiz assets generated per token
  name: AutoContent API Quizzes API
  slug: autocontent-api-quizzes-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: Slide deck assets generated per token
  name: AutoContent API Slide Decks API
  slug: autocontent-api-slide-decks-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The sources API from AutoContent API — 2 operation(s) for sources.
  name: AutoContent API Sources API
  slug: autocontent-api-sources-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The voices API from AutoContent API — 2 operation(s) for voices.
  name: AutoContent API Voices API
  slug: autocontent-api-voices-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: The webhooks API from AutoContent API — 2 operation(s) for webhooks.
  name: AutoContent API Webhooks API
  slug: autocontent-api-webhooks-api
- baseURL: https://api.autocontentapi.com
  baseurl_source: declared
  description: X (Twitter) operations
  name: AutoContent API X API
  slug: autocontent-api-x-api
artifact_total: 71
asyncapis:
- description: ''
  name: Autocontent Api Webhooks
  slug: autocontent-api-webhooks
collections:
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
- group: commercial
  href: https://artifacts.apis.io/autocontent-api/finops/autocontent-api-finops.yml
  title: ''
  type: FinOps
  url: finops/autocontent-api-finops.yml
- group: other
  href: https://artifacts.apis.io/autocontent-api/capabilities/autocontent-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/autocontent-api-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/autocontent-api/overlays/autocontent-api-platform-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/autocontent-api-platform-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/autocontent-api/overlays/autocontent-api-legacy-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/autocontent-api-legacy-content-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/autocontent-api/agentic-access/autocontent-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/autocontent-api-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/autocontent-api/security/autocontent-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autocontent-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/autocontent-api/authentication/autocontent-api-authentication.yml
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
  href: https://artifacts.apis.io/autocontent-api/packages/autocontent-api-packages.yml
  title: ''
  type: Packages
  url: packages/autocontent-api-packages.yml
- group: build
  href: https://artifacts.apis.io/autocontent-api/cli/autocontent-api-cli.yml
  title: ''
  type: CLI
  url: cli/autocontent-api-cli.yml
- group: agent
  href: https://artifacts.apis.io/autocontent-api/well-known/autocontent-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autocontent-api-well-known.yml
- group: agent
  href: https://artifacts.apis.io/autocontent-api/mcp/autocontent-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/autocontent-api-mcp.yml
- group: build
  href: https://artifacts.apis.io/autocontent-api/mcp/autocontent-api-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/autocontent-api-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/autocontent-api/conformance/autocontent-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autocontent-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/autocontent-api/errors/autocontent-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/autocontent-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/autocontent-api/lifecycle/autocontent-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/autocontent-api-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/autocontent-api/lifecycle/autocontent-api-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/autocontent-api-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/autocontent-api/scopes/autocontent-api-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/autocontent-api-scopes.yml
- group: design
  href: https://artifacts.apis.io/autocontent-api/conventions/autocontent-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/autocontent-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/autocontent-api/conventions/autocontent-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/autocontent-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/autocontent-api/data-model/autocontent-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/autocontent-api-data-model.yml
- group: design
  href: https://artifacts.apis.io/autocontent-api/asyncapi/autocontent-api-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/autocontent-api-webhooks.yml
- group: commercial
  href: https://artifacts.apis.io/autocontent-api/plans/autocontent-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autocontent-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/autocontent-api/rate-limits/autocontent-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/autocontent-api-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/autocontent-api/skills/_index.yml
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
- has_sources: true
  method: derived
  name: Autocontent Api Finops
  primary_unit: license
  service_category: ''
  slug: autocontent-api-finops
  template: false
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
  slug: autocontent-api-mcp-yml
modified: '2026-09-04'
name: AutoContent API
nav: Providers
network: true
overview: 'AutoContent API publishes 34 API contracts indexed on the [APIs.io](https://apis.io/) network, including Content API, Dedicated Account API, Podcast API, and 31 more. Tagged areas include Artificial Intelligence, Audio, Content Generation, Podcasts, and Video.


  The AutoContent API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  AutoContent API''s developer surface includes authentication, engineering blog, documentation, signup flow, pricing, API reference, getting-started guide, and 28 more developer resources.'
plans:
- name: Autocontent Api Plans Pricing
  plan_count: 4
  slug: autocontent-api-plans-pricing
- name: Autocontent Api Price Estimates
  plan_count: 0
  slug: autocontent-api-price-estimates
random_paper: 3
rate_limits:
- limit_count: 9
  name: Autocontent Api Rate Limits
  slug: autocontent-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: AutoContent API API Rules
  rule_count: 55
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 8
  slug: autocontent-api-rules
scopes:
- name: Autocontent Api Scopes
  scope_count: 8
  slug: autocontent-api-scopes
  summary_line: 8 scopes
score:
  band: strong
  composite: 63.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 71.5
    catalog_earned_first_party: 24.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 59.6
    developer_ergonomics: 61.3
    discoverability: 80.0
    operational_transparency: 47.4
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 86.7
      total: 30
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/autocontent-api/autocontent-api-2026-06-20T172653.png
security:
- kind: authentication
  name: Autocontent Api Authentication
  slug: autocontent-api-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Autocontent Api Domain Security
  slug: autocontent-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: autocontent-api-consume-webhooks
  slug: autocontent-api-consume-webhooks
- name: autocontent-api-generate-assets
  slug: autocontent-api-generate-assets
- name: autocontent-api-recover-from-errors
  slug: autocontent-api-recover-from-errors
- name: autocontent-api-run-content-loop
  slug: autocontent-api-run-content-loop
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
