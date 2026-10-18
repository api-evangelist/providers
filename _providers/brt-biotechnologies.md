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
  href: https://raw.githubusercontent.com/api-evangelist/brt-biotechnologies/refs/heads/main/plans/brt-biotechnologies-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brt-biotechnologies-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brt-biotechnologies/refs/heads/main/hosts/brt-biotechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brt-biotechnologies-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://brtbio.com/archive/pricing
- group: company
  title: ''
  type: Blog
  url: https://brtbio.com/archive/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brt-biotechnologies/refs/heads/main/security/brt-biotechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brt-biotechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brtbio.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://brtbio.com
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: BRT Biotechnologies advances drug discovery by providing high-quality macrocycle libraries that enable rapid identification of promising drug leads. Their platform accelerates the creation of diverse macrocycles, unlocking new possibilities for treating hard‑to‑drug targets and precision therapeutics.
image: https://framerusercontent.com/assets/4vpajD3S35ibe4wPWghPgtyiS7A.png
layout: provider
modified: '2026-10-06'
name: BRT Biotechnologies
nav: Providers
network: true
overview: 'BRT Biotechnologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Drug Discovery, Macrocycles, Therapeutics, and Company.


  BRT Biotechnologies'' developer surface includes pricing, engineering blog, and 4 more developer resources.'
plans:
- name: Brt Biotechnologies Plans Pricing
  plan_count: 3
  slug: brt-biotechnologies-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brt Biotechnologies Domain Security
  slug: brt-biotechnologies-domain-security
  summary_line: TLSv1.3 · HSTS
slug: brt-biotechnologies
tags:
- Biotechnology
- Drug Discovery
- Macrocycles
- Therapeutics
- Company
website: https://brtbio.com
---
