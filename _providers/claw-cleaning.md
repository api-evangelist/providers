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
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/claw-cleaning/llms/claw-cleaning-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claw-cleaning-llms.txt
- group: build
  href: https://artifacts.apis.io/claw-cleaning/mcp/claw-cleaning-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/claw-cleaning-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/claw-cleaning/mcp/claw-cleaning-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/claw-cleaning-mcp.yml
- group: other
  href: https://artifacts.apis.io/claw-cleaning/hosts/claw-cleaning-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claw-cleaning-hosts.yml
- group: other
  href: https://artifacts.apis.io/claw-cleaning/vendors/claw-cleaning-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claw-cleaning-vendors.yml
- group: auth
  href: https://artifacts.apis.io/claw-cleaning/security/claw-cleaning-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claw-cleaning-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claw.cleaning/
- group: docs
  title: ''
  type: APIReference
  url: https://claw.cleaning/mcp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claw.cleaning/privacy
- group: operate
  title: ''
  type: Contact
  url: mailto:connor@getcolby.com
coverage:
  checked: '2026-11-04'
  detail: Provider's website serves only HTML pages and a JSON MCP endpoint without any published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://claw.cleaning/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: claw.cleaning provides an AI‑driven apartment cleaning service in San Francisco. Users can book weekend cleaning slots via natural‑language commands to an AI assistant, which handles availability, scheduling, and payment directly with the cleaner. The service operates through a Model Context Protocol (MCP) endpoint and integrates with calendar tools. It emphasizes privacy, with no upfront payment collection or personal data sharing beyond booking details.
image: https://claw.cleaning/assets/icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at claw.cleaning; 3 tools listed.
  name: claw.cleaning MCP Server
  slug: claw-cleaning-mcp-yml
modified: '2026-11-03'
name: claw.cleaning
nav: Providers
network: true
overview: 'claw.cleaning is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cleaning, Artificial Intelligence, ApartmentService, San Francisco, and Booking.


  claw.cleaning''s developer surface includes API reference and 9 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claw Cleaning Domain Security
  slug: claw-cleaning-domain-security
  summary_line: TLSv1.3
slug: claw-cleaning
tags:
- Cleaning
- Artificial Intelligence
- ApartmentService
- San Francisco
- Booking
website: https://claw.cleaning/
---
