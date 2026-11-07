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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/agencyai-app/plans/agencyai-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agencyai-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/agencyai-app/llms/agencyai-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agencyai-app-llms.txt
- group: other
  href: https://artifacts.apis.io/agencyai-app/hosts/agencyai-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agencyai-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/agencyai-app/vendors/agencyai-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agencyai-app-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://agencyai.app/security
- group: auth
  href: https://artifacts.apis.io/agencyai-app/security/agencyai-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agencyai-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agencyai.app/
- group: docs
  title: ''
  type: Documentation
  url: https://agencyai.app/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://agencyai.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://agencyai.app/blog
- group: operate
  title: ''
  type: Support
  url: https://support.agencyai.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agencyai.app/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agencyai.app/privacy-policy
coverage:
  checked: '2026-10-31'
  detail: The provider's documentation page https://agencyai.app/mcp returns HTML but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://agencyai.app/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Agency AI provides an AI‑powered platform that automates Meta and Google advertising for Shopify merchants. Built by operators who have scaled Shopify stores into the top 0.1% of merchants, the service offers a creative studio, campaign automation, and real‑time optimization, aiming to keep margins high while removing the need for a retainer. It integrates Claude and ChatGPT for ad copy generation and supports a free trial with no credit‑card required.
image: https://agencyai.app/assets/og/default.png
layout: provider
modified: '2026-10-31'
name: Agency AI
nav: Providers
network: true
overview: 'Agency AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Advertising, Shopify, Automation, and Marketing.


  Agency AI''s developer surface includes documentation, pricing, engineering blog, support, and 9 more developer resources.'
plans:
- name: Agencyai App Plans Pricing
  plan_count: 2
  slug: agencyai-app-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 19.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agencyai App Domain Security
  slug: agencyai-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agencyai-app
tags:
- Artificial Intelligence
- Advertising
- Shopify
- Automation
- Marketing
website: https://agencyai.app/
---
