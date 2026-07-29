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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Microsoft Azure Traffic Manager Agentic Access
  operation_count: 15
  slug: microsoft-azure-traffic-manager-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 9
apis:
- description: 'REST API for managing endpoints within a Traffic Manager profile. Supports adding, updating, and removing Azure, external, and nested endpoints that receive traffic according to the profile''s routing '
  name: Azure Traffic Manager Endpoints REST API
  slug: azure-traffic-manager-endpoints-rest-api
- description: REST API for retrieving Traffic Manager heatmap data, which provides geographic visualization of DNS query volumes and endpoint selection by region. Useful for analyzing traffic distribution and routi
  name: Azure Traffic Manager Heatmap REST API
  slug: azure-traffic-manager-heatmap-rest-api
- description: REST API for managing real user measurements (RUM) keys used by Traffic Manager performance routing. User metrics enable Traffic Manager to make more accurate latency-based routing decisions using tel
  name: Azure Traffic Manager User Metrics REST API
  slug: azure-traffic-manager-user-metrics-rest-api
- description: REST API for retrieving the geographic hierarchy used by Traffic Manager for geographic routing. Returns the supported regions, countries, and subdivisions that can be configured as endpoint geo-mappi
  name: Azure Traffic Manager Geographic Hierarchies REST API
  slug: azure-traffic-manager-geographic-hierarchies-rest-api
- description: Endpoint operations within a profile
  name: Azure Traffic Manager Endpoints API
  slug: microsoft-azure-traffic-manager-endpoints-api
- description: Default geographic hierarchy
  name: Azure Traffic Manager GeographicHierarchies API
  slug: microsoft-azure-traffic-manager-geographichierarchies-api
- description: Geographic heatmap analytics
  name: Azure Traffic Manager HeatMap API
  slug: microsoft-azure-traffic-manager-heatmap-api
- description: Traffic Manager profile operations
  name: Azure Traffic Manager Profiles API
  slug: microsoft-azure-traffic-manager-profiles-api
- description: Real User Measurements (RUM) keys
  name: Azure Traffic Manager UserMetrics API
  slug: microsoft-azure-traffic-manager-usermetrics-api
artifact_total: 23
collections:
- collection_type: postman
  name: Azure Traffic Manager REST Endpoints API
  slug: postman-microsoft-azure-traffic-manager-endpoints-api
- collection_type: postman
  name: Azure Traffic Manager REST Endpoints GeographicHierarchies API
  slug: postman-microsoft-azure-traffic-manager-geographichierarchies-api
- collection_type: postman
  name: Azure Traffic Manager REST Endpoints HeatMap API
  slug: postman-microsoft-azure-traffic-manager-heatmap-api
- collection_type: postman
  name: Azure Traffic Manager REST Endpoints Profiles API
  slug: postman-microsoft-azure-traffic-manager-profiles-api
- collection_type: postman
  name: Azure Traffic Manager REST Endpoints UserMetrics API
  slug: postman-microsoft-azure-traffic-manager-usermetrics-api
- collection_type: open
  name: Azure Traffic Manager REST API
  slug: open-microsoft-azure-traffic-manager
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-traffic-manager/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-traffic-manager-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-traffic-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-traffic-manager-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-traffic-manager-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/traffic-manager
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/traffic-manager/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/traffic-manager/quickstart-create-traffic-manager-profile
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/traffic-manager/
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://azure.microsoft.com/en-us/support/legal/sla/traffic-manager/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/topics/networking/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com
- group: build
  title: ''
  type: SDKs
  url: https://azure.microsoft.com/en-us/downloads/
- group: build
  title: ''
  type: SDK - Python
  url: https://pypi.org/project/azure-mgmt-trafficmanager/
- group: build
  title: ''
  type: SDK - .NET
  url: https://www.nuget.org/packages/Azure.ResourceManager.TrafficManager
- group: build
  title: ''
  type: SDK - JavaScript
  url: https://www.npmjs.com/package/@azure/arm-trafficmanager
- group: build
  title: ''
  type: SDK - Java
  url: https://learn.microsoft.com/en-us/java/api/overview/azure/resourcemanager-trafficmanager-readme
- group: build
  title: ''
  type: CLI Tools
  url: https://learn.microsoft.com/en-us/cli/azure/network/traffic-manager
- group: operate
  title: ''
  type: ChangeLog
  url: https://azure.microsoft.com/en-us/updates/?product=traffic-manager
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: build
  title: ''
  type: GitHub REST API Specs
  url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/trafficmanager
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-traffic-manager
- group: operate
  title: ''
  type: Community
  url: https://learn.microsoft.com/en-us/answers/tags/175/azure-traffic-manager
- group: operate
  title: ''
  type: FAQ
  url: https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-FAQs
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/modules/distribute-load-with-traffic-manager/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Azure/Azure-Resource-Manager-MCP
created: '2026-03-13'
description: Azure Traffic Manager is a DNS-based traffic load balancer that enables you to distribute traffic optimally to services across global Azure regions, while providing high availability and responsiveness. It supports configurable routing methods including priority, weighted, performance, geographic, multivalue, and subnet routing.
finops:
- name: Microsoft Azure Traffic Manager Finops
  service_category: API
  slug: microsoft-azure-traffic-manager-finops
image: https://azure.microsoft.com/svghandler/traffic-manager/
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Azure Traffic Manager
nav: Providers
network: true
overview: 'Azure Traffic Manager publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Endpoints API, GeographicHierarchies API, HeatMap API, and 2 more. Tagged areas include DNS Load Balancing, Failover, Global Routing, Networking, and Traffic Distribution.


  Azure Traffic Manager''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, support, and 26 more developer resources.'
plans:
- name: Microsoft Azure Traffic Manager Plans Pricing
  plan_count: 3
  slug: microsoft-azure-traffic-manager-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 5
  name: Microsoft Azure Traffic Manager Rate Limits
  slug: microsoft-azure-traffic-manager-rate-limits
scopes:
- name: Microsoft Azure Traffic Manager Scopes
  scope_count: 1
  slug: microsoft-azure-traffic-manager-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 60.3
  delta: -0.4
  facets:
    commercial_clarity: 84.2
    contract_quality: 53.4
    developer_ergonomics: 65.2
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 60.7
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
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-traffic-manager/refs/heads/main/screenshots/microsoft-azure-traffic-manager-2026-06-20T185440.png
security:
- kind: authentication
  name: Microsoft Azure Traffic Manager Authentication
  slug: microsoft-azure-traffic-manager-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Traffic Manager Domain Security
  slug: microsoft-azure-traffic-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-traffic-manager
tags:
- DNS Load Balancing
- Failover
- Global Routing
- Networking
- Traffic Distribution
- Traffic Manager
website: https://azure.microsoft.com/en-us/products/traffic-manager
---
