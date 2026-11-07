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
  band: human-only
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Claidex MCP provides a JSON-RPC 2.0 interface for managing devices.
  name: Claidex MCP
  slug: claidex-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/claidex-com/llms/claidex-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claidex-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/claidex-com/mcp/claidex-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/claidex-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/claidex-com/hosts/claidex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claidex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/claidex-com/vendors/claidex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claidex-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://claidex.com/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claidex.com/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.claidex.com/auth/login
- group: auth
  href: https://artifacts.apis.io/claidex-com/security/claidex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claidex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claidex.com/
created: '2026-11-03'
description: Claidex provides a continuously‑updated record that traces terminated clinical trials back to their preclinical origins and publishes a mechanistic post‑mortem called a Claim. The service is used by translational researchers, MD/PhD trainees, drug discovery scientists, and science journalists who need fast mechanistic context on failed drug programs.
image: https://framerusercontent.com/assets/9DFjsyweJw1TZjYqypmx5eIPp3s.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.claidex.com.
  name: Claidex MCP Server
  slug: claidex-com-mcp-yml
modified: '2026-11-03'
name: Claidex
nav: Providers
network: true
overview: Claidex is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biomedicine, Clinical Trials, Drug Discovery, and Research.
random_paper: 14
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claidex Com Domain Security
  slug: claidex-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: claidex-com
tags:
- Biomedicine
- Clinical Trials
- Drug Discovery
- Research
website: https://claidex.com/
---
