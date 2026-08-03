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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Phraseanet Agentic Access
  operation_count: 34
  slug: phraseanet-agentic-access
  summary_line: 34 operations · 14 acting
api_count: 9
apis:
- description: The authenticated user (me) and access rights.
  name: Phraseanet Account API
  slug: phraseanet-account-api
- description: User-curated working sets of records.
  name: Phraseanet Baskets API
  slug: phraseanet-baskets-api
- description: Databoxes, their collections, status structure, and metadata structure.
  name: Phraseanet Databoxes API
  slug: phraseanet-databoxes-api
- description: Published feeds and their entries.
  name: Phraseanet Feeds API
  slug: phraseanet-feeds-api
- description: Record captions, metadata values, and status flags.
  name: Phraseanet Metadata API
  slug: phraseanet-metadata-api
- description: Items awaiting validation before entering a collection.
  name: Phraseanet Quarantine API
  slug: phraseanet-quarantine-api
- description: Individual media records (assets) within a databox.
  name: Phraseanet Records API
  slug: phraseanet-records-api
- description: Elasticsearch-backed search across records and stories.
  name: Phraseanet Search API
  slug: phraseanet-search-api
- description: Records that group other records.
  name: Phraseanet Stories API
  slug: phraseanet-stories-api
artifact_total: 17
collections:
- collection_type: open
  name: Phraseanet API (v1)
  slug: open-phraseanet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/phraseanet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phraseanet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/phraseanet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/phraseanet-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alchemy-fr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/products/alchemy-sarl-phraseanet/
- group: company
  title: ''
  type: Website
  url: https://www.phraseanet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phraseanet.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/alchemy-fr/Phraseanet
- group: commercial
  title: ''
  type: Plans
  url: plans/phraseanet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/phraseanet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/phraseanet-finops.yml
created: '2026-07-05'
description: Phraseanet is an open-source (GPL-v3) Digital Asset Management (DAM) platform built in PHP and developed by Alchemy. It centralizes photos, videos, documents, and other media with metadata management (Dublin Core mapping), Elasticsearch-powered search, multi-resolution sub-definitions, thesaurus, rights administration, stories, baskets, and feeds. Phraseanet exposes a documented RESTful API (v1 and v2, with a newer v3 published on SwaggerHub) secured with OAuth2, covering records, databoxes and collections, metadata, search, stories, baskets, and feeds. Because Phraseanet is self-hosted, there is no single public shared API endpoint - the API runs on each organization's own Phraseanet instance. Alchemy provides commercial hosting, setup, training, and support around the open-source core.
finops:
- name: Phraseanet Finops
  service_category: Digital Asset Management
  slug: phraseanet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phraseanet.png
layout: provider
modified: '2026-07-05'
name: Phraseanet
nav: Providers
network: true
overview: 'Phraseanet publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Baskets API, Databoxes API, and 6 more. Tagged areas include Digital Asset Management, DAM, Media, Metadata, and Open Source.


  Phraseanet''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Phraseanet Plans Pricing
  plan_count: 3
  slug: phraseanet-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 4
  name: Phraseanet Rate Limits
  slug: phraseanet-rate-limits
scopes:
- name: Phraseanet Scopes
  scope_count: 0
  slug: phraseanet-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Phraseanet Authentication
  slug: phraseanet-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Phraseanet Domain Security
  slug: phraseanet-domain-security
  summary_line: TLSv1.3
slug: phraseanet
tags:
- Digital Asset Management
- DAM
- Media
- Metadata
- Open Source
- Search
website: https://www.phraseanet.com/
---
