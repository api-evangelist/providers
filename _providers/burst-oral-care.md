---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/burst-oral-care/refs/heads/main/llms/burst-oral-care-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/burst-oral-care-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/burst-oral-care/refs/heads/main/well-known/burst-oral-care-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/burst-oral-care-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/burst-oral-care/refs/heads/main/hosts/burst-oral-care-hosts.yml
  title: ''
  type: Hosts
  url: hosts/burst-oral-care-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/burst-oral-care/refs/heads/main/vendors/burst-oral-care-vendors.yml
  title: ''
  type: Vendors
  url: vendors/burst-oral-care-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://burstoralcare.com/pages/terms-of-use
- group: start
  title: ''
  type: SignUp
  url: https://burstoralcare.com/pages/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://burstoralcare.com/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://burstoralcare.com/pages/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/burst-oral-care/refs/heads/main/security/burst-oral-care-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/burst-oral-care-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://burstoralcare.com/
coverage:
  checked: '2026-10-06'
  detail: Burst Oral Care provides only an e‑commerce storefront with no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://burstoralcare.com/
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Burst Oral Care is a consumer oral‑care brand offering a range of electric toothbrushes, accessories, and oral‑health products. Backed by dental professionals, the company focuses on high‑quality design, innovative technology, and subscription‑based brush‑head replacement. Their e‑commerce site provides detailed product information, customer support, and a blog on oral health.
image: http://burstoralcare.com/cdn/shop/files/BURST_Social_Share_image.png?v=1790086938
layout: provider
modified: '2026-10-06'
name: Burst Oral Care
nav: Providers
network: true
overview: 'Burst Oral Care is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Oral Care, Consumer Goods, Health, and E-Commerce.


  Burst Oral Care''s developer surface includes signup flow and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
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
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Burst Oral Care Domain Security
  slug: burst-oral-care-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: burst-oral-care
tags:
- Company
- Oral Care
- Consumer Goods
- Health
- E-Commerce
website: https://burstoralcare.com/
---
