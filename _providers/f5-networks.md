---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: F5 Networks Agentic Access
  operation_count: 32
  slug: f5-networks-agentic-access
  summary_line: 32 operations · 16 acting
api_count: 14
apis:
- description: REST API for managing NGINX instances, monitoring performance, and configuring application delivery through NGINX Management Suite.
  name: F5 NGINX Management Suite API
  slug: f5-nginx-management-suite-api
- description: API for managing F5's application security services including WAF policies, bot defense, and API protection.
  name: F5 Essential App Protect API
  slug: f5-essential-app-protect-api
- description: REST API for BIG-IQ Centralized Management providing programmatic control over BIG-IP device management, licensing, monitoring, and analytics across your F5 infrastructure.
  name: F5 BIG-IQ Centralized Management API
  slug: f5-big-iq-centralized-management-api
- description: Declarative API for automating layer 4-7 application services on BIG-IP using JSON declarations. AS3 enables infrastructure-as-code for application delivery configuration.
  name: F5 BIG-IP Application Services 3 Extension API
  slug: f5-big-ip-application-services-3-extension-api
- description: Declarative API for automating layer 1-3 BIG-IP onboarding and initial device configuration using JSON declarations, making BIG-IP available on the network and ready for application services.
  name: F5 Declarative Onboarding API
  slug: f5-declarative-onboarding-api
- description: Declarative API for aggregating, normalizing, and forwarding BIG-IP statistics and events to third-party analytics consumers including Splunk, Azure Log Analytics, AWS CloudWatch, and more.
  name: F5 Telemetry Streaming API
  slug: f5-telemetry-streaming-api
- description: REST API for NGINX Plus providing real-time live activity monitoring, dynamic upstream configuration, key-value store management, and server health statistics without requiring configuration reloads.
  name: F5 NGINX Plus API
  slug: f5-nginx-plus-api
- description: API for managing and monitoring NGINX instances across environments from a single console, including configuration management, performance metrics, security vulnerability tracking, and SSL certificate
  name: F5 NGINX One Console API
  slug: f5-nginx-one-console-api
- description: Kubernetes Ingress Controller implementation for NGINX and NGINX Plus providing load balancing, SSL/TLS termination, content-based routing, and advanced traffic management for containerized applicatio
  name: F5 NGINX Ingress Controller API
  slug: f5-nginx-ingress-controller-api
- description: Manage nodes representing individual backend servers by IP address or FQDN.
  name: F5 Networks Nodes API
  slug: f5-networks-nodes-api
- description: Manage individual members within a pool, including their health status, session state, and load balancing weight.
  name: F5 Networks Pool Members API
  slug: f5-networks-pool-members-api
- description: Manage pools of backend servers for load distribution and health monitoring.
  name: F5 Networks Pools API
  slug: f5-networks-pools-api
- description: Manage profiles that define traffic handling behavior for virtual servers, including HTTP, TCP, UDP, client SSL, and persistence profiles.
  name: F5 Networks Profiles API
  slug: f5-networks-profiles-api
- description: Manage virtual servers that direct client traffic to appropriate server pools based on configured rules and profiles.
  name: F5 Networks Virtual Servers API
  slug: f5-networks-virtual-servers-api
artifact_total: 157
collections:
- collection_type: postman
  name: F5 BIG-IP iControl REST Nodes API
  slug: postman-f5-networks-nodes-api
- collection_type: postman
  name: F5 BIG-IP iControl REST Nodes Pool Members API
  slug: postman-f5-networks-pool-members-api
- collection_type: postman
  name: F5 BIG-IP iControl REST Nodes Pools API
  slug: postman-f5-networks-pools-api
- collection_type: postman
  name: F5 BIG-IP iControl REST Nodes Profiles API
  slug: postman-f5-networks-profiles-api
- collection_type: postman
  name: F5 BIG-IP iControl REST Nodes Virtual Servers API
  slug: postman-f5-networks-virtual-servers-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: F5 BIG-IP iControl REST API
  slug: open-bigip-icontrol-rest
- collection_type: open
  name: F5 BIG-IP iControl REST Nodes API
  slug: open-f5-networks-nodes-api
- collection_type: open
  name: F5 BIG-IP iControl REST Nodes Pool Members API
  slug: open-f5-networks-pool-members-api
- collection_type: open
  name: F5 BIG-IP iControl REST Nodes Pools API
  slug: open-f5-networks-pools-api
- collection_type: open
  name: F5 BIG-IP iControl REST Nodes Profiles API
  slug: open-f5-networks-profiles-api
- collection_type: open
  name: F5 BIG-IP iControl REST Nodes Virtual Servers API
  slug: open-f5-networks-virtual-servers-api
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/F5Networks/f5-appsvcs-extension/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/F5Networks/f5-appsvcs-extension/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/f5-networks/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/f5-networks-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/f5-networks-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/f5-networks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/f5-networks-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nginx.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://clouddocs.f5.com/
- group: company
  title: ''
  type: Blog
  url: https://www.f5.com/company/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/F5Networks
- group: build
  title: F5 DevCentral
  type: GitHubOrganization
  url: https://github.com/f5devcentral/
- group: operate
  title: ''
  type: Support
  url: https://support.f5.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.f5cloudstatus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.f5.com/company/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.f5.com/company/policies/privacy-notice
- group: start
  title: ''
  type: Signup
  url: https://account.f5.com/myf5
- group: start
  title: ''
  type: Login
  url: https://identity.account.f5.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/f5
- group: other
  title: ''
  type: X
  url: https://twitter.com/f5networks
- group: learn
  title: ''
  type: YouTube
  url: https://www.f5.com/resources/videos
created: '2024'
description: F5 Networks is a leader in application delivery networking technology that specializes in application availability, acceleration, and security solutions.
examples:
- key_count: 21
  name: Bigip Icontrol Rest Client Ssl Profile Example
  slug: bigip-icontrol-rest-client-ssl-profile-example
- key_count: 22
  name: Bigip Icontrol Rest Cookie Persistence Profile Example
  slug: bigip-icontrol-rest-cookie-persistence-profile-example
- key_count: 4
  name: Bigip Icontrol Rest Error Response Example
  slug: bigip-icontrol-rest-error-response-example
- key_count: 26
  name: Bigip Icontrol Rest Http Profile Example
  slug: bigip-icontrol-rest-http-profile-example
- key_count: 9
  name: Bigip Icontrol Rest Node Create Example
  slug: bigip-icontrol-rest-node-create-example
- key_count: 18
  name: Bigip Icontrol Rest Node Example
  slug: bigip-icontrol-rest-node-example
- key_count: 8
  name: Bigip Icontrol Rest Node Update Example
  slug: bigip-icontrol-rest-node-update-example
- key_count: 10
  name: Bigip Icontrol Rest Pool Create Example
  slug: bigip-icontrol-rest-pool-create-example
- key_count: 27
  name: Bigip Icontrol Rest Pool Example
  slug: bigip-icontrol-rest-pool-example
- key_count: 10
  name: Bigip Icontrol Rest Pool Member Create Example
  slug: bigip-icontrol-rest-pool-member-create-example
- key_count: 19
  name: Bigip Icontrol Rest Pool Member Example
  slug: bigip-icontrol-rest-pool-member-example
- key_count: 8
  name: Bigip Icontrol Rest Pool Member Update Example
  slug: bigip-icontrol-rest-pool-member-update-example
- key_count: 8
  name: Bigip Icontrol Rest Pool Update Example
  slug: bigip-icontrol-rest-pool-update-example
- key_count: 25
  name: Bigip Icontrol Rest Tcp Profile Example
  slug: bigip-icontrol-rest-tcp-profile-example
- key_count: 18
  name: Bigip Icontrol Rest Virtual Server Create Example
  slug: bigip-icontrol-rest-virtual-server-create-example
- key_count: 35
  name: Bigip Icontrol Rest Virtual Server Example
  slug: bigip-icontrol-rest-virtual-server-example
- key_count: 21
  name: Bigip Icontrol Rest Virtual Server Update Example
  slug: bigip-icontrol-rest-virtual-server-update-example
- key_count: 6
  name: F5 Networks Addpoolmember Example
  slug: f5-networks-addpoolmember-example
- key_count: 6
  name: F5 Networks Createnode Example
  slug: f5-networks-createnode-example
- key_count: 6
  name: F5 Networks Createpool Example
  slug: f5-networks-createpool-example
- key_count: 6
  name: F5 Networks Createvirtualserver Example
  slug: f5-networks-createvirtualserver-example
- key_count: 6
  name: F5 Networks Getclientsslprofile Example
  slug: f5-networks-getclientsslprofile-example
- key_count: 6
  name: F5 Networks Getcookiepersistenceprofile Example
  slug: f5-networks-getcookiepersistenceprofile-example
- key_count: 6
  name: F5 Networks Gethttpprofile Example
  slug: f5-networks-gethttpprofile-example
- key_count: 6
  name: F5 Networks Getnode Example
  slug: f5-networks-getnode-example
- key_count: 6
  name: F5 Networks Getpool Example
  slug: f5-networks-getpool-example
- key_count: 6
  name: F5 Networks Getpoolmember Example
  slug: f5-networks-getpoolmember-example
- key_count: 6
  name: F5 Networks Gettcpprofile Example
  slug: f5-networks-gettcpprofile-example
- key_count: 6
  name: F5 Networks Getvirtualserver Example
  slug: f5-networks-getvirtualserver-example
- key_count: 6
  name: F5 Networks Listclientsslprofiles Example
  slug: f5-networks-listclientsslprofiles-example
- key_count: 6
  name: F5 Networks Listcookiepersistenceprofiles Example
  slug: f5-networks-listcookiepersistenceprofiles-example
- key_count: 6
  name: F5 Networks Listhttpprofiles Example
  slug: f5-networks-listhttpprofiles-example
- key_count: 6
  name: F5 Networks Listnodes Example
  slug: f5-networks-listnodes-example
- key_count: 6
  name: F5 Networks Listpoolmembers Example
  slug: f5-networks-listpoolmembers-example
- key_count: 6
  name: F5 Networks Listpools Example
  slug: f5-networks-listpools-example
- key_count: 6
  name: F5 Networks Listtcpprofiles Example
  slug: f5-networks-listtcpprofiles-example
- key_count: 6
  name: F5 Networks Listvirtualservers Example
  slug: f5-networks-listvirtualservers-example
- key_count: 6
  name: F5 Networks Patchnode Example
  slug: f5-networks-patchnode-example
- key_count: 6
  name: F5 Networks Patchpool Example
  slug: f5-networks-patchpool-example
- key_count: 6
  name: F5 Networks Patchpoolmember Example
  slug: f5-networks-patchpoolmember-example
- key_count: 6
  name: F5 Networks Patchvirtualserver Example
  slug: f5-networks-patchvirtualserver-example
- key_count: 6
  name: F5 Networks Updatenode Example
  slug: f5-networks-updatenode-example
- key_count: 6
  name: F5 Networks Updatepool Example
  slug: f5-networks-updatepool-example
- key_count: 6
  name: F5 Networks Updatepoolmember Example
  slug: f5-networks-updatepoolmember-example
- key_count: 6
  name: F5 Networks Updatevirtualserver Example
  slug: f5-networks-updatevirtualserver-example
features:
- description: Connect and secure applications across any cloud, data center, or edge environment with consistent policy and visibility.
  name: Multi-Cloud Networking
- description: Advanced load balancing, traffic management, and application acceleration for high availability and performance.
  name: Application Delivery Controller
- description: Comprehensive protection against OWASP Top 10 threats, bot attacks, and API vulnerabilities.
  name: Web Application Firewall
- description: Declarative APIs (AS3, DO, TS) for automating BIG-IP configuration and application delivery.
  name: Infrastructure as Code
- description: High-performance reverse proxy, load balancing, and web serving for modern applications.
  name: NGINX Reverse Proxy
- description: Secure and manage API traffic with rate limiting, authentication, and traffic shaping.
  name: API Gateway
- description: Volumetric and application-layer DDoS mitigation with always-on or on-demand protection.
  name: DDoS Protection
- description: Centralized SSL/TLS certificate management and encryption offloading for improved performance.
  name: SSL/TLS Offloading
finops:
- name: F5 Networks Finops
  service_category: Application Delivery / Multi-Cloud Security
  slug: f5-networks-finops
image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
integrations:
- description: Deploy BIG-IP and Distributed Cloud services natively on AWS with CloudFormation templates and marketplace offerings.
  name: AWS
- description: Integrate F5 solutions with Azure services including AKS, App Gateway, and Azure AD for cloud-native security.
  name: Azure
- description: Deploy F5 solutions on GCP with support for GKE, Cloud Load Balancing, and Anthos.
  name: Google Cloud
- description: Native Kubernetes integration through NGINX Ingress Controller, Container Ingress Services, and Helm charts.
  name: Kubernetes
- description: Infrastructure as Code support with official Terraform providers for BIG-IP and Distributed Cloud.
  name: Terraform
- description: Ansible modules and roles for automating BIG-IP configuration, deployment, and orchestration.
  name: Ansible
- description: Forward telemetry data to Splunk for centralized logging, analytics, and security monitoring.
  name: Splunk
- description: ITSM integration for automated incident management and change control of F5 infrastructure.
  name: ServiceNow
json_schemas:
- name: ClientSslProfile
  property_count: 21
  slug: bigip-icontrol-rest-client-ssl-profile
- name: CookiePersistenceProfile
  property_count: 22
  slug: bigip-icontrol-rest-cookie-persistence-profile
- name: ErrorResponse
  property_count: 4
  slug: bigip-icontrol-rest-error-response
- name: HttpProfile
  property_count: 26
  slug: bigip-icontrol-rest-http-profile
- name: NodeCreate
  property_count: 9
  slug: bigip-icontrol-rest-node-create
- name: Node
  property_count: 18
  slug: bigip-icontrol-rest-node
- name: NodeUpdate
  property_count: 8
  slug: bigip-icontrol-rest-node-update
- name: PoolCreate
  property_count: 10
  slug: bigip-icontrol-rest-pool-create
- name: PoolMemberCreate
  property_count: 10
  slug: bigip-icontrol-rest-pool-member-create
- name: PoolMember
  property_count: 19
  slug: bigip-icontrol-rest-pool-member
- name: PoolMemberUpdate
  property_count: 8
  slug: bigip-icontrol-rest-pool-member-update
- name: Pool
  property_count: 27
  slug: bigip-icontrol-rest-pool
- name: PoolUpdate
  property_count: 8
  slug: bigip-icontrol-rest-pool-update
- name: TcpProfile
  property_count: 25
  slug: bigip-icontrol-rest-tcp-profile
- name: VirtualServerCreate
  property_count: 18
  slug: bigip-icontrol-rest-virtual-server-create
- name: VirtualServer
  property_count: 35
  slug: bigip-icontrol-rest-virtual-server
- name: VirtualServerUpdate
  property_count: 21
  slug: bigip-icontrol-rest-virtual-server-update
- name: ClientSslProfile
  property_count: 21
  slug: f5-networks-clientsslprofile
- name: CookiePersistenceProfile
  property_count: 22
  slug: f5-networks-cookiepersistenceprofile
- name: ErrorResponse
  property_count: 4
  slug: f5-networks-errorresponse
- name: HttpProfile
  property_count: 26
  slug: f5-networks-httpprofile
- name: Node
  property_count: 18
  slug: f5-networks-node
- name: NodeCreate
  property_count: 9
  slug: f5-networks-nodecreate
- name: NodeUpdate
  property_count: 8
  slug: f5-networks-nodeupdate
- name: Pool
  property_count: 27
  slug: f5-networks-pool
- name: PoolCreate
  property_count: 10
  slug: f5-networks-poolcreate
- name: PoolMember
  property_count: 19
  slug: f5-networks-poolmember
- name: PoolMemberCreate
  property_count: 10
  slug: f5-networks-poolmembercreate
- name: PoolMemberUpdate
  property_count: 8
  slug: f5-networks-poolmemberupdate
- name: PoolUpdate
  property_count: 8
  slug: f5-networks-poolupdate
- name: TcpProfile
  property_count: 25
  slug: f5-networks-tcpprofile
- name: VirtualServer
  property_count: 35
  slug: f5-networks-virtualserver
- name: VirtualServerCreate
  property_count: 18
  slug: f5-networks-virtualservercreate
- name: VirtualServerUpdate
  property_count: 21
  slug: f5-networks-virtualserverupdate
- name: F5 BIG-IP Virtual Server
  property_count: 37
  slug: f5-virtual-server
json_structures:
- name: Bigip Icontrol Rest Client Ssl Profile Structure
  property_count: 21
  slug: bigip-icontrol-rest-client-ssl-profile-structure
- name: Bigip Icontrol Rest Cookie Persistence Profile Structure
  property_count: 22
  slug: bigip-icontrol-rest-cookie-persistence-profile-structure
- name: Bigip Icontrol Rest Error Response Structure
  property_count: 4
  slug: bigip-icontrol-rest-error-response-structure
- name: Bigip Icontrol Rest Http Profile Structure
  property_count: 26
  slug: bigip-icontrol-rest-http-profile-structure
- name: Bigip Icontrol Rest Node Create Structure
  property_count: 9
  slug: bigip-icontrol-rest-node-create-structure
- name: Bigip Icontrol Rest Node Structure
  property_count: 18
  slug: bigip-icontrol-rest-node-structure
- name: Bigip Icontrol Rest Node Update Structure
  property_count: 8
  slug: bigip-icontrol-rest-node-update-structure
- name: Bigip Icontrol Rest Pool Create Structure
  property_count: 10
  slug: bigip-icontrol-rest-pool-create-structure
- name: Bigip Icontrol Rest Pool Member Create Structure
  property_count: 10
  slug: bigip-icontrol-rest-pool-member-create-structure
- name: Bigip Icontrol Rest Pool Member Structure
  property_count: 19
  slug: bigip-icontrol-rest-pool-member-structure
- name: Bigip Icontrol Rest Pool Member Update Structure
  property_count: 8
  slug: bigip-icontrol-rest-pool-member-update-structure
- name: Bigip Icontrol Rest Pool Structure
  property_count: 27
  slug: bigip-icontrol-rest-pool-structure
- name: Bigip Icontrol Rest Pool Update Structure
  property_count: 8
  slug: bigip-icontrol-rest-pool-update-structure
- name: Bigip Icontrol Rest Tcp Profile Structure
  property_count: 25
  slug: bigip-icontrol-rest-tcp-profile-structure
- name: Bigip Icontrol Rest Virtual Server Create Structure
  property_count: 18
  slug: bigip-icontrol-rest-virtual-server-create-structure
- name: Bigip Icontrol Rest Virtual Server Structure
  property_count: 35
  slug: bigip-icontrol-rest-virtual-server-structure
- name: Bigip Icontrol Rest Virtual Server Update Structure
  property_count: 21
  slug: bigip-icontrol-rest-virtual-server-update-structure
- name: F5 Networks Structure
  property_count: 0
  slug: f5-networks-structure
jsonld:
- class_count: 0
  name: Bigip Icontrol Rest Context
  property_count: 0
  slug: bigip-icontrol-rest-context
- class_count: 0
  name: F5 Networks Context
  property_count: 6
  slug: f5-networks-context
layout: provider
modified: '2026-05-19'
name: F5 Networks
nav: Providers
network: true
overview: 'F5 Networks publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Nodes API, Pool Members API, Pools API, and 2 more. Tagged areas include API Gateway, Application Delivery, Automation, Edge Computing, and Kubernetes.


  The F5 Networks catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  F5 Networks'' developer surface includes authentication, documentation, engineering blog, support, signup flow, YouTube channel, and 15 more developer resources.'
plans:
- name: F5 Networks Plans Pricing
  plan_count: 5
  slug: f5-networks-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: F5 Networks Rate Limits
  slug: f5-networks-rate-limits
rules:
- name: F5 Networks API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: f5-networks-jsonschema-spectral-rules
- name: F5 Networks API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 7
  slug: f5-networks-spectral-rules
score:
  band: strong
  composite: 56.9
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 69.8
    developer_ergonomics: 39.1
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 44.7
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/f5-networks/refs/heads/main/screenshots/f5-networks-2026-06-20T180959.png
security:
- kind: authentication
  name: F5 Networks Authentication
  slug: f5-networks-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: F5 Networks Domain Security
  slug: f5-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: F5 Networks Trust Center
  slug: f5-networks-trust-center
  summary_line: PCI DSS, GDPR
slug: f5-networks
tags:
- API Gateway
- Application Delivery
- Automation
- Edge Computing
- Kubernetes
- Load Balancing
- Multi-Cloud
- NGINX
- Security
- WAF
use_cases:
- description: Distribute application traffic across servers for high availability, performance, and fault tolerance.
  name: Application Load Balancing
- description: Implement zero trust architecture with identity-aware proxy, micro-segmentation, and continuous verification.
  name: Zero Trust Security
- description: Manage ingress traffic for containerized applications with NGINX Ingress Controller in Kubernetes clusters.
  name: Kubernetes Ingress
- description: Deliver applications consistently across AWS, Azure, GCP, and on-premises with unified policy management.
  name: Multi-Cloud Application Delivery
- description: Protect APIs from abuse, injection attacks, and unauthorized access with granular security policies.
  name: API Security
- description: Automate network and security infrastructure provisioning using declarative APIs and CI/CD pipelines.
  name: DevOps Automation
website: https://clouddocs.f5.com/
---
