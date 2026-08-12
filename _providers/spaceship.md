---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Spaceship Agentic Access
  operation_count: 40
  slug: spaceship-agentic-access
  summary_line: 40 operations · 23 acting
api_count: 10
apis:
- description: The Async Operations API from Spaceship — 1 operation(s) for async operations.
  name: Spaceship Async Operations API
  slug: spaceship-async-operations-api
- description: The Contacts API from Spaceship — 2 operation(s) for contacts.
  name: Spaceship Contacts API
  slug: spaceship-contacts-api
- description: The Contacts attributes API from Spaceship — 2 operation(s) for contacts attributes.
  name: Spaceship Contacts attributes API
  slug: spaceship-contacts-attributes-api
- description: The DNS records API from Spaceship — 1 operation(s) for dns records.
  name: Spaceship DNS records API
  slug: spaceship-dns-records-api
- description: The Domain Availability API from Spaceship — 2 operation(s) for domain availability.
  name: Spaceship Domain Availability API
  slug: spaceship-domain-availability-api
- description: The Domain Management API from Spaceship — 4 operation(s) for domain management.
  name: Spaceship Domain Management API
  slug: spaceship-domain-management-api
- description: The Domain Settings API from Spaceship — 5 operation(s) for domain settings.
  name: Spaceship Domain Settings API
  slug: spaceship-domain-settings-api
- description: The Domain Transfer API from Spaceship — 3 operation(s) for domain transfer.
  name: Spaceship Domain Transfer API
  slug: spaceship-domain-transfer-api
- description: The Personal Nameservers API from Spaceship — 2 operation(s) for personal nameservers.
  name: Spaceship Personal Nameservers API
  slug: spaceship-personal-nameservers-api
- description: The SellerHub API from Spaceship — 7 operation(s) for sellerhub.
  name: Spaceship SellerHub API
  slug: spaceship-sellerhub-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.spaceship.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.spaceship.com/application/api-manager/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spaceship.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spaceship.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spaceship.dev/
- group: operate
  title: ''
  type: Support
  url: https://www.spaceship.com/about/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spaceshipapp
- group: auth
  title: ''
  type: Authentication
  url: authentication/spaceship-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spaceship-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spaceship-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spaceship-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spaceship-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spaceship-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spaceship-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spaceship-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spaceship-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/spaceship-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spaceship-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/spaceship-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spaceship-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spaceship-agentic-access.yml
created: '2026-07-17'
description: Spaceship is a domain registrar and domain marketplace offering domain registration, DNS management, WHOIS privacy protection, and a SellerHub resale marketplace with SafePay escrow. Its public REST API (https://spaceship.dev/api, v1) exposes 40 operations across domain management, availability, settings, transfers, personal nameservers, contacts, DNS records, SellerHub, and asynchronous operations. Authentication uses a paired API key and secret (X-API-Key / X-API-Secret) with per-key scopes; long-running actions use an async-operation polling model (202 + a spaceship-async-operationid header polled at /v1/async-operations/{operationId}).
image: https://spaceship-cdn.com/spaceship-api-doc-assets/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: spaceship-mcp.yml
  slug: spaceship-mcpyml
modified: '2026-07-21'
name: Spaceship
nav: Providers
network: true
overview: 'Spaceship publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Async Operations API, Contacts API, Contacts attributes API, and 7 more. Tagged areas include Company, Domains, Domain Registrar, DNS, and Domain Marketplace.


  Spaceship''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 17 more developer resources.'
random_paper: 32
scopes:
- name: Spaceship Scopes
  scope_count: 11
  slug: spaceship-scopes
  summary_line: 11 scopes
score:
  band: thin
  composite: 36.4
  delta: -1.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 61.6
    developer_ergonomics: 53.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Spaceship Authentication
  slug: spaceship-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Spaceship Domain Security
  slug: spaceship-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: spaceship
tags:
- Company
- Domains
- Domain Registrar
- DNS
- Domain Marketplace
- Nameservers
- WHOIS
- Developer Tools
- API
website: https://www.spaceship.com/
---
