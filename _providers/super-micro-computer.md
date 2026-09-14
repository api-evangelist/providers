---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 12
  human_in_the_loop: 2
  name: Super Micro Computer Agentic Access
  operation_count: 35
  slug: super-micro-computer-agentic-access
  summary_line: 35 operations · 12 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://{bmc-ip}/redfish/v1
  baseurl_source: declared
  description: User account management
  name: Super Micro Computer Accounts API
  slug: super-micro-computer-accounts-api
- baseURL: https://{bmc-ip}/redfish/v1
  baseurl_source: declared
  description: Chassis management including power and thermal
  name: Super Micro Computer Chassis API
  slug: super-micro-computer-chassis-api
- baseURL: https://{bmc-ip}/redfish/v1
  baseurl_source: declared
  description: Event subscription and notification management
  name: Super Micro Computer Event Service API
  slug: super-micro-computer-event-service-api
- baseURL: https://{bmc-ip}/redfish/v1
  baseurl_source: declared
  description: BMC manager configuration and management
  name: Super Micro Computer Managers API
  slug: super-micro-computer-managers-api
- baseURL: https://{bmc-ip}/redfish/v1
  baseurl_source: declared
  description: Network interface management
  name: Super Micro Computer Network API
  slug: super-micro-computer-network-api
- baseURL: https://{bmc-ip}/redfish/v1
  baseurl_source: declared
  description: Root service discovery and metadata
  name: Super Micro Computer Service Root API
  slug: super-micro-computer-service-root-api
- baseURL: https://{bmc-ip}/redfish/v1
  baseurl_source: declared
  description: Session authentication and management
  name: Super Micro Computer Sessions API
  slug: super-micro-computer-sessions-api
- baseURL: https://{bmc-ip}/redfish/v1
  baseurl_source: declared
  description: Storage controller and drive management
  name: Super Micro Computer Storage API
  slug: super-micro-computer-storage-api
- baseURL: https://{bmc-ip}/redfish/v1
  baseurl_source: declared
  description: Computer system management and health monitoring
  name: Super Micro Computer Systems API
  slug: super-micro-computer-systems-api
- baseURL: https://{bmc-ip}/redfish/v1
  baseurl_source: declared
  description: Firmware and BIOS update management
  name: Super Micro Computer Update Service API
  slug: super-micro-computer-update-service-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Supermicro Redfish Accounts API
  slug: open-super-micro-computer-accounts-api
- collection_type: open
  name: Supermicro Redfish Accounts Chassis API
  slug: open-super-micro-computer-chassis-api
- collection_type: open
  name: Supermicro Redfish Accounts Event Service API
  slug: open-super-micro-computer-event-service-api
- collection_type: open
  name: Supermicro Redfish Accounts Managers API
  slug: open-super-micro-computer-managers-api
- collection_type: open
  name: Supermicro Redfish Accounts Network API
  slug: open-super-micro-computer-network-api
- collection_type: open
  name: Supermicro Redfish Accounts Service Root API
  slug: open-super-micro-computer-service-root-api
- collection_type: open
  name: Supermicro Redfish Accounts Sessions API
  slug: open-super-micro-computer-sessions-api
- collection_type: open
  name: Supermicro Redfish Accounts Storage API
  slug: open-super-micro-computer-storage-api
- collection_type: open
  name: Supermicro Redfish Accounts Systems API
  slug: open-super-micro-computer-systems-api
- collection_type: open
  name: Supermicro Redfish Accounts Update Service API
  slug: open-super-micro-computer-update-service-api
- collection_type: open
  name: Supermicro Redfish API
  slug: open-supermicro-redfish
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/super-micro-computer-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/supermicro/redfish/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/supermicro/redfish/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/super-micro-computer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/super-micro-computer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/super-micro-computer-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/supermicro
- group: company
  title: ''
  type: Website
  url: https://www.supermicro.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.supermicro.com/en/solutions/management-software
- group: docs
  title: ''
  type: Documentation
  url: https://www.supermicro.com/manuals/other/redfish-ref-guide-html/Content/general-content/introduction.htm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/supermicro
- group: company
  title: ''
  type: Blog
  url: https://www.supermicro.com/en/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.supermicro.com/en/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.supermicro.com/en/products/servers
created: '2026-03-21'
description: Super Micro Computer (Supermicro) is a global leader in high-performance, high-efficiency server technology and innovation, providing complete server, storage, and networking solutions for data center, cloud, AI, and edge applications. Supermicro exposes its server management capabilities through the DMTF Redfish RESTful API standard, enabling programmatic management of servers, storage, and networking hardware via BMC.
examples:
- key_count: 2
  name: Supermicro Create Session Example
  slug: supermicro-create-session-example
- key_count: 2
  name: Supermicro Get System Example
  slug: supermicro-get-system-example
- key_count: 2
  name: Supermicro Reset System Example
  slug: supermicro-reset-system-example
finops:
- name: Super Micro Computer Finops
  service_category: API
  slug: super-micro-computer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/super-micro-computer.png
json_schemas:
- name: Supermicro Computer System
  property_count: 15
  slug: supermicro-computer-system
json_structures:
- name: Supermicro Computer System Structure
  property_count: 0
  slug: supermicro-computer-system-structure
jsonld:
- class_count: 11
  name: Super Micro Computer Context
  property_count: 14
  slug: super-micro-computer-context
layout: provider
modified: '2026-05-19'
name: Super Micro Computer
nav: Providers
network: true
overview: 'Super Micro Computer publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Chassis API, Event Service API, and 7 more. Tagged areas include Servers, Data-Center, Hardware, Server Management, and Redfish.


  The Super Micro Computer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Super Micro Computer''s developer surface includes authentication, documentation, engineering blog, support, pricing, and 9 more developer resources.'
plans:
- name: Super Micro Computer Plans Pricing
  plan_count: 3
  slug: super-micro-computer-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Super Micro Computer Rate Limits
  slug: super-micro-computer-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Super Micro Computer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: super-micro-computer-jsonschema-spectral-rules
- effective_rule_count: 10
  extends: []
  name: Super Micro Computer API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: supermicro-redfish-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/super-micro-computer/refs/heads/main/screenshots/super-micro-computer-2026-06-20T194706.png
security:
- kind: authentication
  name: Super Micro Computer Authentication
  slug: super-micro-computer-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Super Micro Computer Domain Security
  slug: super-micro-computer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: super-micro-computer
tags:
- Servers
- Data-Center
- Hardware
- Server Management
- Redfish
- BMC
- IPMI
- Fortune 500
- Infrastructure
- Cloud
website: https://www.supermicro.com
---
