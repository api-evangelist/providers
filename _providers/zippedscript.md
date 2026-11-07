---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Zippedscript Agentic Access
  operation_count: 58
  slug: zippedscript-agentic-access
  summary_line: 58 operations · 23 acting
api_count: 1
apis:
- baseURL: http://app.zippedscript.com/api/v1
  baseurl_source: declared
  description: The authentication API from ZippedScript — 2 operation(s) for authentication.
  name: ZippedScript Authentication API
  slug: zippedscript-authentication-api
- baseURL: http://app.zippedscript.com/api/v1
  baseurl_source: declared
  description: The direct API from ZippedScript — 20 operation(s) for direct.
  name: ZippedScript Direct API
  slug: zippedscript-direct-api
- baseURL: http://app.zippedscript.com/api/v1
  baseurl_source: declared
  description: The employment API from ZippedScript — 10 operation(s) for employment.
  name: ZippedScript Employment API
  slug: zippedscript-employment-api
- baseURL: http://app.zippedscript.com/api/v1
  baseurl_source: declared
  description: The institution API from ZippedScript — 3 operation(s) for institution.
  name: ZippedScript Institution API
  slug: zippedscript-institution-api
- baseURL: http://app.zippedscript.com/api/v1
  baseurl_source: declared
  description: The reference_checks API from ZippedScript — 7 operation(s) for reference_checks.
  name: ZippedScript Reference Checks API
  slug: zippedscript-reference-checks-api
- baseURL: http://app.zippedscript.com/api/v1
  baseurl_source: declared
  description: The user API from ZippedScript — 2 operation(s) for user.
  name: ZippedScript User API
  slug: zippedscript-user-api
- baseURL: http://app.zippedscript.com/api/v1
  baseurl_source: declared
  description: The verification API from ZippedScript — 5 operation(s) for verification.
  name: ZippedScript Verification API
  slug: zippedscript-verification-api
artifact_total: 40
common:
- group: design
  href: https://artifacts.apis.io/zippedscript/json-ld/zippedscript-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zippedscript-context.jsonld
- group: auth
  href: https://artifacts.apis.io/zippedscript/well-known/zippedscript-calendly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zippedscript-calendly-security.txt
- group: auth
  href: https://artifacts.apis.io/zippedscript/well-known/zippedscript-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zippedscript-api-security.txt
- group: agent
  href: https://artifacts.apis.io/zippedscript/agentic-access/zippedscript-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zippedscript-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/zippedscript/rules/zippedscript-rules.yml
  title: ''
  type: Spectral
  url: rules/zippedscript-rules.yml
- group: design
  href: https://artifacts.apis.io/zippedscript/vocabulary/zippedscript-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zippedscript-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/zippedscript/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/zippedscript/data-model/zippedscript-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zippedscript-data-model.yml
- group: auth
  href: https://artifacts.apis.io/zippedscript/authentication/zippedscript-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zippedscript-authentication.yml
- group: design
  href: https://artifacts.apis.io/zippedscript/errors/zippedscript-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zippedscript-problem-types.yml
- group: design
  href: https://artifacts.apis.io/zippedscript/conformance/zippedscript-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zippedscript-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zippedscript/mcp/zippedscript-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zippedscript-mcp.yml
- group: agent
  href: https://artifacts.apis.io/zippedscript/well-known/zippedscript-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zippedscript-well-known.yml
- group: other
  href: https://artifacts.apis.io/zippedscript/hosts/zippedscript-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zippedscript-hosts.yml
- group: other
  href: https://artifacts.apis.io/zippedscript/vendors/zippedscript-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zippedscript-vendors.yml
- group: auth
  href: https://artifacts.apis.io/zippedscript/security/zippedscript-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zippedscript-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zippedscript.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zippedscript.com/
- group: docs
  title: ''
  type: APIReference
  url: https://app.zippedscript.com/swagger/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zippedscript.com/
- group: start
  title: ''
  type: SignUp
  url: https://calendly.com/d/cv6h-dp7-sqh/zippedscript-intro
created: '2026-10-29'
description: ZippedScript provides fast, accurate education and employment verification services worldwide through a secure, automated API platform. Leveraging AI and a global database of over 20 million degrees and 70k institutions, the SaaS solution streamlines background checks for companies, delivering rapid turnaround times and comprehensive verification results. The company aims to modernize credential validation and improve hiring efficiency across industries.
image: https://verify.zippedscript.com/zp-opengraph.jpg
json_schemas:
- name: CreateEmployment
  property_count: 21
  slug: zippedscript-create-employment
- name: CreateEmploymentVerification
  property_count: 12
  slug: zippedscript-create-employment-verification
- name: CreateRedSeal
  property_count: 4
  slug: zippedscript-create-red-seal
- name: CreateReferenceCheck
  property_count: 7
  slug: zippedscript-create-reference-check
- name: CreateReferenceCheckVerification
  property_count: 6
  slug: zippedscript-create-reference-check-verification
- name: CreateVerification
  property_count: 9
  slug: zippedscript-create-verification
- name: DegreeDirectInstitution
  property_count: 6
  slug: zippedscript-degree-direct-institution
- name: EmploymentStatus
  property_count: 2
  slug: zippedscript-employment-status
- name: Login
  property_count: 3
  slug: zippedscript-login
- name: PaginatedContactSerializer
  property_count: 4
  slug: zippedscript-paginated-contact-serializer
- name: PaginatedReadEmploymentSerializer
  property_count: 4
  slug: zippedscript-paginated-read-employment-serializer
- name: PaginatedReadInstitutionSerializer
  property_count: 4
  slug: zippedscript-paginated-read-institution-serializer
- name: PaginatedReadReferenceCheckSerializer
  property_count: 4
  slug: zippedscript-paginated-read-reference-check-serializer
- name: PaginatedReadSearchSerializer
  property_count: 4
  slug: zippedscript-paginated-read-search-serializer
- name: PaginatedReadVerificationSerializer
  property_count: 4
  slug: zippedscript-paginated-read-verification-serializer
- name: ReadEmployment
  property_count: 29
  slug: zippedscript-read-employment
- name: ReadInstitution
  property_count: 9
  slug: zippedscript-read-institution
- name: ReadReferenceCheck
  property_count: 18
  slug: zippedscript-read-reference-check
- name: ReadSearch
  property_count: 13
  slug: zippedscript-read-search
- name: ReadVerification
  property_count: 15
  slug: zippedscript-read-verification
- name: ReferenceStatus
  property_count: 2
  slug: zippedscript-reference-status
- name: Status
  property_count: 2
  slug: zippedscript-status
- name: UpdateReferenceCheck
  property_count: 13
  slug: zippedscript-update-reference-check
- name: UpdateVerification
  property_count: 5
  slug: zippedscript-update-verification
jsonld:
- class_count: 33
  name: Zippedscript Context
  property_count: 127
  slug: zippedscript-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.zippedscript.com.
  name: ZippedScript MCP Server
  slug: zippedscript-mcp-yml
modified: '2026-10-29'
name: ZippedScript
nav: Providers
network: true
overview: 'ZippedScript publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Direct API, Employment API, and 4 more. Tagged areas include Company, Education, Verification, Software-as-a-Service, and Background Checks.


  The ZippedScript catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ZippedScript''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, and 16 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 0
  name: Zippedscript Rate Limits
  slug: zippedscript-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: ZippedScript API Rules
  rule_count: 56
  severity_counts:
    error: 45
    hint: 0
    info: 5
    warn: 6
  slug: zippedscript-rules
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 62.1
    developer_ergonomics: 32.6
    discoverability: 68.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Zippedscript Authentication
  slug: zippedscript-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zippedscript Domain Security
  slug: zippedscript-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: direct-ar-create
  slug: zippedscript-direct-ar-create
- name: direct-institutions-list
  slug: zippedscript-direct-institutions-list
slug: zippedscript
tags:
- Company
- Education
- Verification
- Software-as-a-Service
- Background Checks
website: https://www.zippedscript.com/
---
