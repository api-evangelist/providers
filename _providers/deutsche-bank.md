---
access_model:
  confidence: high
  label: Free self-service sandbox; production access by reviewed go-live request and separate agreement
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://developer.db.com/faq
  - plans/deutsche-bank-plans-pricing.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-09-12'
api_count: 2
apis:
- baseURL: https://api.db.com/gw/dbapi
  baseurl_source: declared
  description: The Deutsche Bank API Program (dbAPI) - 30 published OpenAPI contracts covering cash accounts, transactions and transaction analysis, credit cards, SEPA credit transfer, instant credit transfer and di
  name: Deutsche Bank API Program
  slug: deutsche-bank
- baseURL: https://testmerch.directpos.de/rest-api
  baseurl_source: declared
  description: Merchant Solutions is the payment acceptance and issuing product portfolio of Deutsche Bank - the Merchant-Server II REST platform behind Deutsche Bank's payment gateway. Three contracts are published
  name: Deutsche Bank Merchant Solutions
  slug: merchant-solutions
artifact_total: 11
asyncapis:
- description: ''
  name: Deutsche Bank Webhooks
  slug: deutsche-bank-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.db.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.db.com/apidocumentation
- group: docs
  title: ''
  type: APIReference
  url: https://developer.db.com/apiexplorer
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.db.com/apidocumentation/apigettingstartedguide/introduction
- group: start
  title: ''
  type: SignUp
  url: https://developer.db.com/registration
- group: operate
  title: ''
  type: Support
  url: https://developer.db.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://developer.db.com/faq
- group: company
  title: ''
  type: Blog
  url: https://developer.db.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.db.com/releasenotes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/deutsche-bank-changelog.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.db.com/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.db.com/privacynotice
- group: company
  title: ''
  type: Partners
  url: https://developer.db.com/partnernetwork
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deutschebank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deutsche-bank
- group: company
  title: ''
  type: Website
  url: https://www.db.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/deutsche-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/deutsche-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/deutsche-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/deutsche-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/deutsche-bank-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/deutsche-bank-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/deutsche-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/deutsche-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deutsche-bank-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/deutsche-bank-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/deutsche-bank-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/deutsche-bank-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/deutsche-bank-packages.yml
- group: design
  title: ''
  type: Components
  url: components/deutsche-bank-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/deutsche-bank-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deutsche-bank-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/deutsche-bank-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deutsche-bank-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/deutsche-bank-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/deutsche-bank-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deutsche-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/deutsche-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deutsche-bank-domain-security.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/deutsche-bank-finops.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-addresses-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-ageCertificate-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-banking-cashAccountOpenings-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-cashAccounts-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-creditCardTransactions-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-creditCards-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-customerSolvency-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-assets-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-earningTransactions-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-espSecuritiesAccounts-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-orders-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-performances-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-reports-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-securityAccounts-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-investments-securityTransactions-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-loanOffers-privatebanking-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-loanOffers-privatebanking-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-partners-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-payments-sepaInstantCreditTransfer-v3-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-processingOrders-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-processingOrders-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-sepaCreditTransfer-v3-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-sepaDirectDebit-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-subscriptions-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-swaggers-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-transactionAnalysis-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-transactionAuthorization-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-transactions-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-dbapi-verifyCustomer-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-merchant-solution-callback-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-merchant-solution-callback-v2_1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-merchant-solution-security-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-merchant-solution-security-v2_1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-merchant-solution-services-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-merchant-solution-services-v2.1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deutsche-bank-oneid-fakerock-v1-overlay.yaml
created: '2025-02-08'
description: 'Deutsche Bank is a global financial institution headquartered in Frankfurt, providing retail, corporate and investment banking, asset management and wealth management. Its developer programme - dbAPI, published at developer.db.com - goes well beyond the PSD2 regulatory minimum: 36 first-party OpenAPI 3.0.x contracts covering 195 operations across banking, cards, payments, investments, lending, onboarding, reference data and merchant acquiring, all retrievable from Deutsche Bank''s own public swagger catalogue. The same contracts serve three tenants - Deutsche Bank, norisbank and Postbank. Access is OAuth 2.0 / OpenID Connect with 42 published scopes, PSD2 strong customer authentication exposed as its own API, a free self-service simulation gateway with persona-based test users, and a reviewed go-live process for production data.'
finops:
- name: Deutsche Bank Finops
  service_category: API
  slug: deutsche-bank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deutsche-bank.png
layout: provider
mcp_servers:
- description: Deutsche Bank ships NO Model Context Protocol server. This is a DERIVED candidate tool surface, computed from the read-safe operations in Deutsche Bank's own published OpenAPI contracts so the shape o
  name: Derived candidate tool surface (no server ships)
  slug: derived-candidate-tool-surface-no-server-ships
modified: '2026-09-06'
name: Deutsche Bank
nav: Providers
network: true
overview: 'Deutsche Bank publishes 2 APIs on the [APIs.io](https://apis.io/) network: API Program and Merchant Solutions. Tagged areas include Banking, Financial, Wealth Management, Open Banking, and PSD2.


  The Deutsche Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Deutsche Bank''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, changelog, and 70 more developer resources.'
plans:
- name: Deutsche Bank Plans Pricing
  plan_count: 0
  slug: deutsche-bank-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Deutsche Bank Rate Limits
  slug: deutsche-bank-rate-limits
scopes:
- name: Deutsche Bank Scopes
  scope_count: 0
  slug: deutsche-bank-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 56.2
    developer_ergonomics: 37.5
    discoverability: 75.9
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 51.8
  provenance:
    conformance: derived
    contracts:
      callable: 11.8
      derived: 0
      marker_coverage: 0.0
      total: 36
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 84.8
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/screenshots/deutsche-bank-2026-06-20T175943.png
security:
- kind: authentication
  name: Deutsche Bank Authentication
  slug: deutsche-bank-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Deutsche Bank Domain Security
  slug: deutsche-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deutsche Bank Vulnerability Disclosure
  slug: deutsche-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deutsche-bank
tags:
- Banking
- Financial
- Wealth Management
- Open Banking
- PSD2
- Payments
- SEPA
- Investments
- Credit Cards
- Merchant Solutions
- Germany
- Financial Services
website: https://www.db.com/
---
