---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Simply Energy Agentic Access
  operation_count: 27
  slug: simply-energy-agentic-access
  summary_line: 27 operations · 5 acting
api_count: 3
apis:
- description: Public, unauthenticated Consumer Data Right Generic Tariff Data for the Simply Energy / ENGIE retail brand, conforming to the Data Standards Body Consumer Data Standards energy schemas. Confirmed live
  name: Simply Energy (ENGIE) CDR Energy Generic Plans API
  slug: simply-energy-cdr-energy-generic-plans-api
- description: The Consumer Data Standards Common Discovery API served from the brand's own registered CDR Public Base URI. Confirmed live on 2026-07-27. GET /discovery/status returns HTTP 200 at x-v 1 with status O
  name: Simply Energy (ENGIE) CDR Discovery API
  slug: simply-energy-cdr-discovery-api
- description: The mandated Consumer Data Right consumer data sharing surface, covering energy accounts, balances, billing, invoices, concessions, payment schedules, electricity service points, usage and distributed
  name: Simply Energy (ENGIE) CDR Energy Consumer Data API
  slug: simply-energy-cdr-energy-consumer-data-api
artifact_total: 9
common:
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
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: Simply Energy
nav: Providers
network: true
overview: 'Simply Energy publishes 3 APIs on the [APIs.io](https://apis.io/) network: (ENGIE) CDR Energy Generic Plans API, (ENGIE) CDR Discovery API, and (ENGIE) CDR Energy Consumer Data API. Tagged areas include Energy, Australia, Utilities, Electricity, and Gas.


  Simply Energy''s developer surface includes documentation, API reference, engineering blog, authentication, changelog, and 25 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 0
  name: Simply Energy Rate Limits
  slug: simply-energy-rate-limits
scopes:
- name: Simply Energy Scopes
  scope_count: 13
  slug: simply-energy-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: developing
  composite: 43.9
  delta: -3.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 47.2
    developer_ergonomics: 34.2
    discoverability: 83.3
    governance: 20.8
    operational_transparency: 50.0
  previous_composite: 47.0
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
