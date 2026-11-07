---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Algeriacertify Com Agentic Access
  operation_count: 9
  slug: algeriacertify-com-agentic-access
  summary_line: 9 operations · 3 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://algeriacertify.com/api/v1
  baseurl_source: declared
  description: Issue, list, and revoke certificates
  name: Algeria Certify Certificates API
  slug: algeriacertify-com-certificates-api
- baseURL: https://algeriacertify.com/api/v1
  baseurl_source: declared
  description: Health check and system status
  name: Algeria Certify System API
  slug: algeriacertify-com-system-api
- baseURL: https://algeriacertify.com/api/v1
  baseurl_source: declared
  description: Public certificate verification
  name: Algeria Certify Verification API
  slug: algeriacertify-com-verification-api
- baseURL: https://algeriacertify.com/api/v1
  baseurl_source: declared
  description: Zapier-specific endpoints (auth test, triggers, actions)
  name: Algeria Certify Zapier API
  slug: algeriacertify-com-zapier-api
artifact_total: 19
common:
- group: auth
  title: ''
  type: Security
  url: https://www.tkawen.com/security
- group: other
  href: https://artifacts.apis.io/algeriacertify-com/a2a/algeriacertify-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/algeriacertify-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/algeriacertify-com/agentic-access/algeriacertify-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/algeriacertify-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/algeriacertify-com/rate-limits/algeriacertify-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/algeriacertify-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/algeriacertify-com/rules/algeriacertify-com-rules.yml
  title: ''
  type: Spectral
  url: rules/algeriacertify-com-rules.yml
- group: design
  href: https://artifacts.apis.io/algeriacertify-com/json-ld/algeriacertify-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/algeriacertify-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/algeriacertify-com/vocabulary/algeriacertify-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/algeriacertify-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/algeriacertify-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/algeriacertify-com/data-model/algeriacertify-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/algeriacertify-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/algeriacertify-com/authentication/algeriacertify-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/algeriacertify-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/algeriacertify-com/errors/algeriacertify-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/algeriacertify-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/algeriacertify-com/conformance/algeriacertify-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/algeriacertify-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/algeriacertify-com/llms/algeriacertify-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algeriacertify-com-llms.txt
- group: build
  href: https://artifacts.apis.io/algeriacertify-com/mcp/algeriacertify-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/algeriacertify-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/algeriacertify-com/mcp/algeriacertify-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/algeriacertify-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/algeriacertify-com/well-known/algeriacertify-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/algeriacertify-com-www-security.txt
- group: auth
  href: https://artifacts.apis.io/algeriacertify-com/well-known/algeriacertify-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/algeriacertify-com-security.txt
- group: agent
  href: https://artifacts.apis.io/algeriacertify-com/well-known/algeriacertify-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/algeriacertify-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/algeriacertify-com/hosts/algeriacertify-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/algeriacertify-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/algeriacertify-com/vendors/algeriacertify-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/algeriacertify-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://algeriacertify.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tkawen
- group: auth
  href: https://artifacts.apis.io/algeriacertify-com/security/algeriacertify-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/algeriacertify-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/algeriacertify-com/security/algeriacertify-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algeriacertify-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://algeriacertify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://algeriacertify.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://algeriacertify.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://algeriacertify.com/developers
- group: operate
  title: ''
  type: Support
  url: https://algeriacertify.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://algeriacertify.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://algeriacertify.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://algeriacertify.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://algeriacertify.com/privacy
created: '2026-11-01'
description: Algeria Certify is a platform that issues, manages, and instantly verifies academic and professional digital certificates using enterprise‑grade security standards. It offers QR‑based verification, API integration for institutions, and a developer portal for building certificate‑verification workflows.
image: https://algeriacertify.com/images/social-share.jpg
json_schemas:
- name: AuthUser
  property_count: 5
  slug: algeriacertify-com-auth-user
- name: Certificate
  property_count: 10
  slug: algeriacertify-com-certificate
- name: IssueCertificateRequest
  property_count: 5
  slug: algeriacertify-com-issue-certificate-request
jsonld:
- class_count: 4
  name: Algeriacertify Com Context
  property_count: 20
  slug: algeriacertify-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at algeriacertify.com.
  name: Algeria Certify MCP Server
  slug: algeriacertify-com-mcp-yml
modified: '2026-11-01'
name: Algeria Certify
nav: Providers
network: true
overview: 'Algeria Certify publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Certificates API, System API, Verification API, and 1 more. Tagged areas include Certificate Management, Digital Verification, Education, Algeria, and Security.


  The Algeria Certify catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Algeria Certify''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, engineering blog, and 26 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 1
  name: Algeriacertify Com Rate Limits
  slug: algeriacertify-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Algeria Certify API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: algeriacertify-com-rules
scopes:
- name: Algeriacertify Com Scopes
  scope_count: 0
  slug: algeriacertify-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 67.8
    catalog_earned_first_party: 8.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 64.2
    developer_ergonomics: 36.2
    discoverability: 65.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - algeria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
    - mena
    - north-africa
  previous_composite: 53.0
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
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Algeriacertify Com Authentication
  slug: algeriacertify-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Algeriacertify Com Domain Security
  slug: algeriacertify-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Algeriacertify Com Vulnerability Disclosure
  slug: algeriacertify-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: issue-certificate
  slug: algeriacertify-com-issue-certificate-skill
- name: list-issued-certificates
  slug: algeriacertify-com-list-issued-certificates-skill
- name: verify-certificate
  slug: algeriacertify-com-verify-certificate-skill
slug: algeriacertify-com
tags:
- Certificate Management
- Digital Verification
- Education
- Algeria
- Security
website: https://algeriacertify.com/
---
