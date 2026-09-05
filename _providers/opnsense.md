---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Opnsense Agentic Access
  operation_count: 6
  slug: opnsense-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- description: REST API covering all core OPNsense modules including firewall, NAT, interfaces, VPN (IPsec, OpenVPN, WireGuard), routing, DHCP, DNS, users, and system administration. Authentication uses HTTP basic a
  name: OPNsense Core REST API
  slug: core-api
- baseURL: https://opnsense.local/api
  baseurl_source: declared
  description: Core OPNsense service controllers.
  name: OPNsense Core API
  slug: opnsense-core-api
- baseURL: https://opnsense.local/api
  baseurl_source: declared
  description: Interface and system diagnostics.
  name: OPNsense Diagnostics API
  slug: opnsense-diagnostics-api
- baseURL: https://opnsense.local/api
  baseurl_source: declared
  description: Firewall filter and aliases.
  name: OPNsense Firewall API
  slug: opnsense-firewall-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OPNsense REST Core API
  slug: open-opnsense-core-api
- collection_type: open
  name: OPNsense REST Core Diagnostics API
  slug: open-opnsense-diagnostics-api
- collection_type: open
  name: OPNsense REST Core Firewall API
  slug: open-opnsense-firewall-api
- collection_type: open
  name: OPNsense Core REST API
  slug: open-opnsense
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/opnsense-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opnsense-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opnsense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opnsense-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/opnsense
- group: company
  title: ''
  type: Website
  url: https://opnsense.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opnsense.org
- group: other
  title: ''
  type: Download
  url: https://opnsense.org/download/
- group: operate
  title: ''
  type: Forums
  url: https://forum.opnsense.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opnsense
- group: other
  title: ''
  type: Business Edition
  url: https://shop.opnsense.com
created: '2026-05-11'
description: OPNsense is an open source FreeBSD-based firewall and routing platform providing stateful packet filtering, VPN (IPsec, OpenVPN, WireGuard), intrusion detection (Suricata), traffic shaping, captive portal, and high availability for home, enterprise, and managed service provider deployments. The platform features a web UI, plugin ecosystem, and a comprehensive Business Edition. OPNsense exposes a REST API for managing every core module and plugin, using HTTP basic authentication with an API key and secret.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opnsense.png
layout: provider
modified: '2026-05-11'
name: OPNsense
nav: Providers
network: true
overview: 'OPNsense publishes 3 APIs on the [APIs.io](https://apis.io/) network: Core API, Diagnostics API, and Firewall API. Tagged areas include Firewall, Networking, Security, VPN, and Routing.


  OPNsense''s developer surface includes authentication, documentation, and 9 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 25.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opnsense/refs/heads/main/screenshots/opnsense-2026-06-20T191103.png
security:
- kind: authentication
  name: Opnsense Authentication
  slug: opnsense-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opnsense Domain Security
  slug: opnsense-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: opnsense
tags:
- Firewall
- Networking
- Security
- VPN
- Routing
- Open-Source
website: https://opnsense.org
---
