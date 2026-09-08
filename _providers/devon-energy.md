---
access_model:
  confidence: high
  label: No public API surface — nothing to onboard to
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.devonenergy.com'', ''status'': 200, ''note'': ''live corporate site; no developer, API or documentation section in the navigation (probed 2026-09-06)''}'
  - '{''url'': ''https://www.devonenergy.com/openapi.json'', ''status'': 404, ''note'': ''no OpenAPI on the corporate host''}'
  - '{''url'': ''https://github.com/devonenergy'', ''status'': 200, ''note'': ''GitHub organization exists but publishes zero public repositories''}'
  - '{''url'': ''https://www.devon-energy.com'', ''status'': 302, ''note'': ''the previously-recorded website was a lapsed domain redirecting to hugedomains.com; corrected to www.devonenergy.com (roadmap#169, roadmap#250)''}'
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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.devonenergy.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/devonenergy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/devon-energy
- group: company
  title: ''
  type: Blog
  url: https://www.devonenergy.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.devonenergy.com/about-us/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.devonenergy.com/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/devon-energy-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/devon-energy-llms.txt
coverage:
  checked: '2026-09-06'
  detail: Devon Energy is an independent oil and gas exploration and production company; its corporate site has no developer, API or documentation section, no api./developer./data. subdomain of devonenergy.com resolves in DNS, every OpenAPI/GraphQL/AsyncAPI path 404s on www.devonenergy.com, and its GitHub organization publishes zero public repositories — the interest-owner and supplier surfaces it does link to are third-party platforms (EnergyLink, Enverus OpenInvoice) rather than Devon-operated APIs.
  evidence:
  - status: 200
    url: https://www.devonenergy.com
  - status: 404
    url: https://www.devonenergy.com/openapi.json
  - status: 404
    url: https://www.devonenergy.com/developers
  - status: 404
    url: https://www.devonenergy.com/.well-known/api-catalog
  - status: 200
    url: https://api.github.com/orgs/devonenergy/repos
  reason: not-a-software-company
  state: none
created: '2026-03-21'
description: 'Devon Energy Corporation (NYSE: DVN) is an independent oil and natural gas exploration and production company operating across U.S. onshore basins, anchored by a leading position in the economic core of the Delaware Basin. On May 7, 2026 Devon completed an all-stock merger with Coterra Energy, creating a large-cap shale operator with an estimated combined enterprise value of about $58 billion; the combined company retains the Devon Energy name and the DVN ticker, is headquartered in Houston and keeps a significant presence in Oklahoma City. Devon publishes a corporate website, an investor-relations site, sustainability and cybersecurity reporting, and a supplier and interest-owner information section, but operates no public developer program, no API and no machine-readable API artifacts. Owner statements are delivered through EnergyLink and supplier invoicing through Enverus OpenInvoice — both third-party platforms, neither a Devon API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/devon-energy.png
layout: provider
modified: '2026-09-06'
name: Devon Energy
nav: Providers
network: true
overview: 'Devon Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Energy, Oil and Gas, Exploration and Production, and Natural Gas.


  Devon Energy''s developer surface includes engineering blog, support, and 6 more developer resources.'
press:
- date: '2026-05-25'
  title: Devon Energy Corp. (DVN)
  url: https://s2.q4cdn.com/462548525/files/doc_presentations/2026/DVN-CTRA-Merger_WebcastTranscript.pdf
- date: '2026-05-25'
  title: Devon Energy Empowers Teams with AI and ChatDVN
  url: https://www.linkedin.com/posts/treylowe_for-devon-energy-ai-in-drilling-comes-down-activity-7417202227309613057-vp1b
- date: '2026-05-25'
  title: Devon Energy and Coterra Energy to Combine, Creating a ...
  url: https://investors.devonenergy.com/investors/press-releases/press-release-details/2026/Devon-Energy-and-Coterra-Energy-to-Combine-Creating-a-Premier-Shale-Operator/
- date: '2026-05-25'
  title: Devon Energy Stays Ahead Of Technology Curve
  url: https://www.aogr.com/magazine/cover-story/devon-energy-stays-ahead-of-technology-curve
- date: '2026-05-25'
  title: Devon Energy and Coterra Energy Complete Merger
  url: https://investors.devonenergy.com/investors/press-releases/press-release-details/2026/Devon-Energy-and-Coterra-Energy-Complete-Merger/
random_paper: 17
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 8.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/devon-energy/refs/heads/main/screenshots/devon-energy-2026-06-20T175950.png
security:
- kind: domain-security
  name: Devon Energy Domain Security
  slug: devon-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: devon-energy
tags:
- Fortune 500
- Energy
- Oil and Gas
- Exploration and Production
- Natural Gas
- Petroleum
website: https://www.devonenergy.com
---
