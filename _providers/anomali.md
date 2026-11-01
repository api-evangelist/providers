---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-10-31'
api_count: 3
apis:
- description: REST API for the Anomali ThreatStream Threat Intelligence Platform — manage threat intelligence, observables, investigations, imports, and integrations. Authentication uses an apikey credential in the
  name: Anomali ThreatStream API
  slug: anomali-threatstream-api
- description: Remote Model Context Protocol server for ThreatStream at https://api.threatstream.com/mcp. Its OAuth protected-resource metadata (/.well-known/oauth-protected-resource) names the resource "ThreatStrea
  name: Anomali ThreatStream MCP Server
  slug: anomali-threatstream-mcp-server
- baseURL: https://api.threatstream.com
  baseurl_source: declared
  description: 'Anomali API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Anomali API
  slug: anomali-api
artifact_total: 14
common:
- group: operate
  href: https://artifacts.apis.io/anomali/lifecycle/anomali-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/anomali-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/anomali/rate-limits/anomali-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anomali-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/anomali/rules/anomali-rules.yml
  title: ''
  type: Spectral
  url: rules/anomali-rules.yml
- group: design
  href: https://artifacts.apis.io/anomali/json-ld/anomali-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anomali-context.jsonld
- group: design
  href: https://artifacts.apis.io/anomali/vocabulary/anomali-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anomali-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/anomali/data-model/anomali-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anomali-data-model.yml
- group: design
  href: https://artifacts.apis.io/anomali/conventions/anomali-conventions.yml
  title: ''
  type: Conventions
  url: conventions/anomali-conventions.yml
- group: auth
  href: https://artifacts.apis.io/anomali/authentication/anomali-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anomali-authentication.yml
- group: auth
  href: https://artifacts.apis.io/anomali/scopes/anomali-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/anomali-scopes.yml
- group: design
  href: https://artifacts.apis.io/anomali/conformance/anomali-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anomali-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anomali/llms/anomali-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anomali-llms.txt
- group: auth
  href: https://artifacts.apis.io/anomali/well-known/anomali-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anomali-status-security.txt
- group: agent
  href: https://artifacts.apis.io/anomali/well-known/anomali-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anomali-well-known.yml
- group: other
  href: https://artifacts.apis.io/anomali/hosts/anomali-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anomali-hosts.yml
- group: build
  href: https://artifacts.apis.io/anomali/integrations/anomali-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/anomali-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/anomali/vendors/anomali-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anomali-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.anomali.com/marketplace/sdks
- group: other
  title: ''
  type: Leadership
  url: https://www.anomali.com/company/leadership
- group: company
  title: ''
  type: Website
  url: https://www.anomali.com
- group: company
  title: ''
  type: Blog
  url: https://www.anomali.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.anomali.com/customer-success
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anomali
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anomali.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anomali.com/privacy-policy
- group: other
  title: ''
  type: Marketplace
  url: https://www.anomali.com/marketplace
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anomali.com/Content/Introduction/welcome_Anomali.htm
- group: docs
  title: ''
  type: APIReference
  url: https://docs.anomali.com/Content/ThreatStream%20API/supported_endpoints.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anomali.com/Content/ThreatStream%20API/introduction_api.htm
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.anomali.com/Content/TS_Release_Notes.htm
- group: auth
  title: ''
  type: Security
  url: https://www.anomali.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.anomali.com/press-room/news
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anomali.com
- group: auth
  title: ''
  type: Security
  url: https://www.anomali.com/security
- group: design
  href: https://artifacts.apis.io/anomali/lifecycle/anomali-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/anomali-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/anomali/security/anomali-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anomali-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/anomali/security/anomali-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anomali-domain-security.yml
created: '2026-07-17'
description: Anomali is an enterprise cybersecurity vendor whose Agentic SOC Platform unifies threat intelligence, security data, and agentic AI. Its flagship ThreatStream is a leading Threat Intelligence Platform (TIP) that operationalizes indicators of compromise across a Unified Security Data Lake with SIEM, SOAR, and XDR capabilities. Anomali exposes a ThreatStream REST API (api.threatstream.com) for managing intelligence, observables, investigations, and integrations, and maintains a partner marketplace of prebuilt integrations. This API Evangelist profile was seeded from the general-catalyst portfolio and enriched from Anomali's public surfaces (status page, security/responsible-disclosure program, privacy and terms pages, GitHub organization, and blog).
image: https://cdn.prod.website-files.com/6453db2ad32b573c40a15c49/6627ff6e7f8cb72de4b695f6_Anomali-OpenGraph-2024.webp
json_schemas:
- name: GetApiApiversionResponse
  property_count: 3
  slug: anomali-get-api-apiversion-response
- name: GetApiV2IntelligenceResponse
  property_count: 3
  slug: anomali-get-api-v2-intelligence-response
- name: PostOauthTokenResponse
  property_count: 3
  slug: anomali-post-oauth-token-response
jsonld:
- class_count: 3
  name: Anomali Context
  property_count: 3
  slug: anomali-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.threatstream.com requiring an API key.
  name: ThreatStream MCP Server
  slug: threatstream-mcp-server
modified: '2026-10-20'
name: Anomali
nav: Providers
network: true
overview: 'Anomali is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Cybersecurity, Threat Intelligence, and Security.


  The Anomali catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Anomali''s developer surface includes authentication, engineering blog, support, documentation, API reference, getting-started guide, changelog, and 29 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 6
  name: Anomali Rate Limits
  slug: anomali-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Anomali API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: anomali-rules
scopes:
- name: Anomali Scopes
  scope_count: 6
  slug: anomali-scopes
  summary_line: 6 scopes
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 71.0
    catalog_earned_first_party: 12.0
    catalog_gap: 44.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 19.7
    contract_quality: 21.0
    developer_ergonomics: 54.8
    discoverability: 73.3
    operational_transparency: 86.8
  previous_composite: 45.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/anomali/anomali-2026-07-25T200450.png
security:
- kind: authentication
  name: Anomali Authentication
  slug: anomali-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Anomali Domain Security
  slug: anomali-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anomali Vulnerability Disclosure
  slug: anomali-vulnerability-disclosure
  summary_line: contact published
slug: anomali
tags:
- Company
- Enterprise
- Cybersecurity
- Threat Intelligence
- Security
- SIEM
- SOAR
- XDR
- Threat Intelligence Platform
website: https://www.anomali.com
---
