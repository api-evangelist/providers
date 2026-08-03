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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: RESTful API for AppNeta Performance Manager, covering monitoring policies and policy groups, web paths, web applications (locations, targets, user flows), monitoring points, alarm connectors (v4), and
  name: AppNeta Performance Manager API
  slug: appneta-performance-manager-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.broadcom.com/products/software/network-management/appneta
- group: start
  title: ''
  type: DeveloperPortal
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta/GA.html
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta/GA/integrate/api.html
- group: docs
  title: ''
  type: APIReference
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta/GA/integrate/api/api-v4.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/appneta-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://support.broadcom.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appneta
- group: build
  title: ''
  type: Packages
  url: packages/appneta-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appneta-domain-security.yml
created: '2026-07-17'
description: AppNeta is a network performance monitoring (NPM) platform for the distributed, cloud-connected enterprise, now delivered as a Broadcom product under its IT Operations Management / Network Management portfolio. AppNeta Performance Manager continuously measures network paths, delivery quality, usage, and end-user application experience across SaaS, cloud, and internet paths using a combination of active (synthetic) and passive monitoring from distributed monitoring points. It exposes a RESTful API (v3 for AppNeta Classic and v4 for AppNeta with Intelligent Alarms) for programmatic access to monitoring policies, web paths, web applications, alarm connectors, and event/observer integrations, authenticated with API access tokens. As of February 2026 the API interface and documentation were upgraded from Swagger to OpenAPI 3.0. AppNeta was originally an independent, Battery Ventures-backed company before joining Broadcom.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appneta.png
layout: provider
modified: '2026-07-17'
name: AppNeta
nav: Providers
network: true
overview: 'AppNeta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Network Monitoring, Network Performance Monitoring, Observability, and Application Performance Monitoring.


  AppNeta''s developer surface includes documentation, API reference, authentication, support, and 5 more developer resources.'
random_paper: 80
score:
  band: emerging
  composite: 14.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/screenshots/appneta-2026-07-25T200818.png
security:
- kind: authentication
  name: Appneta Authentication
  slug: appneta-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Appneta Domain Security
  slug: appneta-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: appneta
tags:
- Company
- Network Monitoring
- Network Performance Monitoring
- Observability
- Application Performance Monitoring
- Synthetic Monitoring
- Monitoring
- Broadcom
website: https://www.broadcom.com/products/software/network-management/appneta
---
