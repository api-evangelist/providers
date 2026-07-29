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
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Hcp Agentic Access
  operation_count: 9
  slug: hcp-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 9
apis:
- description: The HCP Packer API provides programmatic access to manage image buckets, channels, and iterations, enabling automated image pipelines and golden image management across cloud providers.
  name: HCP Packer API
  slug: hcp-packer
- description: The HCP Consul API enables management of HCP Consul clusters, including provisioning, scaling, and federation for service networking and service mesh deployments.
  name: HCP Consul API
  slug: hcp-consul
- description: The HCP Boundary API provides programmatic access to identity-based secure remote access for managing users, hosts, sessions, and access policies in HashiCorp Cloud Platform Boundary.
  name: HCP Boundary API
  slug: hcp-boundary
- description: The HCP Waypoint API enables programmatic management of application templates, add-ons, and deployment workflows for delivering golden patterns to developer teams.
  name: HCP Waypoint API
  slug: hcp-waypoint
- description: HCP Vault Secrets applications
  name: HashiCorp Cloud Platform Apps API
  slug: hcp-apps-api
- description: Gateway pools
  name: HashiCorp Cloud Platform Gateway API
  slug: hcp-gateway-api
- description: External integrations
  name: HashiCorp Cloud Platform Integrations API
  slug: hcp-integrations-api
- description: Static and rotating secrets
  name: HashiCorp Cloud Platform Secrets API
  slug: hcp-secrets-api
- description: Secret synchronization
  name: HashiCorp Cloud Platform Sync API
  slug: hcp-sync-api
artifact_total: 16
collections:
- collection_type: open
  name: HCP Vault Secrets API
  slug: open-hcp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hcp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hcp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hcp-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hashicorp
- group: company
  title: ''
  type: Website
  url: https://cloud.hashicorp.com
- group: other
  title: ''
  type: Developer
  url: https://developer.hashicorp.com/hcp
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hashicorp.com/hcp/docs
- group: docs
  title: ''
  type: API Documentation
  url: https://developer.hashicorp.com/hcp/api-docs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hashicorp.com
- group: company
  title: ''
  type: Blog
  url: https://www.hashicorp.com/en/blog/feed.xml
created: '2024-12-03'
description: HashiCorp Cloud Platform (HCP) is a fully managed platform for HashiCorp products including Vault, Consul, Packer, Boundary, Waypoint, and Terraform. HCP provides a unified set of APIs for managing infrastructure, secrets, service networking, and image pipelines across cloud and on-premises environments.
finops:
- name: Hcp Finops
  service_category: Cloud / Managed Infrastructure Services
  slug: hcp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hcp.png
layout: provider
modified: '2026-05-19'
name: HashiCorp Cloud Platform
nav: Providers
network: true
overview: 'HashiCorp Cloud Platform publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Gateway API, Integrations API, and 2 more. Tagged areas include Cloud, Infrastructure, DevOps, Secrets Management, and Service Networking.


  HashiCorp Cloud Platform''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Hcp Plans Pricing
  plan_count: 6
  slug: hcp-plans-pricing
press:
- date: '2026-05-25'
  title: Charter HCP Announces Direct Investment Focus on ...
  url: https://www.heraldnews.com/press-release/story/111082/charter-hcp-announces-direct-investment-focus-on-financial-services-and-ai-guardrail-startups/
- date: '2026-05-25'
  title: Press
  url: https://www.impiricus.com/press/
- date: '2026-05-25'
  title: Designing Omnichannel Strategies to Drive HCP Behavior ...
  url: https://www.viz.ai/blog/designing-omnichannel-strategies-to-drive-hcp-behavior-change
- date: '2026-05-25'
  title: Charter HCP Announces Direct Investment Focus on Financial ...
  url: https://www.siskiyoudaily.com/press-release/story/25796/charter-hcp-announces-direct-investment-focus-on-financial-services-and-ai-guardrail-startups/
- date: '2026-05-25'
  title: Charter HCP Announces Direct Investment Focus on ...
  url: https://www.jacksonville.com/press-release/story/990353/charter-hcp-announces-direct-investment-focus-on-financial-services-and-ai-guardrail-startups/
random_paper: 72
rate_limits:
- limit_count: 4
  name: Hcp Rate Limits
  slug: hcp-rate-limits
score:
  band: thin
  composite: 41.2
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.4
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hcp/refs/heads/main/screenshots/hcp-2026-06-20T182554.png
security:
- kind: authentication
  name: Hcp Authentication
  slug: hcp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hcp Domain Security
  slug: hcp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hcp
tags:
- Cloud
- Infrastructure
- DevOps
- Secrets Management
- Service Networking
- Fortune 1000
website: https://cloud.hashicorp.com
---
