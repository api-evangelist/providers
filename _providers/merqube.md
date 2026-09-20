---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-09-19'
api_count: 3
apis:
- baseURL: https://api.merqube.com
  baseurl_source: declared
  description: The api API from MerQube — 1 operation(s) for api.
  name: MerQube API
  slug: merqube-api-api
- baseURL: https://api.merqube.com
  baseurl_source: declared
  description: The helper API from MerQube — 14 operation(s) for helper.
  name: MerQube Helper API
  slug: merqube-helper-api
- baseURL: https://api.merqube.com
  baseurl_source: declared
  description: tickers for various providers
  name: MerQube Identifier API
  slug: merqube-identifier-api
- baseURL: https://api.merqube.com
  baseurl_source: declared
  description: APIs for MerQube Indices
  name: MerQube Index API
  slug: merqube-index-api
- baseURL: https://api.merqube.com
  baseurl_source: declared
  description: Equity securities (legacy non secapi)
  name: MerQube Legacy Equity Security API
  slug: merqube-legacy-equity-security-api
- baseURL: https://api.merqube.com
  baseurl_source: declared
  description: Option Pricing APIs
  name: MerQube Options API
  slug: merqube-options-api
- baseURL: https://api.merqube.com
  baseurl_source: declared
  description: list of portfolio handlers
  name: MerQube Portfolio Handler API
  slug: merqube-portfolio-handler-api
- baseURL: https://api.merqube.com
  baseurl_source: declared
  description: securities
  name: MerQube Security API
  slug: merqube-security-api
- baseURL: https://api.merqube.com
  baseurl_source: declared
  description: lists of securities
  name: MerQube Security List API
  slug: merqube-security-list-api
artifact_total: 13
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/security/merqube-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/merqube-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://merqube.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://merqube.stoplight.io/
- group: docs
  title: ''
  type: Documentation
  url: https://merqube.stoplight.io/
- group: docs
  title: ''
  type: APIReference
  url: https://www.merqube.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://merqube.stoplight.io/docs/api/p6s6m4p35ehfv-authentication
- group: operate
  title: ''
  type: Support
  url: https://support.merqube.com/
- group: company
  title: ''
  type: Blog
  url: https://merqube.com/news/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/merqube
- group: start
  title: ''
  type: SignUp
  url: https://merqube.com/register
- group: start
  title: ''
  type: Login
  url: https://merqube.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://merqube.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://merqube.com/privacy-notice
- group: operate
  title: ''
  type: Contact
  url: https://merqube.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://merqube.com/faqs
- group: other
  title: ''
  type: Governance
  url: https://merqube.com/governance
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/openapi/_original/merqube-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/merqube-api-openapi.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/authentication/merqube-authentication.yml
  title: ''
  type: Authentication
  url: authentication/merqube-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/conventions/merqube-conventions.yml
  title: ''
  type: Conventions
  url: conventions/merqube-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/errors/merqube-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/merqube-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/data-model/merqube-data-model.yml
  title: ''
  type: DataModel
  url: data-model/merqube-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/overlays/merqube-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/merqube-api-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/conformance/merqube-conformance.yml
  title: ''
  type: Conformance
  url: conformance/merqube-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/lifecycle/merqube-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/merqube-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/packages/merqube-packages.yml
  title: ''
  type: Packages
  url: packages/merqube-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/packages/merqube-packages.yml
  title: ''
  type: SDKs
  url: packages/merqube-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/cli/merqube-cli.yml
  title: ''
  type: CLI
  url: cli/merqube-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/rate-limits/merqube-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/merqube-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/plans/merqube-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/merqube-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/changelog/merqube-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/merqube-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/sandbox/merqube-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/merqube-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/llms/merqube-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/merqube-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-25'
description: 'MerQube is an index technology company that designs, calculates and administers rules-based investment strategies and custom indices for banks, asset managers and ETF issuers. Its cloud-native platform is API-first: the public MerQube API (api.merqube.com) exposes an IndexAPI for creating, editing, running and deleting index manifests, target portfolios, index documents and identifiers, and a SecAPI for retrieving security metrics, index levels, portfolios and statistics across equities, futures, options and MerQube indices. The company publishes a link-resolved OpenAPI 3.1 description from the API host itself, a browsable rendering at merqube.com/api, a Stoplight documentation portal, and a first-party Apache-2.0 Python client library on PyPI and GitHub.'
image: https://merqube.com/MerQube_Favicon_apple-touch-icon.png
layout: provider
modified: '2026-09-16'
name: MerQube
nav: Providers
network: true
overview: 'MerQube publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Helper API, Identifier API, and 7 more. Tagged areas include Company, Financial-Services, Index Data, Market Data, and Capital Markets.


  MerQube''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, FAQ, and 26 more developer resources.'
plans:
- name: Merqube Plans Pricing
  plan_count: 0
  slug: merqube-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Merqube Rate Limits
  slug: merqube-rate-limits
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 48.1
    developer_ergonomics: 70.8
    discoverability: 74.1
    operational_transparency: 18.4
  previous_composite: 39.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/merqube/refs/heads/main/screenshots/merqube-2026-09-02T150527.png
security:
- kind: authentication
  name: Merqube Authentication
  slug: merqube-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Merqube Domain Security
  slug: merqube-domain-security
  summary_line: TLSv1.3 · HSTS
slug: merqube
tags:
- Company
- Financial-Services
- Index Data
- Market Data
- Capital Markets
- investment-strategies
- Asset Management
- ETFs
- Structured Products
- Quantitative Finance
- OpenAPI
website: https://merqube.com/
---
