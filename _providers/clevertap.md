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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Clevertap Agentic Access
  operation_count: 10
  slug: clevertap-agentic-access
  summary_line: 10 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Upload, retrieve, update, and delete user profiles in CleverTap with identity, demographic, and custom property data.
  name: CleverTap Profile API
  slug: profile-api
- description: Record user events with arbitrary properties for behavioral segmentation, funnels, and triggered messaging.
  name: CleverTap Event API
  slug: event-api
- description: Programmatically create and manage push, email, SMS, web, and in-app campaigns and retrieve message status reports.
  name: CleverTap Campaign API
  slug: campaign-api
- description: Raise a Bulletin in CleverTap when a business event is triggered, used to drive real-time campaign delivery from external systems.
  name: CleverTap Bulletins API
  slug: bulletins-api
- description: Manage product catalog data feeding personalization, recommendations, and product-aware messaging.
  name: CleverTap Catalog API
  slug: catalog-api
- description: Create and update custom lists used as audience segments in campaigns and journeys.
  name: CleverTap Custom List API
  slug: custom-list-api
- description: Manage feature flags and remote configuration variables delivered to mobile apps and websites.
  name: CleverTap Remote Config API
  slug: remote-config-api
- description: Query real-time counts and trends of events, profiles, and segments.
  name: CleverTap Real-Time Counts API
  slug: counts-api
- description: The Campaigns API from CleverTap — 3 operation(s) for campaigns.
  name: CleverTap Campaigns API
  slug: clevertap-campaigns-api
- description: The Events API from CleverTap — 2 operation(s) for events.
  name: CleverTap Events API
  slug: clevertap-events-api
- description: The Profiles API from CleverTap — 4 operation(s) for profiles.
  name: CleverTap Profiles API
  slug: clevertap-profiles-api
- description: The Reports API from CleverTap — 2 operation(s) for reports.
  name: CleverTap Reports API
  slug: clevertap-reports-api
artifact_total: 30
asyncapis:
- description: ''
  name: Clevertap Webhooks
  slug: clevertap-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CleverTap REST Campaigns API
  slug: open-clevertap-campaigns-api
- collection_type: open
  name: CleverTap REST Campaigns Events API
  slug: open-clevertap-events-api
- collection_type: open
  name: CleverTap REST Campaigns Profiles API
  slug: open-clevertap-profiles-api
- collection_type: open
  name: CleverTap REST Campaigns Reports API
  slug: open-clevertap-reports-api
- collection_type: open
  name: CleverTap REST API
  slug: open-clevertap
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clevertap-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clevertap-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clevertap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clevertap-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CleverTap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clevertap
- group: company
  title: ''
  type: Website
  url: https://clevertap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clevertap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clevertap.com/docs
- group: auth
  title: ''
  type: Authentication
  url: https://developer.clevertap.com/docs/api-authentication
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clevertap.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://clevertap.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clevertap.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clevertap.com/terms-of-service/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clevertap-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clevertap-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.clevertap.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://clevertap.com/blog
- group: build
  title: ''
  type: Packages
  url: packages/clevertap-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/clevertap-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clevertap-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clevertap-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/clevertap-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clevertap-llms.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clevertap-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clevertap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clevertap-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clevertap-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clevertap-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.clevertap.com/docs/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/clevertap-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://clevertap.com/security/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/clevertap-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clevertap-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/clevertap-profiles-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clevertap-events-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clevertap-campaigns-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/clevertap-reports-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/clevertap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clevertap-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clevertap-finops.yml
- group: build
  title: ''
  type: Postman
  url: https://developer.clevertap.com/docs/clevertap-postman-collection
- group: docs
  title: ''
  type: APIReference
  url: https://developer.clevertap.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.clevertap.com/docs/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://developer.clevertap.com/docs/api-quickstart-guide
- group: operate
  title: ''
  type: Support
  url: https://help.clevertap.com/
- group: start
  title: ''
  type: SignUp
  url: https://eu1.dashboard.clevertap.com/self-serve.html
- group: start
  title: ''
  type: Login
  url: https://eu1.dashboard.clevertap.com/
created: '2024-11-14'
description: CleverTap is a customer engagement and retention platform that helps businesses understand user behavior, segment audiences, and deliver personalized experiences across mobile push, email, SMS, in-app, web push, and WhatsApp channels. CleverTap exposes a comprehensive REST API surface covering profiles, events, campaigns, real-time analytics, catalogs, feature flags, and more, authenticated via account ID and passcode headers.
finops:
- name: Clevertap Finops
  service_category: API
  slug: clevertap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clevertap.png
jsonld:
- class_count: 0
  name: Clevertap Context
  property_count: 6
  slug: clevertap-context
layout: provider
mcp_servers:
- description: CleverTap operates a first-party remote MCP server at mcp.clevertap.com. The server is OAuth-protected end to end, so tools/list and initialize both return 401 anonymously and the live tool schemas ca
  name: CleverTap MCP Server
  slug: clevertap-mcp-server
modified: '2026-08-13'
name: CleverTap
nav: Providers
network: true
overview: 'CleverTap publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Events API, Profiles API, and 1 more. Tagged areas include Audiences, Customer Engagement, Customer Retention, Marketing Automation, and Mobile Engagement.


  The CleverTap catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  CleverTap''s developer surface includes authentication, documentation, pricing, engineering blog, changelog, API reference, getting-started guide, and 42 more developer resources.'
plans:
- name: Clevertap Plans Pricing
  plan_count: 3
  slug: clevertap-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 23
  name: Clevertap Rate Limits
  slug: clevertap-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: CleverTap API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: clevertap-rules
scopes:
- name: Clevertap Scopes
  scope_count: 4
  slug: clevertap-scopes
  summary_line: 4 scopes · authorizationCode/refreshToken
score:
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 26
    catalog_gap: 31.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 63.6
    contract_quality: 61.7
    developer_ergonomics: 38.7
    discoverability: 75.9
    governance: 63.6
    operational_transparency: 65.8
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clevertap/refs/heads/main/screenshots/clevertap-2026-06-20T174517.png
security:
- kind: authentication
  name: Clevertap Authentication
  slug: clevertap-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Clevertap Domain Security
  slug: clevertap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clevertap Trust Center
  slug: clevertap-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, HIPAA, GDPR, CSA STAR
slug: clevertap
tags:
- Audiences
- Customer Engagement
- Customer Retention
- Marketing Automation
- Mobile Engagement
- Push Notifications
- User Behavior
website: https://clevertap.com/
---
