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
  href: https://raw.githubusercontent.com/api-evangelist/chimney-trail-health/refs/heads/main/plans/chimney-trail-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chimney-trail-health-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chimney-trail-health/refs/heads/main/llms/chimney-trail-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chimney-trail-health-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chimney-trail-health/refs/heads/main/hosts/chimney-trail-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chimney-trail-health-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chimney-trail-health/refs/heads/main/vendors/chimney-trail-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chimney-trail-health-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chimneytrailhealth.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.chimneytrailhealth.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chimney-trail-health/refs/heads/main/security/chimney-trail-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chimney-trail-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chimneytrailhealth.com/
coverage:
  checked: '2026-10-08'
  detail: No machine‑readable API specification was found on the provider's documented sites.
  evidence:
  - status: 200
    url: https://portal.chimneytrailhealth.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Chimney Trail Health provides evidence‑based mental health and cognitive‑defense training for high‑pressure environments. Their programs serve U.S. military, corporate teams, and elite performers, offering in‑person training, self‑led tools, and scalable solutions backed by scientific research. The company focuses on building resilience, improving psychological literacy, and delivering measurable performance benefits for organizations facing critical challenges.
image: https://static.wixstatic.com/media/0c176e_dde84e70c3e440c8a277c2c5501e0ca6~mv2.png/v1/fill/w_1000,h_500,al_c/0c176e_dde84e70c3e440c8a277c2c5501e0ca6~mv2.png
layout: provider
modified: '2026-10-08'
name: Chimney Trail Health
nav: Providers
network: true
overview: 'Chimney Trail Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mental Health, Training, Military, and Corporate.


  Chimney Trail Health''s developer surface includes pricing and 7 more developer resources.'
plans:
- name: Chimney Trail Health Plans Pricing
  plan_count: 1
  slug: chimney-trail-health-plans-pricing
random_paper: 7
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chimney Trail Health Domain Security
  slug: chimney-trail-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chimney-trail-health
tags:
- Company
- Mental Health
- Training
- Military
- Corporate
- Resilience
website: https://www.chimneytrailhealth.com/
---
