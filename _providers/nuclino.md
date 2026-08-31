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
    openapi_examples: verified
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
  name: Nuclino Agentic Access
  operation_count: 11
  slug: nuclino-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 1
apis:
- description: Groups/folders of items
  name: Nuclino Collections API
  slug: nuclino-collections-api
- description: File management
  name: Nuclino Files API
  slug: nuclino-files-api
- description: Wiki pages and documents
  name: Nuclino Items API
  slug: nuclino-items-api
- description: Team management
  name: Nuclino Teams API
  slug: nuclino-teams-api
- description: User management
  name: Nuclino Users API
  slug: nuclino-users-api
- description: Workspace management
  name: Nuclino Workspaces API
  slug: nuclino-workspaces-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nuclino Collections API
  slug: open-nuclino-collections-api
- collection_type: open
  name: Nuclino Collections Files API
  slug: open-nuclino-files-api
- collection_type: open
  name: Nuclino Collections Items API
  slug: open-nuclino-items-api
- collection_type: open
  name: Nuclino Collections Teams API
  slug: open-nuclino-teams-api
- collection_type: open
  name: Nuclino Collections Users API
  slug: open-nuclino-users-api
- collection_type: open
  name: Nuclino Collections Workspaces API
  slug: open-nuclino-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nuclino-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nuclino-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuclino-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nuclino-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.nuclino.com/d3a29686-api
- group: auth
  title: ''
  type: Authentication
  url: https://help.nuclino.com/8090bb76-authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://help.nuclino.com/b147124e-rate-limiting
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nuclino.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.nuclino.com/
- group: start
  title: ''
  type: Signup
  url: https://app.nuclino.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.nuclino.com/login
- group: auth
  title: ''
  type: APIKeys
  url: https://help.nuclino.com/04598850-manage-api-keys
- group: docs
  title: ''
  type: Documentation
  url: https://help.nuclino.com/70af7f4f-connect-nuclino-to-ai-assistants-with-mcp
- group: commercial
  title: ''
  type: Plans
  url: plans/nuclino-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nuclino-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nuclino-finops.yml
created: '2026-06-13'
description: Nuclino is a unified team workspace that combines wikis, docs, and project management into one collaborative platform. Its REST API enables developers to build integrations and automate tasks by programmatically managing items, collections, workspaces, teams, users, fields, and files using Markdown content. The API covers the full content lifecycle — create, read, update, delete, and search — making it possible to sync knowledge bases with external systems, trigger content updates from CI/CD pipelines, and build custom tooling on top of team documentation.
examples:
- key_count: 3
  name: Create Item
  slug: create-item
- key_count: 3
  name: List Workspaces
  slug: list-workspaces
- key_count: 3
  name: Search Items
  slug: search-items
finops:
- name: Nuclino Finops
  service_category: ''
  slug: nuclino-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuclino.png
json_schemas:
- name: Nuclino Item
  property_count: 12
  slug: item
- name: Nuclino Team
  property_count: 3
  slug: team
- name: Nuclino User
  property_count: 6
  slug: user
- name: Nuclino Workspace
  property_count: 8
  slug: workspace
jsonld:
- class_count: 9
  name: Nuclino Context
  property_count: 19
  slug: nuclino-context
layout: provider
modified: '2026-06-13'
name: Nuclino
nav: Providers
network: true
overview: 'Nuclino publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Files API, Items API, and 3 more. Tagged areas include Knowledge-Management, Team Workspace, Documentation, Wiki, and Collaboration.


  The Nuclino catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nuclino''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, and 11 more developer resources.'
plans:
- name: Nuclino Plans Pricing
  plan_count: 3
  slug: nuclino-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Nuclino Rate Limits
  slug: nuclino-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Nuclino API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nuclino-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 40.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 64.5
    commercial_clarity: 64.5
    contract_governance: 9.8
    contract_quality: 69.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 46.3
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
screenshot: https://raw.githubusercontent.com/api-evangelist/nuclino/refs/heads/main/screenshots/nuclino-2026-06-20T190507.png
security:
- kind: authentication
  name: Nuclino Authentication
  slug: nuclino-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nuclino Domain Security
  slug: nuclino-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Nuclino Trust Center
  slug: nuclino-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, GDPR
slug: nuclino
tags:
- Knowledge-Management
- Team Workspace
- Documentation
- Wiki
- Collaboration
- Project Management
- REST API
---
