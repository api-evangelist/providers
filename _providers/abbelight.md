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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.abbelight.com/
- group: operate
  title: ''
  type: Support
  url: https://www.abbelight.com/customer-care/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abbelight.com/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abbelight.com/data-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abbelight-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abbelight-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: Abbelight sells super-resolution microscopes, consumables and the desktop SAFe Neo analysis suite through account executives and a WooCommerce shop; its entire 26-page WordPress site contains no developer, API, SDK or integration page, and the only machine-readable surface on any host it controls is the default WordPress REST API at shop.abbelight.com/wp-json/, which returns 401 rest_not_logged_in to anonymous callers.
  evidence:
  - status: 404
    url: https://www.abbelight.com/openapi.json
  - status: 404
    url: https://www.abbelight.com/llms.txt
  - status: 404
    url: https://www.abbelight.com/.well-known/agent-card.json
  - status: 401
    url: https://shop.abbelight.com/wp-json/
  - status: 200
    url: https://api.github.com/orgs/abbelight
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: Abbelight is a French bioimaging company founded in 2016 and headquartered in Cachan, near Paris, that designs and manufactures single-molecule localization microscopy (SMLM) and nanoscopy instrumentation. Its modular SAFe platform — SAFe Excitation, SAFe Detection and the SAFe Nexus optronic control bay — mounts on the camera port of any inverted microscope and upgrades it from diffraction-limited widefield and TIRF imaging to super-resolution techniques including STORM, PALM, DNA-PAINT and spectral demixing. The company also ships the Smart Flow automated sample-preparation system, ready-to-use staining and buffer kits, and the SAFe Neo software suite for 3D quantitative analysis and visualization of localization data. Abbelight sells through account executives and a consumables webshop, and raised a Series B led by AVANT BIO in January 2026. As of this profile it publishes no public API, SDK, developer portal or machine-readable specification.
image: https://www.abbelight.com/wp-content/themes/abbelight/assets/images/svg/abbelight_black.svg
layout: provider
modified: '2026-09-05'
name: Abbelight
nav: Providers
network: true
overview: 'Abbelight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bioimaging, Microscopy, Nanoscopy, and Super Resolution.


  Abbelight''s developer surface includes support and 5 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.0
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: Abbelight Domain Security
  slug: abbelight-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: abbelight
tags:
- Company
- Bioimaging
- Microscopy
- Nanoscopy
- Super Resolution
- Scientific Instruments
- Life Sciences
- Laboratory
- Medical Devices
- France
website: https://www.abbelight.com/
---
