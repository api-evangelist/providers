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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Routeros Agentic Access
  operation_count: 35
  slug: routeros-agentic-access
  summary_line: 35 operations · 15 acting
api_count: 1
apis:
- description: 'The RouterOS TCP API is the native binary protocol for RouterOS, running on TCP port 8728 (standard) and TCP port 8729 (SSL/TLS). It uses a sentence-based word protocol with variable-length encoding, '
  name: RouterOS TCP API
  slug: routeros-tcp-api
- description: Bridge interface management
  name: RouterOS Bridge API
  slug: routeros-bridge-api
- description: DHCP server and client management
  name: RouterOS DHCP API
  slug: routeros-dhcp-api
- description: DNS cache and configuration
  name: RouterOS DNS API
  slug: routeros-dns-api
- description: Firewall rules, NAT, and address lists
  name: RouterOS Firewall API
  slug: routeros-firewall-api
- description: Network interface management
  name: RouterOS Interface API
  slug: routeros-interface-api
- description: IP address configuration and management
  name: RouterOS IP Address API
  slug: routeros-ip-address-api
- description: Routing tables, BGP, OSPF, and static routes
  name: RouterOS Routing API
  slug: routeros-routing-api
- description: System information, identity, and scripts
  name: RouterOS System API
  slug: routeros-system-api
- description: VPN tunnels and configurations
  name: RouterOS VPN API
  slug: routeros-vpn-api
- description: Wireless interface and station management
  name: RouterOS Wireless API
  slug: routeros-wireless-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RouterOS REST Bridge API
  slug: open-routeros-bridge-api
- collection_type: open
  name: RouterOS REST Bridge DHCP API
  slug: open-routeros-dhcp-api
- collection_type: open
  name: RouterOS REST Bridge DNS API
  slug: open-routeros-dns-api
- collection_type: open
  name: RouterOS REST Bridge Firewall API
  slug: open-routeros-firewall-api
- collection_type: open
  name: RouterOS REST Bridge Interface API
  slug: open-routeros-interface-api
- collection_type: open
  name: RouterOS REST Bridge IP Address API
  slug: open-routeros-ip-address-api
- collection_type: open
  name: RouterOS REST API
  slug: open-routeros-rest-api
- collection_type: open
  name: RouterOS REST Bridge Routing API
  slug: open-routeros-routing-api
- collection_type: open
  name: RouterOS REST Bridge System API
  slug: open-routeros-system-api
- collection_type: open
  name: RouterOS REST Bridge VPN API
  slug: open-routeros-vpn-api
- collection_type: open
  name: RouterOS REST Bridge Wireless API
  slug: open-routeros-wireless-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/routeros-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/routeros-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/routeros-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/routeros-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/routeros-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mikrotik.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.mikrotik.com/docs/spaces/ROS
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/mikrotik
- group: operate
  title: ''
  type: Forums
  url: https://forum.mikrotik.com
- group: other
  title: ''
  type: Wiki
  url: https://wiki.mikrotik.com
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/vocabulary/routeros-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/json-ld/routeros-context.jsonld
created: '2024-11-07'
description: RouterOS is MikroTik's powerful network operating system designed for managing routers, switches, access points, and other network devices. It provides a comprehensive REST API (v7.1+) and a TCP-based binary API for programmatic management of IP addresses, interfaces, firewall rules, routing, VPN configurations, DHCP, DNS, and system resources. RouterOS powers MikroTik hardware and can also be deployed as a virtual machine (CHR).
examples:
- key_count: 4
  name: Routeros Get System Resource Example
  slug: routeros-get-system-resource-example
- key_count: 4
  name: Routeros List Firewall Filters Example
  slug: routeros-list-firewall-filters-example
- key_count: 4
  name: Routeros List Ip Addresses Example
  slug: routeros-list-ip-addresses-example
finops:
- name: Routeros Finops
  service_category: API
  slug: routeros-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/routeros.png
json_schemas:
- name: RouterOS Firewall Filter Rule
  property_count: 15
  slug: routeros-firewall-filter
- name: RouterOS Interface
  property_count: 8
  slug: routeros-interface
- name: RouterOS IP Address
  property_count: 7
  slug: routeros-ip-address
json_structures:
- name: Routeros Ip Address Structure
  property_count: 0
  slug: routeros-ip-address-structure
jsonld:
- class_count: 0
  name: Routeros Context
  property_count: 24
  slug: routeros-context
layout: provider
modified: '2026-05-19'
name: RouterOS
nav: Providers
network: true
overview: 'RouterOS publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Bridge API, DHCP API, DNS API, and 7 more. Tagged areas include Networking, Router, Network Management, Firewall, and MikroTik.


  The RouterOS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  RouterOS''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Routeros Plans Pricing
  plan_count: 3
  slug: routeros-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Routeros Rate Limits
  slug: routeros-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: RouterOS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: routeros-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: RouterOS API Rules
  rule_count: 10
  severity_counts:
    error: 0
    hint: 2
    info: 2
    warn: 6
  slug: routeros-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 41.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 67.1
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/screenshots/routeros-2026-06-20T193227.png
security:
- kind: authentication
  name: Routeros Authentication
  slug: routeros-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Routeros Domain Security
  slug: routeros-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Routeros Vulnerability Disclosure
  slug: routeros-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: routeros
tags:
- Networking
- Router
- Network Management
- Firewall
- MikroTik
website: https://mikrotik.com
---
