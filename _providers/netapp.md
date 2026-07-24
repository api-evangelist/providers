---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 59.6
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Netapp Agentic Access
  operation_count: 23
  slug: netapp-agentic-access
  summary_line: 23 operations · 11 acting
api_count: 18
apis:
- description: API for managing NetApp Cloud Volumes Service in major cloud providers.
  name: NetApp Cloud Volumes Service API
  slug: netapp-cloud-volumes-service-api
- description: API for Kubernetes-native application data management.
  name: NetApp Astra Control API
  slug: netapp-astra-control-api
- description: API for object storage management with StorageGRID.
  name: NetApp StorageGRID API
  slug: netapp-storagegrid-api
- description: API for NetApp Element software and NetApp HCI storage management.
  name: NetApp Element API
  slug: netapp-element-api
- description: API for infrastructure monitoring and analytics.
  name: NetApp Cloud Insights API
  slug: netapp-cloud-insights-api
- description: REST API for automating the administration of cloud-based and on-premises storage resources managed by NetApp BlueXP, including Cloud Volumes ONTAP, on-premises ONTAP, and other BlueXP services.
  name: NetApp BlueXP Automation API
  slug: netapp-bluexp-automation-api
- description: REST API for managing and monitoring storage resources on supported NetApp storage systems, including health, performance, capacity, and event management.
  name: NetApp Active IQ Unified Manager API
  slug: netapp-active-iq-unified-manager-api
- description: API services for NetApp Active IQ Digital Advisor providing system information, storage efficiency, performance, health, and upgrade insights across your NetApp installed base.
  name: NetApp Active IQ Digital Advisor API
  slug: netapp-active-iq-digital-advisor-api
- description: REST API for automating SnapCenter data protection operations including backup, restore, and clone management for applications and databases.
  name: NetApp SnapCenter API
  slug: netapp-snapcenter-api
- description: RESTful API for managing and monitoring NetApp E-Series and EF-Series storage systems through the SANtricity Web Services Proxy.
  name: NetApp E-Series SANtricity Web Services API
  slug: netapp-e-series-santricity-web-services-api
- description: REST API for managing Azure NetApp Files resources including NetApp accounts, capacity pools, volumes, and snapshots in Microsoft Azure.
  name: Azure NetApp Files REST API
  slug: azure-netapp-files-rest-api
- description: REST API for managing ONTAP tools for VMware vSphere, enabling storage provisioning, virtual machine lifecycle management, and vSphere integration.
  name: NetApp ONTAP Tools for VMware vSphere API
  slug: netapp-ontap-tools-for-vmware-vsphere-api
- description: Operations for managing storage aggregates (local tiers)
  name: NetApp Aggregates API
  slug: netapp-aggregates-api
- description: Operations for managing ONTAP cluster configuration, nodes, licensing, and health
  name: NetApp Cluster API
  slug: netapp-cluster-api
- description: Operations for managing network interfaces, ports, and IP configuration
  name: NetApp Network API
  slug: netapp-network-api
- description: Operations for managing volume snapshots
  name: NetApp Snapshots API
  slug: netapp-snapshots-api
- description: Operations for managing storage virtual machines (SVMs / vservers)
  name: NetApp SVMs API
  slug: netapp-svms-api
- description: Operations for creating, modifying, and managing storage volumes
  name: NetApp Volumes API
  slug: netapp-volumes-api
artifact_total: 95
collections:
- collection_type: open
  name: NetApp ONTAP REST API
  slug: open-netapp-ontap
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/netapp-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/netapp-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netapp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/netapp-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netapp
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devnet.netapp.com/
- group: operate
  title: ''
  type: Support
  url: https://www.netapp.com/support-and-training/
- group: company
  title: ''
  type: Blog
  url: https://netapp.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NetApp
- group: company
  title: ''
  type: Blog
  url: https://blog.netapp.com/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/NetApp/mcp
created: '2024'
description: Collection of NetApp APIs for cloud data services, storage management, and infrastructure.
examples:
- key_count: 8
  name: Netapp Ontap Aggregate Example
  slug: netapp-ontap-aggregate-example
- key_count: 2
  name: Netapp Ontap Aggregate Reference Example
  slug: netapp-ontap-aggregate-reference-example
- key_count: 10
  name: Netapp Ontap Cluster Example
  slug: netapp-ontap-cluster-example
- key_count: 8
  name: Netapp Ontap Cluster Node Example
  slug: netapp-ontap-cluster-node-example
- key_count: 2
  name: Netapp Ontap Cluster Node Reference Example
  slug: netapp-ontap-cluster-node-reference-example
- key_count: 2
  name: Netapp Ontap Collection Links Example
  slug: netapp-ontap-collection-links-example
- key_count: 1
  name: Netapp Ontap Error Response Example
  slug: netapp-ontap-error-response-example
- key_count: 2
  name: Netapp Ontap Job Link Example
  slug: netapp-ontap-job-link-example
- key_count: 4
  name: Netapp Ontap License Example
  slug: netapp-ontap-license-example
- key_count: 8
  name: Netapp Ontap Network Interface Example
  slug: netapp-ontap-network-interface-example
- key_count: 1
  name: Netapp Ontap Self Link Example
  slug: netapp-ontap-self-link-example
- key_count: 8
  name: Netapp Ontap Snapshot Example
  slug: netapp-ontap-snapshot-example
- key_count: 18
  name: Netapp Ontap Svm Example
  slug: netapp-ontap-svm-example
- key_count: 2
  name: Netapp Ontap Svm Reference Example
  slug: netapp-ontap-svm-reference-example
- key_count: 19
  name: Netapp Ontap Volume Example
  slug: netapp-ontap-volume-example
- key_count: 2
  name: Netapp Ontap Volume Reference Example
  slug: netapp-ontap-volume-reference-example
finops:
- name: Netapp Finops
  service_category: Storage + Data Management
  slug: netapp-finops
image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
json_schemas:
- name: Aggregate
  property_count: 10
  slug: netapp-aggregate
- name: AggregateReference
  property_count: 3
  slug: netapp-aggregatereference
- name: Cluster
  property_count: 11
  slug: netapp-cluster
- name: ClusterNode
  property_count: 9
  slug: netapp-clusternode
- name: ClusterNodeReference
  property_count: 3
  slug: netapp-clusternodereference
- name: CollectionLinks
  property_count: 2
  slug: netapp-collectionlinks
- name: ErrorResponse
  property_count: 1
  slug: netapp-errorresponse
- name: JobLink
  property_count: 2
  slug: netapp-joblink
- name: License
  property_count: 5
  slug: netapp-license
- name: NetworkInterface
  property_count: 10
  slug: netapp-networkinterface
- name: AggregateReference
  property_count: 2
  slug: netapp-ontap-aggregate-reference
- name: Aggregate
  property_count: 8
  slug: netapp-ontap-aggregate
- name: ClusterNodeReference
  property_count: 2
  slug: netapp-ontap-cluster-node-reference
- name: ClusterNode
  property_count: 8
  slug: netapp-ontap-cluster-node
- name: Cluster
  property_count: 10
  slug: netapp-ontap-cluster
- name: CollectionLinks
  property_count: 2
  slug: netapp-ontap-collection-links
- name: ErrorResponse
  property_count: 1
  slug: netapp-ontap-error-response
- name: JobLink
  property_count: 2
  slug: netapp-ontap-job-link
- name: License
  property_count: 4
  slug: netapp-ontap-license
- name: NetworkInterface
  property_count: 8
  slug: netapp-ontap-network-interface
- name: SelfLink
  property_count: 1
  slug: netapp-ontap-self-link
- name: Snapshot
  property_count: 8
  slug: netapp-ontap-snapshot
- name: SvmReference
  property_count: 2
  slug: netapp-ontap-svm-reference
- name: Svm
  property_count: 18
  slug: netapp-ontap-svm
- name: VolumeReference
  property_count: 2
  slug: netapp-ontap-volume-reference
- name: Volume
  property_count: 19
  slug: netapp-ontap-volume
- name: SelfLink
  property_count: 1
  slug: netapp-selflink
- name: Snapshot
  property_count: 10
  slug: netapp-snapshot
- name: Svm
  property_count: 19
  slug: netapp-svm
- name: SvmReference
  property_count: 3
  slug: netapp-svmreference
- name: NetApp ONTAP Volume
  property_count: 21
  slug: netapp-volume
- name: VolumeReference
  property_count: 3
  slug: netapp-volumereference
json_structures:
- name: Netapp Ontap Aggregate Reference Structure
  property_count: 2
  slug: netapp-ontap-aggregate-reference-structure
- name: Netapp Ontap Aggregate Structure
  property_count: 8
  slug: netapp-ontap-aggregate-structure
- name: Netapp Ontap Cluster Node Reference Structure
  property_count: 2
  slug: netapp-ontap-cluster-node-reference-structure
- name: Netapp Ontap Cluster Node Structure
  property_count: 8
  slug: netapp-ontap-cluster-node-structure
- name: Netapp Ontap Cluster Structure
  property_count: 10
  slug: netapp-ontap-cluster-structure
- name: Netapp Ontap Collection Links Structure
  property_count: 2
  slug: netapp-ontap-collection-links-structure
- name: Netapp Ontap Error Response Structure
  property_count: 1
  slug: netapp-ontap-error-response-structure
- name: Netapp Ontap Job Link Structure
  property_count: 2
  slug: netapp-ontap-job-link-structure
- name: Netapp Ontap License Structure
  property_count: 4
  slug: netapp-ontap-license-structure
- name: Netapp Ontap Network Interface Structure
  property_count: 8
  slug: netapp-ontap-network-interface-structure
- name: Netapp Ontap Self Link Structure
  property_count: 1
  slug: netapp-ontap-self-link-structure
- name: Netapp Ontap Snapshot Structure
  property_count: 8
  slug: netapp-ontap-snapshot-structure
- name: Netapp Ontap Svm Reference Structure
  property_count: 2
  slug: netapp-ontap-svm-reference-structure
- name: Netapp Ontap Svm Structure
  property_count: 18
  slug: netapp-ontap-svm-structure
- name: Netapp Ontap Volume Reference Structure
  property_count: 2
  slug: netapp-ontap-volume-reference-structure
- name: Netapp Ontap Volume Structure
  property_count: 19
  slug: netapp-ontap-volume-structure
- name: Netapp Structure
  property_count: 0
  slug: netapp-structure
jsonld:
- class_count: 0
  name: Netapp Context
  property_count: 8
  slug: netapp-context
- class_count: 0
  name: Netapp Ontap Context
  property_count: 0
  slug: netapp-ontap-context
layout: provider
modified: '2026-05-19'
name: NetApp
nav: Providers
network: true
overview: 'NetApp publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Aggregates API, Cluster API, Network API, and 3 more. Tagged areas include Cloud, Data Management, Hybrid Cloud, Infrastructure, and Storage.


  The NetApp catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  NetApp''s developer surface includes authentication, support, engineering blog, and 8 more developer resources.'
plans:
- name: Netapp Plans Pricing
  plan_count: 7
  slug: netapp-plans-pricing
press:
- date: '2026-05-25'
  title: AI infrastructure and data management
  url: https://www.netapp.com/artificial-intelligence/
- date: '2026-05-25'
  title: Press Releases - News and Information
  url: https://www.netapp.com/newsroom/press-releases/
- date: '2026-05-25'
  title: Unleash AI innovation with your data with the ...
  url: https://www.netapp.com/video/ofx1pmmqag8/unleash-ai-innovation-with-your-data-with-the-netapp-platform/
- date: '2026-05-25'
  title: Data Storage and Cloud Storage Newsroom
  url: https://www.netapp.com/newsroom/
- date: '2026-05-25'
  title: AI in the wild | Watts the Future
  url: https://www.netapp.com/video/tM47Foy3L_U/ai-in-the-wild-watts-the-future/
random_paper: 36
rate_limits:
- limit_count: 4
  name: Netapp Rate Limits
  slug: netapp-rate-limits
rules:
- name: NetApp API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: netapp-jsonschema-spectral-rules
- name: NetApp API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 6
  slug: netapp-spectral-rules
score:
  band: developing
  composite: 51.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 64.6
    developer_ergonomics: 34.8
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 51.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netapp/refs/heads/main/screenshots/netapp-2026-06-20T190143.png
security:
- kind: authentication
  name: Netapp Authentication
  slug: netapp-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Netapp Domain Security
  slug: netapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Netapp Trust Center
  slug: netapp-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR, FIPS 140
slug: netapp
tags:
- Cloud
- Data Management
- Hybrid Cloud
- Infrastructure
- Storage
- Fortune 500
website: https://devnet.netapp.com/
---
