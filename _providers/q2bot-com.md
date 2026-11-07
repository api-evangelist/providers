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
api_count: 1
apis:
- description: Integration API for WhatsApp Business connecting Tienda Nube stores, enabling order notifications, cart recovery, and AI agent messaging.
  name: Q2 WhatsApp API
  slug: q2-whatsapp-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/q2bot-com/hosts/q2bot-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/q2bot-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/q2bot-com/vendors/q2bot-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/q2bot-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://q2bot.com/tns/tiendanube/privacy.html
- group: auth
  href: https://artifacts.apis.io/q2bot-com/security/q2bot-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/q2bot-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://q2bot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://q2bot.com/tns/
- group: operate
  title: ''
  type: Support
  url: https://wa.me/5491153770458?text=Hola!%20Quiero%20m%C3%A1s%20info%20sobre%20Q2%20WhatsApp%20para%20Tienda%20Nube
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are public HTML but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract was found.
  evidence:
  - status: 200
    url: https://q2bot.com/tns/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Q2bot provides an automated WhatsApp solution for Tienda Nube stores, leveraging the official Meta WhatsApp Business API. The platform sends order notifications, recovers abandoned carts, and offers a 24/7 AI agent for customer inquiries, all without code. It also offers custom software development with AI. Q2bot connects e‑commerce shops to WhatsApp to improve sales and support.
image: https://q2bot.com/tns/ms-icon-310x310.png
layout: provider
modified: '2026-10-30'
name: q2bot-com
nav: Providers
network: true
overview: 'q2bot-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, WhatsApp, Artificial Intelligence, and Automation.


  q2bot-com''s developer surface includes documentation, support, and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/q2bot-com/q2bot-com-2026-11-03T141734.png
security:
- kind: domain-security
  name: Q2Bot Com Domain Security
  slug: q2bot-com-domain-security
  summary_line: TLSv1.3
slug: q2bot-com
tags:
- Company
- E-Commerce
- WhatsApp
- Artificial Intelligence
- Automation
- Tienda Nube
website: https://q2bot.com/
---
