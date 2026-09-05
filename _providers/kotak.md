---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://kotak.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.kotak.bank.in/en/home.html — a different registrable domain (kotak.com -> bank.in), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'The Kotak Mahindra Bank enterprise open-banking API platform. A curated corporate banking API stack of 39 published API products across six categories — Account Services, Payment Services, Collection '
  name: Kotak API Platform
  slug: kotak-api-platform
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://kotak.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.kotak.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.kotak.bank.in/en/open-banking.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.kotak.bank.in/explore
- group: start
  title: ''
  type: GettingStarted
  url: https://api.kotak.bank.in/auth/registration
- group: start
  title: ''
  type: SignUp
  url: https://api.kotak.bank.in/auth/registration
- group: start
  title: ''
  type: Login
  url: https://api.kotak.bank.in/auth/login
- group: operate
  title: ''
  type: Support
  url: https://api.kotak.bank.in/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.kotak.bank.in/en/help-center.html
- group: operate
  title: ''
  type: FAQ
  url: https://api.kotak.bank.in/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.kotak.bank.in/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kotak.com/en/privacy-policy.html
- group: company
  title: ''
  type: Partners
  url: https://api.kotak.bank.in/connectedbanking
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kotak-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kotak-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kotak-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kotak-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kotak-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kotak-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/kotak-api-catalog.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kotak-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kotak-llms.txt
created: '2026-07-17'
description: Kotak Mahindra Bank Limited is an Indian private-sector bank headquartered in Mumbai, and the first non-banking finance company in India to convert into a full commercial bank. Alongside retail, corporate, and NRI banking it operates the Kotak API Platform (api.kotak.com), an enterprise open-banking developer portal offering a curated stack of corporate banking APIs across six product categories — Account Services (balance enquiry, account statement), Payment Services (24x7 NEFT/RTGS/IFT, CMS bulk payments, corporate IMPS remittance, name enquiry, UPI merchant cashback), Collection Services (UPI web collect and autopay, e-collection virtual accounts, NACH physical/e-mandate/Aadhaar e-mandate, BBPS agent and biller integration, direct debit queryback), Trade Finance (import/export letters of credit, standby LCs, bankers guarantees, collections, inward/outward remittance, shipping guarantee, document upload), Onboarding (application, dedupe, offers, OTP), and Authorization Services
  (OAuth 2.0 access tokens). The platform is aimed at fintechs, ERP providers, and NBFCs through its Connected Banking partner program, and pairs an integrated sandbox testing environment with per-product documentation and downloadable kits that are released after developer registration and login.
image: https://api.kotak.bank.in/commonIcons/API_Banking_Kotak_Bank_Logo.png
layout: provider
modified: '2026-07-19'
name: Kotak Mahindra Bank
nav: Providers
network: true
overview: 'Kotak Mahindra Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Financial-Services, Open Banking, and Payments.


  Kotak Mahindra Bank''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, FAQ, sandbox, and 15 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 27.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: IN
      standard: upi
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kotak/refs/heads/main/screenshots/kotak-2026-07-25T224245.png
security:
- kind: authentication
  name: Kotak Authentication
  slug: kotak-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Kotak Domain Security
  slug: kotak-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: kotak
tags:
- Company
- Banking
- Financial-Services
- Open Banking
- Payments
- Collection
- Trade Finance
- Corporate Banking
- India
- UPI
website: https://kotak.com
---
