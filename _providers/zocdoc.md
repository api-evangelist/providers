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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Zocdoc Agentic Access
  operation_count: 32
  slug: zocdoc-agentic-access
  summary_line: 32 operations · 11 acting
api_count: 1
apis:
- description: Endpoints for booking, cancelling, and rescheduling appointments, including retrieving current appointment statuses and updated information.
  name: Zocdoc appointments API
  slug: zocdoc-appointments-api
- description: Endpoints to manage timeslots for providers.
  name: Zocdoc calendar-integration-timeslots API
  slug: zocdoc-calendar-integration-timeslots-api
- description: Endpoints for managing API credentials.
  name: Zocdoc credentials API
  slug: zocdoc-credentials-api
- description: Endpoints to retrieve facilities within the developer's directory.
  name: Zocdoc facilities API
  slug: zocdoc-facilities-api
- description: Endpoints to retrieve insurance plans supported by Zocdoc.
  name: Zocdoc insurance-reference API
  slug: zocdoc-insurance-reference-api
- description: Endpoints for retrieving and modifying provider location objects and their related insurance plans and availability.
  name: Zocdoc provider-locations API
  slug: zocdoc-provider-locations-api
- description: Endpoints to retrieve providers within the developer's directory.
  name: Zocdoc providers API
  slug: zocdoc-providers-api
- description: Endpoints to retrieve information about the developer's directory.
  name: Zocdoc reference API
  slug: zocdoc-reference-api
- description: Endpoints to retrieve schedulable entities with availability information.
  name: Zocdoc schedulable-entities API
  slug: zocdoc-schedulable-entities-api
- description: Sandbox endpoints to mock webhook behavior
  name: Zocdoc webhook API
  slug: zocdoc-webhook-api
- description: Endpoints to retrieve aggregate review summaries for providers, individually or in batches of up to 100 provider IDs.
  name: Zocdoc reviews API
  slug: zocdoc-reviews-api
- description: Reference endpoints to retrieve the specialties Zocdoc supports and their default visit reasons, optionally filtered by care category.
  name: Zocdoc specialties API
  slug: zocdoc-specialties-api
- description: Reference endpoints to retrieve the visit reasons Zocdoc supports and the specialty each one belongs to. Visit reason drives appointment duration and bookable timeslots.
  name: Zocdoc visit-reasons API
  slug: zocdoc-visit-reasons-api
artifact_total: 42
asyncapis:
- description: ''
  name: Zocdoc Webhooks
  slug: zocdoc-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Documentation appointments API
  slug: open-zocdoc-appointments-api
- collection_type: open
  name: API Documentation appointments calendar-integration-timeslots API
  slug: open-zocdoc-calendar-integration-timeslots-api
- collection_type: open
  name: API Documentation appointments credentials API
  slug: open-zocdoc-credentials-api
- collection_type: open
  name: API Documentation appointments facilities API
  slug: open-zocdoc-facilities-api
- collection_type: open
  name: API Documentation appointments insurance-reference API
  slug: open-zocdoc-insurance-reference-api
- collection_type: open
  name: API Documentation appointments provider-locations API
  slug: open-zocdoc-provider-locations-api
- collection_type: open
  name: API Documentation appointments providers API
  slug: open-zocdoc-providers-api
- collection_type: open
  name: API Documentation appointments reference API
  slug: open-zocdoc-reference-api
- collection_type: open
  name: API Documentation appointments schedulable-entities API
  slug: open-zocdoc-schedulable-entities-api
- collection_type: open
  name: API Documentation appointments webhook API
  slug: open-zocdoc-webhook-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/zocdoc-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zocdoc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zocdoc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zocdoc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zocdoc-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zocdoc.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.zocdoc.com/guides
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Zocdoc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zocdoc
- group: company
  title: ''
  type: Blog
  url: https://medium.com/zocdoc-engineering
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zocdoc.com/about/news/zocdoc-launches-its-first-ever-public-api-platform-zocdoc-for-developers/
- group: other
  title: ''
  type: X
  url: https://x.com/Zocdoc
- group: commercial
  title: ''
  type: Plans
  url: plans/zocdoc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zocdoc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zocdoc-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/zocdoc-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/zocdoc-provider.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/zocdoc-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/zocdoc-jsonschema-spectral-rules.yml
- group: build
  title: ''
  type: Examples
  url: examples/book-appointment-request.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zocdoc-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zocdoc-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/zocdoc-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zocdoc-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/zocdoc-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zocdoc-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zocdoc-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zocdoc-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zocdoc-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zocdoc-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zocdoc-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zocdoc-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zocdoc-webhooks.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.zocdoc.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.zocdoc.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.zocdoc.com/guides
- group: operate
  title: ''
  type: Support
  url: https://api-docs.zocdoc.com/guides/faqs
- group: start
  title: ''
  type: SignUp
  url: https://developer.zocdoc.com/?utm_medium=organicpro&utm_routing=API_Sender#api-form
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zocdoc.com/about/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zocdoc.com/about/consumer-health-data-privacy-policy/
created: '2026-06-13'
description: Zocdoc is a healthcare appointment booking platform that provides a REST API for accessing provider availability, booking appointments, managing insurance verification, and patient scheduling. The Zocdoc for Developers platform enables integration with Zocdoc's provider network through patient booking, provider calendar integration, and insurance APIs using OAuth 2.0 authentication with both sandbox and production environments.
examples:
- key_count: 2
  name: Availability Response
  slug: availability-response
- key_count: 2
  name: Book Appointment Request
  slug: book-appointment-request
- key_count: 2
  name: Book Appointment Response
  slug: book-appointment-response
finops:
- name: Zocdoc Finops
  service_category: ''
  slug: zocdoc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zocdoc.png
json_schemas:
- name: Appointment
  property_count: 6
  slug: zocdoc-appointment
- name: Availability
  property_count: 3
  slug: zocdoc-availability
- name: Provider
  property_count: 16
  slug: zocdoc-provider
jsonld:
- class_count: 0
  name: Zocdoc Context
  property_count: 70
  slug: zocdoc-context
layout: provider
mcp_servers:
- description: ''
  name: Zocdoc MCP Server
  slug: zocdoc-mcp-server
modified: '2026-08-15'
name: Zocdoc
nav: Providers
network: true
overview: 'Zocdoc publishes 13 APIs on the [APIs.io](https://apis.io/) network, including appointments API, calendar-integration-timeslots API, credentials API, and 10 more. Tagged areas include Healthcare, Appointments, Booking, Providers, and Insurance.


  The Zocdoc catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Zocdoc''s developer surface includes authentication, documentation, engineering blog, pricing, code examples, changelog, sandbox, and 34 more developer resources.'
plans:
- name: Zocdoc Plans Pricing
  plan_count: 2
  slug: zocdoc-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Zocdoc Rate Limits
  slug: zocdoc-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Zocdoc API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: zocdoc-jsonschema-spectral-rules
scopes:
- name: Zocdoc Scopes
  scope_count: 10
  slug: zocdoc-scopes
  summary_line: 10 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 65.3
  coverage:
    artifact_dirs: 31
    catalog_gap: 50.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.8
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 29.5
    contract_quality: 71.6
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 29.5
    operational_transparency: 28.9
  previous_composite: 67.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 60.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zocdoc/refs/heads/main/screenshots/zocdoc-2026-06-20T201932.png
security:
- kind: authentication
  name: Zocdoc Authentication
  slug: zocdoc-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Zocdoc Domain Security
  slug: zocdoc-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Zocdoc Vulnerability Disclosure
  slug: zocdoc-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: zocdoc
tags:
- Healthcare
- Appointments
- Booking
- Providers
- Insurance
- Telehealth
- Scheduling
website: https://www.zocdoc.com
---
