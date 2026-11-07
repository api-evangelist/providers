---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/send4-com-br/plans/send4-com-br-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/send4-com-br-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/send4-com-br/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/send4-com-br/llms/send4-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/send4-com-br-llms.txt
- group: other
  href: https://artifacts.apis.io/send4-com-br/hosts/send4-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/send4-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/send4-com-br/vendors/send4-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/send4-com-br-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://send4.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://send4.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://send4.ai/pricing
- group: auth
  href: https://artifacts.apis.io/send4-com-br/security/send4-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/send4-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://send4.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://send4.ai
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Send4 Tecnologia provides a platform that automates lead qualification via SMS and chat, instantly answering inbound inquiries and routing qualified leads into CRM systems such as HubSpot, Pipedrive, and Zapier. The service integrates with popular tools, offers a 14‑day free trial, and aims to accelerate sales pipelines for businesses in Brazil and globally. Founded with backing from 500‑global, Send4 focuses on AI‑driven conversational automation to improve response times and conversion rates.
image: https://send4.ai/og-image.png
layout: provider
modified: '2026-10-21'
name: Send4 Tecnologia
nav: Providers
network: true
overview: 'Send4 Tecnologia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lead Qualification, SMS, Chatbots, and CRM Integration.


  Send4 Tecnologia''s developer surface includes pricing and 9 more developer resources.'
plans:
- name: Send4 Com Br Plans Pricing
  plan_count: 3
  slug: send4-com-br-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.0
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/send4-com-br/send4-com-br-2026-11-03T143015.png
security:
- kind: domain-security
  name: Send4 Com Br Domain Security
  slug: send4-com-br-domain-security
  summary_line: TLSv1.3 · DMARC
slug: send4-com-br
tags:
- Company
- Lead Qualification
- SMS
- Chatbots
- CRM Integration
- Artificial Intelligence
website: https://send4.ai
---
