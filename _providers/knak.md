---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.1
  scored_at: '2026-08-11'
api_count: 21
apis:
- description: The Asset Custom Fieldsets API from Knak — 2 operation(s) for asset custom fieldsets.
  name: Knak Asset Custom Fieldsets API
  slug: knak-asset-custom-fieldsets-api
- description: The AssetFolders API from Knak — 2 operation(s) for assetfolders.
  name: Knak AssetFolders API
  slug: knak-assetfolders-api
- description: The Assets API from Knak — 7 operation(s) for assets.
  name: Knak Assets API
  slug: knak-assets-api
- description: The AvailablePlatforms API from Knak — 1 operation(s) for availableplatforms.
  name: Knak AvailablePlatforms API
  slug: knak-availableplatforms-api
- description: The Brands API from Knak — 1 operation(s) for brands.
  name: Knak Brands API
  slug: knak-brands-api
- description: Create, retrieve and list contacts in Knak Send.
  name: Knak Contacts API
  slug: knak-contacts-api
- description: Endpoints to retrieve DAM Assets
  name: Knak DAM Assets API
  slug: knak-dam-assets-api
- description: Create and list custom contact fields (schema metadata).
  name: Knak Fields API
  slug: knak-fields-api
- description: The Integrations API from Knak — 1 operation(s) for integrations.
  name: Knak Integrations API
  slug: knak-integrations-api
- description: The MarketingPlatformSyncs API from Knak — 1 operation(s) for marketingplatformsyncs.
  name: Knak MarketingPlatformSyncs API
  slug: knak-marketingplatformsyncs-api
- description: The MergeTags API from Knak — 2 operation(s) for mergetags.
  name: Knak MergeTags API
  slug: knak-mergetags-api
- description: The Modules API from Knak — 3 operation(s) for modules.
  name: Knak Modules API
  slug: knak-modules-api
- description: Endpoints that need to be implemented to support OAuth2
  name: Knak OAuth2 API
  slug: knak-oauth2-api
- description: The Project Management API from Knak — 1 operation(s) for project management.
  name: Knak Project Management API
  slug: knak-project-management-api
- description: The Status API from Knak — 1 operation(s) for status.
  name: Knak Status API
  slug: knak-status-api
- description: Endpoints to retrieve Sync Location
  name: Knak Sync Location API
  slug: knak-sync-location-api
- description: The SyncStatuses API from Knak — 1 operation(s) for syncstatuses.
  name: Knak SyncStatuses API
  slug: knak-syncstatuses-api
- description: The Themes API from Knak — 2 operation(s) for themes.
  name: Knak Themes API
  slug: knak-themes-api
- description: The TranslationRequests API from Knak — 5 operation(s) for translationrequests.
  name: Knak TranslationRequests API
  slug: knak-translationrequests-api
- description: The Users API from Knak — 4 operation(s) for users.
  name: Knak Users API
  slug: knak-users-api
- description: The Validation API from Knak — 1 operation(s) for validation.
  name: Knak Validation API
  slug: knak-validation-api
artifact_total: 28
asyncapis:
- description: ''
  name: Knak Enterprise Webhooks
  slug: knak-enterprise-webhooks
common:
- group: auth
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
  title: ''
  type: VulnerabilityDisclosure
  url: security/knak-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/knak-dam-openapi-original.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/knak-custom-validator-openapi-original.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/knak-custom-sync-location-openapi-original.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/knak-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/knak-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/knak-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/knak-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/knak-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/knak-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/knak-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/knak-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/knak-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/knak-enterprise-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/knak-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knak-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/knak-enterprise-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knak-send-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knak-scim-overlay.yaml
created: '2026-07-17'
description: Knak is a no-code email and landing page creation platform built for enterprise marketing teams. Marketers design on-brand, responsive emails and landing pages in a drag-and-drop builder, then sync the finished HTML directly into their marketing automation platform (Marketo, Eloqua, Salesforce Marketing Cloud, Braze, HubSpot and others) without writing code or waiting on developers. For technical teams Knak publishes a documented developer surface -- the Knak Enterprise REST API for automating users, assets, themes, modules, brands, folders, merge tags and translation requests; the Knak Send Contacts API; a SCIM 2.0 API for identity-provider driven user provisioning; signed webhooks for asset and translation lifecycle events; a set of customer-implemented integration contracts (Custom DAM, Custom Validator, Custom Sync Location); and a hosted, OAuth 2.1 protected MCP server that lets AI clients generate and browse Knak assets.
image: https://s3.amazonaws.com/assets.knak.io/img/Knak-Logo-Medium.png
layout: provider
mcp_servers:
- description: ''
  name: knak-mcp.yml
  slug: knak-mcpyml
modified: '2026-07-19'
name: Knak
nav: Providers
network: true
overview: 'Knak publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Asset Custom Fieldsets API, AssetFolders API, Assets API, and 18 more. Tagged areas include Company, Email Marketing, Marketing Automation, Landing Pages, and Content Creation.


  The Knak catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Knak''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 73
scopes:
- name: Knak Scopes
  scope_count: 1
  slug: knak-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 55.6
  delta: -0.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 63.5
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 34.2
  previous_composite: 56.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knak/refs/heads/main/screenshots/knak-2026-07-25T223953.png
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
- Webhooks
website: https://knak.com/
---
