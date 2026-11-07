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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Camdentools Com Agentic Access
  operation_count: 2
  slug: camdentools-com-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://camdentools.com
  baseurl_source: declared
  description: The Mcp API from Camden Tools — 2 operation(s) for mcp.
  name: Camden Tools MCP API
  slug: camdentools-com-mcp-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/camdentools-com/agentic-access/camdentools-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/camdentools-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/camdentools-com/rules/camdentools-com-rules.yml
  title: ''
  type: Spectral
  url: rules/camdentools-com-rules.yml
- group: design
  href: https://artifacts.apis.io/camdentools-com/conformance/camdentools-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/camdentools-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/camdentools-com/llms/camdentools-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/camdentools-com-llms.txt
- group: other
  href: https://artifacts.apis.io/camdentools-com/a2a/camdentools-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/camdentools-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/camdentools-com/well-known/camdentools-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/camdentools-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/camdentools-com/hosts/camdentools-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/camdentools-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/camdentools-com/vendors/camdentools-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/camdentools-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://camdentools.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://camdentools.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://camdentools.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://camdentools.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://camdentools.com/developers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CamdenTools
- group: auth
  href: https://artifacts.apis.io/camdentools-com/security/camdentools-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/camdentools-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://camdentools.com/
created: '2026-11-04'
description: Camden Tools is a UK‑based online retailer specialising in professional construction tools and accessories. It offers a wide range of power tools, hand tools, safety gear and consumables for contractors, tradespeople and DIY enthusiasts worldwide. The site provides detailed product information, pricing (including VAT), stock levels and bulk‑order options, with a focus on durability and performance.
layout: provider
modified: '2026-11-04'
name: Camden Tools
nav: Providers
network: true
overview: 'Camden Tools publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: MCP API. Tagged areas include Company, Tools, Construction, Retail, and United Kingdom.


  The Camden Tools catalog on APIs.io includes 1 Spectral governance ruleset.


  Camden Tools'' developer surface includes support, engineering blog, API reference, and 13 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: Camden Tools API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: camdentools-com-rules
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 31.8
    contract_quality: 46.5
    developer_ergonomics: 7.1
    discoverability: 62.5
    operational_transparency: 2.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Camdentools Com Domain Security
  slug: camdentools-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: camdentools-com
tags:
- Company
- Tools
- Construction
- Retail
- United Kingdom
website: https://camdentools.com/
---
