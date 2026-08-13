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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Tealium Agentic Access
  operation_count: 15
  slug: tealium-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 11
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
- description: The Collect API from Tealium — 5 operation(s) for collect.
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
artifact_total: 29
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
modified: '2026-06-13'
name: Tealium
nav: Providers
network: true
overview: 'Tealium publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Collect API, Customer API, and 2 more. Tagged areas include Customer Data Platform, CDP, Tag Management, AudienceStream, and Real-Time Events.


  The Tealium catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tealium''s developer surface includes authentication, documentation, engineering blog, pricing, release notes, and 11 more developer resources.'
plans:
- name: Tealium Plans Pricing
  plan_count: 3
  slug: tealium-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 0
  name: Tealium Rate Limits
  slug: tealium-rate-limits
rules:
- name: Tealium API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tealium-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.1
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 63.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tealium/refs/heads/main/screenshots/tealium-2026-06-20T194955.png
security:
- kind: authentication
  name: Tealium Authentication
  slug: tealium-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tealium Domain Security
  slug: tealium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tealium Trust Center
  slug: tealium-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, HIPAA, GDPR
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
