---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Patreon Agentic Access
  operation_count: 16
  slug: patreon-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 2
apis:
- description: 'The Patreon REST API v2 follows the JSON:API specification. It exposes campaigns, members (patrons), posts, tiers, benefits, addresses, and webhooks. Authentication uses OAuth 2.0 with creator-issued '
  name: Patreon API v2
  slug: patreon-api-v2
- description: The Oauth2 API from Patreon — 13 operation(s) for oauth2.
  name: Patreon Oauth2 API
  slug: patreon-oauth2-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Patreon API v2 Oauth2 API
  slug: open-patreon-oauth2-api
- collection_type: open
  name: Patreon API v2
  slug: open-patreon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/patreon-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/patreon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patreon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/patreon-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Patreon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/patreon
- group: company
  title: ''
  type: Website
  url: https://www.patreon.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.patreon.com/
- group: start
  title: ''
  type: Signup
  url: https://www.patreon.com/portal/registration/register-clients
- group: operate
  title: ''
  type: Forums
  url: https://www.patreondevelopers.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.patreon.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/patreon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/patreon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/patreon-finops.yml
created: '2026-05-08'
description: Patreon is a membership platform for creators offering tiered subscriptions, content publishing, community, and payments. The Patreon API v2 follows the JSON:API specification and exposes campaigns, members, posts, tiers, benefits, and webhooks via OAuth 2.0.
finops:
- name: Patreon Finops
  service_category: Creator Economy
  slug: patreon-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Patreon platform, derived from
  name: Patreon GraphQL Schema
  slug: patreon-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/patreon.png
layout: provider
modified: '2026-05-08'
name: Patreon
nav: Providers
network: true
overview: 'Patreon publishes 1 API on the [APIs.io](https://apis.io/) network: Oauth2 API. Tagged areas include Creator Economy, Membership, Subscription, Content, and Community.


  Patreon''s developer surface includes authentication, developer portal, signup flow, pricing, and 10 more developer resources.'
plans:
- name: Patreon Plans Pricing
  plan_count: 1
  slug: patreon-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Patreon Rate Limits
  slug: patreon-rate-limits
score:
  band: thin
  composite: 33.8
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 52.5
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/patreon/refs/heads/main/screenshots/patreon-2026-06-20T191442.png
security:
- kind: authentication
  name: Patreon Authentication
  slug: patreon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Patreon Domain Security
  slug: patreon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Patreon Vulnerability Disclosure
  slug: patreon-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: patreon
tags:
- Creator Economy
- Membership
- Subscription
- Content
- Community
website: https://www.patreon.com/
---
