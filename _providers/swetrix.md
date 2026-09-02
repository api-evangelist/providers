---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Swetrix Agentic Access
  operation_count: 49
  slug: swetrix-agentic-access
  summary_line: 49 operations · 25 acting
api_count: 2
apis:
- description: The Swetrix Events API provides endpoints for recording pageview events, custom events, heartbeat events, error events, and revenue transactions. Used for sending analytics data from client or server-
  name: Swetrix Events API
  slug: swetrix-events-api
- description: Manage chart annotations
  name: Swetrix Annotations API
  slug: swetrix-annotations-api
- description: Custom event analytics
  name: Swetrix Custom Events API
  slug: swetrix-custom-events-api
- description: Record JavaScript error events
  name: Swetrix Errors API
  slug: swetrix-errors-api
- description: Feature flag evaluation statistics
  name: Swetrix Feature Flags API
  slug: swetrix-feature-flags-api
- description: Manage conversion funnels
  name: Swetrix Funnels API
  slug: swetrix-funnels-api
- description: Manage organisations and member access
  name: Swetrix Organisations API
  slug: swetrix-organisations-api
- description: Frontend and backend performance metrics
  name: Swetrix Performance API
  slug: swetrix-performance-api
- description: Manage analytics projects
  name: Swetrix Projects API
  slug: swetrix-projects-api
- description: Record revenue transactions (server-side only, requires API key)
  name: Swetrix Revenue API
  slug: swetrix-revenue-api
- description: Individual visitor session data
  name: Swetrix Sessions API
  slug: swetrix-sessions-api
- description: Aggregated traffic and pageview analytics
  name: Swetrix Traffic API
  slug: swetrix-traffic-api
- description: Manage saved dashboard views (segments)
  name: Swetrix Views API
  slug: swetrix-views-api
artifact_total: 58
asyncapis:
- description: ''
  name: Swetrix Alerts Webhooks
  slug: swetrix-alerts-webhooks
collections:
- collection_type: postman
  name: Swetrix Admin Annotations API
  slug: postman-swetrix-annotations-api
- collection_type: postman
  name: Swetrix Admin Annotations Custom Events API
  slug: postman-swetrix-custom-events-api
- collection_type: postman
  name: Swetrix Admin Annotations Errors API
  slug: postman-swetrix-errors-api
- collection_type: postman
  name: Swetrix Admin Annotations Feature Flags API
  slug: postman-swetrix-feature-flags-api
- collection_type: postman
  name: Swetrix Admin Annotations Funnels API
  slug: postman-swetrix-funnels-api
- collection_type: postman
  name: Swetrix Admin Annotations Organisations API
  slug: postman-swetrix-organisations-api
- collection_type: postman
  name: Swetrix Admin Annotations Performance API
  slug: postman-swetrix-performance-api
- collection_type: postman
  name: Swetrix Admin Annotations Projects API
  slug: postman-swetrix-projects-api
- collection_type: postman
  name: Swetrix Admin Annotations Revenue API
  slug: postman-swetrix-revenue-api
- collection_type: postman
  name: Swetrix Admin Annotations Sessions API
  slug: postman-swetrix-sessions-api
- collection_type: postman
  name: Swetrix Admin Annotations Traffic API
  slug: postman-swetrix-traffic-api
- collection_type: postman
  name: Swetrix Admin Annotations Views API
  slug: postman-swetrix-views-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Swetrix Admin API
  slug: open-swetrix-admin-api
- collection_type: open
  name: Swetrix Admin Annotations API
  slug: open-swetrix-annotations-api
- collection_type: open
  name: Swetrix Admin Annotations Custom Events API
  slug: open-swetrix-custom-events-api
- collection_type: open
  name: Swetrix Admin Annotations Errors API
  slug: open-swetrix-errors-api
- collection_type: open
  name: Swetrix Admin Annotations Events API
  slug: open-swetrix-events-api
- collection_type: open
  name: Swetrix Admin Annotations Feature Flags API
  slug: open-swetrix-feature-flags-api
- collection_type: open
  name: Swetrix Admin Annotations Funnels API
  slug: open-swetrix-funnels-api
- collection_type: open
  name: Swetrix Admin Annotations Organisations API
  slug: open-swetrix-organisations-api
- collection_type: open
  name: Swetrix Admin Annotations Performance API
  slug: open-swetrix-performance-api
- collection_type: open
  name: Swetrix Admin Annotations Projects API
  slug: open-swetrix-projects-api
- collection_type: open
  name: Swetrix Admin Annotations Revenue API
  slug: open-swetrix-revenue-api
- collection_type: open
  name: Swetrix Admin Annotations Sessions API
  slug: open-swetrix-sessions-api
- collection_type: open
  name: Swetrix Statistics API
  slug: open-swetrix-statistics-api
- collection_type: open
  name: Swetrix Admin Annotations Traffic API
  slug: open-swetrix-traffic-api
- collection_type: open
  name: Swetrix Admin Annotations Views API
  slug: open-swetrix-views-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/swetrix/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swetrix-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/swetrix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swetrix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swetrix-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swetrix
- group: company
  title: ''
  type: Website
  url: https://swetrix.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.swetrix.com
- group: company
  title: ''
  type: Blog
  url: https://swetrix.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://swetrix.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Swetrix/swetrix
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Swetrix
- group: start
  title: ''
  type: Login
  url: https://swetrix.com/login
- group: start
  title: ''
  type: Signup
  url: https://swetrix.com/signup
- group: operate
  title: ''
  type: Support
  url: https://swetrix.com/contact
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/Swetrix/swetrix-api
- group: build
  title: ''
  type: JavaScript SDK
  url: https://www.npmjs.com/package/swetrix
- group: build
  title: ''
  type: Node.js SDK
  url: https://www.npmjs.com/package/@swetrix/node
- group: operate
  title: ''
  type: StatusPage
  url: https://status.swetrix.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://swetrix.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://swetrix.com/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://swetrix.com/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/swetrix-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/swetrix-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swetrix-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/swetrix-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/swetrix-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/swetrix-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/swetrix-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/swetrix-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Swetrix/swetrix/releases
- group: design
  title: ''
  type: Conformance
  url: conformance/swetrix-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://swetrix.com/dpa
- group: auth
  title: ''
  type: Security
  url: https://swetrix.com/security
- group: start
  title: ''
  type: Sandbox
  url: sandbox/swetrix-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/swetrix-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/swetrix-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/swetrix-alerts-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swetrix-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/swetrix-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/swetrix-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/swetrix-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/swetrix-rules.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/swetrix-jsonschema-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/swetrix-project-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/swetrix-session-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/swetrix-project-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/swetrix-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/swetrix-create-project-example.json
- group: build
  title: ''
  type: Examples
  url: examples/swetrix-record-pageview-example.json
- group: build
  title: ''
  type: Examples
  url: examples/swetrix-get-traffic-log-example.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://swetrix.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://swetrix.com/docs/statistics-api
- group: start
  title: ''
  type: GettingStarted
  url: https://swetrix.com/docs/install-script
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/Swetrix/swetrix/issues
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/ZVK8Tw2E8j
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/swetrix
- group: other
  title: ''
  type: DataPolicy
  url: https://swetrix.com/data-policy
created: '2026-03-26'
description: Swetrix is an open source, privacy-focused web analytics platform that provides cookieless tracking, real-time dashboards, and GDPR-compliant analytics without collecting personal data. It offers a fully-featured REST API for tracking events, querying statistics, managing projects, and integrating analytics into custom applications.
examples:
- key_count: 4
  name: Swetrix Create Project Example
  slug: swetrix-create-project-example
- key_count: 4
  name: Swetrix Get Traffic Log Example
  slug: swetrix-get-traffic-log-example
- key_count: 4
  name: Swetrix Record Pageview Example
  slug: swetrix-record-pageview-example
finops:
- name: Swetrix Finops
  service_category: Web Analytics
  slug: swetrix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swetrix.png
json_schemas:
- name: Swetrix Project
  property_count: 12
  slug: swetrix-project
- name: Swetrix Session
  property_count: 16
  slug: swetrix-session
json_structures:
- name: Swetrix Project Structure
  property_count: 0
  slug: swetrix-project-structure
jsonld:
- class_count: 30
  name: Swetrix Context
  property_count: 6
  slug: swetrix-context
layout: provider
modified: '2026-08-13'
name: Swetrix
nav: Providers
network: true
overview: 'Swetrix publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Events API, Annotations API, Custom Events API, and 10 more. Tagged areas include Analytics, Cookieless Tracking, GDPR Compliant, Open-Source, and Privacy.


  The Swetrix catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Swetrix''s developer surface includes authentication, documentation, engineering blog, pricing, GitHub presence, signup flow, support, and 52 more developer resources.'
plans:
- name: Swetrix Plans Pricing
  plan_count: 3
  slug: swetrix-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Swetrix Rate Limits
  slug: swetrix-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Swetrix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: swetrix-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Swetrix API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 6
  slug: swetrix-rules
score:
  band: exemplar
  composite: 76.3
  coverage:
    artifact_dirs: 32
    catalog_gap: 33.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 47.0
    contract_quality: 75.6
    developer_ergonomics: 87.5
    discoverability: 75.9
    governance: 47.0
    operational_transparency: 73.7
  previous_composite: 76.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swetrix/refs/heads/main/screenshots/swetrix-2026-06-20T194812.png
security:
- kind: authentication
  name: Swetrix Authentication
  slug: swetrix-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Swetrix Domain Security
  slug: swetrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Swetrix Vulnerability Disclosure
  slug: swetrix-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: swetrix
tags:
- Analytics
- Cookieless Tracking
- GDPR Compliant
- Open-Source
- Privacy
- Real-Time Analytics
- Web Analytics
website: https://swetrix.com
---
