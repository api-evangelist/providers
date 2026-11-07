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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cortex is a semantic memory infrastructure enabling AI models to retain context across conversations.
  name: Cortex
  slug: cortex
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/skynetlab-cortex/plans/skynetlab-cortex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/skynetlab-cortex-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://skynetlab-cortex.com/sicurezza
- group: auth
  href: https://artifacts.apis.io/skynetlab-cortex/security/skynetlab-cortex-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/skynetlab-cortex-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/skynetlab-cortex/llms/skynetlab-cortex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skynetlab-cortex-llms.txt
- group: other
  href: https://artifacts.apis.io/skynetlab-cortex/hosts/skynetlab-cortex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skynetlab-cortex-hosts.yml
- group: other
  href: https://artifacts.apis.io/skynetlab-cortex/vendors/skynetlab-cortex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skynetlab-cortex-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skynetlab-cortex.com/privacy.html
- group: other
  title: ''
  type: Leadership
  url: https://skynetlab-cortex.com/team
- group: auth
  href: https://artifacts.apis.io/skynetlab-cortex/security/skynetlab-cortex-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/skynetlab-cortex-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/skynetlab-cortex/security/skynetlab-cortex-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/skynetlab-cortex-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/skynetlab-cortex/security/skynetlab-cortex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skynetlab-cortex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skynetlab-cortex.com/
coverage:
  checked: '2026-10-19'
  detail: No public API documentation or developer program is provided on the website.
  evidence:
  - status: 200
    url: https://skynetlab-cortex.com/abbonamenti.html
  reason: no-developer-program
  state: none
created: '2026-10-18'
description: SKYNETLAB offers Cortex, a patent‑pending semantic memory infrastructure that provides persistent, model‑independent AI context. It enables AI systems to retain information across conversations, acting as a long‑term memory layer for large language models. Available as a ChatGPT connector, Cortex aims to reduce forgetting in AI applications and improve continuity of user interactions.
image: https://skynetlab-cortex.com/assets/og-cortex.jpg
layout: provider
modified: '2026-10-18'
name: SKYNETLAB
nav: Providers
network: true
overview: SKYNETLAB is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, SemanticMemory, ChatGPTConnector, and Infrastructure.
plans:
- name: Skynetlab Cortex Plans Pricing
  plan_count: 4
  slug: skynetlab-cortex-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.2
    operational_transparency: 10.5
  previous_composite: 20.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/skynetlab-cortex/skynetlab-cortex-2026-11-03T143317.png
security:
- kind: domain-security
  name: Skynetlab Cortex Domain Security
  slug: skynetlab-cortex-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Skynetlab Cortex Vulnerability Disclosure
  slug: skynetlab-cortex-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Skynetlab Cortex Trust Center
  slug: skynetlab-cortex-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: skynetlab-cortex
tags:
- Company
- Artificial Intelligence
- SemanticMemory
- ChatGPTConnector
- Infrastructure
website: https://skynetlab-cortex.com/
---
