---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: A live, OAuth-gated Model Context Protocol endpoint served from Seyond's own corporate host at https://seyond.com/wp-json/mcp/mcp-oauth-server. It is provided by the WordPress MCP adapter running on s
  name: Seyond MCP Server
  slug: seyond-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://seyond.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Seyond-Inc/inno-lidar-sdk/blob/main/docs/HOW_TO_USE_CLIENT_SDK.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Seyond-Inc/inno-lidar-sdk#quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Seyond-Inc
- group: operate
  title: ''
  type: Support
  url: https://seyond.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://seyond.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://seyond.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seyond.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seyond.com/privacy-policy/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Seyond-Inc
- group: other
  title: ''
  type: OpenSource
  url: https://seyond.com/open-source-software/
- group: other
  title: ''
  type: Downloads
  url: https://seyond.com/downloads/
- group: other
  title: ''
  type: Products
  url: https://seyond.com/products/
- group: build
  title: ''
  type: Packages
  url: packages/innovusion-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/innovusion-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/innovusion-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/innovusion-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/innovusion-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/innovusion-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/innovusion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/innovusion-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/innovusion-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/innovusion-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/innovusion-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/innovusion-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/innovusion-domain-security.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/innovusion-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/innovusion-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/innovusion-llms.txt
created: '2026-08-23'
description: 'Seyond (formerly Innovusion) is a Sunnyvale, California LiDAR maker with R&D and business operations in Germany and China. It designs and mass-produces image-grade LiDAR sensors — Falcon K, Robin W, Robin E1X and Hummingbird D1 — plus perception software and SIMPL, the Seyond ITS Management Platform used by cities, DOTs and tolling agencies for intersection and highway traffic detection. Its public developer surface is not a web API: it is a first-party C/C++ client SDK (inno-lidar-sdk) and a ROS/ROS2 driver published on GitHub that speak a proprietary TCP/UDP command-and-pointcloud protocol directly to the sensor. No OpenAPI, GraphQL, gRPC or SOAP contract is published; api.seyond.com is live but answers 404 on every discovery path. The corporate site does serve a live, OAuth-gated MCP server.'
image: https://seyond.com/wp-content/uploads/2024/11/cropped-seyond_favicon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: Seyond MCP Server
  slug: seyond-mcp-server
modified: '2026-08-23'
name: Seyond
nav: Providers
network: true
overview: 'Seyond publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LiDAR, Sensors, Autonomous Driving, and Intelligent Transportation.


  Seyond''s developer surface includes documentation, getting-started guide, support, engineering blog, CLI, changelog, authentication, and 22 more developer resources.'
plans:
- name: Innovusion Plans Pricing
  plan_count: 0
  slug: innovusion-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Innovusion Rate Limits
  slug: innovusion-rate-limits
scopes:
- name: Innovusion Scopes
  scope_count: 0
  slug: innovusion-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 26.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Innovusion Authentication
  slug: innovusion-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Innovusion Domain Security
  slug: innovusion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: innovusion
tags:
- Company
- LiDAR
- Sensors
- Autonomous Driving
- Intelligent Transportation
- Robotics
- Perception
- Smart Cities
- Automotive
- Hardware
website: https://seyond.com/
---
