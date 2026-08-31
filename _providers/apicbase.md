---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Apicbase Agentic Access
  operation_count: 10
  slug: apicbase-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- description: Ingredient library entities.
  name: Apicbase Ingredients API
  slug: apicbase-ingredients-api
- description: Outlets (locations / accounts).
  name: Apicbase Outlets API
  slug: apicbase-outlets-api
- description: Purchase orders.
  name: Apicbase Procurement API
  slug: apicbase-procurement-api
- description: Recipes and menu engineering entities.
  name: Apicbase Recipes API
  slug: apicbase-recipes-api
- description: Stock items and inventory.
  name: Apicbase Stock API
  slug: apicbase-stock-api
- description: Suppliers and their packages.
  name: Apicbase Suppliers API
  slug: apicbase-suppliers-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apicbase Ingredients API
  slug: open-apicbase-ingredients-api
- collection_type: open
  name: Apicbase Ingredients Outlets API
  slug: open-apicbase-outlets-api
- collection_type: open
  name: Apicbase Ingredients Procurement API
  slug: open-apicbase-procurement-api
- collection_type: open
  name: Apicbase Ingredients Recipes API
  slug: open-apicbase-recipes-api
- collection_type: open
  name: Apicbase Ingredients Stock API
  slug: open-apicbase-stock-api
- collection_type: open
  name: Apicbase Ingredients Suppliers API
  slug: open-apicbase-suppliers-api
- collection_type: open
  name: Apicbase API
  slug: open-apicbase
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/apicbase-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apicbase-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apicbase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apicbase-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/apicbase-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/APICBASE
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apicbase
- group: company
  title: ''
  type: Website
  url: https://www.apicbase.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.apicbase.com/docs/welcome
- group: commercial
  title: ''
  type: Plans
  url: plans/apicbase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apicbase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/apicbase-finops.yml
created: '2026-06-21'
description: Apicbase is a cloud-based food & beverage back-of-house management platform for restaurants, hotels, and catering groups, covering recipes and menu engineering, ingredient libraries, inventory and stock, procurement, suppliers, and multi-outlet operations. The Apicbase REST API exposes these entities over HTTPS with OAuth 2.0 authentication, plus webhooks for integrated supplier ordering.
finops:
- name: Apicbase Finops
  service_category: Management and Governance
  slug: apicbase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apicbase.png
layout: provider
modified: '2026-06-21'
name: Apicbase
nav: Providers
network: true
overview: 'Apicbase publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Ingredients API, Outlets API, Procurement API, and 3 more. Tagged areas include Food and Beverage, Restaurant, Back Of House, Inventory, and Procurement.


  Apicbase''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Apicbase Plans Pricing
  plan_count: 4
  slug: apicbase-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Apicbase Rate Limits
  slug: apicbase-rate-limits
scopes:
- name: Apicbase Scopes
  scope_count: 2
  slug: apicbase-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apicbase/refs/heads/main/screenshots/apicbase-2026-07-25T200623.png
security:
- kind: authentication
  name: Apicbase Authentication
  slug: apicbase-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Apicbase Domain Security
  slug: apicbase-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: apicbase
tags:
- Food and Beverage
- Restaurant
- Back Of House
- Inventory
- Procurement
- Recipes
website: https://www.apicbase.com
---
