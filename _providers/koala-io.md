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
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 76.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Koala Io Agentic Access
  operation_count: 7
  slug: koala-io-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 5
apis:
- description: The client-side pixel loaded from cdn.getkoala.com/v1/{key}/sdk.js. Exposes ko.identify(), ko.track(), ko.qualify(), ko.reset() and autotracks pageviews, form fills, and session time. This is a browse
  name: Koala Web Pixel (JavaScript SDK)
  slug: koala-io-web-pixel-sdk
- description: Account-level (company) trait and event ingestion.
  name: Koala Accounts API
  slug: koala-io-accounts-api
- description: Server-side ingestion of visitor identifies, events, and traits.
  name: Koala Collection API
  slug: koala-io-collection-api
- description: GDPR right-to-erasure requests and status.
  name: Koala Deletion API
  slug: koala-io-deletion-api
- description: Bootstrap configuration used by the client-side pixel.
  name: Koala SDK API
  slug: koala-io-sdk-api
artifact_total: 31
asyncapis:
- description: ''
  name: Koala Io Auto Outbound Webhooks
  slug: koala-io-auto-outbound-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Koala Server-Side Account Ingestion API
  slug: open-koala-io-account-ingestion-api
- collection_type: open
  name: Koala Accounts API
  slug: open-koala-io-accounts-api
- collection_type: open
  name: Koala Accounts Collection API
  slug: open-koala-io-collection-api
- collection_type: open
  name: Koala Accounts Deletion API
  slug: open-koala-io-deletion-api
- collection_type: open
  name: Koala Server-Side Account Ingestion Profile Ingestion API
  slug: open-koala-io-profile-ingestion-api
- collection_type: open
  name: Koala Accounts SDK API
  slug: open-koala-io-sdk-api
- collection_type: open
  name: Koala API
  slug: open-koala-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/koala-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/koala-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koala-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/koala-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getkoala
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getkoala
- group: company
  title: ''
  type: Website
  url: https://getkoala.com
- group: docs
  title: ''
  type: Documentation
  url: https://getkoala.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/koala-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/koala-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/koala-io-finops.yml
- group: other
  title: ''
  type: X
  url: https://x.com/getkoala_com
- group: commercial
  title: ''
  type: Pricing
  url: https://getkoala.com/pricing
- group: build
  title: ''
  type: SDKs
  url: https://github.com/getkoala/react
- group: build
  title: ''
  type: NPM
  url: https://www.npmjs.com/package/@getkoala/edge-api-client
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/koala-io-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/koala-io-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/koala-io-profile-batch-request-schema.json
- group: other
  title: ''
  type: AgentCard
  url: a2a/koala-io-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/koala-io-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/koala-io-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/koala-io-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/koala-io-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/koala-io-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/koala-io-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/koala-io-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/koala-io-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/koala-io-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/koala-io-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://koala.instatus.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/koala-io-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/koala-io-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://app.vanta.com/koala/trust/tzb87epi5imm1qbxktj0bn
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/koala-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://getkoala.com/security
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/koala-io-auto-outbound-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/koala-io-jsonschema-spectral-rules.yml
- group: build
  title: ''
  type: Examples
  url: examples/koala-io-profile-batch-identify-example.json
- group: build
  title: ''
  type: Examples
  url: examples/koala-io-profile-batch-track-example.json
- group: build
  title: ''
  type: Examples
  url: examples/koala-io-account-batch-traits-example.json
- group: build
  title: ''
  type: Examples
  url: examples/koala-io-account-batch-event-example.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/koala-io-account-batch-request-schema.json
- group: docs
  title: ''
  type: APIReference
  url: https://getkoala.com/docs/developer-guides/server-side
- group: start
  title: ''
  type: GettingStarted
  url: https://getkoala.com/docs/get-started/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://app.getkoala.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.getkoala.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getkoala.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getkoala.com/legal/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@getkoala.com
created: '2026-07-01'
description: Koala is a B2B buyer-intent and go-to-market platform that de-anonymizes website and product traffic, identifies the visitors and companies behind it, enriches them with firmographic and contact data (via Clearbit Reveal/Enrich and ZoomInfo), and scores first-party intent so sales teams can act on the accounts showing the strongest signals. Its developer surface is a client-side JavaScript pixel plus an HTTP collection API for server-side identify, event, and account ingestion, with a separate secret-key admin API for GDPR deletion.
examples:
- key_count: 3
  name: Koala Io Account Batch Event Example
  slug: koala-io-account-batch-event-example
- key_count: 3
  name: Koala Io Account Batch Traits Example
  slug: koala-io-account-batch-traits-example
- key_count: 3
  name: Koala Io Profile Batch Identify Example
  slug: koala-io-profile-batch-identify-example
- key_count: 3
  name: Koala Io Profile Batch Track Example
  slug: koala-io-profile-batch-track-example
finops:
- name: Koala Io Finops
  service_category: Analytics and Sales Intelligence
  slug: koala-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/koala-io.png
json_schemas:
- name: KoalaAccountBatchRequest
  property_count: 4
  slug: koala-io-account-batch-request
- name: KoalaProfileBatchRequest
  property_count: 5
  slug: koala-io-profile-batch-request
jsonld:
- class_count: 0
  name: Koala Io Context
  property_count: 23
  slug: koala-io-context
layout: provider
mcp_servers:
- description: ''
  name: koala-io-mcp.yml
  slug: koala-io-mcpyml
modified: '2026-08-13'
name: Koala
nav: Providers
network: true
overview: 'Koala publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Collection API, Deletion API, and 1 more. Tagged areas include Buyer Intent, Visitor Identification, De-anonymization, Enrichment, and Go-to-Market.


  The Koala catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Koala''s developer surface includes authentication, documentation, pricing, code examples, API reference, getting-started guide, signup flow, and 43 more developer resources.'
plans:
- name: Koala Io Plans Pricing
  plan_count: 4
  slug: koala-io-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 11
  name: Koala Io Rate Limits
  slug: koala-io-rate-limits
rules:
- name: Koala API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: koala-io-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 80.8
  delta: 26.3
  facets:
    commercial_clarity: 100.0
    contract_quality: 76.3
    developer_ergonomics: 63.0
    discoverability: 81.5
    governance: 89.6
    operational_transparency: 78.9
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/koala-io/refs/heads/main/screenshots/koala-io-2026-07-25T224023.png
security:
- kind: authentication
  name: Koala Io Authentication
  slug: koala-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Koala Io Domain Security
  slug: koala-io-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Koala Io Vulnerability Disclosure
  slug: koala-io-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Koala Io Trust Center
  slug: koala-io-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA
slug: koala-io
tags:
- Buyer Intent
- Visitor Identification
- De-anonymization
- Enrichment
- Go-to-Market
- Sales Intelligence
- B2B
website: https://getkoala.com
---
