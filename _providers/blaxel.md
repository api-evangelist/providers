---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
- acting_count: 34
  human_in_the_loop: 1
  name: Blaxel Agentic Access
  operation_count: 65
  slug: blaxel-agentic-access
  summary_line: 65 operations · 34 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Agents API from Blaxel — 3 operation(s) for agents.
  name: Blaxel Agents API
  slug: blaxel-agents-api
- description: The Compute API from Blaxel — 6 operation(s) for compute.
  name: Blaxel Compute API
  slug: blaxel-compute-api
- description: The Functions API from Blaxel — 3 operation(s) for functions.
  name: Blaxel Functions API
  slug: blaxel-functions-api
- description: The Integrations API from Blaxel — 5 operation(s) for integrations.
  name: Blaxel Integrations API
  slug: blaxel-integrations-api
- description: The Jobs API from Blaxel — 4 operation(s) for jobs.
  name: Blaxel Jobs API
  slug: blaxel-jobs-api
- description: The Locations API from Blaxel — 1 operation(s) for locations.
  name: Blaxel Locations API
  slug: blaxel-locations-api
- description: The Models API from Blaxel — 3 operation(s) for models.
  name: Blaxel Models API
  slug: blaxel-models-api
- description: The Policies API from Blaxel — 2 operation(s) for policies.
  name: Blaxel Policies API
  slug: blaxel-policies-api
- description: The Service Accounts API from Blaxel — 2 operation(s) for service accounts.
  name: Blaxel Service Accounts API
  slug: blaxel-service-accounts-api
- description: The Volumes API from Blaxel — 1 operation(s) for volumes.
  name: Blaxel Volumes API
  slug: blaxel-volumes-api
- description: The Workspaces API from Blaxel — 3 operation(s) for workspaces.
  name: Blaxel Workspaces API
  slug: blaxel-workspaces-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blaxel Control Plane Agents API
  slug: open-blaxel-agents-api
- collection_type: open
  name: Blaxel Control Plane Agents Compute API
  slug: open-blaxel-compute-api
- collection_type: open
  name: Blaxel Control Plane Agents Functions API
  slug: open-blaxel-functions-api
- collection_type: open
  name: Blaxel Control Plane Agents Integrations API
  slug: open-blaxel-integrations-api
- collection_type: open
  name: Blaxel Control Plane Agents Jobs API
  slug: open-blaxel-jobs-api
- collection_type: open
  name: Blaxel Control Plane Agents Locations API
  slug: open-blaxel-locations-api
- collection_type: open
  name: Blaxel Control Plane Agents Models API
  slug: open-blaxel-models-api
- collection_type: open
  name: Blaxel Control Plane Agents Policies API
  slug: open-blaxel-policies-api
- collection_type: open
  name: Blaxel Control Plane Agents Service Accounts API
  slug: open-blaxel-service-accounts-api
- collection_type: open
  name: Blaxel Control Plane Agents Volumes API
  slug: open-blaxel-volumes-api
- collection_type: open
  name: Blaxel Control Plane Agents Workspaces API
  slug: open-blaxel-workspaces-api
- collection_type: open
  name: Blaxel Control Plane API
  slug: open-blaxel
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blaxel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blaxel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blaxel-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blaxel-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blaxel
- group: company
  title: ''
  type: Website
  url: https://blaxel.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blaxel.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/blaxel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blaxel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/blaxel-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blaxel.ai/rss.xml
created: '2026-07-01'
description: Blaxel (formerly Beamlit) is an infrastructure and compute platform built for AI agents. Its control plane API deploys and manages agents, MCP/function servers, serverless code sandboxes, batch jobs, a multi-provider model gateway, deployment policies, integrations, and multi-tenant workspaces. The REST control plane lives at api.blaxel.ai/v0 and authenticates with a Bearer API key or OAuth 2.0.
finops:
- name: Blaxel Finops
  service_category: Compute
  slug: blaxel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blaxel.png
layout: provider
modified: '2026-07-01'
name: Blaxel
nav: Providers
network: true
overview: 'Blaxel publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Compute API, Functions API, and 8 more. Tagged areas include Artificial Intelligence, Agents, Infrastructure, Sandboxes, and MCP.


  Blaxel''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Blaxel Plans Pricing
  plan_count: 4
  slug: blaxel-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 6
  name: Blaxel Rate Limits
  slug: blaxel-rate-limits
score:
  band: developing
  composite: 39.4
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
    contract_quality: 52.4
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blaxel/refs/heads/main/screenshots/blaxel-2026-07-25T203304.png
security:
- kind: authentication
  name: Blaxel Authentication
  slug: blaxel-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Blaxel Domain Security
  slug: blaxel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blaxel
tags:
- Artificial Intelligence
- Agents
- Infrastructure
- Sandboxes
- MCP
- Compute
- Serverless
website: https://blaxel.ai/
---
