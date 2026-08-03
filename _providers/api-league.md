---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The API League Platform provides access to 60+ APIs spanning books, news, humor, food, knowledge, art, web, text processing, and media categories. Authentication uses API keys with free signup. SDKs a
  name: API League Platform
  slug: api-league-platform
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/api-league-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apileague.com
- group: docs
  title: ''
  type: Documentation
  url: https://apileague.com/apis/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/apileague
- group: agent
  title: ''
  type: LlmsText
  url: https://apileague.com/llms.txt
created: '2025-03-01'
description: API League is a comprehensive API marketplace aggregating 60+ best-in-class APIs across categories including books, news, humor, food, knowledge, art, web, text processing, and media. It offers code examples in 21 languages, SDKs, Postman collections, and free API key access for developers to launch projects quickly.
features:
- description: Access to over 60 best-in-class APIs across books, news, humor, food, knowledge, art, web, text, and media categories.
  name: 60+ APIs
- description: Official SDKs available in 21 programming languages including Java, JavaScript, Python, Go, and C#.
  name: SDKs in 21 Languages
- description: Ready-to-use Postman collections for testing and exploring all available APIs.
  name: Postman Collections
- description: Multi-language code examples for every API endpoint.
  name: Code Examples
- description: Free API key signup allowing immediate access to the platform without upfront payment.
  name: Free API Key
- description: Built-in AI chat assistant to help developers navigate the API catalog.
  name: AI Chat Assistant
finops:
- name: Api League Finops
  service_category: API
  slug: api-league-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/api-league.png
layout: provider
modified: '2026-04-19'
name: API League
nav: Providers
network: true
overview: 'API League publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Marketplace, Books, Developer Tools, Food, and Humor.


  API League''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Api League Plans Pricing
  plan_count: 3
  slug: api-league-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Api League Rate Limits
  slug: api-league-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 19.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/api-league/refs/heads/main/screenshots/api-league-2026-06-20T172214.png
security:
- kind: domain-security
  name: Api League Domain Security
  slug: api-league-domain-security
  summary_line: TLSv1.3 · DMARC
slug: api-league
tags:
- API Marketplace
- Books
- Developer Tools
- Food
- Humor
- News
- SDKs
- Text Processing
use_cases:
- description: Build news aggregators, book discovery apps, and article readers using News and Books APIs.
  name: Content Applications
- description: Integrate recipe search, nutrition data, and drink recommendations into food applications.
  name: Food and Recipe Platforms
- description: Add sentiment analysis, language detection, readability scoring, and entity extraction to applications.
  name: Text Analysis
- description: Integrate jokes, memes, GIFs, trivia, and humor APIs into games and social applications.
  name: Entertainment Apps
- description: Add screenshot capture, image search, color detection, and vector search to media workflows.
  name: Media Processing
- description: Embed quotes, trivia, life hacks, affirmations, and riddles into productivity and wellness apps.
  name: Knowledge Products
website: https://apileague.com
---
