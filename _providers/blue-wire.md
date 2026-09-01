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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blue-wire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluewirepods.com
- group: operate
  title: ''
  type: Support
  url: https://bluewirepods.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bluewirepods.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bluewirepods.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://bluewirepods.com/news
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blue-wire-llms.txt
coverage:
  checked: '2026-08-10'
  detail: Blue Wire sells podcast advertising inventory and creator services from a Webflow-published marketing site; the 430-URL sitemap contains only posts, shows, team and jobs pages, and api./developer./docs.bluewirepods.com are all NXDOMAIN.
  evidence:
  - status: 404
    url: https://bluewirepods.com/developers
  - status: 404
    url: https://bluewirepods.com/openapi.json
  - status: 404
    url: https://bluewirepods.com/.well-known/agent-card.json
  - status: 200
    url: https://bluewirepods.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-07-17'
description: Blue Wire is a podcast network and monetization platform built for independent sports content creators, positioning itself as "The Monetization Engine for Sports Creators." The company provides sales, marketing, distribution, and operational support so creators can focus on producing content while Blue Wire handles ad sales and sponsorship coordination across a network of 200+ shows and 500+ creators reaching hundreds of millions of listeners. Backed by 500 Global. Blue Wire operates as a media and advertising business and does not publish a public developer API; this profile captures its company identity and domain-security posture within the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blue-wire.png
layout: provider
modified: '2026-08-10'
name: Blue Wire
nav: Providers
network: true
overview: 'Blue Wire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Podcasting, Media, Sports, and Advertising.


  Blue Wire''s developer surface includes support, engineering blog, and 5 more developer resources.'
plans:
- name: Blue Wire Plans Pricing
  plan_count: 0
  slug: blue-wire-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Blue Wire Rate Limits
  slug: blue-wire-rate-limits
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blue-wire/refs/heads/main/screenshots/blue-wire-2026-07-25T203442.png
security:
- kind: domain-security
  name: Blue Wire Domain Security
  slug: blue-wire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blue-wire
tags:
- Company
- Podcasting
- Media
- Sports
- Advertising
- Monetization
- Content Creators
website: https://bluewirepods.com
---
