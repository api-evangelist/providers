---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: One authenticated surface over 50 platforms — profiles, posts and engagement from the social sources, listings and markets from the commerce sources, and a unified cross-platform search. 403 paths, 41
  name: SocialCrawl API
  slug: socialcrawl-api
artifact_total: 1
common:
- group: other
  title: ''
  type: APIsJSON
  url: well-known/socialcrawl-provider-apis.json
- group: start
  title: ''
  type: Onboarding
  url: well-known/socialcrawl-api-onboarding.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/socialcrawl-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.socialcrawl.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.socialcrawl.dev/docs
- group: commercial
  title: ''
  type: Plans
  url: https://www.socialcrawl.dev/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://www.socialcrawl.dev/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.socialcrawl.dev/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.socialcrawl.dev/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.socialcrawl.dev/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.socialcrawl.dev/contact
- group: company
  title: ''
  type: Blog
  url: https://www.socialcrawl.dev/blog
- group: company
  title: ''
  type: BlogFeed
  url: https://www.socialcrawl.dev/rss.xml
created: '2026-08-25'
description: 'SocialCrawl is a unified social, commerce and research data API: one key, one response schema, 50 platforms and roughly 400 endpoints, plus a cross-platform search that fans out across 17 sources in a single call. The social side covers TikTok, Instagram, YouTube, X, LinkedIn, Reddit, Threads, Pinterest, Facebook, Snapchat, Twitch, Truth Social and Kick; the non-social side covers Amazon, Polymarket, Hacker News, GitHub, Google Search, Perplexity and Tavily. Responses are normalised to one shape regardless of source. The published contract is an OpenAPI 3.1 document of 403 paths and 411 operations across 58 tags, with a free tier of 100 credits and no card required.'
layout: provider
modified: '2026-08-25'
name: SocialCrawl
nav: Providers
network: true
overview: 'SocialCrawl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media, Scraping, Data, Search, and Commerce.


  SocialCrawl''s developer surface includes changelog, support, engineering blog, and 10 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 33.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 57.1
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 31.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
slug: socialcrawl
tags:
- Social Media
- Scraping
- Data
- Search
- Commerce
- Research
- Agents
website: https://www.socialcrawl.dev
---
