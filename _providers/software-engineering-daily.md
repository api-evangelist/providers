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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: Software Engineering Daily provides RSS podcast feeds for its main episode stream as well as topic-specific feeds. These standard podcast RSS feeds are compatible with all major podcast clients includ
  name: Software Engineering Daily Podcast RSS Feed
  slug: podcast-rss-feed
- description: The Software Engineering Daily Backend API is an open-source REST API that powers the platform's web, iOS, and Android front ends. Built with Node.js, MongoDB, and Redis, it provides endpoints for acc
  name: Software Engineering Daily Backend API
  slug: backend-api
- description: The Software Engineering Daily mobile application is an open-source React Native app available on iOS and Android. It provides access to the full episode catalog, topic-specific feeds, bookmarking, an
  name: Software Engineering Daily Mobile App
  slug: mobile-app
artifact_total: 12
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/SoftwareEngineeringDaily/software-engineering-daily-api/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/software-engineering-daily-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://softwareengineeringdaily.com/
- group: company
  title: ''
  type: About
  url: https://softwareengineeringdaily.com/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://softwareengineeringdaily.com/premium/
- group: other
  title: ''
  type: RSSFeed
  url: https://softwareengineeringdaily.com/feed/podcast/
- group: other
  title: ''
  type: RSSFeeds
  url: https://softwareengineeringdaily.com/2017/07/05/new-topic-feeds/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/SoftwareEngineeringDaily/software-engineering-daily-api
- group: docs
  title: ''
  type: Documentation
  url: https://softwareengineeringdaily.github.io/Backend/gettingstarted/
- group: other
  title: ''
  type: Podcast
  url: https://podcasts.apple.com/podcast/software-engineering-daily/id1019576853
- group: other
  title: ''
  type: Podcast
  url: https://open.spotify.com/show/6UCtBYL29hwhw4YbTdX83N
- group: other
  title: ''
  type: X
  url: https://twitter.com/software_daily
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/software-engineering-daily
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/softwareengineeringdaily
- group: commercial
  title: ''
  type: TermsOfService
  url: https://softwareengineeringdaily.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://softwareengineeringdaily.com/privacy-policy/
created: '2026-03-24'
description: Software Engineering Daily is a podcast and media platform dedicated to covering software engineering topics through daily technical interviews and discussions. Founded by Jeff Meyerson in 2015, the platform publishes episodes five days a week featuring conversations with software engineers, startup founders, and technology leaders on topics ranging from distributed systems, cloud computing, databases, and programming languages to AI, machine learning, and the business of software. The platform also offers a membership program for premium content and provides open-source backend and mobile apps for community development.
examples:
- key_count: 13
  name: Software Engineering Daily Episode Example
  slug: software-engineering-daily-episode-example
finops:
- name: Software Engineering Daily Finops
  service_category: API
  slug: software-engineering-daily-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/software-engineering-daily.png
json_schemas:
- name: Episode
  property_count: 13
  slug: software-engineering-daily-episode
json_structures:
- name: Software Engineering Daily Episode Structure
  property_count: 0
  slug: software-engineering-daily-episode-structure
jsonld:
- class_count: 19
  name: Software Engineering Daily Context
  property_count: 7
  slug: software-engineering-daily-context
layout: provider
modified: '2026-05-02'
name: Software Engineering Daily
nav: Providers
network: true
overview: 'Software Engineering Daily publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Podcasts, Software Engineering, Technical Content, and Open-Source.


  The Software Engineering Daily catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Software Engineering Daily''s developer surface includes pricing, documentation, and 14 more developer resources.'
plans:
- name: Software Engineering Daily Plans Pricing
  plan_count: 3
  slug: software-engineering-daily-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Software Engineering Daily Rate Limits
  slug: software-engineering-daily-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Software Engineering Daily API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: software-engineering-daily-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.4
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 24.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/software-engineering-daily/refs/heads/main/screenshots/software-engineering-daily-2026-06-20T194137.png
security:
- kind: domain-security
  name: Software Engineering Daily Domain Security
  slug: software-engineering-daily-domain-security
  summary_line: TLSv1.3 · DMARC
slug: software-engineering-daily
tags:
- Media
- Podcasts
- Software Engineering
- Technical Content
- Open-Source
website: https://softwareengineeringdaily.com/
---
