---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Walt Disney Agentic Access
  operation_count: 2
  slug: walt-disney-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Disney character data including films, TV shows, and park attractions
  name: Walt Disney Characters API
  slug: walt-disney-characters-api
artifact_total: 14
collections:
- collection_type: open
  name: Disney Characters API
  slug: open-walt-disney-disney-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/walt-disney-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/walt-disney-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-walt-disney-company
- group: company
  title: ''
  type: Website
  url: https://www.disney.com/
- group: start
  title: ''
  type: Portal
  url: https://disneyapi.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://disneyapi.dev/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://disney.github.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/disney
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/disneystreaming
- group: company
  title: ''
  type: Blog
  url: https://medium.com/disney-streaming
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/disney-streaming
- group: start
  title: ''
  type: Portal
  url: https://developer.disney.com/
created: '2026-03-21'
description: The Walt Disney Company is a leading diversified international family entertainment and media enterprise with operations across media networks, parks and resorts, studio entertainment, and direct-to-consumer streaming. Disney's developer APIs and open source projects enable partners and developers to integrate Disney content, characters, and experiences into their applications.
examples:
- key_count: 2
  name: Walt Disney Listcharacters Example
  slug: walt-disney-listCharacters-example
finops:
- name: Walt Disney Finops
  service_category: Entertainment / Media
  slug: walt-disney-finops
graphqls:
- description: ''
  name: Walt Disney GraphQL API
  slug: walt-disney-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/walt-disney.png
json_schemas:
- name: Disney Character
  property_count: 13
  slug: walt-disney-character
json_structures:
- name: Walt Disney Character Structure
  property_count: 0
  slug: walt-disney-character-structure
jsonld:
- class_count: 6
  name: Walt Disney Context
  property_count: 11
  slug: walt-disney-context
layout: provider
modified: '2026-05-19'
name: Walt Disney
nav: Providers
network: true
overview: 'Walt Disney publishes 1 API on the [APIs.io](https://apis.io/) network: Characters API. Tagged areas include Fortune 100, Entertainment, Media, Streaming, and Parks.


  The Walt Disney catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Walt Disney''s developer surface includes developer portal, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Walt Disney Plans Pricing
  plan_count: 1
  slug: walt-disney-plans-pricing
press:
- date: '2026-05-25'
  title: Disney's New Advertising Solutions from Global Tech & ...
  url: https://thewaltdisneycompany.com/news/tech-data-showcase-advertising-2026/
- date: '2026-05-25'
  title: The Walt Disney Company and OpenAI reach landmark ...
  url: https://openai.com/index/disney-sora-agreement/
- date: '2026-05-25'
  title: Disney has officially opened the floodgates on AI ...
  url: https://www.facebook.com/comicbookdotcom/posts/disney-has-officially-opened-the-floodgates-on-ai-as-reports-are-now-in-that-the/1264375688889438/
- date: '2026-05-25'
  title: Disney's Groundbreaking AI Deal is Dead.
  url: https://www.disneytouristblog.com/disneys-groundbreaking-ai-deal-is-dead/
- date: '2026-05-25'
  title: The Walt Disney Company and OpenAI Reach Agreement ...
  url: https://thewaltdisneycompany.com/news/disney-openai-sora-agreement/
random_paper: 3
rate_limits:
- limit_count: 1
  name: Walt Disney Rate Limits
  slug: walt-disney-rate-limits
rules:
- name: Walt Disney API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: walt-disney-jsonschema-spectral-rules
- name: Walt Disney API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: walt-disney-rules
score:
  band: developing
  composite: 44.5
  delta: -4.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 70.3
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Walt Disney Domain Security
  slug: walt-disney-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: walt-disney
tags:
- Fortune 100
- Entertainment
- Media
- Streaming
- Parks
- Content
website: https://www.disney.com/
---
