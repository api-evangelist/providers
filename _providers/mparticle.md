---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
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
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Mparticle Agentic Access
  operation_count: 16
  slug: mparticle-agentic-access
  summary_line: 16 operations · 13 acting
api_count: 6
apis:
- description: 'Server-to-server REST API for sending event batches and bulk uploads into mParticle from backend systems. Authenticates with HTTP Basic auth using a server-side API key and secret pair. Accepts up to '
  name: mParticle Events API
  slug: events-api
- description: 'Identity resolution REST API used to match, link, and modify user identities across devices and channels in mParticle, returning a stable mParticle ID (MPID) for downstream use. Accepts HTTP Basic or '
  name: mParticle IDSync API
  slug: idsync-api
- description: REST API for retrieving unified user profiles, identities, attributes, and audience memberships at scale to personalize downstream applications.
  name: mParticle Profile API
  slug: profile-api
- description: Management REST API used to programmatically configure mParticle inputs, outputs, filters, audiences, data plans, and workspace settings as part of a fully versioned CDP-as-code workflow. Authenticate
  name: mParticle Platform API
  slug: platform-api
- description: REST API for managing data plans and data plan versions in a workspace, and for validating an event batch against a plan without ingesting it. Each plan version is a set of data points, where a data p
  name: mParticle Data Planning API
  slug: data-planning-api
- description: REST API for building reverse-ETL pipelines that pull data out of a customer data warehouse (connections, data models, field transformations and pipelines) and load it into mParticle profiles and audi
  name: mParticle Warehouse Sync API
  slug: warehouse-sync-api
artifact_total: 22
asyncapis:
- description: ''
  name: Mparticle Webhooks
  slug: mparticle-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: mParticle Events Bulkevents API
  slug: open-mparticle-bulkevents-api
- collection_type: open
  name: mParticle Bulkevents Events API
  slug: open-mparticle-events-api
- collection_type: open
  name: mParticle Events API
  slug: open-mparticle
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mparticle-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mparticle-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mparticle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.rokt.com/vulnerability-disclosure/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mparticle.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mparticle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mparticle-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mparticle-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mparticle-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mparticle-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mparticle-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mparticle-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mparticle-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mparticle-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mparticle-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mparticle-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/mparticle-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mparticle-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mparticle-cli.yml
- group: design
  title: ''
  type: Components
  url: components/mparticle-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mparticle-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mparticle-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mparticle-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/mparticle-security.txt
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mparticle-eventsapi-schema.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mparticle-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mparticle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mparticle-inc-
- group: company
  title: ''
  type: Website
  url: https://www.mparticle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mparticle.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mparticle.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mparticle.com/developers/apis/http/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mparticle.com/guides/getting-started/
- group: build
  title: ''
  type: Postman
  url: https://docs.mparticle.com/downloads/dataplanning.postman_collection.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mparticle.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.mparticle.com/get-a-demo/
- group: start
  title: ''
  type: Login
  url: https://app.mparticle.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mparticle.com/legal/platform-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mparticle.com/privacypolicy/
- group: company
  title: ''
  type: Blog
  url: https://www.mparticle.com/blog/
created: '2026-05-11'
description: mParticle is a customer data platform (CDP) that helps brands collect, unify, and activate customer data across mobile, web, OTT, and server sources, then forward it in real time to hundreds of analytics, marketing, and warehouse destinations. The mParticle developer platform exposes server Events, IDSync, Profile, Warehouse Sync, Calculated Attributes, Data Planning and Platform APIs that let teams ingest events, resolve identity, manage configurations, and orchestrate audiences using HTTP Basic, an HMAC request digest, and OAuth 2.0 client-credentials bearer tokens. mParticle was acquired by Rokt.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mparticle.png
json_schemas:
- name: Mparticle Eventsapi Bulk
  property_count: 0
  slug: mparticle-eventsapi-bulk
- name: Mparticle Eventsapi Sample
  property_count: 0
  slug: mparticle-eventsapi-sample
- name: Mparticle Eventsapi
  property_count: 25
  slug: mparticle-eventsapi
layout: provider
mcp_servers:
- description: ''
  name: mparticle-mcp.yml
  slug: mparticle-mcpyml
modified: '2026-08-13'
name: mParticle
nav: Providers
network: true
overview: 'mParticle publishes 3 APIs on the [APIs.io](https://apis.io/) network: Events API, IDSync API, and Data Planning API. Tagged areas include Customer Data Platform, CDP, Analytics, Identity Resolution, and Audience.


  The mParticle catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  mParticle''s developer surface includes authentication, changelog, sandbox, CLI, documentation, API reference, getting-started guide, and 34 more developer resources.'
plans:
- name: Mparticle Plans Pricing
  plan_count: 0
  slug: mparticle-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 14
  name: Mparticle Rate Limits
  slug: mparticle-rate-limits
score:
  band: strong
  composite: 58.4
  delta: -8.6
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 64.1
    developer_ergonomics: 42.3
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 68.4
  previous_composite: 67.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/mparticle/refs/heads/main/screenshots/mparticle-2026-06-20T185839.png
security:
- kind: authentication
  name: Mparticle Authentication
  slug: mparticle-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Mparticle Domain Security
  slug: mparticle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mparticle Vulnerability Disclosure
  slug: mparticle-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mparticle Trust Center
  slug: mparticle-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: mparticle
tags:
- Customer Data Platform
- CDP
- Analytics
- Identity Resolution
- Audience
- Data Pipeline
- Marketing Data
- Event Streaming
- Data Governance
website: https://www.mparticle.com/
---
