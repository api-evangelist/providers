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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Podcastindex Agentic Access
  operation_count: 52
  slug: podcastindex-agentic-access
  summary_line: 52 operations · 4 acting
api_count: 11
apis:
- description: 'Add new podcast feeds to the index. **NOTE**: To add to the index, the API Key must have write or publisher permissions.'
  name: PodcastIndex Add API
  slug: podcastindex-add-api
- description: The Apple Replacement API from PodcastIndex — 2 operation(s) for apple replacement.
  name: PodcastIndex Apple Replacement API
  slug: podcastindex-apple-replacement-api
- description: Categories used by the Podcast Index
  name: PodcastIndex Categories API
  slug: podcastindex-categories-api
- description: Find details about one or more episodes of a podcast or podcasts.
  name: PodcastIndex Episodes API
  slug: podcastindex-episodes-api
- description: Notify the index that a feed has changed
  name: PodcastIndex Hub API
  slug: podcastindex-hub-api
- description: Find details about a Podcast and its feed.
  name: PodcastIndex Podcasts API
  slug: podcastindex-podcasts-api
- description: Find recent additions to the index
  name: PodcastIndex Recent API
  slug: podcastindex-recent-api
- description: Search the index
  name: PodcastIndex Search API
  slug: podcastindex-search-api
- description: The Static Data API from PodcastIndex — 11 operation(s) for static data.
  name: PodcastIndex Static Data API
  slug: podcastindex-static-data-api
- description: Statistics for items in the Podcast Index
  name: PodcastIndex Stats API
  slug: podcastindex-stats-api
- description: The podcast's "Value for Value" information
  name: PodcastIndex Value API
  slug: podcastindex-value-api
artifact_total: 18
collections:
- collection_type: open
  name: PodcastIndex.org API
  slug: open-podcastindex
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/podcastindex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podcastindex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/podcastindex-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podcast-index
- group: company
  title: ''
  type: Website
  url: https://podcastindex.org/
- group: docs
  title: ''
  type: Documentation
  url: https://podcastindex-org.github.io/docs-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Podcastindex-org
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Podcastindex-org/docs-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/Podcastindex-org/legal/blob/main/TermsOfService.md
created: '2025-05-02'
description: The Podcast Index (Podcast Index LLC) is a software developer focused partnership that provides tools and data to anyone who aspires to create new and exciting Podcast experiences without the heavy lifting of indexing, aggregation and data management.
finops:
- name: Podcastindex Finops
  service_category: API
  slug: podcastindex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podcastindex.png
layout: provider
modified: '2026-05-19'
name: PodcastIndex
nav: Providers
network: true
overview: 'PodcastIndex publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Add API, Apple Replacement API, Categories API, and 8 more. Tagged areas include Podcasting, Podcast Index, Discovery, and Open Data.


  PodcastIndex''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Podcastindex Plans Pricing
  plan_count: 3
  slug: podcastindex-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 5
  name: Podcastindex Rate Limits
  slug: podcastindex-rate-limits
score:
  band: thin
  composite: 38.3
  delta: -3.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.4
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Podcastindex Authentication
  slug: podcastindex-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Podcastindex Domain Security
  slug: podcastindex-domain-security
  summary_line: TLSv1.3 · HSTS
slug: podcastindex
tags:
- Podcasting
- Podcast Index
- Discovery
- Open Data
website: https://podcastindex.org/
---
