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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Energyaustralia Agentic Access
  operation_count: 27
  slug: energyaustralia-agentic-access
  summary_line: 27 operations · 5 acting
api_count: 3
apis:
- description: Public, unauthenticated Consumer Data Right energy Product Reference Data for the EnergyAustralia brand, conforming to the Australian Consumer Data Standards energy schemas. Unlike CDR banking — where
  name: EnergyAustralia CDR Energy Plans API
  slug: energyaustralia-cdr-energy-plans-api
- description: 'The Consumer Data Standards Common API discovery endpoints served for the EnergyAustralia brand path on the AER Energy Made Easy CDR gateway. Public and unauthenticated. Confirmed live on 2026-07-27: '
  name: EnergyAustralia CDR Discovery Status API
  slug: energyaustralia-cdr-discovery-api
- description: The mandated, authenticated Consumer Data Right consumer data-sharing surface — energy accounts, invoices, billing, balances, concessions, payment schedules, electricity service points, interval usage
  name: EnergyAustralia CDR Energy Consumer Data Sharing API
  slug: energyaustralia-cdr-energy-consumer-data-api
artifact_total: 7
common:
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
overview: 'EnergyAustralia publishes 3 APIs on the [APIs.io](https://apis.io/) network: CDR Energy Plans API, CDR Discovery Status API, and CDR Energy Consumer Data Sharing API. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  EnergyAustralia''s developer surface includes authentication, changelog, API reference, documentation, support, signup flow, pricing, and 23 more developer resources.'
random_paper: 36
scopes:
- name: Energyaustralia Scopes
  scope_count: 12
  slug: energyaustralia-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: developing
  composite: 44.4
  delta: -3.5
  facets:
    commercial_clarity: 44.7
    contract_quality: 45.8
    developer_ergonomics: 32.1
    discoverability: 88.9
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 47.9
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
    score: 56.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
