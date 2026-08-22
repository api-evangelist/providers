---
access_model:
  confidence: medium
  label: Onboarding required
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://platform.gist.ai/docs/gist-content-api
  - https://platform.gist.ai/docs/about-gist-services
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.4
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: REST API behind Gist Answers. Creates chats against a publisher's licensed corpus, streams the answer back over Server-Sent Events, and returns the citations and the per-source attribution credit dist
  name: Gist Answers API (Prorata API Service)
  slug: gist-answers-api-prorata-api-service
- description: Publisher ingest API for the Gist Content Network. Lets publisher partners push articles to ProRata in real time (`POST /ingest/article`) or in bulk for archival backfill (`POST /ingest/multiple_artic
  name: Gist Content API
  slug: gist-content-api
- description: Advertising delivery surface for Gist Ads. Publishers load the `adtag.js` bundle from tp-at.prorata.ai and call `window.prtag.defineSlot({id, api_key, url, geo}, slotId, sizes, adTypes)` to request co
  name: Gist Ads Ad Tag and Display Ad API
  slug: gist-ads-ad-tag-and-display-ad-api
artifact_total: 12
collections:
- collection_type: open
  name: Prorata API Service
  slug: open-gist-answers-api
common:
- group: company
  title: ''
  type: Website
  url: https://gist.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.gist.ai/docs/about-gist-services
- group: docs
  title: ''
  type: Documentation
  url: https://platform.gist.ai/docs/about-gist-services
- group: docs
  title: ''
  type: APIReference
  url: https://platform.gist.ai/reference/get_v1-health
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.gist.ai/docs/quick-start-using-widgets
- group: company
  title: ''
  type: Blog
  url: https://gist.ai/get-the-gist
- group: operate
  title: ''
  type: Support
  url: https://gist.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Prorata-ai
- group: start
  title: ''
  type: Login
  url: https://console.gist.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gist.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gist.ai/terms-of-use
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gist-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/gist-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gist-packages.yml
- group: design
  title: ''
  type: Components
  url: components/gist-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gist-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gist-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gist-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gist-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gist-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gist-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gist-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gist-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gist-data-model.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gist-attribution-extension.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gist-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/gist-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gist-answers-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gist-domain-security.yml
created: '2026-07-17'
description: 'Gist is an AI brand-visibility, answer-engine and content-monetization platform built by ProRata (founded 2024) that helps publishers and advertisers stay visible, measurable and monetizable inside generative AI experiences. It ships three products: Gist GEO (generative engine optimization for consistent organic visibility in AI answers), Gist Ads (paid brand amplification placed directly in AI search surfaces, with native iOS and Android ad SDKs and a publisher ad tag), and Gist Answers (an embeddable, publisher-backed AI answer engine for on-site engagement and monetization). Behind those products sits a real developer surface documented at the Gist Developer Hub: the Prorata API Service (chat, streaming completions, citations, per-source attribution, threads, recommended and related questions, publisher management and document summarization) at api.gist.ai, the Gist Content API for publisher article ingestion, the Gist Content Network crawler and CMS/RSS ingestion paths,
  and the gist-chat-widget web component distributed from cdn.gist.ai. Gist positions itself as turning AI from a black box into a measurable, actionable channel for brands and content owners, with fair attribution and a 50/50 publisher revenue share as the stated basis of the model.'
image: https://cdn.prod.website-files.com/69b4128468609a447fd7dd25/6a05c44830dff65379b10594_512x512.png
json_schemas:
- name: Fractional Attribution Extension - definitions
  property_count: 0
  slug: gist-attribution-extension
- name: Fractional Attribution Standalone Report
  property_count: 7
  slug: gist-attribution-report
- name: Content Telemetry Session with Fractional Attribution (strict)
  property_count: 0
  slug: gist-attribution-session-strict
layout: provider
mcp_servers:
- description: ''
  name: gist-mcp.yml
  slug: gist-mcpyml
modified: '2026-08-12'
name: Gist
nav: Providers
network: true
overview: 'Gist publishes 1 API on the [APIs.io](https://apis.io/) network: Answers API (Prorata API Service). Tagged areas include Company, Artificial Intelligence, Generative AI, Advertising, and Marketing.


  Gist''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, sandbox, authentication, and 23 more developer resources.'
plans:
- name: Gist Plans Pricing
  plan_count: 0
  slug: gist-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Gist Rate Limits
  slug: gist-rate-limits
score:
  band: developing
  composite: 43.9
  delta: -5.7
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 16.7
    contract_quality: 54.2
    developer_ergonomics: 62.5
    discoverability: 72.2
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 49.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/gist/refs/heads/main/screenshots/gist-2026-07-25T215832.png
security:
- kind: authentication
  name: Gist Authentication
  slug: gist-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gist Domain Security
  slug: gist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gist
tags:
- Company
- Artificial Intelligence
- Generative AI
- Advertising
- Marketing
- Brand Visibility
- Publishers
- Search
- Content
- Answer Engine
- Attribution
- Content Licensing
- Media
- RAG
- Advertising Technology
website: https://gist.ai
---
