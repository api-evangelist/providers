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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/artifactos-studio/llms/artifactos-studio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/artifactos-studio-llms.txt
- group: other
  href: https://artifacts.apis.io/artifactos-studio/hosts/artifactos-studio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artifactos-studio-hosts.yml
- group: other
  href: https://artifacts.apis.io/artifactos-studio/vendors/artifactos-studio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artifactos-studio-vendors.yml
- group: auth
  href: https://artifacts.apis.io/artifactos-studio/security/artifactos-studio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artifactos-studio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://artifactos.studio/
- group: commercial
  title: ''
  type: Pricing
  url: https://artifactos.studio/precios/
- group: operate
  title: ''
  type: Support
  url: https://artifactos.studio/seguridad/
- group: start
  title: ''
  type: GettingStarted
  url: https://artifactos.studio/como-funciona/
coverage:
  checked: '2026-11-02'
  detail: Public website provides product information but no machine‑readable API specification is published.
  evidence:
  - status: 200
    url: https://artifactos.studio/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Artifactos provides AI agents for insurance producer societies, enabling automated renewal workflows via WhatsApp. The platform offers agents that detect policy expirations, gather quotes from multiple insurers, and draft renewal messages, all approved by the producer before sending. It aims to prevent missed renewals and streamline communication, with features like secure data handling, approval workflows, and exportable records.
image: https://artifactos.studio/opengraph-image-12o0cb?0cbec7e671800af3
layout: provider
modified: '2026-11-01'
name: Artifactos
nav: Providers
network: true
overview: 'Artifactos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Artificial Intelligence, Automation, WhatsApp, and Latin America.


  Artifactos'' developer surface includes pricing, support, getting-started guide, and 5 more developer resources.'
plans:
- name: Artifactos Studio Plans Pricing
  plan_count: 0
  slug: artifactos-studio-plans-pricing
random_paper: 5
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 8.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 4.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Artifactos Studio Domain Security
  slug: artifactos-studio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: artifactos-studio
tags:
- Insurance
- Artificial Intelligence
- Automation
- WhatsApp
- Latin America
website: https://artifactos.studio/
---
