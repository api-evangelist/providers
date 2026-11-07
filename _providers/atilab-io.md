---
access_model:
  confidence: low
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/atilab-io/llms/atilab-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atilab-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/atilab-io/mcp/atilab-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atilab-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/atilab-io/well-known/atilab-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atilab-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/atilab-io/hosts/atilab-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atilab-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/atilab-io/vendors/atilab-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atilab-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/atilab-io/security/atilab-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atilab-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atilab.io/
- group: company
  title: ''
  type: Blog
  url: https://www.atilab.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atilab.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atilab.io/terms
- group: operate
  title: ''
  type: Support
  url: https://www.atilab.io/contact
- group: company
  title: ''
  type: About
  url: https://www.atilab.io/about
coverage:
  checked: '2026-11-02'
  detail: All standard OpenAPI discovery paths on api.atilab.io and www.atilab.io returned 404 or non‑spec content, and the advertised API reference URL https://www.atilab.io/api is a 404 page.
  evidence:
  - status: 404
    url: https://api.atilab.io/openapi.json
  - status: 404
    url: https://www.atilab.io/openapi.json
  - status: 404
    url: https://www.atilab.io/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ATI Lab is a long‑term AI partner serving logistics, insurance, accounting, legal and financial services firms. They advise on AI strategy, build custom tools integrated with existing workflows, and operate them for continuous improvement. Their services include AI‑automation, consulting, full‑stack development, and ROI calculators, all measured against baseline performance metrics.
image: https://www.atilab.io/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.atilab.io.
  name: ATI Lab MCP Server
  slug: atilab-io-mcp-yml
modified: '2026-11-02'
name: ATI Lab
nav: Providers
network: true
overview: 'ATI Lab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Logistics, Insurance, Accounting, and Legal.


  ATI Lab''s developer surface includes engineering blog, support, and 10 more developer resources.'
plans:
- name: Atilab Io Plans Pricing
  plan_count: 0
  slug: atilab-io-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Atilab Io Rate Limits
  slug: atilab-io-rate-limits
scopes:
- name: Atilab Io Scopes
  scope_count: 0
  slug: atilab-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 11.8
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atilab Io Authentication
  slug: atilab-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atilab Io Domain Security
  slug: atilab-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atilab-io
tags:
- Artificial Intelligence
- Logistics
- Insurance
- Accounting
- Legal
- Financial Services
- Automation
website: https://www.atilab.io/
---
