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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spothopper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spothopperapp.com/
- group: company
  title: ''
  type: Blog
  url: https://www.spothopperapp.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.spothopperapp.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spothopperapp.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spothopperapp.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpotHopperLLC
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spothopper/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/spothopperapp/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/spothopper_official/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spothopper-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/spothopper-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spothopper-rate-limits.yml
coverage:
  checked: '2026-08-29'
  detail: 'SpotHopper ships its restaurant marketing platform only as an end-user product — its own FAQ says guests are linked out to OpenTable, Yelp and UberEats with "no integrations needed" — and there is no developer page, API reference or spec on any host it controls: www.spothopperapp.com and api.spotapps.co (which, despite the "api." label, resolves to the same 34.194.50.185 marketing application) answer every spec path with the 171,924-byte single-page-application homepage, while /api returns a hard 404.'
  evidence:
  - status: 404
    url: https://www.spothopperapp.com/api
  - status: 404
    url: https://api.spotapps.co/api/v1
  - status: 200
    url: https://api.spotapps.co/openapi.json
  - status: 200
    url: https://www.spothopperapp.com/developers
  - status: 200
    url: https://www.spothopperapp.com/faq
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: SpotHopper is a Milwaukee, Wisconsin based restaurant marketing and web technology company, founded in 2015, selling an all-in-one, AI-assisted platform to independent restaurants and multi-location restaurant groups. The platform bundles restaurant website design and hosting (customer sites are served from the spotapps.co domain), SEO and Google Business Profile syncing, menu / specials / event publishing, automated social posting to Facebook and Instagram, email and SMS campaigns, review generation and reputation management, and link-outs to reservation and ordering partners such as OpenTable, Yelp and UberEats. The company markets itself as powering more than 20,000 restaurants. As of the 2026-08-29 enrichment probe SpotHopper publishes no developer portal, no API reference, and no machine-readable API contract on any host it controls.
image: https://spothopper-static.s3.us-east-1.amazonaws.com/assets/landing-page/meta-default.jpg
layout: provider
modified: '2026-08-29'
name: SpotHopper
nav: Providers
network: true
overview: 'SpotHopper is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Hospitality, Marketing, and Websites.


  SpotHopper''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Spothopper Plans Pricing
  plan_count: 0
  slug: spothopper-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Spothopper Rate Limits
  slug: spothopper-rate-limits
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Spothopper Domain Security
  slug: spothopper-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spothopper
tags:
- Company
- Restaurant
- Hospitality
- Marketing
- Websites
- SEO
- Reviews
- Social-Media
- Email Marketing
- SMS
- Small Business
website: https://www.spothopperapp.com/
---
