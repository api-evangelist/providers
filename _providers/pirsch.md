---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 54
  human_in_the_loop: 0
  name: Pirsch Agentic Access
  operation_count: 97
  slug: pirsch-agentic-access
  summary_line: 97 operations · 54 acting
api_count: 1
apis:
- description: Manage shareable access links for dashboard visibility
  name: Pirsch Access Links API
  slug: pirsch-access-links-api
- description: Obtain access tokens using OAuth2 client credentials
  name: Pirsch Authentication API
  slug: pirsch-authentication-api
- description: Manage OAuth2 and access-key API clients
  name: Pirsch Clients API
  slug: pirsch-clients-api
- description: Define and manage conversion goals with path patterns or events
  name: Pirsch Conversion Goals API
  slug: pirsch-conversion-goals-api
- description: Manage tracked domains and their configuration
  name: Pirsch Domains API
  slug: pirsch-domains-api
- description: Schedule and manage recurring email analytics reports
  name: Pirsch Email Reports API
  slug: pirsch-email-reports-api
- description: Define and manage multi-step conversion funnels
  name: Pirsch Funnels API
  slug: pirsch-funnels-api
- description: Manage domain members, roles, and invitations
  name: Pirsch Members API
  slug: pirsch-members-api
- description: Create and manage UTM-enriched short links
  name: Pirsch Short Links API
  slug: pirsch-short-links-api
- description: Query analytics statistics by date range and filter criteria
  name: Pirsch Statistics API
  slug: pirsch-statistics-api
- description: Send page views, events, and session keep-alive signals
  name: Pirsch Tracking API
  slug: pirsch-tracking-api
- description: Filter traffic and configure spike/warning notifications
  name: Pirsch Traffic Management API
  slug: pirsch-traffic-management-api
- description: Manage the authenticated user account
  name: Pirsch User API
  slug: pirsch-user-api
- description: Save and manage custom analytics views
  name: Pirsch Views API
  slug: pirsch-views-api
- description: Configure webhooks for event-driven integrations
  name: Pirsch Webhooks API
  slug: pirsch-webhooks-api
artifact_total: 49
asyncapis:
- description: ''
  name: Pirsch Webhooks
  slug: pirsch-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pirsch Access Links API
  slug: open-pirsch-access-links-api
- collection_type: open
  name: Pirsch Access Links Authentication API
  slug: open-pirsch-authentication-api
- collection_type: open
  name: Pirsch Access Links Clients API
  slug: open-pirsch-clients-api
- collection_type: open
  name: Pirsch Access Links Conversion Goals API
  slug: open-pirsch-conversion-goals-api
- collection_type: open
  name: Pirsch Access Links Domains API
  slug: open-pirsch-domains-api
- collection_type: open
  name: Pirsch Access Links Email Reports API
  slug: open-pirsch-email-reports-api
- collection_type: open
  name: Pirsch Access Links Funnels API
  slug: open-pirsch-funnels-api
- collection_type: open
  name: Pirsch Access Links Members API
  slug: open-pirsch-members-api
- collection_type: open
  name: Pirsch Access Links Short Links API
  slug: open-pirsch-short-links-api
- collection_type: open
  name: Pirsch Access Links Statistics API
  slug: open-pirsch-statistics-api
- collection_type: open
  name: Pirsch Access Links Tracking API
  slug: open-pirsch-tracking-api
- collection_type: open
  name: Pirsch Access Links Traffic Management API
  slug: open-pirsch-traffic-management-api
- collection_type: open
  name: Pirsch Access Links User API
  slug: open-pirsch-user-api
- collection_type: open
  name: Pirsch Access Links Views API
  slug: open-pirsch-views-api
- collection_type: open
  name: Pirsch Access Links Webhooks API
  slug: open-pirsch-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pirsch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pirsch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pirsch-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://pirsch.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pirsch.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/pirsch-analytics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/products/emvi-software-gmbh-pirsch-analytics/
- group: company
  title: ''
  type: Blog
  url: https://pirsch.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pirsch.io/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/PirschAnalytics
- group: commercial
  title: ''
  type: Plans
  url: plans/pirsch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pirsch-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pirsch-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pirsch.io/api-sdks/api-v1
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pirsch.io/api-sdks/api-v1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pirsch.io/get-started/frontend-integration
- group: operate
  title: ''
  type: Support
  url: https://forum.pirsch.io
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.pirsch.io/faq
- group: start
  title: ''
  type: Console
  url: https://pirsch.pirsch.io
- group: company
  title: ''
  type: About
  url: https://pirsch.io/about-us
- group: company
  title: ''
  type: News
  url: https://pirsch.io/news
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://pirsch.io/static/files/Data%20Processing%20Agreement%20-%20Pirsch%20Analytics.pdf
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/pirsch.bsky.social
- group: company
  title: ''
  type: Mastodon
  url: https://social.anoxinon.de/@pirsch
- group: other
  title: ''
  type: ProductHunt
  url: https://www.producthunt.com/products/pirsch-analytics
- group: start
  title: ''
  type: SignUp
  url: https://pirsch.io/signup
- group: start
  title: ''
  type: Login
  url: https://pirsch.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pirsch.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pirsch.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pirsch-analytics
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.pirsch.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pirsch-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/pirsch-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pirsch-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pirsch-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/pirsch-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pirsch-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pirsch-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pirsch-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.pirsch.io/privacy
- group: design
  title: ''
  type: DataModel
  url: data-model/pirsch-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/pirsch-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pirsch-webhooks.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/pirsch-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/pirsch-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/pirsch-context.jsonld
- group: design
  title: ''
  type: Rules
  url: rules/pirsch-jsonschema-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/pirsch-hit-request.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/pirsch-event-request.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/pirsch-visitor-stats.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/pirsch-domain.json
- group: build
  title: ''
  type: Examples
  url: examples/pirsch-hit-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/pirsch-event-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/pirsch-token-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/pirsch-token-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/pirsch-visitor-stats-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/pirsch-domain-example.json
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-access-links-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-authentication-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-clients-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-conversion-goals-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-domains-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-email-reports-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-funnels-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-members-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-short-links-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-statistics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-tracking-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-traffic-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-user-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-views-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/pirsch-webhooks-overlay.yaml
created: '2026-06-13'
description: Pirsch is a privacy-first website analytics platform built and hosted in Germany. GDPR, CCPA, PECR, and Schrems II compliant, it tracks page views, sessions, custom events, conversion goals, funnels, and traffic sources without cookies or personal data storage. Developers access all data via a RESTful API with OAuth and access-key authentication, supported by official Go, JavaScript, and PHP SDKs.
examples:
- key_count: 16
  name: Pirsch Domain Example
  slug: pirsch-domain-example
- key_count: 8
  name: Pirsch Event Request Example
  slug: pirsch-event-request-example
- key_count: 10
  name: Pirsch Hit Request Example
  slug: pirsch-hit-request-example
- key_count: 2
  name: Pirsch Token Request Example
  slug: pirsch-token-request-example
- key_count: 2
  name: Pirsch Token Response Example
  slug: pirsch-token-response-example
finops:
- name: Pirsch Finops
  service_category: ''
  slug: pirsch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pirsch.png
json_schemas:
- name: Domain
  property_count: 16
  slug: pirsch-domain
- name: EventRequest
  property_count: 14
  slug: pirsch-event-request
- name: HitRequest
  property_count: 13
  slug: pirsch-hit-request
- name: VisitorStats
  property_count: 12
  slug: pirsch-visitor-stats
jsonld:
- class_count: 7
  name: Pirsch Context
  property_count: 63
  slug: pirsch-context
layout: provider
modified: '2026-08-13'
name: Pirsch
nav: Providers
network: true
overview: 'Pirsch publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Access Links API, Authentication API, Clients API, and 12 more. Tagged areas include Analytics, Web Analytics, Privacy, GDPR, and Cookie-Free.


  The Pirsch catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Pirsch''s developer surface includes authentication, documentation, engineering blog, pricing, API reference, getting-started guide, support, and 66 more developer resources.'
plans:
- name: Pirsch Plans Pricing
  plan_count: 3
  slug: pirsch-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Pirsch Rate Limits
  slug: pirsch-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Pirsch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pirsch-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 66.5
  coverage:
    artifact_dirs: 29
    catalog_gap: 31.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 25.0
    contract_quality: 69.8
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 57.9
  previous_composite: 66.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/screenshots/pirsch-2026-06-20T191730.png
security:
- kind: authentication
  name: Pirsch Authentication
  slug: pirsch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pirsch Domain Security
  slug: pirsch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pirsch
tags:
- Analytics
- Web Analytics
- Privacy
- GDPR
- Cookie-Free
- Page Views
- Sessions
- Event
- Conversion Goals
- Funnels
- Traffic Sources
website: https://pirsch.io
---
