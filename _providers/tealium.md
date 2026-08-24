---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Tealium Agentic Access
  operation_count: 15
  slug: tealium-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 12
apis:
- description: Sends authenticated events from any application via HTTP requests into the Tealium Customer Data Hub. Supports single-event and bulk-event endpoints (up to 10 events per request) with regional routing
  name: Tealium Collect HTTP API
  slug: tealium-collect-http-api
- description: Provides programmatic access to iQ Tag Management configuration, allowing retrieval and modification of tags, load rules, events, variables, JavaScript extensions, and tag templates within an iQ profi
  name: Tealium iQ Profiles API
  slug: tealium-iq-profiles-api
- description: Queries full visitor profile records from the AudienceStream Customer Data Hub, returning audience memberships, badges, and attribute values for a given visitor. Used to retrieve the complete live pro
  name: Tealium Visitor Profile API
  slug: tealium-visitor-profile-api
- description: Supports GDPR and CCPA compliance by allowing retrieval and deletion of visitor profile records from the Customer Data Hub. Provides endpoints to look up all known data about a specific visitor and to
  name: Tealium Visitor Privacy API
  slug: tealium-visitor-privacy-api
- description: A high-performance, configurable endpoint that retrieves a targeted slice of live visitor context for real-time personalization, AI systems, and cross-channel experiences. Operates through customizabl
  name: Tealium Moments API
  slug: tealium-moments-api
- description: Enables bulk import and export of event and audience data between Tealium and external systems. Supports the Tealium Events App for streaming event records. Rate limits are 500 events per second and 5
  name: Tealium Data Connect API
  slug: tealium-data-connect-api
- description: The Auth API from Tealium — 1 operation(s) for auth.
  name: Tealium Auth API
  slug: tealium-auth-api
- description: The Collect API from Tealium — 6 operation(s) for collect.
  name: Tealium Collect API
  slug: tealium-collect-api
- description: The Customer API from Tealium — 2 operation(s) for customer.
  name: Tealium Customer API
  slug: tealium-customer-api
- description: The Personalization API from Tealium — 2 operation(s) for personalization.
  name: Tealium Personalization API
  slug: tealium-personalization-api
- description: The Privacy API from Tealium — 3 operation(s) for privacy.
  name: Tealium Privacy API
  slug: tealium-privacy-api
- description: Tealium's own minimal, read-only API for AI agents, published as OpenAPI 3.0.3 at https://tealium.com/.well-known/openapi.yaml and discovered from https://tealium.com/llms.txt. Three unauthenticated G
  name: Tealium AI Read API
  slug: tealium-ai-read-api
artifact_total: 39
asyncapis:
- description: ''
  name: Tealium Webhooks
  slug: tealium-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tealium AI Read API
  slug: open-tealium-ai-read
- collection_type: open
  name: Tealium Authentication Auth API
  slug: open-tealium-auth-api
- collection_type: open
  name: Tealium Authentication Auth Collect API
  slug: open-tealium-collect-api
- collection_type: open
  name: Tealium Authentication Auth Customer API
  slug: open-tealium-customer-api
- collection_type: open
  name: Tealium Authentication Auth Personalization API
  slug: open-tealium-personalization-api
- collection_type: open
  name: Tealium Authentication Auth Privacy API
  slug: open-tealium-privacy-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tealium-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tealium-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tealium-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tealium-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tealium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tealium.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Tealium
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tealium
- group: company
  title: ''
  type: Blog
  url: https://tealium.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://tealium.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tealium.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/tealium
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.tealium.com/release-notes/
- group: commercial
  title: ''
  type: Plans
  url: plans/tealium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tealium-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tealium-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tealium-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/tealium-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tealium-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tealium-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tealium-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/tealium-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tealium-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tealium-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tealium-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tealium-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://tealium.com/security/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tealium-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tealium-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tealium-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tealium-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/tealium-jsonschema-spectral-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tealium-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tealium.com/developer-center/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tealium.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tealium.com/api/v3/getting-started/request-format/
- group: operate
  title: ''
  type: Support
  url: https://tealium.com/customer-support-packages/
- group: start
  title: ''
  type: Login
  url: https://my.tealiumiq.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tealium.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tealium.com/privacy/
created: '2026-06-13'
description: Tealium is a customer data platform (CDP) providing REST APIs for iQ Tag Management and AudienceStream — enabling enterprises to manage tags, audiences, attributes, connectors, and real-time event data collection across web, mobile, and server-side channels. The Tealium Customer Data Hub unifies data collection via the Collect HTTP API, real-time visitor profiling via the Visitor Profile and Moments APIs, tag and load-rule management via the iQ Profiles API, and privacy compliance via the Visitor Privacy API.
examples:
- key_count: 4
  name: Tealium Collect Bulk Event Example
  slug: tealium-collect-bulk-event-example
- key_count: 4
  name: Tealium Collect Single Event Example
  slug: tealium-collect-single-event-example
- key_count: 4
  name: Tealium Moments Response Example
  slug: tealium-moments-response-example
- key_count: 3
  name: Tealium Visitor Privacy Delete Example
  slug: tealium-visitor-privacy-delete-example
finops:
- name: Tealium Finops
  service_category: ''
  slug: tealium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tealium.png
json_schemas:
- name: Tealium Authentication Response
  property_count: 2
  slug: tealium-auth-response
- name: Tealium Bulk Event Payload
  property_count: 2
  slug: tealium-bulk-event-payload
- name: Tealium Event Payload
  property_count: 6
  slug: tealium-event-payload
- name: Tealium Moments API Response
  property_count: 6
  slug: tealium-moments-response
- name: Tealium Visitor Profile
  property_count: 7
  slug: tealium-visitor-profile
jsonld:
- class_count: 4
  name: Tealium Context
  property_count: 53
  slug: tealium-context
layout: provider
mcp_servers:
- description: Tealium operates a first-party, fully managed remote MCP server in front of the Moments API. AI systems connect over Streamable HTTP to retrieve a targeted slice of live visitor context — audiences, b
  name: Tealium MCP Server
  slug: tealium-mcp-server
modified: '2026-08-13'
name: Tealium
nav: Providers
network: true
overview: 'Tealium publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Collect API, Customer API, and 3 more. Tagged areas include Customer Data Platform, CDP, Tag Management, AudienceStream, and Real-Time Events.


  The Tealium catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Tealium''s developer surface includes authentication, documentation, engineering blog, pricing, release notes, changelog, sandbox, and 35 more developer resources.'
plans:
- name: Tealium Plans Pricing
  plan_count: 3
  slug: tealium-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Tealium Rate Limits
  slug: tealium-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tealium API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tealium-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 68.9
  delta: 0.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 55.3
    contract_quality: 60.0
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 55.3
    operational_transparency: 44.7
  previous_composite: 68.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 16.7
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tealium/refs/heads/main/screenshots/tealium-2026-06-20T194955.png
security:
- kind: authentication
  name: Tealium Authentication
  slug: tealium-authentication
  summary_line: http/apiKey/none · 4 schemes
- kind: domain-security
  name: Tealium Domain Security
  slug: tealium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tealium Trust Center
  slug: tealium-trust-center
  summary_line: SSAE18 SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27018, ISO/IEC 27701:2019, HIPAA & HITECH, TISAX, TX-RAMP, Cloud Security Alliance (CSA), GDPR, CCPA
slug: tealium
tags:
- Customer Data Platform
- CDP
- Tag Management
- AudienceStream
- Real-Time Events
- Visitor Profiles
- Audience Segmentation
- Data Collection
- Privacy Compliance
- Personalization
website: https://tealium.com/
---
