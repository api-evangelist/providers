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
  href: https://artifacts.apis.io/neysa/plans/neysa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/neysa-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/neysa/llms/neysa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/neysa-llms.txt
- group: other
  href: https://artifacts.apis.io/neysa/hosts/neysa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/neysa-hosts.yml
- group: other
  href: https://artifacts.apis.io/neysa/vendors/neysa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/neysa-vendors.yml
- group: auth
  href: https://artifacts.apis.io/neysa/security/neysa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/neysa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://neysa.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://neysa.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://neysa.ai/pricing/
- group: company
  title: ''
  type: Blog
  url: https://neysa.ai/blogs/
- group: company
  title: ''
  type: AboutUs
  url: https://neysa.ai/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://neysa.ai/contact-us/
coverage:
  checked: '2026-10-21'
  detail: The provider's website serves HTML pages without machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://neysa.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Neysa is on a mission to democratise AI and machine‑learning technologies at scale for enterprises, offering a high‑performance GPU‑accelerated cloud platform, managed MLOps, and AI‑native services. Their Velocis platform provides scalable inference and training, a marketplace for AI applications, and security features like the Aegis LLM Shield. Serving banking, insurance, e‑commerce, manufacturing and more, Neysa aims to simplify AI infrastructure and compete with major cloud providers.
image: https://neysa.ai/wp-content/uploads/2025/06/neysa-1024x498.png
layout: provider
modified: '2026-10-21'
name: Neysa
nav: Providers
network: true
overview: 'Neysa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Cloud, GPU, and MLOps.


  Neysa''s developer surface includes documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Neysa Plans Pricing
  plan_count: 22
  slug: neysa-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 14.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/neysa/neysa-2026-11-03T140208.png
security:
- kind: domain-security
  name: Neysa Domain Security
  slug: neysa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: neysa
tags:
- Company
- Artificial Intelligence
- Cloud
- GPU
- MLOps
website: https://neysa.ai/
---
