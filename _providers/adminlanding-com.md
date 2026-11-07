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
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'AdminLanding — French Admin in English: Leases, Tax & Rental Tools'
  name: AdminLanding API
  slug: adminlanding-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: Security
  url: https://www.adminlanding.com/privacy
- group: agent
  href: https://artifacts.apis.io/adminlanding-com/llms/adminlanding-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adminlanding-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/adminlanding-com/mcp/adminlanding-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adminlanding-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/adminlanding-com/well-known/adminlanding-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adminlanding-com-security.txt
- group: auth
  href: https://artifacts.apis.io/adminlanding-com/well-known/adminlanding-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adminlanding-com-api-security.txt
- group: auth
  href: https://artifacts.apis.io/adminlanding-com/well-known/adminlanding-com-adminlanding-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adminlanding-com-adminlanding-security.txt
- group: agent
  href: https://artifacts.apis.io/adminlanding-com/well-known/adminlanding-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adminlanding-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adminlanding-com/hosts/adminlanding-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adminlanding-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adminlanding-com/vendors/adminlanding-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adminlanding-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.adminlanding.com/login
- group: auth
  href: https://artifacts.apis.io/adminlanding-com/security/adminlanding-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adminlanding-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/adminlanding-com/security/adminlanding-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adminlanding-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adminlanding.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adminlanding.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adminlanding.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adminlanding.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.adminlanding.com/contact
coverage:
  checked: '2026-10-31'
  detail: MCP tools/list endpoint requires authentication (Bearer token) and no public OpenAPI spec is available.
  evidence:
  - status: 406
    url: https://www.adminlanding.com/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: AdminLanding is a bilingual French‑administration SaaS that helps residents and expats generate legally‑valid leases, rent receipts, tax forms and other official documents. The platform guides users step‑by‑step through more than 25 French government portals, offering free tools and paid packs. Founded by Julien Maurice, the service provides English‑language explanations while all generated documents remain in French to satisfy legal requirements. It includes mobile apps, a Chrome extension, and a secure EU‑hosted backend with AES‑256 encryption.
image: https://www.adminlanding.com/2.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.adminlanding.com requiring OAuth.
  name: AdminLanding MCP Server
  slug: adminlanding-com-mcp-yml
modified: '2026-10-31'
name: AdminLanding
nav: Providers
network: true
overview: 'AdminLanding is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Software-as-a-Service, French Administration, Real Estate, and Tax.


  AdminLanding''s developer surface includes pricing, support, and 15 more developer resources.'
plans:
- name: Adminlanding Com Plans Pricing
  plan_count: 0
  slug: adminlanding-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Adminlanding Com Rate Limits
  slug: adminlanding-com-rate-limits
scopes:
- name: Adminlanding Com Scopes
  scope_count: 0
  slug: adminlanding-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.3
    operational_transparency: 5.3
  previous_composite: 20.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adminlanding Com Authentication
  slug: adminlanding-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adminlanding Com Domain Security
  slug: adminlanding-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Adminlanding Com Vulnerability Disclosure
  slug: adminlanding-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: adminlanding-com
tags:
- Software-as-a-Service
- French Administration
- Real Estate
- Tax
website: https://adminlanding.com/
---
