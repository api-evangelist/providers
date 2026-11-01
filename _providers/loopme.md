---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Loopme Agentic Access
  operation_count: 3
  slug: loopme-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- baseURL: https://loopme.me/api/s2s
  baseurl_source: declared
  description: 'LoopMe''s server-to-server ad request endpoint. A third-party ad server, exchange or mediation platform sends a GET describing the device, app and user, and LoopMe returns an MRAID ad payload (ad HTML '
  name: LoopMe S2S Ad Serving API
  slug: loopme-ad-serving-api
- baseURL: https://reports.loopme.com/api/v1
  baseurl_source: declared
  description: The Advertiser Reporting API from LoopMe — 1 operation(s) for advertiser reporting.
  name: LoopMe Advertiser Reporting API
  slug: loopme-advertiser-reporting-api
- baseURL: https://reports.loopme.com/api/v1
  baseurl_source: declared
  description: The Publisher Reporting API from LoopMe — 1 operation(s) for publisher reporting.
  name: LoopMe Publisher Reporting API
  slug: loopme-publisher-reporting-api
artifact_total: 14
collections:
- collection_type: open
  name: LoopMe S2S Ad Request API
  slug: open-loopme-ad-serving-api
- collection_type: open
  name: LoopMe Reporting Ad Serving Advertiser Reporting API
  slug: open-loopme-advertiser-reporting-api
- collection_type: open
  name: LoopMe Reporting Ad Serving Publisher Reporting API
  slug: open-loopme-publisher-reporting-api
common:
- group: company
  title: ''
  type: Website
  url: https://loopme.cool
- group: agent
  href: https://artifacts.apis.io/loopme/agentic-access/loopme-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/loopme-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wiki.loopme.cool/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.loopme.cool/
- group: docs
  title: ''
  type: APIReference
  url: https://wiki.loopme.cool/publishers/reporting-api
- group: company
  title: ''
  type: Blog
  url: https://loopme.ai/news-blog/
- group: operate
  title: ''
  type: Support
  url: https://www.loopme.io/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/loopme
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.loopme.com/privacy-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.loopme.com/legal-centre/terms-of-use
- group: build
  href: https://artifacts.apis.io/loopme/packages/loopme-packages.yml
  title: ''
  type: SDKs
  url: packages/loopme-packages.yml
- group: build
  href: https://artifacts.apis.io/loopme/packages/loopme-packages.yml
  title: ''
  type: Packages
  url: packages/loopme-packages.yml
- group: auth
  href: https://artifacts.apis.io/loopme/authentication/loopme-authentication.yml
  title: ''
  type: Authentication
  url: authentication/loopme-authentication.yml
- group: design
  href: https://artifacts.apis.io/loopme/errors/loopme-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/loopme-error-codes.yml
- group: design
  href: https://artifacts.apis.io/loopme/conventions/loopme-conventions.yml
  title: ''
  type: Conventions
  url: conventions/loopme-conventions.yml
- group: design
  href: https://artifacts.apis.io/loopme/lifecycle/loopme-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/loopme-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/loopme/mcp/loopme-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/loopme-mcp.yml
- group: auth
  href: https://artifacts.apis.io/loopme/security/loopme-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loopme-domain-security.yml
- group: design
  href: https://artifacts.apis.io/loopme/data-model/loopme-data-model.yml
  title: ''
  type: DataModel
  url: data-model/loopme-data-model.yml
- group: operate
  href: https://artifacts.apis.io/loopme/changelog/loopme-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/loopme-changelog.yml
- group: agent
  href: https://artifacts.apis.io/loopme/llms/loopme-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loopme-llms.txt
- group: agent
  href: https://artifacts.apis.io/loopme/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/loopme/skills/loopme-request-ad-s2s.md
  title: ''
  type: AgentSkill
  url: skills/loopme-request-ad-s2s.md
- group: commercial
  href: https://artifacts.apis.io/loopme/plans/loopme-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/loopme-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/loopme/rate-limits/loopme-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/loopme-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/loopme/sandbox/loopme-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/loopme-sandbox.yml
- group: design
  href: https://artifacts.apis.io/loopme/conformance/loopme-conformance.yml
  title: ''
  type: Conformance
  url: conformance/loopme-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://legal.loopme.com/privacy-center
- group: auth
  href: https://artifacts.apis.io/loopme/security/loopme-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/loopme-trust-center.yml
- group: design
  href: https://artifacts.apis.io/loopme/components/loopme-components.yml
  title: ''
  type: Components
  url: components/loopme-components.yml
- group: start
  title: ''
  type: Login
  url: https://loopme.ai/product-logins/
created: '2026-07-17'
description: LoopMe is a global brand-performance advertising platform that uses AI to bring brands into mobile and CTV apps. Its products span an AI-powered intelligent marketplace, PurchaseLoop outcome-based brand advertising, the Chartboost in-app monetization platform, and an Audience & Measurement Platform (AMP). For developers, LoopMe exposes a REST Reporting API for publisher (app/site) and advertiser (campaign) statistics, a server-to-server (S2S) ad request API, first-party United SDKs for Android and iOS, and a Prebid.js header-bidding adapter. LoopMe is backed by HV Capital and headquartered in the UK.
image: https://loopme.ai/wp-content/themes/loopme/assets/images/logo.svg
layout: provider
modified: '2026-09-16'
name: LoopMe
nav: Providers
network: true
overview: 'LoopMe publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: S2S Ad Serving API, Advertiser Reporting API, and Publisher Reporting API. Tagged areas include Company, Advertising, AdTech, Mobile Advertising, and CTV.


  LoopMe''s developer surface includes documentation, API reference, engineering blog, support, authentication, changelog, sandbox, and 24 more developer resources.'
plans:
- name: Loopme Plans Pricing
  plan_count: 0
  slug: loopme-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Loopme Rate Limits
  slug: loopme-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 13.2
    developer_ergonomics: 61.3
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/loopme/loopme-2026-08-17T121137.png
security:
- kind: authentication
  name: Loopme Authentication
  slug: loopme-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Loopme Domain Security
  slug: loopme-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Loopme Trust Center
  slug: loopme-trust-center
  summary_line: ePrivacyseal, TAG registered (Trustworthy Accountability Group)
skill_count: 2
skills:
- name: Pull LoopMe reporting statistics
  slug: loopme-pull-reporting
- name: Request a LoopMe ad server-to-server
  slug: loopme-request-ad-s2s
slug: loopme
tags:
- Company
- Advertising
- AdTech
- Mobile Advertising
- CTV
- Reporting
- Programmatic
- Ai Enterprise Software
- SDK
website: https://loopme.cool
---
