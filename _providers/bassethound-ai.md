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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Bassethound API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Bassethound API
  slug: bassethound-ai-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bassethound-ai/plans/bassethound-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bassethound-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bassethound-ai/rules/bassethound-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bassethound-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bassethound-ai/vocabulary/bassethound-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bassethound-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bassethound-ai/conformance/bassethound-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bassethound-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bassethound-ai/llms/bassethound-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bassethound-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/bassethound-ai/well-known/bassethound-ai-nimblebrain-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bassethound-ai-nimblebrain-security.txt
- group: agent
  href: https://artifacts.apis.io/bassethound-ai/well-known/bassethound-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bassethound-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bassethound-ai/hosts/bassethound-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bassethound-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bassethound-ai/vendors/bassethound-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bassethound-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bassethound.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://bassethound.ai/pricing
- group: auth
  href: https://artifacts.apis.io/bassethound-ai/security/bassethound-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bassethound-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bassethound.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://bassethound.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.bassethound.ai/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://bassethound.ai/docs
- group: operate
  title: ''
  type: Support
  url: https://bassethound.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bassethound.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bassethound.ai/terms
coverage:
  checked: '2026-11-02'
  detail: The provider’s documentation site returns only HTML pages without any published OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 301
    url: https://bassethound.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bassethound provides company intelligence using AI, offering a remote MCP server that returns source‑linked dossiers for any domain. The platform includes tools for AI‑readiness assessment, enrichment use cases, and integrates with Claude, ChatGPT, Cursor, and other clients. It aims to give a comprehensive view of a company’s technology stack, AI adoption, and overall signal with a simple API call.
image: https://bassethound.ai/og.png
layout: provider
modified: '2026-11-02'
name: Bassethound
nav: Providers
network: true
overview: 'Bassethound is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Intelligence, MCP, and Company Intelligence.


  The Bassethound catalog on APIs.io includes 1 Spectral governance ruleset.


  Bassethound''s developer surface includes pricing, documentation, API reference, getting-started guide, support, and 14 more developer resources.'
plans:
- name: Bassethound Ai Plans Pricing
  plan_count: 4
  slug: bassethound-ai-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Bassethound API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: bassethound-ai-rules
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bassethound Ai Domain Security
  slug: bassethound-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bassethound-ai
tags:
- Company
- Artificial Intelligence
- Intelligence
- MCP
- Company Intelligence
website: https://bassethound.ai/
---
