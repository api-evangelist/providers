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
  score: 0.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Machine-readable access to the AIO Framework vocabulary, papers, benchmark distributions, and the Tier 0 measurement pipeline.
  name: AIO Public API
  slug: aio-public-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/aioq-org/vocabulary/aioq-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aioq-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aioq-org/conformance/aioq-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aioq-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aioq-org/llms/aioq-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aioq-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/aioq-org/mcp/aioq-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aioq-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/aioq-org/hosts/aioq-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aioq-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/aioq-org/vendors/aioq-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aioq-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aioq.org/en/terms
- group: operate
  title: ''
  type: Support
  url: https://aioq.org/en/join/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aioq.org/en/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://aioq.org/en/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://aioq.org/en/developers
- group: auth
  href: https://artifacts.apis.io/aioq-org/security/aioq-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aioq-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aioq.org/
created: '2026-11-01'
description: AIO (AI Integrity Organization) is a global non‑profit that standardizes and operates a common vocabulary for AI decision‑making. It builds a trusted AI integrity ecosystem by measuring, recording, and openly verifying how AI systems reach judgments, offering open standards, verification, and governance to ensure transparent and accountable AI outcomes.
image: https://aioq.org/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at aioq.org.
  name: AIO MCP Server
  slug: aioq-org-mcp-yml
modified: '2026-11-01'
name: AIO
nav: Providers
network: true
overview: 'AIO is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Integrity, Open Standard, Measurements, Legal Reference Data, and Framework.


  AIO''s developer surface includes support, getting-started guide, API reference, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 18.6
  provenance:
    conformance: first-party
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aioq Org Domain Security
  slug: aioq-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aioq-org
tags:
- AI Integrity
- Open Standard
- Measurements
- Legal Reference Data
- Framework
- Research
- Regulations
website: https://aioq.org/
---
