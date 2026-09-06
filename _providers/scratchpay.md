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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Scratchpay Agentic Access
  operation_count: 3
  slug: scratchpay-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 3
apis:
- baseURL: https://scratchpay.com/api
  baseurl_source: declared
  description: The Borrower application API from Scratchpay — 1 operation(s) for borrower application.
  name: Scratchpay Borrower application API
  slug: scratchpay-borrower-application-api
- baseURL: https://scratchpay.com/api
  baseurl_source: declared
  description: The Borrower application result API from Scratchpay — 1 operation(s) for borrower application result.
  name: Scratchpay Borrower application result API
  slug: scratchpay-borrower-application-result-api
artifact_total: 9
asyncapis:
- description: ''
  name: Scratchpay Partner Webhooks
  slug: scratchpay-partner-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Partner Borrower application API
  slug: open-scratchpay-borrower-application-api
- collection_type: open
  name: Partner Borrower application Borrower application result API
  slug: open-scratchpay-borrower-application-result-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/scratchpay-care-credit-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://scratchpay.com
- group: docs
  title: ''
  type: Documentation
  url: https://scratchpay-lending.stonly.com/kb/guide/en/integrate-scratch-pay-plans-with-third-party-services-fnFPz1e3De/Steps/2720498
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/scratchpay/Scratchpay-API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scratchpay
- group: operate
  title: ''
  type: Support
  url: https://scratchpay.com/practice-support
- group: company
  title: ''
  type: Blog
  url: https://scratchpay.com/news
- group: start
  title: ''
  type: Login
  url: https://dashboard.scratchpay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scratchpay.com/legal/terms-of-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scratchpay.com/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/scratchpay-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scratchpay-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scratchpay-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/scratchpay-partner-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/scratchpay-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scratchpay-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/scratchpay-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/scratchpay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scratchpay-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scratchpay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scratchpay-domain-security.yml
created: '2026-07-17'
description: Scratchpay (Scratch Financial, Inc., NMLS ID 1582666) is a digital payment and financing platform for veterinary and human healthcare. Practices offer borrowers Scratch Pay installment plans ($200-$10,000 over 12-24 months, 0-36% APR) with no hidden fees and a soft credit check, plus Scratch Checkout payment processing and Scratch Comms patient communications. Over 12,000 veterinary hospitals across the U.S. and Canada integrate Scratch, which pays practices up front and collects from borrowers. Scratchpay exposes a partner/borrower API (published as archived OpenAPI on GitHub) for submitting loan applications and receiving an asynchronous approve/decline decision via a partner callback. Backed by Norwest Venture Partners.
image: https://6598889.fs1.hubspotusercontent-na1.net/hubfs/6598889/New%20Site%202025/newsite.png
layout: provider
modified: '2026-07-21'
name: Scratchpay
nav: Providers
network: true
overview: 'Scratchpay publishes 2 APIs on the [APIs.io](https://apis.io/) network: Borrower application API and Borrower application result API. Tagged areas include Company, Financing, Payments, Lending, and Veterinary.


  The Scratchpay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Scratchpay''s developer surface includes documentation, API reference, support, engineering blog, authentication, sandbox, and 15 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 51.0
    developer_ergonomics: 33.3
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scratchpay/refs/heads/main/screenshots/scratchpay-2026-09-02T154604.png
security:
- kind: authentication
  name: Scratchpay Authentication
  slug: scratchpay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scratchpay Domain Security
  slug: scratchpay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: scratchpay
tags:
- Company
- Financing
- Payments
- Lending
- Veterinary
- Healthcare
- Fintech
- Buy Now Pay Later
- Point-of-Sale
website: https://scratchpay.com
---
