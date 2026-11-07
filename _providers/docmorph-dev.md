---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Docmorph Dev Agentic Access
  operation_count: 9
  slug: docmorph-dev-agentic-access
  summary_line: 9 operations · 8 acting
api_count: 1
apis:
- baseURL: https://docmorph.dev
  baseurl_source: declared
  description: The Tools API from DocMorph — 9 operation(s) for tools.
  name: DocMorph Tools API
  slug: docmorph-dev-tools-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/docmorph-dev/agentic-access/docmorph-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/docmorph-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/docmorph-dev/plans/docmorph-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docmorph-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/docmorph-dev/rules/docmorph-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/docmorph-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/docmorph-dev/conformance/docmorph-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docmorph-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docmorph-dev/llms/docmorph-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docmorph-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/docmorph-dev/mcp/docmorph-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/docmorph-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/docmorph-dev/mcp/docmorph-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/docmorph-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/docmorph-dev/well-known/docmorph-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docmorph-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/docmorph-dev/hosts/docmorph-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docmorph-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/docmorph-dev/vendors/docmorph-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docmorph-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/docmorph-dev/authentication/docmorph-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/docmorph-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/docmorph-dev/security/docmorph-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docmorph-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docmorph.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docmorph.dev/en
- group: commercial
  title: ''
  type: Pricing
  url: https://docmorph.dev/en/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docmorph.dev/en/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docmorph.dev/en/terms
created: '2026-11-05'
description: DocMorph Studio provides a browser‑based, local‑first workspace for private PDF, document, image, video and audio processing. All core conversions, OCR, metadata scrubbing and watermarking run 100 % in the user’s browser via WebAssembly, ensuring no files are uploaded to a server. The platform offers free tools with daily credit limits, a VIP annual pass for unlimited use, and an on‑premise enterprise edition for air‑gapped environments, targeting privacy‑sensitive sectors such as legal, healthcare, finance and government.
image: https://docmorph.dev/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at docmorph.dev.
  name: DocMorph MCP Server
  slug: docmorph-dev-mcp-yml
modified: '2026-11-05'
name: DocMorph
nav: Providers
network: true
overview: 'DocMorph publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Tools API. Tagged areas include Document Processing, Privacy, OCR, Media, and Local-First.


  The DocMorph catalog on APIs.io includes 1 Spectral governance ruleset.


  DocMorph''s developer surface includes authentication, documentation, pricing, and 14 more developer resources.'
plans:
- name: Docmorph Dev Plans Pricing
  plan_count: 3
  slug: docmorph-dev-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: DocMorph API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: docmorph-dev-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 48.0
    developer_ergonomics: 21.4
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Docmorph Dev Authentication
  slug: docmorph-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Docmorph Dev Domain Security
  slug: docmorph-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: docmorph-dev
tags:
- Document Processing
- Privacy
- OCR
- Media
- Local-First
website: https://docmorph.dev/
---
