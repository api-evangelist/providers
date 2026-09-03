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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alliance-one-international-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pyxus.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pyxus.com/privacy-policy.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pyxus.com/pyxus-alliance-terms.php
- group: operate
  title: ''
  type: Support
  url: https://www.pyxus.com/contact.php
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alliance-one-international-llms.txt
coverage:
  checked: '2026-09-01'
  detail: The Alliance One International brand was retired in 2018 when the company renamed itself Pyxus International, and the domain of record for it, pyxusinternational.com, is now a parked domain that answers every path — including a negative-control path that cannot exist — with a 114-byte JavaScript lander; the successor's live site at www.pyxus.com is a corporate brochure for an agricultural commodity business with no developer section, no API, and clean 404s on every named /.well-known/ path.
  evidence:
  - status: 200
    url: https://www.pyxusinternational.com/.well-known/alliance-one-international-negative-control-7f3ab91c.json
  - status: 404
    url: https://www.pyxus.com/developers
  - status: 404
    url: https://www.pyxus.com/openapi.json
  - status: 404
    url: https://www.pyxus.com/.well-known/api-catalog
  reason: defunct
  state: none
created: '2026-04-19'
description: 'Alliance One International was a global leaf tobacco merchant that purchased, processed, and sold leaf tobacco to manufacturers of cigarettes and other consumer tobacco products. Founded in 2005 through the merger of Dimon Incorporated and Standard Commercial Corporation, Alliance One International became one of the world''s two largest leaf tobacco dealers. The company sourced tobacco from major growing regions including the United States, Brazil, Zimbabwe, Malawi, Turkey, and other countries. In 2018, Alliance One International changed its name to Pyxus International, reflecting a broader diversification strategy beyond tobacco into hemp, cannabis, and e-liquids. As an agricultural commodity trading business, Alliance One International did not maintain a public developer API program, and probes on 2026-09-01 found none at its successor either: pyxusinternational.com is now a parked domain and the live corporate site at www.pyxus.com publishes no API, SDK, webhook surface,
  or machine-readable specification.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alliance-one-international.png
layout: provider
modified: '2026-09-01'
name: Alliance One International
nav: Providers
network: true
overview: 'Alliance One International is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Tobacco, Agriculture, Commodities, Leaf Tobacco, and Manufacturing.


  Alliance One International''s developer surface includes support and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alliance-one-international/refs/heads/main/screenshots/alliance-one-international-2026-07-25T195703.png
security:
- kind: domain-security
  name: Alliance One International Domain Security
  slug: alliance-one-international-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alliance-one-international
tags:
- Tobacco
- Agriculture
- Commodities
- Leaf Tobacco
- Manufacturing
website: https://www.pyxus.com
---
