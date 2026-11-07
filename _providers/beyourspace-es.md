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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 5.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Beyourspace Es Agentic Access
  operation_count: 4
  slug: beyourspace-es-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 6
apis:
- description: Normaliza definiciones JSON Schema en un manifiesto JSON de tools con nombres, descripciones y esquemas de entrada consistentes para agentes de código.
  name: Convierte JSON Schema
  slug: convierte-json-schema
- description: ''
  name: Convierte Lista Tareas
  slug: convierte-lista-tareas
- description: ''
  name: Convierte Operaciones
  slug: convierte-operaciones
- description: ''
  name: Normaliza Handoffs
  slug: normaliza-handoffs
- description: ''
  name: Normaliza Logs Uso LLM
  slug: normaliza-logs-uso-llm
- description: ''
  name: Normalize SaaS
  slug: normalize-saas
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/beyourspace-es/agentic-access/beyourspace-es-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/beyourspace-es-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/beyourspace-es/rules/beyourspace-es-rules.yml
  title: ''
  type: Spectral
  url: rules/beyourspace-es-rules.yml
- group: design
  href: https://artifacts.apis.io/beyourspace-es/errors/beyourspace-es-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beyourspace-es-problem-types.yml
- group: design
  href: https://artifacts.apis.io/beyourspace-es/conformance/beyourspace-es-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beyourspace-es-conformance.yml
- group: agent
  href: https://artifacts.apis.io/beyourspace-es/llms/beyourspace-es-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beyourspace-es-llms.txt
- group: other
  href: https://artifacts.apis.io/beyourspace-es/hosts/beyourspace-es-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beyourspace-es-hosts.yml
- group: other
  href: https://artifacts.apis.io/beyourspace-es/vendors/beyourspace-es-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beyourspace-es-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beyourspace.es/privacy
- group: auth
  href: https://artifacts.apis.io/beyourspace-es/security/beyourspace-es-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beyourspace-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beyourspace.es/
created: '2026-11-02'
description: beyourspace provides a catalog of pay‑per‑use tools and APIs, automatically published and maintained by an automated system. It offers a searchable directory of APIs with usage‑based pricing, aiming to simplify discovery and integration for developers seeking ready‑to‑use services.
layout: provider
modified: '2026-11-02'
name: beyourspace
nav: Providers
network: true
overview: 'beyourspace is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Catalog, Pay-Per-Use, Automation, Discovery, and Spanish.


  The beyourspace catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: beyourspace API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: beyourspace-es-rules
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beyourspace Es Domain Security
  slug: beyourspace-es-domain-security
  summary_line: TLSv1.3 · HSTS
slug: beyourspace-es
tags:
- API Catalog
- Pay-Per-Use
- Automation
- Discovery
- Spanish
website: https://beyourspace.es/
---
