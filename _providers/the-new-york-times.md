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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: The New York Times Agentic Access
  operation_count: 12
  slug: the-new-york-times-agentic-access
  summary_line: 12 operations
api_count: 7
apis:
- description: The Archive API from The New York Times — 1 operation(s) for archive.
  name: The New York Times Archive API
  slug: the-new-york-times-archive-api
- description: The Content API from The New York Times — 3 operation(s) for content.
  name: The New York Times Content API
  slug: the-new-york-times-content-api
- description: The Movies API from The New York Times — 3 operation(s) for movies.
  name: The New York Times Movies API
  slug: the-new-york-times-movies-api
- description: The Name API from The New York Times — 1 operation(s) for name.
  name: The New York Times Name API
  slug: the-new-york-times-name-api
- description: The Search API from The New York Times — 1 operation(s) for search.
  name: The New York Times Search API
  slug: the-new-york-times-search-api
- description: The Stories API from The New York Times — 2 operation(s) for stories.
  name: The New York Times Stories API
  slug: the-new-york-times-stories-api
- description: The Timestags API from The New York Times — 1 operation(s) for timestags.
  name: The New York Times Timestags API
  slug: the-new-york-times-timestags-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-new-york-times-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/the-new-york-times-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-new-york-times-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-new-york-times-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-new-york-times
- group: start
  title: ''
  type: Portal
  url: https://developer.nytimes.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.nytimes.com/get-started
- group: start
  title: ''
  type: Signup
  url: https://developer.nytimes.com/accounts/create
- group: start
  title: ''
  type: Login
  url: https://developer.nytimes.com/accounts/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.nytimes.com/terms
- group: operate
  title: ''
  type: FAQ
  url: https://developer.nytimes.com/faq
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nytimes
- group: company
  title: ''
  type: Website
  url: https://nytimes.com
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/nytimes/public_api_specs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nytimes/times_wire
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nytimes/nytcampfin
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/new-york-times-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/new-york-times-article-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/new-york-times-book-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/the-new-york-times-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/the-new-york-times-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.nytimes.com/llms.txt
created: '2023-10-06T00:00:00.000Z'
description: The New York Times is one of the world's most respected news organizations, providing comprehensive journalism across politics, culture, business, science, health, and the arts since 1851. The NYT Developer Network exposes a suite of RESTful APIs enabling developers to search and access NYT articles, best-seller book lists, movie reviews, semantic metadata, top stories, and popular content. All APIs require an API key obtained from the NYT Developer Portal.
examples:
- key_count: 2
  name: New York Times Search Articles Example
  slug: new-york-times-search-articles-example
- key_count: 2
  name: New York Times Top Stories Example
  slug: new-york-times-top-stories-example
finops:
- name: The New York Times Finops
  service_category: News / Media
  slug: the-new-york-times-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-new-york-times.png
json_schemas:
- name: NYT Article
  property_count: 18
  slug: new-york-times-article
- name: NYT Best Seller Book
  property_count: 11
  slug: new-york-times-book
json_structures:
- name: New York Times Article Structure
  property_count: 0
  slug: new-york-times-article-structure
jsonld:
- class_count: 40
  name: The New York Times Context
  property_count: 2
  slug: the-new-york-times-context
layout: provider
modified: '2026-05-19'
name: The New York Times
nav: Providers
network: true
overview: 'The New York Times publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Archive API, Content API, Movies API, and 4 more. Tagged areas include Articles, Books, Movies, News, and Media.


  The The New York Times catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  The New York Times'' developer surface includes authentication, developer portal, getting-started guide, signup flow, FAQ, GitHub presence, and 16 more developer resources.'
plans:
- name: The New York Times Plans Pricing
  plan_count: 2
  slug: the-new-york-times-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: The New York Times Rate Limits
  slug: the-new-york-times-rate-limits
rules:
- name: The New York Times API Rules
  rule_count: 12
  severity_counts:
    error: 3
    hint: 2
    info: 0
    warn: 7
  slug: new-york-times-rules
- name: The New York Times API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: the-new-york-times-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 50.3
    developer_ergonomics: 37.0
    discoverability: 100.0
    governance: 39.5
    operational_transparency: 26.3
  previous_composite: 48.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-new-york-times/refs/heads/main/screenshots/the-new-york-times-2026-06-20T195228.png
security:
- kind: authentication
  name: The New York Times Authentication
  slug: the-new-york-times-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: The New York Times Domain Security
  slug: the-new-york-times-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: The New York Times Vulnerability Disclosure
  slug: the-new-york-times-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: the-new-york-times
tags:
- Articles
- Books
- Movies
- News
- Media
- Publishing
- Journalism
website: https://nytimes.com
---
