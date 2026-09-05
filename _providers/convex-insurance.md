---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The partner-gated REST API surface behind Convex Digital Underwriting. Convex publicly describes building "a suite of insurance specific APIs" that let broker and client platforms connect to Convex pr
  name: Convex Digital Underwriting API
  slug: convex-digital-underwriting-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/convex-insurance-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/convex-insurance-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/convex-insurance-llms.txt
- group: company
  title: ''
  type: Website
  url: https://convexin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://convexin.com/underwriting/digital-underwriting/
- group: docs
  title: ''
  type: Documentation
  url: https://convexin.com/underwriting/quick-quote/
- group: docs
  title: ''
  type: Documentation
  url: https://convexin.com/wp-content/uploads/2025/10/Convex-Digital-Underwriting-One-Pager-1025.pdf
- group: company
  title: ''
  type: Website
  url: https://us.convexin.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/convex-insurance
- group: operate
  title: ''
  type: Contact
  url: https://convexin.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://convexin.com/articles/
- group: company
  title: ''
  type: BlogRSS
  url: https://convexin.com/feed/
- group: other
  title: ''
  type: Podcast
  url: https://convexin.com/podcasts/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://convexin.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://convexin.com/privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://convexin.com/legal/
- group: company
  title: ''
  type: InvestorRelations
  url: https://convexin.com/investor-relations/
- group: company
  title: ''
  type: Careers
  url: https://convexin.com/life-at-convex/careers/
created: '2026-07-25'
description: 'Convex Group Limited is an international specialty insurer and reinsurer founded in 2019 by Stephen Catlin and Paul Brand, headquartered in London with operations in Bermuda, Luxembourg, Guernsey and the United States. Convex writes complex commercial and specialty risk across property, casualty, marine, energy, aviation, cyber, political risk and credit, crisis management, accident and health, and equine/livestock/aquaculture, and writes property, casualty and specialty treaty reinsurance through Convex Re Limited in Bermuda and London. Convex Insurance UK Limited is authorised by the Prudential Regulation Authority and regulated by the FCA and PRA; it is a London company-market carrier rather than a Lloyd''s syndicate, and it reported roughly $5.2bn of gross written premium in 2024. Convex operates a named Digital Underwriting function that publicly describes building "a suite of insurance specific APIs" for automated quote and bind on high-volume, low-complexity specialty
  books, delivered either through a Convex-hosted broker portal or by connecting Convex products into a broker''s or client''s existing portal via API. That API programme is real but entirely partner-gated: as of 2026-07-25 Convex publishes no public developer portal, no API reference, no OpenAPI or other machine- readable definition, no sandbox and no self-serve signup. The api.convexin.com host is live but answers every anonymous request with HTTP 401 Unauthorized, the digital.convexin.com broker application is an authenticated Unqork-hosted portal, and the Convex Quick Quote event-insurance surface is behind a broker account registration form. Integration is arranged through the Business Development team, not through documentation. No ACORD, AL3, NGDS or IVANS reference appears anywhere on Convex''s public web presence.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Convex
nav: Providers
network: true
overview: 'Convex publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Property and Casualty, Specialty Insurance, and Reinsurance.


  Convex''s developer surface includes documentation, engineering blog, legal docs, and 15 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/convex-insurance/refs/heads/main/screenshots/convex-insurance-2026-07-25T210353.png
security:
- kind: domain-security
  name: Convex Insurance Domain Security
  slug: convex-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: convex-insurance
tags:
- Insurance
- United Kingdom
- Property and Casualty
- Specialty Insurance
- Reinsurance
- Underwriting
- Claims
- London Market
- Carrier
- Digital Underwriting
website: https://convexin.com/
---
