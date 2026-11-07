---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: 'Dejavoo / iPOSpays APIs as documented publicly on Dejavoo Developer Central (Theneo): iPOSpays iposTransact (sale, preauth, refund, void, tip adjust, ticket, settle batch), recurring-payment subscript'
  name: Dejavoo API
  slug: dejavoo-api
- description: Merchant Onboarding API enabling ISOs and partners to create and edit merchants, stores and TPNs in iPOSpays. Docs state Sandbox URL https://externalapi.ipospays.tech/v1/onboardmerchant and Production
  name: iPOSpays Management API (Merchant Onboarding)
  slug: ipospays-management-api
- description: SPIn Proxy RESTful API for semi-integrating POS systems with Dejavoo payment terminals (Sale, Return, Void, Auth, Capture, Settle and more, e.g. POST v2/Payment/Sale). The docs do not state a base URL
  name: SPIn Proxy RESTful API
  slug: spin-rest-api
artifact_total: 19
common:
- group: design
  href: https://artifacts.apis.io/dejavoo/rules/dejavoo-rules.yml
  title: ''
  type: Spectral
  url: rules/dejavoo-rules.yml
- group: design
  href: https://artifacts.apis.io/dejavoo/json-ld/dejavoo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dejavoo-context.jsonld
- group: design
  href: https://artifacts.apis.io/dejavoo/vocabulary/dejavoo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dejavoo-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dejavoo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dejavoo/data-model/dejavoo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dejavoo-data-model.yml
- group: design
  href: https://artifacts.apis.io/dejavoo/components/dejavoo-components.yml
  title: ''
  type: Components
  url: components/dejavoo-components.yml
- group: operate
  href: https://artifacts.apis.io/dejavoo/changelog/dejavoo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dejavoo-changelog.yml
- group: design
  href: https://artifacts.apis.io/dejavoo/conventions/dejavoo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dejavoo-conventions.yml
- group: start
  href: https://artifacts.apis.io/dejavoo/sandbox/dejavoo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/dejavoo-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://dejavoo.io/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/dejavoo/authentication/dejavoo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dejavoo-authentication.yml
- group: design
  href: https://artifacts.apis.io/dejavoo/lifecycle/dejavoo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dejavoo-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/dejavoo/errors/dejavoo-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/dejavoo-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/dejavoo/errors/dejavoo-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/dejavoo-error-codes.yml
- group: design
  href: https://artifacts.apis.io/dejavoo/errors/dejavoo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dejavoo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dejavoo/conformance/dejavoo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dejavoo-conformance.yml
- group: other
  href: https://artifacts.apis.io/dejavoo/overlays/dejavoo-dejavoo-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dejavoo-dejavoo-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/dejavoo/llms/dejavoo-spin-specification-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dejavoo-spin-specification-llms.txt
- group: agent
  href: https://artifacts.apis.io/dejavoo/llms/dejavoo-spin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dejavoo-spin-llms.txt
- group: agent
  href: https://artifacts.apis.io/dejavoo/llms/dejavoo-management-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dejavoo-management-api-llms.txt
- group: auth
  href: https://artifacts.apis.io/dejavoo/well-known/dejavoo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dejavoo-security.txt
- group: auth
  href: https://artifacts.apis.io/dejavoo/well-known/dejavoo-my-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dejavoo-my-security.txt
- group: agent
  href: https://artifacts.apis.io/dejavoo/well-known/dejavoo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dejavoo-well-known.yml
- group: other
  href: https://artifacts.apis.io/dejavoo/hosts/dejavoo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dejavoo-hosts.yml
- group: build
  href: https://artifacts.apis.io/dejavoo/integrations/dejavoo-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dejavoo-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/dejavoo/vendors/dejavoo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dejavoo-vendors.yml
- group: build
  href: https://artifacts.apis.io/dejavoo/packages/dejavoo-packages.yml
  title: ''
  type: SDKs
  url: packages/dejavoo-packages.yml
- group: build
  href: https://artifacts.apis.io/dejavoo/packages/dejavoo-packages.yml
  title: ''
  type: Packages
  url: packages/dejavoo-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://dejavoo.io/innews/pricing-update/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.theneo.io/get-started/quickstart
- group: company
  title: ''
  type: Website
  url: https://dejavoo.io/
- group: auth
  href: https://artifacts.apis.io/dejavoo/security/dejavoo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dejavoo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dejavoo/security/dejavoo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dejavoo-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.theneo.io/dejavoo/developer-central
- group: docs
  title: ''
  type: Documentation
  url: https://app.theneo.io/dejavoo/developer-central/spin-specification
- group: docs
  title: ''
  type: APIReference
  url: https://app.theneo.io/dejavoo/spin-specification/spin-specification-api
- group: company
  title: ''
  type: Blog
  url: https://dejavoo.io/company/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://dejavoo.io/company/news-center/
- group: operate
  title: ''
  type: Support
  url: https://dejavoo.io/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dejavoo.io/
- group: start
  title: ''
  type: Login
  url: https://my.dejavoo.io/
- group: company
  title: ''
  type: PartnerProgram
  url: https://dejavoo.io/become-a-partner/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dejavoo.io/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dejavoo.io/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dejavoo2006/
created: '2026-11-05'
description: Dejavoo (Dejavoo Systems, dejavoo.io) is a payment technology company that builds Android and Linux payment terminals (P, QD and Z families), terminal applications, DejaPayPro POS, and the iPOSpays omni-commerce gateway with hosted payment pages, virtual terminal, recurring payments, payment links, tokenization and L2/L3 data enrichment. For ISVs and developers it publishes iPOSpays Developer Central, documenting the SPIn semi-integration API for connecting Dejavoo terminals to POS systems, Freedom to Design.js, Hosted Payment Page, Tap to Pay on Android, peripheral SDKs, FEED, OnBoard and Batch Report APIs. Dejavoo sells through ISO and reseller partners and expanded into Israel through its acquisition of Z-Credit.
image: https://dejavoo.io/wp-content/uploads/elementor/thumbs/Dejavoo_Logo-Top-Icon_purple-RGB_R-rkeug1u91p1yt7db7vrga67he6dnuhlk9tq7wsxqmu.webp
json_schemas:
- name: PostApiV1IpostransactPreauthResponse
  property_count: 19
  slug: dejavoo-post-api-v1-ipostransact-preauth-response
- name: PostApiV1IpostransactRefundResponse
  property_count: 19
  slug: dejavoo-post-api-v1-ipostransact-refund-response
- name: PostApiV1IpostransactSaleResponse
  property_count: 19
  slug: dejavoo-post-api-v1-ipostransact-sale-response
- name: PostApiV1IpostransactTicketResponse
  property_count: 19
  slug: dejavoo-post-api-v1-ipostransact-ticket-response
- name: PostApiV1IpostransactTipadjustResponse
  property_count: 19
  slug: dejavoo-post-api-v1-ipostransact-tipadjust-response
- name: PostApiV1IpostransactVoidResponse
  property_count: 19
  slug: dejavoo-post-api-v1-ipostransact-void-response
jsonld:
- class_count: 16
  name: Dejavoo Context
  property_count: 30
  slug: dejavoo-context
layout: provider
modified: '2026-11-05'
name: Dejavoo
nav: Providers
network: true
overview: 'Dejavoo is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Payment Terminals, Point-of-Sale, and Payment Gateway.


  The Dejavoo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dejavoo''s developer surface includes changelog, sandbox, authentication, pricing, getting-started guide, documentation, API reference, and 38 more developer resources.'
plans:
- name: Dejavoo Plans Pricing
  plan_count: 0
  slug: dejavoo-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Dejavoo Rate Limits
  slug: dejavoo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Dejavoo API Rules
  rule_count: 33
  severity_counts:
    error: 30
    hint: 0
    info: 2
    warn: 1
  slug: dejavoo-rules
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 25.2
    developer_ergonomics: 73.2
    discoverability: 64.3
    operational_transparency: 42.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dejavoo Authentication
  slug: dejavoo-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Dejavoo Domain Security
  slug: dejavoo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dejavoo Vulnerability Disclosure
  slug: dejavoo-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: dejavoo-card-sale-lifecycle
  slug: dejavoo-card-sale-lifecycle
- name: dejavoo-merchant-onboarding
  slug: dejavoo-merchant-onboarding
- name: dejavoo-recurring-subscription-management
  slug: dejavoo-recurring-subscription-management
slug: dejavoo
tags:
- Company
- Payments
- Payment Terminals
- Point-of-Sale
- Payment Gateway
- Semi-Integration
- Fintech
- Merchant Services
website: https://dejavoo.io/
---
