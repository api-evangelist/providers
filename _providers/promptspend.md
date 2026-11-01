---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/promptspend/llms/promptspend-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/promptspend-llms.txt
- group: other
  href: https://artifacts.apis.io/promptspend/hosts/promptspend-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptspend-hosts.yml
- group: other
  href: https://artifacts.apis.io/promptspend/vendors/promptspend-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptspend-vendors.yml
- group: auth
  href: https://artifacts.apis.io/promptspend/security/promptspend-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptspend-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptspend.com/
- group: docs
  title: ''
  type: Documentation
  url: https://promptspend.com/
- group: operate
  title: ''
  type: Support
  url: https://promptspend.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://promptspend.com/privacy/
coverage:
  checked: '2026-10-18'
  detail: PromptSpend provides no publicly accessible machine‑readable API specification; attempts to fetch common spec URLs returned 404 or empty responses.
  evidence:
  - status: 200
    url: https://promptspend.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: PromptSpend provides an LLM API cost calculator that helps developers estimate and compare expenses across 84 AI models, including OpenAI, Anthropic, Google, DeepSeek, and Moonshot. The web app offers a simple interface to paste prompts, view pricing details refreshed daily, and understand billing implications for various usage scenarios, supporting both GPT and Claude models.
image: https://promptspend.com/social-card.png?v=a0fd6116
layout: provider
modified: '2026-10-18'
name: PromptSpend
nav: Providers
network: true
overview: 'PromptSpend is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LLM, Cost Calculator, Artificial Intelligence, and Software-as-a-Service.


  PromptSpend''s developer surface includes documentation, support, and 6 more developer resources.'
plans:
- name: Promptspend Plans Pricing
  plan_count: 0
  slug: promptspend-plans-pricing
random_paper: 12
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Promptspend Domain Security
  slug: promptspend-domain-security
  summary_line: TLSv1.3 · DMARC
slug: promptspend
tags:
- Company
- LLM
- Cost Calculator
- Artificial Intelligence
- Software-as-a-Service
website: https://promptspend.com/
---
