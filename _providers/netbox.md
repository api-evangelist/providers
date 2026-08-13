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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 880
  human_in_the_loop: 1
  name: Netbox Agentic Access
  operation_count: 1167
  slug: netbox-agentic-access
  summary_line: 1167 operations · 880 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: A GraphQL API providing flexible querying capabilities for NetBox data with support for nested queries and custom field selection.
  name: NetBox GraphQL API
  slug: netbox-graphql-api
- description: The authentication-check API from NetBox — 1 operation(s) for authentication-check.
  name: NetBox authentication-check API
  slug: netbox-authentication-check-api
- description: The circuits API from NetBox — 24 operation(s) for circuits.
  name: NetBox circuits API
  slug: netbox-circuits-api
- description: The core API from NetBox — 21 operation(s) for core.
  name: NetBox core API
  slug: netbox-core-api
- description: The dcim API from NetBox — 99 operation(s) for dcim.
  name: NetBox dcim API
  slug: netbox-dcim-api
- description: The extras API from NetBox — 48 operation(s) for extras.
  name: NetBox extras API
  slug: netbox-extras-api
- description: The ipam API from NetBox — 41 operation(s) for ipam.
  name: NetBox ipam API
  slug: netbox-ipam-api
- description: The schema API from NetBox — 1 operation(s) for schema.
  name: NetBox schema API
  slug: netbox-schema-api
- description: The status API from NetBox — 1 operation(s) for status.
  name: NetBox status API
  slug: netbox-status-api
- description: The tenancy API from NetBox — 12 operation(s) for tenancy.
  name: NetBox tenancy API
  slug: netbox-tenancy-api
- description: The users API from NetBox — 14 operation(s) for users.
  name: NetBox users API
  slug: netbox-users-api
- description: The virtualization API from NetBox — 13 operation(s) for virtualization.
  name: NetBox virtualization API
  slug: netbox-virtualization-api
- description: The vpn API from NetBox — 20 operation(s) for vpn.
  name: NetBox vpn API
  slug: netbox-vpn-api
- description: The wireless API from NetBox — 6 operation(s) for wireless.
  name: NetBox wireless API
  slug: netbox-wireless-api
artifact_total: 22
collections:
- collection_type: open
  name: NetBox REST API
  slug: open-netbox
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/netbox-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netbox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/netbox-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netboxlabs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netbox-community
- group: operate
  title: ''
  type: Slack Community
  url: https://netdev.chat/
- group: company
  title: ''
  type: Blog
  url: https://netbox.dev/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.netbox.dev/en/stable/getting-started/
- group: build
  title: ''
  type: Plugins
  url: https://netbox.dev/plugins/
- group: start
  title: ''
  type: Demo Instance
  url: https://demo.netbox.dev/
created: '2024-01-15'
description: NetBox is the leading solution for modeling and documenting modern networks. By combining the traditional disciplines of IP address management (IPAM) and datacenter infrastructure management (DCIM) with powerful APIs and extensions, NetBox provides the ideal "source of truth" to power network automation.
finops:
- name: Netbox Finops
  service_category: API
  slug: netbox-finops
graphqls:
- description: A GraphQL API providing flexible querying capabilities for NetBox data with support for nested queries and custom field selection.
  name: NetBox GraphQL API
  slug: netbox-graphql
image: https://netbox.dev/static/img/netbox-logo.svg
layout: provider
modified: '2026-05-19'
name: NetBox
nav: Providers
network: true
overview: 'NetBox publishes 13 APIs on the [APIs.io](https://apis.io/) network, including authentication-check API, circuits API, core API, and 10 more. Tagged areas include Data Center, DCIM, Infrastructure as Code, IPAM, and Network Automation.


  NetBox''s developer surface includes authentication, engineering blog, getting-started guide, and 7 more developer resources.'
plans:
- name: Netbox Plans Pricing
  plan_count: 3
  slug: netbox-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 5
  name: Netbox Rate Limits
  slug: netbox-rate-limits
score:
  band: thin
  composite: 28.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 47.0
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 28.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netbox/refs/heads/main/screenshots/netbox-2026-08-07T184926.png
security:
- kind: authentication
  name: Netbox Authentication
  slug: netbox-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Netbox Domain Security
  slug: netbox-domain-security
  summary_line: TLSv1.3 · HSTS
slug: netbox
tags:
- Data Center
- DCIM
- Infrastructure as Code
- IPAM
- Network Automation
- Network Management
- Open Source
- Source of Truth
---
