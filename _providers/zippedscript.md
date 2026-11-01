---
agent_readiness:
  band: agent-ready
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.2
  scored_at: '2026-10-31'
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
artifact_total: 15
common:
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
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zippedscript.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://calendly.com/d/cv6h-dp7-sqh/zippedscript-intro
created: '2026-10-29'
description: ZippedScript provides fast, accurate education and employment verification services worldwide through a secure, automated API platform. Leveraging AI and a global database of over 20 million degrees and 70k institutions, the SaaS solution streamlines background checks for companies, delivering rapid turnaround times and comprehensive verification results. The company aims to modernize credential validation and improve hiring efficiency across industries.
image: https://verify.zippedscript.com/zp-opengraph.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at app.zippedscript.com.
  name: ZippedScript MCP Server
  slug: zippedscript-mcp-yml
modified: '2026-10-29'
name: ZippedScript
nav: Providers
network: true
overview: 'ZippedScript publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Direct API, Employment API, and 4 more. Tagged areas include Company, Education, Verification, SaaS, and Background-Check.


  The ZippedScript catalog on APIs.io includes 1 Spectral governance ruleset.


  ZippedScript''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, and 16 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 0
  name: Zippedscript Rate Limits
  slug: zippedscript-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ZippedScript API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 2
  slug: zippedscript-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 46.9
    discoverability: 65.0
    operational_transparency: 10.5
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
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- SaaS
- Background-Check
website: https://www.zippedscript.com/
---
