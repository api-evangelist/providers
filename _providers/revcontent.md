---
access_model:
  confidence: high
  label: Account-representative gated API access
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Revcontent Agentic Access
  operation_count: 43
  slug: revcontent-agentic-access
  summary_line: 43 operations · 21 acting
api_count: 12
apis:
- description: REST API providing programmatic access to RevContent's advertising platform for managing campaigns (boosts), widgets, content, targeting, widget blacklisting, conversion pixels, sub accounts, and stat
  name: RevContent Stats & Management API
  slug: revcontent-stats-management-api
- description: OAuth 2.0 client-credentials token issuance and account reactivation.
  name: RevContent Access API
  slug: revcontent-access-api
- description: Create, update, list, archive and report on advertising campaigns.
  name: RevContent Campaigns (Boosts) API
  slug: revcontent-boosts-api
- description: CCPA consumer data access and deletion requests for publishers.
  name: RevContent CCPA API
  slug: revcontent-ccpa-api
- description: Ad creatives attached to campaigns, and their per-widget performance.
  name: RevContent Content API
  slug: revcontent-content-api
- description: Conversion pixel management used by CPA-optimized campaigns.
  name: RevContent Conversions API
  slug: revcontent-conversions-api
- description: Reference lookups for browsers, countries, devices, DMAs, languages, operating systems and regions — the source of every valid targeting code.
  name: RevContent Helpers API
  slug: revcontent-helpers-api
- description: Create, edit, list and enable/disable child accounts under a parent account.
  name: RevContent Sub Accounts API
  slug: revcontent-sub-accounts-api
- description: Per-campaign widget targeting and widget-level bid overrides.
  name: RevContent Targeting API
  slug: revcontent-targeting-api
- description: Publisher widget inventory, geo statistics and Sub ID reporting.
  name: RevContent Widgets API
  slug: revcontent-widgets-api
- description: Publisher-owned content injected into that publisher's own widget.
  name: RevContent Widget Internal Content API
  slug: revcontent-widget-internal-content-api
- description: Campaign-level widget blacklisting.
  name: RevContent Widget Optimizer API
  slug: revcontent-widget-optimizer-api
artifact_total: 62
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revcontent-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revcontent-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revcontent-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/revcontent-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/revcontent-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/revcontent-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/revcontent-lifecycle.yml
- group: design
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
  title: ''
  type: DataModel
  url: data-model/revcontent-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/revcontent-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/revcontent-packages.yml
- group: design
  title: ''
  type: Components
  url: components/revcontent-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revcontent-llms.txt
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/revcontent-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/revcontent-context.jsonld
- group: design
  title: ''
  type: Rules
  url: rules/revcontent-jsonschema-spectral-rules.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/revcontent-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/revcontent-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/revcontent-rate-limits.yml
- group: commercial
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
- name: Revcontent Finops
  service_category: ''
  slug: revcontent-finops
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
overview: 'RevContent publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Access API, Campaigns (Boosts) API, CCPA API, and 8 more. Tagged areas include Native Advertising, Content Recommendation, Ad Network, Publisher Monetization, and Programmatic Advertising.


  The RevContent catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RevContent''s developer surface includes authentication, code examples, changelog, documentation, API reference, getting-started guide, support, and 33 more developer resources.'
plans:
- name: Revcontent Plans Pricing
  plan_count: 0
  slug: revcontent-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Revcontent Rate Limits
  slug: revcontent-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: RevContent API Rules
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
  band: strong
  composite: 60.5
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 84.8
    contract_quality: 69.1
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 84.8
    operational_transparency: 28.9
  previous_composite: 60.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revcontent/refs/heads/main/screenshots/revcontent-2026-06-20T193044.png
security:
- kind: authentication
  name: Revcontent Authentication
  slug: revcontent-authentication
  summary_line: oauth2/http · 1 scheme
- kind: domain-security
  name: Revcontent Domain Security
  slug: revcontent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: revcontent
tags:
- Native Advertising
- Content Recommendation
- Ad Network
- Publisher Monetization
- Programmatic Advertising
- Advertising Technology
- Campaign Management
- Audience Targeting
- Conversion Tracking
- Marketing
website: https://www.revcontent.com
---
