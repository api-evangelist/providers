---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
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
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.7
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: B Well Agentic Access
  operation_count: 3
  slug: b-well-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 2
apis:
- description: 'Federated GraphQL gateway plus REST endpoints that let end-user applications read and write a person''s health data, manage data-source connections, handle consent, and coordinate care workflows in an '
  name: b.well Application APIs
  slug: application-apis
- description: System-level FHIR R4 API over b.well's normalized clinical data store, built on the open-source Helix FHIR Server. Supports standard FHIR REST search, $everything bulk patient retrieval, International
  name: b.well FHIR Server
  slug: fhir-server
- description: A b.well-hosted Model Context Protocol server that exposes a catalog of healthcare agents/tools — insurance coverage validation, FHIR record and lab retrieval, patient summaries, provider search, appo
  name: b.well Health SDK for AI (MCP Server)
  slug: health-sdk-for-ai-mcp
- baseURL: https://api.client-sandbox.icanbwell.com/v1
  baseurl_source: declared
  description: The Users API from b.well — 2 operation(s) for users.
  name: b.well Users API
  slug: b-well-users-api
- baseURL: https://api.client-sandbox.icanbwell.com/v1
  baseurl_source: declared
  description: The Webhook API from b.well — 1 operation(s) for webhook.
  name: b.well Webhook API
  slug: b-well-webhook-api
artifact_total: 20
asyncapis:
- description: ''
  name: B Well Webhooks
  slug: b-well-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Client Webhook API
  slug: open-b-well-client-webhook-api
- collection_type: open
  name: bwell User Data Operations
  slug: open-b-well-user-data-operations
- collection_type: open
  name: bwell User Data Operations Users API
  slug: open-b-well-users-api
- collection_type: open
  name: Client Webhook API
  slug: open-b-well-webhook-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/overlays/b-well-client-webhook-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/b-well-client-webhook-api-overlay.yaml
- group: operate
  title: ''
  type: Releases
  url: https://github.com/icanbwell/fhir-server/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/icanbwell/fhir-server/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/icanbwell/fhir-server/blob/main/LICENSE
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/agentic-access/b-well-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/b-well-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.icanbwell.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bwell.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bwell.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bwell.com/reference/ts-sdk-apireference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bwell.com/docs/welcome
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/authentication/b-well-authentication.yml
  title: ''
  type: Authentication
  url: authentication/b-well-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/scopes/b-well-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/b-well-scopes.yml
- group: operate
  title: ''
  type: Support
  url: mailto:support@icanbwell.com
- group: company
  title: ''
  type: Blog
  url: https://resources.icanbwell.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/icanbwell
- group: start
  title: ''
  type: Login
  url: https://developer.bwell.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.icanbwell.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.icanbwell.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bwell.com
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/changelog/b-well-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/b-well-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/lifecycle/b-well-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/b-well-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/packages/b-well-packages.yml
  title: ''
  type: Packages
  url: packages/b-well-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/packages/b-well-packages.yml
  title: ''
  type: SDKs
  url: packages/b-well-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/well-known/b-well-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/b-well-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/well-known/b-well-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/b-well-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.icanbwell.com/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/security/b-well-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/b-well-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/security/b-well-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/b-well-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/llms/b-well-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/b-well-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/mcp/b-well-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/b-well-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/mcp/b-well-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/b-well-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/conformance/b-well-conformance.yml
  title: ''
  type: Conformance
  url: conformance/b-well-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/errors/b-well-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/b-well-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/conventions/b-well-conventions.yml
  title: ''
  type: Conventions
  url: conventions/b-well-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/sandbox/b-well-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/b-well-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/components/b-well-components.yml
  title: ''
  type: Components
  url: components/b-well-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/data-model/b-well-data-model.yml
  title: ''
  type: DataModel
  url: data-model/b-well-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/asyncapi/b-well-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/b-well-webhooks.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/plans/b-well-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/b-well-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/rate-limits/b-well-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/b-well-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/security/b-well-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/b-well-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/security/b-well-trust-center.yml
  title: ''
  type: Compliance
  url: security/b-well-trust-center.yml
created: '2026-08-06'
description: b.well Connected Health is a Baltimore-based digital health platform that unifies a person's fragmented medical, pharmacy, claims, wearable and lab data into a single FHIR-native longitudinal health record, then exposes that record to partner applications through a developer platform. The company operates a consumer-mediated health data network spanning millions of providers, health plans, HIEs/HINs, TEFCA QHINs and CMS-aligned networks, and licenses it to health systems, payers, employers and retail health brands who embed it in their own apps. Its developer surface is built around four Health SDKs (Web/TypeScript, Android/Kotlin, iOS/Swift and an AI SDK that speaks Model Context Protocol), a federated GraphQL gateway, REST endpoints for user data operations and webhooks, and a FHIR R4 server (the open-source Helix FHIR Server) supporting $everything and International Patient Summary retrieval. Authentication is OAuth 2.0 throughout — token exchange with OIDC for end-user context,
  client credentials for system-to-system access, and HMAC-SHA512 request signing on the user data operations API.
image: https://www.icanbwell.com/wp-content/uploads/2023/01/bwell-logo.png
layout: provider
mcp_servers:
- description: ''
  name: b.well MCP Server
  slug: bwell-mcp-server
modified: '2026-08-15'
name: b.well
nav: Providers
network: true
overview: 'b.well publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Users API, Webhook API, and 3 more. Tagged areas include Company, Health, Healthcare, Digital Health, and FHIR.


  The b.well catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  b.well''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, changelog, and 36 more developer resources.'
plans:
- name: B Well Plans Pricing
  plan_count: 0
  slug: b-well-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: B Well Rate Limits
  slug: b-well-rate-limits
scopes:
- name: B Well Scopes
  scope_count: 4
  slug: b-well-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 57.0
    developer_ergonomics: 49.4
    discoverability: 75.0
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  open_source:
    applies: true
    score: 50.0
  previous_composite: 56.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 46.1
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/screenshots/b-well-2026-08-07T162052.png
security:
- kind: authentication
  name: B Well Authentication
  slug: b-well-authentication
  summary_line: oauth2/apiKey · 7 schemes
- kind: domain-security
  name: B Well Domain Security
  slug: b-well-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: B Well Vulnerability Disclosure
  slug: b-well-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: B Well Trust Center
  slug: b-well-trust-center
  summary_line: HITRUST, NIST Cybersecurity Framework (CSF), HIPAA
slug: b-well
tags:
- Company
- Health
- Healthcare
- Digital Health
- FHIR
- Health Data
- Interoperability
- Patient Access
- Health Records
- MCP
website: https://www.icanbwell.com/
---
