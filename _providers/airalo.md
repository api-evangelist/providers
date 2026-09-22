---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-09-21'
api_count: 1
apis:
- baseURL: https://partners-api.airalo.com
  baseurl_source: declared
  description: REST API (v2) for Airalo partners to browse eSIM packages and product information, place orders (synchronous, asynchronous with webhook callback, future-dated, top-ups and eSIM vouchers), retrieve eSI
  name: Airalo Partner API
  slug: airalo-partner-api
artifact_total: 9
asyncapis:
- description: ''
  name: Airalo Webhooks
  slug: airalo-webhooks
common:
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/airsims/
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/airsims
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Airalo
- group: company
  title: ''
  type: Website
  url: https://www.airalo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.partners.airalo.com/introduction-752219m0
- group: start
  title: ''
  type: Portal
  url: https://partners.airalo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.partners.airalo.com/introduction-752219m0
- group: docs
  title: ''
  type: APIReference
  url: https://developers.partners.airalo.com/endpoints-2663076f0
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.partners.airalo.com/quick-start-2508979f0
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/packages/airalo-packages.yml
  title: ''
  type: Packages
  url: packages/airalo-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/packages/airalo-packages.yml
  title: ''
  type: SDKs
  url: packages/airalo-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Airalo
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/llms/airalo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airalo-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developers.partners.airalo.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/authentication/airalo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/airalo-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/conventions/airalo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/airalo-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/conformance/airalo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airalo-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/lifecycle/airalo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/airalo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.airalo.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.partners.airalo.com/faq-752238m0
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/changelog/airalo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/airalo-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/plans/airalo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airalo-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/rate-limits/airalo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/airalo-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/sandbox/airalo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/airalo-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/asyncapi/airalo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/airalo-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/errors/airalo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/airalo-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/data-model/airalo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/airalo-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/security/airalo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airalo-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.airalo.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airalo/refs/heads/main/security/airalo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/airalo-trust-center.yml
- group: design
  title: ''
  type: AccessibilityConformance
  url: https://www.airalo.com/m/resources/accessibility-statement
- group: operate
  title: ''
  type: Support
  url: https://www.airalo.com/help
- group: company
  title: ''
  type: Blog
  url: https://blog.partners.airalo.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.partners.airalo.com/sign-in
- group: start
  title: ''
  type: SignUp
  url: https://app.partners.airalo.com/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://www.airalo.com/all-esim
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airalo.com/more-info/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airalo.com/more-info/privacy-policy
- group: commercial
  title: ''
  type: Legal
  url: https://www.airalo.com/legal
- group: company
  title: ''
  type: Newsroom
  url: https://www.airalo.com/about-us/newsroom
- group: company
  title: ''
  type: About
  url: https://www.airalo.com/about-us/about-airalo
- group: company
  title: ''
  type: Careers
  url: https://www.airalo.com/airalo-careers/job-vacancies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airalocom/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/airalocom
- group: learn
  title: ''
  type: Youtube
  url: https://www.youtube.com/@Airalo_Partners
- group: build
  title: ''
  type: Plugin
  url: https://wordpress.org/plugins/airalo/
created: '2026-09-19'
description: Airalo is the world's first and largest eSIM marketplace, founded in 2019 and headquartered in Singapore, selling prepaid travel data plans (local, regional and global eSIMs) for 200+ countries and regions to consumers through its website and iOS/Android apps, and to businesses through Airalo Partners. The Airalo Partner API (v2, partners-api.airalo.com) lets 6,500+ partner companies — airlines, travel businesses, financial institutions, MNOs/MVNOs, resellers and enterprises — browse the eSIM package catalog, place synchronous, asynchronous and future-dated orders, top up and manage eSIMs, retrieve installation instructions and QR codes, monitor data/voice/text usage, request refunds, check balances and subscribe to HMAC-signed webhooks for async orders, low-data and credit-limit events. Airalo also ships official PHP, Node.js and Python SDKs, a WooCommerce plugin, and a white-label eSIM platform, and publishes a real llms.txt and per-endpoint OpenAPI 3.0.1 fragments on its
  Apidog-hosted developer portal.
image: https://cdn-revamp.airalo.com/img/logo-homepage-header.png
layout: provider
mcp_servers:
- description: ''
  name: MCP candidate (no server published)
  slug: mcp-candidate-no-server-published
modified: '2026-09-19'
name: Airalo
nav: Providers
network: true
overview: 'Airalo publishes 1 API on the [APIs.io](https://apis.io/) network: Partner API. Tagged areas include Company, eSIM, Telecommunications, Travel, and Connectivity.


  The Airalo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Airalo''s developer surface includes developer portal, documentation, API reference, getting-started guide, authentication, changelog, sandbox, and 40 more developer resources.'
plans:
- name: Airalo Plans Pricing
  plan_count: 0
  slug: airalo-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 9
  name: Airalo Rate Limits
  slug: airalo-rate-limits
score:
  band: strong
  composite: 63.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 65.7
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 63.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Airalo Authentication
  slug: airalo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Airalo Domain Security
  slug: airalo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Airalo Vulnerability Disclosure
  slug: airalo-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Airalo Trust Center
  slug: airalo-trust-center
  summary_line: trust center published
slug: airalo
tags:
- Company
- eSIM
- Telecommunications
- Travel
- Connectivity
- Mobile Data
- Roaming
- Partner API
- Webhook
- Singapore
website: https://www.airalo.com
---
