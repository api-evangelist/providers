---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-24'
api_count: 11
apis:
- description: Fabric interconnect, Ethernet and Fibre Channel port, VLAN/VSAN, link aggregation and network policy operations for Cisco UCS domains managed by Intersight. 629 operations across 369 paths and 8 resou
  name: Cisco Intersight Fabric API
  slug: fabric
- description: HyperFlex hyperconverged cluster profiles, node configuration, capacity forecasting and cluster recommendation operations. 296 operations across 162 paths and 4 resource tag(s), from Cisco's own OpenA
  name: Cisco Intersight HyperFlex API
  slug: hyperflex
- description: Custom resource definition operations for Intersight Kubernetes Service (IKS) cluster and add-on management. 6 operations across 2 paths and 1 resource tag(s), from Cisco's own OpenAPI 3.0.2 document.
  name: Cisco Intersight Kubernetes API
  slug: kubernetes
- description: Nexus Dashboard Insights advisories, telemetry, hardware/software compliance and field-notice operations for Nexus fabrics. 238 operations across 238 paths and 2 resource tag(s), from Cisco's own Open
  name: Cisco Intersight Nexus Insight Advisor API
  slug: nexus-insight-advisor
- description: Workflow designer, connector pack, converged-infrastructure and Infrastructure-as-a-Service orchestration operations. 183 operations across 98 paths and 5 resource tag(s), from Cisco's own OpenAPI 3.0
  name: Cisco Intersight Orchestrator API
  slug: orchestrator
- description: Server profiles, BIOS/boot/adapter/storage policies, firmware upgrade, chassis and equipment inventory, and physical compute lifecycle operations for Cisco UCS. 1499 operations across 984 paths and 46
  name: Cisco Intersight Server API
  slug: server
- description: Third-party and Cisco storage array, controller, volume and disk-group inventory and policy operations. 212 operations across 204 paths and 1 resource tag(s), from Cisco's own OpenAPI 3.0.2 document.
  name: Cisco Intersight Storage API
  slug: storage
- description: 'Account, IAM, appliance, licensing, audit, bulk request, notification, search and platform administration operations for the Intersight tenant itself. 1192 operations across 671 paths and 44 resource '
  name: Cisco Intersight System API
  slug: system
- description: Time-series telemetry query operations returning aggregated infrastructure metrics via the Druid query interface. 8 operations across 8 paths and 1 resource tag(s), from Cisco's own OpenAPI 3.0.2 docu
  name: Cisco Intersight Telemetry API
  slug: telemetry
- description: Hypervisor, virtual machine, datastore and virtual-console operations for VMware, Hyper-V and Intersight-managed virtualization targets. 96 operations across 50 paths and 2 resource tag(s), from Cisco
  name: Cisco Intersight Virtualization API
  slug: virtualization
- description: Workflow definitions, task definitions, batch API executors, service items, catalog items and cross-domain automation operations, including Meraki, DNAC, FMC and Catalyst SD-WAN connectors. 732 operat
  name: Cisco Intersight Workflows API
  slug: workflows
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intersight-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/intersight-scopes.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: start
  title: ''
  type: Portal
  url: https://intersight.com/apidocs/introduction/overview/
- group: docs
  title: ''
  type: Documentation
  url: https://intersight.com/apidocs/introduction/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://intersight.com/apidocs/apirefs/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CiscoDevNet/intersight-python
- group: other
  title: ''
  type: Terraform
  url: https://github.com/CiscoDevNet/terraform-provider-intersight
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: build
  title: ''
  type: Packages
  url: packages/intersight-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/intersight-packages.yml
- group: build
  title: ''
  type: Postman
  url: https://github.com/CiscoDevNet/intersight-postman
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/intersight-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intersight-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/intersight-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/intersight-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/intersight-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/intersight-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/intersight-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/intersight-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.intersight.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/intersight-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/intersight-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/intersight-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/intersight-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/intersight-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/intersight-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cisco.com/site/us/en/products/computing/hybrid-cloud-operations/intersight-platform/licensing.html
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/intersight-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/intersight-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/intersight-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/learning/tracks/intersight-infra/intersight-rest-api/
- group: operate
  title: ''
  type: Support
  url: https://intersight.com/help
- group: start
  title: ''
  type: SignUp
  url: https://www.cisco.com/go/intersightfreetrial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/end_user_license_agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
created: '2026-08-19'
description: 'Cisco Intersight is Cisco''s SaaS operations platform for UCS servers, HyperFlex clusters, Nexus fabrics, third-party storage and virtualization, covering provisioning, firmware lifecycle, workload optimization, telemetry and Kubernetes service delivery. Cisco publishes the full OpenAPI 3.0.2 contract for the platform anonymously — 3,963 operations across 2,448 paths and 5,612 schemas, split into twelve per-service documents plus a combined document, served from cdn.intersight.com and refreshed on every production release. Every operation carries a summary, a tag and a unique operationId. The API uses OData-style query semantics ($filter, $top, $skip, $select, $expand, $apply), HTTP-signature or OAuth2 authorization-code authentication with 54 role scopes, RFC 7240 Prefer: respond-async for long-running work, and conditional requests (If-Match / If-None-Match) for lost-update protection.'
image: https://cdn.intersight.com/components/ucs-an-common/1.0.11-20260717085249663/images/social/socialMediaPreviewImage1024.png
layout: provider
modified: '2026-08-19'
name: Cisco Intersight
nav: Providers
network: true
overview: 'Cisco Intersight publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Fabric API, HyperFlex API, Kubernetes API, and 8 more. Tagged areas include Infrastructure, Cloud Operations, Data-Center, Compute, and Networking.


  Cisco Intersight''s developer surface includes developer portal, documentation, API reference, changelog, pricing, sandbox, authentication, and 30 more developer resources.'
plans:
- name: Intersight Plans Pricing
  plan_count: 2
  slug: intersight-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Intersight Rate Limits
  slug: intersight-rate-limits
scopes:
- name: Intersight Scopes
  scope_count: 3317
  slug: intersight-scopes
  summary_line: 3317 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 59.8
  delta: -0.3
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 16.7
    contract_quality: 51.7
    developer_ergonomics: 75.6
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 52.6
  previous_composite: 60.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Intersight Authentication
  slug: intersight-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Intersight Domain Security
  slug: intersight-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Intersight Vulnerability Disclosure
  slug: intersight-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Intersight Trust Center
  slug: intersight-trust-center
  summary_line: trust center published
slug: intersight
tags:
- Infrastructure
- Cloud Operations
- Data-Center
- Compute
- Networking
- Enterprise
- Storage
- Virtualization
- Kubernetes
- Orchestration
- Telemetry
- Firmware Management
website: https://intersight.com/apidocs/introduction/overview/
---
