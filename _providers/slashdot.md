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
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Slashdot Agentic Access
  operation_count: 8
  slug: slashdot-agentic-access
  summary_line: 8 operations
api_count: 7
apis:
- description: The Apple API from Slashdot — 1 operation(s) for apple.
  name: Slashdot Apple API
  slug: slashdot-apple-api
- description: The Developers API from Slashdot — 1 operation(s) for developers.
  name: Slashdot Developers API
  slug: slashdot-developers-api
- description: The Feeds API from Slashdot — 8 operation(s) for feeds.
  name: Slashdot Feeds API
  slug: slashdot-feeds-api
- description: The Games API from Slashdot — 1 operation(s) for games.
  name: Slashdot Games API
  slug: slashdot-games-api
- description: The Linux API from Slashdot — 1 operation(s) for linux.
  name: Slashdot Linux API
  slug: slashdot-linux-api
- description: The Rights API from Slashdot — 1 operation(s) for rights.
  name: Slashdot Rights API
  slug: slashdot-rights-api
- description: The Science API from Slashdot — 1 operation(s) for science.
  name: Slashdot Science API
  slug: slashdot-science-api
artifact_total: 16
collections:
- collection_type: open
  name: Slashdot RSS/Atom Feeds
  slug: open-slashdot-rss
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/slashdot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slashdot-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/slashdot-media
- group: company
  title: ''
  type: Website
  url: https://slashdot.org/
- group: other
  title: ''
  type: RSS
  url: https://rss.slashdot.org/Slashdot/slashdotMain
- group: other
  title: ''
  type: RSS
  url: https://rss.slashdot.org/Slashdot/slashdotDevelopers
- group: other
  title: ''
  type: RSS
  url: https://rss.slashdot.org/Slashdot/slashdotApple
- group: other
  title: ''
  type: RSS
  url: https://rss.slashdot.org/Slashdot/slashdotLinux
- group: other
  title: ''
  type: RSS
  url: https://rss.slashdot.org/Slashdot/slashdotGames
- group: other
  title: ''
  type: RSS
  url: https://rss.slashdot.org/Slashdot/slashdotScience
- group: other
  title: ''
  type: RSS
  url: https://rss.slashdot.org/Slashdot/slashdotYourRightsOnline
- group: company
  title: ''
  type: About
  url: https://slashdot.org/faq/slashmeta.shtml
- group: operate
  title: ''
  type: FAQ
  url: https://slashdot.org/faq/index.shtml
- group: operate
  title: ''
  type: FAQ-Feeds
  url: https://slashdot.org/faq/feeds.shtml
- group: other
  title: ''
  type: Firehose
  url: https://slashdot.org/faq/firehose.shtml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://slashdot.org/privacy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/slashdot-rss-openapi.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/slashdot-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/slashdot-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://slashdot.org/llms.txt
created: '2026-03-24'
description: Slashdot is a technology news aggregation and community discussion site founded in 1997, focused on open source software, Linux, science, and technology topics. Known by its tagline "News for nerds, stuff that matters," Slashdot allows readers to submit and vote on stories, comment on articles, and follow developments across the technology landscape. The site offers RSS and Atom feeds for programmatic access to its content across multiple topic sections including developers, Linux, games, science, Apple, and more. Feed requests are rate-limited to one per 30 minutes.
examples:
- key_count: 1
  name: Slashdot Rss Feed Example
  slug: slashdot-rss-feed-example
finops:
- name: Slashdot Finops
  service_category: API
  slug: slashdot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/slashdot.png
jsonld:
- class_count: 0
  name: Slashdot Context
  property_count: 5
  slug: slashdot-context
layout: provider
modified: '2026-05-19'
name: Slashdot
nav: Providers
network: true
overview: 'Slashdot publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Apple API, Developers API, Feeds API, and 4 more. Tagged areas include Media, Open Source, Technology News, and RSS.


  The Slashdot catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Slashdot''s developer surface includes FAQ and 19 more developer resources.'
plans:
- name: Slashdot Plans Pricing
  plan_count: 3
  slug: slashdot-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Slashdot Rate Limits
  slug: slashdot-rate-limits
rules:
- name: Slashdot API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: slashdot-rules
score:
  band: thin
  composite: 41.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.5
    developer_ergonomics: 0.0
    discoverability: 55.6
    governance: 52.1
    operational_transparency: 31.6
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/slashdot/refs/heads/main/screenshots/slashdot-2026-06-20T194022.png
security:
- kind: domain-security
  name: Slashdot Domain Security
  slug: slashdot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: slashdot
tags:
- Media
- Open Source
- Technology News
- RSS
website: https://slashdot.org/
---
