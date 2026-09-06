---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/n-drip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ndrip.com/
- group: other
  title: ''
  type: Product
  url: https://ndrip.com/the-ndrip-solution/
- group: other
  title: ''
  type: Application
  url: https://ndrip.com/ndrip-connect/
- group: company
  title: ''
  type: About
  url: https://ndrip.com/about-us/
- group: operate
  title: ''
  type: FAQ
  url: https://ndrip.com/faq/
- group: operate
  title: ''
  type: Support
  url: https://ndrip.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://ndrip.com/news-and-events/
- group: other
  title: ''
  type: Media
  url: https://ndrip.com/media/
- group: start
  title: ''
  type: Login
  url: https://app.ndrip.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ndrip.com/wp-content/themes/ndrip/includes/images/terms.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ndrip.com/wp-content/themes/ndrip/includes/images/privacy.pdf
- group: other
  title: ''
  type: CookiePolicy
  url: https://ndrip.com/wp-content/themes/ndrip/includes/images/cookies.pdf
- group: other
  title: ''
  type: Accessibility
  url: https://ndrip.com/accessibility-statement/
- group: other
  title: ''
  type: Patents
  url: https://ndrip.com/patents/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/n-drip-gravity-micro-irrigation
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.sciroot
- group: commercial
  title: ''
  type: Plans
  url: plans/n-drip-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/n-drip-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/n-drip-llms.txt
coverage:
  checked: '2026-08-26'
  detail: 'N-Drip ships irrigation hardware plus the closed N-Drip Connect web and mobile app, and operates no developer program at all: ndrip.com is a 16-page WordPress marketing site that 404s on /openapi.json, /api, /developers and every /.well-known path, and the only backend behind the app is an undocumented private AWS API Gateway (geffe6u3ma.execute-api.eu-west-1.amazonaws.com) found in the app bundle that answers an anonymous request with 403 "Missing Authentication Token".'
  evidence:
  - status: 404
    url: https://ndrip.com/openapi.json
  - status: 404
    url: https://ndrip.com/developers
  - status: 404
    url: https://ndrip.com/.well-known/api-catalog
  - status: 403
    url: https://geffe6u3ma.execute-api.eu-west-1.amazonaws.com/prod/
  - status: 200
    url: https://app.ndrip.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'N-Drip is an Israeli agritech manufacturer of gravity-powered micro-irrigation systems, led by Prof. Uri Shani, Israel''s former Water Commissioner. Its patented drip system operates on gravity alone at under 0.87 PSI / 0.06 BAR, requiring no pumping station and no pressure-based filtration, and is positioned as a direct replacement for flood irrigation — which still accounts for roughly 85 percent of the world''s irrigated agriculture and wastes an estimated 70 percent of the water it uses. Alongside the hardware the company ships N-Drip Connect, a sensor-and-app decision-support platform that measures root-zone water potential and available nitrogen, layers NDVI satellite imagery over the field, and issues irrigation and fertilization recommendations to growers. N-Drip technology is deployed in ten countries and five US states across 25 crop types including rice, corn, soybeans, potatoes, sugar cane, alfalfa and cotton, with a US production hub in Yuma, Arizona. N-Drip publishes
  no public developer program, API documentation, SDK or machine-readable API contract: N-Drip Connect is delivered strictly as a closed web and mobile application.'
image: https://ndrip.com/wp-content/uploads/2021/05/ndriplogo.png
layout: provider
modified: '2026-08-26'
name: N-Drip
nav: Providers
network: true
overview: 'N-Drip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Irrigation, and Water.


  N-Drip''s developer surface includes FAQ, support, engineering blog, and 17 more developer resources.'
plans:
- name: N Drip Plans Pricing
  plan_count: 0
  slug: n-drip-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: N Drip Rate Limits
  slug: n-drip-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 11.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/n-drip/refs/heads/main/screenshots/n-drip-2026-09-02T150713.png
security:
- kind: domain-security
  name: N Drip Domain Security
  slug: n-drip-domain-security
  summary_line: TLSv1.3 · DMARC
slug: n-drip
tags:
- Company
- Agriculture
- AgTech
- Irrigation
- Water
- Water Conservation
- Sustainability
- Climate
- Precision Agriculture
- Sensors
- IoT
- Israel
website: https://ndrip.com/
---
