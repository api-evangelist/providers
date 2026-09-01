---
agent_readiness:
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: Partner-facing eligibility lookup that returns the list of US states and the Hiscox products offered by profession, used to determine whether a risk can be quoted before a quote is requested. Listed a
  name: Hiscox Eligibility API
  slug: hiscox-eligibility-api
- description: Partner-facing quoting API that returns a competitive general liability, professional liability, business owner's policy (BOP) and/or cyber quote for purchase via partner portals or APIs. Listed as Ac
  name: Hiscox Quote API v4
  slug: hiscox-quote-api
- description: Partner-facing payment API that initiates the Hiscox policy payment process, completing the quote-to-buy flow for partner-distributed small business policies. Listed as Active on the public Hiscox Dev
  name: Hiscox Setup Payment API
  slug: hiscox-setup-payment-api
- description: Hiscox London Market API-based solution for underwriting small cargo and stock throughput risks, launched 30 June 2025 and distributed through broker partners acting as coverholders. Provides near-ins
  name: Hiscox Cargo API
  slug: hiscox-cargo-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hiscox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hiscoxgroup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hiscox.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hiscox.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.hiscox.com/apis
- group: operate
  title: ''
  type: FAQ
  url: https://developer.hiscox.com/frequently-asked-questions
- group: operate
  title: ''
  type: Support
  url: https://developer.hiscox.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.hiscox.com/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hiscox.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://developer.hiscox.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hiscox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hiscox
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.hiscox.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.hiscoxgroup.com/news/blog
- group: auth
  title: ''
  type: Compliance
  url: https://www.hiscoxgroup.com/news/blog/hiscox-gains-cyber-essentials-plus-accreditation
- group: auth
  title: ''
  type: Authentication
  url: authentication/hiscox-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hiscox-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hiscox-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hiscox-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hiscox-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/hiscox-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hiscox-llms.txt
created: '2026-07-25'
description: 'Hiscox Ltd is a diversified international specialist insurance and reinsurance group with roots in the Lloyd''s of London market dating to 1901, domiciled in Bermuda and listed on the London Stock Exchange, operating from 31 offices across 13 countries. Its home market is the United Kingdom, where it underwrites through three segments: Hiscox Retail (small business, professional and specialty personal lines sold direct and through brokers in the UK, Europe and the USA), Hiscox London Market (larger and more complex specialty risks written out of London for a worldwide client base, including marine, energy, aviation, specialty property and casualty, and cyber), and Hiscox Re & ILS (reinsurance and insurance-linked securities). Its API posture is partner-gated rather than public. Hiscox operates a genuine first-party developer portal at developer.hiscox.com serving its US small-business arm, and that portal publicly enumerates three active APIs - Eligibility, Quote v4 and Setup
  Payment - but every reference document, sandbox credential and OpenAPI/Swagger file sits behind a login that is only issued after a Hiscox Partnership Manager approves a commercial partnership. There is no self-serve signup, no downloadable specification and no public claims or FNOL API. The group does ship APIs outside that portal: Hiscox London Market launched a Cargo API for small cargo and stock throughput risks in June 2025, built in-house and distributed through broker partners as coverholders, but it has no developer portal listing, no documentation and no specification - it is announced through the newsroom and reached through a broker partnership. Authentication is OAuth 2.0 plus a partner-issued API key over TLS 1.2 only, all APIs are REST, and both XML and JSON are supported. Hiscox''s most concrete open-standards footprint is ACORD rather than REST: in July 2025 ACORD and Howden announced that ACORD Standards for digital accounting and invoicing went live in the UK retail insurance
  market with Hiscox as the receiving insurer, responding in real time to Howden''s digital invoices through the ACORD Solutions Group ADEPT (ACORD Data Exchange Platform & Translator) receiver portal.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Hiscox
nav: Providers
network: true
overview: 'Hiscox publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Property and Casualty, Specialty Insurance, and Cyber Insurance.


  Hiscox''s developer surface includes documentation, API reference, FAQ, support, signup flow, getting-started guide, engineering blog, and 15 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 33.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hiscox/refs/heads/main/screenshots/hiscox-2026-07-25T221253.png
security:
- kind: authentication
  name: Hiscox Authentication
  slug: hiscox-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Hiscox Domain Security
  slug: hiscox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hiscox
tags:
- Insurance
- United Kingdom
- Property and Casualty
- Specialty Insurance
- Cyber Insurance
- Underwriting
- Reinsurance
- Lloyd's of London
- Small Business Insurance
- Quotes
- ACORD
- Carrier
- Cargo
- Marine
- Payments
- API Gateway
website: https://www.hiscoxgroup.com/
---
