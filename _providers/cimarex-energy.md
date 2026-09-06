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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cimarex-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coterra.com/
- group: company
  title: ''
  type: SuccessorWebsite
  url: https://www.coterra.com/
- group: company
  title: ''
  type: News
  url: https://www.prnewswire.com/news-releases/cabot-oil--gas-and-cimarex-energy-complete-combination-forming-coterra-energy-301389768.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coterra.com/legal-notice/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cimarex-energy-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Cimarex Energy was fully absorbed into Coterra Energy in October 2021 and its own domain is now broken — cimarex.com still resolves through Cloudflare but the origin presents no valid certificate, so every path including the site root answers HTTP 526 rather than redirecting anywhere; no developer/api/docs/data subdomain of cimarex.com resolves in DNS, there is no cimarex GitHub organization, and no first-party package exists on npm or PyPI.
  evidence:
  - status: 526
    url: https://cimarex.com/
  - status: 526
    url: https://cimarex.com/.well-known/api-catalog
  - status: 404
    url: https://www.coterra.com/openapi.json
  - status: 403
    url: https://www.coterra.com/.well-known/security.txt
  - status: 404
    url: https://www.coterra.com/privacy-policy/
  reason: defunct
  state: none
created: '2025-02-21'
description: 'Cimarex Energy was an independent oil and gas exploration and production company headquartered in Denver, Colorado, with operations focused in the Permian Basin and the Mid-Continent. In October 2021 Cimarex Energy combined with Cabot Oil & Gas Corporation to form Coterra Energy (NYSE: CTRA). No public Cimarex-branded developer APIs exist; all current digital channels and any future API offerings are part of Coterra Energy.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cimarex-energy.png
layout: provider
modified: '2026-09-05'
name: Cimarex Energy
nav: Providers
network: true
overview: 'Cimarex Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Defunct, Energy, Merger, Oil and Gas, and Permian Basin.


  Cimarex Energy''s developer surface includes product news and 5 more developer resources.'
press:
- date: '2026-05-25'
  title: Cimarex Energy Co. News and Press Releases
  url: https://www.prnewswire.com/news/cimarex-energy-co./?page=2
- date: '2026-05-25'
  title: 'Devon Energy: An Oil Company With An AI Obsession'
  url: https://seekingalpha.com/article/4856912-devon-energy-an-oil-company-with-an-ai-obsession
- date: '2026-05-25'
  title: Cabot Oil & Gas Corporation and Cimarex Energy have ...
  url: https://www.linkedin.com/posts/coterra-energy_cabot-oil-gas-corporation-and-cimarex-energy-activity-6849697849010077696-IA6p
- date: '2026-05-25'
  title: Kimmeridge Calls for Overhaul at Coterra, Says 2021 ...
  url: https://energynow.com/2025/11/kimmeridge-calls-for-overhaul-at-coterra-says-2021-merger-a-failure/
- date: '2026-05-25'
  title: OAG Analytics Announces Strategic Partnership with Cimarex ...
  url: https://www.prnewswire.com/news-releases/oag-analytics-announces-strategic-partnership-with-cimarex-energy-300890540.html
random_paper: 12
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.7
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cimarex-energy/refs/heads/main/screenshots/cimarex-energy-2026-06-20T174342.png
security:
- kind: domain-security
  name: Cimarex Energy Domain Security
  slug: cimarex-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cimarex-energy
tags:
- Defunct
- Energy
- Merger
- Oil and Gas
- Permian Basin
- Fortune 1000
website: https://www.coterra.com/
---
