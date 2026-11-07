---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
- description: API reference page not found
  name: Artyfile API
  slug: artyfile-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/artyfile-com/plans/artyfile-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/artyfile-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/artyfile-com/llms/artyfile-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/artyfile-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/artyfile-com/mcp/artyfile-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/artyfile-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/artyfile-com/hosts/artyfile-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artyfile-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/artyfile-com/vendors/artyfile-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artyfile-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://artyfile.com/company/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artyfile.com/info/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/artyfile-com/security/artyfile-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artyfile-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://artyfile.com/
- group: company
  title: ''
  type: Blog
  url: https://artyfile.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://artyfile.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://artyfile.com/
created: '2026-11-01'
description: 'Premium music licensing platform: exclusive recordings by real orchestras and musicians, including the London Symphony Orchestra at Abbey Road Studios. Lifetime worldwide sync + master licenses from €29.90, plus fractional master-rights ownership via Limited Editions.'
image: https://media.artyfile.com/media/cf/30/2f/1764608728/artyfile-logo100.png
layout: provider
mcp_servers:
- description: Remote MCP server at artyfile.com.
  name: Artyfile MCP Server
  slug: artyfile-com-mcp-yml
modified: '2026-11-01'
name: Artyfile
nav: Providers
network: true
overview: 'Artyfile is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music Licensing, Sync Licensing, master use license, and orchestral recording.


  Artyfile''s developer surface includes engineering blog, pricing, support, and 9 more developer resources.'
plans:
- name: Artyfile Com Plans Pricing
  plan_count: 2
  slug: artyfile-com-plans-pricing
random_paper: 4
scopes:
- name: Artyfile Com Scopes
  scope_count: 0
  slug: artyfile-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 19.7
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Artyfile Com Authentication
  slug: artyfile-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Artyfile Com Domain Security
  slug: artyfile-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: artyfile-com
tags:
- Company
- Music Licensing
- Sync Licensing
- master use license
- orchestral recording
- music rights investment
website: https://artyfile.com/
---
