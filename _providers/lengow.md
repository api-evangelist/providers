---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Lengow Agentic Access
  operation_count: 14
  slug: lengow-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 2
apis:
- baseURL: https://api.lengow.io
  baseurl_source: declared
  description: The Authentication API from Lengow — 2 operation(s) for authentication.
  name: Lengow Authentication API
  slug: lengow-authentication-api
- baseURL: https://api.lengow.io
  baseurl_source: declared
  description: The Catalogues API from Lengow — 5 operation(s) for catalogues.
  name: Lengow Catalogues API
  slug: lengow-catalogues-api
- baseURL: https://api.lengow.io
  baseurl_source: declared
  description: The Marketplaces API from Lengow — 1 operation(s) for marketplaces.
  name: Lengow Marketplaces API
  slug: lengow-marketplaces-api
- baseURL: https://api.lengow.io
  baseurl_source: declared
  description: The Rate limits API from Lengow — 1 operation(s) for rate limits.
  name: Lengow Rate limits API
  slug: lengow-rate-limits-api
artifact_total: 10
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lengow-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lengow-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lengow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lengow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lengow.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lengow.io/
- group: docs
  title: ''
  type: Documentation
  url: https://api.lengow.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lengow.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.lengow.com/hc/en-us/articles/360011980072-Getting-started-on-the-Lengow-API
- group: operate
  title: ''
  type: Support
  url: https://help.lengow.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.lengow.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://blog.lengow.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lengow
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lengow.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://my.lengow.io/
- group: start
  title: ''
  type: Login
  url: https://my.lengow.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lengow.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lengow.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lengow.io/#api-release-notes
- group: build
  title: ''
  type: Packages
  url: packages/lengow-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lengow-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lengow-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/lengow-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lengow-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/lengow-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lengow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lengow-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lengow-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lengow-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lengow-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lengow-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lengow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lengow-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lengow-channel-execution-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://api.lengow.io/.well-known/security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.lengow.com/gdpr/
created: '2026-08-17'
description: Lengow is a French e-commerce automation platform (Nantes, founded 2009; part of the Lengow group alongside Netrivals and NetMonitor) that connects merchant product catalogues to marketplaces, price-comparison sites and advertising channels across Europe. Its Channel Execution suite covers NetMarkets for marketplace management and NetAmplify for advertising feed management, plus NetRivals price intelligence and NetMonitor reseller monitoring. Lengow publishes a public REST API at api.lengow.io covering order retrieval and order actions (accept, refuse, ship, cancel, refund) across marketplaces, marketplace metadata, invoice and delivery documents, Zalando ZFS warehouse communication, product integration reports, and a beta v1.0 catalogue API for products and attributes. Authentication is a session token exchanged from an account access_token + secret pair. First-party e-commerce plugins are published on GitHub for PrestaShop, Magento 2, WooCommerce, Shopware 6 and Salesforce
  Commerce Cloud.
image: https://www.lengow.com/wp-content/uploads/2024/12/Lengow_Homepage_Loop.png
layout: provider
modified: '2026-08-17'
name: Lengow
nav: Providers
network: true
overview: 'Lengow publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Catalogues API, Marketplaces API, and 1 more. Tagged areas include Company, Software-as-a-Service, E-Commerce, Marketplaces, and Product Feeds.


  Lengow''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Lengow Plans Pricing
  plan_count: 3
  slug: lengow-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Lengow Rate Limits
  slug: lengow-rate-limits
score:
  band: strong
  composite: 59.3
  coverage:
    artifact_dirs: 21
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 56.1
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lengow/refs/heads/main/screenshots/lengow-2026-09-02T150237.png
security:
- kind: authentication
  name: Lengow Authentication
  slug: lengow-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lengow Domain Security
  slug: lengow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lengow Vulnerability Disclosure
  slug: lengow-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: lengow
tags:
- Company
- Software-as-a-Service
- E-Commerce
- Marketplaces
- Product Feeds
- Retail
- Advertising
- Order Management
- Price Intelligence
- France
website: https://www.lengow.com/
---
