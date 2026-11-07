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
- group: commercial
  href: https://artifacts.apis.io/blocktrust-tech/plans/blocktrust-tech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blocktrust-tech-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/blocktrust-tech/hosts/blocktrust-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blocktrust-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/blocktrust-tech/vendors/blocktrust-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blocktrust-tech-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blocktrust.tech/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://blocktrust.tech/pricing
- group: start
  title: ''
  type: Login
  url: https://blocktrust.tech/auth/signin
- group: auth
  href: https://artifacts.apis.io/blocktrust-tech/security/blocktrust-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blocktrust-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blocktrust.tech/
coverage:
  checked: '2026-11-02'
  detail: Provider's website serves HTML pages rendered by JavaScript, with no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract discovered.
  evidence:
  - status: 200
    url: https://blocktrust.tech/pricing
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: BLOCKTRUST provides a French digital identity certification solution that protects against identity theft and phishing. Leveraging blockchain on Polygon, it offers monthly subscription plans, customizable verification tools, and compliance with European data protection standards. The platform enables businesses and individuals to securely verify identities, reduce fraud, and integrate trusted digital credentials into their services.
image: https://blocktrust.tech/opengraph-image.png?3d8b2a1fdcf8777b
layout: provider
modified: '2026-11-02'
name: BLOCKTRUST
nav: Providers
network: true
overview: 'BLOCKTRUST is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, B2B, Freelance, E-Commerce, and Trust Monitoring.


  BLOCKTRUST''s developer surface includes pricing and 7 more developer resources.'
plans:
- name: Blocktrust Tech Plans Pricing
  plan_count: 4
  slug: blocktrust-tech-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blocktrust Tech Domain Security
  slug: blocktrust-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blocktrust-tech
tags:
- Blockchain
- B2B
- Freelance
- E-Commerce
- Trust Monitoring
website: https://blocktrust.tech/
---
