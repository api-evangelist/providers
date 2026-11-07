---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'White-label REST API for electronic invoicing integrated with Ecuador''s SRI: issue invoices, credit notes and retentions as JSON, with OAuth 2.0 auth, asynchronous webhooks for authorization status, a'
  name: Taxo API (Ecuador)
  slug: taxo-api-ecuador
artifact_total: 4
asyncapis:
- description: ''
  name: Taxo Webhooks
  slug: taxo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://taxo.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.taxo.ws
- group: docs
  title: ''
  type: Documentation
  url: https://docs.taxo.ws/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.taxo.ws
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.taxo.ws/getting-started
- group: company
  title: ''
  type: Blog
  url: https://taxo.co/ec/blog
- group: operate
  title: ''
  type: Support
  url: https://taxo.co/ec/ayuda
- group: start
  title: ''
  type: SignUp
  url: https://app.taxo.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taxo.co/ec/terminos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taxo.co/ec/privacidad
- group: agent
  href: https://artifacts.apis.io/taxo/llms/taxo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/taxo-llms.txt
- group: auth
  href: https://artifacts.apis.io/taxo/authentication/taxo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/taxo-authentication.yml
- group: design
  href: https://artifacts.apis.io/taxo/conventions/taxo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/taxo-conventions.yml
- group: design
  href: https://artifacts.apis.io/taxo/asyncapi/taxo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/taxo-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/taxo/mcp/taxo-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/taxo-mcp.yml
- group: design
  href: https://artifacts.apis.io/taxo/conformance/taxo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/taxo-conformance.yml
- group: design
  href: https://artifacts.apis.io/taxo/lifecycle/taxo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/taxo-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/taxo/security/taxo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/taxo-domain-security.yml
created: '2026-07-17'
description: 'Taxo (Contadores del Futuro) is an AI-powered tax and accounting automation platform for accountants and firms (despachos) in Ecuador and Mexico, used by 2,000+ practices. It automates fiscal work across two regional hubs: Ecuador (integrated with the SRI) and Mexico (integrated with the SAT). Products include bulk invoice/CFDI download bots, AI-assisted tax declarations, electronic invoicing (facturación electrónica / CFDI 4.0 timbrado), invoicing by WhatsApp, batch and mass issuance, and white-label REST APIs (Taxo API, SRI API, SAT API) for embedding electronic invoicing and tax-authority queries into fintechs, e-commerce, ERPs and marketplaces. Backed by 500 Global.'
image: https://storage.googleapis.com/gpt-engineer-file-uploads/attachments/og-images/257114fb-6f8f-4ec9-b1ae-795da7ce8772
layout: provider
modified: '2026-07-21'
name: TAXO
nav: Providers
network: true
overview: 'TAXO is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Tax, Fintech, and E-Invoicing.


  The TAXO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TAXO''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 11 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.7
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 57.1
    discoverability: 73.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ecuador
    - mexico
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 33.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/taxo/taxo-2026-09-02T162626.png
security:
- kind: authentication
  name: Taxo Authentication
  slug: taxo-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Taxo Domain Security
  slug: taxo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: taxo
tags:
- Company
- Accounting
- Tax
- Fintech
- E-Invoicing
- Facturación Electrónica
- CFDI
- SRI
- SAT
- Artificial Intelligence
- Ecuador
- Mexico
website: https://taxo.co
---
