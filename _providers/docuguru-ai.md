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
    mcp_server: false
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
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DocuGuru provides AI-powered document analysis APIs.
  name: DocuGuru API
  slug: docuguru-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/docuguru-ai/llms/docuguru-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docuguru-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/docuguru-ai/hosts/docuguru-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docuguru-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/docuguru-ai/vendors/docuguru-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docuguru-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/docuguru-ai/security/docuguru-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docuguru-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docuguru.ai/
coverage:
  checked: '2026-11-05'
  detail: OpenAPI spec endpoint requires authentication (401 Unauthorized)
  evidence:
  - status: 401
    url: https://api.docuguru.ai/openapi.json
  reason: auth-required
  state: gated
created: '2026-11-05'
description: 'docuguru-ai is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://docuguru.ai/og-image.png
layout: provider
modified: '2026-11-05'
name: DocuGuru
nav: Providers
network: true
overview: DocuGuru is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 21
score:
  band: minimal
  composite: 2.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Docuguru Ai Domain Security
  slug: docuguru-ai-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: docuguru-ai
tags:
- Company
website: https://docuguru.ai/
---
