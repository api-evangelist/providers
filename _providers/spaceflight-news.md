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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Spaceflight News Agentic Access
  operation_count: 7
  slug: spaceflight-news-agentic-access
  summary_line: 7 operations
api_count: 5
apis:
- description: Sister API by The Space Devs, used by SNAPI to relate news articles to specific launches and events. Provides upcoming/previous launch data, events, agencies, astronauts, expeditions, spacecraft, laun
  name: Launch Library 2 API
  slug: launch-library-2-api
- description: News articles aggregated from 40+ spaceflight news sites.
  name: Spaceflight News Articles API
  slug: spaceflight-news-articles-api
- description: Blog posts and longform commentary from spaceflight publishers.
  name: Spaceflight News Blogs API
  slug: spaceflight-news-blogs-api
- description: API metadata, version, and the list of currently imported news sites.
  name: Spaceflight News Info API
  slug: spaceflight-news-info-api
- description: Official mission, program, and agency reports.
  name: Spaceflight News Reports API
  slug: spaceflight-news-reports-api
artifact_total: 50
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spaceflight News Articles API
  slug: open-spaceflight-news-articles-api
- collection_type: open
  name: Spaceflight News Articles Blogs API
  slug: open-spaceflight-news-blogs-api
- collection_type: open
  name: Spaceflight News Articles Info API
  slug: open-spaceflight-news-info-api
- collection_type: open
  name: Spaceflight News Articles Reports API
  slug: open-spaceflight-news-reports-api
- collection_type: open
  name: Spaceflight News API
  slug: open-spaceflight-news
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spaceflight-news-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spaceflight-news-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spaceflightnewsapi.net
- group: docs
  title: ''
  type: Documentation
  url: https://api.spaceflightnewsapi.net/v4/docs/
- group: other
  title: ''
  type: Repository
  url: https://github.com/TheSpaceDevs/spaceflightnewsapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheSpaceDevs
- group: commercial
  title: AGPL-3.0
  type: License
  url: https://github.com/TheSpaceDevs/spaceflightnewsapi/blob/main/LICENSE
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/TheSpaceDevs/spaceflightnewsapi/releases
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/the_snapi
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/p7ntkNA
- group: other
  title: Patreon (Funding)
  type: Patreon
  url: https://www.patreon.com/TheSpaceDevs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: learn
  title: TheSpaceDevs Tutorials & FAQs
  type: Tutorials
  url: https://github.com/TheSpaceDevs/Tutorials
- group: operate
  title: SNAPI FAQ
  type: FAQ
  url: https://github.com/TheSpaceDevs/Tutorials/blob/main/faqs/faq_SNAPI.md
- group: operate
  title: TSD FAQ
  type: FAQ
  url: https://github.com/TheSpaceDevs/Tutorials/blob/main/faqs/faq_TSD.md
- group: build
  title: Launch Library MCP Server
  type: Tools
  url: https://github.com/TheSpaceDevs/launch-library-mcp
- group: build
  title: SNAPI Website (snapiwebsite)
  type: Tools
  url: https://github.com/TheSpaceDevs/snapiwebsite
- group: build
  title: Serpy (Serialization Library)
  type: Tools
  url: https://github.com/TheSpaceDevs/serpy
- group: design
  title: ''
  type: SpectralRules
  url: rules/spaceflight-news-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spaceflight-news-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/spaceflight-news-context.jsonld
created: '2026-05-28'
description: The Spaceflight News API (SNAPI) by The Space Devs (TSD) is the most complete and up-to-date open spaceflight news API. It aggregates articles, blogs, and reports from 40+ news sites (NASA, ESA, SpaceX, Spaceflight Now, SpaceNews, Ars Technica, Reuters, and more) and exposes them through a public REST API (and a GraphQL endpoint). The project is open source under AGPL-3.0, runs on community Patreon funding, and is integrated with the Launch Library 2 API so any article can be linked to a specific launch or event.
examples:
- key_count: 12
  name: Spaceflight News Article Example
  slug: spaceflight-news-article-example
- key_count: 2
  name: Spaceflight News Author Example
  slug: spaceflight-news-author-example
- key_count: 12
  name: Spaceflight News Blog Example
  slug: spaceflight-news-blog-example
- key_count: 2
  name: Spaceflight News Event Example
  slug: spaceflight-news-event-example
- key_count: 2
  name: Spaceflight News Info Example
  slug: spaceflight-news-info-example
- key_count: 2
  name: Spaceflight News Launch Example
  slug: spaceflight-news-launch-example
- key_count: 4
  name: Spaceflight News Paginated Article List Example
  slug: spaceflight-news-paginated-article-list-example
- key_count: 4
  name: Spaceflight News Paginated Blog List Example
  slug: spaceflight-news-paginated-blog-list-example
- key_count: 4
  name: Spaceflight News Paginated Report List Example
  slug: spaceflight-news-paginated-report-list-example
- key_count: 9
  name: Spaceflight News Report Example
  slug: spaceflight-news-report-example
- key_count: 6
  name: Spaceflight News Socials Example
  slug: spaceflight-news-socials-example
graphqls:
- description: REST API providing access to aggregated spaceflight news articles, blog posts, and official mission reports from 40+ news sites. Supports rich filtering (full-text search, news-site filters, date rang
  name: Spaceflight News GraphQL API
  slug: spaceflight-news-graphql
image: https://raw.githubusercontent.com/TheSpaceDevs/spaceflightnewsapi/main/.github/profile/assets/snapi_poster.png
json_schemas:
- name: Article
  property_count: 12
  slug: spaceflight-news-article
- name: Author
  property_count: 2
  slug: spaceflight-news-author
- name: Blog
  property_count: 12
  slug: spaceflight-news-blog
- name: Event
  property_count: 2
  slug: spaceflight-news-event
- name: Info
  property_count: 2
  slug: spaceflight-news-info
- name: Launch
  property_count: 2
  slug: spaceflight-news-launch
- name: PaginatedArticleList
  property_count: 4
  slug: spaceflight-news-paginated-article-list
- name: PaginatedBlogList
  property_count: 4
  slug: spaceflight-news-paginated-blog-list
- name: PaginatedReportList
  property_count: 4
  slug: spaceflight-news-paginated-report-list
- name: Report
  property_count: 9
  slug: spaceflight-news-report
- name: Socials
  property_count: 6
  slug: spaceflight-news-socials
json_structures:
- name: Spaceflight News Article Structure
  property_count: 12
  slug: spaceflight-news-article-structure
- name: Spaceflight News Author Structure
  property_count: 2
  slug: spaceflight-news-author-structure
- name: Spaceflight News Blog Structure
  property_count: 12
  slug: spaceflight-news-blog-structure
- name: Spaceflight News Event Structure
  property_count: 2
  slug: spaceflight-news-event-structure
- name: Spaceflight News Info Structure
  property_count: 2
  slug: spaceflight-news-info-structure
- name: Spaceflight News Launch Structure
  property_count: 2
  slug: spaceflight-news-launch-structure
- name: Spaceflight News Paginated Article List Structure
  property_count: 4
  slug: spaceflight-news-paginated-article-list-structure
- name: Spaceflight News Paginated Blog List Structure
  property_count: 4
  slug: spaceflight-news-paginated-blog-list-structure
- name: Spaceflight News Paginated Report List Structure
  property_count: 4
  slug: spaceflight-news-paginated-report-list-structure
- name: Spaceflight News Report Structure
  property_count: 9
  slug: spaceflight-news-report-structure
- name: Spaceflight News Socials Structure
  property_count: 6
  slug: spaceflight-news-socials-structure
jsonld:
- class_count: 11
  name: Spaceflight News Context
  property_count: 29
  slug: spaceflight-news-context
layout: provider
modified: '2026-05-30'
name: Spaceflight News
nav: Providers
network: true
overview: 'Spaceflight News publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Blogs API, Info API, and 1 more. Tagged areas include News, Space, Spaceflight, Aerospace, and Open Source.


  The Spaceflight News catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spaceflight News'' developer surface includes documentation, changelog, FAQ, tooling, and 17 more developer resources.'
random_paper: 14
rules:
- effective_rule_count: 5
  extends: []
  name: Spaceflight News API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spaceflight-news-jsonschema-spectral-rules
- effective_rule_count: 82
  extends:
  - spectral:oas
  name: Spaceflight News API Rules
  rule_count: 41
  severity_counts:
    error: 10
    hint: 0
    info: 7
    warn: 24
  slug: spaceflight-news-rules
score:
  band: emerging
  composite: 21.9
  delta: -5.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 22.1
    developer_ergonomics: 14.3
    discoverability: 81.5
    governance: 25.0
    operational_transparency: 18.4
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/spaceflight-news/refs/heads/main/screenshots/spaceflight-news-2026-06-20T194233.png
security:
- kind: domain-security
  name: Spaceflight News Domain Security
  slug: spaceflight-news-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spaceflight-news
tags:
- News
- Space
- Spaceflight
- Aerospace
- Open Source
- Launches
- Public APIs
website: https://spaceflightnewsapi.net
---
