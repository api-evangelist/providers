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
  band: agent-aware
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
  score: 23.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Api League Agentic Access
  operation_count: 55
  slug: api-league-agentic-access
  summary_line: 55 operations
api_count: 1
apis:
- baseURL: https://api.apileague.com
  baseurl_source: declared
  description: 'The API League Platform exposes 55 read-only GET operations across twelve categories: Books (2), News (3), Humor (6), Food (4), Knowledge (5), Games (3), Art (4), Web (6), Text (13), Media (6), Math ('
  name: API League Platform
  slug: api-league-platform
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/api-league-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/api-league-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/api-league-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apileague.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apileague.com/apis/
- group: docs
  title: ''
  type: Documentation
  url: https://apileague.com/apis/
- group: docs
  title: ''
  type: APIReference
  url: https://apileague.com/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://apileague.com/docs/quick-start/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/QudH9DTNzx
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/QudH9DTNzx
- group: company
  title: ''
  type: Blog
  url: https://apileague.com/articles/
- group: commercial
  title: ''
  type: Pricing
  url: https://apileague.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://apileague.com/console/
- group: start
  title: ''
  type: Login
  url: https://apileague.com/console/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apileague.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apileague.com/terms/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ddsky
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ddsky/api-league-clients
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/spoonacular-api/workspace/api-league/collection/7431899-68556c9b-453c-4759-bd5e-4f783b0117e8
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apileague.com/
- group: start
  title: ''
  type: Sandbox
  url: https://apileague.com/playground/
- group: build
  title: ''
  type: Packages
  url: packages/api-league-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/api-league-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/api-league-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/api-league-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/api-league-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/api-league-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/api-league-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/api-league-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/api-league-text-overlay.yaml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/api-league-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/api-league-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/api-league-finops.yml
created: '2025-03-01'
description: API League is a single-key hub of 55 read-only HTTP APIs spanning twelve categories — Books, News, Humor, Food, Knowledge, Games, Art, Web, Text, Media, Math and Storage — operated by skycraft GmbH of Dresden, Germany, which has been shipping developer APIs since 2015. Every operation is an HTTP GET against https://api.apileague.com, authenticated with one API key passed as an api-key query parameter or an x-api-key header, and described by a published OpenAPI 3.0 contract (v1.9.0) that carries an operationId, a summary, a tag and a worked response example on all 55 operations. Billing is metered in tokens per day rather than requests per month, and every response returns X-API-Quota-Request, X-API-Quota-Used and X-API-Quota-Left so a consumer can read its remaining budget at runtime. Client libraries are generated for 21 languages from that contract, though only the JavaScript client is published to a package registry. Pricing is fully self-serve across four tiers from a free
  50-token-per-day plan to $199/mo, with a 99.9% uptime target and a public status page.
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
modified: '2026-09-02'
name: API League
nav: Providers
network: true
overview: 'API League publishes 1 API on the [APIs.io](https://apis.io/) network: Platform. Tagged areas include API Marketplace, Books, Developer Tools, Food, and Games.


  API League''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Api League Plans Pricing
  plan_count: 4
  slug: api-league-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 12
  name: Api League Rate Limits
  slug: api-league-rate-limits
score:
  band: strong
  composite: 55.7
  coverage:
    artifact_dirs: 21
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 33.3
    developer_ergonomics: 78.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/api-league/refs/heads/main/screenshots/api-league-2026-06-20T172214.png
security:
- kind: authentication
  name: Api League Authentication
  slug: api-league-authentication
  summary_line: apiKey · 2 schemes
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
- Games
- Humor
- Media
- News
- OpenAPI
- SDK
- Text Processing
- Web Scraping
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
