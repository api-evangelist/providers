---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/clearmind-capital-com/security/clearmind-capital-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/clearmind-capital-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/clearmind-capital-com/llms/clearmind-capital-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearmind-capital-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/clearmind-capital-com/mcp/clearmind-capital-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clearmind-capital-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/clearmind-capital-com/well-known/clearmind-capital-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clearmind-capital-com-security.txt
- group: agent
  href: https://artifacts.apis.io/clearmind-capital-com/well-known/clearmind-capital-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clearmind-capital-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/clearmind-capital-com/hosts/clearmind-capital-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearmind-capital-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/clearmind-capital-com/vendors/clearmind-capital-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearmind-capital-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clearmind-capital.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clearmind-capital.com/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://clearmind-capital.com/team/nick-george/
- group: auth
  href: https://artifacts.apis.io/clearmind-capital-com/security/clearmind-capital-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clearmind-capital-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clearmind-capital-com/security/clearmind-capital-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearmind-capital-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clearmind-capital.com/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is published; only an MCP endpoint is available.
  evidence:
  - status: 405
    url: https://clearmind-capital.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: ClearMind Capital is a fee‑only fiduciary financial planning firm based in Columbus, Ohio. They help families navigate major financial decisions, offering personalized strategies for wealth management, retirement planning, tax optimization, and estate planning. Their mission is to empower clients with transparent, client‑first advice and to build lasting financial confidence.
image: https://clearmind-capital.com/assets/og-home-v2.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at clearmind-capital.com.
  name: ClearMind Capital MCP Server
  slug: clearmind-capital-com-mcp-yml
modified: '2026-11-03'
name: ClearMind Capital
nav: Providers
network: true
overview: ClearMind Capital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Financial Planning, Fiduciary, Columbus, and Wealth Management.
random_paper: 22
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clearmind Capital Com Domain Security
  slug: clearmind-capital-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clearmind Capital Com Vulnerability Disclosure
  slug: clearmind-capital-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clearmind-capital-com
tags:
- Financial Services
- Financial Planning
- Fiduciary
- Columbus
- Wealth Management
website: https://clearmind-capital.com/
---
