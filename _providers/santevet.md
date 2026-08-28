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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Santevet Agentic Access
  operation_count: 64
  slug: santevet-agentic-access
  summary_line: 64 operations · 9 acting
api_count: 3
apis:
- description: SantéVet's partner reference-data API and the registry every other SantéVet surface depends on. Publishes species, breeds and breed groups; insurance contract definitions, cover options and rate rows;
  name: SantéVet Toolkit API
  slug: santevet-toolkit
- description: SantéVet's partner claims and settlement API. Creates and retrieves pet-insurance reimbursement claims, lists every claim for an insured animal or for a client, and returns the third-party-payment (ti
  name: SantéVet Reimbursement API
  slug: santevet-reimbursement
- description: SantéVet's partner quote-to-subscribe funnel and rating engine. Creates and updates prospects (with a dedicated GDPR anonymisation operation), creates, searches, validates and subscribes quotations, a
  name: SantéVet Acquisition API
  slug: santevet-acquisition
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.santevet.com/
- group: start
  title: ''
  type: Login
  url: https://espaceclient.santevet.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.santevet.com/partenaire-btob
- group: operate
  title: ''
  type: Support
  url: https://www.santevet.com/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.santevet.com/mentions-legales
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.santevet.com/mes-donnees-personnelles
- group: auth
  title: ''
  type: Authentication
  url: authentication/santevet-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/santevet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/santevet-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/santevet-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/santevet-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/santevet-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/santevet-domain-security.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/santevet-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/santevet-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/santevet-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/santevet-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/santevet-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/santevet-agentic-access.yml
created: '2026-08-17'
description: 'SantéVet is a French pet-insurance company, founded in 2003 and headquartered in Lyon, that insures dogs, cats and small pets (NAC) across five European markets — France, Belgium, Spain, Italy and Germany. Alongside its direct-to-consumer business it runs a B2B distribution network: brokers, retailers, affinity partners and veterinary practices embed SantéVet quoting, subscription and claims into their own channels over HTTP APIs. Three of those partner APIs serve documentation anonymously — a reference-data Toolkit API (58 operations, API Platform, Hydra/JSON-LD), a Reimbursement API behind the PayVet third-party-payment product (6 operations, OpenAPI 3.0.3), and an Acquisition API carrying the quote-to-subscribe funnel and the rating engine (14 operations, HTML reference only). SantéVet publishes no developer portal, no SDK, no pricing and no self-serve signup; credentials are issued through a sales process.'
jsonld:
- class_count: 0
  name: Santevet Toolkit Hydra Docs Context
  property_count: 5
  slug: santevet-toolkit-hydra-docs
layout: provider
modified: '2026-08-17'
name: SantéVet
nav: Providers
network: true
overview: 'SantéVet publishes 2 APIs on the [APIs.io](https://apis.io/) network: Toolkit API and Reimbursement API. Tagged areas include Insurance, Insurtech, Pet Insurance, Veterinary, and Consumer.


  The SantéVet catalog on APIs.io includes 1 JSON-LD context.


  SantéVet''s developer surface includes signup flow, support, authentication, sandbox, and 16 more developer resources.'
plans:
- name: Santevet Plans Pricing
  plan_count: 0
  slug: santevet-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Santevet Rate Limits
  slug: santevet-rate-limits
score:
  band: thin
  composite: 39.2
  delta: 1.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 53.0
    developer_ergonomics: 32.7
    discoverability: 77.8
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Santevet Authentication
  slug: santevet-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Santevet Domain Security
  slug: santevet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: santevet
tags:
- Insurance
- Insurtech
- Pet Insurance
- Veterinary
- Consumer
- Embedded Insurance
- Claims
- Payments
- France
- Europe
- Company
website: https://www.santevet.com/
---
