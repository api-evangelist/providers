---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sellfy Agentic Access
  operation_count: 10
  slug: sellfy-agentic-access
  summary_line: 10 operations
api_count: 3
apis:
- description: Programmatic access to Sellfy stores.
  name: Sellfy API
  slug: sellfy-api
- baseURL: https://sellfy.com
  baseurl_source: declared
  description: Page content in Markdown.
  name: Sellfy Content API
  slug: sellfy-content-api
- baseURL: https://sellfy.com
  baseurl_source: declared
  description: Files that describe the site and what it offers.
  name: Sellfy Discovery API
  slug: sellfy-discovery-api
- baseURL: https://sellfy.com
  baseurl_source: declared
  description: Sitemaps and syndication feeds.
  name: Sellfy Feeds API
  slug: sellfy-feeds-api
- baseURL: https://api.sellfy.com
  baseurl_source: declared
  description: Validate, activate and revoke license keys sold with Sellfy products. A key is located by its `product_id` and `license_key` pair within your account.
  name: Sellfy Licenses API
  slug: sellfy-licenses-api
- baseURL: https://api.sellfy.com
  baseurl_source: declared
  description: Verify that your integration can reach the API.
  name: Sellfy Ping API
  slug: sellfy-ping-api
artifact_total: 23
common:
- group: other
  href: https://artifacts.apis.io/sellfy/capabilities/sellfy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sellfy-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/sellfy/agentic-access/sellfy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sellfy-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/sellfy/rules/sellfy-rules.yml
  title: ''
  type: Spectral
  url: rules/sellfy-rules.yml
- group: design
  href: https://artifacts.apis.io/sellfy/vocabulary/sellfy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sellfy-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sellfy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/sellfy/changelog/sellfy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sellfy-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sellfy.com
- group: design
  href: https://artifacts.apis.io/sellfy/lifecycle/sellfy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sellfy-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sellfy/errors/sellfy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sellfy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sellfy/conformance/sellfy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sellfy-conformance.yml
- group: other
  href: https://artifacts.apis.io/sellfy/overlays/sellfy-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sellfy-api-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/sellfy/llms/sellfy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sellfy-llms.txt
- group: agent
  href: https://artifacts.apis.io/sellfy/well-known/sellfy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sellfy-well-known.yml
- group: other
  href: https://artifacts.apis.io/sellfy/hosts/sellfy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sellfy-hosts.yml
- group: other
  href: https://artifacts.apis.io/sellfy/vendors/sellfy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sellfy-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://sellfy.com/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sellfy.com/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sellfy
- group: auth
  href: https://artifacts.apis.io/sellfy/security/sellfy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sellfy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sellfy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sellfy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.sellfy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.sellfy.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sellfy.com/category/372-quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://docs.sellfy.com/#contact
- group: company
  title: ''
  type: Blog
  url: https://sellfy.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://sellfy.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://sellfy.com/auth/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sellfy.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sellfy.com/privacy/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://sellfy.com/openapi.json
  - status: null
    url: https://api.sellfy.com/openapi.json
  - status: 401
    url: https://api.sellfy.com/mcp
  - status: 403
    url: https://static.sellfy.com/mcp
  - status: 200
    url: https://sellfy.com/
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Sellfy is an online store builder that enables creators to sell digital products, subscriptions, and physical goods directly to their audience. It offers a clean checkout with zero transaction fees and integrates with PayPal, Stripe, Apple Pay, and Google Pay. Founded in 2011 by Maris Dagis, Sellfy provides a no-code storefront, analytics, marketing tools, and instant digital delivery, helping creators monetize their work without technical barriers.
image: https://d369wu82uo9y4b.cloudfront.net/_astro/sellfy-og.DhZsN1Po.png
json_schemas:
- name: LicenseActivateInput
  property_count: 3
  slug: sellfy-license-activate-input
- name: LicenseActivationResponse
  property_count: 3
  slug: sellfy-license-activation-response
- name: LicenseLookupInput
  property_count: 2
  slug: sellfy-license-lookup-input
- name: LicenseStateResponse
  property_count: 3
  slug: sellfy-license-state-response
- name: MarkdownPage
  property_count: 0
  slug: sellfy-markdown-page
- name: PingResponse
  property_count: 1
  slug: sellfy-ping-response
jsonld:
- class_count: 7
  name: Sellfy Context
  property_count: 12
  slug: sellfy-context
layout: provider
modified: '2026-10-28'
name: Sellfy
nav: Providers
network: true
overview: 'Sellfy publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Content API, Discovery API, Feeds API, and 3 more. Tagged areas include E-Commerce, Digital Products, Software-as-a-Service, Payments, and Creators.


  The Sellfy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sellfy''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Sellfy Plans Pricing
  plan_count: 0
  slug: sellfy-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Sellfy Rate Limits
  slug: sellfy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Sellfy API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: sellfy-rules
scopes:
- name: Sellfy Scopes
  scope_count: 0
  slug: sellfy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 35
    catalog_earned: 62.2
    catalog_earned_first_party: 0.0
    catalog_gap: 52.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.6
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 58.1
    developer_ergonomics: 29.0
    discoverability: 78.6
    operational_transparency: 23.7
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sellfy/sellfy-2026-11-03T143003.png
security:
- kind: authentication
  name: Sellfy Authentication
  slug: sellfy-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sellfy Domain Security
  slug: sellfy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: sellfy-get-llms
  slug: sellfy-get-llms
- name: sellfy-get-pricing
  slug: sellfy-get-pricing
- name: sellfy-licensing
  slug: sellfy-licensing
slug: sellfy
tags:
- E-Commerce
- Digital Products
- Software-as-a-Service
- Payments
- Creators
website: https://sellfy.com/
---
