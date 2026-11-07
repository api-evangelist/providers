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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/evt-com/well-known/evt-com-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/evt-com-support-security.txt
- group: agent
  href: https://artifacts.apis.io/evt-com/well-known/evt-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/evt-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/evt-com/hosts/evt-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/evt-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/evt-com/integrations/evt-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/evt-com-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/evt-com/vendors/evt-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/evt-com-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://www.evt.com/
- group: auth
  href: https://artifacts.apis.io/evt-com/security/evt-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evt-com-domain-security.yml
- group: company
  title: ''
  type: AboutUs
  url: https://www.evt.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.evt.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://support.jsm.evt.com/servicedesk/customer/portals
- group: company
  title: ''
  type: Newsroom
  url: https://www.evt.com/news-press/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.evt.com/investors/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evt.com/privacy-policy/
- group: other
  title: ''
  type: Disclaimer
  url: https://www.evt.com/disclaimer/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amalgamated-holdings-limited
created: '2026-10-21'
description: EVT Limited is an Australian entertainment, hospitality and leisure group operating across Australia, New Zealand, Singapore and Southeast Asia. Its Entertainment division runs cinemas (including Event Cinemas, IMAX and ScreenX screens, and outdoor Moonlight Cinemas), theatre, bars and restaurants; Travel covers hotels and resorts such as QT, Rydges and LyLo plus Thredbo Resort; Ventures spans property, development, entertainment technology services and media. In October 2026 Event Cinemas announced an app in ChatGPT for session search and ticket booking. Surfaced via the API Evangelist harvest backlog (australia-apidays-2026).
image: https://cdn.evt.com/wp-content/uploads/2022/09/28192447/EVT_Wordmark_REV-3.png
layout: provider
modified: '2026-10-21'
name: EVT
nav: Providers
network: true
overview: 'EVT is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Entertainment, Cinemas, Hospitality, and Hotels.


  EVT''s developer surface includes support and 14 more developer resources.'
plans:
- name: Evt Com Plans Pricing
  plan_count: 0
  slug: evt-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Evt Com Rate Limits
  slug: evt-com-rate-limits
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 49.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/evt-com/evt-com-2026-11-03T131720.png
security:
- kind: domain-security
  name: Evt Com Domain Security
  slug: evt-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: evt-com
tags:
- Company
- Entertainment
- Cinemas
- Hospitality
- Hotels
- Travel
- Leisure
- Australia
website: https://www.evt.com/
---
