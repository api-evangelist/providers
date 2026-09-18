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
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-09-17'
api_count: 0
artifact_total: 4
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hyatt-hotels/refs/heads/main/security/hyatt-hotels-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hyatt-hotels-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hyatt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyatt
- group: company
  title: ''
  type: Website
  url: https://www.hyatt.com/
- group: company
  title: ''
  type: Website
  url: https://about.hyatt.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hyatt-hotels/refs/heads/main/security/hyatt-hotels-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hyatt-hotels-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/hyatt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hyatt-hotels/refs/heads/main/llms/hyatt-hotels-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hyatt-hotels-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hyatt-hotels/refs/heads/main/packages/hyatt-hotels-packages.yml
  title: ''
  type: Packages
  url: packages/hyatt-hotels-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hyatt-hotels/refs/heads/main/plans/hyatt-hotels-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hyatt-hotels-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hyatt-hotels/refs/heads/main/rate-limits/hyatt-hotels-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hyatt-hotels-rate-limits.yml
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.hyatt.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.hyatt.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.hyatt.com/overview/default.aspx
created: '2026-03-24'
description: 'Hyatt Hotels Corporation (NYSE: H) is a Chicago-headquartered global hospitality company that develops, owns, operates, manages, franchises and licenses hotels, resorts, branded residences and vacation-ownership properties across brands including Park Hyatt, Grand Hyatt, Hyatt Regency, Andaz, Alila, Thompson Hotels, Hyatt Centric, Hyatt Place, Hyatt House and Miraval. No Hyatt developer portal, API reference, machine-readable contract or first-party SDK was found on any reachable Hyatt host or in any public registry as of September 2026; api.hyatt.com resolves to a live but undocumented gateway, and hyatt.com sits behind an edge bot challenge no automated client can read. Partner connectivity runs through third parties (Hapi for event streams and transactional APIs, Sabre SynXis for reservations), and Hyatt''s conversational surface ships as a Hyatt-branded app inside ChatGPT rather than an endpoint Hyatt hosts. Hyatt has run a public HackerOne bug bounty program since January
  2019.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyatt-hotels.png
layout: provider
modified: '2026-09-13'
name: Hyatt Hotels
nav: Providers
network: true
overview: Hyatt Hotels is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, Hotels, Travel, Lodging, and Resorts.
plans:
- name: Hyatt Hotels Plans Pricing
  plan_count: 0
  slug: hyatt-hotels-plans-pricing
press:
- date: '2026-05-25'
  title: Hyatt opens up ChatGPT to employees
  url: https://www.phocuswire.com/news/technology/hyatt-chatgpt-enterprise
- date: '2026-05-25'
  title: Way's Premier Experiential Platform Powers Ancillary and ...
  url: https://www.prnewswire.com/news-releases/ways-premier-experiential-platform-powers-ancillary-and-loyalty-experiences-for-hyatt-302537321.html
- date: '2026-05-25'
  title: Bullish Hoplamazian talks AI, 2026 pace, more
  url: https://www.hotelinvestmenttoday.com/Financials/C-Corps/Bullish-Hoplamazian-talks-AI-2026-pace-more
- date: '2026-05-25'
  title: Hyatt Unveils New Suite of Events Offerings, Together by ...
  url: https://newsroom.hyatt.com/together_by_hyatt
- date: '2026-05-25'
  title: 'Transforming Hospitality: AI''s Game-Changing Role in Hotels'
  url: https://transformhospitality.com/blog/transforming-hospitality-ais-game-changing-role-in-hotels/
random_paper: 0
rate_limits:
- limit_count: 0
  name: Hyatt Hotels Rate Limits
  slug: hyatt-hotels-rate-limits
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 6.0
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hyatt Hotels Domain Security
  slug: hyatt-hotels-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Hyatt Hotels Vulnerability Disclosure
  slug: hyatt-hotels-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: hyatt-hotels
tags:
- Hospitality
- Hotels
- Travel
- Lodging
- Resorts
- Loyalty
- Reservations
- Fortune 1000
website: https://www.hyatt.com/
---
