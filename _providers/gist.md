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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.3
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Publisher ingest API for the Gist Content Network. Lets publisher partners push articles to ProRata in real time (`POST /ingest/article`) or in bulk for archival backfill (`POST /ingest/multiple_artic
  name: Gist Content API
  slug: gist-content-api
- description: Advertising delivery surface for Gist Ads. Publishers load the `adtag.js` bundle from tp-at.prorata.ai and call `window.prtag.defineSlot({id, api_key, url, geo}, slotId, sizes, adTypes)` to request co
  name: Gist Ads Ad Tag and Display Ad API
  slug: gist-ads-ad-tag-and-display-ad-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Chat API from Gist — 5 operation(s) for chat.
  name: Gist Chat API
  slug: gist-chat-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Health API from Gist — 1 operation(s) for health.
  name: Gist Health API
  slug: gist-health-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Publishers API from Gist — 2 operation(s) for publishers.
  name: Gist Publishers API
  slug: gist-publishers-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Questions API from Gist — 2 operation(s) for questions.
  name: Gist Questions API
  slug: gist-questions-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Root API from Gist — 1 operation(s) for root.
  name: Gist Root API
  slug: gist-root-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Summaries API from Gist — 2 operation(s) for summaries.
  name: Gist Summaries API
  slug: gist-summaries-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Threads API from Gist — 2 operation(s) for threads.
  name: Gist Threads API
  slug: gist-threads-api
artifact_total: 18
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
  name: Gist MCP Server
  slug: gist-mcp-server
modified: '2026-08-12'
name: Gist
nav: Providers
network: true
overview: 'Gist publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Health API, Publishers API, and 4 more. Tagged areas include Company, Artificial Intelligence, Generative AI, Advertising, and Marketing.


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
  composite: 41.1
  coverage:
    artifact_dirs: 23
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 51.3
    developer_ergonomics: 62.5
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 41.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
