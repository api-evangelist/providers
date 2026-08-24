---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 165
  human_in_the_loop: 1
  name: Mediavalet Agentic Access
  operation_count: 312
  slug: mediavalet-agentic-access
  summary_line: 312 operations · 165 acting · 1 human-in-the-loop
api_count: 29
apis:
- description: Core digital asset objects, their media files, renditions, versions, comments, history, faces and video clips. The centre of the MediaValet data model. 54 operations.
  name: MediaValet Assets API
  slug: mediavalet-assets-api
- description: Branded Portals — externally shareable, branded, permissioned views onto a subset of the asset library, with their own sections and theming. 46 operations.
  name: MediaValet BrandedPortals API
  slug: mediavalet-branded-portals-api
- description: Hierarchical categories (folders) that organize assets and carry the permission sets granted to user groups. 18 operations.
  name: MediaValet Categories API
  slug: mediavalet-categories-api
- description: Users, their profiles, permissions, entitlements and public self-registration. 18 operations.
  name: MediaValet Users API
  slug: mediavalet-users-api
- description: Lightboxes — user-curated collections of assets that can be shared by share code. 15 operations.
  name: MediaValet Lightbox API
  slug: mediavalet-lightbox-api
- description: Organizational units (libraries) — the MediaValet tenancy root that every asset, category and event is scoped to. 15 operations.
  name: MediaValet OrgUnit API
  slug: mediavalet-org-unit-api
- description: Durable CDN direct links to assets and renditions, for distributing assets outside the DAM without expiring SAS URLs. 12 operations.
  name: MediaValet DirectLinks API
  slug: mediavalet-direct-links-api
- description: Third-party integration registration — apps, allowed origins for iframe embedding, subscriptions, users and entitlements. 12 operations.
  name: MediaValet Integrations API
  slug: mediavalet-integrations-api
- description: Chunked ingest of new files and new asset versions into a library, via MediaValet-issued Azure blob upload URLs. 11 operations.
  name: MediaValet Uploads API
  slug: mediavalet-uploads-api
- description: Custom metadata attribute definitions, their data types (including the Status type added in API version 1.1) and embedded-data mappings. 10 operations.
  name: MediaValet Attributes API
  slug: mediavalet-attributes-api
- description: Usage and activity reporting across the library. 10 operations.
  name: MediaValet Reports API
  slug: mediavalet-reports-api
- description: Asset download requests, packaged downloads and download presets. 9 operations.
  name: MediaValet Downloads API
  slug: mediavalet-downloads-api
- description: In-product notifications and notification preferences. 9 operations.
  name: MediaValet Notification API
  slug: mediavalet-notification-api
- description: Sharing of assets and lightboxes with external recipients by share code. 9 operations.
  name: MediaValet Sharing API
  slug: mediavalet-sharing-api
- description: Server-side cropping of image assets, including reusable crop templates. 8 operations.
  name: MediaValet Crop API
  slug: mediavalet-crop-api
- description: Person and face recognition records used to tag the people appearing in assets. 8 operations.
  name: MediaValet Persons API
  slug: mediavalet-persons-api
- description: Saved search definitions and their re-execution. 8 operations.
  name: MediaValet SavedSearches API
  slug: mediavalet-saved-searches-api
- description: User groups and group membership — the unit that category permissions are granted to. 7 operations.
  name: MediaValet UserGroups API
  slug: mediavalet-user-groups-api
- description: Groupings of custom metadata attributes. Gated by a per-library feature flag. 6 operations.
  name: MediaValet AttributeGroups API
  slug: mediavalet-attribute-groups-api
- description: Hierarchical groupings of controlled-vocabulary keywords. 5 operations.
  name: MediaValet KeywordGroups API
  slug: mediavalet-keyword-groups-api
- description: SkyHOOK webhook and Azure Event Grid subscription management for MediaValet events. 5 operations.
  name: MediaValet Webhooks API
  slug: mediavalet-webhooks-api
- description: Authorization and permission checks for the calling user. 3 operations.
  name: MediaValet Authorization API
  slug: mediavalet-authorization-api
- description: The controlled keyword vocabulary and per-asset tagging, with keyword approval workflow. 3 operations.
  name: MediaValet Keywords API
  slug: mediavalet-keywords-api
- description: Search across the library, including the filter and facet grammar. 3 operations.
  name: MediaValet Searches API
  slug: mediavalet-searches-api
- description: Library and account configuration. 2 operations.
  name: MediaValet Config API
  slug: mediavalet-config-api
- description: The hypermedia entry point and the bulk batching endpoint. 2 operations.
  name: MediaValet Home API
  slug: mediavalet-home-api
- description: Version 2 of the MediaValet usage and activity reporting surface. 2 operations.
  name: MediaValet ReportsV2 API
  slug: mediavalet-reports-v2-api
- description: Introductory and help resources served by the API. 1 operation.
  name: MediaValet IntroductionAndHelp API
  slug: mediavalet-introduction-and-help-api
- description: Terms and conditions acceptance. 1 operation.
  name: MediaValet TermsAndConditions API
  slug: mediavalet-terms-and-conditions-api
artifact_total: 69
asyncapis:
- description: SkyHOOK is MediaValet's event subscription service. It delivers MediaValet asset, category, keyword and attribute events either directly to a subscriber-owned HTTPS endpoint (webhook) or into a privat
  name: MediaValet SkyHOOK Events
  slug: mediavalet-skyhook-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MediaValet Assets API
  slug: open-mediavalet-assets-api
- collection_type: open
  name: MediaValet AttributeGroups API
  slug: open-mediavalet-attribute-groups-api
- collection_type: open
  name: MediaValet Attributes API
  slug: open-mediavalet-attributes-api
- collection_type: open
  name: MediaValet Authorization API
  slug: open-mediavalet-authorization-api
- collection_type: open
  name: MediaValet BrandedPortals API
  slug: open-mediavalet-branded-portals-api
- collection_type: open
  name: MediaValet Categories API
  slug: open-mediavalet-categories-api
- collection_type: open
  name: MediaValet Config API
  slug: open-mediavalet-config-api
- collection_type: open
  name: MediaValet Crop API
  slug: open-mediavalet-crop-api
- collection_type: open
  name: MediaValet DirectLinks API
  slug: open-mediavalet-direct-links-api
- collection_type: open
  name: MediaValet Downloads API
  slug: open-mediavalet-downloads-api
- collection_type: open
  name: MediaValet Home API
  slug: open-mediavalet-home-api
- collection_type: open
  name: MediaValet Integrations API
  slug: open-mediavalet-integrations-api
- collection_type: open
  name: MediaValet IntroductionAndHelp API
  slug: open-mediavalet-introduction-and-help-api
- collection_type: open
  name: MediaValet KeywordGroups API
  slug: open-mediavalet-keyword-groups-api
- collection_type: open
  name: MediaValet Keywords API
  slug: open-mediavalet-keywords-api
- collection_type: open
  name: MediaValet Lightbox API
  slug: open-mediavalet-lightbox-api
- collection_type: open
  name: MediaValet Notification API
  slug: open-mediavalet-notification-api
- collection_type: open
  name: MediaValet OrgUnit API
  slug: open-mediavalet-org-unit-api
- collection_type: open
  name: MediaValet Persons API
  slug: open-mediavalet-persons-api
- collection_type: open
  name: MediaValet Reports API
  slug: open-mediavalet-reports-api
- collection_type: open
  name: MediaValet ReportsV2 API
  slug: open-mediavalet-reports-v2-api
- collection_type: open
  name: MediaValet SavedSearches API
  slug: open-mediavalet-saved-searches-api
- collection_type: open
  name: MediaValet Searches API
  slug: open-mediavalet-searches-api
- collection_type: open
  name: MediaValet Sharing API
  slug: open-mediavalet-sharing-api
- collection_type: open
  name: MediaValet TermsAndConditions API
  slug: open-mediavalet-terms-and-conditions-api
- collection_type: open
  name: MediaValet Uploads API
  slug: open-mediavalet-uploads-api
- collection_type: open
  name: MediaValet UserGroups API
  slug: open-mediavalet-user-groups-api
- collection_type: open
  name: MediaValet Users API
  slug: open-mediavalet-users-api
- collection_type: open
  name: MediaValet Webhooks API
  slug: open-mediavalet-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mediavalet-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mediavalet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mediavalet-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mediavalet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mediavalet-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mediavalet-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/mediavalet-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mediavalet-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mediavalet-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mediavalet-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/mediavalet-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mediavalet-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/mediavalet-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/mediavalet-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mediavalet-mcp.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/mediavalet-skyhook-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mediavalet-skyhook-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mediavalet-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mediavalet-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mediavalet-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/mediavalet-openid-configuration.json
- group: build
  title: ''
  type: Postman
  url: collections/mediavalet-api.postman_collection.json
- group: build
  title: ''
  type: PostmanCollection
  url: collections/mediavalet-api.postman_collection.json
- group: auth
  title: ''
  type: TrustCenter
  url: security/mediavalet-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mediavalet-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mediavalet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mediavalet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mediavalet-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.mediavalet.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mediavalet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mediavalet.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mediavalet.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mediavalet.com/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://developer.mediavalet.com/signup
- group: start
  title: ''
  type: Login
  url: https://developer.mediavalet.com/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mediavalet.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.mediavalet.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mediavalet.com/terms-and-condition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mediavalet.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MediaValet
- group: company
  title: ''
  type: Blog
  url: https://www.mediavalet.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mediavalet
created: '2026-07-05'
description: MediaValet is a cloud-native, Microsoft Azure-based digital asset management (DAM) platform for storing, organizing, governing, sharing and distributing an organization's images, videos, documents and other brand, campaign and product assets. Its Open API is a RESTful, JSON, hypermedia-driven service at https://api.mediavalet.com, fronted by Azure API Management and secured with BOTH an OAuth 2.0 / OpenID Connect bearer token (issuer https://iam.mediavalet.com) and a per-account Ocp-Apim-Subscription-Key. The published surface runs to 312 operations across 29 resources - assets, categories, attributes, keywords, uploads, users, user groups, branded portals, lightboxes, direct/CDN links, downloads, sharing, crops, persons, saved searches, reports, notifications, organizational units and third-party integrations - plus SkyHOOK, an event service that delivers CloudEvents 1.0 messages to a webhook or a private Azure Event Grid instance. API versions are selected per request with
  the x-mv-api-version header (1.0 default, 1.1, 1.2). MediaValet publishes no OpenAPI; its machine-readable contract is a Postman Collection v2.1.0 at docs.mediavalet.com, from which the definitions in this repo are derived. Access requires an existing MediaValet subscription and an approved Developer Portal account.
finops:
- name: Mediavalet Finops
  service_category: Digital Asset Management
  slug: mediavalet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mediavalet.png
layout: provider
mcp_servers:
- description: MediaValet does not publish a Model Context Protocol server. This is a CANDIDATE tool surface derived from MediaValet's real REST operations, offered as a design starting point — nothing here is calla
  name: MediaValet DAM (candidate MCP server)
  slug: mediavalet-dam-candidate-mcp-server
modified: '2026-08-13'
name: MediaValet
nav: Providers
network: true
overview: 'MediaValet publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Assets API, BrandedPortals API, Categories API, and 26 more. Tagged areas include Digital Asset Management, DAM, Media, Assets, and Content.


  The MediaValet catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MediaValet''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, signup flow, and 36 more developer resources.'
plans:
- name: Mediavalet Plans Pricing
  plan_count: 2
  slug: mediavalet-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Mediavalet Rate Limits
  slug: mediavalet-rate-limits
scopes:
- name: Mediavalet Scopes
  scope_count: 7
  slug: mediavalet-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials/password
score:
  band: strong
  composite: 63.4
  delta: 0.0
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 30.3
    contract_quality: 67.0
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 34.2
  previous_composite: 63.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mediavalet/refs/heads/main/screenshots/mediavalet-2026-08-07T172338.png
security:
- kind: authentication
  name: Mediavalet Authentication
  slug: mediavalet-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Mediavalet Domain Security
  slug: mediavalet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mediavalet Trust Center
  slug: mediavalet-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: mediavalet
tags:
- Digital Asset Management
- DAM
- Media
- Assets
- Content
- Marketing
- Brand Management
- Cloud Storage
- Metadata
- Video
- Image
- Webhook
- Azure
website: https://www.mediavalet.com
---
