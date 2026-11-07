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
- description: Machine Control Protocol (MCP) providing tool list for eBilanz Fabrik. Accessible via POST only at /mcp.
  name: eBilanz Fabrik MCP
  slug: ebilanz-fabrik-mcp
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/ebilanzfabrik-de/security/ebilanzfabrik-de-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ebilanzfabrik-de-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/ebilanzfabrik-de/llms/ebilanzfabrik-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ebilanzfabrik-de-llms.txt
- group: agent
  href: https://artifacts.apis.io/ebilanzfabrik-de/mcp/ebilanzfabrik-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ebilanzfabrik-de-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ebilanzfabrik-de/well-known/ebilanzfabrik-de-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ebilanzfabrik-de-security.txt
- group: agent
  href: https://artifacts.apis.io/ebilanzfabrik-de/well-known/ebilanzfabrik-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ebilanzfabrik-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/ebilanzfabrik-de/hosts/ebilanzfabrik-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ebilanzfabrik-de-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ebilanzfabrik-de/security/ebilanzfabrik-de-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ebilanzfabrik-de-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ebilanzfabrik-de/security/ebilanzfabrik-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ebilanzfabrik-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ebilanzfabrik.de/
coverage:
  checked: '2026-11-06'
  detail: MCP endpoint only accepts POST, GET returns 405, preventing contract discovery.
  evidence:
  - status: 405
    url: https://app.ebilanzfabrik.de/mcp
  reason: auth-required
  state: gated
created: '2026-11-06'
description: eBilanz Fabrik provides a cloud-based service to create electronic balance sheets (e‑Bilanz) from PDF, Excel or CSV files and submit them to the German tax authority via ELSTER. Users can upload their annual financial statements, receive XBRL‑formatted e‑Bilanz documents, and complete filing within minutes, with pricing starting at €29.95 per submission. The platform targets small and micro GmbHs, offering a fast, no‑accountancy‑required solution for German businesses.
image: https://ebilanzfabrik.de/og-image-2495.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.ebilanzfabrik.de.
  name: eBilanz Fabrik MCP Server
  slug: ebilanzfabrik-de-mcp-yml
modified: '2026-11-06'
name: eBilanz Fabrik
nav: Providers
network: true
overview: eBilanz Fabrik is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Accounting, Tax, and Software-as-a-Service.
random_paper: 2
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ebilanzfabrik De Domain Security
  slug: ebilanzfabrik-de-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ebilanzfabrik De Vulnerability Disclosure
  slug: ebilanzfabrik-de-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ebilanzfabrik-de
tags:
- Company
- Finance
- Accounting
- Tax
- Software-as-a-Service
- Germany
website: https://ebilanzfabrik.de/
---
