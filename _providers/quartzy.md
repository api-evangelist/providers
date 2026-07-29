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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Quartzy Agentic Access
  operation_count: 17
  slug: quartzy-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 6
apis:
- description: Lab inventory items and their physical instances.
  name: Quartzy Inventory Items API
  slug: quartzy-inventory-items-api
- description: Labs within an organization; the scope for inventory and ordering.
  name: Quartzy Labs API
  slug: quartzy-labs-api
- description: Procurement requests moving through Quartzy's ordering workflow.
  name: Quartzy Order Requests API
  slug: quartzy-order-requests-api
- description: Item type categories used to classify inventory and requests.
  name: Quartzy Types API
  slug: quartzy-types-api
- description: The authenticated user and service health.
  name: Quartzy User API
  slug: quartzy-user-api
- description: Event subscriptions for inventory and order-request changes.
  name: Quartzy Webhooks API
  slug: quartzy-webhooks-api
artifact_total: 15
collections:
- collection_type: open
  name: Quartzy Public API
  slug: open-quartzy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quartzy-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/quartzy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quartzy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quartzy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/quartzy-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quartzy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quartzy
- group: company
  title: ''
  type: Website
  url: https://www.quartzy.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.quartzy.com/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/quartzy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quartzy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/quartzy-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://support.quartzy.com/hc/en-us/articles/5333106670747-Quartzy-API-and-Webhooks
created: '2026-07-04'
description: Quartzy is a lab management platform for life science teams that combines inventory management, supply ordering, and procurement in one place. Labs track every consumable, reagent, and piece of equipment, submit and approve order requests, and buy from a catalog of millions of lab products. Quartzy exposes a documented public REST API at api.quartzy.com so teams can create and update inventory items and order requests from external systems - ELNs, LIMS, and homegrown tools - and subscribe to webhooks for inventory and order-request events. The API is authenticated with a per-user AccessToken (Access-Token header) or OAuth2, and is available to all Quartzy accounts.
finops:
- name: Quartzy Finops
  service_category: Lab Management and Procurement Software
  slug: quartzy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quartzy.png
layout: provider
modified: '2026-07-04'
name: Quartzy
nav: Providers
network: true
overview: 'Quartzy publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Inventory Items API, Labs API, Order Requests API, and 3 more. Tagged areas include Lab Management, Inventory Management, Life Sciences, Procurement, and Ordering.


  Quartzy''s developer surface includes authentication, documentation, support, and 10 more developer resources.'
plans:
- name: Quartzy Plans Pricing
  plan_count: 3
  slug: quartzy-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 3
  name: Quartzy Rate Limits
  slug: quartzy-rate-limits
scopes:
- name: Quartzy Scopes
  scope_count: 0
  slug: quartzy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 40.6
  delta: -4.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.5
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Quartzy Authentication
  slug: quartzy-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Quartzy Domain Security
  slug: quartzy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Quartzy Vulnerability Disclosure
  slug: quartzy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: quartzy
tags:
- Lab Management
- Inventory Management
- Life Sciences
- Procurement
- Ordering
- Laboratory
- Webhooks
website: https://www.quartzy.com
---
