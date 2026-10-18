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
  href: https://raw.githubusercontent.com/api-evangelist/compareaimodels/refs/heads/main/plans/compareaimodels-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/compareaimodels-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/compareaimodels/refs/heads/main/hosts/compareaimodels-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compareaimodels-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/compareaimodels/refs/heads/main/vendors/compareaimodels-vendors.yml
  title: ''
  type: Vendors
  url: vendors/compareaimodels-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.comparemodels.ai/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://www.comparemodels.ai/pricing
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/compareaimodels/refs/heads/main/security/compareaimodels-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compareaimodels-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.comparemodels.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.comparemodels.ai/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Compare AI Models provides a platform to compare AI language models side‑by‑side, offering insights into capabilities, pricing, token limits, and performance. Users can test models like GPT‑4, LLaMA, Claude and others in a unified interface, helping developers and businesses choose the best model for their needs while saving time and costs.
image: https://www.comparemodels.ai/og-image.png
layout: provider
modified: '2026-10-16'
name: Compare AI Models
nav: Providers
network: true
overview: 'Compare AI Models is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Comparison, Platform, and LanguageModels.


  Compare AI Models'' developer surface includes signup flow, pricing, and 5 more developer resources.'
plans:
- name: Compareaimodels Plans Pricing
  plan_count: 2
  slug: compareaimodels-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Compareaimodels Domain Security
  slug: compareaimodels-domain-security
  summary_line: TLSv1.3 · HSTS
slug: compareaimodels
tags:
- Company
- Artificial Intelligence
- Comparison
- Platform
- LanguageModels
website: https://www.comparemodels.ai/
---
