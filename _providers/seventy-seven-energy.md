---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seventy-seven-energy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/seventy-seven-energy
coverage:
  checked: '2026-08-29'
  detail: Seventy Seven Energy was fully absorbed by Patterson-UTI Energy on 20 April 2017 and has published nothing since; its own domain seventysevenenergy.com is now NXDOMAIN, and the seventy-seven-energy.com host this profile had been pointing at is an unrelated Wix domain registered in January 2024 that has never been deployed and answers every path, including the root and all seven /.well-known/ paths, with a "ConnectYourDomain Error" 404.
  evidence:
  - status: 404
    url: https://www.seventy-seven-energy.com/
  - status: 404
    url: https://www.seventy-seven-energy.com/.well-known/security.txt
  - status: 404
    url: https://www.seventy-seven-energy.com/.well-known/agent-card.json
  - status: 404
    url: https://www.seventy-seven-energy.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/seventy-seven-energy
  - status: 200
    url: https://www.prnewswire.com/news-releases/patterson-uti-energy-completes-merger-with-seventy-seven-energy-300443089.html
  reason: defunct
  state: none
created: '2026-03-24'
description: Seventy Seven Energy Inc. was a diversified oilfield services company headquartered in Oklahoma City, providing wellsite services and equipment to U.S. land-based oil and natural gas exploration and production customers. It was formed in 2011 out of Chesapeake Energy's oilfield services arm and spun off as an independent public company, operating through affiliates including Nomac Drilling (contract land drilling), Performance Technologies (hydraulic fracturing and pressure pumping) and Great Plains Oilfield Rental (rental tools and equipment). After the 2014-2016 oil price collapse it completed a prepackaged Chapter 11 restructuring and recapitalization, emerging in August 2016. THE COMPANY NO LONGER EXISTS. Patterson-UTI Energy completed its merger with Seventy Seven Energy on 20 April 2017 in a transaction valued at roughly USD 1.76 billion, issuing about 47.5 million shares and repaying USD 472 million of Seventy Seven Energy debt at closing; Nomac was absorbed into Patterson-UTI
  Drilling and Performance Technologies into Universal Pressure Pumping. Seventy Seven Energy never operated a public developer program, API, SDK, or machine-readable specification of any kind, and there is no surviving entity to publish one — its own domain, seventysevenenergy.com, no longer resolves.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seventy-seven-energy.png
layout: provider
modified: '2026-08-29'
name: Seventy Seven Energy
nav: Providers
network: true
overview: Seventy Seven Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Oil and Gas, Oilfield Services, and Drilling.
press:
- date: '2026-05-25'
  title: Seventy Seven Energy reports $74.7 million loss for quarter
  url: https://journalrecord.com/2015/07/29/seventy-seven-energy-reports-74-7-million-loss-for-quarter-energy/
- date: '2026-05-25'
  title: Seventy Seven Energy emerges from bankruptcy
  url: https://journalrecord.com/2016/08/01/seventy-seven-energy-emerges-from-bankruptcy/
- date: '2026-05-25'
  title: Sheri Pollock - Dallas-Fort Worth Metroplex
  url: https://www.linkedin.com/in/sheri-pollock-29b57b3
- date: '2026-05-25'
  title: Patterson-UTI Buys Seventy Seven Energy In Near-$2B Deal
  url: https://www.law360.com/articles/871959/patterson-uti-buys-seventy-seven-energy-in-near-2b-deal
- date: '2026-05-25'
  title: Oklahoma Department of Agriculture, Food and Forestry
  url: https://www.facebook.com/OklahomaAg/posts/-internship-opportunity-we-are-looking-for-a-qualified-collegiate-student-to-joi/1277918744369735/
random_paper: 9
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Seventy Seven Energy Domain Security
  slug: seventy-seven-energy-domain-security
  summary_line: TLSv1.3
slug: seventy-seven-energy
tags:
- Company
- Energy
- Oil and Gas
- Oilfield Services
- Drilling
- Pressure Pumping
- Equipment Rental
- Oklahoma
- United States
- Acquired
- Defunct
---
