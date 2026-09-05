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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aligned News Agentic Access
  operation_count: 11
  slug: aligned-news-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- description: Reference Model Context Protocol server distributed as a single TypeScript file (mcp-server.ts) that proxies the Aligned News REST API to MCP-compatible AI tools like Claude Code, Claude Desktop, Curs
  name: Aligned News MCP Server
  slug: aligned-news-mcp-server
- baseURL: https://alignednews.com/v1
  baseurl_source: declared
  description: Curated groupings of related stories around themes.
  name: Aligned News Bundles API
  slug: aligned-news-bundles-api
- baseURL: https://alignednews.com/v1
  baseurl_source: declared
  description: All current stories grouped by section.
  name: Aligned News News Feed API
  slug: aligned-news-news-feed-api
- baseURL: https://alignednews.com/v1
  baseurl_source: declared
  description: Trend deep-dives and longer-form analysis.
  name: Aligned News Reports API
  slug: aligned-news-reports-api
- baseURL: https://alignednews.com/v1
  baseurl_source: declared
  description: Full-text search across stories, signals, and reports.
  name: Aligned News Search API
  slug: aligned-news-search-api
- baseURL: https://alignednews.com/v1
  baseurl_source: declared
  description: Topical sections used to organize stories.
  name: Aligned News Sections API
  slug: aligned-news-sections-api
- baseURL: https://alignednews.com/v1
  baseurl_source: declared
  description: Early pattern detections with editorial badges.
  name: Aligned News Signals API
  slug: aligned-news-signals-api
- baseURL: https://alignednews.com/v1
  baseurl_source: declared
  description: AI news stories curated and synthesized from monitored accounts.
  name: Aligned News Stories API
  slug: aligned-news-stories-api
artifact_total: 60
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Aligned News REST Bundles API
  slug: open-aligned-news-bundles-api
- collection_type: open
  name: Aligned News REST Bundles News Feed API
  slug: open-aligned-news-news-feed-api
- collection_type: open
  name: Aligned News REST Bundles Reports API
  slug: open-aligned-news-reports-api
- collection_type: open
  name: Aligned News REST Bundles Search API
  slug: open-aligned-news-search-api
- collection_type: open
  name: Aligned News REST Bundles Sections API
  slug: open-aligned-news-sections-api
- collection_type: open
  name: Aligned News REST Bundles Signals API
  slug: open-aligned-news-signals-api
- collection_type: open
  name: Aligned News REST Bundles Stories API
  slug: open-aligned-news-stories-api
- collection_type: open
  name: Aligned News REST API
  slug: open-aligned-news
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aligned-news-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aligned-news-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aligned-news-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://alignednews.com/
- group: other
  title: ''
  type: How It Works
  url: https://alignednews.com/how-it-works
- group: start
  title: ''
  type: GettingStarted
  url: https://alignednews.com/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://alignednews.com/pricing
- group: other
  title: ''
  type: Developers
  url: https://alignednews.com/developers
- group: start
  title: ''
  type: Signup
  url: https://alignednews.com/account
- group: other
  title: ''
  type: Sitemap
  url: https://alignednews.com/sitemap.xml
- group: other
  title: ''
  type: Robots TXT
  url: https://alignednews.com/robots.txt
- group: other
  title: ''
  type: Research
  url: https://alignednews.com/research
- group: other
  title: ''
  type: Signals
  url: https://alignednews.com/signals
- group: other
  title: ''
  type: Reports
  url: https://alignednews.com/reports
- group: other
  title: ''
  type: Bundles
  url: https://alignednews.com/bundles
- group: other
  title: ''
  type: AI
  url: https://alignednews.com/ai
- group: agent
  title: ''
  type: MCP Server
  url: https://alignednews.com/mcp-server.ts
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Aligned-news
- group: company
  title: ''
  type: Blog
  url: https://alignednews.com/feed
created: '2026-05-06'
description: Aligned News is an AI-native intelligence and news platform that synthesizes AI-powered briefings from 63 curated X lists tracking 100,000+ accounts in AI, tech, and science, and publishes Stories, Signals, Reports, and Bundles via web, REST API, and a downloadable MCP server for AI tools like Claude, Cursor, and Windsurf.
examples:
- key_count: 1
  name: Aligned News Getbundle Example
  slug: aligned-news-getBundle-example
- key_count: 1
  name: Aligned News Getnewsfeed Example
  slug: aligned-news-getNewsFeed-example
- key_count: 1
  name: Aligned News Getreport Example
  slug: aligned-news-getReport-example
- key_count: 1
  name: Aligned News Getsignal Example
  slug: aligned-news-getSignal-example
- key_count: 1
  name: Aligned News Getstory Example
  slug: aligned-news-getStory-example
- key_count: 1
  name: Aligned News Listbundles Example
  slug: aligned-news-listBundles-example
- key_count: 1
  name: Aligned News Listreports Example
  slug: aligned-news-listReports-example
- key_count: 1
  name: Aligned News Listsections Example
  slug: aligned-news-listSections-example
- key_count: 1
  name: Aligned News Listsignals Example
  slug: aligned-news-listSignals-example
- key_count: 1
  name: Aligned News Liststories Example
  slug: aligned-news-listStories-example
- key_count: 1
  name: Aligned News Searchcontent Example
  slug: aligned-news-searchContent-example
features:
- AI-powered intelligence from 63 curated X lists
- Tracks 100,000+ accounts across AI, technology, and science
- Stories surface breaking AI news with full body content
- Signals provide early pattern detection with badges (bullish, caution, critical, signal, interview, vc, action)
- Reports deliver trend deep-dives and summaries
- Bundles group related stories around themes
- Section-organized news feed across all topics
- Full-text Search across stories, signals, and reports
- REST API gated behind Pro tier with Bearer alnw_ API keys
- Downloadable single-file MCP server for Claude Code, Claude Desktop, Cursor, and Windsurf
- Free tier exposes headlines, summaries, signal badges, and report summaries only
- Pro tier unlocks full content + API access
- Enterprise tier adds team access, priority support, and custom analysis
- Built on Fly.io (edge), Supabase (data), Clerk (auth and billing), Stripe (payments)
finops:
- name: Aligned News Finops
  service_category: AI News Intelligence
  slug: aligned-news-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aligned-news.png
json_schemas:
- name: Bundle
  property_count: 5
  slug: aligned-news-bundle
- name: Report
  property_count: 6
  slug: aligned-news-report
- name: Section
  property_count: 3
  slug: aligned-news-section
- name: Signal
  property_count: 8
  slug: aligned-news-signal
- name: Story
  property_count: 9
  slug: aligned-news-story
json_structures:
- name: Aligned News Bundle Structure
  property_count: 5
  slug: aligned-news-bundle-structure
- name: Aligned News Report Structure
  property_count: 6
  slug: aligned-news-report-structure
- name: Aligned News Section Structure
  property_count: 3
  slug: aligned-news-section-structure
- name: Aligned News Signal Structure
  property_count: 8
  slug: aligned-news-signal-structure
- name: Aligned News Story Structure
  property_count: 9
  slug: aligned-news-story-structure
jsonld:
- class_count: 18
  name: Aligned News Context
  property_count: 9
  slug: aligned-news-context
layout: provider
modified: '2026-07-25'
name: Aligned News
nav: Providers
network: true
overview: 'Aligned News publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bundles API, News Feed API, Reports API, and 4 more. Tagged areas include Artificial Intelligence, News, Intelligence, MCP, and Signals.


  The Aligned News catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aligned News'' developer surface includes authentication, getting-started guide, pricing, signup flow, engineering blog, and 14 more developer resources.'
plans:
- name: Aligned News Plans Pricing
  plan_count: 3
  slug: aligned-news-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Aligned News Rate Limits
  slug: aligned-news-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Aligned News API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aligned-news-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 75.3
    catalog_earned_first_party: 0.0
    catalog_gap: 39.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 9.8
    contract_quality: 63.5
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aligned-news/refs/heads/main/screenshots/aligned-news-2026-06-20T171522.png
security:
- kind: authentication
  name: Aligned News Authentication
  slug: aligned-news-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aligned News Domain Security
  slug: aligned-news-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aligned-news
tags:
- Artificial Intelligence
- News
- Intelligence
- MCP
- Signals
website: https://alignednews.com/
---
