---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    agentic_access: true
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Meredith Agentic Access
  operation_count: 0
  slug: meredith-agentic-access
  summary_line: 0 operations
api_count: 30
apis:
- description: RSS 2.0 feeds for People.com, the flagship celebrity-and-human-interest brand of People Inc. People.com is the largest property in the portfolio (~187M monthly visits per 2025 estimates). Section feed
  name: PEOPLE RSS Feeds
  slug: people-rss-feeds
- description: RSS 2.0 feeds for BHG.com, People Inc's flagship home + gardening brand and the second-largest US monthly magazine by circulation.
  name: Better Homes & Gardens RSS Feeds
  slug: better-homes-gardens-rss-feeds
- description: RSS feeds for Allrecipes.com, the largest food brand in the portfolio and one of the most-trafficked recipe sites globally.
  name: Allrecipes RSS Feeds
  slug: allrecipes-rss-feeds
- description: RSS feeds for Investopedia.com, the dominant retail-investor finance reference site in the portfolio. Carries dictionary-style term entries and breaking finance/markets articles.
  name: Investopedia RSS Feeds
  slug: investopedia-rss-feeds
- description: RSS feeds across the Verywell sub-brands (Verywell Health, Verywell Mind, Verywell Fit). Largest consumer-health network in the US per Comscore.
  name: Verywell Family RSS Feeds
  slug: verywell-family-rss-feeds
- description: RSS feeds for Food & Wine, the culinary lifestyle brand.
  name: Food & Wine RSS Feeds
  slug: food-wine-rss-feeds
- description: RSS feeds for Real Simple, a Home + Lifestyle brand.
  name: Real Simple RSS Feeds
  slug: real-simple-rss-feeds
- description: RSS feeds for Southern Living, a regional lifestyle brand.
  name: Southern Living RSS Feeds
  slug: southern-living-rss-feeds
- description: RSS feeds for Travel + Leisure, the brand that also seeds the publicly-traded Wyndham Destinations spin-off.
  name: Travel + Leisure RSS Feeds
  slug: travel-leisure-rss-feeds
- description: RSS feeds for Byrdie, the People Inc beauty brand.
  name: Byrdie RSS Feeds
  slug: byrdie-rss-feeds
- description: RSS feeds for InStyle, fashion and beauty brand.
  name: InStyle RSS Feeds
  slug: instyle-rss-feeds
- description: RSS feeds for Brides, the wedding planning brand.
  name: Brides RSS Feeds
  slug: brides-rss-feeds
- description: RSS feeds for EatingWell, the healthy-eating food brand.
  name: EatingWell RSS Feeds
  slug: eatingwell-rss-feeds
- description: RSS feeds for Serious Eats, the technique-driven food brand.
  name: Serious Eats RSS Feeds
  slug: serious-eats-rss-feeds
- description: RSS feeds for Simply Recipes.
  name: Simply Recipes RSS Feeds
  slug: simply-recipes-rss-feeds
- description: RSS feeds for The Spruce, The Spruce Eats, and The Spruce Pets.
  name: The Spruce RSS Feeds
  slug: the-spruce-rss-feeds
- description: RSS feeds for Health, the wellness magazine brand.
  name: Health RSS Feeds
  slug: health-rss-feeds
- description: RSS feeds for Shape, the fitness and women's wellness brand.
  name: Shape RSS Feeds
  slug: shape-rss-feeds
- description: RSS feeds for Parents, the family + parenting brand.
  name: Parents RSS Feeds
  slug: parents-rss-feeds
- description: RSS feeds for Entertainment Weekly.
  name: Entertainment Weekly RSS Feeds
  slug: entertainment-weekly-rss-feeds
- description: RSS feeds for Lifewire, the consumer-tech how-to brand.
  name: Lifewire RSS Feeds
  slug: lifewire-rss-feeds
- description: RSS feeds for Treehugger, the sustainability and environment brand.
  name: Treehugger RSS Feeds
  slug: treehugger-rss-feeds
- description: RSS feeds for TripSavvy, the travel guides brand.
  name: TripSavvy RSS Feeds
  slug: tripsavvy-rss-feeds
- description: RSS feeds for The Balance Money, personal finance brand.
  name: The Balance RSS Feeds
  slug: the-balance-rss-feeds
- description: RSS feeds for Daily Paws, the pets brand.
  name: Daily Paws RSS Feeds
  slug: daily-paws-rss-feeds
- description: RSS feeds for MarthaStewart.com, the home/lifestyle brand.
  name: Martha Stewart RSS Feeds
  slug: martha-stewart-rss-feeds
- description: RSS feeds for Liquor.com, the spirits and cocktail brand.
  name: Liquor.com RSS Feeds
  slug: liquorcom-rss-feeds
- description: Every People Inc brand exposes a discoverable sitemap index at /sitemap.xml with per-section sitemap files. These are the canonical machine-readable index of all published URLs on each brand. Useful f
  name: XML Sitemaps Across Properties
  slug: xml-sitemaps-across-properties
- description: D/Cipher is People Inc's proprietary intent-based contextual advertising platform — a cookieless targeting solution that derives audience-intent signals from how readers engage across People Inc's own
  name: D/Cipher Contextual Advertising Platform
  slug: dcipher-contextual-advertising-platform
- description: 'A bundle of B2B services run by People Inc with no public developer surface but with discrete branded sub-products: Content Solutions (content marketing consultancy), Awards & Accolades (licensing of '
  name: Specialty Marketing Solutions (SMS) Suite
  slug: specialty-marketing-solutions-sms-suite
artifact_total: 46
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meredith-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/meredith-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meredith-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/meredith-security.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meredith-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/meredith-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/meredith-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/meredith-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/meredith-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/meredith-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meredith-llms.txt
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/meredith-vocabulary.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/api-evangelist/meredith/issues
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meredith-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.people.inc/
- group: start
  title: ''
  type: Portal
  url: https://www.iac.com/brands/peopleinc
- group: company
  title: ''
  type: Blog
  url: https://www.people.inc/news-awards
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.people.inc/news-awards
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MeredithCorp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/MeredithCorp/sqs-consumer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/People-INC
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/peopleinc-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.people.inc/brands-termsofservice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.people.inc/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://ir.iac.com/code-business-conduct-and-ethics
- group: operate
  title: ''
  type: Support
  url: https://www.people.inc/contact
- group: operate
  title: ''
  type: Contact
  url: mailto:contentlicensing@people.inc
- group: operate
  title: ''
  type: Contact
  url: mailto:advertising@peopleinc.com
- group: operate
  title: ''
  type: Contact
  url: mailto:marketing@peopleinc.com
- group: operate
  title: ''
  type: Contact
  url: mailto:press@peopleinc.com
- group: operate
  title: ''
  type: Contact
  url: mailto:subscriptions@peopleinc.com
- group: operate
  title: ''
  type: Contact
  url: mailto:licensing@peopleinc.com
- group: commercial
  title: ''
  type: Pricing
  url: https://raw.githubusercontent.com/api-evangelist/meredith/main/plans/meredith-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/meredith/main/rate-limits/meredith-rate-limits.yml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/meredith/main/json-ld/meredith-context.jsonld
created: '2025-05-05'
description: 'Profile for People Inc (formerly Dotdash Meredith) in the API Evangelist network. America''s largest digital and print publisher, operating 40+ brands including PEOPLE, Better Homes & Gardens, Allrecipes, Investopedia, Verywell, Food & Wine, Southern Living, Real Simple, Travel + Leisure, Byrdie, InStyle, The Spruce, EatingWell, Serious Eats, Simply Recipes, Brides, Health, Shape, Parents, Entertainment Weekly, Lifewire, TreeHugger, TripSavvy, The Balance, and more. An IAC (NASDAQ: IAC) operating company since the December 2021 merger of Dotdash and Meredith Corporation ($2.7B transaction); rebranded to "People Inc." on July 31, 2025 to elevate the company''s flagship brand. There is no public read/write developer API surface — the addressable machine-readable surface is per-brand RSS feeds, XML sitemaps, robots.txt policy declarations, and the D/Cipher intent-based contextual advertising platform sold as a B2B media buy (no self-serve developer console). All major brand domains
  explicitly disallow ClaudeBot, anthropic-ai, CCBot, PerplexityBot and 70+ other AI crawlers in robots.txt — with the OpenAI crawlers (GPTBot, OAI-SearchBot, ChatGPT-User) notably exempted down to a single /thmb/ path, and sponsored-content paths (*/presented/, */integrated/) carved back OUT of the denylist so advertiser content stays crawlable while editorial does not. The policy is enforced at the Cloudflare edge as well as declared: as of 2026-08-12 every People Inc host answers a declared AI crawler with HTTP 402 Payment Required and the body "If you wish to license content from People Inc, please contact contentlicensing@people.inc". Discovery metadata (robots.txt, sitemap.xml, google-news-sitemap.xml and an RFC 9116 security.txt pointing at a private HackerOne program) is served at 200 to every client; article and RSS paths return 403 to every non-browser client. The map is open, the corpus is not.'
examples:
- key_count: 1
  name: Allrecipes Sitemap Index Example
  slug: allrecipes-sitemap-index-example
- key_count: 5
  name: People Inc Robots Policy Example
  slug: people-inc-robots-policy-example
- key_count: 1
  name: People Rss Feed Example
  slug: people-rss-feed-example
finops:
- name: Meredith Finops
  service_category: ''
  slug: meredith-finops
image: https://avatars.githubusercontent.com/u/46611466?v=4
json_schemas:
- name: PeopleIncRobotsPolicy
  property_count: 5
  slug: robots-policy
- name: PeopleIncRSSFeed
  property_count: 1
  slug: rss-feed
- name: PeopleIncSitemap
  property_count: 2
  slug: sitemap
json_structures:
- name: Brand Structure
  property_count: 9
  slug: brand-structure
jsonld:
- class_count: 33
  name: Meredith Context
  property_count: 0
  slug: meredith-context
layout: provider
modified: '2026-08-12'
name: Dotdash Meredith / People Inc
nav: Providers
network: true
overview: 'Dotdash Meredith / People Inc publishes 30 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Publishing, Magazines, Content, and Advertising.


  The Dotdash Meredith / People Inc catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Dotdash Meredith / People Inc''s developer surface includes developer portal, engineering blog, changelog, support, pricing, and 30 more developer resources.'
plans:
- name: Meredith Plans Pricing
  plan_count: 8
  slug: meredith-plans-pricing
random_paper: 105
rate_limits:
- limit_count: 0
  name: Meredith Rate Limits
  slug: meredith-rate-limits
rules:
- name: Dotdash Meredith / People Inc API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: meredith-jsonschema-spectral-rules
- name: Dotdash Meredith / People Inc API Rules
  rule_count: 2
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 0
  slug: people-inc-rss-rules
score:
  band: developing
  composite: 47.3
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 22.6
    developer_ergonomics: 15.2
    discoverability: 92.6
    governance: 81.3
    operational_transparency: 31.6
  previous_composite: 47.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Meredith Domain Security
  slug: meredith-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Meredith Vulnerability Disclosure
  slug: meredith-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: meredith
tags:
- Media
- Publishing
- Magazines
- Content
- Advertising
- Contextual Advertising
- Lifestyle
- News
- RSS
- Sitemaps
- Robots
- AI Policy
- IAC
website: https://www.people.inc/
---
