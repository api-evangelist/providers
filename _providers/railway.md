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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Railway public API is a GraphQL API that powers the Railway dashboard, enabling automation of projects, services, deployments, environments, variables, volumes, and team workflows.
  name: Railway Public GraphQL API
  slug: public-api
artifact_total: 23
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/railway-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/railway-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/railwayapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/railwayapp
- group: docs
  title: ''
  type: Documentation
  url: https://docs.railway.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.railway.com/guides/public-api
- group: start
  title: ''
  type: Signup
  url: https://railway.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://railway.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://railway.com/legal/terms
- group: auth
  title: ''
  type: Authentication
  url: https://docs.railway.com/guides/public-api#authentication
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.railway.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.railway.com/rss.xml
created: '2025-02-06'
description: The Railway public API is built with GraphQL and is the same API that powers the Railway dashboard, providing automation for projects, services, deployments, environments, volumes, and CI/CD workflows on the Railway platform.
features:
- 'Free: $5 trial credits, then $1/mo, up to 1 vCPU / 0.5 GB'
- 'Hobby: $5 min/mo + $5 credits, up to 48 vCPU / 48 GB'
- 'Pro: $20 min/mo + $20 credits, up to 1,000 vCPU / 1 TB'
- 'Enterprise: up to 2,400 vCPU / 2.4 TB, SSO/HIPAA'
- 'Per-second billing: memory, CPU, volumes, egress'
- GraphQL API at backboard.railway.com/graphql
- 'API rate limit: 1,000 req/min/token'
- 'Build concurrency: 1 Hobby, 5 Pro'
- GitHub auto-deploy
- Built-in databases (Postgres, MySQL, MongoDB, Redis, Vector)
- Templates and stacks
- Volumes for persistent storage
- Multi-region deployment (Pro+)
- Public + private networking
- Webhooks + GraphQL subscriptions
- OAuth 2.0 + project tokens
finops:
- name: Railway Finops
  service_category: Edge Hosting
  slug: railway-finops
graphqls:
- description: The Railway public API is a GraphQL API that powers the Railway dashboard, enabling automation of projects, services, deployments, environments, variables, volumes, and team workflows.
  name: Railway GraphQL API
  slug: railway-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/railway.png
layout: provider
modified: '2026-05-04'
name: Railway
nav: Providers
network: true
overview: 'Railway publishes 1 API on the [APIs.io](https://apis.io/) network: Public GraphQL API. Tagged areas include Platform-as-a-Service, Deployment, GraphQL, Infrastructure, and DevOps.


  Railway''s developer surface includes documentation, getting-started guide, signup flow, pricing, authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Railway Plans Pricing
  plan_count: 5
  slug: railway-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Railway Rate Limits
  slug: railway-rate-limits
score:
  band: thin
  composite: 28.4
  delta: 0.7
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 39.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 27.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/railway/refs/heads/main/screenshots/railway-2026-06-20T192535.png
security:
- kind: domain-security
  name: Railway Domain Security
  slug: railway-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Railway Trust Center
  slug: railway-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: railway
tags:
- Platform-as-a-Service
- Deployment
- GraphQL
- Infrastructure
- DevOps
---
