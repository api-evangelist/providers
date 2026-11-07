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
    agent_skills: derived
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
  score: 6.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Brandone Ir Agentic Access
  operation_count: 3
  slug: brandone-ir-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: Order a branded IPFS gateway for your domain. Pay exact USDT (TRC20) amount.
  name: Portvan Order API
  slug: portvan-order-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/brandone-ir/agentic-access/brandone-ir-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/brandone-ir-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/brandone-ir/rules/brandone-ir-rules.yml
  title: ''
  type: Spectral
  url: rules/brandone-ir-rules.yml
- group: agent
  href: https://artifacts.apis.io/brandone-ir/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/brandone-ir/errors/brandone-ir-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brandone-ir-problem-types.yml
- group: design
  href: https://artifacts.apis.io/brandone-ir/conformance/brandone-ir-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brandone-ir-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brandone-ir/llms/brandone-ir-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brandone-ir-llms.txt
- group: other
  href: https://artifacts.apis.io/brandone-ir/hosts/brandone-ir-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brandone-ir-hosts.yml
- group: other
  href: https://artifacts.apis.io/brandone-ir/vendors/brandone-ir-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brandone-ir-vendors.yml
- group: auth
  href: https://artifacts.apis.io/brandone-ir/security/brandone-ir-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brandone-ir-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandone.ir/
created: '2026-11-02'
description: برندوان یک شرکت مشاوره‌ای در زمینه برندینگ، تولید محتوا و تحول دیجیتال است که از سال ۱۳۹۶ فعالیت می‌کند. این شرکت به کسب‌وکارها کمک می‌کند تا هویت برند خود را بسازند، محتوای دقیق تولید کنند و برای تحول دیجیتال آماده شوند.
layout: provider
modified: '2026-11-02'
name: برندوان
nav: Providers
network: true
overview: 'برندوان is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Branding, Consulting, Digital Transformation, Content Creation, and Iran.


  The برندوان catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: برندوان API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: brandone-ir-rules
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 1.8
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brandone Ir Domain Security
  slug: brandone-ir-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: brandone-ir-purchase-plan
  slug: brandone-ir-purchase-plan
slug: brandone-ir
tags:
- Branding
- Consulting
- Digital Transformation
- Content Creation
- Iran
website: https://brandone.ir/
---
