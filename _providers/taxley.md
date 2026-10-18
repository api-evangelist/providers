---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Taxley Agentic Access
  operation_count: 35
  slug: taxley-agentic-access
  summary_line: 35 operations · 17 acting
api_count: 1
apis:
- description: Taxley provides free UK corporation tax calculators via a public JSON API.
  name: Taxley API
  slug: taxley-api
- baseURL: https://taxley.co.uk
  baseurl_source: spec
  description: The Tools API from Taxley (UK Corporation Tax API) — 18 operation(s) for tools.
  name: Taxley (UK Corporation Tax API) Tools API
  slug: taxley-tools-api
artifact_total: 9
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/agentic-access/taxley-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/taxley-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/plans/taxley-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/taxley-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/rules/taxley-rules.yml
  title: ''
  type: Spectral
  url: rules/taxley-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/json-ld/taxley-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/taxley-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/vocabulary/taxley-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/taxley-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/data-model/taxley-data-model.yml
  title: ''
  type: DataModel
  url: data-model/taxley-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/errors/taxley-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/taxley-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/conformance/taxley-conformance.yml
  title: ''
  type: Conformance
  url: conformance/taxley-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/llms/taxley-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/taxley-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/mcp/taxley-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/taxley-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/well-known/taxley-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/taxley-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/well-known/taxley-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/taxley-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/hosts/taxley-hosts.yml
  title: ''
  type: Hosts
  url: hosts/taxley-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taxley.co.uk/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://taxley.co.uk/help
- group: auth
  title: ''
  type: Security
  url: https://taxley.co.uk/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taxley.co.uk/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://taxley.co.uk/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://taxley.co.uk/press
- group: start
  title: ''
  type: Login
  url: https://taxley.co.uk/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/security/taxley-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/taxley-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taxley/refs/heads/main/security/taxley-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/taxley-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://taxley.co.uk
- group: docs
  title: ''
  type: Documentation
  url: https://taxley.co.uk/developers
coverage:
  checked: '2026-10-15'
  detail: The developers page returns HTML with no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://taxley.co.uk/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Taxley provides free UK Corporation Tax calculators and a public JSON API for developers and AI assistants. It offers tools to compute corporation tax, deadlines, penalties, and related calculations without requiring an API key. Results link back to Taxley’s website for verification. The service is operated by Taxley UK LLP, a UK‑registered limited liability partnership, and integrates with HMRC filing processes.
image: https://taxley.co.uk/images/og/taxley-share-v1.jpg
jsonld:
- class_count: 2
  name: Taxley Context
  property_count: 9
  slug: taxley-context
layout: provider
mcp_servers:
- description: Remote MCP server at taxley.co.uk.
  name: Taxley (UK Corporation Tax API) MCP Server
  slug: taxley-mcp-yml
modified: '2026-10-15'
name: Taxley (UK Corporation Tax API)
nav: Providers
network: true
overview: 'Taxley (UK Corporation Tax API) publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Tools API, and 1 more. Tagged areas include Company, Tax, United Kingdom, and Finance.


  The Taxley (UK Corporation Tax API) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Taxley (UK Corporation Tax API)''s developer surface includes support, pricing, documentation, and 21 more developer resources.'
plans:
- name: Taxley Plans Pricing
  plan_count: 3
  slug: taxley-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Taxley (UK Corporation Tax API) API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: taxley-rules
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 51.8
    developer_ergonomics: 14.3
    discoverability: 60.0
    operational_transparency: 10.5
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
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Taxley Domain Security
  slug: taxley-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Taxley Vulnerability Disclosure
  slug: taxley-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: taxley
tags:
- Company
- Tax
- United Kingdom
- Finance
website: https://taxley.co.uk
---
