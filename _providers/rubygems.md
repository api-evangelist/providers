---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Rubygems Agentic Access
  operation_count: 28
  slug: rubygems-agentic-access
  summary_line: 28 operations · 9 acting
api_count: 9
apis:
- description: The RubyGems Gems API (v1) provides endpoints for retrieving gem metadata, listing owned gems, submitting new gems, yanking gem versions, managing gem ownership, retrieving user profiles, querying gem
  name: RubyGems Gems API
  slug: gems-api
- description: The RubyGems Downloads API provides download count statistics for gems and individual gem versions hosted on RubyGems.org.
  name: RubyGems Downloads API
  slug: downloads-api
- description: The RubyGems Search API allows developers to search for gems by matching a query string against gem names and descriptions. Returns paginated results of active gems.
  name: RubyGems Search API
  slug: search-api
- description: The RubyGems Activity API provides activity feeds of the most recently added and most recently updated gems on RubyGems.org, useful for monitoring new releases and tracking ecosystem changes.
  name: RubyGems Activity API
  slug: activity-api
- description: The RubyGems Webhooks API enables webhook subscriptions that fire when gems are pushed to RubyGems.org. Webhooks can be scoped to a specific gem or applied globally using a wildcard. Includes test-fir
  name: RubyGems Webhooks API
  slug: webhooks-api
- description: Endpoints for querying gem dependency information.
  name: RubyGems Dependencies API
  slug: rubygems-dependencies-api
- description: Endpoints for managing gem ownership, including listing owners, adding and removing owners, and listing gems by owner.
  name: RubyGems Owners API
  slug: rubygems-owners-api
- description: Endpoints for retrieving user profile information from RubyGems.org.
  name: RubyGems Profiles API
  slug: rubygems-profiles-api
- description: Endpoints for querying detailed version information for specific gem versions, including metadata, dependencies, checksums, and platform-specific builds.
  name: RubyGems Versions API
  slug: rubygems-versions-api
artifact_total: 30
asyncapis:
- description: The RubyGems webhook event system delivers HTTP POST notifications when gems are pushed to RubyGems.org. Webhook subscribers receive a JSON payload containing the full gem metadata whenever a new vers
  name: RubyGems Webhook Events
  slug: rubygems-webhooks-asyncapi
collections:
- collection_type: open
  name: RubyGems Activity API
  slug: open-rubygems-activity-api
- collection_type: open
  name: RubyGems API V2
  slug: open-rubygems-api-v2
- collection_type: open
  name: RubyGems Downloads API
  slug: open-rubygems-downloads-api
- collection_type: open
  name: RubyGems Gems API
  slug: open-rubygems-gems-api
- collection_type: open
  name: RubyGems Search API
  slug: open-rubygems-search-api
- collection_type: open
  name: RubyGems Webhooks API
  slug: open-rubygems-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rubygems-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rubygems-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rubygems-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://rubygems.org/
- group: docs
  title: ''
  type: Documentation
  url: https://guides.rubygems.org/
- group: auth
  title: ''
  type: Authentication
  url: https://guides.rubygems.org/api-key-scopes/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rubygems/rubygems.org
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rubygems.org/
- group: company
  title: ''
  type: Blog
  url: https://blog.rubygems.org/
- group: agent
  title: ''
  type: LlmsText
  url: https://blog.rubygems.org/llms.txt
created: '2025-01-01'
description: RubyGems.org is the Ruby community's primary gem hosting service, providing the infrastructure for publishing, discovering, and installing Ruby gems. The RubyGems API enables programmatic access to gem metadata, version information, download statistics, search, owner management, webhooks, and the compact index used by Bundler for dependency resolution. RubyGems.org hosts over 160,000 gems with billions of total downloads.
examples:
- key_count: 2
  name: Rubygems Get Gem Info Example
  slug: rubygems-get-gem-info-example
- key_count: 2
  name: Rubygems Search Gems Example
  slug: rubygems-search-gems-example
finops:
- name: Rubygems Finops
  service_category: Developer Tools / Package Registry
  slug: rubygems-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rubygems.png
json_schemas:
- name: RubyGems Gem
  property_count: 23
  slug: rubygems-gem
json_structures:
- name: Rubygems Structure
  property_count: 0
  slug: rubygems-structure
jsonld:
- class_count: 0
  name: Rubygems Context
  property_count: 5
  slug: rubygems-context
layout: provider
modified: '2026-05-19'
name: RubyGems
nav: Providers
network: true
overview: 'RubyGems publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Gems API, Downloads API, Search API, and 6 more. Tagged areas include Ruby, Package Manager, Open Source, and Developer Tools.


  The RubyGems catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  RubyGems'' developer surface includes authentication, developer portal, documentation, GitHub presence, engineering blog, and 5 more developer resources.'
plans:
- name: Rubygems Plans Pricing
  plan_count: 1
  slug: rubygems-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 6
  name: Rubygems Rate Limits
  slug: rubygems-rate-limits
rules:
- name: RubyGems API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: rubygems-asyncapi-spectral-rules
- name: RubyGems API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: rubygems-jsonschema-spectral-rules
- name: RubyGems API Rules
  rule_count: 16
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 13
  slug: rubygems-spectral-rules
score:
  band: developing
  composite: 45.6
  delta: -3.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 71.9
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rubygems/refs/heads/main/screenshots/rubygems-2026-06-20T193246.png
security:
- kind: authentication
  name: Rubygems Authentication
  slug: rubygems-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Rubygems Domain Security
  slug: rubygems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rubygems
tags:
- Ruby
- Package Manager
- Open Source
- Developer Tools
website: https://rubygems.org/
---
