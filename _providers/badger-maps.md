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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Badger Maps Agentic Access
  operation_count: 13
  slug: badger-maps-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- baseURL: https://badgerapis.badgermapping.com/api/2
  baseurl_source: declared
  description: Accounts (customers) - the businesses and contacts a rep maps and visits.
  name: Badger Maps Accounts API
  slug: badger-maps-accounts-api
- baseURL: https://badgerapis.badgermapping.com/api/2
  baseurl_source: declared
  description: Timestamped activity logs recorded against an account (the /appointments/ resource).
  name: Badger Maps Check-Ins API
  slug: badger-maps-check-ins-api
- baseURL: https://badgerapis.badgermapping.com/api/2
  baseurl_source: declared
  description: Physical, geocoded locations attached to an account.
  name: Badger Maps Locations API
  slug: badger-maps-locations-api
- baseURL: https://badgerapis.badgermapping.com/api/2
  baseurl_source: declared
  description: Optimized driving routes and their ordered waypoints.
  name: Badger Maps Routes API
  slug: badger-maps-routes-api
- baseURL: https://badgerapis.badgermapping.com/api/2
  baseurl_source: declared
  description: Authentication, the authenticated user profile, and user search.
  name: Badger Maps Users API
  slug: badger-maps-users-api
artifact_total: 20
asyncapis:
- description: ''
  name: Badger Maps Webhooks
  slug: badger-maps-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Badger Maps Accounts API
  slug: open-badger-maps-accounts-api
- collection_type: open
  name: Badger Maps Accounts Check-Ins API
  slug: open-badger-maps-check-ins-api
- collection_type: open
  name: Badger Maps Accounts Locations API
  slug: open-badger-maps-locations-api
- collection_type: open
  name: Badger Maps Accounts Routes API
  slug: open-badger-maps-routes-api
- collection_type: open
  name: Badger Maps Accounts Users API
  slug: open-badger-maps-users-api
- collection_type: open
  name: Badger Maps API
  slug: open-badger-maps
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/badger-maps-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/badger-maps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/badger-maps-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BadgerMaps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/badger-maps
- group: company
  title: ''
  type: Website
  url: https://www.badgermapping.com
- group: docs
  title: ''
  type: Documentation
  url: https://badgerupdatedapi.docs.apiary.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/badger-maps-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/badger-maps-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/badger-maps-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.badgermapping.com/blog/
- group: other
  title: ''
  type: APIBlueprint
  url: openapi/_original/badger-maps-apiary-blueprint.apib
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/badger-maps-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/badger-maps-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/badger-maps-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/badger-maps-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/badger-maps-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.badgermapping.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/badger-maps-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/badger-maps-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/badger-maps-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/badger-maps-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/badger-maps-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://badgerupdatedapi.docs.apiary.io/
- group: docs
  title: ''
  type: APIReference
  url: https://badgerupdatedapi.docs.apiary.io/#reference
- group: start
  title: ''
  type: GettingStarted
  url: https://badgerupdatedapi.docs.apiary.io/#introduction/authorization
- group: operate
  title: ''
  type: Support
  url: https://www.badgermapping.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.badgermapping.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.badgermapping.com/free-trial/
- group: start
  title: ''
  type: Login
  url: https://www.badgermapping.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.badgermapping.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.badgermapping.com/privacy-policy/
created: '2026-07-04'
description: Badger Maps is field sales route planning, mapping, and CRM software for outside sales and field teams - it optimizes daily driving routes, maps and filters accounts on a territory, captures check-ins, and reports on rep activity. Badger Maps also exposes a token-authenticated REST API (base https://badgerapis.badgermapping.com/api/2) that lets teams programmatically manage accounts (customers), account locations, routes, check-ins, and users, and sync data with CRMs and other systems. API/Developer Key access is included with paid plans (max 25k requests per day, per team); the key must be enabled by contacting Badger Maps support.
finops:
- name: Badger Maps Finops
  service_category: Field Sales and Route Planning Software
  slug: badger-maps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/badger-maps.png
layout: provider
mcp_servers:
- description: Badger Maps ships no Model Context Protocol server. A search of the provider docs, the company GitHub organization (github.com/BadgerMaps), npm and the public MCP registries on 2026-08-13 found no fir
  name: Badger Maps MCP Server
  slug: badger-maps-mcp-server
modified: '2026-08-13'
name: Badger Maps
nav: Providers
network: true
overview: 'Badger Maps publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Check-Ins API, Locations API, and 2 more. Tagged areas include Field Sales, Route Planning, Mapping, CRM, and Sales Enablement.


  The Badger Maps catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Badger Maps'' developer surface includes authentication, documentation, engineering blog, sandbox, API reference, getting-started guide, support, and 26 more developer resources.'
plans:
- name: Badger Maps Plans Pricing
  plan_count: 6
  slug: badger-maps-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Badger Maps Rate Limits
  slug: badger-maps-rate-limits
score:
  band: strong
  composite: 58.8
  coverage:
    artifact_dirs: 23
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 66.8
    developer_ergonomics: 51.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/badger-maps/refs/heads/main/screenshots/badger-maps-2026-07-25T202239.png
security:
- kind: authentication
  name: Badger Maps Authentication
  slug: badger-maps-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Badger Maps Domain Security
  slug: badger-maps-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: badger-maps
tags:
- Field Sales
- Route Planning
- Mapping
- CRM
- Sales Enablement
- Territory Management
website: https://www.badgermapping.com
---
