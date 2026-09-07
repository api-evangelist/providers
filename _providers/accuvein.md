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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.accuvein.com/
- group: operate
  title: ''
  type: Support
  url: https://www.accuvein.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.accuvein.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.accuvein.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accuvein.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.accuvein.com/contact/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accuvein-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accuvein-llms.txt
coverage:
  checked: '2026-09-06'
  detail: AccuVein manufactures handheld near-infrared vein-visualization hardware (AV500/AV600) sold through medical distributors and GPOs; its only web presence is a WordPress marketing and product-support site with no developer surface, and developer./api./docs. accuvein.com do not resolve in DNS.
  evidence:
  - status: 200
    url: https://www.accuvein.com/
  - status: 404
    url: https://www.accuvein.com/openapi.json
  - status: 404
    url: https://www.accuvein.com/api-docs
  - status: 404
    url: https://www.accuvein.com/graphql
  - status: 404
    url: https://www.accuvein.com/.well-known/agent-card.json
  - status: 404
    url: https://www.accuvein.com/.well-known/security.txt
  - status: 200
    url: https://api.github.com/users/accuvein/repos
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'AccuVein, Inc. is a Medford, New York medical device manufacturer that builds handheld, near-infrared (NIR) vein visualization systems used by clinicians for peripheral vascular access. Its AV500 and AV600 devices project a real-time green image of superficial vasculature onto the surface of the skin, letting nurses and phlebotomists see veins, valves and bifurcations that are not visible to the naked eye before a needle stick. The company sells into acute care, non-acute care and aesthetics, and supports the product line with published instructions for use, product manuals, troubleshooting guidance and a knowledge center. AccuVein is a hardware business: as of this profile it publishes no developer program, no public API, no SDK and no machine-readable API description.'
image: https://www.accuvein.com/wp-content/uploads/2022/05/AccuVein-Two-Color-Logo-954x160.png
layout: provider
modified: '2026-09-06'
name: AccuVein
nav: Providers
network: true
overview: 'AccuVein is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Vein Visualization, and Vascular Access.


  AccuVein''s developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: domain-security
  name: Accuvein Domain Security
  slug: accuvein-domain-security
  summary_line: TLSv1.3 · DMARC
slug: accuvein
tags:
- Company
- Medical Devices
- Healthcare
- Vein Visualization
- Vascular Access
- Near-Infrared Imaging
- Medical Imaging
- Hardware
website: https://www.accuvein.com/
---
