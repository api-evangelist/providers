---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The CNI specification defines the interface between container runtimes and network plugins. It specifies how runtimes invoke plugins via environment variables (CNI_COMMAND, CNI_CONTAINERID, CNI_NETNS,
  name: CNI Specification
  slug: cni-spec
- description: A collection of reference and example networking plugins maintained by the containernetworking team that implement the CNI specification. Includes main plugins such as bridge, ipvlan, macvlan, ptp, ho
  name: CNI Reference Plugins
  slug: cni-plugins
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cni-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cni.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cni.dev/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/containernetworking
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/containernetworking/cni
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/containernetworking/plugins
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cni-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cni-network-config-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cni-result-schema.json
created: '2026-03-16'
description: CNI (Container Network Interface) is a CNCF-incubating project that defines a specification and libraries for configuring network interfaces in Linux containers. It provides a simple exec/stdin interface between the container runtime and network implementation plugins, enabling pluggable networking for Kubernetes and other container orchestrators. The CNI spec defines four operations (ADD, DEL, CHECK, VERSION), a network configuration document format, and a plugin Result document. CNI also publishes a collection of reference plugins (bridge, ipvlan, macvlan, host-device, ptp, loopback) and meta-plugins (portmap, bandwidth, firewall, sbr).
finops:
- name: Cni Finops
  service_category: API
  slug: cni-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cni.png
json_schemas:
- name: CNI Network Configuration
  property_count: 11
  slug: cni-network-config
- name: CNI Plugin Result
  property_count: 5
  slug: cni-result
jsonld:
- class_count: 0
  name: Cni Context
  property_count: 11
  slug: cni-context
layout: provider
modified: '2026-04-23'
name: Container Network Interface (CNI)
nav: Providers
network: true
overview: 'Container Network Interface (CNI) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Native, Containers, Incubating, Kubernetes, and Networking.


  The Container Network Interface (CNI) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Container Network Interface (CNI)''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Cni Plans Pricing
  plan_count: 3
  slug: cni-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Cni Rate Limits
  slug: cni-rate-limits
rules:
- name: Container Network Interface (CNI) API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: cni-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.3
  delta: -4.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 29.0
    developer_ergonomics: 8.7
    discoverability: 66.7
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 39.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cni/refs/heads/main/screenshots/cni-2026-06-20T174634.png
security:
- kind: domain-security
  name: Cni Domain Security
  slug: cni-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cni
tags:
- Cloud Native
- Containers
- Incubating
- Kubernetes
- Networking
- Plugins
website: https://www.cni.dev/
---
