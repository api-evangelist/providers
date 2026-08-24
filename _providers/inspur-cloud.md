---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.1
  scored_at: '2026-08-24'
api_count: 18
apis:
- description: 'REST API for Inspur Cloud''s elastic compute service: create, start, stop, reboot, resize, rebuild and delete cloud servers, manage private images, security-group membership, attached volumes, SSH key '
  name: Inspur Cloud Elastic Cloud Server (ECS) API
  slug: inspur-cloud-elastic-cloud-server-ecs-api
- description: REST API for Inspur Cloud's bare-metal cloud physical host service — list, start, stop, reboot and inspect dedicated physical servers. 14 documented operations.
  name: Inspur Cloud Physical Server (CPS) API
  slug: inspur-cloud-physical-server-cps-api
- description: REST API for Inspur Cloud block storage — create, extend, renew, attach, detach and delete cloud disks, plus backup creation, restore, statistics and backup strategy management. 52 documented operatio
  name: Inspur Cloud Elastic Block Storage (EBS) API
  slug: inspur-cloud-elastic-block-storage-ebs-api
- description: REST API for Inspur Cloud's cloud backup service, covering backup jobs, restore and backup policy operations. 10 documented operations.
  name: Inspur Cloud Backup Service (CBS) API
  slug: inspur-cloud-backup-service-cbs-api
- description: REST API for Inspur Cloud software-defined networking — create and manage VPCs, subnets, route tables, routes, security groups and security-group rules. 26 documented operations.
  name: Inspur Cloud Virtual Private Cloud (VPC) API
  slug: inspur-cloud-virtual-private-cloud-vpc-api
- description: REST API for elastic public IP addresses, shared bandwidth packages and the IPv6 translation service — create, bind, unbind, resize bandwidth, renew and release. 27 documented operations.
  name: Inspur Cloud Elastic IP (EIP) API
  slug: inspur-cloud-elastic-ip-eip-api
- description: REST API for the IPv6 translation service that fronts IPv4 resources with IPv6 addresses. 6 documented operations, served from the EIP host.
  name: Inspur Cloud IPv6 Translation Service (IPTS) API
  slug: inspur-cloud-ipv6-translation-service-ipts-api
- description: 'REST API for Inspur Cloud load balancing: load balancer, listener, backend server group, certificate and forwarding-strategy management, plus EIP binding. 40 documented operations. The reference does '
  name: Inspur Cloud Server Load Balancer (SLB) API
  slug: inspur-cloud-server-load-balancer-slb-api
- description: REST API for Inspur Cloud identity — services and resource-type discovery, policy CRUD and attach/detach, user and user-group management, MFA/TOTP binding, and access-key management. 59 documented ope
  name: Inspur Cloud Identity and Access Management (IAM) API
  slug: inspur-cloud-identity-and-access-management-iam-api
- description: REST API for Inspur Cloud's managed MySQL relational database service — instance lifecycle, instance classes, database and account management, backup, restore and instance monitoring. 57 documented op
  name: Inspur Cloud RDS for MySQL API
  slug: inspur-cloud-rds-for-mysql-api
- description: 'S3-compatible REST API for Inspur Cloud object storage: ListBuckets, PutBucket, HeadBucket, DeleteBucket, bucket ACL/lifecycle/CORS/versioning/encryption/ website/custom-domain configuration, and obje'
  name: Inspur Cloud Object Storage Service (OSS) API
  slug: inspur-cloud-object-storage-service-oss-api
- description: REST API for Inspur Cloud's managed time-series database — instance lifecycle, parameter configuration, data write and query, OpenTSDB-compatible endpoints, HBase service and Ambari operations. 67 doc
  name: Inspur Cloud Time Series Database (TSDB) API
  slug: inspur-cloud-time-series-database-tsdb-api
- description: REST API for Inspur Cloud's Kubernetes container engine — application and instance management, service mesh (VirtualService) discovery, service gateway routes, cluster create/delete/scale, node and na
  name: Inspur Cloud Container Engine (ICE/CKS) API
  slug: inspur-cloud-container-engine-icecks-api
- description: REST API for Inspur Cloud blockchain-as-a-service instance management — name checking, instance listing, instance detail and deletion. 5 documented operations.
  name: Inspur Cloud Blockchain Service (IBaaS) API
  slug: inspur-cloud-blockchain-service-ibaas-api
- description: REST API for Inspur Cloud's consortium blockchain service — instance management and renewal orders. 6 documented operations.
  name: Inspur Cloud Consortium Chain Service (ACS) API
  slug: inspur-cloud-consortium-chain-service-acs-api
- description: REST API for Inspur Cloud's IBot intelligent assistant — POST /qa/bot/sdk/talk for a conversation turn, /qa/bot/sdk/similarities for a similar-question list and /qa/bot/sdk/media for media files. 4 do
  name: Inspur Cloud IBot Conversational AI API
  slug: inspur-cloud-ibot-conversational-ai-api
- description: Cloud-side and device-side API for the Inspur Cloud IoT platform, with an MQTT device protocol, device dynamic registration and a C device SDK built on mbedTLS.
  name: Inspur Cloud IoT Platform API
  slug: inspur-cloud-iot-platform-api
- description: Inspur Cloud's API Gateway product, which lets customers publish their own APIs with Swagger import/export, traffic control, circuit breaking, anti-replay, IAM AK/SK and token auth plugins, mock and f
  name: Inspur Cloud API Gateway (APIG)
  slug: inspur-cloud-api-gateway-apig
artifact_total: 24
common:
- group: company
  title: ''
  type: Website
  url: https://cloud.inspur.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console1.cloud.inspur.com/document/
- group: docs
  title: ''
  type: Documentation
  url: https://console1.cloud.inspur.com/document/
- group: docs
  title: ''
  type: APIReference
  url: https://console1.cloud.inspur.com/document/ecs/5-API/5.1-1-api-overview.html
- group: start
  title: ''
  type: GettingStarted
  url: https://console1.cloud.inspur.com/document/ecs/3-quickstart.html
- group: operate
  title: ''
  type: Support
  url: https://cloud.inspur.com/support/index.html
- group: company
  title: ''
  type: Blog
  url: https://cloud.inspur.com/about-inspurcloud/about-us/news/index.html
- group: start
  title: ''
  type: SignUp
  url: https://console1.cloud.inspur.com/
- group: start
  title: ''
  type: Login
  url: https://console1.cloud.inspur.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://console1.cloud.inspur.com/document/declaration/protocol/client/client.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloud.inspur.com/privacy-policy/index.html
- group: commercial
  title: ''
  type: Pricing
  url: https://console1.cloud.inspur.com/document/ecs/2-product-pricing.html
- group: build
  title: ''
  type: Packages
  url: packages/inspur-cloud-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/inspur-cloud-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inspur-cloud-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inspur-cloud-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inspur-cloud-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inspur-cloud-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/inspur-cloud-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inspur-cloud-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inspur-cloud-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/inspur-cloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.inspur.com/lcjtww/2312126/2432763/index.html
- group: design
  title: ''
  type: DataModel
  url: data-model/inspur-cloud-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/inspur-cloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inspur-cloud-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/inspur-cloud-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inspur-cloud-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenInspur
created: '2026-08-23'
description: 'Inspur Cloud (浪潮云) is the public-cloud arm of the Chinese IT conglomerate Inspur Group, operating from cloud.inspur.com across the cn-north-3 (华北三), cn-south-1 (华南一) and cn-east-1 (华东一) regions. It publishes a broad IaaS/PaaS catalog — 94 products documented in its GitBook help centre — of which at least 16 ship a public HTTP API reference covering elastic compute (ECS), bare metal (CPS), block storage (EBS), backup (CBS), VPC networking, elastic IP, load balancing, IAM, RDS for MySQL, time-series database, container engine, blockchain and an S3-compatible object storage service (OSS). APIs are authenticated with an AK/SK request signature (x-secret-id / x-sign / x-time / x-random headers) or an IAM-issued bearer token. No OpenAPI, AsyncAPI or other machine-readable contract is published: the entire surface is hand-written HTML reference documentation in Simplified Chinese.'
image: https://cloud.inspur.com/cn/template/images/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: Inspur Cloud MCP Server
  slug: inspur-cloud-mcp-server
modified: '2026-08-23'
name: Inspur Cloud
nav: Providers
network: true
overview: 'Inspur Cloud publishes 18 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Infrastructure, Compute, Storage, and Networking.


  Inspur Cloud''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 22 more developer resources.'
plans:
- name: Inspur Cloud Plans Pricing
  plan_count: 0
  slug: inspur-cloud-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Inspur Cloud Rate Limits
  slug: inspur-cloud-rate-limits
score:
  band: thin
  composite: 32.8
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 28.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Inspur Cloud Authentication
  slug: inspur-cloud-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Inspur Cloud Domain Security
  slug: inspur-cloud-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Inspur Cloud Vulnerability Disclosure
  slug: inspur-cloud-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: inspur-cloud
tags:
- Cloud
- Infrastructure
- Compute
- Storage
- Networking
- Object Storage
- Identity
- Database
- Containers
- Internet of Things
- Blockchain
- China
- Company
website: https://cloud.inspur.com/
---
