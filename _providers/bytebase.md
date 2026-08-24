---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Bytebase Agentic Access
  operation_count: 24
  slug: bytebase-agentic-access
  summary_line: 24 operations · 12 acting
api_count: 12
apis:
- description: The Auth API from Bytebase — 1 operation(s) for auth.
  name: Bytebase Auth API
  slug: bytebase-auth-api
- description: The Databases API from Bytebase — 2 operation(s) for databases.
  name: Bytebase Databases API
  slug: bytebase-databases-api
- description: The Groups API from Bytebase — 1 operation(s) for groups.
  name: Bytebase Groups API
  slug: bytebase-groups-api
- description: The Instances API from Bytebase — 2 operation(s) for instances.
  name: Bytebase Instances API
  slug: bytebase-instances-api
- description: The Issues API from Bytebase — 3 operation(s) for issues.
  name: Bytebase Issues API
  slug: bytebase-issues-api
- description: The Plans API from Bytebase — 1 operation(s) for plans.
  name: Bytebase Plans API
  slug: bytebase-plans-api
- description: The Projects API from Bytebase — 2 operation(s) for projects.
  name: Bytebase Projects API
  slug: bytebase-projects-api
- description: The Roles API from Bytebase — 1 operation(s) for roles.
  name: Bytebase Roles API
  slug: bytebase-roles-api
- description: The Rollouts API from Bytebase — 2 operation(s) for rollouts.
  name: Bytebase Rollouts API
  slug: bytebase-rollouts-api
- description: The Sheets API from Bytebase — 1 operation(s) for sheets.
  name: Bytebase Sheets API
  slug: bytebase-sheets-api
- description: The Users API from Bytebase — 1 operation(s) for users.
  name: Bytebase Users API
  slug: bytebase-users-api
- description: The Webhooks API from Bytebase — 1 operation(s) for webhooks.
  name: Bytebase Webhooks API
  slug: bytebase-webhooks-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bytebase Auth API
  slug: open-bytebase-auth-api
- collection_type: open
  name: Bytebase Auth Databases API
  slug: open-bytebase-databases-api
- collection_type: open
  name: Bytebase Auth Groups API
  slug: open-bytebase-groups-api
- collection_type: open
  name: Bytebase Auth Instances API
  slug: open-bytebase-instances-api
- collection_type: open
  name: Bytebase Auth Issues API
  slug: open-bytebase-issues-api
- collection_type: open
  name: Bytebase Auth Plans API
  slug: open-bytebase-plans-api
- collection_type: open
  name: Bytebase Auth Projects API
  slug: open-bytebase-projects-api
- collection_type: open
  name: Bytebase Auth Roles API
  slug: open-bytebase-roles-api
- collection_type: open
  name: Bytebase Auth Rollouts API
  slug: open-bytebase-rollouts-api
- collection_type: open
  name: Bytebase Auth Sheets API
  slug: open-bytebase-sheets-api
- collection_type: open
  name: Bytebase Auth Users API
  slug: open-bytebase-users-api
- collection_type: open
  name: Bytebase Auth Webhooks API
  slug: open-bytebase-webhooks-api
- collection_type: open
  name: Bytebase API
  slug: open-bytebase
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bytebase-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bytebase-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bytebase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bytebase-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bytebase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bytebase
- group: company
  title: ''
  type: Website
  url: https://www.bytebase.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bytebase.com/integrations/api/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/bytebase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bytebase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bytebase-finops.yml
created: '2026-06-21'
description: Bytebase is a database DevOps and CI/CD platform - the GitOps-style control plane for schema change, migration, and access management across MySQL, PostgreSQL, and many other engines. Every action in the web console is backed by a documented API exposed as both Connect/gRPC and RESTful HTTP (gRPC transcoding), authenticated with a service-account Bearer token. Bytebase ships as free, self-hostable open source (OSS) with paid Pro and Enterprise tiers.
finops:
- name: Bytebase Finops
  service_category: Developer Tools
  slug: bytebase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bytebase.png
layout: provider
modified: '2026-06-21'
name: Bytebase
nav: Providers
network: true
overview: 'Bytebase publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Databases API, Groups API, and 9 more. Tagged areas include Database, DevOps, Schema Migration, CI/CD, and DevSecOps.


  Bytebase''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Bytebase Plans Pricing
  plan_count: 3
  slug: bytebase-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Bytebase Rate Limits
  slug: bytebase-rate-limits
score:
  band: thin
  composite: 37.0
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 53.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bytebase/refs/heads/main/screenshots/bytebase-2026-07-25T204142.png
security:
- kind: authentication
  name: Bytebase Authentication
  slug: bytebase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bytebase Domain Security
  slug: bytebase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bytebase Trust Center
  slug: bytebase-trust-center
  summary_line: SOC 2, HIPAA
slug: bytebase
tags:
- Database
- DevOps
- Schema Migration
- CI/CD
- DevSecOps
website: https://www.bytebase.com
---
