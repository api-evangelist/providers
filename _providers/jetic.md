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
- acting_count: 10
  human_in_the_loop: 0
  name: Jetic Agentic Access
  operation_count: 22
  slug: jetic-agentic-access
  summary_line: 22 operations · 10 acting
api_count: 5
apis:
- description: Manage OpenAPI specifications via the API Builder
  name: Jetic API Specifications API
  slug: jetic-api-specifications-api
- description: Manage connected Kubernetes clusters
  name: Jetic Clusters API
  slug: jetic-clusters-api
- description: Deploy and manage integration deployments on Kubernetes
  name: Jetic Deployments API
  slug: jetic-deployments-api
- description: Manage integration projects and routes
  name: Jetic Integrations API
  slug: jetic-integrations-api
- description: Monitor integration status, logs, and metrics
  name: Jetic Monitoring API
  slug: jetic-monitoring-api
artifact_total: 52
collections:
- collection_type: open
  name: Jetic Platform API
  slug: open-jetic-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jetic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jetic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jetic-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jetic-io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jetic.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jetic.io/docs/installationguide/quickstart/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jetic.io/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jetic.io/legal
- group: company
  title: ''
  type: Blog
  url: https://jetic.io/blog
- group: start
  title: ''
  type: Login
  url: https://app.us1.jetic.io/login
- group: start
  title: ''
  type: Signup
  url: https://app.us1.jetic.io/registration
- group: company
  title: ''
  type: Website
  url: https://jetic.io/
created: '2025-06-10T00:00:00.000Z'
description: Jetic is the first and only cloud-native API & Integration Platform based on Apache Camel. An iPaaS solution for avoiding costly vendor lock-ins and regaining command of your development - without any drawbacks.
features:
- name: Monitor Cluster Status
- name: Integrated with Git
- name: Host on any Kubernetes
- name: Build Integrations
- name: Deploy Integrations
- name: Manage INtegrations
- name: Monitor Cluster Status
- name: Integrated with Git
- name: Host on any Kubernetes
- name: Native Apache Camel Integration
- name: Automatic structure detection
- name: Visual Mapping
- name: Multi-source document support
- name: Professional Services
- name: Data-as-a-service
- name: Generate OpenAPI
- name: Transform Data
- name: Data Formats
- name: Integration Monitoring
- name: Integration Releases
- name: Data Visualization
- name: Kubernetes Deployment
- name: Code Generation
- name: Cluster monitoring
- name: Message Broker
- name: Shared Cluster
finops:
- name: Jetic Finops
  service_category: API
  slug: jetic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jetic.png
json_schemas:
- name: Jetic API Specification
  property_count: 9
  slug: api-specification
- name: Jetic Cluster
  property_count: 8
  slug: cluster
- name: Jetic Deployment
  property_count: 10
  slug: deployment
- name: Jetic Integration
  property_count: 8
  slug: integration
- name: Jetic Route
  property_count: 5
  slug: route
jsonld:
- class_count: 0
  name: Jetic Context
  property_count: 5
  slug: jetic-context
layout: provider
modified: '2026-05-19'
name: Jetic
nav: Providers
network: true
overview: 'Jetic publishes 5 APIs on the [APIs.io](https://apis.io/) network, including API Specifications API, Clusters API, Deployments API, and 2 more. Tagged areas include Apache Camel, Integrations, iPaaS, and Pro-Code API Composition.


  The Jetic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Jetic''s developer surface includes authentication, documentation, getting-started guide, engineering blog, signup flow, and 7 more developer resources.'
plans:
- name: Jetic Plans Pricing
  plan_count: 3
  slug: jetic-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Jetic Rate Limits
  slug: jetic-rate-limits
rules:
- name: Jetic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: jetic-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.5
  delta: -3.5
  facets:
    commercial_clarity: 63.2
    contract_quality: 74.6
    developer_ergonomics: 32.6
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 58.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/jetic/refs/heads/main/screenshots/jetic-2026-06-20T183725.png
security:
- kind: authentication
  name: Jetic Authentication
  slug: jetic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jetic Domain Security
  slug: jetic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jetic
tags:
- Apache Camel
- Integrations
- iPaaS
- Pro-Code API Composition
use_cases:
- name: Real-time Integration
- name: API Build & Design
- name: Serverless iPaaS
- name: Data Mapping
- name: Streaming and Events
- name: Data Lakes
- name: Data Governance
website: https://jetic.io/
---
