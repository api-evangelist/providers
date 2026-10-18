---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/centre-for-sight/refs/heads/main/plans/centre-for-sight-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/centre-for-sight-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/centre-for-sight/refs/heads/main/llms/centre-for-sight-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/centre-for-sight-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/centre-for-sight/refs/heads/main/well-known/centre-for-sight-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/centre-for-sight-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centre-for-sight/refs/heads/main/hosts/centre-for-sight-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centre-for-sight-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centre-for-sight/refs/heads/main/vendors/centre-for-sight-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centre-for-sight-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.centreforsight.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.centreforsight.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.centreforsight.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.centreforsight.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centre-for-sight/refs/heads/main/security/centre-for-sight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centre-for-sight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.centreforsight.com
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://www.centreforsight.com/mcp
  - status: 200
    url: https://www.centreforsight.com
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: partner-login
  state: gated
created: '2026-10-07'
description: Centre For Sight is a UK‑based private eye‑care provider offering premium laser eye surgery, cataract surgery, glaucoma treatments and a wide range of ophthalmology services across multiple locations. Established in 1996, it operates over 95 centres in the UK and internationally, delivering advanced technology and specialist care to patients. The organisation also runs a charitable trust supporting eye health initiatives.
layout: provider
modified: '2026-10-07'
name: Centre for Sight
nav: Providers
network: true
overview: 'Centre for Sight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Ophthalmology, EyeCare, Medical, and United Kingdom.


  Centre for Sight''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Centre For Sight Plans Pricing
  plan_count: 17
  slug: centre-for-sight-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Centre For Sight Domain Security
  slug: centre-for-sight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: centre-for-sight
tags:
- Healthcare
- Ophthalmology
- EyeCare
- Medical
- United Kingdom
website: https://www.centreforsight.com
---
