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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Routeros Agentic Access
  operation_count: 35
  slug: routeros-agentic-access
  summary_line: 35 operations · 15 acting
api_count: 11
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
artifact_total: 29
collections:
- collection_type: open
  name: RouterOS REST API
  slug: open-routeros-rest-api
common:
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
overview: 'RouterOS publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Bridge API, DHCP API, DNS API, and 7 more. Tagged areas include Networking, Routers, Network Management, Firewall, and MikroTik.


  The RouterOS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  RouterOS''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Routeros Plans Pricing
  plan_count: 3
  slug: routeros-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Routeros Rate Limits
  slug: routeros-rate-limits
rules:
- name: RouterOS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: routeros-jsonschema-spectral-rules
- name: RouterOS API Rules
  rule_count: 10
  severity_counts:
    error: 0
    hint: 2
    info: 2
    warn: 6
  slug: routeros-rules
score:
  band: developing
  composite: 56.0
  delta: 5.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 75.8
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 50.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: rising
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
- Routers
- Network Management
- Firewall
- MikroTik
website: https://mikrotik.com
---
