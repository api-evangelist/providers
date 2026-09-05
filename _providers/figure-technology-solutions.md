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
  - sandbox
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Figure Technology Solutions Agentic Access
  operation_count: 36
  slug: figure-technology-solutions-agentic-access
  summary_line: 36 operations · 15 acting
api_count: 3
apis:
- baseURL: https://api.figure.com
  baseurl_source: declared
  description: The Encryption API from Figure Technology Solutions — 1 operation(s) for encryption.
  name: Figure Technology Solutions Encryption API
  slug: figure-technology-solutions-encryption-api
- baseURL: https://api.figure.com
  baseurl_source: declared
  description: The HELOC application requests API from Figure Technology Solutions — 19 operation(s) for heloc application requests.
  name: Figure Technology Solutions HELOC application requests API
  slug: figure-technology-solutions-heloc-application-requests-api
- baseURL: https://api.figure.com
  baseurl_source: declared
  description: The HELOC Offers API from Figure Technology Solutions — 2 operation(s) for heloc offers.
  name: Figure Technology Solutions HELOC Offers API
  slug: figure-technology-solutions-heloc-offers-api
- baseURL: https://api.figure.com
  baseurl_source: declared
  description: The Loan Originator requests API from Figure Technology Solutions — 1 operation(s) for loan originator requests.
  name: Figure Technology Solutions Loan Originator requests API
  slug: figure-technology-solutions-loan-originator-requests-api
- baseURL: https://api.figure.com
  baseurl_source: declared
  description: The Loan Tape V1 API from Figure Technology Solutions — 6 operation(s) for loan tape v1.
  name: Figure Technology Solutions Loan Tape V1 API
  slug: figure-technology-solutions-loan-tape-v1-api
- baseURL: https://api.figure.com
  baseurl_source: declared
  description: The Loan Tape V2 API from Figure Technology Solutions — 3 operation(s) for loan tape v2.
  name: Figure Technology Solutions Loan Tape V2 API
  slug: figure-technology-solutions-loan-tape-v2-api
- baseURL: https://api.figure.com
  baseurl_source: declared
  description: The Payment History V1 API from Figure Technology Solutions — 3 operation(s) for payment history v1.
  name: Figure Technology Solutions Payment History V1 API
  slug: figure-technology-solutions-payment-history-v1-api
- baseURL: https://api.figure.com
  baseurl_source: declared
  description: The Payment History V2 API from Figure Technology Solutions — 1 operation(s) for payment history v2.
  name: Figure Technology Solutions Payment History V2 API
  slug: figure-technology-solutions-payment-history-v2-api
artifact_total: 21
asyncapis:
- description: ''
  name: Figure Technology Solutions Webhooks
  slug: figure-technology-solutions-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HELOC Inquiries Encryption API
  slug: open-figure-technology-solutions-encryption-api
- collection_type: open
  name: HELOC Inquiries Encryption HELOC application requests API
  slug: open-figure-technology-solutions-heloc-application-requests-api
- collection_type: open
  name: HELOC Inquiries Encryption HELOC Offers API
  slug: open-figure-technology-solutions-heloc-offers-api
- collection_type: open
  name: HELOC Inquiries Encryption Loan Originator requests API
  slug: open-figure-technology-solutions-loan-originator-requests-api
- collection_type: open
  name: HELOC Inquiries Encryption Loan Tape V1 API
  slug: open-figure-technology-solutions-loan-tape-v1-api
- collection_type: open
  name: HELOC Inquiries Encryption Loan Tape V2 API
  slug: open-figure-technology-solutions-loan-tape-v2-api
- collection_type: open
  name: HELOC Inquiries Encryption Payment History V1 API
  slug: open-figure-technology-solutions-payment-history-v1-api
- collection_type: open
  name: HELOC Inquiries Encryption Payment History V2 API
  slug: open-figure-technology-solutions-payment-history-v2-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/figure-technology-solutions-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/figure-technology-solutions-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/figure-technology-solutions-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/figure-technology-solutions-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.figure.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.figure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.figure.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.figure.com/heloc-inquiries/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.figure.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.figure.com/partner/success-center/
- group: company
  title: ''
  type: Blog
  url: https://www.figure.com/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FigureTechnologies
- group: operate
  title: ''
  type: StatusPage
  url: https://status.figure.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.figure.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.figure.com/privacy/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/figure-technology-solutions-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/figure-technology-solutions-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/figure-technology-solutions-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/figure-technology-solutions-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/figure-technology-solutions-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/figure-technology-solutions-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/figure-technology-solutions-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/figure-technology-solutions-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/figure-technology-solutions-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/figure-technology-solutions-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/figure-technology-solutions-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/figure-technology-solutions-heloc-inquiries-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figure-technology-solutions-heloc-pre-qualification-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figure-technology-solutions-portfolio-manager-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/figure-technology-solutions-run-heloc-inquiry.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/figure-technology-solutions-prequalify-heloc.md
created: '2026-07-17'
description: 'Figure Technology Solutions is a Reno, Nevada financial-technology company (founded 2018) that builds and operates blockchain-based platforms for lending, capital markets, and asset management. Its public Partner APIs let integrators originate and manage Home Equity Line of Credit (HELOC) loans end to end: non-licensed pre-qualification and offer retrieval, full HELOC inquiry lifecycle management (start inquiry, select property, add income/SSN, verify liens, select offer, documents), loan-originator directory management, and Portfolio Manager reporting over owned and pledged loan pools. Figure also runs Figure Connect, a blockchain-based loan marketplace connecting loan sellers and buyers. The REST/JSON APIs authenticate with an apikey header and protect PII in transit with JWE encryption (RSA-OAEP-256 + A256GCM).'
image: https://docs.figure.com/img/docusaurus-social-card.jpg
layout: provider
modified: '2026-07-19'
name: Figure Technology Solutions
nav: Providers
network: true
overview: 'Figure Technology Solutions publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Encryption API, HELOC application requests API, HELOC Offers API, and 5 more. Tagged areas include Company, Fintech, Lending, HELOC, and Home Equity.


  The Figure Technology Solutions catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Figure Technology Solutions'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, sandbox, and 24 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 53.1
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/figure-technology-solutions/refs/heads/main/screenshots/figure-technology-solutions-2026-07-25T214442.png
security:
- kind: authentication
  name: Figure Technology Solutions Authentication
  slug: figure-technology-solutions-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Figure Technology Solutions Domain Security
  slug: figure-technology-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: figure-technology-solutions
tags:
- Company
- Fintech
- Lending
- HELOC
- Home Equity
- Mortgage
- Capital Markets
- Blockchain
- Loan Origination
- Financial-Services
website: https://www.figure.com/
---
