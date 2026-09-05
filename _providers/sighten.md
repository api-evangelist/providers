---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://sighten.io'', ''status'': 301, ''note'': ''declared website redirects to https://www.goeverbright.com/ — a different registrable domain (sighten.io -> goeverbright.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://sighten.io
- group: company
  title: ''
  type: Blog
  url: https://www.goeverbright.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goeverbright.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.goeverbright.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.goeverbright.com/faq
- group: start
  title: ''
  type: Login
  url: https://myeverbright.com/login
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.goeverbright.com/
- group: auth
  title: ''
  type: Compliance
  url: security/sighten-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sighten-domain-security.yml
created: '2026-07-17'
description: Sighten was a San Francisco software company, backed by Obvious Ventures, that built a cloud platform for the residential and commercial solar industry — covering system design, proposal generation, sales, and financing workflows used by solar installers, dealers, and finance providers. The Sighten business was acquired (by GoodLeap) and folded into EverBright; the original sighten.io domain now redirects to goeverbright.com. EverBright operates as a residential solar and home-battery financing platform, connecting homeowners with local installers through lease and Power Purchase Agreement (PPA) products and the MyEverBright monitoring portal. No public developer API, developer portal, or API documentation is published for the Sighten or EverBright brand; a partner-facing platform (engine.goeverbright.com) and a protected API host (api.goeverbright.com, HTTP 401) exist but are not publicly documented. This profile records the company's current, honest public surface after enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sighten.png
layout: provider
modified: '2026-07-21'
name: Sighten
nav: Providers
network: true
overview: 'Sighten is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Solar, Clean Energy, Renewable Energy, and Solar Software.


  Sighten''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sighten/refs/heads/main/screenshots/sighten-2026-09-02T155424.png
security:
- kind: domain-security
  name: Sighten Domain Security
  slug: sighten-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Sighten Trust Center
  slug: sighten-trust-center
  summary_line: CCPA, GLBA
slug: sighten
tags:
- Company
- Solar
- Clean Energy
- Renewable Energy
- Solar Software
- Solar Financing
- Home Energy
- Energy
website: https://sighten.io
---
