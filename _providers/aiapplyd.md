---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 61.4
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 242
  human_in_the_loop: 6
  name: Aiapplyd Agentic Access
  operation_count: 372
  slug: aiapplyd-agentic-access
  summary_line: 372 operations · 242 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.aiapplyd.com/api/v1
  baseurl_source: declared
  description: 'The REST backend of the AI Applyd application (Hono + Zod), published as OpenAPI 3.0 with a Scalar reference: accounts, job matches and preferences, ATS scoring and optimization, resume builder, user '
  name: AI Applyd API
  slug: ai-applyd-api
- description: 'Hosted remote MCP server (streamable HTTP, OAuth 2.1 with dynamic client registration) exposing 10 tools: ATS resume scoring, job-description analysis, resume optimization and translation, interview q'
  name: AI Applyd MCP Server
  slug: ai-applyd-mcp-server
artifact_total: 18
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/agentic-access/aiapplyd-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aiapplyd-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/rate-limits/aiapplyd-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aiapplyd-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/plans/aiapplyd-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiapplyd-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/rules/aiapplyd-rules.yml
  title: ''
  type: Spectral
  url: rules/aiapplyd-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/json-ld/aiapplyd-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aiapplyd-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/vocabulary/aiapplyd-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aiapplyd-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/data-model/aiapplyd-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aiapplyd-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/changelog/aiapplyd-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aiapplyd-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/conventions/aiapplyd-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aiapplyd-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/conventions/aiapplyd-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aiapplyd-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/authentication/aiapplyd-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aiapplyd-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/scopes/aiapplyd-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aiapplyd-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/lifecycle/aiapplyd-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aiapplyd-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/errors/aiapplyd-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aiapplyd-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/conformance/aiapplyd-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiapplyd-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/overlays/aiapplyd-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aiapplyd-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/llms/aiapplyd-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiapplyd-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/mcp/aiapplyd-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aiapplyd-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/mcp/aiapplyd-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiapplyd-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/well-known/aiapplyd-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiapplyd-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/hosts/aiapplyd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiapplyd-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/vendors/aiapplyd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiapplyd-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/packages/aiapplyd-packages.yml
  title: ''
  type: SDKs
  url: packages/aiapplyd-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/packages/aiapplyd-packages.yml
  title: ''
  type: Packages
  url: packages/aiapplyd-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/security/aiapplyd-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aiapplyd-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiapplyd/refs/heads/main/security/aiapplyd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiapplyd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiapplyd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aiapplyd.com/mcps
- group: docs
  title: ''
  type: APIReference
  url: https://api.aiapplyd.com/api/v1/scalar
- group: commercial
  title: ''
  type: Pricing
  url: https://aiapplyd.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://aiapplyd.com/support
- group: operate
  title: ''
  type: FAQ
  url: https://aiapplyd.com/faq
- group: company
  title: ''
  type: Blog
  url: https://aiapplyd.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aiapplyd
- group: start
  title: ''
  type: SignUp
  url: https://aiapplyd.com/auth/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiapplyd.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiapplyd.com/legal/privacy
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://aiapplyd.com/legal/security
created: '2026-09-23'
description: 'AI Applyd is a job-application automation platform for candidates: it scores a resume against a posting for ATS compatibility, rewrites the resume and writes a cover letter per role, prepares interview material, matches new postings to a profile, and fills and submits applications on the employer''s own hiring system across 15 ATS platforms (Workday, Greenhouse, Lever, Ashby, Workable, iCIMS, SmartRecruiters and more), counting an application as sent only when the employer''s system confirms it. It publishes a hosted remote MCP server at mcp.aiapplyd.com/mcp (OAuth 2.1, 10 tools, listed in the official MCP Registry as com.aiapplyd/aiapplyd) with an MIT-licensed stdio bridge on GitHub, and serves the OpenAPI 3.0 description of its application backend at api.aiapplyd.com/api/v1/openapi.json.'
image: https://aiapplyd.com/static/images/logos/icon-logo-dark-square.png
json_schemas:
- name: ApplyHeartbeatBody
  property_count: 11
  slug: aiapplyd-apply-heartbeat-body
- name: AutoSetupRequest
  property_count: 23
  slug: aiapplyd-auto-setup-request
- name: PatchUserPreferences
  property_count: 3
  slug: aiapplyd-patch-user-preferences
- name: PostAiDataPermissionData
  property_count: 4
  slug: aiapplyd-post-ai-data-permission-data
- name: UpdatePreferencesRequest
  property_count: 19
  slug: aiapplyd-update-preferences-request
- name: UpsertApplicationProfile
  property_count: 34
  slug: aiapplyd-upsert-application-profile
jsonld:
- class_count: 120
  name: Aiapplyd Context
  property_count: 210
  slug: aiapplyd-context
layout: provider
mcp_servers:
- description: ''
  name: AI Applyd
  slug: ai-applyd
modified: '2026-09-23'
name: AI Applyd
nav: Providers
network: true
overview: 'AI Applyd publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Job Search, Recruiting, Resume, Applicant Tracking Systems, and Careers.


  The AI Applyd catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Applyd''s developer surface includes changelog, authentication, documentation, API reference, pricing, support, FAQ, and 31 more developer resources.'
plans:
- name: Aiapplyd Plans Pricing
  plan_count: 3
  slug: aiapplyd-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 6
  name: Aiapplyd Rate Limits
  slug: aiapplyd-rate-limits
rules:
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: AI Applyd API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: aiapplyd-rules
scopes:
- name: Aiapplyd Scopes
  scope_count: 0
  slug: aiapplyd-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 87.8
    catalog_earned_first_party: 24.0
    catalog_gap: 27.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 64.0
    developer_ergonomics: 42.9
    discoverability: 75.9
    operational_transparency: 63.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: true
    score: 72.2
security:
- kind: authentication
  name: Aiapplyd Authentication
  slug: aiapplyd-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Aiapplyd Domain Security
  slug: aiapplyd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aiapplyd Vulnerability Disclosure
  slug: aiapplyd-vulnerability-disclosure
  summary_line: disclosure policy published
slug: aiapplyd
tags:
- Job Search
- Recruiting
- Resume
- Applicant Tracking Systems
- Careers
- Artificial Intelligence
- MCP
- Automation
website: https://aiapplyd.com/
---
