---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-08-26'
api_count: 13
apis:
- description: 'Administration and platform settings operations on Cisco Catalyst SD-WAN Manager: user and group administration, role assignment, authentication events (server-sent), and the configuration settings th'
  name: Cisco Catalyst SD-WAN Manager API — Administration and Settings
  slug: administration-and-settings
- description: 'The UX 1.0 (classic) configuration surface: device templates, feature templates, template attach/detach and the full policy builder — data, control, application-aware routing, security, voice and ever'
  name: Cisco Catalyst SD-WAN Manager API — UX 1.0 Configuration
  slug: ux-1-0-configuration
- description: 'The UX 2.0 configuration surface: configuration groups, policy groups and topology groups, the group-based provisioning model that replaces device templates.'
  name: Cisco Catalyst SD-WAN Manager API — UX 2.0 Configuration
  slug: ux-2-0-configuration
- description: 'UX 2.0 system feature profiles for the SD-WAN solution: AAA, BFD, logging, NTP, OMP, security, SNMP, global and basic system parcels.'
  name: Cisco Catalyst SD-WAN Manager API — Feature Profiles - SD-WAN System
  slug: feature-profiles-sd-wan-system
- description: 'UX 2.0 transport feature profiles for the SD-WAN solution: WAN VPN and its interfaces (ethernet, cellular, GRE, IPsec, T1/E1, DSL), routing, trackers, management VPN and cellular controllers.'
  name: Cisco Catalyst SD-WAN Manager API — Feature Profiles - SD-WAN Transport
  slug: feature-profiles-sd-wan-transport
- description: 'UX 2.0 service (VPN-side) feature profiles for the SD-WAN solution: LAN VPN and interfaces, DHCP server, routing (BGP/OSPF/multicast), switchport, wireless LAN, trackers, AppQoE and voice/security ser'
  name: Cisco Catalyst SD-WAN Manager API — Feature Profiles - SD-WAN Service
  slug: feature-profiles-sd-wan-service
- description: 'The remaining UX 2.0 SD-WAN feature profiles: application priority, DNS security, embedded security, other profiles, policy objects, service-insertion, SIG security and SSE.'
  name: Cisco Catalyst SD-WAN Manager API — Feature Profiles - Others
  slug: feature-profiles-others
- description: 'UX 2.0 feature profiles for the SD-Routing solution: system, transport and service profiles for routers managed by SD-WAN Manager without the SD-WAN overlay.'
  name: Cisco Catalyst SD-WAN Manager API — Feature Profiles - SD-Routing
  slug: feature-profiles-sd-routing
- description: 'UX 2.0 feature profiles for Cisco Catalyst mobility (cellular gateway) and NFVirtual deployments: network, compute, cluster and networks parcels.'
  name: Cisco Catalyst SD-WAN Manager API — Feature Profiles - Mobility and NFV
  slug: feature-profiles-mobility-and-nfv
- description: 'The monitoring, real-time monitoring and troubleshooting surface of Cisco Catalyst SD-WAN Manager: device health and statistics, BFD, BGP, OMP, control connections, application-aware routing, cflowd, '
  name: Cisco Catalyst SD-WAN Manager API — Monitoring and Troubleshooting
  slug: monitoring-and-troubleshooting
- description: 'Cloud and interconnect services operated through Cisco Catalyst SD-WAN Manager: multicloud gateways and accounts, Multicloud Interconnect connectivity, entitlement and resource audit, service chaining'
  name: Cisco Catalyst SD-WAN Manager API — SD-WAN Services
  slug: sd-wan-services
- description: 'Partner and third-party integration operations: Cisco Catalyst Center (DNAC) SDA, ACI policy builder, Cisco ISE servers, Umbrella, Webex cloud service, Cisco software licensing and TAC case tooling ex'
  name: Cisco Catalyst SD-WAN Manager API — Partner Integrations
  slug: partner-integrations
- description: 'The remainder of the SD-WAN Manager surface: device inventory and certificates, software and image management, disaster recovery, multitenancy and tenant management, cluster management, smart licensin'
  name: Cisco Catalyst SD-WAN Manager API — Others
  slug: others
artifact_total: 23
asyncapis:
- description: ''
  name: Cisco Catalyst Sdwan Webhooks
  slug: cisco-catalyst-sdwan-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-catalyst-sdwan-domain-security.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/docs/sdwan/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cisco.com/docs/sdwan/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cisco.com/docs/sdwan/
- group: other
  title: ''
  type: Terraform
  url: https://github.com/CiscoDevNet/terraform-provider-sdwan
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/CiscoDevNet/catalyst-sdwan-mcp-community
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cisco.com/docs/sdwan/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/docs/sdwan/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://developer.cisco.com/docs/sdwan/developer-support/
- group: company
  title: ''
  type: Blog
  url: https://blogs.cisco.com/tag/sd-wan
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: start
  title: ''
  type: SignUp
  url: https://id.cisco.com/signin/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: operate
  title: ''
  type: Community
  url: https://community.cisco.com/t5/networking-knowledge-base/cisco-sd-wan-tools-and-resources/ta-p/4862067
- group: learn
  title: ''
  type: Training
  url: https://developer.cisco.com/learning/tracks/sd-wan_programmability/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-catalyst-sdwan-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cisco-catalyst-sdwan-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cisco-catalyst-sdwan-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cisco-catalyst-sdwan-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cisco-catalyst-sdwan-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.cisco.com/docs/sdwan/versioning-and-deprecation/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cisco-catalyst-sdwan-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cisco-catalyst-sdwan-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cisco-catalyst-sdwan-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cisco-catalyst-sdwan-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/cisco-catalyst-sdwan-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cisco-catalyst-sdwan-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cisco-catalyst-sdwan-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cisco-catalyst-sdwan-sandbox.yml
- group: start
  title: ''
  type: Sandbox
  url: https://devnetsandbox.cisco.com/RM/Diagram/Index/ed2c839d-621e-4c55-b176-db2457baf4c8?diagramType=Topology
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cisco-catalyst-sdwan-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cisco-catalyst-sdwan-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cisco-catalyst-sdwan-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cisco-catalyst-sdwan-llms.txt
- group: auth
  title: ''
  type: Security
  url: https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-catalyst-sdwan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cisco-catalyst-sdwan-trust-center.yml
- group: other
  title: ''
  type: Terraform
  url: https://registry.terraform.io/providers/CiscoDevNet/sdwan/latest
- group: other
  title: ''
  type: Ansible
  url: https://galaxy.ansible.com/ui/repo/published/cisco/catalystwan
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/CiscoDevNet/sastre
created: '2026-08-19'
description: 'Cisco Catalyst SD-WAN, built on the Viptela platform Cisco acquired in 2017, is Cisco''s wide-area network overlay: centralized policy, application-aware routing, and secure transport across MPLS, broadband and LTE. Its controller — SD-WAN Manager, formerly vManage — exposes a REST API of 4,138 published operations across 2,841 paths, documented on Cisco DevNet as thirteen OpenAPI 3.1.0 documents at release 26.1.0. The controller is customer-operated, so the base URL is each customer''s own instance at https://<sdwan-manager-host>:8443/dataservice — but the specification itself is public and anonymously fetchable from the DevNet documentation CDN, and is harvested verbatim here. Authentication is a JWT bearer token (20.18.1+) or a legacy JSESSIONID session, plus an X-XSRF-TOKEN header on writes; authorization is role-based, with every operation declaring the SD-WAN Manager permission it needs. The ecosystem includes a Terraform provider, three Ansible collections, the catalystwan
  Python SDK, the Sastre CLI and two community MCP servers published in the CiscoDevNet GitHub organization.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco.png
layout: provider
mcp_servers:
- description: ''
  name: Cisco Catalyst SD-WAN MCP Server
  slug: cisco-catalyst-sd-wan-mcp-server
- description: ''
  name: Cisco Catalyst SD-WAN MCP Server
  slug: cisco-catalyst-sd-wan-mcp-server-2
modified: '2026-08-19'
name: Cisco Catalyst SD-WAN
nav: Providers
network: true
overview: 'Cisco Catalyst SD-WAN publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Manager API — Administration and Settings, Manager API — UX 1.0 Configuration, Manager API — UX 2.0 Configuration, and 10 more. Tagged areas include SD-WAN, Networking, WAN, Automation, and Policy.


  The Cisco Catalyst SD-WAN catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cisco Catalyst SD-WAN''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 37 more developer resources.'
plans:
- name: Cisco Catalyst Sdwan Plans Pricing
  plan_count: 0
  slug: cisco-catalyst-sdwan-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Cisco Catalyst Sdwan Rate Limits
  slug: cisco-catalyst-sdwan-rate-limits
scopes:
- name: Cisco Catalyst Sdwan Scopes
  scope_count: 0
  slug: cisco-catalyst-sdwan-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 64.6
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 16.7
    contract_quality: 54.0
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 76.3
  previous_composite: 64.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 80.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Cisco Catalyst Sdwan Authentication
  slug: cisco-catalyst-sdwan-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Cisco Catalyst Sdwan Domain Security
  slug: cisco-catalyst-sdwan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cisco Catalyst Sdwan Vulnerability Disclosure
  slug: cisco-catalyst-sdwan-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Cisco Catalyst Sdwan Trust Center
  slug: cisco-catalyst-sdwan-trust-center
  summary_line: trust center published
slug: cisco-catalyst-sdwan
tags:
- SD-WAN
- Networking
- WAN
- Automation
- Policy
- Enterprise
- Network Management
- Infrastructure as Code
- Observability
- Cisco
website: https://developer.cisco.com/docs/sdwan/
---
