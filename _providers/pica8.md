---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.1
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: JSON REST API on the customer-deployed AmpCon controller. A JWT bearer token is minted from POST /token by a superadmin user and carried in the Authorization header on every call. The API covers Jinja
  name: Pica8 AmpCon Network Controller API
  slug: pica8-ampcon-network-controller-api
- description: Standards-based on-device programmability in the PICOS network operating system. RESTCONF (RFC 8040) exposes OPTIONS/HEAD/GET/POST/PATCH/PUT/DELETE over YANG-modelled configuration and state at /restc
  name: PICOS RESTCONF / NETCONF / gNMI Device API
  slug: picos-restconf-netconf-gnmi-device-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pica8-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pica8.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pica8-fs.atlassian.net/wiki
- group: docs
  title: ''
  type: Documentation
  url: https://pica8-fs.atlassian.net/wiki
- group: docs
  title: ''
  type: APIReference
  url: https://pica8-fs.atlassian.net/wiki/spaces/ampcon/pages/753668/AmpCon+API+document
- group: operate
  title: ''
  type: Support
  url: https://www.pica8.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.pica8.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.pica8.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pica8
- group: start
  title: ''
  type: Login
  url: https://www.pica8.com/partners/portal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pica8.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pica8.com/support/warranty-and-agreements/
- group: other
  title: ''
  type: Products
  url: https://www.pica8.com/products/
- group: other
  title: ''
  type: Resources
  url: https://www.pica8.com/resources/
- group: operate
  title: ''
  type: Contact
  url: https://www.pica8.com/contact/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/pica8-ampcon-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/pica8-ampcon-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pica8-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pica8-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pica8-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pica8-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pica8-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pica8-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pica8-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/pica8-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pica8-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pica8-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/pica8-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pica8-rate-limits.yml
- group: build
  title: ''
  type: CLI
  url: cli/pica8-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: 'Pica8 is a Palo Alto, California open-networking software company, first to market with a commercial SDN network operating system in 2012. It publishes PICOS, a Debian-Linux-based network operating system that runs on third-party white-box and brite-box switches (Edgecore, UfiSpace, FS and others), and AmpCon, a centralized controller that automates zero-touch provisioning, configuration templating, image upgrade, licensing and Ansible playbook execution across a fleet of PICOS switches. PICOS exposes standards-based programmatic interfaces on the device itself - RESTCONF over YANG-modelled datastores, NETCONF with get/get-config/get-schema/edit-config, gNMI-over-gRPC streaming telemetry, sFlow v5, OpenFlow 1.3/1.4 and OVSDB in CrossFlow mode - while AmpCon exposes a JWT-authenticated JSON REST API covering templates, global and per-switch configuration, backup and rollback, switch lifecycle (stage/import/DECOM/RMA/upgrade), grouping, licensing, settings and Ansible playbooks
  and jobs. Both are customer-deployed: there is no Pica8-hosted API endpoint, so every base URL is the operator''s own controller or switch address.'
image: https://www.pica8.com/images/pica8-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Pica8 MCP Server
  slug: pica8-mcp-server
modified: '2026-08-26'
name: Pica8
nav: Providers
network: true
overview: 'Pica8 publishes 1 API on the [APIs.io](https://apis.io/) network: AmpCon Network Controller API. Tagged areas include Networking, Open Networking, Software Defined Networking, Network Automation, and Network Operating System.


  Pica8''s developer surface includes documentation, API reference, support, engineering blog, authentication, changelog, CLI, and 24 more developer resources.'
plans:
- name: Pica8 Plans Pricing
  plan_count: 0
  slug: pica8-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Pica8 Rate Limits
  slug: pica8-rate-limits
score:
  band: thin
  composite: 33.6
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 30.3
    contract_quality: 13.1
    developer_ergonomics: 54.2
    discoverability: 79.6
    governance: 30.3
    operational_transparency: 18.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Pica8 Authentication
  slug: pica8-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Pica8 Domain Security
  slug: pica8-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: pica8
tags:
- Networking
- Open Networking
- Software Defined Networking
- Network Automation
- Network Operating System
- White Box Switching
- Network Management
- Campus Networking
- Data Center Networking
- RESTCONF
- NETCONF
- Telemetry
website: https://www.pica8.com/
---
