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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://458energy.com/
- group: company
  title: ''
  type: About
  url: https://458energy.com/story/
- group: operate
  title: ''
  type: ContactUs
  url: https://458energy.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://458energy.com/recrutement/
- group: company
  title: ''
  type: InvestorRelations
  url: https://458energy.com/investors/
- group: operate
  title: ''
  type: PressReleases
  url: https://458energy.com/press/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://458energy.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://458energy.com/mentions-legales/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/458energy-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/458energy-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/458energy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/458energy-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: 45-8 ENERGY drills for helium and natural hydrogen; the entire public site is 62 corporate pages enumerated from its own sitemap with no developer, docs or data section, and the only machine-readable surface on the domain is the stock WordPress REST API at /wp-json/ whose 23 namespaces are all WordPress core or third-party plugins (Elementor, Yoast, Contact Form 7, OceanWP, Polylang), not a 45-8 ENERGY product.
  evidence:
  - status: 200
    url: https://458energy.com/page-sitemap.xml
  - status: 404
    url: https://458energy.com/openapi.json
  - status: 404
    url: https://458energy.com/llms.txt
  - status: 404
    url: https://458energy.com/.well-known/agent-card.json
  - status: 200
    url: https://458energy.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 45-8 ENERGY is a French exploration and production company, founded in 2017 and headquartered in Metz with offices in Lyon, dedicated to helium and natural (native) hydrogen in Europe. It is the first company in France and Western Europe specialised in the exploration and production of these two low-carbon subsurface gases, covering the full value chain from geoscientific exploration through production, distribution and recycling. In 2024 it delivered the first helium produced on Western European soil, and it operates RECYCL'He, Europe's first mobile helium recovery and recycling unit. Its exploration and production portfolio spans France (Fonts-Bouillants, Avant-Monts, Marensin, Beauvoir), Germany (Guhlen, Brimir), the Balkans and the United States (Humboldt, Fayette). In April 2026 Ad Terra took a majority stake in the company. 45-8 ENERGY is a physical-resources operator and publishes no developer program, public API, SDK or machine-readable data surface.
image: https://458energy.com/wp-content/uploads/2023/01/Logo-45-8-ENERGY-Fond-transparent.png
layout: provider
modified: '2026-09-05'
name: 45-8 ENERGY
nav: Providers
network: true
overview: 45-8 ENERGY is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Helium, Natural Hydrogen, and Natural Resources.
plans:
- name: 458Energy Plans Pricing
  plan_count: 0
  slug: 458energy-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: 458Energy Rate Limits
  slug: 458energy-rate-limits
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 458Energy Domain Security
  slug: 458energy-domain-security
  summary_line: TLSv1.3
slug: 458energy
tags:
- Company
- Energy
- Helium
- Natural Hydrogen
- Natural Resources
- Exploration and Production
- Industrial Gases
- Cleantech
- France
website: https://458energy.com/
---
