---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Tracetail Io Agentic Access
  operation_count: 8
  slug: tracetail-io-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://tracetail.io
  baseurl_source: declared
  description: What the browser SDK calls.
  name: tracetail-io Identification API
  slug: tracetail-io-identification-api
- baseURL: https://tracetail.io
  baseurl_source: declared
  description: What a customer's backend calls to verify identifications, with a secret server key.
  name: tracetail-io Server API
  slug: tracetail-io-server-api-api
- baseURL: https://tracetail.io
  baseurl_source: declared
  description: Health and first-party proxy checks.
  name: tracetail-io Service API
  slug: tracetail-io-service-api
- baseURL: https://tracetail.io
  baseurl_source: declared
  description: 'How an AI agent gets API keys for the person it works for: a link they open to sign in and add a card or continue without a card.'
  name: tracetail-io Setup links API
  slug: tracetail-io-setup-links-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/tracetail-io/agentic-access/tracetail-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tracetail-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/tracetail-io/rate-limits/tracetail-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tracetail-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tracetail-io/plans/tracetail-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tracetail-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tracetail-io/rules/tracetail-io-rules.yml
  title: ''
  type: Spectral
  url: rules/tracetail-io-rules.yml
- group: design
  href: https://artifacts.apis.io/tracetail-io/json-ld/tracetail-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tracetail-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/tracetail-io/vocabulary/tracetail-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tracetail-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tracetail-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tracetail-io/data-model/tracetail-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tracetail-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/tracetail-io/conventions/tracetail-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tracetail-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/tracetail-io/conventions/tracetail-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tracetail-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/tracetail-io/security/tracetail-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tracetail-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tracetail-io/authentication/tracetail-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tracetail-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/tracetail-io/errors/tracetail-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tracetail-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tracetail-io/conformance/tracetail-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tracetail-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tracetail-io/llms/tracetail-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tracetail-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/tracetail-io/mcp/tracetail-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tracetail-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/tracetail-io/well-known/tracetail-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tracetail-io-security.txt
- group: agent
  href: https://artifacts.apis.io/tracetail-io/well-known/tracetail-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tracetail-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/tracetail-io/hosts/tracetail-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tracetail-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/tracetail-io/vendors/tracetail-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tracetail-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/tracetail-io/packages/tracetail-io-packages.yml
  title: ''
  type: SDKs
  url: packages/tracetail-io-packages.yml
- group: build
  href: https://artifacts.apis.io/tracetail-io/packages/tracetail-io-packages.yml
  title: ''
  type: Packages
  url: packages/tracetail-io-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://tracetail.io/status
- group: auth
  href: https://artifacts.apis.io/tracetail-io/security/tracetail-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tracetail-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tracetail-io/security/tracetail-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tracetail-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tracetail.io/
- group: docs
  title: ''
  type: Documentation
  url: https://tracetail.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://tracetail.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://tracetail.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tracetail.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tracetail.io/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://tracetail.io/auth
created: '2026-10-31'
description: TraceTail provides a browser fingerprinting API that identifies returning visitors without cookies or local storage. It turns over 40 browser signals into a stable visitor ID that remains consistent across normal and incognito windows. The service offers 1,000 free requests each month, enabling developers to recognize users reliably while respecting privacy.
image: https://tracetail.io/favicon.svg
json_schemas:
- name: DetailedIdentification
  property_count: 8
  slug: tracetail-io-detailed-identification
- name: IdentificationRequest
  property_count: 4
  slug: tracetail-io-identification-request
- name: Identification
  property_count: 6
  slug: tracetail-io-identification
- name: ServerIdentification
  property_count: 14
  slug: tracetail-io-server-identification
- name: SetupLink
  property_count: 9
  slug: tracetail-io-setup-link
- name: Visitor
  property_count: 9
  slug: tracetail-io-visitor
jsonld:
- class_count: 8
  name: Tracetail Io Context
  property_count: 35
  slug: tracetail-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at tracetail.io.
  name: tracetail-io MCP Server
  slug: tracetail-io-mcp-yml
modified: '2026-10-31'
name: tracetail-io
nav: Providers
network: true
overview: 'tracetail-io publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Identification API, Server API, Service API, and 1 more. Tagged areas include Browser Fingerprinting, Privacy, Analytics, and Device Identification.


  The tracetail-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tracetail-io''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, and 27 more developer resources.'
plans:
- name: Tracetail Io Plans Pricing
  plan_count: 2
  slug: tracetail-io-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Tracetail Io Rate Limits
  slug: tracetail-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: tracetail-io API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 1
  slug: tracetail-io-rules
scopes:
- name: Tracetail Io Scopes
  scope_count: 0
  slug: tracetail-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 73.8
    catalog_earned_first_party: 16.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 65.8
    developer_ergonomics: 31.4
    discoverability: 56.7
    operational_transparency: 39.5
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tracetail-io/tracetail-io-2026-11-03T144943.png
security:
- kind: authentication
  name: Tracetail Io Authentication
  slug: tracetail-io-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Tracetail Io Domain Security
  slug: tracetail-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tracetail Io Vulnerability Disclosure
  slug: tracetail-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: tracetail-io-identify
  slug: tracetail-io-identify-skill
slug: tracetail-io
tags:
- Browser Fingerprinting
- Privacy
- Analytics
- Device Identification
website: https://tracetail.io/
---
