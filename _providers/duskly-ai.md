---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Duskly Ai Agentic Access
  operation_count: 3
  slug: duskly-ai-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://duskly.ai
  baseurl_source: declared
  description: The Health API from duskly-ai — 1 operation(s) for health.
  name: duskly-ai Health API
  slug: duskly-ai-health-api
- baseURL: https://duskly.ai
  baseurl_source: declared
  description: The Verify API from duskly-ai — 2 operation(s) for verify.
  name: duskly-ai Verify API
  slug: duskly-ai-verify-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/duskly-ai/agentic-access/duskly-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/duskly-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/duskly-ai/plans/duskly-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/duskly-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/duskly-ai/rules/duskly-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/duskly-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/duskly-ai/json-ld/duskly-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/duskly-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/duskly-ai/vocabulary/duskly-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/duskly-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/duskly-ai/data-model/duskly-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/duskly-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/duskly-ai/errors/duskly-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/duskly-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/duskly-ai/conformance/duskly-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/duskly-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/duskly-ai/llms/duskly-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duskly-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/duskly-ai/mcp/duskly-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/duskly-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/duskly-ai/well-known/duskly-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/duskly-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/duskly-ai/hosts/duskly-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/duskly-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/duskly-ai/vendors/duskly-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/duskly-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://duskly.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://duskly.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://duskly.ai/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://duskly.ai/guides
- group: docs
  title: ''
  type: APIReference
  url: https://duskly.ai/developers
- group: auth
  href: https://artifacts.apis.io/duskly-ai/security/duskly-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duskly-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://duskly.ai/
created: '2026-11-06'
description: Duskly provides AI-powered virtual staging and photo editing tools for real‑estate listings. It offers services such as virtual furniture placement, decluttering, sky replacement, day‑to‑dusk conversion, and virtual renovation, delivering edited images with original photos, disclosure wording, and audit records to meet MLS compliance requirements. Pricing is per photo ($5), per listing ($29), or via subscription plans for agents and studios.
image: https://duskly.ai/og-image.jpg
json_schemas:
- name: Health
  property_count: 3
  slug: duskly-ai-health
- name: VerificationReport
  property_count: 4
  slug: duskly-ai-verification-report
jsonld:
- class_count: 3
  name: Duskly Ai Context
  property_count: 10
  slug: duskly-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at duskly.ai.
  name: duskly-ai MCP Server
  slug: duskly-ai-mcp-yml
modified: '2026-11-06'
name: duskly-ai
nav: Providers
network: true
overview: 'duskly-ai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API and Verify API. Tagged areas include Virtual Staging, AI Photo Editing, Real Estate, MLS Compliance, and Real Estate Tools.


  The duskly-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  duskly-ai''s developer surface includes pricing, documentation, API reference, and 17 more developer resources.'
plans:
- name: Duskly Ai Plans Pricing
  plan_count: 5
  slug: duskly-ai-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: duskly-ai API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: duskly-ai-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 57.5
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Duskly Ai Domain Security
  slug: duskly-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: duskly-ai
tags:
- Virtual Staging
- AI Photo Editing
- Real Estate
- MLS Compliance
- Real Estate Tools
website: https://duskly.ai/
---
