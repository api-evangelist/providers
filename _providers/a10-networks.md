---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 18.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Thunder Kubernetes Connector (TKC) runs inside Kubernetes and configures upstream Thunder ADC objects automatically as pods are created and scaled. It defines 24 CRDs covering VirtualServer, Virtu
  name: A10 Thunder Kubernetes Connector (TKC)
  slug: thunder-kubernetes-connector
- description: Session sign-on and sign-off
  name: A10 Networks Authentication API
  slug: a10-networks-authentication-api
- description: Active health probes attached to servers and service groups
  name: A10 Networks SLB Health Monitor API
  slug: a10-networks-slb-health-monitor-api
- description: Real backend servers
  name: A10 Networks SLB Server API
  slug: a10-networks-slb-server-api
- description: Service groups (pools) that bind real servers to a load-balancing method
  name: A10 Networks SLB Service Group API
  slug: a10-networks-slb-service-group-api
- description: Virtual servers (VIPs) that front pools of real servers
  name: A10 Networks SLB Virtual Server API
  slug: a10-networks-slb-virtual-server-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: A10 Networks ACOS aXAPI v3 Authentication API
  slug: open-a10-networks-authentication-api
- collection_type: open
  name: A10 Networks ACOS aXAPI v3 SLB Health Monitor API
  slug: open-a10-networks-slb-health-monitor-api
- collection_type: open
  name: A10 Networks ACOS aXAPI v3 SLB Server API
  slug: open-a10-networks-slb-server-api
- collection_type: open
  name: A10 Networks ACOS aXAPI v3 SLB Service Group API
  slug: open-a10-networks-slb-service-group-api
- collection_type: open
  name: A10 Networks ACOS aXAPI v3 SLB Virtual Server API
  slug: open-a10-networks-slb-virtual-server-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/a10-networks-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/a10-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.a10networks.com
- group: other
  title: ''
  type: Products
  url: https://www.a10networks.com/products/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.a10networks.com
- group: docs
  title: ''
  type: aXAPI Documentation
  url: https://documentation.a10networks.com/ACOS-Docs/axapi/702/start_here.html
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/a10networks
- group: other
  title: ''
  type: TerraformProvider
  url: https://github.com/a10networks/terraform-provider-thunder
- group: build
  title: ''
  type: AnsibleCollection
  url: https://github.com/a10networks/a10-acos-axapi
- group: build
  title: ''
  type: PythonClient
  url: https://github.com/a10networks/acos-client
- group: other
  title: ''
  type: KubernetesConnector
  url: https://github.com/a10networks/tkc-doc
- group: operate
  title: ''
  type: OpenStackOctavia
  url: https://github.com/a10networks/a10-octavia
- group: other
  title: ''
  type: PrometheusExporter
  url: https://github.com/a10networks/PrometheusExporter
- group: other
  title: ''
  type: AWSCloudFormation
  url: https://github.com/a10networks/AWS-CFT
- group: other
  title: ''
  type: AzureARMTemplates
  url: https://github.com/a10networks/A10-azure-arm-templates
- group: other
  title: ''
  type: VMwareTemplates
  url: https://github.com/a10networks/a10-vmware-templates
- group: other
  title: ''
  type: aFleXScripts
  url: https://github.com/a10networks/aflex-collection
- group: other
  title: ''
  type: HelmChart
  url: https://github.com/a10networks/acos-prometheus-exporter-helm-chart
- group: operate
  title: ''
  type: Support
  url: https://support.a10networks.com
- group: operate
  title: ''
  type: Community
  url: https://glm.a10networks.com
- group: company
  title: ''
  type: Blog
  url: https://www.a10networks.com/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://www.a10networks.com/news/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.a10networks.com
- group: company
  title: ''
  type: Careers
  url: https://www.a10networks.com/company/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.a10networks.com/contact-us/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/A10Networks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/a10networks
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/a10networks
- group: build
  title: ''
  type: GitHub
  url: https://github.com/a10networks
crds:
- name: A10IPPool
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/A10IPPool.yaml
- name: AccessListExtended
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/AccessListExtended.yaml
- name: AccessListStandard
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/AccessListStandard.yaml
- name: ActiveActiveHADevice
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/ActiveActiveHADevice.yaml
- name: ClientSsl
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/ClientSsl.yaml
- name: DeploymentConfig
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/DeploymentConfig.yaml
- name: HealthMonitor
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/HealthMonitor.yaml
- name: NatPool
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/NatPool.yaml
- name: ServerSsl
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/ServerSsl.yaml
- name: ServiceGroup
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/ServiceGroup.yaml
- name: TemplateCipher
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/TemplateCipher.yaml
- name: TemplateExternalService
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/TemplateExternalService.yaml
- name: TemplateHttp
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/TemplateHttp.yaml
- name: TemplateHttpPolicy
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/TemplateHttpPolicy.yaml
- name: TemplatePersistSourceIp
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/TemplatePersistSourceIp.yaml
- name: TemplatePolicy
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/TemplatePolicy.yaml
- name: TemplatePort
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/TemplatePort.yaml
- name: TemplateSlbServer
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/TemplateSlbServer.yaml
- name: TemplateTcp
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/TemplateTcp.yaml
- name: TemplateTcpProxy
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/TemplateTcpProxy.yaml
- name: TemplateUdp
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/TemplateUdp.yaml
- name: TemplateVirtualPort
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/TemplateVirtualPort.yaml
- name: VirtualPort
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/VirtualPort.yaml
- name: VirtualServer
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/VirtualServer.yaml
- name: a10 crd installation
  url: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/crd/a10-crd-installation.yaml
created: '2026-05-25'
description: 'A10 Networks (NYSE: ATEN) is a San Jose, California–headquartered application delivery and cybersecurity company founded in 2004 by Lee Chen. A10 builds the ACOS (Application Centric Operating System) software platform that powers its Thunder family of physical appliances, virtual machines (vThunder), and containerized form factors across hyperscalers and private clouds. The product line spans the Thunder ADC (Application Delivery Controller for L4–L7 server load balancing and GSLB), the Thunder TPS / A10 Defend portfolio (DDoS detection, mitigation, orchestration, and Threat Control SaaS) protecting service-provider and enterprise networks from volumetric and application-layer attacks, Thunder CGN (Carrier-Grade NAT and IPv4/IPv6 transition), Thunder CFW (consolidated firewall, VPN, CGN, and secure web gateway), SSL Insight for encrypted traffic decryption, the A10 Defend Next-Gen WAF (incorporating ThreatX), and the A10 AI Firewall for protecting LLM and AI application traffic.
  Every ACOS device exposes the aXAPI v3 — a RESTful HTTPS interface that is the primary configuration and operational control plane for the platform, supporting ACOS 4.0.0 through 7.0.2. The aXAPI surface is exhaustive (the official Terraform provider exposes 3,627 resources) and is wrapped by official Ansible collections (a10-acos-axapi, a10-acos-cli), a Python client (acos-client), the Thunder Kubernetes Connector (TKC, with 24 CRDs for pod-driven VIP automation), and integrations for OpenStack Octavia, Neutron LBaaS, AWS CloudFormation, Azure ARM, VMware vSphere, Helm, and Prometheus. A10 reported record annual revenue of $290.6M in FY2025 (up 11.0% year over year) under CEO Dhrupad Trivedi, serving 7,700+ customers across 117 countries.'
examples:
- key_count: 2
  name: A10 Networks Auth Example
  slug: a10-networks-auth-example
- key_count: 2
  name: A10 Networks Create Virtual Server Example
  slug: a10-networks-create-virtual-server-example
finops:
- name: A10 Networks Finops
  service_category: Networking and Security
  slug: a10-networks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/a10-networks.png
json_schemas:
- name: A10 ACOS Real Server
  property_count: 9
  slug: a10-networks-server
- name: A10 ACOS SLB Service Group
  property_count: 8
  slug: a10-networks-service-group
- name: A10 ACOS Virtual Server
  property_count: 7
  slug: a10-networks-virtual-server
json_structures:
- name: A10 Networks Virtual Server Structure
  property_count: 0
  slug: a10-networks-virtual-server-structure
jsonld:
- class_count: 0
  name: A10 Networks Context
  property_count: 5
  slug: a10-networks-context
layout: provider
modified: '2026-05-25'
name: A10 Networks
nav: Providers
network: true
overview: 'A10 Networks publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, SLB Health Monitor API, SLB Server API, and 2 more. Tagged areas include Application Delivery, Load Balancing, DDoS Protection, Application Delivery Controller, and Network Security.


  The A10 Networks catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  A10 Networks'' developer surface includes documentation, support, engineering blog, YouTube channel, GitHub presence, and 24 more developer resources.'
plans:
- name: A10 Networks Plans Pricing
  plan_count: 6
  slug: a10-networks-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: A10 Networks Rate Limits
  slug: a10-networks-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: A10 Networks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: a10-networks-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: A10 Networks API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: a10-networks-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 61.9
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 5.3
  previous_composite: 35.0
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/a10-networks/refs/heads/main/screenshots/a10-networks-2026-06-20T162934.png
security:
- kind: domain-security
  name: A10 Networks Domain Security
  slug: a10-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: a10-networks
tags:
- Application Delivery
- Load Balancing
- DDoS Protection
- Application Delivery Controller
- Network Security
- Web Application Firewall
- SSL Decryption
- CGNAT
- Cybersecurity
- Infrastructure
- Kubernetes
- Terraform
- Ansible
- REST API
- Networking
website: https://www.a10networks.com
---
