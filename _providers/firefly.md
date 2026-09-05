---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.fireflyon.com/contact
  - https://www.fireflyon.com/advertising-solutions
  - https://www.fireflyon.com/pricing
  trial: false
  try_now: false
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
    dynamic_client_registration: true
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
  score: 17.6
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://fireflyon.com
- group: company
  title: ''
  type: Blog
  url: https://fireflyon.com/blog
- group: operate
  title: ''
  type: Support
  url: https://fireflyon.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fireflyon.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fireflyon.com/advertising-terms-and-conditions
- group: auth
  title: ''
  type: DomainSecurity
  url: security/firefly-domain-security.yml
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.fireflyon.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://app.fireflyon.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/firefly-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/firefly-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/firefly-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/firefly-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/firefly-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/firefly-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/firefly-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Firefly ships no developer site of its own — fireflyon.com/developers, /api, /docs and /pricing all 404 and its 90-URL sitemap contains no reference page — and the only live Firefly API host, the advertiser-dashboard gateway app-gw.api.fireflyon.com, answers 404 text/plain to every unauthenticated path including /openapi.json; the integration surface a buyer actually programs against is Firefly's inventory listed inside third-party DOOH SSPs (Place Exchange, Vistar Media, Hivestack, Broadsign, VIOOH), whose OpenRTB contracts belong to those platforms rather than to Firefly.
  evidence:
  - status: 404
    url: https://app-gw.api.fireflyon.com/openapi.json
  - status: 404
    url: https://www.fireflyon.com/developers
  - status: 200
    url: https://www.fireflyon.com/sitemap.xml
  - status: 200
    url: https://www.fireflyon.com/advertising-solutions
  - status: 200
    url: https://auth.fireflyon.com/.well-known/openid-configuration
  reason: marketplace-only
  state: gated
created: '2026-07-17'
description: Firefly Systems Inc. is a data-first moving out-of-home (mOOH) advertising network that turns taxis, rideshare vehicles, and other mobility assets into digital and static advertising surfaces across 15+ major North American markets and several countries. Its network of tens of thousands of GPS-connected screens delivers geo-targeted, contextual, and programmatic digital out-of-home (DOOH) campaigns with advanced tracking, attribution, and measurement. Firefly offers digital and static car tops, full and partial car wraps, in-car TaxiTV, around-car activations, and experiential LED and hologram truck formats. Programmatic demand reaches Firefly inventory through third-party DOOH supply-side platforms rather than a Firefly endpoint — its own advertising-solutions page names Place Exchange, Vistar Media, Hivestack and Broadsign, alongside a VIOOH integration, and supports Programmatic Guaranteed and open-marketplace deals. The company is backed by investors including 500 Global,
  Andreessen Horowitz (a16z), and GV (Google Ventures).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firefly.png
layout: provider
modified: '2026-08-12'
name: Firefly
nav: Providers
network: true
overview: 'Firefly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Digital Out Of Home, DOOH, and Mobility.


  Firefly''s developer surface includes engineering blog, support, authentication, and 12 more developer resources.'
plans:
- name: Firefly Plans Pricing
  plan_count: 0
  slug: firefly-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Firefly Rate Limits
  slug: firefly-rate-limits
scopes:
- name: Firefly Scopes
  scope_count: 14
  slug: firefly-scopes
  summary_line: 14 scopes
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 17.2
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firefly/refs/heads/main/screenshots/firefly-2026-07-25T214553.png
security:
- kind: authentication
  name: Firefly Authentication
  slug: firefly-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Firefly Domain Security
  slug: firefly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: firefly
tags:
- Company
- Advertising
- Digital Out Of Home
- DOOH
- Mobility
- Advertising Technology
- AdTech
- Marketing
- Measurements
- Programmatic Advertising
website: https://fireflyon.com
---
