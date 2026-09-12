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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.alleyesonscreens.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.alleyesonscreens.com/faq
- group: operate
  title: ''
  type: Support
  url: https://www.alleyesonscreens.com/getintouch
- group: start
  title: ''
  type: SignUp
  url: https://cockpit.alleyesonscreens.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alleyesonscreens.com/toc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alleyesonscreens.com/privacypolicy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adscanner-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adscanner-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/adscanner-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adscanner-rate-limits.yml
coverage:
  checked: '2026-09-07'
  detail: The company's own FAQ states "our data can be obtained via reporting (pdf, Excel, CSV, json) and API on request", but there is no developer portal, no API reference and no spec anywhere on the site — the 29-URL sitemap has no /developers, /docs or /api page, and info@alleyesonscreens.com plus the /getintouch form are the only stated routes to the API.
  evidence:
  - status: 200
    url: https://www.alleyesonscreens.com/faq
  - status: 200
    url: https://www.alleyesonscreens.com/sitemap.xml
  - status: 404
    url: https://api.alleyesonscreens.com/openapi.json
  - status: 403
    url: https://api.alleyesonscreens.com/.well-known/api-catalog
  reason: sales-gate
  state: gated
created: '2026-09-07'
description: AdScanner — now trading as all eyes on screens (AEOS), the legal entity all eyes on screens d.o.o. of Zagreb, Croatia, formerly Adscanner d.o.o. — is a European TV and video advertising measurement, planning and activation platform founded in 2012. In-house AI video-recognition software matches broadcast ad creatives second-by-second against viewing data supplied by IPTV and telco partners, producing cross-channel reach, frequency and attribution measurement for linear, addressable and connected TV. Products include the AdScanner/AEOS Cockpit analytics dashboard, the Apollo AI-based ex-ante planning module, TV Boost data activation on post-code segments, and TV Match cross-device targeting and TV-sync signals that fire digital campaigns when a spot airs. AEOS operates in Croatia, Austria, Germany, Bulgaria and Switzerland. The company states in its own FAQ that its data can be obtained via reporting (PDF, Excel, CSV, JSON) and API on request, but publishes no public developer
  portal, API reference or machine-readable contract.
layout: provider
modified: '2026-09-07'
name: Adscanner
nav: Providers
network: true
overview: 'Adscanner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Television, and Media Measurement.


  Adscanner''s developer surface includes documentation, support, signup flow, and 7 more developer resources.'
plans:
- name: Adscanner Plans Pricing
  plan_count: 0
  slug: adscanner-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Adscanner Rate Limits
  slug: adscanner-rate-limits
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 46.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 14.3
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adscanner Domain Security
  slug: adscanner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adscanner
tags:
- Company
- Advertising
- AdTech
- Television
- Media Measurement
- Analytics
- Attribution
- Connected TV
- Addressable TV
- Audience Data
- Artificial Intelligence
- Croatia
website: https://www.alleyesonscreens.com/
---
