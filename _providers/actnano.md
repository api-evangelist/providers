---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/actnano-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/actnano-llms.txt
- group: company
  title: ''
  type: Website
  url: https://actnano.com/
- group: operate
  title: ''
  type: Support
  url: https://actnano.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://actnano.com/articles/
- group: company
  title: ''
  type: News
  url: https://actnano.com/news/
- group: operate
  title: ''
  type: PressReleases
  url: https://actnano.com/press/
- group: operate
  title: ''
  type: FAQ
  url: https://actnano.com/faq/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://actnano.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://actnano.com/terms-and-conditions/
- group: company
  title: ''
  type: Investors
  url: https://actnano.com/investors/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/advanced-consulting-technologies-inc-/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCva2fDHgJ2fjAd5jdbHKKQw
coverage:
  checked: '2026-08-06'
  detail: actnano manufactures PFAS-free protective nanocoatings for circuit boards — a chemicals and materials product with no software offering; its entire WordPress site is product, safety-data-sheet and press content, and no api./developer./docs./portal. subdomain resolves in DNS.
  evidence:
  - status: 404
    url: https://actnano.com/developers
  - status: 404
    url: https://actnano.com/openapi.json
  - status: 404
    url: https://actnano.com/.well-known/agent-card.json
  - status: 404
    url: https://actnano.com/llms.txt
  - status: 200
    url: https://actnano.com/contact-us/
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'actnano, Inc. is a Massachusetts-based advanced materials company that develops and manufactures PFAS-free protective nanocoatings for electronics. Its flagship Advanced nanoGUARD technology is a gel-state, 100% fluorine-free conformal coating applied to printed circuit board assemblies, connectors, antennas, LEDs and high-heat-generating components, delivering up to IPx8 moisture and condensation protection without trapping heat or degrading signal integrity. Founded in 2012 and headquartered in Cambridge, Massachusetts, with a Munich center of excellence and operations in Mexico and Japan, actnano serves mobility and automotive electronics, consumer electronics, AI and data-center infrastructure, solar, industrial electronics, medical devices and optical anti-fog applications. The company states REACH and RoHS compliance and ISO 9001:2015 certification, and is backed by BMW i Ventures, Porsche Ventures and Emerald Technology Ventures. actnano is a materials manufacturer:
  it publishes no public developer program, API, or machine-readable API contract.'
image: https://actnano.com/wp-content/uploads/2023/03/asset-3-2-x-1-new.png
layout: provider
modified: '2026-08-06'
name: actnano
nav: Providers
network: true
overview: 'actnano is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advanced Materials, Nanotechnology, Coatings, and Electronics Manufacturing.


  actnano''s developer surface includes support, engineering blog, product news, FAQ, YouTube channel, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/actnano/refs/heads/main/screenshots/actnano-2026-08-07T160857.png
security:
- kind: domain-security
  name: Actnano Domain Security
  slug: actnano-domain-security
  summary_line: TLSv1.3
slug: actnano
tags:
- Company
- Advanced Materials
- Nanotechnology
- Coatings
- Electronics Manufacturing
- Automotive
- Consumer Electronics
- Data Center Infrastructure
- Solar
- Medical Devices
- Manufacturing
website: https://actnano.com/
---
