---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magnusmetal-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/magnusmetal-llms.txt
- group: company
  title: ''
  type: Website
  url: https://magnusmetal.com/
- group: company
  title: ''
  type: About
  url: https://magnusmetal.com/about/
- group: operate
  title: ''
  type: Support
  url: https://magnusmetal.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://magnusmetal.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://magnusmetal.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://magnusmetal.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/magnusmetal/
coverage:
  checked: '2026-08-25'
  detail: Magnus Metal manufactures metal castings and Digital Casting machines; its entire public web presence is six WordPress pages plus job listings, with no developer, docs or API section anywhere in its sitemap, and api./docs./developer.magnusmetal.com do not resolve in DNS.
  evidence:
  - status: 200
    url: https://magnusmetal.com/
  - status: 200
    url: https://magnusmetal.com/page-sitemap.xml
  - status: 404
    url: https://magnusmetal.com/openapi.json
  - status: 404
    url: https://magnusmetal.com/.well-known/agent-card.json
  - status: 404
    url: https://magnusmetal.com/docs
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'Magnus Metal (MagnusMetal Ltd.) is an Israeli advanced-manufacturing company bringing metal casting into the Industry 4.0 era with its patent-pending Digital Casting System. Founded in 2017 and headquartered at the Revadim Industrial Park in Kibbutz Revadim, Israel, the company builds machines that combine additive-manufacturing and casting principles: a slicer designs a ceramic mold layer by layer and solid alloy is deposited into each layer, so parts are produced from widely available solid metals rather than powders and with no hard tooling. The company markets the process for powertrains, engines, industrial machinery and structural components, claiming removal of 6-18 weeks of tooling lead time, up to 70% raw-material savings and roughly 50% lower energy use. Magnus Metal is a hardware and materials manufacturer - it sells castings and casting systems, not software - and publishes no public developer program, API, SDK or machine-readable contract of any kind.'
image: https://magnusmetal.com/wp-content/uploads/2023/01/Magnus-Elements_02_layers_04_00000.jpg
layout: provider
modified: '2026-08-25'
name: MagnusMetal
nav: Providers
network: true
overview: 'MagnusMetal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Advanced Manufacturing, Metal Casting, and Additive Manufacturing.


  MagnusMetal''s developer surface includes support and 8 more developer resources.'
plans:
- name: Magnusmetal Plans Pricing
  plan_count: 0
  slug: magnusmetal-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Magnusmetal Rate Limits
  slug: magnusmetal-rate-limits
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magnusmetal/refs/heads/main/screenshots/magnusmetal-2026-09-02T150402.png
security:
- kind: domain-security
  name: Magnusmetal Domain Security
  slug: magnusmetal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: magnusmetal
tags:
- Company
- Manufacturing
- Advanced Manufacturing
- Metal Casting
- Additive Manufacturing
- Industrial
- Materials
- Hardware
- Industry 4.0
- Israel
website: https://magnusmetal.com/
---
