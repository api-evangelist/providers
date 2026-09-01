---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: Create and update projects and organize their contents in folders - the top-level container that takeoffs, plans, and estimates hang off of. Modeled from STACK's developer tutorials (POST/PUT /Project
  name: STACK Projects API
  slug: stack-takeoff-projects-api
- description: Upload plan sets and supporting documents into project folders, read file metadata, update file properties, and download plans. Modeled from STACK's developer tutorials (Folders/Files endpoints).
  name: STACK Plans & Files API
  slug: stack-takeoff-plans-files-api
- description: Create takeoffs on a project, list a takeoff's pages, set page scale, and retrieve measured quantities. On-screen takeoff is STACK's core workflow. Modeled from STACK's developer tutorials (CreateTake
  name: STACK Takeoffs API
  slug: stack-takeoff-takeoffs-api
- description: Create, update, and retrieve estimate proposals - turning takeoff quantities into priced line items and a bid. Modeled from STACK's developer tutorials (EstimateProposals endpoints).
  name: STACK Estimates API
  slug: stack-takeoff-estimates-api
- description: Manage items and assemblies attached to takeoffs and retrieve their quantities and costs, so partner tools can pull takeoff/estimating data into invoices, purchase orders, or a separate estimating sys
  name: STACK Items & Assemblies API
  slug: stack-takeoff-items-assemblies-api
- description: Read-only lookup endpoints for cost types, states, and countries used when constructing projects and estimates. Modeled from STACK's developer tutorials (CostTypes, States, Countries).
  name: STACK Reference Data API
  slug: stack-takeoff-reference-data-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stack-takeoff-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stack-construction-technologies
- group: company
  title: ''
  type: Website
  url: https://www.stackct.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.stackct.com/developers-docs/
- group: auth
  title: ''
  type: Authentication
  url: https://www.stackct.com/developers-docs-authentication/
- group: start
  title: ''
  type: SignUp
  url: https://www.stackct.com/developers/
- group: commercial
  title: ''
  type: Plans
  url: plans/stack-takeoff-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stack-takeoff-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stack-takeoff-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.stackct.com/blog/
created: '2026-07-04'
description: STACK Construction Technologies makes cloud-based preconstruction software for on-screen takeoff and estimating used by contractors across most trades. STACK does expose a real, documented REST API (v2), but access is gated - you must be a STACK customer on an API-Enabled Subscription (or an approved partner) to obtain credentials. Authentication is OAuth 2.0, offered as two-legged (client-credentials, server-to-server) and three-legged (authorization-code, on behalf of a user) flows. Tokens are issued by a per-tenant authorization server (base pattern https://{server}/api/v2). The full endpoint reference sits behind an access request; the API surface catalogued here is modeled from STACK's public developer overview, authentication guide, and tutorials - it is not sourced from an official machine-readable OpenAPI document.
finops:
- name: Stack Takeoff Finops
  service_category: Construction Software (SaaS)
  slug: stack-takeoff-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stack-takeoff.png
layout: provider
modified: '2026-07-04'
name: STACK
nav: Providers
network: true
overview: 'STACK publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Preconstruction, Takeoff, Estimating, and Construction Technology.


  STACK''s developer surface includes documentation, authentication, signup flow, engineering blog, and 6 more developer resources.'
plans:
- name: Stack Takeoff Plans Pricing
  plan_count: 4
  slug: stack-takeoff-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Stack Takeoff Rate Limits
  slug: stack-takeoff-rate-limits
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 28.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Stack Takeoff Domain Security
  slug: stack-takeoff-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stack-takeoff
tags:
- Construction
- Preconstruction
- Takeoff
- Estimating
- Construction Technology
- Partner API
website: https://www.stackct.com/
---
