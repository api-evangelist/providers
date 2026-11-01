---
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Batesio Com Agentic Access
  operation_count: 1
  slug: batesio-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: 'Batesio: the monthly US and GB search demand across the tools this product ships, read from monthly searches (September 2026), served as an agent-callable dataset.'
  name: Batesio API
  slug: batesio-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/batesio-com/agentic-access/batesio-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/batesio-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/batesio-com/plans/batesio-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/batesio-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/batesio-com/rules/batesio-com-rules.yml
  title: ''
  type: Spectral
  url: rules/batesio-com-rules.yml
- group: design
  href: https://artifacts.apis.io/batesio-com/vocabulary/batesio-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/batesio-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/batesio-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://batesio.com/terms
- group: design
  href: https://artifacts.apis.io/batesio-com/errors/batesio-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/batesio-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/batesio-com/conformance/batesio-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/batesio-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/batesio-com/llms/batesio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/batesio-com-llms.txt
- group: build
  href: https://artifacts.apis.io/batesio-com/mcp/batesio-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/batesio-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/batesio-com/mcp/batesio-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/batesio-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/batesio-com/well-known/batesio-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/batesio-com-security.txt
- group: auth
  href: https://artifacts.apis.io/batesio-com/well-known/batesio-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/batesio-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/batesio-com/well-known/batesio-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/batesio-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/batesio-com/hosts/batesio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/batesio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/batesio-com/vendors/batesio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/batesio-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/batesio-com/packages/batesio-com-packages.yml
  title: ''
  type: SDKs
  url: packages/batesio-com-packages.yml
- group: build
  href: https://artifacts.apis.io/batesio-com/packages/batesio-com-packages.yml
  title: ''
  type: Packages
  url: packages/batesio-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://batesio.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://batesio.com/privacy/
- group: auth
  href: https://artifacts.apis.io/batesio-com/authentication/batesio-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/batesio-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/batesio-com/security/batesio-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/batesio-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/batesio-com/security/batesio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/batesio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://batesio.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://batesio.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://batesio.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://app.batesio.com/?upgrade=pro
created: '2026-10-29'
description: Batesio provides free document capture worksheet tools for small accounting, real estate and professional firms, allowing users to capture documents from their own boxes, pages and lookups. The platform offers a paid plan that includes a client document portal, page numbering, retention records, and secure sharing features. Founded in 2026, Batesio aims to simplify document management for small businesses with a SaaS solution.
image: https://batesio.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at batesio.com.
  name: batesio-com MCP Server
  slug: batesio-com-mcp-yml
modified: '2026-10-29'
name: batesio-com
nav: Providers
network: true
overview: 'batesio-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Document Management, Accounting, SaaS, Small Business, and File Sharing.


  The batesio-com catalog on APIs.io includes 1 Spectral governance ruleset.


  batesio-com''s developer surface includes authentication, pricing, support, signup flow, and 23 more developer resources.'
plans:
- name: Batesio Com Plans Pricing
  plan_count: 2
  slug: batesio-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Batesio Com Rate Limits
  slug: batesio-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: batesio-com API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: batesio-com-rules
scopes:
- name: Batesio Com Scopes
  scope_count: 0
  slug: batesio-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 6.0
    developer_ergonomics: 30.2
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Batesio Com Authentication
  slug: batesio-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Batesio Com Domain Security
  slug: batesio-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Batesio Com Vulnerability Disclosure
  slug: batesio-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset
  slug: batesio-com-dataset-skill
slug: batesio-com
tags:
- Document Management
- Accounting
- SaaS
- Small Business
- File Sharing
website: https://batesio.com/
---
