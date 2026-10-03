---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.7
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 21
  human_in_the_loop: 2
  name: Arcadiapower2 Agentic Access
  operation_count: 42
  slug: arcadiapower2-agentic-access
  summary_line: 42 operations · 21 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.arcadia.com
  baseurl_source: declared
  description: The Auth API from Arcadiapower2 — 4 operation(s) for auth.
  name: Arcadiapower2 Auth API
  slug: arcadiapower2-auth-api
- baseURL: https://api.arcadia.com
  baseurl_source: declared
  description: The Bundle (Beta) API from Arcadiapower2 — 8 operation(s) for bundle (beta).
  name: Arcadiapower2 Bundle (Beta) API
  slug: arcadiapower2-bundle-beta-api
- baseURL: https://api.arcadia.com
  baseurl_source: declared
  description: The Bundle Webhook Events API from Arcadiapower2 — 0 operation(s) for bundle webhook events.
  name: Arcadiapower2 Bundle Webhook Events API
  slug: arcadiapower2-bundle-webhook-events-api
- baseURL: https://api.arcadia.com
  baseurl_source: declared
  description: The Plug API from Arcadiapower2 — 2 operation(s) for plug.
  name: Arcadiapower2 Plug API
  slug: arcadiapower2-plug-api
- baseURL: https://api.arcadia.com
  baseurl_source: declared
  description: The Spark API from Arcadiapower2 — 8 operation(s) for spark.
  name: Arcadiapower2 Spark API
  slug: arcadiapower2-spark-api
- baseURL: https://api.arcadia.com
  baseurl_source: declared
  description: The Users API from Arcadiapower2 — 2 operation(s) for users.
  name: Arcadiapower2 Users API
  slug: arcadiapower2-users-api
- baseURL: https://api.arcadia.com
  baseurl_source: declared
  description: The Utility Accounts API from Arcadiapower2 — 2 operation(s) for utility accounts.
  name: Arcadiapower2 Utility Accounts API
  slug: arcadiapower2-utility-accounts-api
- baseURL: https://api.arcadia.com
  baseurl_source: declared
  description: The Utility Credentials API from Arcadiapower2 — 3 operation(s) for utility credentials.
  name: Arcadiapower2 Utility Credentials API
  slug: arcadiapower2-utility-credentials-api
- baseURL: https://api.arcadia.com
  baseurl_source: declared
  description: The Utility Meters (Beta) API from Arcadiapower2 — 2 operation(s) for utility meters (beta).
  name: Arcadiapower2 Utility Meters (Beta) API
  slug: arcadiapower2-utility-meters-beta-api
- baseURL: https://api.arcadia.com
  baseurl_source: declared
  description: The Webhook Events API from Arcadiapower2 — 0 operation(s) for webhook events.
  name: Arcadiapower2 Webhook Events API
  slug: arcadiapower2-webhook-events-api
- baseURL: https://api.arcadia.com
  baseurl_source: declared
  description: The Webhooks API from Arcadiapower2 — 7 operation(s) for webhooks.
  name: Arcadiapower2 Webhooks API
  slug: arcadiapower2-webhooks-api
artifact_total: 26
asyncapis:
- description: ''
  name: Arcadiapower2 Webhooks
  slug: arcadiapower2-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/vendors/arcadiapower2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcadiapower2-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/agentic-access/arcadiapower2-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arcadiapower2-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/rate-limits/arcadiapower2-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/arcadiapower2-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/rules/arcadiapower2-rules.yml
  title: ''
  type: Spectral
  url: rules/arcadiapower2-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/json-ld/arcadiapower2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arcadiapower2-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/vocabulary/arcadiapower2-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arcadiapower2-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/asyncapi/arcadiapower2-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/arcadiapower2-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/data-model/arcadiapower2-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arcadiapower2-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/changelog/arcadiapower2-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/arcadiapower2-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/conventions/arcadiapower2-conventions.yml
  title: ''
  type: Conventions
  url: conventions/arcadiapower2-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/sandbox/arcadiapower2-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/arcadiapower2-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.arcadia.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/authentication/arcadiapower2-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arcadiapower2-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/errors/arcadiapower2-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arcadiapower2-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/conformance/arcadiapower2-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arcadiapower2-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/llms/arcadiapower2-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcadiapower2-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/well-known/arcadiapower2-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arcadiapower2-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/hosts/arcadiapower2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcadiapower2-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://www.arcadia.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.arcadia.com/press
- group: start
  title: ''
  type: Login
  url: https://www.arcadia.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.arcadia.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arcadia.com/docs/dashboard-quick-start-guide
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/security/arcadiapower2-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/arcadiapower2-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/security/arcadiapower2-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arcadiapower2-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcadiapower2/refs/heads/main/security/arcadiapower2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcadiapower2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arcadia.com
created: '2026-09-25'
description: Arcadiapower2, operating under the brand Arcadia, provides an energy intelligence platform that unifies utility data, AI‑driven analytics, and advisory services to help enterprises manage energy costs, mitigate risk, and achieve sustainability goals. The platform offers tools for utility bill payment, procurement, carbon management, and detailed reporting, serving thousands of customers across the United States and supporting a significant portion of Fortune 500 enterprises.
image: https://images.prismic.io/arcadia-marketing-site-2023/82c6fcdf-2cdf-4557-bfd0-725b02c020ad_Arcadia-Global-Meta.png?auto=compress,format
json_schemas:
- name: StorageOptimizationSchedulesRequestParams
  property_count: 22
  slug: arcadiapower2-storage-optimization-schedules-request-params
- name: StorageOptimizationSchedulesResponse
  property_count: 11
  slug: arcadiapower2-storage-optimization-schedules-response
- name: TariffApplicabilityQuestionsResponse
  property_count: 4
  slug: arcadiapower2-tariff-applicability-questions-response
- name: TariffScenarioCostRequestParams
  property_count: 6
  slug: arcadiapower2-tariff-scenario-cost-request-params
- name: UtilityAccount
  property_count: 22
  slug: arcadiapower2-utility-account
- name: UtilityStatement
  property_count: 26
  slug: arcadiapower2-utility-statement
jsonld:
- class_count: 109
  name: Arcadiapower2 Context
  property_count: 177
  slug: arcadiapower2-context
layout: provider
modified: '2026-09-25'
name: Arcadiapower2
nav: Providers
network: true
overview: 'Arcadiapower2 publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Bundle (Beta) API, Bundle Webhook Events API, and 8 more. Tagged areas include Energy, Software-as-a-Service, Enterprise, Sustainability, and Data.


  The Arcadiapower2 catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Arcadiapower2''s developer surface includes changelog, sandbox, authentication, engineering blog, getting-started guide, documentation, and 23 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 4
  name: Arcadiapower2 Rate Limits
  slug: arcadiapower2-rate-limits
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Arcadiapower2 API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: arcadiapower2-rules
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 68.7
    developer_ergonomics: 44.6
    discoverability: 75.0
    operational_transparency: 65.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Arcadiapower2 Authentication
  slug: arcadiapower2-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Arcadiapower2 Domain Security
  slug: arcadiapower2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arcadiapower2 Vulnerability Disclosure
  slug: arcadiapower2-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Arcadiapower2 Trust Center
  slug: arcadiapower2-trust-center
  summary_line: SOC 2, ISO 27001
slug: arcadiapower2
tags:
- Energy
- Software-as-a-Service
- Enterprise
- Sustainability
- Data
website: https://www.arcadia.com
---
