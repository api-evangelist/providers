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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/berrystreetafa3/refs/heads/main/vendors/berrystreetafa3-vendors.yml
  title: ''
  type: Vendors
  url: vendors/berrystreetafa3-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/berrystreetafa3/refs/heads/main/llms/berrystreetafa3-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/berrystreetafa3-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/berrystreetafa3/refs/heads/main/well-known/berrystreetafa3-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/berrystreetafa3-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/berrystreetafa3/refs/heads/main/hosts/berrystreetafa3-hosts.yml
  title: ''
  type: Hosts
  url: hosts/berrystreetafa3-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.berrystreet.co/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.berrystreet.co/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.berrystreet.co/berry-street-provider-handbook/new-provider-training/healthie-quick-start-guide
- group: docs
  title: ''
  type: Documentation
  url: https://docs.berrystreet.co/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/berrystreetafa3/refs/heads/main/security/berrystreetafa3-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/berrystreetafa3-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.berrystreet.co
- group: company
  title: ''
  type: Blog
  url: https://www.berrystreet.co/blog
coverage:
  checked: '2026-09-27'
  detail: Documentation is available at https://docs.berrystreet.co/ but no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract was found.
  evidence:
  - status: 200
    url: https://docs.berrystreet.co/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Berry Street provides nutrition therapy services covered by insurance, connecting patients with board‑certified dietitians via an online platform. The company offers personalized diet plans, condition‑specific programs, and enterprise solutions for health providers, aiming to improve health outcomes through evidence‑based nutrition care.
image: https://framerusercontent.com/assets/UmbD9dceSXtVGZev7BzQjRwuydU.png
layout: provider
modified: '2026-09-27'
name: Berrystreetafa3
nav: Providers
network: true
overview: 'Berrystreetafa3 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nutrition, Health Tech, Telehealth, and Dietetics.


  Berrystreetafa3''s developer surface includes getting-started guide, documentation, engineering blog, and 8 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Berrystreetafa3 Domain Security
  slug: berrystreetafa3-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: berrystreetafa3
tags:
- Company
- Nutrition
- Health Tech
- Telehealth
- Dietetics
website: https://www.berrystreet.co
---
