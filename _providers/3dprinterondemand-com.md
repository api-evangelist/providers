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
api_count: 1
apis:
- description: Provides instant pricing quotes for 3D printed parts via a public endpoint.
  name: Instant Quote API
  slug: instant-quote-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/3dprinterondemand-com/plans/3dprinterondemand-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/3dprinterondemand-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/3dprinterondemand-com/llms/3dprinterondemand-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/3dprinterondemand-com-llms.txt
- group: other
  href: https://artifacts.apis.io/3dprinterondemand-com/hosts/3dprinterondemand-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3dprinterondemand-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/3dprinterondemand-com/vendors/3dprinterondemand-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/3dprinterondemand-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://3dprinterondemand.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://3dprinterondemand.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://3dprinterondemand.com/pricing
- group: start
  title: ''
  type: Login
  url: https://3dprinterondemand.com/login
- group: company
  title: ''
  type: Blog
  url: https://3dprinterondemand.com/blog
- group: auth
  href: https://artifacts.apis.io/3dprinterondemand-com/security/3dprinterondemand-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3dprinterondemand-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://3dprinterondemand.com/
coverage:
  checked: '2026-10-31'
  detail: The provider's public website offers documentation but no discoverable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://3dprinterondemand.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 3D Printer on Demand provides an instant quote service for 3D printed parts. Users can upload STL files and receive a flat per-part price without login. The service offers FDM parts made in the USA, handling orders from a single sample up to 10,000 units, with typical shipping in 3 to 5 business days. It targets rapid prototyping and low‑volume manufacturing, delivering quick turnaround and transparent pricing for developers and makers.
image: https://3dprinterondemand.com/opengraph-image.png?opengraph-image.86f4c625.png
layout: provider
modified: '2026-10-31'
name: 3D Printer on Demand
nav: Providers
network: true
overview: '3D Printer on Demand is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D Printing, Instant Quote, and Manufacturing.


  3D Printer on Demand''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: 3Dprinterondemand Com Plans Pricing
  plan_count: 1
  slug: 3dprinterondemand-com-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 19.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 3Dprinterondemand Com Domain Security
  slug: 3dprinterondemand-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 3dprinterondemand-com
tags:
- Company
- 3D Printing
- Instant Quote
- Manufacturing
website: https://3dprinterondemand.com/
---
