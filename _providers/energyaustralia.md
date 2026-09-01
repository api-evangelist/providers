---
access_model:
  confidence: high
  label: Public CDR product data · Consumer data accredited-only
  onboarding: unknown
  pricing: free
  public: true
  source:
  - review
  trial: false
  try_now: false
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
  name: Energyaustralia Agentic Access
  operation_count: 27
  slug: energyaustralia-agentic-access
  summary_line: 27 operations · 5 acting
api_count: 2
apis:
- description: Data Holder Customer endpoints
  name: EnergyAustralia Data Holder Customers API
  slug: energyaustralia-data-holder-customers-api
- description: Data Holder Operations endpoints
  name: EnergyAustralia Data Holder Operations API
  slug: energyaustralia-data-holder-operations-api
- description: Distributed Energy Resource endpoints
  name: EnergyAustralia Distributed Energy Resources API
  slug: energyaustralia-distributed-energy-resources-api
- description: Electricity Service Point endpoints
  name: EnergyAustralia Electricity Service Points API
  slug: energyaustralia-electricity-service-points-api
- description: Electricity Usage endpoints
  name: EnergyAustralia Electricity Usage API
  slug: energyaustralia-electricity-usage-api
- description: Energy Account Balance endpoints
  name: EnergyAustralia Energy Account Balances API
  slug: energyaustralia-energy-account-balances-api
- description: Energy Account Billing endpoints
  name: EnergyAustralia Energy Account Billing API
  slug: energyaustralia-energy-account-billing-api
- description: Energy Account endpoints
  name: EnergyAustralia Energy Accounts API
  slug: energyaustralia-energy-accounts-api
- description: Energy Plan endpoints
  name: EnergyAustralia Energy Plans API
  slug: energyaustralia-energy-plans-api
artifact_total: 15
collections:
- collection_type: open
  name: CDR Common API
  slug: open-energyaustralia-cds-common-api
- collection_type: open
  name: CDR Energy API
  slug: open-energyaustralia-cds-energy-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/energyaustralia-compare-energy-plans.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/energyaustralia-check-status-and-outages.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/energyaustralia-consumer-data-sharing.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/energyaustralia-usage-and-der.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/energyaustralia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/energyaustralia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/energyaustralia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/energyaustralia-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/energyaustralia-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/energyaustralia-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/energyaustralia-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://cdr.energymadeeasy.gov.au/energyaustralia/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#future-dated-obligations
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/energyaustralia-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/energyaustralia-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/energyaustralia-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/energyaustralia-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/energyaustralia-cds-energy-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/energyaustralia-cds-common-api-overlay.yaml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/energyaustralia-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/energyaustralia-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.energyaustralia.com.au/
- group: other
  title: ''
  type: ConsumerDataRight
  url: https://www.energyaustralia.com.au/home/help-support/faqs/consumer-data-right
- group: other
  title: ''
  type: APIStandards
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#energy-apis
- group: docs
  title: ''
  type: Documentation
  url: https://www.energymadeeasy.gov.au/frequently-asked-questions/how-can-i-get-access-to-the-energy-made-easy-plan-data
- group: start
  title: ''
  type: CDRRegister
  url: https://api.cdr.gov.au/cdr-register/v1/energy/data-holders/brands/summary
- group: operate
  title: ''
  type: Support
  url: https://www.energyaustralia.com.au/home/help-and-support
- group: start
  title: ''
  type: SignUp
  url: https://www.energyaustralia.com.au/myaccount-login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.energyaustralia.com.au/home/electricity-and-gas/plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.energyaustralia.com.au/energyaustralia-website-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.energyaustralia.com.au/sites/default/files/2024-07/Privacy%20Policy.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/energyaustralia
created: '2026-07-27'
description: 'EnergyAustralia is one of Australia''s "big three" gentailers — a vertically integrated electricity and gas business owned by Hong Kong''s CLP Group and headquartered in Melbourne, generating from Yallourn, Mount Piper and Hallett alongside wind assets and retailing to more than 1.7 million residential and business customers across Victoria, New South Wales, Queensland, South Australia and the ACT. It sits on both sides of the National Electricity Market value chain: a scheduled generator into the NEM, and a retailer of record holding the customer relationship, the billing account and the meter data. Its API posture is entirely a function of the Consumer Data Right rather than of any product strategy. EnergyAustralia is a designated and live CDR energy data holder — brand id 1cc7833a-b834-ed11-a832-000d3a8830d6 in the ACCC CDR Register, public base URI https://authncdr.energyaustralia.com.au — but the only anonymously reachable contract carrying its name is the Product Reference
  Data surface, and that is hosted by the Australian Energy Regulator''s Energy Made Easy CDR gateway, not by EnergyAustralia. The company publishes no developer portal, no OpenAPI of its own, no open market or generation data, and no self-serve signup; its own gateway at api.energyaustralia.com.au (MuleSoft Anypoint) answers 403 to the public. Consumer usage, billing and DER data is real, standardised and live, but reachable only by an ACCC-accredited data recipient under consent. Open on plans, closed on everything else.'
layout: provider
modified: '2026-07-27'
name: EnergyAustralia
nav: Providers
network: true
overview: 'EnergyAustralia publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Data Holder Customers API, Data Holder Operations API, Distributed Energy Resources API, and 6 more. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  EnergyAustralia''s developer surface includes authentication, changelog, API reference, documentation, support, signup flow, pricing, and 27 more developer resources.'
random_paper: 20
scopes:
- name: Energyaustralia Scopes
  scope_count: 12
  slug: energyaustralia-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 32.7
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    conformance: derived
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
    score: 51.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/energyaustralia/refs/heads/main/screenshots/energyaustralia-2026-08-07T164911.png
security:
- kind: authentication
  name: Energyaustralia Authentication
  slug: energyaustralia-authentication
  summary_line: none/mutualTLS/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Energyaustralia Domain Security
  slug: energyaustralia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: energyaustralia
tags:
- Energy
- Australia
- Utilities
- Electricity
- Gas
- Energy Retailer
- Consumer Data Right
- CDR
- Product Reference Data
- Smart Metering
- Energy Markets
- Renewables
website: https://www.energyaustralia.com.au/
---
