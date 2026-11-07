---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Revcontent Agentic Access
  operation_count: 43
  slug: revcontent-agentic-access
  summary_line: 43 operations · 20 acting
api_count: 3
apis:
- description: REST API providing programmatic access to RevContent's advertising platform for managing campaigns (boosts), widgets, content, targeting, widget blacklisting, conversion pixels, sub accounts, and stat
  name: RevContent Stats & Management API
  slug: revcontent-stats-management-api
- baseURL: https://api.revcontent.io
  baseurl_source: declared
  description: OAuth 2.0 client-credentials token issuance and account reactivation.
  name: RevContent Access API
  slug: revcontent-access-api
- baseURL: https://api.revcontent.io
  baseurl_source: declared
  description: CCPA consumer data access and deletion requests for publishers.
  name: RevContent CCPA API
  slug: revcontent-ccpa-api
- baseURL: https://api.revcontent.io
  baseurl_source: declared
  description: Ad creatives attached to campaigns, and their per-widget performance.
  name: RevContent Content API
  slug: revcontent-content-api
- baseURL: https://api.revcontent.io
  baseurl_source: declared
  description: Conversion pixel management used by CPA-optimized campaigns.
  name: RevContent Conversions API
  slug: revcontent-conversions-api
- baseURL: https://api.revcontent.io
  baseurl_source: declared
  description: Reference lookups for browsers, countries, devices, DMAs, languages, operating systems and regions — the source of every valid targeting code.
  name: RevContent Helpers API
  slug: revcontent-helpers-api
- baseURL: https://api.revcontent.io
  baseurl_source: declared
  description: Per-campaign widget targeting and widget-level bid overrides.
  name: RevContent Targeting API
  slug: revcontent-targeting-api
- baseURL: https://api.revcontent.io
  baseurl_source: declared
  description: Publisher-owned content injected into that publisher's own widget.
  name: RevContent Widget Internal Content API
  slug: revcontent-widget-internal-content-api
- baseURL: https://api.revcontent.io
  baseurl_source: declared
  description: Campaign-level widget blacklisting.
  name: RevContent Widget Optimizer API
  slug: revcontent-widget-optimizer-api
- baseURL: https://api.revcontent.io
  baseurl_source: declared
  description: Create, update, list, archive and report on advertising campaigns (boosts).
  name: RevContent Campaigns API
  slug: revcontent-campaigns-api
- baseURL: https://api.revcontent.io
  baseurl_source: declared
  description: Publisher widget inventory, geo statistics and Sub ID reporting.
  name: RevContent Widget API
  slug: revcontent-widget-api
- baseURL: https://api.revcontent.io
  baseurl_source: declared
  description: Create, edit, list and enable/disable sub accounts under a parent account.
  name: RevContent Subaccounts API
  slug: revcontent-subaccounts-api
artifact_total: 66
collections:
- collection_type: open
  name: RevContent Access API
  slug: open-revcontent-access-api
- collection_type: open
  name: RevContent Campaigns API
  slug: open-revcontent-boosts-api
- collection_type: open
  name: RevContent CCPA API
  slug: open-revcontent-ccpa-api
- collection_type: open
  name: RevContent Content API
  slug: open-revcontent-content-api
- collection_type: open
  name: RevContent Conversions API
  slug: open-revcontent-conversions-api
- collection_type: open
  name: RevContent Helpers API
  slug: open-revcontent-helpers-api
- collection_type: open
  name: RevContent Sub Accounts API
  slug: open-revcontent-sub-accounts-api
- collection_type: open
  name: RevContent Targeting API
  slug: open-revcontent-targeting-api
- collection_type: open
  name: RevContent Widget Internal Content API
  slug: open-revcontent-widget-internal-content-api
- collection_type: open
  name: RevContent Widget Optimizer API
  slug: open-revcontent-widget-optimizer-api
- collection_type: open
  name: RevContent Widget API
  slug: open-revcontent-widgets-api
common:
- group: other
  href: https://artifacts.apis.io/revcontent/overlays/revcontent-sub-accounts-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/revcontent-sub-accounts-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/revcontent/overlays/revcontent-boosts-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/revcontent-boosts-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/revcontent/overlays/revcontent-widgets-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/revcontent-widgets-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/revcontent/agentic-access/revcontent-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/revcontent-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/revcontent/security/revcontent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/revcontent-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/revcontent/authentication/revcontent-authentication.yml
  title: ''
  type: Authentication
  url: authentication/revcontent-authentication.yml
- group: auth
  href: https://artifacts.apis.io/revcontent/scopes/revcontent-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/revcontent-scopes.yml
- group: design
  href: https://artifacts.apis.io/revcontent/conventions/revcontent-conventions.yml
  title: ''
  type: Conventions
  url: conventions/revcontent-conventions.yml
- group: design
  href: https://artifacts.apis.io/revcontent/errors/revcontent-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/revcontent-problem-types.yml
- group: design
  href: https://artifacts.apis.io/revcontent/lifecycle/revcontent-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/revcontent-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/revcontent/conformance/revcontent-conformance.yml
  title: ''
  type: Conformance
  url: conformance/revcontent-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.revcontent.com/policy/security
- group: auth
  title: ''
  type: Security
  url: https://www.revcontent.com/policy/security
- group: design
  href: https://artifacts.apis.io/revcontent/data-model/revcontent-data-model.yml
  title: ''
  type: DataModel
  url: data-model/revcontent-data-model.yml
- group: build
  href: https://artifacts.apis.io/revcontent/packages/revcontent-packages.yml
  title: ''
  type: Packages
  url: packages/revcontent-packages.yml
- group: build
  href: https://artifacts.apis.io/revcontent/packages/revcontent-packages.yml
  title: ''
  type: SDKs
  url: packages/revcontent-packages.yml
- group: design
  href: https://artifacts.apis.io/revcontent/components/revcontent-components.yml
  title: ''
  type: Components
  url: components/revcontent-components.yml
- group: agent
  href: https://artifacts.apis.io/revcontent/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/revcontent/llms/revcontent-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/revcontent-llms.txt
- group: design
  href: https://artifacts.apis.io/revcontent/vocabulary/revcontent-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/revcontent-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/revcontent/json-ld/revcontent-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/revcontent-context.jsonld
- group: design
  href: https://artifacts.apis.io/revcontent/rules/revcontent-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/revcontent-jsonschema-spectral-rules.yml
- group: build
  href: https://artifacts.apis.io/revcontent/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
- group: docs
  href: https://artifacts.apis.io/revcontent/json-schema/_index.yml
  title: ''
  type: JSONSchema
  url: json-schema/_index.yml
- group: operate
  href: https://artifacts.apis.io/revcontent/changelog/revcontent-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/revcontent-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/revcontent/plans/revcontent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/revcontent-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/revcontent/rate-limits/revcontent-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/revcontent-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/revcontent/finops/revcontent-finops.yml
  title: ''
  type: FinOps
  url: finops/revcontent-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.revcontent.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.revcontent.io/docs/stats/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.revcontent.com/knowledge/native-api
- group: docs
  title: ''
  type: APIReference
  url: https://api.revcontent.io/docs/stats/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.revcontent.com/knowledge/publisher-advertiser-api-requests
- group: operate
  title: ''
  type: Support
  url: https://www.revcontent.com/resources/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.revcontent.com/knowledge
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RevContent
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revcontent
- group: company
  title: ''
  type: Blog
  url: https://www.revcontent.com/resources/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.revcontent.com/registration
- group: start
  title: ''
  type: Login
  url: https://www.revcontent.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.revcontent.com/policy/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.revcontent.com/policy/cookie-policy
- group: other
  title: ''
  type: X
  url: https://x.com/RevContent
created: '2026-06-13'
description: RevContent is a performance-driven native advertising and content recommendation network offering a REST API for managing widgets, campaigns (boosts), ad content, audience targeting, bidding, conversion pixels, sub accounts, and performance reporting. Publishers and advertisers access the platform through OAuth 2.0 client-credentials authenticated endpoints to programmatically control campaign settings, device, OS, browser, language and geo targeting, widget blacklisting, content delivery, and statistical reporting at scale. RevContent publishes its machine-readable contract as apiDoc rather than OpenAPI, at https://api.revcontent.io/docs/stats/api_data.json, covering 43 operations across eleven groups.
examples:
- key_count: 4
  name: Access Token Response
  slug: access-token-response
- key_count: 2
  name: Campaign List Error Response
  slug: campaign-list-error-response
- key_count: 2
  name: Campaign List Response
  slug: campaign-list-response
- key_count: 2
  name: Campaign Performance Response
  slug: campaign-performance-response
- key_count: 1
  name: Campaign Settings Request
  slug: campaign-settings-request
- key_count: 2
  name: Campaign Widget Stats Response
  slug: campaign-widget-stats-response
- key_count: 1
  name: Ccpa Data Request
  slug: ccpa-data-request
- key_count: 5
  name: Ccpa Submit Request
  slug: ccpa-submit-request
- key_count: 2
  name: Content List Response
  slug: content-list-response
- key_count: 2
  name: Conversion List Response
  slug: conversion-list-response
- key_count: 2
  name: Helpers Countries Response
  slug: helpers-countries-response
- key_count: 2
  name: Helpers Devices Response
  slug: helpers-devices-response
- key_count: 2
  name: Helpers Operating Systems Response
  slug: helpers-operating-systems-response
- key_count: 2
  name: Sub Account List Response
  slug: sub-account-list-response
- key_count: 1
  name: Widget Blacklist Add Request
  slug: widget-blacklist-add-request
- key_count: 1
  name: Widget Blacklist Response
  slug: widget-blacklist-response
- key_count: 2
  name: Widget List Response
  slug: widget-list-response
- key_count: 2
  name: Widget Subid Stats Response
  slug: widget-subid-stats-response
finops:
- has_sources: true
  method: derived
  name: Revcontent Finops
  primary_unit: ''
  service_category: ''
  slug: revcontent-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revcontent.png
json_schemas:
- name: AccessToken
  property_count: 4
  slug: access-token
- name: CampaignCreateRequest
  property_count: 26
  slug: campaign-create-request
- name: CampaignSettingsRequest
  property_count: 26
  slug: campaign-settings-request
- name: Campaign
  property_count: 40
  slug: campaign
- name: CCPADataRequest
  property_count: 5
  slug: ccpa-data-request
- name: ContentItem
  property_count: 19
  slug: content-item
- name: Conversion
  property_count: 3
  slug: conversion
- name: Error
  property_count: 2
  slug: error
- name: SubAccount
  property_count: 4
  slug: sub-account
- name: WidgetTarget
  property_count: 15
  slug: widget-target
- name: Widget
  property_count: 8
  slug: widget
jsonld:
- class_count: 9
  name: Revcontent Context
  property_count: 34
  slug: revcontent-context
layout: provider
modified: '2026-08-13'
name: RevContent
nav: Providers
network: true
overview: 'RevContent publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access API, CCPA API, Content API, and 9 more. Tagged areas include Native Advertising, Content Recommendation, Ad Network, Publisher Monetization, and Programmatic Advertising.


  The RevContent catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RevContent''s developer surface includes authentication, code examples, changelog, documentation, API reference, getting-started guide, support, and 36 more developer resources.'
plans:
- name: Revcontent Plans Pricing
  plan_count: 0
  slug: revcontent-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Revcontent Rate Limits
  slug: revcontent-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 5
  extends: []
  name: RevContent — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: revcontent-jsonschema-spectral-rules
scopes:
- name: Revcontent Scopes
  scope_count: 2
  slug: revcontent-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 58.8
    catalog_earned_first_party: 0.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 41.7
    contract_quality: 25.1
    developer_ergonomics: 66.1
    discoverability: 71.4
    operational_transparency: 28.9
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
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
screenshot: https://apis.io/screenshots/revcontent/revcontent-2026-06-20T193044.png
security:
- kind: authentication
  name: Revcontent Authentication
  slug: revcontent-authentication
  summary_line: oauth2/http · 1 scheme
- kind: domain-security
  name: Revcontent Domain Security
  slug: revcontent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: Handle a RevContent CCPA data request
  slug: revcontent-ccpa-data-request
- name: Set up RevContent CPA conversion tracking
  slug: revcontent-conversion-tracking
- name: Launch a RevContent campaign
  slug: revcontent-launch-campaign
- name: Optimize RevContent campaign spend by widget
  slug: revcontent-optimize-widget-spend
- name: Pull RevContent publisher widget reporting
  slug: revcontent-publisher-reporting
slug: revcontent
tags:
- Native Advertising
- Content Recommendation
- Ad Network
- Publisher Monetization
- Programmatic Advertising
- AdTech
- Campaign Management
- Audience Targeting
- Conversion Tracking
- Marketing
website: https://www.revcontent.com
---
