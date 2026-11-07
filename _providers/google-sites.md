---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Google Sites Data API is a Google Data (GData) v1.4 Atom/XML API for classic Google Sites. Five feeds — Site, Content, Revision, Activity and ACL — let a client list, create, copy and rename sites
  name: Google Sites Data API
  slug: google-sites-data-api
artifact_total: 9
common:
- group: start
  title: ''
  type: Sandbox
  url: https://play.google.com/console/about/
- group: other
  href: https://artifacts.apis.io/google-sites/hosts/google-sites-hosts.yml
  title: ''
  type: Hosts
  url: hosts/google-sites-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/workspace
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/workspace/sites/docs/developers_guide
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/workspace/sites/docs/1.0/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/guides/get-started
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/workspace/sites/support
- group: company
  title: ''
  type: Blog
  url: https://developers.googleblog.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: commercial
  title: ''
  type: Pricing
  url: https://workspace.google.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://accounts.google.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- group: operate
  href: https://artifacts.apis.io/google-sites/lifecycle/google-sites-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/google-sites-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/google-sites/lifecycle/google-sites-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-sites-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/google-sites/authentication/google-sites-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-sites-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-sites/scopes/google-sites-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-sites-scopes.yml
- group: design
  href: https://artifacts.apis.io/google-sites/conventions/google-sites-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-sites-conventions.yml
- group: design
  href: https://artifacts.apis.io/google-sites/data-model/google-sites-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-sites-data-model.yml
- group: design
  href: https://artifacts.apis.io/google-sites/errors/google-sites-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-sites-problem-types.yml
- group: design
  href: https://artifacts.apis.io/google-sites/conformance/google-sites-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-sites-conformance.yml
- group: auth
  href: https://artifacts.apis.io/google-sites/conformance/google-sites-conformance.yml
  title: ''
  type: Compliance
  url: conformance/google-sites-conformance.yml
- group: build
  href: https://artifacts.apis.io/google-sites/packages/google-sites-packages.yml
  title: ''
  type: Packages
  url: packages/google-sites-packages.yml
- group: build
  href: https://artifacts.apis.io/google-sites/packages/google-sites-packages.yml
  title: ''
  type: SDKs
  url: packages/google-sites-packages.yml
- group: operate
  href: https://artifacts.apis.io/google-sites/changelog/google-sites-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-sites-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/google-sites/plans/google-sites-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-sites-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-sites/rate-limits/google-sites-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-sites-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-sites/finops/google-sites-finops.yml
  title: ''
  type: FinOps
  url: finops/google-sites-finops.yml
- group: agent
  href: https://artifacts.apis.io/google-sites/well-known/google-sites-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-sites-well-known.yml
- group: auth
  href: https://artifacts.apis.io/google-sites/well-known/google-sites-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-sites-security.txt
- group: agent
  href: https://artifacts.apis.io/google-sites/llms/google-sites-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-sites-llms.txt
- group: auth
  href: https://artifacts.apis.io/google-sites/security/google-sites-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/google-sites-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-sites/security/google-sites-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-sites-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-sites/security/google-sites-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-sites-domain-security.yml
coverage:
  checked: '2026-11-04'
  detail: The deprecated Google Sites Data API (GData v1.4 Atom feeds at sites.google.com/feeds) is documented only in prose on developers.google.com; Google publishes no OpenAPI or discovery document and no API for the current Google Sites.
  evidence:
  - status: 200
    url: https://developers.google.com/workspace/sites/docs/1.0/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2024-01-01'
description: Google Sites is Google's no-code website builder, bundled with Google Workspace and available at no cost to consumer Google Accounts. Its only public programmatic surface is the Google Sites Data API, a Google Data (GData) v1.4 Atom/XML API served from https://sites.google.com/feeds/ across five feeds — Site, Content, Revision, Activity and ACL — that list and create sites, read and write pages, announcements, file cabinets, list pages and attachments, walk revision history and activity, and manage sharing permissions. Google marks the API DEPRECATED on every documentation page and states it "might stop working at any time"; critically, it reaches only classic Google Sites and cannot touch the rebuilt Sites launched on 2016-11-22, which is the only version a user can create today. Google publishes no OpenAPI or discovery document for it, no replacement API for new Sites, no webhooks, no rate limits and no MCP server. Authorization is OAuth 2.0 with one coarse read-and-write
  scope. The two first-party client libraries are the generic GData Python and Java libraries, both archived, last published in 2013 and 2012.
finops:
- has_sources: true
  method: derived
  name: Google Sites Finops
  primary_unit: user
  service_category: ''
  slug: google-sites-finops
  template: false
image: https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png
layout: provider
modified: '2026-09-12'
name: Google Sites
nav: Providers
network: true
overview: 'Google Sites is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Content Management, Google Workspace, Websites, and Website Builder.


  Google Sites'' developer surface includes sandbox, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Google Sites Plans Pricing
  plan_count: 4
  slug: google-sites-plans-pricing
- name: Google Sites Price Estimates
  plan_count: 0
  slug: google-sites-price-estimates
random_paper: 10
rate_limits:
- limit_count: 0
  name: Google Sites Rate Limits
  slug: google-sites-rate-limits
scopes:
- name: Google Sites Scopes
  scope_count: 1
  slug: google-sites-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 80.4
    operational_transparency: 52.6
  previous_composite: 52.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/google-sites/google-sites-2026-06-20T182235.png
security:
- kind: authentication
  name: Google Sites Authentication
  slug: google-sites-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Google Sites Domain Security
  slug: google-sites-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Sites Vulnerability Disclosure
  slug: google-sites-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-sites
tags:
- Collaboration
- Content Management
- Google Workspace
- Websites
- Website Builder
- CMS
- Publishing
- Productivity
- Deprecated APIs
- GData
website: https://www.google.com/
---
