---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Citrix Netscaler Agentic Access
  operation_count: 28
  slug: citrix-netscaler-agentic-access
  summary_line: 28 operations · 16 acting
api_count: 9
apis:
- description: The NetScaler Application Delivery Management (ADM) NITRO API provides programmatic access to manage, monitor, and orchestrate multiple NetScaler instances from a centralized platform, covering analyt
  name: NetScaler ADM NITRO API
  slug: netscaler-adm-nitro-api
- description: The NetScaler SDX NITRO API provides programmatic access to configure and manage NetScaler SDX appliances via REST interfaces, enabling provisioning and management of multiple virtual NetScaler instan
  name: NetScaler SDX NITRO API
  slug: netscaler-sdx-nitro-api
- description: NetScaler Next-Gen API is a modern declarative RESTful API built on the OpenAPI 3.0 specification that allows developers to programmatically configure NetScaler with an intuitive application-centric i
  name: NetScaler Next-Gen API
  slug: netscaler-next-gen-api
- description: Session-based authentication for the NITRO API. Obtain an authentication token via login, then include it as a cookie in subsequent requests.
  name: Citrix NetScaler Authentication API
  slug: citrix-netscaler-authentication-api
- description: Content switching virtual servers direct client requests to different load balancing virtual servers based on content switching policies that evaluate HTTP request attributes.
  name: Citrix NetScaler CS Virtual Server API
  slug: citrix-netscaler-cs-virtual-server-api
- description: Load balancing virtual servers accept incoming traffic and distribute it across backend services using configurable load balancing methods such as round robin, least connections, and more.
  name: Citrix NetScaler LB Virtual Server API
  slug: citrix-netscaler-lb-virtual-server-api
- description: NetScaler appliance configuration including IP address, network settings, HTTP ports, and system-level parameters. Supports save, clear, and diff operations.
  name: Citrix NetScaler NS Config API
  slug: citrix-netscaler-ns-config-api
- description: Real-time performance and health statistics for configured resources including virtual servers, services, and system metrics.
  name: Citrix NetScaler Statistics API
  slug: citrix-netscaler-statistics-api
- description: System-level resources for managing the NetScaler appliance including system information, files, users, groups, and global settings.
  name: Citrix NetScaler System API
  slug: citrix-netscaler-system-api
artifact_total: 70
collections:
- collection_type: postman
  name: Citrix NetScaler NITRO REST Authentication API
  slug: postman-citrix-netscaler-authentication-api
- collection_type: postman
  name: Citrix NetScaler NITRO REST Authentication CS Virtual Server API
  slug: postman-citrix-netscaler-cs-virtual-server-api
- collection_type: postman
  name: Citrix NetScaler NITRO REST Authentication LB Virtual Server API
  slug: postman-citrix-netscaler-lb-virtual-server-api
- collection_type: postman
  name: Citrix NetScaler NITRO REST Authentication NS Config API
  slug: postman-citrix-netscaler-ns-config-api
- collection_type: postman
  name: Citrix NetScaler NITRO REST Authentication Statistics API
  slug: postman-citrix-netscaler-statistics-api
- collection_type: postman
  name: Citrix NetScaler NITRO REST Authentication System API
  slug: postman-citrix-netscaler-system-api
- collection_type: open
  name: Citrix NetScaler NITRO REST API
  slug: open-citrix-netscaler-nitro
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/citrix-netscaler/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/citrix-netscaler-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citrix-netscaler-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/citrix-netscaler-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.netscaler.com/platform/apis
- group: docs
  title: ''
  type: Documentation
  url: https://developer-docs.netscaler.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.netscaler.com/
- group: build
  title: ''
  type: CLI
  url: https://developer-docs.netscaler.com/en-us/adc-command-reference-int/current-release.html
- group: company
  title: ''
  type: Blog
  url: https://www.netscaler.com/blog/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/netscaler
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/citrix
- group: operate
  title: ''
  type: Support
  url: https://www.netscaler.com/resources/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.com/
- group: start
  title: ''
  type: Signup
  url: https://onboarding.cloud.com/
- group: start
  title: ''
  type: Login
  url: https://citrix.cloud.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloud.com/legal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloud.com/legal
- group: other
  title: ''
  type: X
  url: https://x.com/NetScaler
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netscaler
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.netscaler.com/en-us/citrix-adc/current-release/citrix-adc-release-notes.html
created: '2024'
description: Citrix NetScaler is an application delivery controller (ADC) that provides load balancing, traffic management, application security, and application acceleration capabilities for web applications and services.
examples:
- key_count: 6
  name: Citrix Netscaler Nitro Cs Vserver Cs Policy Binding Example
  slug: citrix-netscaler-nitro-cs-vserver-cs-policy-binding-example
- key_count: 46
  name: Citrix Netscaler Nitro Cs Vserver Example
  slug: citrix-netscaler-nitro-cs-vserver-example
- key_count: 19
  name: Citrix Netscaler Nitro Cs Vserver Stats Example
  slug: citrix-netscaler-nitro-cs-vserver-stats-example
- key_count: 66
  name: Citrix Netscaler Nitro Lb Vserver Example
  slug: citrix-netscaler-nitro-lb-vserver-example
- key_count: 8
  name: Citrix Netscaler Nitro Lb Vserver Service Binding Example
  slug: citrix-netscaler-nitro-lb-vserver-service-binding-example
- key_count: 45
  name: Citrix Netscaler Nitro Lb Vserver Stats Example
  slug: citrix-netscaler-nitro-lb-vserver-stats-example
- key_count: 3
  name: Citrix Netscaler Nitro Nitro Error Response Example
  slug: citrix-netscaler-nitro-nitro-error-response-example
- key_count: 3
  name: Citrix Netscaler Nitro Nitro Response Example
  slug: citrix-netscaler-nitro-nitro-response-example
- key_count: 30
  name: Citrix Netscaler Nitro Ns Config Example
  slug: citrix-netscaler-nitro-ns-config-example
- key_count: 8
  name: Citrix Netscaler Nitro System File Example
  slug: citrix-netscaler-nitro-system-file-example
features:
- Load balancing across multiple servers and protocols
- Content switching for routing traffic based on request attributes
- SSL offloading and acceleration
- Web Application Firewall for application security
- Global Server Load Balancing (GSLB)
- Application acceleration and optimization
- API gateway capabilities
- Health monitoring and auto-scaling
finops:
- name: Citrix Netscaler Finops
  service_category: Application Delivery
  slug: citrix-netscaler-finops
image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.svg
json_schemas:
- name: CsVserverCsPolicyBinding
  property_count: 6
  slug: citrix-netscaler-nitro-cs-vserver-cs-policy-binding
- name: CsVserver
  property_count: 46
  slug: citrix-netscaler-nitro-cs-vserver
- name: CsVserverStats
  property_count: 19
  slug: citrix-netscaler-nitro-cs-vserver-stats
- name: LbVserver
  property_count: 66
  slug: citrix-netscaler-nitro-lb-vserver
- name: LbVserverServiceBinding
  property_count: 8
  slug: citrix-netscaler-nitro-lb-vserver-service-binding
- name: LbVserverStats
  property_count: 45
  slug: citrix-netscaler-nitro-lb-vserver-stats
- name: NitroErrorResponse
  property_count: 3
  slug: citrix-netscaler-nitro-nitro-error-response
- name: NitroResponse
  property_count: 3
  slug: citrix-netscaler-nitro-nitro-response
- name: NsConfig
  property_count: 30
  slug: citrix-netscaler-nitro-ns-config
- name: SystemFile
  property_count: 8
  slug: citrix-netscaler-nitro-system-file
- name: Citrix NetScaler Virtual Server
  property_count: 53
  slug: citrix-netscaler-vserver
json_structures:
- name: Citrix Netscaler Nitro Cs Vserver Cs Policy Binding Structure
  property_count: 6
  slug: citrix-netscaler-nitro-cs-vserver-cs-policy-binding-structure
- name: Citrix Netscaler Nitro Cs Vserver Stats Structure
  property_count: 19
  slug: citrix-netscaler-nitro-cs-vserver-stats-structure
- name: Citrix Netscaler Nitro Cs Vserver Structure
  property_count: 46
  slug: citrix-netscaler-nitro-cs-vserver-structure
- name: Citrix Netscaler Nitro Lb Vserver Service Binding Structure
  property_count: 8
  slug: citrix-netscaler-nitro-lb-vserver-service-binding-structure
- name: Citrix Netscaler Nitro Lb Vserver Stats Structure
  property_count: 45
  slug: citrix-netscaler-nitro-lb-vserver-stats-structure
- name: Citrix Netscaler Nitro Lb Vserver Structure
  property_count: 66
  slug: citrix-netscaler-nitro-lb-vserver-structure
- name: Citrix Netscaler Nitro Nitro Error Response Structure
  property_count: 3
  slug: citrix-netscaler-nitro-nitro-error-response-structure
- name: Citrix Netscaler Nitro Nitro Response Structure
  property_count: 3
  slug: citrix-netscaler-nitro-nitro-response-structure
- name: Citrix Netscaler Nitro Ns Config Structure
  property_count: 30
  slug: citrix-netscaler-nitro-ns-config-structure
- name: Citrix Netscaler Nitro System File Structure
  property_count: 8
  slug: citrix-netscaler-nitro-system-file-structure
jsonld:
- class_count: 0
  name: Citrix Netscaler Context
  property_count: 7
  slug: citrix-netscaler-context
- class_count: 0
  name: Citrix Netscaler Nitro Context
  property_count: 0
  slug: citrix-netscaler-nitro-context
layout: provider
modified: '2026-05-19'
name: Citrix NetScaler
nav: Providers
network: true
overview: 'Citrix NetScaler publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, CS Virtual Server API, LB Virtual Server API, and 3 more. Tagged areas include API Gateway, Application Delivery Controller, Application Security, Load Balancing, and SSL Offloading.


  The Citrix NetScaler catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Citrix NetScaler''s developer surface includes authentication, developer portal, documentation, CLI, engineering blog, support, signup flow, and 13 more developer resources.'
plans:
- name: Citrix Netscaler Plans Pricing
  plan_count: 4
  slug: citrix-netscaler-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Citrix Netscaler Rate Limits
  slug: citrix-netscaler-rate-limits
rules:
- name: Citrix NetScaler API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: citrix-netscaler-jsonschema-spectral-rules
- name: Citrix NetScaler API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: citrix-netscaler-spectral-rules
score:
  band: strong
  composite: 65.2
  delta: -3.6
  facets:
    commercial_clarity: 73.7
    contract_quality: 69.2
    developer_ergonomics: 45.7
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 68.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/citrix-netscaler/refs/heads/main/screenshots/citrix-netscaler-2026-06-20T174413.png
security:
- kind: authentication
  name: Citrix Netscaler Authentication
  slug: citrix-netscaler-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Citrix Netscaler Domain Security
  slug: citrix-netscaler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citrix-netscaler
tags:
- API Gateway
- Application Delivery Controller
- Application Security
- Load Balancing
- SSL Offloading
- Traffic Management
- Web Application Firewall
use_cases:
- Distributing web traffic across backend servers for high availability
- Securing applications with WAF and DDoS protection
- Offloading SSL processing from application servers
- Routing API traffic through an application delivery controller
- Managing multi-cloud and hybrid application delivery
website: https://www.netscaler.com/platform/apis
---
