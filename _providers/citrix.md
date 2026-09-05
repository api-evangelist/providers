---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 37
  human_in_the_loop: 0
  name: Citrix Agentic Access
  operation_count: 69
  slug: citrix-agentic-access
  summary_line: 69 operations · 37 acting
api_count: 6
apis:
- description: Integrate and customize Citrix Workspace for end users.
  name: Citrix Workspace API
  slug: citrix-workspace-api
- description: Access analytics data for security and performance insights.
  name: Citrix Analytics API
  slug: citrix-analytics-api
- description: OData-based API for querying monitoring data from Citrix Virtual Apps and Desktops deployments, including session, connection, machine, and application usage data for reporting and analytics.
  name: Citrix Monitor Service OData API
  slug: citrix-monitor-service-odata-api
- description: Server-side API for customizing and extending the Citrix StoreFront store services, including endpoint management, authentication, and resource enumeration behaviors.
  name: Citrix StoreFront Store Services API
  slug: citrix-storefront-store-services-api
- description: SDK for building custom authentication methods for Citrix StoreFront, allowing integration with third-party identity providers and custom authentication workflows.
  name: Citrix StoreFront Authentication SDK
  slug: citrix-storefront-authentication-sdk
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Manage zero trust access policies
  name: Citrix Access Policies API
  slug: citrix-access-policies-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Manage application domain configurations
  name: Citrix Application Domains API
  slug: citrix-application-domains-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Manage published applications
  name: Citrix Applications API
  slug: citrix-applications-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Login and session management
  name: Citrix Authentication API
  slug: citrix-authentication-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Manage application certificates
  name: Citrix Certificates API
  slug: citrix-certificates-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Content switching virtual servers and policies
  name: Citrix Content Switching API
  slug: citrix-content-switching-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Manage delivery groups for resource assignment
  name: Citrix Delivery Groups API
  slug: citrix-delivery-groups-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Device enrollment and lifecycle management
  name: Citrix Devices API
  slug: citrix-devices-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Manage hypervisor connections
  name: Citrix Hypervisors API
  slug: citrix-hypervisors-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Launch applications and desktops
  name: Citrix Launch API
  slug: citrix-launch-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Load balancing virtual servers and services
  name: Citrix Load Balancing API
  slug: citrix-load-balancing-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Manage machine catalogs and provisioning
  name: Citrix Machine Catalogs API
  slug: citrix-machine-catalogs-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Manage individual machines in catalogs
  name: Citrix Machines API
  slug: citrix-machines-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Manage platform notifications
  name: Citrix Notifications API
  slug: citrix-notifications-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Device and app policy management
  name: Citrix Policies API
  slug: citrix-policies-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Manage resource locations within a customer
  name: Citrix Resource Locations API
  slug: citrix-resource-locations-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Enumerate available applications and desktops
  name: Citrix Resources API
  slug: citrix-resources-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Manage service principals for API automation
  name: Citrix Service Principals API
  slug: citrix-service-principals-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: Manage and monitor active sessions
  name: Citrix Sessions API
  slug: citrix-sessions-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: SSL certificates and configuration
  name: Citrix SSL API
  slug: citrix-ssl-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: System configuration and statistics
  name: Citrix System API
  slug: citrix-system-api
- baseURL: https://{customer-id}.xendesktop.net
  baseurl_source: declared
  description: User and group management
  name: Citrix Users API
  slug: citrix-users-api
artifact_total: 133
collections:
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies API
  slug: postman-citrix-access-policies-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Application Domains API
  slug: postman-citrix-application-domains-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Applications API
  slug: postman-citrix-applications-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Authentication API
  slug: postman-citrix-authentication-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Certificates API
  slug: postman-citrix-certificates-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Content Switching API
  slug: postman-citrix-content-switching-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Delivery Groups API
  slug: postman-citrix-delivery-groups-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Devices API
  slug: postman-citrix-devices-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Hypervisors API
  slug: postman-citrix-hypervisors-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Launch API
  slug: postman-citrix-launch-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Load Balancing API
  slug: postman-citrix-load-balancing-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Machine Catalogs API
  slug: postman-citrix-machine-catalogs-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Machines API
  slug: postman-citrix-machines-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Notifications API
  slug: postman-citrix-notifications-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies API
  slug: postman-citrix-policies-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Resource Locations API
  slug: postman-citrix-resource-locations-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Resources API
  slug: postman-citrix-resources-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Service Principals API
  slug: postman-citrix-service-principals-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Sessions API
  slug: postman-citrix-sessions-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies SSL API
  slug: postman-citrix-ssl-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies System API
  slug: postman-citrix-system-api
- collection_type: postman
  name: Citrix ADC (NetScaler) NITRO Access Policies Users API
  slug: postman-citrix-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies API
  slug: open-citrix-access-policies-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO API
  slug: open-citrix-adc-nitro
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Application Domains API
  slug: open-citrix-application-domains-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Applications API
  slug: open-citrix-applications-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Authentication API
  slug: open-citrix-authentication-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Certificates API
  slug: open-citrix-certificates-api
- collection_type: open
  name: Citrix Cloud API
  slug: open-citrix-cloud
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Content Switching API
  slug: open-citrix-content-switching-api
- collection_type: open
  name: Citrix DaaS REST API
  slug: open-citrix-daas
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Delivery Groups API
  slug: open-citrix-delivery-groups-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Devices API
  slug: open-citrix-devices-api
- collection_type: open
  name: Citrix Endpoint Management REST API
  slug: open-citrix-endpoint-management
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Hypervisors API
  slug: open-citrix-hypervisors-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Launch API
  slug: open-citrix-launch-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Load Balancing API
  slug: open-citrix-load-balancing-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Machine Catalogs API
  slug: open-citrix-machine-catalogs-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Machines API
  slug: open-citrix-machines-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Notifications API
  slug: open-citrix-notifications-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies API
  slug: open-citrix-policies-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Resource Locations API
  slug: open-citrix-resource-locations-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Resources API
  slug: open-citrix-resources-api
- collection_type: open
  name: Citrix Secure Private Access API
  slug: open-citrix-secure-private-access
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Service Principals API
  slug: open-citrix-service-principals-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Sessions API
  slug: open-citrix-sessions-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies SSL API
  slug: open-citrix-ssl-api
- collection_type: open
  name: Citrix StoreFront Web API
  slug: open-citrix-storefront-web
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies System API
  slug: open-citrix-system-api
- collection_type: open
  name: Citrix ADC (NetScaler) NITRO Access Policies Users API
  slug: open-citrix-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/citrix-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/citrix/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/citrix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citrix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/citrix-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/citrix
- group: start
  title: ''
  type: Portal
  url: https://developer-docs.citrix.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer-docs.citrix.com/en-us/citrix-cloud/citrix-cloud-api-overview/get-started-with-citrix-cloud-apis.html
- group: auth
  title: ''
  type: Authentication
  url: https://developer-docs.citrix.com/en-us/citrix-cloud/citrix-cloud-api-overview/get-started-with-citrix-cloud-apis.html
- group: company
  title: ''
  type: Blog
  url: https://www.citrix.com/blogs/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.com/
- group: operate
  title: ''
  type: Support
  url: https://support.citrix.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.cloud.com/citrix-developer-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.citrix.com/about/legal/privacy/plain.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/citrix
- group: operate
  title: ''
  type: Community
  url: https://discussions.citrix.com/
- group: build
  title: ''
  type: SDKs
  url: https://docs.citrix.com/en-us/citrix-cloud/sdk-api.html
- group: company
  title: ''
  type: Website
  url: https://www.citrix.com
- group: start
  title: ''
  type: Login
  url: https://accounts.cloud.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/citrix-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/citrix-machine-catalog-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/citrix-session-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/citrix-rules.yml
created: '2024-01-01'
description: Citrix is a global software company providing virtualization, networking, workspace, and digital experience products that allow organizations to deliver applications and desktops securely from data centers and clouds to any device. Citrix exposes its programmable surface through the Citrix Cloud platform and developer.citrix.com / developer-docs.citrix.com, with REST APIs spanning Virtual Apps and Desktops, DaaS, Workspace, Citrix Cloud, ADC (NetScaler) NITRO, Endpoint Management, Secure Private Access, and Analytics. Authentication uses OAuth 2.0 bearer tokens issued through Citrix Cloud customer-id-scoped credentials.
finops:
- name: Citrix Finops
  service_category: End-User Computing
  slug: citrix-finops
image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
json_schemas:
- name: AccessPolicy
  property_count: 7
  slug: citrix-accesspolicy
- name: Application
  property_count: 7
  slug: citrix-application
- name: ApplicationCollection
  property_count: 1
  slug: citrix-applicationcollection
- name: ApplicationFilterRequest
  property_count: 2
  slug: citrix-applicationfilterrequest
- name: Certificate
  property_count: 5
  slug: citrix-certificate
- name: CreateAccessPolicyRequest
  property_count: 4
  slug: citrix-createaccesspolicyrequest
- name: CreateApplicationRequest
  property_count: 4
  slug: citrix-createapplicationrequest
- name: CreateCertificateRequest
  property_count: 3
  slug: citrix-createcertificaterequest
- name: CreateDeliveryGroupRequest
  property_count: 3
  slug: citrix-createdeliverygrouprequest
- name: CreateMachineCatalogRequest
  property_count: 5
  slug: citrix-createmachinecatalogrequest
- name: CreateServicePrincipalRequest
  property_count: 1
  slug: citrix-createserviceprincipalrequest
- name: CsVserver
  property_count: 5
  slug: citrix-csvserver
- name: DeliveryGroup
  property_count: 7
  slug: citrix-deliverygroup
- name: DeliveryGroupCollection
  property_count: 1
  slug: citrix-deliverygroupcollection
- name: DeliveryGroupFilterRequest
  property_count: 2
  slug: citrix-deliverygroupfilterrequest
- name: Device
  property_count: 10
  slug: citrix-device
- name: DeviceFilterRequest
  property_count: 4
  slug: citrix-devicefilterrequest
- name: Hypervisor
  property_count: 4
  slug: citrix-hypervisor
- name: HypervisorCollection
  property_count: 1
  slug: citrix-hypervisorcollection
- name: LaunchStatus
  property_count: 2
  slug: citrix-launchstatus
- name: LbVserver
  property_count: 7
  slug: citrix-lbvserver
- name: LbVserverStats
  property_count: 8
  slug: citrix-lbvserverstats
- name: Citrix Machine Catalog
  property_count: 8
  slug: citrix-machine-catalog
- name: Machine
  property_count: 7
  slug: citrix-machine
- name: MachineCatalog
  property_count: 8
  slug: citrix-machinecatalog
- name: MachineCatalogCollection
  property_count: 1
  slug: citrix-machinecatalogcollection
- name: MachineCollection
  property_count: 1
  slug: citrix-machinecollection
- name: Notification
  property_count: 5
  slug: citrix-notification
- name: NsConfig
  property_count: 4
  slug: citrix-nsconfig
- name: Resource
  property_count: 6
  slug: citrix-resource
- name: ResourceLocation
  property_count: 5
  slug: citrix-resourcelocation
- name: ResourcesResponse
  property_count: 1
  slug: citrix-resourcesresponse
- name: Service
  property_count: 5
  slug: citrix-service
- name: ServiceGroup
  property_count: 3
  slug: citrix-servicegroup
- name: ServicePrincipal
  property_count: 5
  slug: citrix-serviceprincipal
- name: Citrix Session
  property_count: 7
  slug: citrix-session
- name: SessionCollection
  property_count: 1
  slug: citrix-sessioncollection
- name: SslCertKey
  property_count: 5
  slug: citrix-sslcertkey
- name: SystemStats
  property_count: 6
  slug: citrix-systemstats
- name: TokenResponse
  property_count: 3
  slug: citrix-tokenresponse
- name: UpdateApplicationRequest
  property_count: 4
  slug: citrix-updateapplicationrequest
- name: UpdateDeliveryGroupRequest
  property_count: 3
  slug: citrix-updatedeliverygrouprequest
- name: UpdateMachineCatalogRequest
  property_count: 2
  slug: citrix-updatemachinecatalogrequest
- name: User
  property_count: 5
  slug: citrix-user
- name: UserFilterRequest
  property_count: 3
  slug: citrix-userfilterrequest
json_structures:
- name: Citrix Structure
  property_count: 0
  slug: citrix-structure
jsonld:
- class_count: 0
  name: Citrix Context
  property_count: 8
  slug: citrix-context
layout: provider
modified: '2026-05-19'
name: Citrix
nav: Providers
network: true
overview: 'Citrix publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Access Policies API, Application Domains API, Applications API, and 19 more. Tagged areas include Application Delivery, Desktop as a Service, Networking, Virtualization, and Workspace.


  The Citrix catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Citrix''s developer surface includes authentication, developer portal, getting-started guide, engineering blog, support, and 18 more developer resources.'
plans:
- name: Citrix Plans Pricing
  plan_count: 3
  slug: citrix-plans-pricing
press:
- date: '2026-05-25'
  title: Citrix Introduces NetScaler AI Gateway to Bring Enterprise ...
  url: https://www.businesswire.com/news/home/20260409250389/en/Citrix-Introduces-NetScaler-AI-Gateway-to-Bring-Enterprise-Governance-to-AI-Application-Delivery
- date: '2026-05-25'
  title: Top Citrix Systems Alternatives 2026 — Best Cloud Computing ...
  url: https://www.startuphub.ai/startups/citrix-systems/alternatives
- date: '2026-05-25'
  title: 'Work 2035: Citrix Research Reveals a More Intelligent Future'
  url: https://aithority.com/the-future/work-2035-citrix-research-reveals-a-more-intelligent-future/
- date: '2026-05-25'
  title: 'Citrix Workspace Secure Access: Latest News'
  url: https://thesiliconreview.com/citrix
- date: '2026-05-25'
  title: Citrix Systems Archives - Software Strategies Blog
  url: http://softwarestrategiesblog.com/tag/citrix-systems/
random_paper: 8
rate_limits:
- limit_count: 3
  name: Citrix Rate Limits
  slug: citrix-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Citrix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: citrix-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Citrix API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: citrix-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 55.5
    catalog_earned_first_party: 0.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 13.6
    contract_quality: 61.7
    developer_ergonomics: 63.1
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/citrix/refs/heads/main/screenshots/citrix-2026-06-20T174413.png
security:
- kind: authentication
  name: Citrix Authentication
  slug: citrix-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Citrix Domain Security
  slug: citrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citrix
tags:
- Application Delivery
- Desktop as a Service
- Networking
- Virtualization
- Workspace
- Fortune 1000
website: https://www.citrix.com
---
