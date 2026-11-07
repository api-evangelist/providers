---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: LawToolBox MCP provides AI‑enhanced integration for Microsoft 365, but the API contract is gated behind authentication.
  name: LawToolBox MCP
  slug: lawtoolbox-mcp
- description: 'LawToolBox API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: LawToolBox API
  slug: lawtoolbox-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/lawtoolbox/rules/lawtoolbox-rules.yml
  title: ''
  type: Spectral
  url: rules/lawtoolbox-rules.yml
- group: design
  href: https://artifacts.apis.io/lawtoolbox/json-ld/lawtoolbox-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lawtoolbox-context.jsonld
- group: design
  href: https://artifacts.apis.io/lawtoolbox/vocabulary/lawtoolbox-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lawtoolbox-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/lawtoolbox/data-model/lawtoolbox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lawtoolbox-data-model.yml
- group: design
  href: https://artifacts.apis.io/lawtoolbox/conformance/lawtoolbox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lawtoolbox-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lawtoolbox/mcp/lawtoolbox-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lawtoolbox-mcp.yml
- group: other
  href: https://artifacts.apis.io/lawtoolbox/hosts/lawtoolbox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lawtoolbox-hosts.yml
- group: other
  href: https://artifacts.apis.io/lawtoolbox/vendors/lawtoolbox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lawtoolbox-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lawtoolbox.com
- group: company
  title: ''
  type: Newsroom
  url: https://lawtoolbox.com/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LawToolBox
- group: auth
  href: https://artifacts.apis.io/lawtoolbox/security/lawtoolbox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lawtoolbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lawtoolbox.com/
- group: operate
  title: ''
  type: Support
  url: https://lawtoolbox.com/support
- group: company
  title: ''
  type: Blog
  url: https://lawtoolbox.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://lawtoolbox.com/pricing/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://lawtoolbox.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lawtoolbox.com/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://lawtoolbox.com/signup
- group: operate
  title: ''
  type: HelpCenter
  url: https://lawtoolbox.com/faqs
coverage:
  checked: '2026-10-28'
  detail: The MCP endpoint at https://support.lawtoolbox.com/mcp returns 401 Unauthorized, indicating the API is gated behind authentication.
  evidence:
  - status: 401
    url: https://support.lawtoolbox.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-28'
description: LawToolBox provides automated calendaring and matter management software for law firms and legal departments. Its platform integrates tightly with Microsoft 365, Teams, Word, and other productivity tools, enabling users to schedule, track, and manage legal matters efficiently. The solution offers AI‑enhanced features, customizable workflows, and a client portal, helping legal professionals streamline case timelines and improve collaboration across teams.
image: https://lawtoolbox.com/wp-content/uploads/2025/06/LTB-Logo-2.webp
json_schemas:
- name: GetFirmsFirmidUsersUseridMattersMatteridResponse
  property_count: 15
  slug: lawtoolbox-get-firms-firmid-users-userid-matters-matterid-response
- name: GetFirmsFirmidUsersUseridMattersResponse
  property_count: 15
  slug: lawtoolbox-get-firms-firmid-users-userid-matters-response
- name: PostApiFirmsFirmidUsersUseridMattersMatteridResponse
  property_count: 18
  slug: lawtoolbox-post-api-firms-firmid-users-userid-matters-matterid-response
- name: PostApiFirmsFirmidUsers1MattersMatteridDeadlinesCalculateReq
  property_count: 6
  slug: lawtoolbox-post-api-firms-firmid-users1-matters-matterid-deadlines-calculate-req
- name: PostApiFirmsFirmidUsers1MattersMatteridDeadlinesCalculateRes
  property_count: 18
  slug: lawtoolbox-post-api-firms-firmid-users1-matters-matterid-deadlines-calculate-res
- name: PostFirmsFirmidUsers1MattersResponse
  property_count: 15
  slug: lawtoolbox-post-firms-firmid-users1-matters-response
jsonld:
- class_count: 34
  name: Lawtoolbox Context
  property_count: 82
  slug: lawtoolbox-context
layout: provider
mcp_servers:
- description: Remote MCP server at support.lawtoolbox.com.
  name: LawToolBox MCP Server
  slug: lawtoolbox-mcp-yml
modified: '2026-10-28'
name: LawToolBox
nav: Providers
network: true
overview: 'LawToolBox is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Calendar, Matter Management, Microsoft 365, and Integration.


  The LawToolBox catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LawToolBox''s developer surface includes support, engineering blog, pricing, getting-started guide, and 16 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: LawToolBox API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: lawtoolbox-rules
scopes:
- name: Lawtoolbox Scopes
  scope_count: 0
  slug: lawtoolbox-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 29.6
    developer_ergonomics: 9.5
    discoverability: 60.8
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lawtoolbox/lawtoolbox-2026-11-03T134725.png
security:
- kind: authentication
  name: Lawtoolbox Authentication
  slug: lawtoolbox-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lawtoolbox Domain Security
  slug: lawtoolbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lawtoolbox
tags:
- Legal Tech
- Calendar
- Matter Management
- Microsoft 365
- Integration
website: https://lawtoolbox.com/
---
