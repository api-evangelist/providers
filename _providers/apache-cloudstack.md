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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Apache Cloudstack Agentic Access
  operation_count: 8
  slug: apache-cloudstack-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 4
apis:
- description: Network and IP address management operations.
  name: Apache CloudStack Networks API
  slug: apache-cloudstack-networks-api
- description: Virtual machine lifecycle management operations.
  name: Apache CloudStack Virtual Machines API
  slug: apache-cloudstack-virtual-machines-api
- description: Volume and snapshot storage management operations.
  name: Apache CloudStack Volumes API
  slug: apache-cloudstack-volumes-api
- description: Zone and availability zone management operations.
  name: Apache CloudStack Zones API
  slug: apache-cloudstack-zones-api
artifact_total: 53
collections:
- collection_type: postman
  name: Apache CloudStack Networks API
  slug: postman-apache-cloudstack-networks-api
- collection_type: postman
  name: Apache CloudStack Networks Virtual Machines API
  slug: postman-apache-cloudstack-virtual-machines-api
- collection_type: postman
  name: Apache CloudStack Networks Volumes API
  slug: postman-apache-cloudstack-volumes-api
- collection_type: postman
  name: Apache CloudStack Networks Zones API
  slug: postman-apache-cloudstack-zones-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apache-cloudstack/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-cloudstack-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-cloudstack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-cloudstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-cloudstack-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apachecloudstack
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/cloudstack
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudstack.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudstack.apache.org/en/latest/installguide/
- group: operate
  title: ''
  type: Support
  url: https://cloudstack.apache.org/community/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/apache/cloudstack/releases
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-cloudstack-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-cloudstack-vocabulary.yaml
created: '2026-03-16'
description: Apache CloudStack is an open-source cloud computing platform developed by the Apache Software Foundation for creating, managing, and deploying infrastructure cloud services. It provides a comprehensive IaaS platform supporting multiple hypervisors (KVM, VMware vSphere, XenServer) and a rich API for programmatic cloud resource management. CloudStack is used by service providers and enterprises to build public, private, and hybrid cloud environments with virtual machine management, networking, storage, and multi-tenancy features.
examples:
- key_count: 6
  name: Cloudstack Api Network Example
  slug: cloudstack-api-network-example
- key_count: 10
  name: Cloudstack Api Virtual Machine Example
  slug: cloudstack-api-virtual-machine-example
- key_count: 5
  name: Cloudstack Api Zone Example
  slug: cloudstack-api-zone-example
features:
- description: Full VM lifecycle management including deploy, start, stop, reboot, migrate, and destroy across multiple hypervisors.
  name: Virtual Machine Management
- description: Support for KVM, VMware vSphere, XenServer, and Hyper-V hypervisors within a single CloudStack deployment.
  name: Multi-Hypervisor Support
- description: Advanced networking with isolated networks, shared networks, VLANs, VPNs, and software-defined networking.
  name: Network Management
- description: Primary and secondary storage management with volume snapshots, templates, and ISOs.
  name: Storage Management
- description: Account and domain hierarchy for isolating resources between tenants, departments, and organizations.
  name: Multi-Tenancy
- description: Long-running operations return async job IDs that can be polled for completion status.
  name: Asynchronous API
- description: Stateful firewall rules for controlling inbound and outbound traffic to virtual machines.
  name: Security Groups
- description: Automatic scaling of VM instances in response to load conditions using configurable policies.
  name: Auto Scaling
- description: Comprehensive query-parameter-based REST API with HMAC-SHA1 authentication for programmatic cloud management.
  name: REST API
- description: Web-based management console for administrators and users to manage cloud resources visually.
  name: CloudStack UI
finops:
- name: Apache Cloudstack Finops
  service_category: API
  slug: apache-cloudstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-cloudstack.png
integrations:
- description: KVM hypervisor support for Linux-based compute clusters in CloudStack zones.
  name: KVM
- description: VMware vSphere integration for managing ESXi hosts and vCenter clusters via CloudStack.
  name: VMware vSphere
- description: Integration with Apache Cloudbridge for hybrid cloud connectivity between CloudStack and AWS.
  name: Apache Cloudbridge
- description: Ceph distributed storage integration for primary storage in CloudStack deployments.
  name: Ceph
- description: OpenDaylight SDN controller integration for software-defined networking in CloudStack.
  name: OpenDaylight
- description: HashiCorp Terraform CloudStack provider for infrastructure-as-code provisioning.
  name: Terraform
- description: Ansible CloudStack modules for automating VM provisioning and cloud management tasks.
  name: Ansible
json_schemas:
- name: AsyncJobResponse
  property_count: 2
  slug: cloudstack-api-async-job-response
- name: Network
  property_count: 6
  slug: cloudstack-api-network
- name: VirtualMachine
  property_count: 10
  slug: cloudstack-api-virtual-machine
- name: Volume
  property_count: 6
  slug: cloudstack-api-volume
- name: Zone
  property_count: 5
  slug: cloudstack-api-zone
json_structures:
- name: Cloudstack Api Async Job Response Structure
  property_count: 0
  slug: cloudstack-api-async-job-response-structure
- name: Cloudstack Api Network Structure
  property_count: 0
  slug: cloudstack-api-network-structure
- name: Cloudstack Api Virtual Machine Structure
  property_count: 0
  slug: cloudstack-api-virtual-machine-structure
- name: Cloudstack Api Volume Structure
  property_count: 0
  slug: cloudstack-api-volume-structure
- name: Cloudstack Api Zone Structure
  property_count: 0
  slug: cloudstack-api-zone-structure
jsonld:
- class_count: 6
  name: Apache Cloudstack Context
  property_count: 21
  slug: apache-cloudstack-context
layout: provider
modified: '2026-05-19'
name: Apache CloudStack
nav: Providers
network: true
overview: 'Apache CloudStack publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Networks API, Virtual Machines API, Volumes API, and 1 more. Tagged areas include Apache, Cloud, IaaS, Infrastructure, and Open Source.


  The Apache CloudStack catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache CloudStack''s developer surface includes authentication, documentation, getting-started guide, support, changelog, and 10 more developer resources.'
plans:
- name: Apache Cloudstack Plans Pricing
  plan_count: 3
  slug: apache-cloudstack-plans-pricing
random_paper: 100
rate_limits:
- limit_count: 5
  name: Apache Cloudstack Rate Limits
  slug: apache-cloudstack-rate-limits
rules:
- name: Apache CloudStack API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: apache-cloudstack-jsonschema-spectral-rules
- name: Apache CloudStack API Rules
  rule_count: 19
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 15
  slug: apache-cloudstack-spectral-rules
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 23.1
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-cloudstack/refs/heads/main/screenshots/apache-cloudstack-2026-06-20T172047.png
security:
- kind: authentication
  name: Apache Cloudstack Authentication
  slug: apache-cloudstack-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apache Cloudstack Domain Security
  slug: apache-cloudstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Cloudstack Vulnerability Disclosure
  slug: apache-cloudstack-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-cloudstack
tags:
- Apache
- Cloud
- IaaS
- Infrastructure
- Open Source
- Virtualization
use_cases:
- description: Build and operate public IaaS clouds for service providers offering compute, storage, and networking.
  name: Public Cloud Infrastructure
- description: Deploy private clouds for enterprise organizations needing isolated, on-premises infrastructure.
  name: Private Enterprise Cloud
- description: Extend on-premises CloudStack clouds to public cloud providers for burst capacity and disaster recovery.
  name: Hybrid Cloud Orchestration
- description: Host multi-tenant virtual server environments for managed service providers and resellers.
  name: Managed Service Provider Hosting
- description: Provision self-service development and testing environments on demand for engineering teams.
  name: Development and Test Environments
---
