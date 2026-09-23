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
    agent_skills: derived
    agentic_access: false
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
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-09-23'
api_count: 5
apis:
- description: Brands report new orders, order updates (including partial returns), and cancellations to Button server-to-server, passing the Button Attribution Token (btn_ref) captured by the Merchant Library; docu
  name: Button Order API
  slug: button-order-api
- baseURL: https://api.usebutton.com/v1/brands
  baseurl_source: declared
  description: The Accounts API from Button — 2 operation(s) for accounts.
  name: Button Accounts API
  slug: usebutton-accounts-api
- baseURL: https://api.usebutton.com/v1/brands
  baseurl_source: declared
  description: The Brands Api API from Button — 1 operation(s) for brands api.
  name: Button Brands Api
  slug: usebutton-brands-api-api
- baseURL: https://api.usebutton.com/v1/brands
  baseurl_source: declared
  description: The Create API from Button — 2 operation(s) for create.
  name: Button Create API
  slug: usebutton-create-api
- baseURL: https://api.usebutton.com/v1/brands
  baseurl_source: declared
  description: The Links Api API from Button — 1 operation(s) for links api.
  name: Button Links Api
  slug: usebutton-links-api-api
- baseURL: https://api.usebutton.com/v1/brands
  baseurl_source: declared
  description: The Offers API from Button — 1 operation(s) for offers.
  name: Button Offers API
  slug: usebutton-offers-api
- baseURL: https://api.usebutton.com/v1/brands
  baseurl_source: declared
  description: The Transactions API from Button — 1 operation(s) for transactions.
  name: Button Transactions API
  slug: usebutton-transactions-api
artifact_total: 25
asyncapis:
- description: ''
  name: Usebutton Webhooks
  slug: usebutton-webhooks
collections:
- collection_type: postman
  name: billing-api Accounts API
  slug: postman-usebutton-accounts-api
- collection_type: postman
  name: billing-api Accounts Brands Api API
  slug: postman-usebutton-brands-api-api
- collection_type: postman
  name: billing-api Accounts Create API
  slug: postman-usebutton-create-api
- collection_type: postman
  name: billing-api Accounts Links Api API
  slug: postman-usebutton-links-api-api
- collection_type: postman
  name: billing-api Accounts Offers API
  slug: postman-usebutton-offers-api
- collection_type: postman
  name: billing-api Accounts Transactions API
  slug: postman-usebutton-transactions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: billing-api Accounts API
  slug: open-usebutton-accounts-api
- collection_type: open
  name: billing-api Accounts Brands Api API
  slug: open-usebutton-brands-api-api
- collection_type: open
  name: billing-api Accounts Create API
  slug: open-usebutton-create-api
- collection_type: open
  name: billing-api Accounts Links Api API
  slug: open-usebutton-links-api-api
- collection_type: open
  name: billing-api Accounts Offers API
  slug: open-usebutton-offers-api
- collection_type: open
  name: billing-api Accounts Transactions API
  slug: open-usebutton-transactions-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/overlays/usebutton-billing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/usebutton-billing-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/button/overview
- group: company
  title: ''
  type: Website
  url: https://usebutton.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.usebutton.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.usebutton.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.usebutton.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.usebutton.com/reference/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.usebutton.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.usebutton.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/button
- group: start
  title: ''
  type: Login
  url: https://app.usebutton.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usebutton.com/support/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usebutton.com/support/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usebutton.com
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/changelog/usebutton-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/usebutton-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.usebutton.com/changelog
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/lifecycle/usebutton-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/usebutton-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/authentication/usebutton-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usebutton-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/conventions/usebutton-conventions.yml
  title: ''
  type: Conventions
  url: conventions/usebutton-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/errors/usebutton-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/usebutton-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/asyncapi/usebutton-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/usebutton-webhooks.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/sandbox/usebutton-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/usebutton-sandbox.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/packages/usebutton-packages.yml
  title: ''
  type: Packages
  url: packages/usebutton-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/packages/usebutton-packages.yml
  title: ''
  type: SDKs
  url: packages/usebutton-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/mcp/usebutton-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/usebutton-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/llms/usebutton-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usebutton-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/well-known/usebutton-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usebutton-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/conformance/usebutton-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usebutton-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.usebutton.com/support/security
- group: auth
  title: ''
  type: Security
  url: https://www.usebutton.com/support/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/data-model/usebutton-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usebutton-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/skills/usebutton-offers-to-link.md
  title: ''
  type: AgentSkill
  url: skills/usebutton-offers-to-link.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/skills/usebutton-billing-reconciliation.md
  title: ''
  type: AgentSkill
  url: skills/usebutton-billing-reconciliation.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/skills/usebutton-creator-shortlinks.md
  title: ''
  type: AgentSkill
  url: skills/usebutton-creator-shortlinks.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/security/usebutton-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/usebutton-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/security/usebutton-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/usebutton-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/security/usebutton-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usebutton-domain-security.yml
created: '2026-07-17'
description: 'Button (usebutton.com) is a mobile commerce technology company whose platform connects Publishers and Brands in a two-sided marketplace: publishers deep-link their users into retailer apps and sites with full attribution, and brands acquire and re-engage customers through those optimized journeys. Its server-to-server APIs cover personalized Offers, attributed Link and Shortlink generation (including Amazon creator links), Brand partnership details, Billing/affiliation transaction reporting, and Order reporting, complemented by Publisher SDKs, Merchant Libraries, and HMAC-signed transaction webhooks.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usebutton.png
layout: provider
modified: '2026-09-16'
name: Button
nav: Providers
network: true
overview: 'Button publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Brands Api, Create API, and 3 more. Tagged areas include Commerce, Mobile Commerce, Affiliates, Attribution, and Deep Linking.


  The Button catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Button''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 30 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 62.5
    developer_ergonomics: 58.9
    discoverability: 81.5
    operational_transparency: 44.7
  previous_composite: 49.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/usebutton/refs/heads/main/screenshots/usebutton-2026-08-17T082649.png
security:
- kind: authentication
  name: Usebutton Authentication
  slug: usebutton-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Usebutton Domain Security
  slug: usebutton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Usebutton Vulnerability Disclosure
  slug: usebutton-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Usebutton Trust Center
  slug: usebutton-trust-center
  summary_line: SOC 2, GDPR
slug: usebutton
tags:
- Commerce
- Mobile Commerce
- Affiliates
- Attribution
- Deep Linking
- Offers
- Publishers
- Retail
website: https://usebutton.com
---
