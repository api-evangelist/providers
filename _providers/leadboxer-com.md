---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Leadboxer Com Agentic Access
  operation_count: 42
  slug: leadboxer-com-agentic-access
  summary_line: 42 operations · 23 acting
api_count: 3
apis:
- baseURL: https://api.leadboxer.com
  baseurl_source: declared
  description: The Credit Management API from leadboxer-com — 1 operation(s) for credit management.
  name: leadboxer-com Credit Management API
  slug: leadboxer-com-credit-management-api
- baseURL: https://api.leadboxer.com
  baseurl_source: declared
  description: The Custom Tracking Domains API from leadboxer-com — 4 operation(s) for custom tracking domains.
  name: leadboxer-com Custom Tracking Domains API
  slug: leadboxer-com-custom-tracking-domains-api
- baseURL: https://api.leadboxer.com
  baseurl_source: declared
  description: Manage your datasets. Add, update, delete datasets from your account, configure preferences, and manage form tracking.
  name: leadboxer-com Dataset Management API
  slug: leadboxer-com-dataset-management-api
- baseURL: https://api.leadboxer.com
  baseurl_source: declared
  description: Manage your Lead.
  name: leadboxer-com Lead Operation API
  slug: leadboxer-com-leadoperation-api
- baseURL: https://api.leadboxer.com
  baseurl_source: declared
  description: Get your top leads with fine grained filtering criteria.
  name: leadboxer-com Leads API
  slug: leadboxer-com-leads-api
- baseURL: https://track.leadboxer.com
  baseurl_source: declared
  description: The Log API from leadboxer-com — 1 operation(s) for log.
  name: leadboxer-com Log API
  slug: leadboxer-com-log-api
- baseURL: https://api.leadboxer.com
  baseurl_source: declared
  description: APIs for IP, Domain and Email lookup operations
  name: leadboxer-com Lookup API
  slug: leadboxer-com-lookup-api-api
- baseURL: https://api.leadboxer.com
  baseurl_source: declared
  description: 'Defines and manages which segment is set as default for a given combination of User ID and Dataset ID. A user can have multiple segments under a dataset, but only one of them can be designated as the '
  name: leadboxer-com Segment Preference API
  slug: leadboxer-com-segment-preference-api
- baseURL: https://api.leadboxer.com
  baseurl_source: declared
  description: Manage your segments. Add, update, delete segments for your datasets etc.
  name: leadboxer-com Segments API
  slug: leadboxer-com-segments-api
- baseURL: https://log.leadboxer.com
  baseurl_source: declared
  description: The Track API API from leadboxer-com — 1 operation(s) for track api.
  name: leadboxer-com Track API
  slug: leadboxer-com-track-api-api
- baseURL: https://api.leadboxer.com
  baseurl_source: declared
  description: API endpoints for managing users within an account. These operations allow you to create users, update their basic information, manage invitations, retrieve their accessible datasets, and remove users
  name: leadboxer-com User Management API
  slug: leadboxer-com-user-management-api
- baseURL: https://api.leadboxer.com
  baseurl_source: declared
  description: Manage access to your datasets. Associate/dissociate datasets with users etc.
  name: leadboxer-com User Datasets API
  slug: leadboxer-com-userdatasets-api
artifact_total: 29
common:
- group: agent
  href: https://artifacts.apis.io/leadboxer-com/agentic-access/leadboxer-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/leadboxer-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/leadboxer-com/rate-limits/leadboxer-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/leadboxer-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/leadboxer-com/plans/leadboxer-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leadboxer-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/leadboxer-com/rules/leadboxer-com-rules.yml
  title: ''
  type: Spectral
  url: rules/leadboxer-com-rules.yml
- group: design
  href: https://artifacts.apis.io/leadboxer-com/json-ld/leadboxer-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/leadboxer-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/leadboxer-com/vocabulary/leadboxer-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/leadboxer-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/leadboxer-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/leadboxer-com/data-model/leadboxer-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leadboxer-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/leadboxer-com/changelog/leadboxer-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/leadboxer-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/leadboxer-com/authentication/leadboxer-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leadboxer-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/leadboxer-com/errors/leadboxer-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leadboxer-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/leadboxer-com/conformance/leadboxer-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leadboxer-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/leadboxer-com/llms/leadboxer-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leadboxer-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/leadboxer-com/mcp/leadboxer-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/leadboxer-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/leadboxer-com/well-known/leadboxer-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leadboxer-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/leadboxer-com/hosts/leadboxer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/leadboxer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/leadboxer-com/vendors/leadboxer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/leadboxer-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.leadboxer.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leadboxer
- group: auth
  href: https://artifacts.apis.io/leadboxer-com/security/leadboxer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leadboxer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://leadboxer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.leadboxer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.leadboxer.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.leadboxer.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.leadboxer.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.leadboxer.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.leadboxer.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.leadboxer.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leadboxer.com/resources/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leadboxer.com/resources/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.leadboxer.com/sign-up
created: '2026-10-30'
description: LeadBoxer provides a B2B signals platform that captures website and email activity to identify and enrich company profiles. Its API offers IP, email, website tracking, server‑side events, and data enrichment endpoints, enabling SaaS builders, RevOps teams, and agencies to integrate real‑time lead intelligence into their workflows.
image: https://framerusercontent.com/images/MiIImBTHBqtHCrelllmZDJyxvrk.png
json_schemas:
- name: ContactProfileDetails
  property_count: 9
  slug: leadboxer-com-contact-profile-details
- name: CreateSegmentRequest
  property_count: 28
  slug: leadboxer-com-create-segment-request
- name: CustomTrackingDomainValidationResponse
  property_count: 4
  slug: leadboxer-com-custom-tracking-domain-validation-response
- name: DomainOrganizationDetails
  property_count: 17
  slug: leadboxer-com-domain-organization-details
- name: IpLookupDetails
  property_count: 15
  slug: leadboxer-com-ip-lookup-details
- name: UpdateSegmentRequest
  property_count: 26
  slug: leadboxer-com-update-segment-request
jsonld:
- class_count: 51
  name: Leadboxer Com Context
  property_count: 146
  slug: leadboxer-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at developers.leadboxer.com.
  name: leadboxer-com MCP Server
  slug: leadboxer-com-mcp-yml
modified: '2026-10-30'
name: leadboxer-com
nav: Providers
network: true
overview: 'leadboxer-com publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Credit Management API, Custom Tracking Domains API, Dataset Management API, and 9 more. Tagged areas include B2B, LeadEnrichment, Marketing, Data, and API.


  The leadboxer-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  leadboxer-com''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 24 more developer resources.'
plans:
- name: Leadboxer Com Plans Pricing
  plan_count: 4
  slug: leadboxer-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 30
  name: Leadboxer Com Rate Limits
  slug: leadboxer-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: leadboxer-com API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 10
  slug: leadboxer-com-rules
score:
  band: exemplar
  composite: 66.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 102.3
    catalog_earned_first_party: 0.0
    catalog_gap: 12.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 60.5
    developer_ergonomics: 63.6
    discoverability: 70.0
    operational_transparency: 49.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Leadboxer Com Authentication
  slug: leadboxer-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Leadboxer Com Domain Security
  slug: leadboxer-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: get-dataset-exclusions
  slug: leadboxer-com-get-dataset-exclusions
- name: lookup-email
  slug: leadboxer-com-lookup-email
- name: save-dataset-exclusion
  slug: leadboxer-com-save-dataset-exclusion
slug: leadboxer-com
tags:
- B2B
- LeadEnrichment
- Marketing
- Data
- API
website: https://leadboxer.com/
---
