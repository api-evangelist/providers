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
  name: Alinta Energy Agentic Access
  operation_count: 27
  slug: alinta-energy-agentic-access
  summary_line: 27 operations · 5 acting
api_count: 2
apis:
- description: Data Holder Customer endpoints
  name: Alinta Energy Data Holder Customers API
  slug: alinta-energy-data-holder-customers-api
- description: Data Holder Operations endpoints
  name: Alinta Energy Data Holder Operations API
  slug: alinta-energy-data-holder-operations-api
- description: Distributed Energy Resource endpoints
  name: Alinta Energy Distributed Energy Resources API
  slug: alinta-energy-distributed-energy-resources-api
- description: Electricity Service Point endpoints
  name: Alinta Energy Electricity Service Points API
  slug: alinta-energy-electricity-service-points-api
- description: Electricity Usage endpoints
  name: Alinta Energy Electricity Usage API
  slug: alinta-energy-electricity-usage-api
- description: Energy Account Balance endpoints
  name: Alinta Energy Energy Account Balances API
  slug: alinta-energy-energy-account-balances-api
- description: Energy Account Billing endpoints
  name: Alinta Energy Energy Account Billing API
  slug: alinta-energy-energy-account-billing-api
- description: Energy Account endpoints
  name: Alinta Energy Energy Accounts API
  slug: alinta-energy-energy-accounts-api
- description: Energy Plan endpoints
  name: Alinta Energy Energy Plans API
  slug: alinta-energy-energy-plans-api
artifact_total: 17
collections:
- collection_type: open
  name: CDR Common API
  slug: open-alinta-energy-cds-common-api
- collection_type: open
  name: CDR Energy API
  slug: open-alinta-energy-cds-energy-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/alinta-energy-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alinta-energy-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alinta-energy-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alinta-energy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alinta-energy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alinta-energy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alinta-energy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alinta-energy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://public.cdr.alintaenergy.com.au/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alinta-energy-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/alinta-energy-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alinta-energy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alinta-energy-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alinta-energy-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/alinta-energy-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alinta-energy-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alinta-energy-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/alinta-energy-cds-energy-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/alinta-energy-cds-common-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/alinta-energy-plan-catalogue.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/alinta-energy-cdr-availability.md
- group: docs
  title: ''
  type: Documentation
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#energy-apis
- group: operate
  title: ''
  type: Support
  url: https://www.alintaenergy.com.au/help-and-support/help-and-support/customer-support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alintaenergy.com.au/help-and-support/terms-and-conditions/website-terms-and-conditions
- group: other
  title: ''
  type: ConsumerDataRight
  url: https://www.alintaenergy.com.au/help-and-support/terms-and-conditions/consumer-data-right-cdr/consumer-data-right-policy
- group: company
  title: ''
  type: Website
  url: https://www.alintaenergy.com.au/
- group: other
  title: ''
  type: ConsumerDataRight
  url: https://www.alintaenergy.com.au/help-and-support/terms-and-conditions/consumer-data-right-cdr
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alintaenergy.com.au/help-and-support/terms-and-conditions/privacy-policy
- group: other
  title: ''
  type: APIStandards
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: start
  title: ''
  type: Registry
  url: https://api.cdr.gov.au/cdr-register/v1/energy/data-holders/brands/summary
- group: other
  title: ''
  type: Regulator
  url: https://www.cdr.gov.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlintaEnergy
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/alinta-energy
- group: operate
  title: ''
  type: Status
  url: https://public.cdr.alintaenergy.com.au/cds-au/v1/discovery/status
created: '2026-07-27'
description: 'Alinta Energy is one of Australia''s largest integrated energy retailers and generators, owned by Hong Kong-based Chow Tai Fook Enterprises, supplying electricity and gas to more than a million homes and businesses across Western Australia, South Australia, Victoria, New South Wales and Queensland while operating an owned and contracted generation portfolio of roughly 3,000 MW spanning gas, coal, wind, solar and battery storage, plus the Lumo Energy retail brand. It sits at the retail end of the value chain — the tier the Australian Consumer Data Right binds. Alinta is a designated and live CDR energy data holder: its own public base URI https://public.cdr.alintaenergy.com.au serves the standards-conformant discovery endpoints (confirmed HTTP 200), and 493 of its energy plans are published anonymously through the CDR generic plan data channel — but that plan channel is hosted by the Australian Energy Regulator''s Energy Made Easy platform, not by Alinta. Its API posture is
  therefore honestly summarised as mandate-implemented but developer-closed: everything of substance sits behind ACCC accreditation and consumer consent, Alinta publishes no developer portal, no self-serve API, no proprietary OpenAPI and no open grid or market data of its own.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alinta-energy.png
layout: provider
mcp_servers:
- description: ''
  name: Alinta Energy MCP Server
  slug: alinta-energy-mcp-server
modified: '2026-07-27'
name: Alinta Energy
nav: Providers
network: true
overview: 'Alinta Energy publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Data Holder Customers API, Data Holder Operations API, Distributed Energy Resources API, and 6 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  Alinta Energy''s developer surface includes authentication, changelog, documentation, API reference, support, status page, and 30 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 7
  name: Alinta Energy Rate Limits
  slug: alinta-energy-rate-limits
scopes:
- name: Alinta Energy Scopes
  scope_count: 11
  slug: alinta-energy-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 65.8
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    conformance: derived
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
security:
- kind: authentication
  name: Alinta Energy Authentication
  slug: alinta-energy-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Alinta Energy Domain Security
  slug: alinta-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alinta-energy
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Energy Retail
- Consumer Data Right
- CDR
- Open Energy Data
- Smart Metering
- Renewables
- Generation
website: https://www.alintaenergy.com.au/
---
