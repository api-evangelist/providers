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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
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
artifact_total: 28
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
  href: https://artifacts.apis.io/usebutton/capabilities/usebutton-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/usebutton-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/usebutton/overlays/usebutton-billing-overlay.yaml
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
  href: https://artifacts.apis.io/usebutton/changelog/usebutton-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/usebutton-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.usebutton.com/changelog
- group: design
  href: https://artifacts.apis.io/usebutton/lifecycle/usebutton-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/usebutton-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/usebutton/authentication/usebutton-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usebutton-authentication.yml
- group: design
  href: https://artifacts.apis.io/usebutton/conventions/usebutton-conventions.yml
  title: ''
  type: Conventions
  url: conventions/usebutton-conventions.yml
- group: design
  href: https://artifacts.apis.io/usebutton/errors/usebutton-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/usebutton-problem-types.yml
- group: design
  href: https://artifacts.apis.io/usebutton/asyncapi/usebutton-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/usebutton-webhooks.yml
- group: start
  href: https://artifacts.apis.io/usebutton/sandbox/usebutton-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/usebutton-sandbox.yml
- group: build
  href: https://artifacts.apis.io/usebutton/packages/usebutton-packages.yml
  title: ''
  type: Packages
  url: packages/usebutton-packages.yml
- group: build
  href: https://artifacts.apis.io/usebutton/packages/usebutton-packages.yml
  title: ''
  type: SDKs
  url: packages/usebutton-packages.yml
- group: agent
  href: https://artifacts.apis.io/usebutton/mcp/usebutton-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/usebutton-mcp.yml
- group: agent
  href: https://artifacts.apis.io/usebutton/llms/usebutton-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usebutton-llms.txt
- group: agent
  href: https://artifacts.apis.io/usebutton/well-known/usebutton-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usebutton-well-known.yml
- group: design
  href: https://artifacts.apis.io/usebutton/conformance/usebutton-conformance.yml
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
  href: https://artifacts.apis.io/usebutton/data-model/usebutton-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usebutton-data-model.yml
- group: agent
  href: https://artifacts.apis.io/usebutton/skills/usebutton-offers-to-link.md
  title: ''
  type: AgentSkill
  url: skills/usebutton-offers-to-link.md
- group: agent
  href: https://artifacts.apis.io/usebutton/skills/usebutton-billing-reconciliation.md
  title: ''
  type: AgentSkill
  url: skills/usebutton-billing-reconciliation.md
- group: agent
  href: https://artifacts.apis.io/usebutton/skills/usebutton-creator-shortlinks.md
  title: ''
  type: AgentSkill
  url: skills/usebutton-creator-shortlinks.md
- group: auth
  href: https://artifacts.apis.io/usebutton/security/usebutton-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/usebutton-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/usebutton/security/usebutton-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/usebutton-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/usebutton/security/usebutton-domain-security.yml
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
overview: 'Button publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Brands Api, Create API, and 4 more. Tagged areas include Commerce, Mobile Commerce, Affiliates, Attribution, and Deep Linking.


  The Button catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Button''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 31 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Button API Rules
  rule_count: 49
  severity_counts:
    error: 45
    hint: 0
    info: 3
    warn: 1
  slug: usebutton-rules
score:
  band: developing
  composite: 53.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.7
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 57.1
    developer_ergonomics: 63.7
    discoverability: 78.6
    operational_transparency: 44.7
  previous_composite: 52.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/usebutton/usebutton-2026-08-17T082649.png
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
skill_count: 3
skills:
- name: Reconcile commissions with the Billing API
  slug: usebutton-billing-reconciliation
- name: Create attributed creator shortlinks
  slug: usebutton-creator-shortlinks
- name: Fetch offers and generate an attributed link
  slug: usebutton-offers-to-link
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
