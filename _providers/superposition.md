---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-10-31'
api_count: 4
apis:
- description: Authenticated API for managing jobs, candidates, pipelines, and agents.
  name: Superposition API
  slug: superposition-api
- baseURL: https://app.superposition.ai
  baseurl_source: declared
  description: 'Superposition API Reference Authenticate and integrate with the Superposition API. API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-29); n'
  name: Superposition API Reference Authenticate and integrate with the Superposition API. API
  slug: api-api
- baseURL: https://app.superposition.ai
  baseurl_source: declared
  description: 'Superposition core API as documented publicly: 31 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Superposition core API
  slug: core-api
- baseURL: https://app.superposition.ai
  baseurl_source: declared
  description: 'Superposition Guides Set up your workspace, create a role, and run your first search. API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-29)'
  name: Superposition Guides Set up your workspace, create a role, and run your first search. API
  slug: guides-api
artifact_total: 19
common:
- group: operate
  href: https://artifacts.apis.io/superposition/rate-limits/superposition-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/superposition-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/superposition/rules/superposition-rules.yml
  title: ''
  type: Spectral
  url: rules/superposition-rules.yml
- group: design
  href: https://artifacts.apis.io/superposition/json-ld/superposition-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/superposition-context.jsonld
- group: design
  href: https://artifacts.apis.io/superposition/vocabulary/superposition-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/superposition-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/superposition/data-model/superposition-data-model.yml
  title: ''
  type: DataModel
  url: data-model/superposition-data-model.yml
- group: auth
  href: https://artifacts.apis.io/superposition/security/superposition-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/superposition-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/superposition/authentication/superposition-authentication.yml
  title: ''
  type: Authentication
  url: authentication/superposition-authentication.yml
- group: auth
  href: https://artifacts.apis.io/superposition/scopes/superposition-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/superposition-scopes.yml
- group: design
  href: https://artifacts.apis.io/superposition/errors/superposition-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/superposition-problem-types.yml
- group: design
  href: https://artifacts.apis.io/superposition/conformance/superposition-conformance.yml
  title: ''
  type: Conformance
  url: conformance/superposition-conformance.yml
- group: agent
  href: https://artifacts.apis.io/superposition/llms/superposition-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/superposition-llms.txt
- group: auth
  href: https://artifacts.apis.io/superposition/well-known/superposition-superposition-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/superposition-superposition-security.txt
- group: auth
  href: https://artifacts.apis.io/superposition/well-known/superposition-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/superposition-security.txt
- group: agent
  href: https://artifacts.apis.io/superposition/well-known/superposition-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/superposition-well-known.yml
- group: other
  href: https://artifacts.apis.io/superposition/hosts/superposition-hosts.yml
  title: ''
  type: Hosts
  url: hosts/superposition-hosts.yml
- group: other
  href: https://artifacts.apis.io/superposition/vendors/superposition-vendors.yml
  title: ''
  type: Vendors
  url: vendors/superposition-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.superposition.ai/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.superposition.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.superposition.ai/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.superposition.ai/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superpositionhq
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.superposition.ai/changelog
- group: auth
  href: https://artifacts.apis.io/superposition/security/superposition-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/superposition-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/superposition/security/superposition-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/superposition-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://superposition.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.superposition.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.superposition.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.superposition.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.superposition.ai/docs/guides/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.superposition.ai/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.superposition.ai/pricing
coverage:
  checked: '2026-10-29'
  detail: Docs provide API reference but no public OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://docs.superposition.ai/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Superposition is an AI-powered recruiter that helps startup founders find and hire top talent. The platform leverages AI agents to autonomously source, evaluate, and engage candidates, enabling founders to focus on building their product and team. It positions itself as an AI headhunter for founding teams, sourcing rare startup talent and streamlining the hiring process.
image: https://superposition.ai/images/logo.png
json_schemas:
- name: GetApiV1ScopesResponse
  property_count: 1
  slug: superposition-get-api-v1-scopes-response
- name: GetSchedulingStringStringAvailabilityResponse
  property_count: 1
  slug: superposition-get-scheduling-string-string-availability-response
- name: GetV1JobsResponse
  property_count: 1
  slug: superposition-get-v1-jobs-response
- name: PatchApiV1AtsJobLinksLinkidRequest
  property_count: 2
  slug: superposition-patch-api-v1-ats-job-links-linkid-request
- name: PatchAtsConnectionsStringResponse
  property_count: 1
  slug: superposition-patch-ats-connections-string-response
- name: PostApiV1AgentInvokeResponse
  property_count: 4
  slug: superposition-post-api-v1-agent-invoke-response
- name: PostApiV1CandidatesCandidateidAtsPushRequest
  property_count: 1
  slug: superposition-post-api-v1-candidates-candidateid-ats-push-request
- name: PostSchedulingStringStringBookingsRequest
  property_count: 2
  slug: superposition-post-scheduling-string-string-bookings-request
jsonld:
- class_count: 10
  name: Superposition Context
  property_count: 13
  slug: superposition-context
layout: provider
modified: '2026-10-29'
name: Superposition
nav: Providers
network: true
overview: 'Superposition is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including API Reference Authenticate and integrate with the Superposition API. API, core API, Guides Set up your workspace, create a role, and run your first search. API, and 1 more. Tagged areas include Company, AI, Recruiting, Startup, and Talent.


  The Superposition catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Superposition''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 24 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 2
  name: Superposition Rate Limits
  slug: superposition-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Superposition API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: superposition-rules
scopes:
- name: Superposition Scopes
  scope_count: 0
  slug: superposition-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 25.8
    developer_ergonomics: 52.4
    discoverability: 71.4
    operational_transparency: 68.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Superposition Authentication
  slug: superposition-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Superposition Domain Security
  slug: superposition-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Superposition Vulnerability Disclosure
  slug: superposition-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: superposition
tags:
- Company
- AI
- Recruiting
- Startup
- Talent
- Hiring
website: https://superposition.ai
---
