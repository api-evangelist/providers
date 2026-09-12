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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aeremc36d-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aerem.co/
- group: company
  title: ''
  type: Blog
  url: https://www.aerem.co/blog
- group: operate
  title: ''
  type: Support
  url: https://www.aerem.co/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aerem.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aerem.co/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aeremc36d-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/aeremc36d-packages.yml
coverage:
  checked: '2026-09-10'
  detail: 'Aerem ships real software — a Webflow marketing site, Next.js installer and monitoring portals, a B2B marketplace and two mobile apps — but exposes none of it to third parties: there is no developer portal (https://www.aerem.co/developers returns 404), the provider''s own llms.txt indexes every public page and lists no API or developer section, /.well-known/ is a blanket nginx 403 on all six application hosts, and the only backend that answers anonymously, auth.aerem.co, returns the plain string "Server is up and running" with no discovery document.'
  evidence:
  - status: 404
    url: https://www.aerem.co/developers
  - status: 200
    url: https://www.aerem.co/llms.txt
  - status: 404
    url: https://partner.aerem.co/openapi.json
  - status: 403
    url: https://auth.aerem.co/.well-known/openid-configuration
  - status: 404
    url: https://api.github.com/orgs/aerem
  reason: no-developer-program
  state: none
created: '2026-09-10'
description: Aerem is a Mumbai-based "FinTech for CleanTech" group that finances, supplies and monitors rooftop solar in India. The group comprises Aerem Solutions Private Limited, NetZero Finance Private Limited — an RBI-licensed, solar-focused NBFC — and Sunstore Solar Private Limited. Aerem underwrites collateral-free rooftop solar loans for MSMEs and homeowners, provides supply chain finance to solar EPC installers, runs the SunStore B2B solar equipment marketplace, and operates AeROC, an inverter-agnostic remote monitoring portal for installed plants. It also ships two mobile products — the Aerem App for borrowers and the Aerem Partner App for installers — and an AAA (Aerem Asset Assurance) quality-certification programme for EPCs. Aerem publishes a machine-readable llms.txt and five first-party npm packages, but no public API, developer portal or machine-readable API contract of any kind.
image: https://cdn.prod.website-files.com/659794dc6660d7bd9a22884d/69fc574bc9b0245e966fc0ed_754ed9b4063855dc515626105e5540d4_logo-new.svg
layout: provider
modified: '2026-09-10'
name: Aerem
nav: Providers
network: true
overview: 'Aerem is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Lending, Energy, and Solar.


  Aerem''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: Aeremc36D Plans Pricing
  plan_count: 0
  slug: aeremc36d-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Aeremc36D Rate Limits
  slug: aeremc36d-rate-limits
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aeremc36D Domain Security
  slug: aeremc36d-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aeremc36d
tags:
- Company
- Financial Services
- Lending
- Energy
- Solar
- Clean Energy
- Fintech
- Marketplace
- India
- Non-Banking Financial Company
website: https://www.aerem.co/
---
