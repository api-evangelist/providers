---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Philadelphia Inquirer Agentic Access
  operation_count: 11
  slug: philadelphia-inquirer-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 3
apis:
- baseURL: https://www.inquirer.com/arc/outboundfeeds/rss
  baseurl_source: declared
  description: Site-wide and per-category RSS feeds.
  name: The Philadelphia Inquirer Feeds API
  slug: philadelphia-inquirer-feeds-api
- baseURL: https://www.inquirer.com/arc/outboundfeeds/rss
  baseurl_source: declared
  description: Liveness and readiness probes.
  name: The Philadelphia Inquirer Health API
  slug: philadelphia-inquirer-health-api
- baseURL: https://www.inquirer.com/arc/outboundfeeds/rss
  baseurl_source: declared
  description: Model Context Protocol surface.
  name: The Philadelphia Inquirer MCP API
  slug: philadelphia-inquirer-mcp-api
- baseURL: https://www.inquirer.com/arc/outboundfeeds/rss
  baseurl_source: declared
  description: XML sitemaps and sitemap indexes.
  name: The Philadelphia Inquirer Sitemaps API
  slug: philadelphia-inquirer-sitemaps-api
artifact_total: 49
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dewey MCP
  slug: open-dewey-mcp
- collection_type: open
  name: Dewey MCP Feeds API
  slug: open-philadelphia-inquirer-feeds-api
- collection_type: open
  name: Dewey MCP Feeds Health API
  slug: open-philadelphia-inquirer-health-api
- collection_type: open
  name: Dewey Feeds MCP API
  slug: open-philadelphia-inquirer-mcp-api
- collection_type: open
  name: Dewey MCP Feeds Sitemaps API
  slug: open-philadelphia-inquirer-sitemaps-api
- collection_type: open
  name: The Philadelphia Inquirer RSS Feeds
  slug: open-rss
- collection_type: open
  name: The Philadelphia Inquirer Sitemaps
  slug: open-sitemaps
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/phillymedia/dewey-mcp/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/phillymedia/dewey-mcp/blob/main/docs/contributing.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/philadelphia-inquirer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/philadelphia-inquirer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.inquirer.com
- group: company
  title: ''
  type: About
  url: https://about.inquirer.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phillymedia
- group: other
  title: iOS App
  type: MobileApp
  url: https://apps.apple.com/us/app/the-philadelphia-inquirer/id1495601779
- group: other
  title: Android App
  type: MobileApp
  url: https://play.google.com/store/apps/details?id=com.philly.philly_native_android
- group: company
  title: ''
  type: Newsletter
  url: https://www.inquirer.com/newsletters/
- group: other
  title: ''
  type: Subscribe
  url: https://www.inquirer.com/subscribe/
- group: company
  title: ''
  type: Careers
  url: https://www.inquirer.com/careers/
- group: other
  title: The Lenfest Institute for Journalism
  type: ParentOrganization
  url: https://www.lenfestinstitute.org
- group: other
  title: ''
  type: Customers
  url: ''
- group: other
  title: ''
  type: Awards
  url: ''
- group: build
  title: Dewey MCP Server
  type: GitHubRepository
  url: https://github.com/phillymedia/dewey-mcp
- group: build
  title: Dewey AI Librarian
  type: GitHubRepository
  url: https://github.com/phillymedia/dewey-ai
- group: build
  title: Vestapol (web data to SQL)
  type: GitHubRepository
  url: https://github.com/phillymedia/vestapol
- group: build
  title: Inquirer Data Engineering Handbook
  type: GitHubRepository
  url: https://github.com/phillymedia/data-engineering-handbook
- group: build
  title: Inquirer API GitHub Pages (Swagger UI shell, unconfigured)
  type: GitHubRepository
  url: https://github.com/phillymedia/inquirer-api.github.io
- group: other
  title: ''
  type: X
  url: https://x.com/PhillyInquirer
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/philly.com
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/phillyinquirer/
- group: company
  title: ''
  type: Blog
  url: https://www.inquirer.com/arc/outboundfeeds/rss/?outputType=xml
created: '2026-05-23'
description: The Philadelphia Inquirer is the largest newspaper in Pennsylvania, owned by the nonprofit Lenfest Institute for Journalism. Inquirer.com publishes Philadelphia, regional, national, and world news, sports, business, opinion, arts, food, and obituaries. The Inquirer does not operate a public commercial developer program. Programmatic surfaces are limited to Arc XP-generated RSS feeds, news sitemaps, and a small set of open-source repositories from its `phillymedia` GitHub organization, including the `dewey-mcp` Model Context Protocol server that wraps an Azure AI Search index of the Inquirer archive.
examples:
- key_count: 2
  name: Dewey Mcp Searcharchive Example
  slug: dewey-mcp-searchArchive-example
- key_count: 2
  name: Rss Getcategoryrssfeed Example
  slug: rss-getCategoryRssFeed-example
- key_count: 2
  name: Rss Getsiterssfeed Example
  slug: rss-getSiteRssFeed-example
- key_count: 2
  name: Sitemaps Getnewssitemap Example
  slug: sitemaps-getNewsSitemap-example
- key_count: 2
  name: Sitemaps Getsitemapindex Example
  slug: sitemaps-getSitemapIndex-example
features:
- description: Site-wide and per-category RSS 2.0 feeds generated by Arc XP outbound feeds, updated hourly.
  name: RSS Feeds
- description: Google News sitemap exposing the most recent articles for crawler discovery.
  name: News Sitemap
- description: Sitemap index with hundreds of dated child sitemaps spanning roughly two years of inquirer.com URLs.
  name: Sitemap Index
- description: LLM-powered archive search assistant built on Azure OpenAI, Azure AI Search, and Azure Blob Storage; cites article sources.
  name: Dewey AI Librarian
- description: FastMCP server exposing a single `search_archive` tool over the Inquirer archive index.
  name: Dewey MCP Server
- description: Native iOS and Android apps for reading Inquirer.com content.
  name: Mobile Apps
- description: Topical email newsletters across news, sports, business, food, and opinion.
  name: Newsletters
- description: Daily replica e-edition of the printed newspaper for subscribers.
  name: E-Edition
- description: Searchable obituaries and statutory legal notices sections.
  name: Obituaries and Legal Notices
finops:
- name: Philadelphia Inquirer Finops
  service_category: ''
  slug: philadelphia-inquirer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/philadelphia-inquirer.png
integrations:
- description: Inquirer.com is published on Arc Publishing (Arc XP); RSS and sitemap surfaces are generated by Arc's outbound feeds.
  name: Arc XP
- description: Dewey indexes Inquirer articles into Azure AI Search and queries it via the FastMCP server.
  name: Azure AI Search
- description: Dewey AI uses Azure OpenAI for embeddings and chat completions over retrieved article chunks.
  name: Azure OpenAI
- description: The Inquirer's Data Engineering team uses dbt as a primary transformation tool, per the public data-engineering-handbook.
  name: dbt
- description: dbt models target BigQuery as the analytics warehouse.
  name: BigQuery
- description: The Inquirer is a founding member of Spotlight PA, a Pennsylvania investigative-journalism collaboration.
  name: Spotlight PA
json_schemas:
- name: Dewey Search Result
  property_count: 8
  slug: dewey-search-result
- name: Philadelphia Inquirer RSS Item
  property_count: 8
  slug: rss-item
- name: Philadelphia Inquirer Sitemap URL
  property_count: 5
  slug: sitemap-url
json_structures:
- name: Rss Item Structure
  property_count: 0
  slug: rss-item-structure
jsonld:
- class_count: 0
  name: Philadelphia Inquirer Context
  property_count: 5
  slug: philadelphia-inquirer-context
layout: provider
modified: '2026-05-23'
name: The Philadelphia Inquirer
nav: Providers
network: true
overview: 'The Philadelphia Inquirer publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Feeds API, Health API, MCP API, and 1 more. Tagged areas include News, News Media, Newspaper, Journalism, and Philadelphia.


  The The Philadelphia Inquirer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  The Philadelphia Inquirer''s developer surface includes engineering blog and 21 more developer resources.'
plans:
- name: Philadelphia Inquirer Plans Pricing
  plan_count: 1
  slug: philadelphia-inquirer-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Philadelphia Inquirer Rate Limits
  slug: philadelphia-inquirer-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: The Philadelphia Inquirer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: philadelphia-inquirer-jsonschema-spectral-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: The Philadelphia Inquirer API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: rss-rules
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 54.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 52.7
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 2.6
  open_source:
    applies: true
    score: 25.0
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/philadelphia-inquirer/refs/heads/main/screenshots/philadelphia-inquirer-2026-06-20T191649.png
security:
- kind: domain-security
  name: Philadelphia Inquirer Domain Security
  slug: philadelphia-inquirer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: philadelphia-inquirer
tags:
- News
- News Media
- Newspaper
- Journalism
- Philadelphia
- Pennsylvania
- Local News
- RSS
- Sitemap
- Arc Publishing
- MCP
use_cases:
- description: Aggregators and readers pull Inquirer headlines and full article HTML via RSS feeds.
  name: News Aggregation
- description: Google News, Bing, and other crawlers consume the news sitemap and sitemap index for article discovery.
  name: Search Engine Indexing
- description: Newsroom staff and partners search the Inquirer archive via the Dewey AI librarian and Dewey MCP.
  name: Local Journalism Archive Search
- description: AI agents that speak MCP can connect to Dewey MCP to query the Inquirer archive as part of larger research workflows.
  name: AI Agent Integration
- description: Per-category RSS feeds (sports, politics, business, opinion) power topical syndication on third-party sites.
  name: Sports and Politics Syndication
website: https://www.inquirer.com
---
