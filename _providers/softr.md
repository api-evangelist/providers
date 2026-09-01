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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Softr Agentic Access
  operation_count: 14
  slug: softr-agentic-access
  summary_line: 14 operations · 11 acting
api_count: 1
apis:
- description: 'Softr Workflows fire outbound automations and HTTP webhook calls in response to app events (such as record or user changes), letting external systems react to activity inside a Softr app. There is no '
  name: Softr Webhooks and Workflows
  slug: webhooks
- description: List and manage Softr Databases.
  name: Softr Databases API
  slug: softr-databases-api
- description: Create, read, update, delete, and search records.
  name: Softr Records API
  slug: softr-records-api
- description: Manage end users of a published Softr app.
  name: Softr Users API
  slug: softr-users-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Softr Databases API
  slug: open-softr-databases-api
- collection_type: open
  name: Softr Databases Records API
  slug: open-softr-records-api
- collection_type: open
  name: Softr Databases Users API
  slug: open-softr-users-api
- collection_type: open
  name: Softr API
  slug: open-softr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/softr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/softr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/softr-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/softr-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/softr
- group: company
  title: ''
  type: Website
  url: https://www.softr.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.softr.io
- group: commercial
  title: ''
  type: Plans
  url: plans/softr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/softr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/softr-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.softr.io/blog
created: '2026-06-20'
description: Softr is a no-code platform for building client portals, internal tools, and web apps on top of Airtable, Google Sheets, and the native Softr Database. Its public REST APIs let you manage app users (create, invite, activate, magic links) and read and write records in Softr Databases programmatically using a Softr-Api-Key header.
finops:
- name: Softr Finops
  service_category: Developer Tools and No-Code Platforms
  slug: softr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/softr.png
layout: provider
modified: '2026-06-20'
name: Softr
nav: Providers
network: true
overview: 'Softr publishes 3 APIs on the [APIs.io](https://apis.io/) network: Databases API, Records API, and Users API. Tagged areas include No-Code, App Builder, Client Portals, User Management, and Database.


  Softr''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Softr Plans Pricing
  plan_count: 5
  slug: softr-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 6
  name: Softr Rate Limits
  slug: softr-rate-limits
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/softr/refs/heads/main/screenshots/softr-2026-06-20T194132.png
security:
- kind: authentication
  name: Softr Authentication
  slug: softr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Softr Domain Security
  slug: softr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: softr
tags:
- No-Code
- App Builder
- Client Portals
- User Management
- Database
website: https://www.softr.io
---
