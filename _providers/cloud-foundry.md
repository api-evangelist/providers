---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Cloud Foundry Agentic Access
  operation_count: 29
  slug: cloud-foundry-agentic-access
  summary_line: 29 operations · 16 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: The User Account and Authentication (UAA) server is Cloud Foundry's identity provider and OAuth 2.0 authorization server. It issues tokens consumed by the Cloud Controller, brokers, and operator tooli
  name: Cloud Foundry UAA
  slug: uaa
- description: Loggregator is Cloud Foundry's distributed log and metric pipeline that aggregates application logs, platform component logs, and metrics for streaming consumption by users and external sinks. It expo
  name: Cloud Foundry Loggregator
  slug: loggregator
- description: The Open Service Broker API is the open specification originally developed by Cloud Foundry and now used by Kubernetes and other platforms to provision and manage backing services through a common HTT
  name: Open Service Broker API
  slug: open-service-broker-api
- description: BOSH is Cloud Foundry's release engineering tool for packaging, deploying, and managing distributed software. The BOSH Director API exposes deployment, stemcell, release, task, and VM lifecycle operat
  name: BOSH Director API
  slug: bosh
- description: The Apps API from Cloud Foundry — 4 operation(s) for apps.
  name: Cloud Foundry Apps API
  slug: cloud-foundry-apps-api
- description: The Builds API from Cloud Foundry — 1 operation(s) for builds.
  name: Cloud Foundry Builds API
  slug: cloud-foundry-builds-api
- description: The Cloud Foundry Cloud Controller API V3 API from Cloud Foundry — 2 operation(s) for cloud foundry cloud controller api v3.
  name: Cloud Foundry Cloud Foundry Cloud Controller API V3 API
  slug: cloud-foundry-cloud-foundry-cloud-controller-api-v3-api
- description: The Deployments API from Cloud Foundry — 1 operation(s) for deployments.
  name: Cloud Foundry Deployments API
  slug: cloud-foundry-deployments-api
- description: The Jobs API from Cloud Foundry — 1 operation(s) for jobs.
  name: Cloud Foundry Jobs API
  slug: cloud-foundry-jobs-api
- description: The Organizations API from Cloud Foundry — 2 operation(s) for organizations.
  name: Cloud Foundry Organizations API
  slug: cloud-foundry-organizations-api
- description: The Service Instances API from Cloud Foundry — 2 operation(s) for service instances.
  name: Cloud Foundry Service Instances API
  slug: cloud-foundry-service-instances-api
- description: The Spaces API from Cloud Foundry — 2 operation(s) for spaces.
  name: Cloud Foundry Spaces API
  slug: cloud-foundry-spaces-api
artifact_total: 18
collections:
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3
  slug: open-cloud-foundry
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloud-foundry-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloud-foundry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloud-foundry-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloud-foundry
- group: company
  title: ''
  type: Website
  url: https://www.cloudfoundry.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudfoundry.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cloudfoundry
- group: other
  title: ''
  type: Foundation
  url: https://www.cloudfoundry.org/foundation/
- group: operate
  title: ''
  type: Community
  url: https://www.cloudfoundry.org/community/
- group: operate
  title: ''
  type: Slack
  url: https://slack.cloudfoundry.org/
- group: company
  title: ''
  type: Blog
  url: https://www.cloudfoundry.org/blog/
- group: other
  title: ''
  type: Events
  url: https://www.cloudfoundry.org/events/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudfoundry.org/privacy-policy/
- group: other
  title: ''
  type: Trademark
  url: https://www.cloudfoundry.org/trademark-policy/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloud-foundry-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloud-foundry-rules.yml
created: '2024-01-01'
description: Cloud Foundry is an open-source, multi-cloud Platform as a Service (PaaS) governed by the Cloud Foundry Foundation. It provides a developer-friendly application platform where operators push source code or container images and Cloud Foundry handles staging, routing, scaling, and lifecycle management. The CF API (api.cloudfoundry.org) is the primary control plane and is documented at v3.cloudfoundry.org/version/release-candidate. The ecosystem also includes the User Account and Authentication (UAA) OAuth 2.0 server, the Loggregator log and metric pipeline, the Diego container scheduler, the Open Service Broker API for marketplace services, and the Eirini Kubernetes-based scheduler.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloud-foundry.png
jsonld:
- class_count: 0
  name: Cloud Foundry Context
  property_count: 11
  slug: cloud-foundry-context
layout: provider
modified: '2026-04-23'
name: Cloud Foundry
nav: Providers
network: true
overview: 'Cloud Foundry publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Builds API, Cloud Foundry Cloud Controller API V3 API, and 5 more. Tagged areas include Cloud Foundry Foundation, Containers, Multi-Cloud, Open Source, and PaaS.


  The Cloud Foundry catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloud Foundry''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 12 more developer resources.'
random_paper: 35
rules:
- name: Cloud Foundry API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: cloud-foundry-rules
score:
  band: thin
  composite: 31.7
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 55.8
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 27.1
    operational_transparency: 5.3
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/screenshots/cloud-foundry-2026-06-20T174548.png
security:
- kind: authentication
  name: Cloud Foundry Authentication
  slug: cloud-foundry-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cloud Foundry Domain Security
  slug: cloud-foundry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloud-foundry
tags:
- Cloud Foundry Foundation
- Containers
- Multi-Cloud
- Open Source
- PaaS
- Platform
website: https://www.cloudfoundry.org/
---
