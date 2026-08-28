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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Simon Data Agentic Access
  operation_count: 2
  slug: simon-data-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: The Simon Audience API returns a single Simon Data contact profile at request time so marketers can personalise content across email, SMS, push and front-of-house tools. Contacts are looked up with an
  name: Simon Data Audience API
  slug: simon-data-contacts-api
- description: Simon Signal is Simon Data's event protocol and event-processing pipeline. The Event Ingestion API accepts a single behavioural or transactional event per request at POST /events/v1/collect across pro
  name: Simon Data Event Ingestion API
  slug: simon-data-events-api
artifact_total: 23
asyncapis:
- description: ''
  name: Simon Data Webhooks
  slug: simon-data-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Simon Data Audience API
  slug: open-simon-data-audience-api
- collection_type: open
  name: Simon Data Event Ingestion API (Simon Signal)
  slug: open-simon-data-event-ingestion
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/simon-data-audience-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/simon-data-event-ingestion-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/simon-data-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/simon-data-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simon-data-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simon-data-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simon-data-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/simon-data-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/simon-data-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/simon-data-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/simon-data-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simon-data-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.simondata.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/simon-data-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.simondata.com/changelog
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/simon-data-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/simon-data-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/simon-data-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/simon-data-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/simon-data-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.simon.ai/terms/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/simon-data-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.simon.ai/terms/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/simon-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simon-data-domain-security.yml
- group: build
  title: ''
  type: Examples
  url: examples/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/simon-data-contact-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/simon-data-event-payload-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/simon-data-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/simon-data-context.jsonld
- group: design
  title: ''
  type: Rules
  url: rules/simon-data-jsonschema-spectral-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/simon-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simon-data-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/simon-data-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.simon.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.simondata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.simondata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.simondata.com/reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.simondata.com/reference/ingestion-and-egress-in-5-minutes
- group: operate
  title: ''
  type: Support
  url: https://docs.simondata.com/docs/support-center
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Radico
- group: company
  title: ''
  type: Blog
  url: https://www.simon.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.simon.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.simondata.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.simon.ai/terms/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.simon.ai/terms/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simon-ai-the-agentic-marketing-platform/
- group: other
  title: ''
  type: X
  url: https://x.com/simon_data
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@simon-ai-marketing-platform
created: '2026-06-13'
description: 'Simon Data — now trading as Simon AI, and acquired by Monetate on 30 July 2026 — is a composable, AI-first customer data platform for marketing teams. It reads customer data directly from a cloud warehouse (Snowflake, BigQuery, Redshift, Azure) without ETL, resolves identity into unified profiles, and activates segments across email, SMS, push, paid media and 70-plus downstream tools including Braze, Iterable, Attentive, Klaviyo, Salesforce Marketing Cloud, Amazon Ads and The Trade Desk. Two callable APIs are published: the Simon Signal Event Ingestion API, which accepts fourteen documented behavioural and transactional event types at a single collect endpoint, and the premium Audience API, which returns one contact profile at a time for send-time personalisation. Outbound webhooks and a Real-Time Content client cover the reverse direction, calling customer endpoints at send time.'
examples:
- key_count: 2
  name: Simon Data Get Contact Example
  slug: simon-data-get-contact-example
- key_count: 8
  name: Simon Data Identify Example
  slug: simon-data-identify-example
- key_count: 9
  name: Simon Data Track Transaction Example
  slug: simon-data-track-transaction-example
finops:
- name: Simon Data Finops
  service_category: ''
  slug: simon-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simon-data.png
json_schemas:
- name: Simon Data Contact
  property_count: 2
  slug: simon-data-contact
- name: Simon Data Event Payload
  property_count: 12
  slug: simon-data-event-payload
jsonld:
- class_count: 4
  name: Simon Data Context
  property_count: 40
  slug: simon-data-context
layout: provider
mcp_servers:
- description: ''
  name: Simon Data MCP Server
  slug: simon-data-mcp-server
modified: '2026-08-13'
name: Simon Data
nav: Providers
network: true
overview: 'Simon Data publishes 2 APIs on the [APIs.io](https://apis.io/) network: Audience API and Event Ingestion API. Tagged areas include Customer Data Platform, CDP, Marketing Automation, Audience Segmentation, and Event Tracking.


  The Simon Data catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Simon Data''s developer surface includes authentication, changelog, sandbox, code examples, documentation, API reference, getting-started guide, and 43 more developer resources.'
plans:
- name: Simon Data Plans Pricing
  plan_count: 1
  slug: simon-data-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Simon Data Rate Limits
  slug: simon-data-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Simon Data API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: simon-data-jsonschema-spectral-rules
scopes:
- name: Simon Data Scopes
  scope_count: 0
  slug: simon-data-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.0
  delta: 0.0
  facets:
    access_clarity: 82.9
    commercial_clarity: 82.9
    contract_governance: 41.7
    contract_quality: 76.9
    developer_ergonomics: 44.6
    discoverability: 87.0
    governance: 41.7
    operational_transparency: 65.8
  previous_composite: 67.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simon-data/refs/heads/main/screenshots/simon-data-2026-06-20T193927.png
security:
- kind: authentication
  name: Simon Data Authentication
  slug: simon-data-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Simon Data Domain Security
  slug: simon-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Simon Data Vulnerability Disclosure
  slug: simon-data-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Simon Data Trust Center
  slug: simon-data-trust-center
  summary_line: SOC 2, GDPR
slug: simon-data
tags:
- Customer Data Platform
- CDP
- Marketing Automation
- Audience Segmentation
- Event Tracking
- Data Ingestion
- Personalization
- Marketing Technology
- Identity Resolution
- Customer Profiles
- Journey Orchestration
- Snowflake
website: https://www.simon.ai/
---
