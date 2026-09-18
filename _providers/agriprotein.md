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
  scored_at: '2026-09-17'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agriprotein
- group: company
  title: ''
  type: Investors
  url: https://equityzen.com/company/agriprotein
coverage:
  checked: '2026-09-13'
  detail: AgriProtein's parent Insect Technology Group went into administration in February 2021 and the assets were sold that June; agriprotein.com was not renewed and now serves an unrelated online-poker affiliate site, leaving only a 2013-era parked placeholder at agriprotein.co.za where all sixteen discovery paths return 404.
  evidence:
  - status: 200
    url: https://agriprotein.com/
  - status: 200
    url: https://agriprotein.co.za/
  - status: 404
    url: https://agriprotein.co.za/.well-known/api-catalog
  - status: 404
    url: https://agriprotein.co.za/openapi.json
  - status: 404
    url: https://api.github.com/orgs/agriprotein
  - status: 200
    url: https://en.wikipedia.org/wiki/AgriProtein
  reason: defunct
  state: none
created: '2026-09-13'
description: 'AgriProtein was a South African industrial insect-farming company, founded in Cape Town in 2008, that pioneered commercial black soldier fly (Hermetia illucens) bioconversion: it fed organic waste from food factories, supermarkets, farms and restaurants to fly larvae and processed the result into MagMeal insect protein for aquaculture, poultry and pet food, MagOil, and MagSoil soil conditioner. It opened the world''s first full-scale BSF facility in Philippi, Cape Town in 2014 and raised USD 105 million in 2018 to build out a global factory network. Its UK parent, Insect Technology Group, entered administration in February 2021 and the group''s assets, intellectual property and plant were sold in June 2021. The company is defunct; it published no developer program, API, or machine-readable specification, and the agriprotein.com domain has since lapsed to an unrelated operator.'
layout: provider
modified: '2026-09-13'
name: Agriprotein
nav: Providers
network: true
overview: Agriprotein is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Animal Feed, Insect Protein, and Sustainability.
random_paper: 0
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 4.6
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: agriprotein
tags:
- Company
- Agriculture
- Animal Feed
- Insect Protein
- Sustainability
- Waste Management
- Biotechnology
---
