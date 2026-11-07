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
  title: ''
  type: Security
  url: https://dronelicencechecker.co.uk/terms
- group: agent
  href: https://artifacts.apis.io/dronelicencechecker-co-uk/llms/dronelicencechecker-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dronelicencechecker-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/dronelicencechecker-co-uk/mcp/dronelicencechecker-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dronelicencechecker-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dronelicencechecker-co-uk/mcp/dronelicencechecker-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dronelicencechecker-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dronelicencechecker-co-uk/well-known/dronelicencechecker-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dronelicencechecker-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/dronelicencechecker-co-uk/well-known/dronelicencechecker-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dronelicencechecker-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/dronelicencechecker-co-uk/hosts/dronelicencechecker-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dronelicencechecker-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/dronelicencechecker-co-uk/vendors/dronelicencechecker-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dronelicencechecker-co-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dronelicencechecker-co-uk/security/dronelicencechecker-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dronelicencechecker-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dronelicencechecker-co-uk/security/dronelicencechecker-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dronelicencechecker-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dronelicencechecker.co.uk/
- group: company
  title: ''
  type: About
  url: https://dronelicencechecker.co.uk/about/
- group: operate
  title: ''
  type: Contact
  url: https://dronelicencechecker.co.uk/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dronelicencechecker.co.uk/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dronelicencechecker.co.uk/terms/
created: '2026-11-06'
description: Drone Licence Checker UK provides a free online tool to help UK drone operators determine whether they need to register their drone, obtain an Operator ID or Flyer ID, and understand the applicable CAA rules. The site offers guides, data tables, and links to official UK Civil Aviation Authority resources, covering categories A1, A2, A3, weight thresholds, camera requirements, and near‑people flight restrictions as of 2026.
image: https://dronelicencechecker.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at dronelicencechecker.co.uk requiring an API key.
  name: Drone Licence Checker UK MCP Server
  slug: dronelicencechecker-co-uk-mcp-yml
modified: '2026-11-06'
name: Drone Licence Checker UK
nav: Providers
network: true
overview: Drone Licence Checker UK is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drone, United Kingdom, Aviation, and Regulations.
random_paper: 12
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 10.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dronelicencechecker Co Uk Domain Security
  slug: dronelicencechecker-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dronelicencechecker Co Uk Vulnerability Disclosure
  slug: dronelicencechecker-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dronelicencechecker-co-uk
tags:
- Company
- Drone
- United Kingdom
- Aviation
- Regulations
website: https://dronelicencechecker.co.uk/
---
