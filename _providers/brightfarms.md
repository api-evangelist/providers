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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brightfarms/refs/heads/main/hosts/brightfarms-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brightfarms-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brightfarms/refs/heads/main/vendors/brightfarms-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brightfarms-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brightfarms/refs/heads/main/security/brightfarms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brightfarms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brightfarms.com
- group: company
  title: ''
  type: AboutUs
  url: https://www.brightfarms.com/about-us/
- group: other
  title: ''
  type: Farms
  url: https://www.brightfarms.com/farms/
- group: other
  title: ''
  type: Products
  url: https://www.brightfarms.com/products/
- group: other
  title: ''
  type: StoreLocator
  url: https://www.brightfarms.com/storelocator/
- group: learn
  title: ''
  type: Recipes
  url: https://www.brightfarms.com/salad-recipes/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brightfarms.com/privacy-policy/
- group: company
  title: ''
  type: Press
  url: https://www.brightfarms.com/press/
- group: operate
  title: ''
  type: Contact
  url: https://www.brightfarms.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://www.brightfarms.com/faq/
coverage:
  checked: '2026-10-06'
  detail: BrightFarms website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.brightfarms.com
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: BrightFarms grows fresh, pesticide‑free greens in indoor farms across the United States, delivering crisp lettuce and salads directly to grocery stores within a day of harvest. The company emphasizes sustainable agriculture, using less water and land while eliminating pesticides, herbicides, and fungicides. Their mission is to create a new generation of farming that benefits the planet and consumers, offering year‑round produce regardless of weather or season.
image: https://www.brightfarms.com/wp-content/uploads/2024/06/Image-Still.jpg
layout: provider
modified: '2026-10-06'
name: BrightFarms
nav: Providers
network: true
overview: 'BrightFarms is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Sustainability, FreshProduce, and IndoorFarming.


  BrightFarms'' developer surface includes FAQ and 12 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brightfarms Domain Security
  slug: brightfarms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brightfarms
tags:
- Company
- Agriculture
- Sustainability
- FreshProduce
- IndoorFarming
website: https://www.brightfarms.com
---
