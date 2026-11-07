---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.3
  scored_at: '2026-11-06'
api_count: 6
apis:
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The Asset Custom Fieldsets API from Knak — 2 operation(s) for asset custom fieldsets.
  name: Knak Asset Custom Fieldsets API
  slug: knak-asset-custom-fieldsets-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The Assets API from Knak — 7 operation(s) for assets.
  name: Knak Assets API
  slug: knak-assets-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The AvailablePlatforms API from Knak — 1 operation(s) for availableplatforms.
  name: Knak AvailablePlatforms API
  slug: knak-availableplatforms-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The Brands API from Knak — 1 operation(s) for brands.
  name: Knak Brands API
  slug: knak-brands-api
- baseURL: https://send.knak.io/api/public/v1
  baseurl_source: declared
  description: Create, retrieve and list contacts in Knak Send.
  name: Knak Contacts API
  slug: knak-contacts-api
- baseURL: https://yourService.com/yourDamApi
  baseurl_source: declared
  description: Endpoints to retrieve DAM Assets. This is a contract the CUSTOMER implements so Knak can browse images from their own digital asset management system; the base URL is the placeholder host Knak publish
  name: Knak DAM Assets API
  slug: knak-dam-assets-api
- baseURL: https://send.knak.io/api/public/v1
  baseurl_source: declared
  description: Create and list custom contact fields (schema metadata).
  name: Knak Fields API
  slug: knak-fields-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The Integrations API from Knak — 1 operation(s) for integrations.
  name: Knak Integrations API
  slug: knak-integrations-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The MarketingPlatformSyncs API from Knak — 1 operation(s) for marketingplatformsyncs.
  name: Knak MarketingPlatformSyncs API
  slug: knak-marketingplatformsyncs-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The MergeTags API from Knak — 2 operation(s) for mergetags.
  name: Knak MergeTags API
  slug: knak-mergetags-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The Modules API from Knak — 3 operation(s) for modules.
  name: Knak Modules API
  slug: knak-modules-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The Project Management API from Knak — 1 operation(s) for project management.
  name: Knak Project Management API
  slug: knak-project-management-api
- baseURL: https://yourService.com/yourValidationApi
  baseurl_source: declared
  description: The health-check ping every Knak customer-implemented contract must expose — 1 operation (GET /v1/ping). Implemented by the CUSTOMER, not by Knak; the base URL is the placeholder host Knak publishes i
  name: Knak Status API
  slug: knak-status-api
- baseURL: https://yourService.com/your-sync-location-api
  baseurl_source: declared
  description: Endpoints to retrieve Sync Location. This is a contract the CUSTOMER implements so their own logic determines and restricts the sync location for Knak assets; the base URL is the placeholder host Knak
  name: Knak Sync Location API
  slug: knak-sync-location-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The SyncStatuses API from Knak — 1 operation(s) for syncstatuses.
  name: Knak SyncStatuses API
  slug: knak-syncstatuses-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The Themes API from Knak — 2 operation(s) for themes.
  name: Knak Themes API
  slug: knak-themes-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The TranslationRequests API from Knak — 5 operation(s) for translationrequests.
  name: Knak TranslationRequests API
  slug: knak-translationrequests-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The Users API from Knak — 4 operation(s) for users.
  name: Knak Users API
  slug: knak-users-api
- baseURL: https://yourService.com/yourValidationApi
  baseurl_source: declared
  description: The Custom Validator contract — 1 operation. This is a contract the CUSTOMER implements so Knak can run assets through their own validation pipeline; the base URL is the placeholder host Knak publishe
  name: Knak Validation API
  slug: knak-validation-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The asset.approval_status_updated API from Knak — 0 operation(s) for asset.approval_status_updated.
  name: Knak Asset.approval Status Updated API
  slug: knak-asset-approval-status-updated-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The asset.created API from Knak — 0 operation(s) for asset.created.
  name: Knak Asset.created API
  slug: knak-asset-created-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The asset.sync_confirmation_responded API from Knak — 0 operation(s) for asset.sync_confirmation_responded.
  name: Knak Asset.sync Confirmation Responded API
  slug: knak-asset-sync-confirmation-responded-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The asset.sync_requested API from Knak — 0 operation(s) for asset.sync_requested.
  name: Knak Asset.sync Requested API
  slug: knak-asset-sync-requested-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The asset.translation_requested API from Knak — 0 operation(s) for asset.translation_requested.
  name: Knak Asset.translation Requested API
  slug: knak-asset-translation-requested-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The translation_request.created API from Knak — 0 operation(s) for translation_request.created.
  name: Knak Translation Request.created API
  slug: knak-translation-request-created-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: Endpoints that need to be implemented to support OAuth2
  name: Knak O Auth2 API
  slug: knak-oauth2-api
- baseURL: https://enterprise.knak.io/api/published/v1
  baseurl_source: declared
  description: The Asset Folders API from Knak — 2 operation(s) for asset folders.
  name: Knak Asset Folders API
  slug: knak-asset-folders-api
artifact_total: 64
asyncapis:
- description: ''
  name: Knak Enterprise Webhooks
  slug: knak-enterprise-webhooks
collections:
- collection_type: open
  name: Knak Enterprise API — Asset Custom Fieldsets
  slug: open-knak-asset-custom-fieldsets-api
- collection_type: open
  name: Knak Enterprise API — AssetFolders
  slug: open-knak-assetfolders-api
- collection_type: open
  name: Knak Enterprise API — Assets
  slug: open-knak-assets-api
- collection_type: open
  name: Knak Enterprise API — AvailablePlatforms
  slug: open-knak-availableplatforms-api
- collection_type: open
  name: Knak Enterprise API — Brands
  slug: open-knak-brands-api
- collection_type: open
  name: Knak Send Contacts API Reference — Contacts
  slug: open-knak-contacts-api
- collection_type: open
  name: Custom Digital Asset Management (DAM) API Reference — DAM Assets
  slug: open-knak-dam-assets-api
- collection_type: open
  name: Knak Send Contacts API Reference — Fields
  slug: open-knak-fields-api
- collection_type: open
  name: Knak Enterprise API — Integrations
  slug: open-knak-integrations-api
- collection_type: open
  name: Knak Enterprise API — MarketingPlatformSyncs
  slug: open-knak-marketingplatformsyncs-api
- collection_type: open
  name: Knak Enterprise API — MergeTags
  slug: open-knak-mergetags-api
- collection_type: open
  name: Knak Enterprise API — Modules
  slug: open-knak-modules-api
- collection_type: open
  name: Custom Digital Asset Management (DAM) API Reference — OAuth2
  slug: open-knak-oauth2-api
- collection_type: open
  name: Knak Enterprise API — Project Management
  slug: open-knak-project-management-api
- collection_type: open
  name: Knak Custom Validator API Reference — Status
  slug: open-knak-status-api
- collection_type: open
  name: Custom Sync Location API Reference — Sync Location
  slug: open-knak-sync-location-api
- collection_type: open
  name: Knak Enterprise API — SyncStatuses
  slug: open-knak-syncstatuses-api
- collection_type: open
  name: Knak Enterprise API — Themes
  slug: open-knak-themes-api
- collection_type: open
  name: Knak Enterprise API — TranslationRequests
  slug: open-knak-translationrequests-api
- collection_type: open
  name: Knak Enterprise API — Users
  slug: open-knak-users-api
- collection_type: open
  name: Knak Custom Validator API Reference — Validation
  slug: open-knak-validation-api
common:
- group: other
  href: https://artifacts.apis.io/knak/capabilities/knak-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/knak-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/knak/security/knak-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/knak-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://knak.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.knak.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.knak.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.knak.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.knak.com/welcome/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://help.knak.io/en/
- group: company
  title: ''
  type: Blog
  url: https://knak.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://knak.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://enterprise.knak.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://knak.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://knak.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.knak.io/
- group: auth
  title: ''
  type: Compliance
  url: https://knak.com/security/
- group: auth
  title: ''
  type: Security
  url: https://knak.com/security/
- group: auth
  href: https://artifacts.apis.io/knak/security/knak-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/knak-vulnerability-disclosure.yml
- group: docs
  href: https://artifacts.apis.io/knak/openapi/_original/knak-dam-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/knak-dam-openapi-original.yml
- group: docs
  href: https://artifacts.apis.io/knak/openapi/_original/knak-custom-validator-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/knak-custom-validator-openapi-original.yml
- group: docs
  href: https://artifacts.apis.io/knak/openapi/_original/knak-custom-sync-location-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/knak-custom-sync-location-openapi-original.yml
- group: agent
  href: https://artifacts.apis.io/knak/mcp/knak-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/knak-mcp.yml
- group: auth
  href: https://artifacts.apis.io/knak/authentication/knak-authentication.yml
  title: ''
  type: Authentication
  url: authentication/knak-authentication.yml
- group: auth
  href: https://artifacts.apis.io/knak/scopes/knak-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/knak-scopes.yml
- group: agent
  href: https://artifacts.apis.io/knak/well-known/knak-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/knak-well-known.yml
- group: design
  href: https://artifacts.apis.io/knak/conventions/knak-conventions.yml
  title: ''
  type: Conventions
  url: conventions/knak-conventions.yml
- group: design
  href: https://artifacts.apis.io/knak/errors/knak-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/knak-problem-types.yml
- group: design
  href: https://artifacts.apis.io/knak/lifecycle/knak-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/knak-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/knak/conformance/knak-conformance.yml
  title: ''
  type: Conformance
  url: conformance/knak-conformance.yml
- group: design
  href: https://artifacts.apis.io/knak/data-model/knak-data-model.yml
  title: ''
  type: DataModel
  url: data-model/knak-data-model.yml
- group: design
  href: https://artifacts.apis.io/knak/asyncapi/knak-enterprise-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/knak-enterprise-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/knak/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/knak/llms/knak-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/knak-llms.txt
- group: auth
  href: https://artifacts.apis.io/knak/security/knak-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/knak-domain-security.yml
- group: other
  href: https://artifacts.apis.io/knak/overlays/knak-enterprise-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knak-enterprise-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knak/overlays/knak-send-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knak-send-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knak/overlays/knak-scim-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knak-scim-overlay.yaml
- group: operate
  href: https://artifacts.apis.io/knak/rate-limits/knak-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/knak-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/knak/plans/knak-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/knak-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/knak/mcp/knak-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/knak-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/knak/errors/knak-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/knak-error-codes.yml
- group: design
  href: https://artifacts.apis.io/knak/components/knak-components.yml
  title: ''
  type: Components
  url: components/knak-components.yml
created: '2026-07-17'
description: Knak is a no-code email and landing page creation platform built for enterprise marketing teams. Marketers design on-brand, responsive emails and landing pages in a drag-and-drop builder, then sync the finished HTML directly into their marketing automation platform (Marketo, Eloqua, Salesforce Marketing Cloud, Braze, HubSpot and others) without writing code or waiting on developers. For technical teams Knak publishes a documented developer surface -- the Knak Enterprise REST API for automating users, assets, themes, modules, brands, folders, merge tags and translation requests; the Knak Send Contacts API; a SCIM 2.0 API for identity-provider driven user provisioning; signed webhooks for asset and translation lifecycle events; a set of customer-implemented integration contracts (Custom DAM, Custom Validator, Custom Sync Location); and a hosted, OAuth 2.1 protected MCP server that lets AI clients generate and browse Knak assets.
finops:
- has_sources: true
  method: derived
  name: Knak Finops
  primary_unit: ''
  service_category: ''
  slug: knak-finops
  template: true
image: https://s3.amazonaws.com/assets.knak.io/img/Knak-Logo-Medium.png
layout: provider
mcp_servers:
- description: Remote MCP server at enterprise.knak.io over HTTP; 7 tools listed.
  name: Knak MCP Server
  slug: knak
modified: '2026-08-13'
name: Knak
nav: Providers
network: true
overview: 'Knak publishes 27 API contracts indexed on the [APIs.io](https://apis.io/) network, including Asset Custom Fieldsets API, Assets API, AvailablePlatforms API, and 24 more. Tagged areas include Company, Email Marketing, Marketing Automation, Landing Pages, and Content Creation.


  The Knak catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Knak''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Knak Plans Pricing
  plan_count: 1
  slug: knak-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Knak Rate Limits
  slug: knak-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Knak API Rules
  rule_count: 61
  severity_counts:
    error: 38
    hint: 0
    info: 3
    warn: 20
  slug: knak-rules
scopes:
- name: Knak Scopes
  scope_count: 1
  slug: knak-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 69.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 61.8
    developer_ergonomics: 58.9
    discoverability: 80.0
    operational_transparency: 65.8
  previous_composite: 69.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 7.4
      total: 27
    mcp: first-party
    skills: derived
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
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/knak/knak-2026-07-25T223953.png
security:
- kind: authentication
  name: Knak Authentication
  slug: knak-authentication
  summary_line: http/oauth2/apiKey · 6 schemes
- kind: domain-security
  name: Knak Domain Security
  slug: knak-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Knak Vulnerability Disclosure
  slug: knak-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Knak Trust Center
  slug: knak-trust-center
  summary_line: SOC 2
skill_count: 5
skills:
- name: Receive and verify Knak webhooks
  slug: knak-consume-webhooks
- name: Generate a Knak email and sync it to a marketing platform
  slug: knak-generate-and-sync-email
- name: Manage Knak Send contacts and fields
  slug: knak-manage-send-contacts
- name: Provision and deprovision Knak users
  slug: knak-provision-users-scim
- name: Run a Knak asset through a translation round trip
  slug: knak-translate-asset
slug: knak
tags:
- Company
- Email Marketing
- Marketing Automation
- Landing Pages
- Content Creation
- Marketing Operations
- Campaign Management
- No-Code
- SCIM
- Webhook
website: https://knak.com/
---
