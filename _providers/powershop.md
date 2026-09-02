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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Powershop Agentic Access
  operation_count: 27
  slug: powershop-agentic-access
  summary_line: 27 operations · 5 acting
api_count: 2
apis:
- description: Data Holder Customer endpoints
  name: Powershop Data Holder Customers API
  slug: powershop-data-holder-customers-api
- description: Data Holder Operations endpoints
  name: Powershop Data Holder Operations API
  slug: powershop-data-holder-operations-api
- description: Distributed Energy Resource endpoints
  name: Powershop Distributed Energy Resources API
  slug: powershop-distributed-energy-resources-api
- description: Electricity Service Point endpoints
  name: Powershop Electricity Service Points API
  slug: powershop-electricity-service-points-api
- description: Electricity Usage endpoints
  name: Powershop Electricity Usage API
  slug: powershop-electricity-usage-api
- description: Energy Account Balance endpoints
  name: Powershop Energy Account Balances API
  slug: powershop-energy-account-balances-api
- description: Energy Account Billing endpoints
  name: Powershop Energy Account Billing API
  slug: powershop-energy-account-billing-api
- description: Energy Account endpoints
  name: Powershop Energy Accounts API
  slug: powershop-energy-accounts-api
- description: Energy Plan endpoints
  name: Powershop Energy Plans API
  slug: powershop-energy-plans-api
artifact_total: 16
collections:
- collection_type: open
  name: CDR Common API
  slug: open-powershop-cdr-common-api
- collection_type: open
  name: CDR Energy API
  slug: open-powershop-cdr-energy-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/powershop-lookup-energy-plans.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/powershop-check-cdr-status.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/powershop-share-consumer-energy-data.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/powershop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/powershop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/powershop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/powershop-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/powershop-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/powershop-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/powershop-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://public.cdr.powershop.com.au/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/powershop-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/powershop-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/powershop-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/powershop-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/powershop-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/powershop-cdr-energy-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/powershop-cdr-common-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/powershop-packages.yml
- group: company
  title: ''
  type: Website
  url: https://www.powershop.com.au/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#energy-apis
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#common-apis
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.powershop.com.au/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.powershop.com.au/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.powershop.com.au/help-centre
- group: company
  title: ''
  type: Blog
  url: https://www.powershop.com.au/energy-insights
- group: commercial
  title: ''
  type: Pricing
  url: https://www.powershop.com.au/energy-rates-and-prices
- group: start
  title: ''
  type: SignUp
  url: https://www.powershop.com.au/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.powershop.com.au/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.powershop.com.au/privacy-policy/cdr-policy
- group: docs
  title: ''
  type: Documentation
  url: https://www.powershop.com.au/powershop-and-shell
- group: start
  title: ''
  type: Registry
  url: https://api.cdr.gov.au/cdr-register/v1/energy/data-holders/brands/summary
- group: docs
  title: ''
  type: Documentation
  url: https://www.cdr.gov.au/rollout/cdr-energy-sector
- group: docs
  title: ''
  type: Specification
  url: https://consumerdatastandardsaustralia.github.io/standards/
created: '2026-07-27'
description: 'Powershop is an Australian retail energy brand selling electricity in New South Wales, Victoria, south-east Queensland and South Australia, and gas in New South Wales and Victoria. It is operated by Powershop Australia Pty Ltd (ABN 41 154 914 075), a wholly owned Shell Energy Australia business since Shell completed its acquisition from Meridian Energy in February 2022. Powershop sits at the retail end of the energy value chain — it buys wholesale, bills the customer, and owns the customer relationship — and is known for its "Powerpacks" prepay purchasing model, GreenPower add-on, and EV Day/EV Night plans. Its API posture is entirely regulatory, not commercial: Powershop publishes NO first-party developer portal, no API keys, and no self-serve documentation, and has publicly said since 2017 that it has no public API. What it does have is a verified Consumer Data Right (CDR) energy implementation. Powershop is a designated CDR energy data holder listed live on the ACCC CDR
  Register with a public base URI of https://public.cdr.powershop.com.au, which returns standards-conformant Consumer Data Standards responses for /cds-au/v1/discovery/status and /cds-au/v1/discovery/outages without authentication. Its Generic Tariff (plan) data is served openly and anonymously from the Australian Energy Regulator''s Energy Made Easy CDR host, where 482 Powershop electricity and gas plans are retrievable with no credentials at all. The customer-level data the mandate actually exists to unlock — accounts, billing, invoices, payment schedules, concessions, plus AEMO-sourced metering, NMI standing and DER register data — is real, documented, and reachable only by an accredited data recipient acting on an authenticated consumer consent. Open tariff data, closed consumer data: a mandate that was implemented, not merely claimed.'
image: https://www.powershop.com.au/powershop-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Powershop MCP Server
  slug: powershop-mcp-server
modified: '2026-07-27'
name: Powershop
nav: Providers
network: true
overview: 'Powershop publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Data Holder Customers API, Data Holder Operations API, Distributed Energy Resources API, and 6 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  Powershop''s developer surface includes authentication, changelog, API reference, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
random_paper: 12
scopes:
- name: Powershop Scopes
  scope_count: 11
  slug: powershop-scopes
  summary_line: 11 scopes
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/powershop/refs/heads/main/screenshots/powershop-2026-08-17T124837.png
security:
- kind: authentication
  name: Powershop Authentication
  slug: powershop-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 0 schemes
- kind: domain-security
  name: Powershop Domain Security
  slug: powershop-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: powershop
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Consumer Data Right
- Energy Retail
- Smart Metering
- Solar
- Tariffs
- Open Data
website: https://www.powershop.com.au/
---
