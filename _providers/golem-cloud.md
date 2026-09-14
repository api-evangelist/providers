---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Golem Cloud Agentic Access
  operation_count: 33
  slug: golem-cloud-agentic-access
  summary_line: 33 operations · 19 acting
api_count: 1
apis:
- baseURL: https://release.api.golem.cloud
  baseurl_source: declared
  description: Custom HTTP API definitions and deployments (Worker Gateway).
  name: Golem ApiDefinition API
  slug: golem-cloud-apidefinition-api
- baseURL: https://release.api.golem.cloud
  baseurl_source: declared
  description: WebAssembly component registry operations.
  name: Golem Component API
  slug: golem-cloud-component-api
- baseURL: https://release.api.golem.cloud
  baseurl_source: declared
  description: Plugin registration and grants.
  name: Golem Plugin API
  slug: golem-cloud-plugin-api
- baseURL: https://release.api.golem.cloud
  baseurl_source: declared
  description: Durable worker lifecycle and invocation operations.
  name: Golem Worker API
  slug: golem-cloud-worker-api
artifact_total: 18
asyncapis:
- description: AsyncAPI description of Golem's worker `connect` WebSocket endpoint. The REST route GET /v1/components/{component_id}/workers/{agent_name}/connect upgrades the connection to a WebSocket (wss://) and s
  name: Golem Worker Connect (WebSocket) API
  slug: golem-cloud-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Golem Cloud ApiDefinition API
  slug: open-golem-cloud-apidefinition-api
- collection_type: open
  name: Golem Cloud ApiDefinition Component API
  slug: open-golem-cloud-component-api
- collection_type: open
  name: Golem Cloud ApiDefinition Plugin API
  slug: open-golem-cloud-plugin-api
- collection_type: open
  name: Golem Cloud ApiDefinition Worker API
  slug: open-golem-cloud-worker-api
- collection_type: open
  name: Golem Cloud API
  slug: open-golem-cloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/golem-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/golem-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/golem-cloud-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/golemcloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/golem-cloud
- group: company
  title: ''
  type: Website
  url: https://www.golem.cloud
- group: docs
  title: ''
  type: Documentation
  url: https://learn.golem.cloud
- group: commercial
  title: ''
  type: Plans
  url: plans/golem-cloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/golem-cloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/golem-cloud-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.golem.cloud/rss.xml
created: '2026-06-20'
description: Golem is an open-source durable computing platform for building agents and distributed applications that never lose state. You deploy WebAssembly components and invoke durable serverless workers through a REST API; the runtime transparently persists every worker's execution so it survives crashes, restarts, and redeploys. Golem ships as open source you self-host and as the managed Golem Cloud hosted service.
finops:
- name: Golem Cloud Finops
  service_category: Compute
  slug: golem-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/golem-cloud.png
layout: provider
modified: '2026-06-20'
name: Golem
nav: Providers
network: true
overview: 'Golem publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ApiDefinition API, Component API, Plugin API, and 1 more. Tagged areas include Durable Computing, Serverless, WebAssembly, Workers, and Agents.


  The Golem catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Golem''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Golem Cloud Plans Pricing
  plan_count: 4
  slug: golem-cloud-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Golem Cloud Rate Limits
  slug: golem-cloud-rate-limits
rules:
- effective_rule_count: 29
  extends:
  - spectral:asyncapi
  name: Golem API Rules
  rule_count: 2
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 2
  slug: golem-cloud-asyncapi-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/golem-cloud/refs/heads/main/screenshots/golem-cloud-2026-06-20T181950.png
security:
- kind: authentication
  name: Golem Cloud Authentication
  slug: golem-cloud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Golem Cloud Domain Security
  slug: golem-cloud-domain-security
  summary_line: TLSv1.3 · HSTS
slug: golem-cloud
tags:
- Durable Computing
- Serverless
- WebAssembly
- Workers
- Agents
website: https://www.golem.cloud
---
