---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
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
    agent_skills: unknown
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
  score: 6.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/waply-online/plans/waply-online-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/waply-online-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/waply-online/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/waply-online/llms/waply-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/waply-online-llms.txt
- group: agent
  href: https://artifacts.apis.io/waply-online/well-known/waply-online-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/waply-online-well-known.yml
- group: other
  href: https://artifacts.apis.io/waply-online/hosts/waply-online-hosts.yml
  title: ''
  type: Hosts
  url: hosts/waply-online-hosts.yml
- group: other
  href: https://artifacts.apis.io/waply-online/vendors/waply-online-vendors.yml
  title: ''
  type: Vendors
  url: vendors/waply-online-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://waply.online/en/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://waply.online/en/privacy
- group: auth
  href: https://artifacts.apis.io/waply-online/security/waply-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/waply-online-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://waply.online/
- group: docs
  title: ''
  type: Documentation
  url: https://waply.online/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://waply.online/pricing/calculator/
- group: start
  title: ''
  type: GettingStarted
  url: https://waply.online/what-is-waply/
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://waply.online/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Waply Online provides a WhatsApp integration platform tailored for Kommo CRM, enabling businesses to send messages, make calls, and deploy AI-driven voice agents directly through WhatsApp. The service offers tools for agencies and enterprises across various industries, including retail, education, healthcare, and automotive, with customizable solutions, pricing calculators, and extensive documentation to streamline communication workflows.
image: https://waply.online/social.png
layout: provider
modified: '2026-10-31'
name: waply-online
nav: Providers
network: true
overview: 'waply-online is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WhatsApp, Artificial Intelligence, Voice, and Integration.


  waply-online''s developer surface includes support, documentation, pricing, getting-started guide, and 9 more developer resources.'
plans:
- name: Waply Online Plans Pricing
  plan_count: 1
  slug: waply-online-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.5
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 18.9
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Waply Online Domain Security
  slug: waply-online-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: waply-meta-calculator
  slug: waply-meta-calculator
slug: waply-online
tags:
- Company
- WhatsApp
- Artificial Intelligence
- Voice
- Integration
website: https://waply.online/
---
