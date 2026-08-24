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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mastodon Instances Agentic Access
  operation_count: 6
  slug: mastodon-instances-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- description: The instances.social API allows searching for and retrieving information about Mastodon server instances, including user counts, language, software version, and uptime statistics.
  name: Mastodon Instances API
  slug: mastodon-instances
- description: The Instances API from Mastodon Instances — 4 operation(s) for instances.
  name: Mastodon Instances Instances API
  slug: mastodon-instances-instances-api
- description: The Versions API from Mastodon Instances — 2 operation(s) for versions.
  name: Mastodon Instances Versions API
  slug: mastodon-instances-versions-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mastodon Instances API
  slug: open-mastodon-instances-instances-api
- collection_type: open
  name: Mastodon Instances Versions API
  slug: open-mastodon-instances-versions-api
- collection_type: open
  name: Mastodon Instances API
  slug: open-mastodon-instances
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mastodon-instances-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mastodon-instances-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mastodon-instances-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://instances.social
- group: start
  title: ''
  type: Signup
  url: https://instances.social/api/token
created: '2024-12-02'
description: Mastodon Instances (instances.social) is a service for discovering Mastodon server instances. Its API allows developers to search for instances by criteria including language, user count, and stability, and to retrieve metadata about specific instances.
finops:
- name: Mastodon Instances Finops
  service_category: API
  slug: mastodon-instances-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mastodon-instances.png
layout: provider
modified: '2026-04-28'
name: Mastodon Instances
nav: Providers
network: true
overview: 'Mastodon Instances publishes 2 APIs on the [APIs.io](https://apis.io/) network: Instances API and Versions API. Tagged areas include Fediverse, Mastodon, Search, and Social.


  Mastodon Instances'' developer surface includes authentication, developer portal, signup flow, and 2 more developer resources.'
plans:
- name: Mastodon Instances Plans Pricing
  plan_count: 3
  slug: mastodon-instances-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Mastodon Instances Rate Limits
  slug: mastodon-instances-rate-limits
score:
  band: thin
  composite: 30.5
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mastodon-instances/refs/heads/main/screenshots/mastodon-instances-2026-06-20T185025.png
security:
- kind: authentication
  name: Mastodon Instances Authentication
  slug: mastodon-instances-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mastodon Instances Domain Security
  slug: mastodon-instances-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: mastodon-instances
tags:
- Fediverse
- Mastodon
- Search
- Social
website: https://instances.social
---
