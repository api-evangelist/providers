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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Apicbase Agentic Access
  operation_count: 10
  slug: apicbase-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.apicbase.com/api/v2/products/ingredients
  baseurl_source: declared
  description: Ingredient library entities.
  name: Apicbase Ingredients API
  slug: apicbase-ingredients-api
- baseURL: https://api.apicbase.com/api/v2/products/ingredients
  baseurl_source: declared
  description: Outlets (locations / accounts).
  name: Apicbase Outlets API
  slug: apicbase-outlets-api
- baseURL: https://api.apicbase.com/api/v2/products/ingredients
  baseurl_source: declared
  description: Purchase orders.
  name: Apicbase Procurement API
  slug: apicbase-procurement-api
- baseURL: https://api.apicbase.com/api/v2/products/ingredients
  baseurl_source: declared
  description: Recipes and menu engineering entities.
  name: Apicbase Recipes API
  slug: apicbase-recipes-api
- baseURL: https://api.apicbase.com/api/v2/products/ingredients
  baseurl_source: declared
  description: Stock items and inventory.
  name: Apicbase Stock API
  slug: apicbase-stock-api
- baseURL: https://api.apicbase.com/api/v2/products/ingredients
  baseurl_source: declared
  description: Suppliers and their packages.
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
  href: https://raw.githubusercontent.com/api-evangelist/apicbase/refs/heads/main/capabilities/apicbase-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/apicbase-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apicbase/refs/heads/main/agentic-access/apicbase-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apicbase-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apicbase/refs/heads/main/security/apicbase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apicbase-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apicbase/refs/heads/main/authentication/apicbase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apicbase-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apicbase/refs/heads/main/scopes/apicbase-scopes.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/apicbase/refs/heads/main/plans/apicbase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apicbase-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apicbase/refs/heads/main/rate-limits/apicbase-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apicbase-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apicbase/refs/heads/main/finops/apicbase-finops.yml
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
random_paper: 10
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
  composite: 36.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 21.4
    discoverability: 68.5
    operational_transparency: 34.2
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
