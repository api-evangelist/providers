---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
- acting_count: 5
  human_in_the_loop: 0
  name: Port Io Agentic Access
  operation_count: 8
  slug: port-io-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 16
apis:
- description: Public REST API for the Port platform. Bearer-token authenticated (3-hour tokens minted from Port credentials), with regional base URLs for EU and US tenants. Body size capped at 1 MiB and every respo
  name: Port REST API
  slug: rest-api
- description: Endpoints to create, read, update, and delete blueprints - the schemas that define an organization's data model in the Port catalog (services, environments, AI agents, cloud resources, etc.).
  name: Port Blueprints API
  slug: blueprints
- description: Endpoints to create, search, update, and delete entities (instances of a blueprint) in the Port catalog, plus bulk operations and relations.
  name: Port Entities API
  slug: entities
- description: Endpoints to manage self-service actions on blueprints and entities - day-2 operations, scaffolding, and workflows that developers run from the Port UI or programmatically.
  name: Port Actions API
  slug: actions
- description: Endpoints to trigger action runs, fetch their status and logs, post progress updates from external runners, and approve or reject pending runs.
  name: Port Action Runs API
  slug: action-runs
- description: Endpoints to define and orchestrate multi-step workflows that chain Port actions, integration runs, and approvals.
  name: Port Workflows API
  slug: workflows
- description: Endpoints to manage scorecards (production readiness, security, SLO compliance, etc.) and query scores per entity.
  name: Port Scorecards API
  slug: scorecards
- description: Endpoints to register, configure, and ingest data from Port integrations (Ocean), including resync, mapping configuration, and integration lifecycle.
  name: Port Integrations API
  slug: integrations
- description: Endpoints to register webhook subscriptions and to receive inbound webhook events from upstream systems for ingestion into the Port catalog.
  name: Port Webhooks API
  slug: webhooks
- description: Endpoints to manage teams, users, roles, and team-membership for the Port organization.
  name: Port Teams and Users API
  slug: teams-users
- description: Endpoints to query Port audit logs for catalog, action, integration, and administrative events.
  name: Port Audit API
  slug: audit
- description: Endpoints to manage AI agents, prompts, memory, and LLM-driven capabilities embedded in the Port platform.
  name: Port AI and LLM Management API
  slug: ai-agents
- description: Endpoints to manage portal pages, apps, and plugin extensions that compose the developer-facing surface of the Port IDP.
  name: Port Pages, Apps, and Plugins API
  slug: pages
- description: Open-source framework used to build Port integrations that ingest data from third-party systems into the catalog. Maintained at github.com/port-labs/ocean.
  name: Port Ocean Integration Framework
  slug: ocean
- description: Manage blueprint definitions in the software catalog.
  name: Port Blueprints API
  slug: port-io-blueprints-api
- description: Manage catalog entities created from blueprints.
  name: Port Entities API
  slug: port-io-entities-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Port REST Blueprints API
  slug: open-port-io-blueprints-api
- collection_type: open
  name: Port REST Blueprints Entities API
  slug: open-port-io-entities-api
- collection_type: open
  name: Port REST API
  slug: open-port-io
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/port-labs/ocean/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/port-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/port-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/port-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/port-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/port-io-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getport
- group: company
  title: ''
  type: Website
  url: https://www.port.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.port.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/port-labs
- group: commercial
  title: ''
  type: Plans
  url: plans/port-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/port-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/port-io-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.port.io/llms.txt
created: '2026-05-23'
description: Port is an Internal Developer Portal built around an API-first software catalog, customizable blueprints and entities, self-service actions, and scorecards. Platform teams model their own domain (services, environments, pipelines, AI agents, cloud resources) as blueprints, ingest data from integrations (GitHub, GitLab, AWS, Azure, GCP, Kubernetes, Datadog, PagerDuty, Snyk, ServiceNow), and expose developer workflows as self-service actions backed by GitHub Actions, GitLab pipelines, Jenkins, Argo, or webhooks. Everything in Port - blueprints, entities, actions, runs, scorecards, integrations, pages, webhooks, AI agents - is reachable via the public REST API.
finops:
- name: Port Io Finops
  service_category: API
  slug: port-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/port-io.png
layout: provider
modified: '2026-05-23'
name: Port
nav: Providers
network: true
overview: 'Port publishes 2 APIs on the [APIs.io](https://apis.io/) network: Blueprints API and Entities API. Tagged areas include Internal Developer Portal, Service Catalog, Self-Service Actions, Platform Engineering, and Scorecards.


  Port''s developer surface includes authentication, documentation, GitHub presence, and 11 more developer resources.'
plans:
- name: Port Io Plans Pricing
  plan_count: 1
  slug: port-io-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Port Io Rate Limits
  slug: port-io-rate-limits
score:
  band: thin
  composite: 36.1
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 21.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/port-io/refs/heads/main/screenshots/port-io-2026-06-20T191928.png
security:
- kind: authentication
  name: Port Io Authentication
  slug: port-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Port Io Domain Security
  slug: port-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Port Io Vulnerability Disclosure
  slug: port-io-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Port Io Trust Center
  slug: port-io-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: port-io
tags:
- Internal Developer Portal
- Service Catalog
- Self-Service Actions
- Platform Engineering
- Scorecards
- Developer Experience
website: https://www.port.io/
---
