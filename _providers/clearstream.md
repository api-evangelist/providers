---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-05'
api_count: 8
apis:
- description: 'Xact via SWIFT delivers settlement, custody, asset servicing and reporting messages over the SWIFTNet FIN network. The interface uses ISO 15022 MT messages today and is being migrated to ISO 20022 MX '
  name: Clearstream Xact via SWIFT
  slug: xact-via-swift
- description: 'Xact File Transfer offers bulk and report-style exchange of settlement, custody, and collateral messages over SWIFTNet FileAct. Files may be delivered in ISO 15022, ISO 20022, PDF, XML or XLS formats '
  name: Clearstream Xact File Transfer
  slug: xact-file-transfer
- description: Xact Web Portal is the browser-based interface to ClearstreamXact for instructing settlement, custody and collateral activity, monitoring status, and reviewing reports. It complements the SWIFT and Fi
  name: Clearstream Xact Web Portal
  slug: xact-web-portal
- description: CASCADE is the German central securities depository (CSD) settlement platform. CASCADE is reachable via SWIFT FIN/FileAct messages and via MQ-based host-to-host connectivity for instructing domestic a
  name: Clearstream CASCADE (CSD)
  slug: cascade
- description: Vestima is Clearstream's investment fund processing platform. It routes subscription, redemption, switch and transfer orders for mutual funds, ETFs, hedge funds and alternatives, and integrates with S
  name: Clearstream Vestima
  slug: vestima
- description: 'CmaX is Clearstream''s triparty collateral management platform, automating collateral allocation, optimisation, margining and substitution across repo, securities lending and OTC derivative exposures. '
  name: Clearstream CmaX (Triparty Collateral)
  slug: cmax
- description: The Clearstream API Platform is the REST tier of ClearstreamXact, reachable at https://api.clearstream.com with a pre-production twin at https://api-t2s-test.clearstream.com. It issues JWT bearer toke
  name: Clearstream API Platform (Playground)
  slug: api-platform
- description: 'The first business API Clearstream published on its API platform: User Management (SCIM2), an implementation of the SCIM 2.0 standard for provisioning, maintaining and monitoring Xact Web Portal users'
  name: Clearstream Xact User Management (SCIM 2.0)
  slug: scim2-user-management
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clearstream-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clearstream
- group: company
  title: ''
  type: Website
  url: https://www.clearstream.com/
- group: docs
  title: ''
  type: Connectivity Manuals
  url: https://www.clearstream.com/clearstream-en/keydocuments-1-/icsd-1-/connectivity-manuals
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clearstream-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clearstream-rules.yml
- group: start
  title: ''
  type: Portal
  url: https://www.clearstream.com/clearstream-en/securities-services
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.developer.deutsche-boerse.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.clearstream.com/clearstream-en/res-library/connectivity/clearstream-api-services-2916788
- group: start
  title: ''
  type: GettingStarted
  url: https://www.clearstream.com/caas/v1/media/2934048/data/3fa3fec668d8dd198e9bed4df879b26b/api-developer-guide.pdf
- group: operate
  title: ''
  type: Support
  url: https://www.clearstream.com/clearstream-en/about-clearstream/office-locations
- group: start
  title: ''
  type: SignUp
  url: https://www.clearstream.com/clearstream-en/about-clearstream/becoming-a-clearstream-client-1277376
- group: company
  title: ''
  type: Blog
  url: https://www.clearstream.com/clearstream-en/newsroom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.developer.deutsche-boerse.com/files/DBAG_API_Platform_Terms_of_Use.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearstream.com/clearstream-en/privacy-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://www.clearstream.com/clearstream-en/res-library/operational-news
- group: auth
  title: ''
  type: Authentication
  url: authentication/clearstream-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clearstream-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clearstream-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clearstream-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clearstream-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clearstream-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/clearstream-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clearstream-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clearstream-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clearstream-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/clearstream-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clearstream-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/clearstream-mcp.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clearstream.com/clearstream-en/res-library/key-documents/clearstream-fee-schedule-1274812
- group: operate
  title: ''
  type: Roadmap
  url: https://www.clearstream.com/clearstream-en/res-library/releases-and-initiatives
created: '2024-01-15'
description: 'Clearstream Banking S.A. is the Deutsche Borse Group post-trade infrastructure business, providing settlement, custody, collateral management and investment-fund order routing for international securities. Its programmable surface has two layers. The incumbent layer is regulated post-trade messaging: clients connect through ClearstreamXact (Xact Web Portal, Xact File Transfer over SWIFTNet FileAct, and Xact via SWIFT FIN), CASCADE via SWIFT and MQ, Vestima for fund order routing and CmaX for triparty collateral, exchanging ISO 15022 MT and ISO 20022 MX messages whose specifications Clearstream publishes to SWIFT MyStandards, with migration to ISO 20022 driven by the SWIFT CBPR+ programme. The newer layer is a genuine REST platform at api.clearstream.com, running an OAuth 2.0 password grant hardened by mandatory mutual TLS, whose first published API is SCIM 2.0 user management for the Xact Web Portal; a free synthetic Playground API and a CmaX collateral surface are live alongside
  it. The OpenAPI definitions are published into the Deutsche Borse Digital Business Platform catalogue, which requires registration.'
finops:
- name: Clearstream Finops
  service_category: API
  slug: clearstream-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clearstream.png
jsonld:
- class_count: 0
  name: Clearstream Context
  property_count: 6
  slug: clearstream-context
layout: provider
modified: '2026-09-05'
name: Clearstream
nav: Providers
network: true
overview: 'Clearstream publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Platform, Capital Markets, Collateral Management, Custody, and Financial-Services.


  The Clearstream catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clearstream''s developer surface includes developer portal, documentation, getting-started guide, support, signup flow, engineering blog, authentication, and 24 more developer resources.'
plans:
- name: Clearstream Plans Pricing
  plan_count: 0
  slug: clearstream-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Clearstream Rate Limits
  slug: clearstream-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Clearstream API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 8
  slug: clearstream-rules
scopes:
- name: Clearstream Scopes
  scope_count: 4
  slug: clearstream-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.0
    catalog_earned_first_party: 0.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 26.4
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 63.6
    contract_quality: 6.7
    developer_ergonomics: 52.4
    discoverability: 72.2
    governance: 63.6
    operational_transparency: 36.8
  previous_composite: 20.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/clearstream/refs/heads/main/screenshots/clearstream-2026-06-20T174506.png
security:
- kind: authentication
  name: Clearstream Authentication
  slug: clearstream-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Clearstream Domain Security
  slug: clearstream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearstream
tags:
- API Platform
- Capital Markets
- Collateral Management
- Custody
- Financial-Services
- ISO 15022
- ISO 20022
- Mutual TLS
- OAuth 2.0
- Post-Trade
- Post-Trade Infrastructure
- SCIM
- Securities
- Settlement
- Swift
website: https://www.clearstream.com/
---
