---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Simply Energy Agentic Access
  operation_count: 27
  slug: simply-energy-agentic-access
  summary_line: 27 operations · 5 acting
api_count: 2
apis:
- description: Data Holder Customer endpoints
  name: Simply Energy Data Holder Customers API
  slug: simply-energy-data-holder-customers-api
- description: Data Holder Operations endpoints
  name: Simply Energy Data Holder Operations API
  slug: simply-energy-data-holder-operations-api
- description: Distributed Energy Resource endpoints
  name: Simply Energy Distributed Energy Resources API
  slug: simply-energy-distributed-energy-resources-api
- description: Electricity Service Point endpoints
  name: Simply Energy Electricity Service Points API
  slug: simply-energy-electricity-service-points-api
- description: Electricity Usage endpoints
  name: Simply Energy Electricity Usage API
  slug: simply-energy-electricity-usage-api
- description: Energy Account Balance endpoints
  name: Simply Energy Energy Account Balances API
  slug: simply-energy-energy-account-balances-api
- description: Energy Account Billing endpoints
  name: Simply Energy Energy Account Billing API
  slug: simply-energy-energy-account-billing-api
- description: Energy Account endpoints
  name: Simply Energy Energy Accounts API
  slug: simply-energy-energy-accounts-api
- description: Energy Plan endpoints
  name: Simply Energy Energy Plans API
  slug: simply-energy-energy-plans-api
artifact_total: 18
collections:
- collection_type: open
  name: CDR Common API
  slug: open-simply-energy-cds-common
- collection_type: open
  name: CDR Energy API
  slug: open-simply-energy-cds-energy
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/simply-energy-cds-energy-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/simply-energy-compare-energy-plans.md
- group: other
  title: ''
  type: Overlay
  url: overlays/simply-energy-cds-common-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/simply-energy-check-data-holder-health.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/simply-energy-retrieve-consumer-energy-data.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/simply-energy-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simply-energy-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simply-energy-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.simplyenergy.com.au/
- group: company
  title: ''
  type: Website
  url: https://engie.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://engie.com.au/help-centre/cdr-policy
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#energy-apis
- group: start
  title: ''
  type: Registry
  url: https://api.cdr.gov.au/cdr-register/v1/energy/data-holders/brands/summary
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/engie-australia-new-zealand/
- group: operate
  title: ''
  type: HelpCenter
  url: https://engie.com.au/help-centre
- group: company
  title: ''
  type: Blog
  url: https://engie.com.au/media-news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://engie.com.au/help-centre/policies-and-commitments/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://engie.com.au/help-centre/policies-and-commitments/terms-of-use
- group: auth
  title: ''
  type: Authentication
  url: authentication/simply-energy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/simply-energy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/simply-energy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/simply-energy-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simply-energy-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simply-energy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://public.cdr.engie.com.au/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#endpoint-version-schedule
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/simply-energy-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/simply-energy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/simply-energy-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/simply-energy-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/simply-energy-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/simply-energy-engie-group-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/simply-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.engie.com/en/cert/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simply-energy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-27'
description: Simply Energy is the former brand of the Australian electricity and gas retailer that now trades as ENGIE, operated by IPower Pty Ltd (ACN 111 267 228) and IPower 2 Pty Ltd (ABN 24 070 374 293) trading as ENGIE (ABN 67 269 241 237), together with Simply Energy Solutions Pty Ltd. The business carried the Simply Energy name for seventeen years before rebranding to ENGIE in April 2024, and supplies more than 700,000 residential and business accounts across Victoria, South Australia, New South Wales, Queensland and Western Australia. It sits on the retail tier of the National Electricity Market value chain, buying wholesale energy and billing end customers, rather than in generation, transmission or distribution. Its API posture is entirely a product of statutory mandate, and in this case the mandate is genuinely implemented rather than merely claimed. The company is a designated Consumer Data Right energy data holder (data holder provider number DH002028) and is listed on the live
  CDR Register under the ENGIE brand. Its unauthenticated CDR Generic Plans endpoint, hosted for it by the Australian Energy Regulator's Energy Made Easy service, returns 2,452 real ENGIE tariff plans conforming to the Consumer Data Standards energy schemas, and its own registered public base URI serves the Consumer Data Standards discovery endpoints with correct x-v version negotiation. Everything else is closed. Customer usage, billing, service point and DER data are available only to ACCC accredited data recipients with explicit consumer consent, there is no developer portal, no self-serve API keys, no published OpenID Connect discovery document, and no open grid, market or system data of any kind.
layout: provider
mcp_servers:
- description: ''
  name: Simply Energy MCP Server
  slug: simply-energy-mcp-server
modified: '2026-07-27'
name: Simply Energy
nav: Providers
network: true
overview: 'Simply Energy publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Data Holder Customers API, Data Holder Operations API, Distributed Energy Resources API, and 6 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  Simply Energy''s developer surface includes documentation, API reference, engineering blog, authentication, changelog, and 31 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 14
  name: Simply Energy Rate Limits
  slug: simply-energy-rate-limits
scopes:
- name: Simply Energy Scopes
  scope_count: 13
  slug: simply-energy-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 37.5
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simply-energy/refs/heads/main/screenshots/simply-energy-2026-08-17T125320.png
security:
- kind: authentication
  name: Simply Energy Authentication
  slug: simply-energy-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 0 schemes
- kind: domain-security
  name: Simply Energy Domain Security
  slug: simply-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Simply Energy Vulnerability Disclosure
  slug: simply-energy-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: simply-energy
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Energy Retail
- Consumer Data Right
- CDR
- Smart Metering
- Energy Markets
website: https://www.simplyenergy.com.au/
---
