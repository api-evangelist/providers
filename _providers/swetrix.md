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
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-10-31'
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
- baseURL: https://api.swetrix.com
  baseurl_source: declared
  description: Manage chart annotations
  name: Swetrix Annotations API
  phrasing_intents:
  - id: listAnnotations
    intent: List a project's chart annotations
    question: Which notes have been pinned to dates on my analytics charts?
  - id: createAnnotation
    intent: Add a note to a chart on a specific date
    question: How do I mark a release date on my traffic chart with a note?
  - id: updateAnnotation
    intent: Change an existing annotation's date or text
    question: Can I fix the wording of a chart annotation I already added?
  - id: deleteAnnotation
    intent: Remove an annotation from a project
    question: How do I get rid of a chart annotation I no longer need?
  phrasing_ops: 4
  slug: swetrix-annotations-api
- baseURL: https://api.swetrix.com
  baseurl_source: declared
  description: Custom event analytics
  name: Swetrix Custom Events API
  phrasing_intents:
  - id: getCustomEvents
    intent: Chart custom event counts over time
    question: How many times did my signup custom event fire each day this month?
  phrasing_ops: 1
  slug: swetrix-custom-events-api
- baseURL: https://api.swetrix.com
  baseurl_source: declared
  description: Record JavaScript error events
  name: Swetrix Errors API
  phrasing_intents:
  - id: listErrors
    intent: List grouped JavaScript errors for a project
    question: Which JavaScript errors are my visitors hitting most this week?
  - id: getError
    intent: View details of one error group
    question: What are the full details behind a specific error group?
  - id: getErrorOverview
    intent: Chart error counts over time
    question: Is my site's error rate going up or down over time?
  - id: recordError
    intent: Report a JavaScript error from a page
    question: How do I send a caught JavaScript exception to Swetrix?
  phrasing_ops: 4
  slug: swetrix-errors-api
- baseURL: https://api.swetrix.com
  baseurl_source: declared
  description: Feature flag evaluation statistics
  name: Swetrix Feature Flags API
  phrasing_intents:
  - id: getFeatureFlagStats
    intent: See how often a feature flag evaluated true or false
    question: How often is my feature flag coming back true versus false?
  phrasing_ops: 1
  slug: swetrix-feature-flags-api
- baseURL: https://api.swetrix.com
  baseurl_source: declared
  description: Manage conversion funnels
  name: Swetrix Funnels API
  phrasing_intents:
  - id: listFunnels
    intent: List a project's saved funnels
    question: Which conversion funnels have I already saved for this project?
  - id: createFunnel
    intent: Save a new conversion funnel
    question: How do I define a signup funnel as a sequence of pages?
  - id: updateFunnel
    intent: Rename a saved funnel or change its steps
    question: Can I add or reorder pages in a funnel I already saved?
  - id: deleteFunnel
    intent: Delete a saved funnel
    question: How do I remove a funnel I no longer use?
  - id: getFunnelAnalysis
    intent: Analyze conversion and drop-off through a funnel
    question: Where do visitors drop off between my homepage, signup and dashboard?
  phrasing_ops: 5
  slug: swetrix-funnels-api
- baseURL: https://api.swetrix.com
  baseurl_source: declared
  description: Manage organisations and member access
  name: Swetrix Organisations API
  phrasing_intents:
  - id: listOrganisations
    intent: List the organisations I belong to
    question: Which organisations am I a member of?
  - id: createOrganisation
    intent: Create a new organisation
    question: How do I set up a new organisation to share analytics projects with a team?
  - id: getOrganisation
    intent: View details of one organisation
    question: What are the details of a specific organisation I belong to?
  - id: updateOrganisation
    intent: Rename an organisation
    question: How do I rename an organisation?
  - id: deleteOrganisation
    intent: Permanently delete an organisation
    question: Who is allowed to permanently delete an organisation?
  - id: inviteOrganisationMember
    intent: Invite someone to an organisation with a role
    question: How do I invite a colleague by email to my organisation?
  - id: updateOrganisationMember
    intent: Change an organisation member's role
    question: Can I promote an existing organisation member to a different role?
  - id: removeOrganisationMember
    intent: Remove a member from an organisation
    question: What's the way to kick someone out of my organisation?
  phrasing_ops: 8
  slug: swetrix-organisations-api
- baseURL: https://api.swetrix.com
  baseurl_source: declared
  description: Frontend and backend performance metrics
  name: Swetrix Performance API
  phrasing_intents:
  - id: getPerformanceLog
    intent: Chart page load and timing metrics
    question: What's the p95 time to first byte on my site this month?
  - id: getPerformanceBirdseye
    intent: Compare performance against the previous period
    question: Did my sites get faster or slower compared with the previous period?
  phrasing_ops: 2
  slug: swetrix-performance-api
- baseURL: https://api.swetrix.com
  baseurl_source: declared
  description: Manage analytics projects
  name: Swetrix Projects API
  phrasing_intents:
  - id: listProjects
    intent: List my analytics projects
    question: Which analytics projects do I have?
  - id: createProject
    intent: Create a new analytics project
    question: How do I start tracking a new website as an analytics project?
  - id: getProject
    intent: View one analytics project's details
    question: What settings does a particular project currently have?
  - id: updateProject
    intent: Change a project's settings
    question: How do I restrict which origins can send data to my project?
  - id: deleteProject
    intent: Permanently delete a project and its data
    question: Does deleting a project also wipe all of its collected analytics data?
  - id: pinProject
    intent: Pin a project to the top of the dashboard
    question: How do I keep my most important project at the top of the dashboard?
  - id: unpinProject
    intent: Unpin a project from the dashboard
    question: Can I take a project out of the pinned section?
  phrasing_ops: 7
  slug: swetrix-projects-api
- baseURL: https://api.swetrix.com
  baseurl_source: declared
  description: Record revenue transactions (server-side only, requires API key)
  name: Swetrix Revenue API
  phrasing_intents:
  - id: recordRevenue
    intent: Record a sale, refund or subscription payment
    question: How do I send a completed sale from my server into Swetrix revenue analytics?
  phrasing_ops: 1
  slug: swetrix-revenue-api
- baseURL: https://api.swetrix.com
  baseurl_source: declared
  description: Individual visitor session data
  name: Swetrix Sessions API
  phrasing_intents:
  - id: listSessions
    intent: List individual visitor sessions
    question: Can I browse individual visitor sessions from last week?
  - id: getSession
    intent: View one visitor session's pages and details
    question: Which pages did a particular visitor go through in their session?
  phrasing_ops: 2
  slug: swetrix-sessions-api
- baseURL: https://api.swetrix.com
  baseurl_source: declared
  description: Aggregated traffic and pageview analytics
  name: Swetrix Traffic API
  phrasing_intents:
  - id: getTrafficLog
    intent: Get a project's traffic data over time
    question: How many visitors and pageviews did my site get each day last month?
  - id: getBirdseyeSummary
    intent: Compare traffic totals against the previous period
    question: Is my traffic up or down compared with the previous period?
  - id: getLiveVisitors
    intent: See who is on the site right now
    question: How many people are on my site right now?
  - id: getKeywords
    intent: Get search keywords from Google Search Console
    question: Which Google search keywords are bringing people to my site?
  - id: getUserFlow
    intent: See how visitors move between pages
    question: Where do visitors usually go after landing on my homepage?
  - id: getFilters
    intent: List available values for an analytics dimension
    question: Which browsers or countries can I filter my analytics by?
  phrasing_ops: 6
  slug: swetrix-traffic-api
- baseURL: https://api.swetrix.com
  baseurl_source: declared
  description: Manage saved dashboard views (segments)
  name: Swetrix Views API
  phrasing_intents:
  - id: listViews
    intent: List a project's saved dashboard views
    question: Which saved segments exist on my project's dashboard?
  - id: createView
    intent: Save a new dashboard view or segment
    question: How do I save a filtered segment of my dashboard for reuse?
  - id: getView
    intent: View one saved dashboard view's configuration
    question: What filters are stored in a particular saved view?
  - id: updateView
    intent: Change a saved view's name, filters or events
    question: Can I change the filters on a segment I already saved?
  - id: deleteView
    intent: Delete a saved dashboard view
    question: How do I get rid of a saved segment I don't use anymore?
  phrasing_ops: 5
  slug: swetrix-views-api
artifact_total: 62
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
- group: other
  href: https://artifacts.apis.io/swetrix/capabilities/swetrix-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/swetrix-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/swetrix/overview
- group: agent
  href: https://artifacts.apis.io/swetrix/agentic-access/swetrix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/swetrix-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/swetrix/security/swetrix-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/swetrix-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/swetrix/security/swetrix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swetrix-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/swetrix/authentication/swetrix-authentication.yml
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
  href: https://artifacts.apis.io/swetrix/packages/swetrix-packages.yml
  title: ''
  type: Packages
  url: packages/swetrix-packages.yml
- group: build
  href: https://artifacts.apis.io/swetrix/packages/swetrix-packages.yml
  title: ''
  type: SDKs
  url: packages/swetrix-packages.yml
- group: agent
  href: https://artifacts.apis.io/swetrix/llms/swetrix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/swetrix-llms.txt
- group: design
  href: https://artifacts.apis.io/swetrix/conventions/swetrix-conventions.yml
  title: ''
  type: Conventions
  url: conventions/swetrix-conventions.yml
- group: design
  href: https://artifacts.apis.io/swetrix/conventions/swetrix-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/swetrix-conventions.yml
- group: design
  href: https://artifacts.apis.io/swetrix/errors/swetrix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/swetrix-problem-types.yml
- group: design
  href: https://artifacts.apis.io/swetrix/lifecycle/swetrix-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/swetrix-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/swetrix/changelog/swetrix-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/swetrix-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Swetrix/swetrix/releases
- group: design
  href: https://artifacts.apis.io/swetrix/conformance/swetrix-conformance.yml
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
  href: https://artifacts.apis.io/swetrix/sandbox/swetrix-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/swetrix-sandbox.yml
- group: design
  href: https://artifacts.apis.io/swetrix/components/swetrix-components.yml
  title: ''
  type: Components
  url: components/swetrix-components.yml
- group: design
  href: https://artifacts.apis.io/swetrix/data-model/swetrix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/swetrix-data-model.yml
- group: design
  href: https://artifacts.apis.io/swetrix/asyncapi/swetrix-alerts-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/swetrix-alerts-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/swetrix/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/swetrix/rate-limits/swetrix-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/swetrix-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/swetrix/plans/swetrix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/swetrix-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/swetrix/finops/swetrix-finops.yml
  title: ''
  type: FinOps
  url: finops/swetrix-finops.yml
- group: design
  href: https://artifacts.apis.io/swetrix/vocabulary/swetrix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/swetrix-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/swetrix/rules/swetrix-rules.yml
  title: ''
  type: SpectralRules
  url: rules/swetrix-rules.yml
- group: design
  href: https://artifacts.apis.io/swetrix/rules/swetrix-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/swetrix-jsonschema-spectral-rules.yml
- group: docs
  href: https://artifacts.apis.io/swetrix/json-schema/swetrix-project-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/swetrix-project-schema.json
- group: docs
  href: https://artifacts.apis.io/swetrix/json-schema/swetrix-session-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/swetrix-session-schema.json
- group: design
  href: https://artifacts.apis.io/swetrix/json-structure/swetrix-project-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/swetrix-project-structure.json
- group: design
  href: https://artifacts.apis.io/swetrix/json-ld/swetrix-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/swetrix-context.jsonld
- group: build
  href: https://artifacts.apis.io/swetrix/examples/swetrix-create-project-example.json
  title: ''
  type: Examples
  url: examples/swetrix-create-project-example.json
- group: build
  href: https://artifacts.apis.io/swetrix/examples/swetrix-record-pageview-example.json
  title: ''
  type: Examples
  url: examples/swetrix-record-pageview-example.json
- group: build
  href: https://artifacts.apis.io/swetrix/examples/swetrix-get-traffic-log-example.json
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
- has_sources: true
  method: derived
  name: Swetrix Finops
  primary_unit: subscription
  service_category: ''
  slug: swetrix-finops
  template: false
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
overview: 'Swetrix publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Events API, Annotations API, Custom Events API, and 10 more. Tagged areas include Analytics, Cookieless Tracking, GDPR Compliant, Open Source, and Privacy.


  The Swetrix catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Swetrix''s developer surface includes authentication, documentation, engineering blog, pricing, GitHub presence, signup flow, support, and 53 more developer resources.'
plans:
- name: Swetrix Plans Pricing
  plan_count: 3
  slug: swetrix-plans-pricing
- name: Swetrix Price Estimates
  plan_count: 0
  slug: swetrix-price-estimates
random_paper: 22
rate_limits:
- limit_count: 3
  name: Swetrix Rate Limits
  slug: swetrix-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Swetrix — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: swetrix-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
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
  composite: 79.9
  coverage:
    artifact_dirs: 35
    catalog_earned: 81.0
    catalog_earned_first_party: 24.0
    catalog_gap: 34.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 92.1
    contract_governance: 45.5
    contract_quality: 67.6
    developer_ergonomics: 83.9
    discoverability: 73.2
    operational_transparency: 92.1
  previous_composite: 78.3
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
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/swetrix/swetrix-2026-06-20T194812.png
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
skill_count: 4
skills:
- name: Instrument a site and send events to Swetrix
  slug: swetrix-instrument-a-site
- name: Manage Swetrix projects, organisations, funnels, views and annotations
  slug: swetrix-manage-projects-and-teams
- name: Pull traffic, performance and session analytics from Swetrix
  slug: swetrix-pull-traffic-analytics
- name: Record revenue transactions in Swetrix idempotently
  slug: swetrix-record-revenue-idempotently
slug: swetrix
tags:
- Analytics
- Cookieless Tracking
- GDPR Compliant
- Open Source
- Privacy
- Real-Time Analytics
- Web Analytics
website: https://swetrix.com
---
