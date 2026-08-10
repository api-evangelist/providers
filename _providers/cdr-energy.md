---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-10'
api_count: 6
apis:
- description: The ACCC-operated Consumer Data Right Register, the ecosystem's source of truth for who is allowed to participate. Unauthenticated endpoints return the energy data holder brand summary (84 brands with
  name: CDR Register API
  slug: cdr-register-api
- description: The mandated energy data contract that every designated Australian electricity retailer must implement identically. Eighteen paths covering generic plan reference data, electricity service points, int
  name: CDR Energy API
  slug: cdr-energy-api
- description: The gateway contract AEMO implements as the CDR Secondary Data Holder for energy. Retailers are the primary data holders for the customer relationship, but the physical data — NMI standing data, meter
  name: CDR Energy Secondary Data Holder API
  slug: cdr-energy-secondary-data-holder-api
- description: The cross-sector endpoints every CDR data holder must expose regardless of industry — GET /common/customer and /common/customer/detail for the consented customer's identity, and the unauthenticated /d
  name: CDR Common API
  slug: cdr-common-api
- description: The onboarding contract. Rather than a developer portal issuing keys, an accredited data recipient presents a Software Statement Assertion obtained from the CDR Register and self-registers with each d
  name: CDR Dynamic Client Registration API
  slug: cdr-dynamic-client-registration-api
- description: The mandated reporting surface every data holder must expose to the ACCC — GET /admin/metrics returns availability, performance, invocation, error and rejection statistics, and POST /admin/register/me
  name: CDR Admin API
  slug: cdr-admin-api
artifact_total: 17
asyncapis:
- description: ''
  name: Cdr Energy Webhooks
  slug: cdr-energy-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cdr-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cdr.gov.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: docs
  title: ''
  type: Documentation
  url: https://dsb.gov.au/consumer-data-right/data-standards
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#cdr-energy-api-schemas
- group: auth
  title: ''
  type: Authentication
  url: https://api.cdr.gov.au/idp/.well-known/openid-configuration
- group: auth
  title: ''
  type: Security
  url: https://consumerdatastandardsaustralia.github.io/infosec/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ConsumerDataStandardsAustralia
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ConsumerDataStandardsAustralia/standards
- group: start
  title: ''
  type: Sandbox
  url: https://github.com/ConsumerDataStandardsAustralia/mock-register
- group: design
  title: ''
  type: Conformance
  url: https://github.com/ConsumerDataStandardsAustralia/standards-testing
- group: operate
  title: ''
  type: Support
  url: https://github.com/ConsumerDataStandardsAustralia/standards-maintenance
- group: company
  title: ''
  type: Blog
  url: https://dsb.gov.au/news-and-announcements
- group: auth
  title: ''
  type: Authentication
  url: authentication/cdr-energy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cdr-energy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cdr-energy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cdr-energy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cdr-energy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://consumerdatastandardsaustralia.github.io/standards/#cdr-common-api-schemas
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#future-dated-obligations
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cdr-energy-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/ConsumerDataStandardsAustralia/standards/releases
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cdr-energy-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cdr-energy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://consumerdatastandardsaustralia.github.io/standards-testing/
- group: build
  title: ''
  type: Packages
  url: packages/cdr-energy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cdr-energy-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cdr-energy-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cdr-energy-sandbox.yml
- group: start
  title: ''
  type: Sandbox
  url: https://cdrsandbox.gov.au/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cdr-energy-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cdr-energy-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cdr-energy-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/cdr-energy-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cdr-energy-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/winter-shadow-541400/workspace/dsb-schema-tests
- group: start
  title: ''
  type: GettingStarted
  url: https://consumerdatastandardsaustralia.github.io/standards/#introduction
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/ConsumerDataStandardsAustralia/standards-maintenance
- group: company
  title: ''
  type: BlogRSS
  url: https://dsb.gov.au/news-and-announcements
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ConsumerDataRight
created: '2026-07-27'
description: 'The Consumer Data Right (CDR) is Australia''s statutory consumer data-sharing regime, created under Part IVD of the Competition and Consumer Act 2010 and extended from banking into electricity by the Consumer Data Right (Energy Sector) Designation 2020. It is run by three bodies: the ACCC as lead regulator and operator of the CDR Register, the OAIC as privacy regulator, and the Treasury Data Standards Body, which writes the binding Consumer Data Standards. In energy the regime obliges electricity retailers to expose plans, accounts, billing, invoices, payment schedules, concessions, service points, interval usage and DER data through one identical, versioned API contract, with AEMO acting as the Secondary Data Holder gateway for NMI standing data, metering data and the DER register. Unlike almost every other energy-sector data mandate, this one is verifiably implemented rather than merely announced: the public CDR Register listed 84 energy data holder brands with live public
  base URIs when probed on 2026-07-27, and 53 of those base URIs returned standards-conformant product data anonymously on the first request. Its API posture is a clean two-speed split — genuinely open, unauthenticated market data (retail plan and tariff reference data, plus the participant register itself) sitting alongside consumer data that is closed behind ACCC accreditation, mutual TLS, FAPI-grade OAuth 2.0 / OpenID Connect and explicit, revocable consumer consent. Home market Australia.'
examples:
- key_count: 2
  name: Cdr Energy Discovery Outages Response Example
  slug: cdr-energy-discovery-outages-response-example
- key_count: 2
  name: Cdr Energy Discovery Status Response Example
  slug: cdr-energy-discovery-status-response-example
- key_count: 2
  name: Cdr Energy Plan Detail Response Example
  slug: cdr-energy-plan-detail-response-example
- key_count: 3
  name: Cdr Energy Plans Response Example
  slug: cdr-energy-plans-response-example
- key_count: 3
  name: Cdr Energy Register Data Holder Brands Summary Example
  slug: cdr-energy-register-data-holder-brands-summary-example
image: https://raw.githubusercontent.com/ConsumerDataRight/mock-data-holder/main/Assets/cdr-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface derived from OpenAPI (no published server)
  slug: candidate-mcp-tool-surface-derived-from-openapi-no-published-server
modified: '2026-07-27'
name: Consumer Data Right (Energy)
nav: Providers
network: true
overview: 'Consumer Data Right (Energy) publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CDR Register API, CDR Energy API, CDR Energy Secondary Data Holder API, and 3 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Consumer Data Right.


  The Consumer Data Right (Energy) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Consumer Data Right (Energy)''s developer surface includes documentation, API reference, authentication, sandbox, support, engineering blog, changelog, and 35 more developer resources.'
random_paper: 80
rate_limits:
- limit_count: 6
  name: Cdr Energy Rate Limits
  slug: cdr-energy-rate-limits
scopes:
- name: Cdr Energy Scopes
  scope_count: 15
  slug: cdr-energy-scopes
  summary_line: 15 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 58.3
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 64.2
    developer_ergonomics: 79.9
    discoverability: 83.3
    governance: 20.8
    operational_transparency: 100.0
  previous_composite: 58.3
  provenance:
    conformance: first-party
    contracts:
      callable: 16.7
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 63.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cdr-energy/refs/heads/main/screenshots/cdr-energy-2026-08-07T163251.png
security:
- kind: authentication
  name: Cdr Energy Authentication
  slug: cdr-energy-authentication
  summary_line: oauth2/openIdConnect/mutualTLS/http · 5 schemes
- kind: domain-security
  name: Cdr Energy Domain Security
  slug: cdr-energy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cdr-energy
tags:
- Energy
- Australia
- Utilities
- Electricity
- Consumer Data Right
- Open Energy
- Smart Metering
- DER
- Energy Markets
- Regulation
- Government
- Open Data
website: https://www.cdr.gov.au/
---
