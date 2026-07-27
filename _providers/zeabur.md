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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 6
apis:
- description: Create, list, clone, export, and delete projects, and manage the environments (production, staging, etc.) within each project, via GraphQL queries and mutations.
  name: Zeabur Projects API
  slug: zeabur-projects-api
- description: Create services from git repositories, uploaded zips, Dockerfiles, or prebuilt marketplace codes; restart, suspend, redeploy, update image tags, read metrics/ports, and run commands inside running ser
  name: Zeabur Services API
  slug: zeabur-services-api
- description: List and inspect deployments for a service and environment, fetch the latest deployment, read build and runtime logs, and stream logs in real time via graphql-ws subscriptions.
  name: Zeabur Deployments API
  slug: zeabur-deployments-api
- description: List and update environment variables scoped to a service within an environment, for injecting configuration and secrets into deployed workloads.
  name: Zeabur Environment Variables API
  slug: zeabur-environment-variables-api
- description: Bind generated (*.zeabur.app) or custom domains to a service, list bound domains, check domain availability, and remove domain bindings.
  name: Zeabur Domains API
  slug: zeabur-domains-api
- description: List and retrieve deploy templates, deploy a template spec into a project, create and update custom templates from spec YAML, and enumerate available deploy regions (including generic bring-your-own-s
  name: Zeabur Templates & Regions API
  slug: zeabur-templates-api
artifact_total: 13
collections:
- collection_type: open
  name: Zeabur GraphQL API
  slug: open-zeabur
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/zeabur-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zeabur-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zeabur
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zeabur
- group: company
  title: ''
  type: Website
  url: https://zeabur.com/
- group: docs
  title: ''
  type: Documentation
  url: https://zeabur.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/zeabur-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zeabur-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zeabur-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://zeabur.com/blogs
created: '2026-07-01'
description: Zeabur is a deploy-anything cloud platform (PaaS) that ships applications, databases, and services with one click. Its public API is GraphQL-first, exposing projects, environments, services, deployments, environment variables, domains, regions, and templates through a single endpoint at https://api.zeabur.com/graphql.
finops:
- name: Zeabur Finops
  service_category: Compute
  slug: zeabur-finops
graphqls:
- description: 'Zeabur is a deploy-anything cloud platform (PaaS) that deploys applications, databases, and services with one click. Its public API is **GraphQL-first**: a single endpoint exposes the entire platform '
  name: Zeabur GraphQL API
  slug: zeabur-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zeabur.png
layout: provider
modified: '2026-07-01'
name: Zeabur
nav: Providers
network: true
overview: 'Zeabur publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include PaaS, Deployment, Cloud, DevOps, and GraphQL.


  Zeabur''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Zeabur Plans Pricing
  plan_count: 3
  slug: zeabur-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 3
  name: Zeabur Rate Limits
  slug: zeabur-rate-limits
score:
  band: emerging
  composite: 26.4
  delta: 3.2
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 23.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Zeabur Domain Security
  slug: zeabur-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Zeabur Trust Center
  slug: zeabur-trust-center
  summary_line: SOC 2
slug: zeabur
tags:
- PaaS
- Deployment
- Cloud
- DevOps
- GraphQL
website: https://zeabur.com/
---
