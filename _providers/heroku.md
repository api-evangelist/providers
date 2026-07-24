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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Heroku Agentic Access
  operation_count: 44
  slug: heroku-agentic-access
  summary_line: 44 operations · 23 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: Account management
  name: Heroku Account API
  slug: heroku-account-api
- description: Add-on service management
  name: Heroku Add-ons API
  slug: heroku-add-ons-api
- description: Application management
  name: Heroku Apps API
  slug: heroku-apps-api
- description: Build management
  name: Heroku Builds API
  slug: heroku-builds-api
- description: App collaborator management
  name: Heroku Collaborators API
  slug: heroku-collaborators-api
- description: Environment configuration variables
  name: Heroku Config Vars API
  slug: heroku-config-vars-api
- description: Custom domain management
  name: Heroku Domains API
  slug: heroku-domains-api
- description: Process (dyno) management
  name: Heroku Dynos API
  slug: heroku-dynos-api
- description: Process type scaling
  name: Heroku Formation API
  slug: heroku-formation-api
- description: Application logging
  name: Heroku Log Sessions API
  slug: heroku-log-sessions-api
- description: Deployment pipeline management
  name: Heroku Pipelines API
  slug: heroku-pipelines-api
- description: Available regions
  name: Heroku Regions API
  slug: heroku-regions-api
- description: Release management
  name: Heroku Releases API
  slug: heroku-releases-api
- description: Available stacks
  name: Heroku Stacks API
  slug: heroku-stacks-api
artifact_total: 52
collections:
- collection_type: open
  name: Heroku App Webhooks
  slug: open-heroku-app-webhooks-asyncapi
- collection_type: open
  name: Heroku Platform API
  slug: open-heroku-platform-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/heroku-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heroku-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/heroku-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heroku
- group: start
  title: ''
  type: Portal
  url: https://devcenter.heroku.com/
- group: company
  title: ''
  type: Website
  url: https://www.heroku.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://devcenter.heroku.com/start
- group: docs
  title: ''
  type: Documentation
  url: https://devcenter.heroku.com/
- group: start
  title: ''
  type: Signup
  url: https://signup.heroku.com/
- group: start
  title: ''
  type: Login
  url: https://id.heroku.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.heroku.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.heroku.com/
- group: operate
  title: ''
  type: Support
  url: https://help.heroku.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.heroku.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heroku
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.heroku.com/policy/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.heroku.com/policy/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://heroku.com/llms.txt
created: '2025-02-08'
description: Heroku is a cloud platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. The Heroku Platform API enables programmatic access to Heroku's features for app deployment, scaling, and management.
features:
- 'Eco Dynos: $5/mo for 1,000 dyno-hours pool (sleeps when idle)'
- 'Basic Dyno: $7/mo, never sleeps, 512 MB RAM'
- 'Standard-1X: $25/mo, 512 MB RAM, horizontal scaling'
- 'Standard-2X: $50/mo, 1 GB RAM'
- 'Performance-M/L/XL/2XL: $250-$1,500/mo, dedicated infra'
- 'Heroku Postgres Essential: $5-$9/mo (hobby)'
- 'Heroku Postgres Standard: $50-$200/mo (production)'
- 'Heroku Postgres Premium: $200-$350/mo (HA)'
- 'Heroku Key-Value Store (Redis-compatible): $3-$120/mo'
- 'Platform API: 4,500 req/hr/token rate limit'
- Buildpacks for languages (Node, Ruby, Python, Java, Go, etc.)
- Heroku Connect for Salesforce sync (separate)
- Heroku Add-ons marketplace
- Pipelines for staging→production promotion
- Review apps for PR previews
- Salesforce-owned with Salesforce integration
finops:
- name: Heroku Finops
  service_category: Platform-as-a-Service
  slug: heroku-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Heroku Platform API. Heroku exposes its platform capabilities through a REST API at `https://api.heroku.com`, documented at [https://devcent
  name: Heroku GraphQL Schema
  slug: heroku-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heroku.png
json_schemas:
- name: Account
  property_count: 16
  slug: heroku-account
- name: Addon
  property_count: 12
  slug: heroku-addon
- name: App
  property_count: 20
  slug: heroku-app
- name: Build
  property_count: 11
  slug: heroku-build
- name: Collaborator
  property_count: 7
  slug: heroku-collaborator
- name: Domain
  property_count: 11
  slug: heroku-domain
- name: Dyno
  property_count: 11
  slug: heroku-dyno
- name: Formation
  property_count: 8
  slug: heroku-formation
- name: Pipeline
  property_count: 5
  slug: heroku-pipeline
- name: PipelineCoupling
  property_count: 6
  slug: heroku-pipelinecoupling
- name: Release
  property_count: 11
  slug: heroku-release
json_structures:
- name: Heroku Structure
  property_count: 0
  slug: heroku-structure
layout: provider
modified: '2026-05-30'
name: Heroku
nav: Providers
network: true
overview: 'Heroku publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Account API, Add-ons API, Apps API, and 11 more. Tagged areas include Application Deployment, Cloud Platform, DevOps, and PaaS.


  The Heroku catalog on APIs.io includes 1 Spectral governance ruleset.


  Heroku''s developer surface includes authentication, developer portal, getting-started guide, documentation, signup flow, engineering blog, support, and 11 more developer resources.'
plans:
- name: Heroku Plans Pricing
  plan_count: 8
  slug: heroku-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 3
  name: Heroku Rate Limits
  slug: heroku-rate-limits
rules:
- name: Heroku API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: heroku-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.2
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 52.1
    developer_ergonomics: 45.7
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 60.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heroku/refs/heads/main/screenshots/heroku-2026-06-20T182649.png
security:
- kind: authentication
  name: Heroku Authentication
  slug: heroku-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Heroku Domain Security
  slug: heroku-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: heroku
tags:
- Application Deployment
- Cloud Platform
- DevOps
- PaaS
website: https://www.heroku.com/
---
