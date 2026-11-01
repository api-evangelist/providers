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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Koala Io Agentic Access
  operation_count: 7
  slug: koala-io-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 2
apis:
- description: The client-side pixel loaded from cdn.getkoala.com/v1/{key}/sdk.js. Exposes ko.identify(), ko.track(), ko.qualify(), ko.reset() and autotracks pageviews, form fills, and session time. This is a browse
  name: Koala Web Pixel (JavaScript SDK)
  slug: koala-io-web-pixel-sdk
- baseURL: https://api2.getkoala.com/web/projects/{public_api_key}
  baseurl_source: declared
  description: Account-level (company) trait and event ingestion.
  name: Koala Accounts API
  slug: koala-io-accounts-api
- baseURL: https://api2.getkoala.com/web/projects/{public_api_key}
  baseurl_source: declared
  description: Server-side ingestion of visitor identifies, events, and traits.
  name: Koala Collection API
  slug: koala-io-collection-api
- baseURL: https://app.getkoala.com
  baseurl_source: declared
  description: GDPR right-to-erasure requests and status.
  name: Koala Deletion API
  slug: koala-io-deletion-api
- baseURL: https://api2.getkoala.com/web/projects/{public_api_key}
  baseurl_source: declared
  description: Bootstrap configuration used by the client-side pixel.
  name: Koala SDK API
  slug: koala-io-sdk-api
artifact_total: 34
asyncapis:
- description: ''
  name: Koala Io Auto Outbound Webhooks
  slug: koala-io-auto-outbound-webhooks
collections:
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
- group: other
  href: https://artifacts.apis.io/koala-io/capabilities/koala-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/koala-io-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/koala-io/agentic-access/koala-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/koala-io-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/koala-io/security/koala-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/koala-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/koala-io/security/koala-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/koala-io-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/koala-io/authentication/koala-io-authentication.yml
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
  href: https://artifacts.apis.io/koala-io/plans/koala-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/koala-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/koala-io/rate-limits/koala-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/koala-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/koala-io/finops/koala-io-finops.yml
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
  href: https://artifacts.apis.io/koala-io/vocabulary/koala-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/koala-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/koala-io/json-ld/koala-io-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/koala-io-context.jsonld
- group: docs
  href: https://artifacts.apis.io/koala-io/json-schema/koala-io-profile-batch-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/koala-io-profile-batch-request-schema.json
- group: other
  href: https://artifacts.apis.io/koala-io/a2a/koala-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/koala-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/koala-io/mcp/koala-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/koala-io-mcp.yml
- group: build
  href: https://artifacts.apis.io/koala-io/mcp/koala-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/koala-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/koala-io/llms/koala-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/koala-io-llms.txt
- group: build
  href: https://artifacts.apis.io/koala-io/packages/koala-io-packages.yml
  title: ''
  type: Packages
  url: packages/koala-io-packages.yml
- group: build
  href: https://artifacts.apis.io/koala-io/packages/koala-io-packages.yml
  title: ''
  type: SDKs
  url: packages/koala-io-packages.yml
- group: design
  href: https://artifacts.apis.io/koala-io/conventions/koala-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/koala-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/koala-io/conventions/koala-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/koala-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/koala-io/errors/koala-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/koala-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/koala-io/data-model/koala-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/koala-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/koala-io/lifecycle/koala-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/koala-io-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://koala.instatus.com
- group: operate
  href: https://artifacts.apis.io/koala-io/lifecycle/koala-io-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/koala-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/koala-io/conformance/koala-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/koala-io-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://app.vanta.com/koala/trust/tzb87epi5imm1qbxktj0bn
- group: auth
  href: https://artifacts.apis.io/koala-io/security/koala-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/koala-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://getkoala.com/security
- group: design
  href: https://artifacts.apis.io/koala-io/asyncapi/koala-io-auto-outbound-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/koala-io-auto-outbound-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/koala-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/koala-io/rules/koala-io-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/koala-io-jsonschema-spectral-rules.yml
- group: build
  href: https://artifacts.apis.io/koala-io/examples/koala-io-profile-batch-identify-example.json
  title: ''
  type: Examples
  url: examples/koala-io-profile-batch-identify-example.json
- group: build
  href: https://artifacts.apis.io/koala-io/examples/koala-io-profile-batch-track-example.json
  title: ''
  type: Examples
  url: examples/koala-io-profile-batch-track-example.json
- group: build
  href: https://artifacts.apis.io/koala-io/examples/koala-io-account-batch-traits-example.json
  title: ''
  type: Examples
  url: examples/koala-io-account-batch-traits-example.json
- group: build
  href: https://artifacts.apis.io/koala-io/examples/koala-io-account-batch-event-example.json
  title: ''
  type: Examples
  url: examples/koala-io-account-batch-event-example.json
- group: docs
  href: https://artifacts.apis.io/koala-io/json-schema/koala-io-account-batch-request-schema.json
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
- has_sources: true
  method: derived
  name: Koala Io Finops
  primary_unit: subscription
  service_category: ''
  slug: koala-io-finops
  template: false
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
- description: Remote MCP server at koala.mintlify.app over HTTP; 3 tools listed.
  name: Koala MCP Server
  slug: koala-docs
modified: '2026-08-13'
name: Koala
nav: Providers
network: true
overview: 'Koala publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Collection API, Deletion API, and 2 more. Tagged areas include Buyer Intent, Visitor Identification, De-anonymization, Data Enrichment, and Go-To-Market.


  The Koala catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Koala''s developer surface includes authentication, documentation, pricing, code examples, API reference, getting-started guide, signup flow, and 44 more developer resources.'
plans:
- name: Koala Io Plans Pricing
  plan_count: 4
  slug: koala-io-plans-pricing
- name: Koala Io Price Estimates
  plan_count: 0
  slug: koala-io-price-estimates
random_paper: 13
rate_limits:
- limit_count: 11
  name: Koala Io Rate Limits
  slug: koala-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Koala — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: koala-io-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 70.7
  coverage:
    artifact_dirs: 30
    catalog_earned: 79.8
    catalog_earned_first_party: 24.0
    catalog_gap: 35.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 28.0
    contract_quality: 65.8
    developer_ergonomics: 55.4
    discoverability: 65.0
    operational_transparency: 78.9
  previous_composite: 69.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
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
screenshot: https://apis.io/screenshots/koala-io/koala-io-2026-07-25T224023.png
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
  summary_line: no policy recorded
- kind: trust-center
  name: Koala Io Trust Center
  slug: koala-io-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA
skill_count: 3
skills:
- name: Identify a Koala visitor from your backend
  slug: koala-io-identify-a-visitor-server-side
- name: Request and verify a Koala GDPR erasure
  slug: koala-io-request-gdpr-erasure
- name: Send Koala account traits and events
  slug: koala-io-send-account-traits-and-events
slug: koala-io
tags:
- Buyer Intent
- Visitor Identification
- De-anonymization
- Data Enrichment
- Go-To-Market
- Sales Intelligence
- B2B
- A2A
website: https://getkoala.com
---
