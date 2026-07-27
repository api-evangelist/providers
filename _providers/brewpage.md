---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Brewpage Agentic Access
  operation_count: 36
  slug: brewpage-agentic-access
  summary_line: 36 operations · 15 acting
api_count: 13
apis:
- description: File hosting up to 5 MB per file, 1000 files per namespace
  name: BrewPage Files API
  slug: brewpage-files-api
- description: Browse public content from the 'public' namespace without password protection
  name: BrewPage Gallery API
  slug: brewpage-gallery-api
- description: HTML page hosting with markdown support
  name: BrewPage HTML API
  slug: brewpage-html-api
- description: JSON document store with up to 10,000 docs per collection
  name: BrewPage JSON API
  slug: brewpage-json-api
- description: Key-Value store with up to 1000 keys per namespace
  name: BrewPage KV API
  slug: brewpage-kv-api
- description: Fresh, collision-free namespace suggestions
  name: BrewPage Namespace API
  slug: brewpage-namespace-api
- description: Lightweight owner-token probe; never increments views or returns content
  name: BrewPage Owner Check API
  slug: brewpage-owner-check-api
- description: OpenGraph metadata for social bots
  name: BrewPage preview API
  slug: brewpage-preview-api
- description: Abuse reports for hosted content
  name: BrewPage Reports API
  slug: brewpage-reports-api
- description: Search engine optimization endpoints
  name: BrewPage SEO API
  slug: brewpage-seo-api
- description: Short URL resolver for sharing
  name: BrewPage Short Links API
  slug: brewpage-short-links-api
- description: Multi-file HTML site hosting via ZIP or folder upload
  name: BrewPage Sites API
  slug: brewpage-sites-api
- description: Platform-wide usage statistics
  name: BrewPage Stats API
  slug: brewpage-stats-api
artifact_total: 68
collections:
- collection_type: open
  name: BrewPage API
  slug: open-brewpage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brewpage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brewpage-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://brewpage.app/api
- group: docs
  title: ''
  type: APIReference
  url: https://kochetkov-ma.github.io/brewpage-openapi/
- group: start
  title: ''
  type: Portal
  url: https://brewpage.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://brewpage.app/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://brewpage.app/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: https://brewpage.app/llms-full.txt
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/brewpage-mcp
- group: commercial
  title: ''
  type: Plans
  url: plans/brewpage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brewpage-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brewpage-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/brewpage-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/brewpage-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/brewpage-context.jsonld
created: '2026-05-16'
description: 'BrewPage is a free, no-registration instant hosting service for HTML pages, Markdown documents, AI-agent artifacts, files, and multi-file static sites. It also offers a namespaced key-value store and a JSON document store. The REST API returns short, shareable HTTPS links (https://brewpage.app/{ns}/{id}) and an owner token used to update or delete content in place. BrewPage is designed to be AI-agent friendly: it provides an MCP server (brewpage-mcp), a Claude Code skill (brewdoc:publish), and a llms.txt manifest, and it requires a self-identifying User-Agent header on every request.'
examples:
- key_count: 2
  name: Brewpage Create Html Example
  slug: brewpage-create-html-example
- key_count: 2
  name: Brewpage Create Markdown Example
  slug: brewpage-create-markdown-example
- key_count: 2
  name: Brewpage Upload File Example
  slug: brewpage-upload-file-example
- key_count: 2
  name: Brewpage Upload Site Example
  slug: brewpage-upload-site-example
- key_count: 2
  name: Brewpage Upsert Kv Example
  slug: brewpage-upsert-kv-example
features:
- description: POST raw HTML or a JSON body to /api/html and receive a 10-char short URL at /{ns}/{id} with no signup.
  name: Instant HTML Hosting
- description: Pass `format=markdown` to publish Markdown that BrewPage renders to styled HTML at view time.
  name: Markdown Rendering
- description: Upload a ZIP archive or files+paths multipart to /api/sites; entry point auto-detected (index.html preferred); 20 MB / 100 files / 5 MB each.
  name: Multi-File Site Hosting
- description: Upload binary or text files via /api/files (5 MB max). Images, PDFs, video, and audio display inline; ?dl=1 forces download.
  name: File Hosting
- description: 1000-key namespaced KV stores via /api/kv with per-key PUT/GET/DELETE and per-store enumeration.
  name: Key-Value Store
- description: 10,000-document collections via /api/json with PUT-in-place semantics on stable short URLs.
  name: JSON Document Store
- description: PUT to /api/html, /api/json, and /api/kv replaces content while keeping the short URL — agents can iterate without breaking shared links.
  name: Update In Place
- description: Save the `ownerToken` returned at creation and reuse it via `X-Owner-Token` to group resources under one owner and scope list endpoints.
  name: Owner Token Grouping
- description: Set `X-Password` (min 4 chars) at creation to require the same header (or `?p=...`) for reads; passworded items are excluded from the gallery and sitemap.
  name: Password Protection
- description: GET /api/gallery surfaces content posted to the default `public` namespace without a password — searchable, social-bot friendly, OG-image generated.
  name: Public Gallery
- description: Per-content 1200×630 PNG at /preview/{ns}/{id}.png plus an /preview-html stub for social media unfurlers.
  name: OpenGraph Preview Images
- description: GET /{ns}/{id} returns the hosted content; GET /{ns}/{id}/{sub} resolves sub-paths inside multi-file sites.
  name: Short Link Resolver
- description: A byte-identical POST /api/html to `public/` within 24h returns the existing id (X-Existing-Resource header set) so retries do not duplicate gallery entries.
  name: Idempotent Owner Re-POST
- description: POST /api/reports lets readers report inappropriate or harmful content for moderation.
  name: Abuse Reports
- description: GET /api/namespace/random returns a fresh, collision-free kebab-case namespace suggestion.
  name: Random Namespace Suggestion
- description: GET /api/stats exposes platform-wide usage statistics; GET /api/sitemap.xml exposes a dynamic sitemap of public content.
  name: Platform Stats
- description: llms.txt and llms-full.txt manifests, an MCP server, a Claude Code skill, and required identifying User-Agent headers make BrewPage first-class for autonomous agents.
  name: AI-Agent Friendly
finops:
- name: Brewpage Finops
  service_category: Web Hosting and Storage
  slug: brewpage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brewpage.png
integrations:
- description: Official MCP server `brewpage-mcp` exposes BrewPage to any LLM/agent (Claude, Codex, Gemini, Cursor) via the Model Context Protocol.
  name: Model Context Protocol (MCP)
- description: Claude Code skill `brewdoc:publish` lets users publish from inside Claude Code via a slash command (claude-brewcode marketplace).
  name: Claude Code
- description: BrewPage submits public content to IndexNow for search engine discovery; PUT-based republish is recommended to preserve quota.
  name: IndexNow
- description: Every short URL exposes `/preview/{ns}/{id}.png` (1200×630) and a `/preview-html/{ns}/{id}` OG stub for link unfurling.
  name: OpenGraph / Social Bots
- description: Client-side syntax highlighting for known code/data file previews (JSON, XML, SVG, HTML, CSS, JS, TS, YAML, TOML, Markdown).
  name: Prism.js
- description: BrewPage publishes a /llms.txt and /llms-full.txt manifest for LLM-friendly discovery of the API surface.
  name: llms.txt
json_schemas:
- name: BrewPage File
  property_count: 13
  slug: brewpage-file
- name: BrewPage HTML Page
  property_count: 14
  slug: brewpage-html-page
- name: BrewPage JSON Document
  property_count: 10
  slug: brewpage-json-document
- name: BrewPage KV Store
  property_count: 9
  slug: brewpage-kv-store
- name: BrewPage Multi-File Site
  property_count: 12
  slug: brewpage-site
json_structures:
- name: Brewpage Html Page Structure
  property_count: 0
  slug: brewpage-html-page-structure
- name: Brewpage Kv Store Structure
  property_count: 0
  slug: brewpage-kv-store-structure
jsonld:
- class_count: 21
  name: Brewpage Context
  property_count: 9
  slug: brewpage-context
layout: provider
modified: '2026-05-19'
name: BrewPage
nav: Providers
network: true
overview: 'BrewPage publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Files API, Gallery API, HTML API, and 10 more. Tagged areas include Hosting, Markdown, HTML, AI Artifacts, and File Hosting.


  The BrewPage catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BrewPage''s developer surface includes documentation, API reference, developer portal, getting-started guide, authentication, and 10 more developer resources.'
plans:
- name: Brewpage Plans Pricing
  plan_count: 1
  slug: brewpage-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 11
  name: Brewpage Rate Limits
  slug: brewpage-rate-limits
rules:
- name: BrewPage API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: brewpage-jsonschema-spectral-rules
- name: BrewPage API Rules
  rule_count: 21
  severity_counts:
    error: 4
    hint: 0
    info: 3
    warn: 14
  slug: brewpage-rules
score:
  band: developing
  composite: 57.2
  delta: 5.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 65.8
    developer_ergonomics: 52.2
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 31.6
  previous_composite: 51.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/brewpage/refs/heads/main/screenshots/brewpage-2026-06-20T173653.png
security:
- kind: domain-security
  name: Brewpage Domain Security
  slug: brewpage-domain-security
  summary_line: TLSv1.3 · HSTS
slug: brewpage
solutions:
- description: Free HTML/Markdown publishing with short URL, OG images, and password gating.
  name: Hosted Web Page
- description: 5 MB files and 20 MB multi-file sites with TTL up to 30 days.
  name: Hosted Files And Sites
- description: KV stores (1000 keys) and JSON collections (10,000 docs) for stateful agent workflows.
  name: Agent State And Documents
- description: MCP server, Claude Code skill, llms.txt manifests, and identifying User-Agent contract.
  name: AI-Agent Integration
tags:
- Hosting
- Markdown
- HTML
- AI Artifacts
- File Hosting
- Developer Tools
use_cases:
- description: Drop a Markdown report, generated HTML page, or JSON artifact and share a short URL with a teammate or end user.
  name: Share AI-Agent Output
- description: Use PUT to refine content at the same short URL across multiple agent iterations without breaking previously shared links.
  name: Iterate On A Stable Link
- description: Upload a ZIP of a static site (docs, demo, status page) and get a 30-day-max hosted URL with relative links between files.
  name: Stand Up A One-Off Microsite
- description: Send a PDF, image, or archive (≤5 MB) to a recipient who shouldn't need to sign up — URL expires automatically.
  name: Ephemeral File Drop
- description: Use /api/kv as a free, server-side scratchpad for feature flags, session state, or memoized tool outputs (≤1000 keys per store).
  name: Scratch KV Storage For Agents
- description: Post to the default `public` namespace and let the gallery + sitemap + OG image expose your content to search engines and social.
  name: Public Knowledge Drop
- description: Apply X-Password to a hosted page or file for lightweight access control without user accounts.
  name: Password-Gated Share
website: https://brewpage.app/
---
