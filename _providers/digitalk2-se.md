---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote MCP server (Streamable HTTP) that lets Claude, ChatGPT, Claude Code, Codex or Cursor work on a user's own DigitalK2 K2 annual-report drafts - create a draft, upload the SIE file, read the incom
  name: DigitalK2 MCP Server
  slug: digitalk2-mcp
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/digitalk2-se/plans/digitalk2-se-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digitalk2-se-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/digitalk2-se/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/digitalk2-se/conventions/digitalk2-se-conventions.yml
  title: ''
  type: Conventions
  url: conventions/digitalk2-se-conventions.yml
- group: auth
  href: https://artifacts.apis.io/digitalk2-se/authentication/digitalk2-se-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digitalk2-se-authentication.yml
- group: auth
  href: https://artifacts.apis.io/digitalk2-se/scopes/digitalk2-se-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/digitalk2-se-scopes.yml
- group: design
  href: https://artifacts.apis.io/digitalk2-se/conformance/digitalk2-se-conformance.yml
  title: ''
  type: Conformance
  url: conformance/digitalk2-se-conformance.yml
- group: agent
  href: https://artifacts.apis.io/digitalk2-se/llms/digitalk2-se-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digitalk2-se-llms.txt
- group: agent
  href: https://artifacts.apis.io/digitalk2-se/mcp/digitalk2-se-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/digitalk2-se-mcp.yml
- group: agent
  href: https://artifacts.apis.io/digitalk2-se/well-known/digitalk2-se-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/digitalk2-se-well-known.yml
- group: other
  href: https://artifacts.apis.io/digitalk2-se/hosts/digitalk2-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digitalk2-se-hosts.yml
- group: build
  href: https://artifacts.apis.io/digitalk2-se/integrations/digitalk2-se-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/digitalk2-se-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/digitalk2-se/vendors/digitalk2-se-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digitalk2-se-vendors.yml
- group: build
  href: https://artifacts.apis.io/digitalk2-se/packages/digitalk2-se-packages.yml
  title: ''
  type: SDKs
  url: packages/digitalk2-se-packages.yml
- group: build
  href: https://artifacts.apis.io/digitalk2-se/packages/digitalk2-se-packages.yml
  title: ''
  type: Packages
  url: packages/digitalk2-se-packages.yml
- group: auth
  href: https://artifacts.apis.io/digitalk2-se/security/digitalk2-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digitalk2-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digitalk2.se/
- group: docs
  title: ''
  type: Documentation
  url: https://www.digitalk2.se/mcp
- group: docs
  title: ''
  type: Guides
  url: https://www.digitalk2.se/guider
- group: commercial
  title: ''
  type: Pricing
  url: https://www.digitalk2.se/priser
- group: operate
  title: ''
  type: Support
  url: https://www.digitalk2.se/om-oss
- group: other
  title: ''
  type: Email
  url: mailto:hej@digitalk2.se
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digitalk2.se/villkor
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digitalk2.se/integritet
- group: auth
  title: ''
  type: GDPR
  url: https://www.digitalk2.se/gdpr
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.digitalk2.se/cookies
created: '2026-11-05'
description: DigitalK2 (digitalk2.se) is a Swedish online service for small limited companies (aktiebolag) to create a K2 annual report (årsredovisning) and file it digitally with Bolagsverket, the Swedish Companies Registration Office. Users upload an SIE file exported from their bookkeeping software (or enter figures manually), review the income statement and balance sheet, complete the directors' report and notes, get a tax calculation and INK2 basis, and sign with BankID; filing costs 399 SEK per submission. DigitalK2 also publishes an MCP server (mcp.digitalk2.se) so Claude, ChatGPT or Cursor can help prepare the report. The site footer names DigitalK2 AB (org. no. 559599-6181); its About page says the service is run by Vinka Hej AB.
image: https://www.digitalk2.se/digitalk2-og-1200x630.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.digitalk2.se over streamable HTTP requiring OAuth; 20 tools listed.
  name: DigitalK2 MCP Server
  slug: se-digitalk2-digitalk2
modified: '2026-11-05'
name: DigitalK2
nav: Providers
network: true
overview: 'DigitalK2 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Annual Reports, Bolagsverket, and Sweden.


  DigitalK2''s developer surface includes authentication, documentation, pricing, support, and 21 more developer resources.'
plans:
- name: Digitalk2 Se Plans Pricing
  plan_count: 2
  slug: digitalk2-se-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Digitalk2 Se Rate Limits
  slug: digitalk2-se-rate-limits
scopes:
- name: Digitalk2 Se Scopes
  scope_count: 2
  slug: digitalk2-se-scopes
  summary_line: 2 scopes
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Digitalk2 Se Authentication
  slug: digitalk2-se-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Digitalk2 Se Domain Security
  slug: digitalk2-se-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: digitalk2
  slug: digitalk2-se-digitalk2-provider-skill
slug: digitalk2-se
tags:
- Company
- Accounting
- Annual Reports
- Bolagsverket
- Sweden
- SIE
- Small Business
- Tax
- MCP
website: https://www.digitalk2.se/
---
