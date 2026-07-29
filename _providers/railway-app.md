---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
api_count: 13
apis:
- description: GraphQL operations for creating, reading, updating, and deleting Railway projects - the top-level container for services and environments. Queries include project and projects; mutations include proje
  name: Railway Projects API
  slug: railway-app-projects-api
- description: GraphQL operations for managing services and their per-environment service instances. Queries include service and serviceInstance; mutations include serviceCreate, serviceUpdate, serviceInstanceUpdate
  name: Railway Services API
  slug: railway-app-services-api
- description: GraphQL operations for triggering and managing deployments. Queries include deployment and deployments; mutations include serviceInstanceDeployV2, serviceInstanceRedeploy, deploymentRedeploy, deployme
  name: Railway Deployments API
  slug: railway-app-deployments-api
- description: GraphQL operations for isolated project environments (for example production and staging). Queries include environment and environments; mutations include environmentCreate, environmentDelete, and env
  name: Railway Environments API
  slug: railway-app-environments-api
- description: GraphQL operations for service and environment configuration variables. Queries include variables; mutations include variableUpsert, variableDelete, and variableCollectionUpsert for bulk updates.
  name: Railway Variables API
  slug: railway-app-variables-api
- description: GraphQL operations for persistent volumes attached to services. Queries include volume; mutations include volumeCreate, volumeUpdate, volumeDelete, and volumeInstanceUpdate for per-environment mounts.
  name: Railway Volumes API
  slug: railway-app-volumes-api
- description: GraphQL operations for legacy plugins (managed database add-ons such as Postgres, MySQL, Redis, and MongoDB). Queries include plugin; mutations include pluginCreate, pluginUpdate, pluginRestart, and p
  name: Railway Plugins API
  slug: railway-app-plugins-api
- description: GraphQL operations for attaching custom and Railway-provided domains to a service. Queries include customDomain and domains; mutations include customDomainCreate, customDomainDelete, and serviceDomain
  name: Railway Custom Domains API
  slug: railway-app-custom-domains-api
- description: GraphQL operations for exposing a service over raw TCP. Queries include tcpProxies; mutations include tcpProxyCreate and tcpProxyDelete.
  name: Railway TCP Proxies API
  slug: railway-app-tcp-proxies-api
- description: GraphQL operations for reading resource consumption and cost. Queries include usage, estimatedUsage, and metrics for per-service vCPU, memory, network egress, and disk utilization.
  name: Railway Usage and Metrics API
  slug: railway-app-usage-metrics-api
- description: GraphQL operations for the authenticated account, its workspaces, teams, and members. Queries include me, workspace, and workspaces; mutations include workspaceUpdate and teamMemberInvite.
  name: Railway Teams and Workspaces API
  slug: railway-app-teams-api
- description: GraphQL operations for project webhooks that notify external URLs of deployment status changes. Queries include projectWebhooks; mutations include webhookCreate, webhookUpdate, and webhookDelete.
  name: Railway Webhooks API
  slug: railway-app-webhooks-api
- description: GraphQL log surface for builds, deployments, environments, and HTTP traffic. Available both as point-in-time queries (buildLogs, deploymentLogs, environmentLogs, httpLogs) and as real-time GraphQL sub
  name: Railway Logs API
  slug: railway-app-logs-api
artifact_total: 22
asyncapis:
- description: AsyncAPI 2.6 description of Railway's **real-time log streaming** surface. Unlike many providers in this catalog, Railway **does** publish a documented public WebSocket transport. Railway's GraphQL Pu
  name: Railway GraphQL Subscriptions (WebSocket)
  slug: railway-app-asyncapi
collections:
- collection_type: open
  name: Railway GraphQL Public API
  slug: open-railway-app
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/railway-app-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/railway-app-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/railwayapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/railwayapp
- group: company
  title: ''
  type: Website
  url: https://railway.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.railway.com
- group: commercial
  title: ''
  type: Plans
  url: plans/railway-app-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/railway-app-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/railway-app-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.railway.com/rss.xml
created: '2026-07-02'
description: Railway is a cloud application deployment platform (PaaS) that builds, deploys, and scales services, databases, and cron jobs from a Git repository or Docker image. Its programmatic surface is a GraphQL-first Public API served at https://backboard.railway.com/graphql/v2 - the same API that powers the Railway dashboard. There is no REST API; all queries and mutations are issued as GraphQL POST requests, and real-time build, deployment, and environment log streams are delivered as GraphQL subscriptions over a WebSocket endpoint at wss://backboard.railway.com/graphql/v2.
finops:
- name: Railway App Finops
  service_category: Compute
  slug: railway-app-finops
graphqls:
- description: Railway is a cloud application deployment platform (PaaS). Its entire programmatic surface is a **GraphQL API** - there is no REST API. The Public API is the same API that powers the Railway dashboard
  name: Railway GraphQL Public API
  slug: railway-app-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/railway-app.png
layout: provider
modified: '2026-07-02'
name: Railway
nav: Providers
network: true
overview: 'Railway publishes 1 API on the [APIs.io](https://apis.io/) network: Logs API. Tagged areas include Deployment, PaaS, Cloud, Infrastructure, and GraphQL.


  The Railway catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Railway''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Railway App Plans Pricing
  plan_count: 5
  slug: railway-app-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 6
  name: Railway App Rate Limits
  slug: railway-app-rate-limits
rules:
- name: Railway API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: railway-app-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.6
  delta: 2.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 59.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 41.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Railway App Domain Security
  slug: railway-app-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Railway App Trust Center
  slug: railway-app-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: railway-app
tags:
- Deployment
- PaaS
- Cloud
- Infrastructure
- GraphQL
- DevOps
website: https://railway.com/
---
