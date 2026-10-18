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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/carbon-lighthouse/refs/heads/main/plans/carbon-lighthouse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carbon-lighthouse-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbon-lighthouse/refs/heads/main/hosts/carbon-lighthouse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbon-lighthouse-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbon-lighthouse/refs/heads/main/vendors/carbon-lighthouse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbon-lighthouse-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.centinelre.com/legal/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://app.centinelre.com/accounts/signup/?next=%2F
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.centinelre.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.centinelre.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.centinelre.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.centinelre.com/team
- group: company
  title: ''
  type: Blog
  url: https://www.centinelre.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbon-lighthouse/refs/heads/main/security/carbon-lighthouse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbon-lighthouse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.centinelre.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.centinelre.com/
  - status: 403
    url: https://forgeglobal.com/carbon-lighthouse_stock/
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Carbon Lighthouse provides energy efficiency and decarbonization services for commercial real‑estate owners and operators. By combining data analytics, engineering expertise, and a performance‑based financing model, they identify and implement measures that reduce building energy consumption and carbon emissions, delivering measurable savings and sustainability outcomes for their clients.
image: https://cdn.prod.website-files.com/686411936593eb0b8567528d/686d47cbb1015d6354512185_Logo%20Positive%20Transparent%202.png
layout: provider
modified: '2026-10-07'
name: Carbon Lighthouse
nav: Providers
network: true
overview: 'Carbon Lighthouse is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Carbon Lighthouse''s developer surface includes signup flow, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Carbon Lighthouse Plans Pricing
  plan_count: 3
  slug: carbon-lighthouse-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 42.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbon Lighthouse Domain Security
  slug: carbon-lighthouse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbon-lighthouse
tags:
- Company
website: https://www.centinelre.com/
---
