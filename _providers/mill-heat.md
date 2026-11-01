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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://millnorway.com/cvd-policy
- group: design
  href: https://artifacts.apis.io/mill-heat/conformance/mill-heat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mill-heat-conformance.yml
- group: auth
  href: https://artifacts.apis.io/mill-heat/well-known/mill-heat-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mill-heat-security.txt
- group: auth
  href: https://artifacts.apis.io/mill-heat/well-known/mill-heat-intercom-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mill-heat-intercom-help-security.txt
- group: agent
  href: https://artifacts.apis.io/mill-heat/well-known/mill-heat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mill-heat-well-known.yml
- group: other
  href: https://artifacts.apis.io/mill-heat/hosts/mill-heat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mill-heat-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://millnorway.com/news/
- group: auth
  href: https://artifacts.apis.io/mill-heat/security/mill-heat-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mill-heat-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mill-heat/security/mill-heat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mill-heat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://millnorway.com/
- group: operate
  title: ''
  type: Support
  url: https://intercom-help.eu/mill-norway/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://millnorway.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://millnorway.com/terms-of-use/
coverage:
  checked: '2026-10-28'
  detail: The Mill website provides documentation but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://millnorway.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Mill is a Norwegian company designing smart and beautiful heating and indoor climate products. It creates modern, minimalist heating solutions that blend Scandinavian design elegance with functional comfort. The company emphasizes sustainable indoor climate control, offering aesthetically pleasing heaters that integrate seamlessly into homes. Mill focuses on innovative, energy-efficient technology to provide reliable warmth while maintaining a sleek, contemporary look.
layout: provider
modified: '2026-10-28'
name: Mill (heaters)
nav: Providers
network: true
overview: 'Mill (heaters) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Heating, IoT, ScandinavianDesign, and EnergyEfficiency.


  Mill (heaters)''s developer surface includes support and 12 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 46.4
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - norway
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mill Heat Domain Security
  slug: mill-heat-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mill Heat Vulnerability Disclosure
  slug: mill-heat-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mill-heat
tags:
- Company
- Heating
- IoT
- ScandinavianDesign
- EnergyEfficiency
website: https://millnorway.com/
---
