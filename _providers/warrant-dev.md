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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Warrant Dev Agentic Access
  operation_count: 29
  slug: warrant-dev-agentic-access
  summary_line: 29 operations · 17 acting
api_count: 5
apis:
- description: Real-time access checks and relationship queries.
  name: Warrant Check API
  slug: warrant-dev-check-api
- description: The authorization model - object types and their relations.
  name: Warrant Object Types API
  slug: warrant-dev-object-types-api
- description: Resources and subjects that participate in the authorization model.
  name: Warrant Objects API
  slug: warrant-dev-objects-api
- description: RBAC and entitlements convenience surface (roles, permissions, users, tenants, features, pricing tiers).
  name: Warrant Roles and Permissions API
  slug: warrant-dev-roles-and-permissions-api
- description: Relationship tuples (access rules) between subjects and objects.
  name: Warrant Warrants API
  slug: warrant-dev-warrants-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Warrant Check API
  slug: open-warrant-dev-check-api
- collection_type: open
  name: Warrant Check Object Types API
  slug: open-warrant-dev-object-types-api
- collection_type: open
  name: Warrant Check Objects API
  slug: open-warrant-dev-objects-api
- collection_type: open
  name: Warrant Check Roles and Permissions API
  slug: open-warrant-dev-roles-and-permissions-api
- collection_type: open
  name: Warrant Check Warrants API
  slug: open-warrant-dev-warrants-api
- collection_type: open
  name: Warrant API (Retired)
  slug: open-warrant-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/warrant-dev-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/warrant-dev-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/warrant-dev-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/warrant-dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/warrant-dev
- group: company
  title: ''
  type: Website
  url: https://warrant.dev
- group: docs
  title: ''
  type: Documentation
  url: https://workos.com/docs/fga
- group: commercial
  title: ''
  type: Plans
  url: plans/warrant-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/warrant-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/warrant-dev-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.warrant.dev
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-07-11'
description: Warrant was a centralized, fine-grained authorization (FGA) and access control service inspired by Google Zanzibar, exposing a real-time REST API to define an authorization model, store relationships (warrants) between objects, and run low-latency access checks and queries. It supported relationship-based (ReBAC), role-based (RBAC), and attribute-based (ABAC) access control, plus entitlements such as pricing tiers and feature gating. The core engine is open source (Apache-2.0, github.com/warrant-dev/warrant) and self-hostable. Warrant was acquired by WorkOS on 2024-04-23 and folded into WorkOS FGA; the standalone hosted Warrant service (api.warrant.dev) and the Warrant-based WorkOS FGA were deprecated and sunset on 2025-11-15. This entry documents Warrant's public API surface historically - the endpoints modeled here reflect the documented api.warrant.dev v1/v2 API and are RETIRED. Current fine-grained authorization is offered through WorkOS; the open-source engine remains self-hostable.
finops:
- name: Warrant Dev Finops
  service_category: Identity and Access Management
  slug: warrant-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/warrant-dev.png
layout: provider
modified: '2026-08-08'
name: Warrant
nav: Providers
network: true
overview: 'Warrant publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Check API, Object Types API, Objects API, and 2 more. Tagged areas include Access Control, Authorization, Fine-Grained Authorization, FGA, and RBAC.


  Warrant''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Warrant Dev Plans Pricing
  plan_count: 4
  slug: warrant-dev-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Warrant Dev Rate Limits
  slug: warrant-dev-rate-limits
score:
  band: thin
  composite: 38.2
  delta: 0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 49.1
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/warrant-dev/refs/heads/main/screenshots/warrant-dev-2026-06-20T201232.png
security:
- kind: authentication
  name: Warrant Dev Authentication
  slug: warrant-dev-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Warrant Dev Domain Security
  slug: warrant-dev-domain-security
  summary_line: DNSSEC · DMARC
slug: warrant-dev
tags:
- Access Control
- Authorization
- Fine-Grained Authorization
- FGA
- RBAC
- ReBAC
- ABAC
- Zanzibar
- Permissions
- Open-Source
- Retired
website: https://warrant.dev
---
