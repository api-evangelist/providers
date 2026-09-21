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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afalight/refs/heads/main/llms/afalight-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/afalight-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afalight/refs/heads/main/security/afalight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afalight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.afalight.com/
- group: company
  title: ''
  type: Blog
  url: https://www.afalight.com/company_news/
- group: operate
  title: ''
  type: Support
  url: https://www.afalight.com/support/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/afalight
coverage:
  checked: '2026-09-12'
  detail: Afalight manufactures physical optoelectronic hardware - HDMI/USB-C fiber optical modules and extenders - and its entire web presence is a product-catalog and sales site with a support form and a downloads page; there is no developer section, no API, and every contract-discovery and /.well-known/ path returned 404 on all three hosts.
  evidence:
  - status: 200
    url: https://www.afalight.com/
  - status: 404
    url: https://www.afalight.com/openapi.json
  - status: 404
    url: https://www.afalight.com/apis.json
  - status: 404
    url: https://www.afalight.com/.well-known/api-catalog
  - status: 404
    url: https://www.afalight.com/.well-known/agent-card.json
  - status: 404
    url: http://en.afalight.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: 'Afalight (Shenzhen Afalight Co., Ltd. / 深圳市埃尔法光电科技有限公司) is a Shenzhen-based optoelectronics manufacturer founded in 2016 that designs and builds next-generation photoelectric modules, optical engines and active optical cable assemblies. Its HDFiberLink, HEXWaveLink and FSO AxisLink product families cover HDMI, USB-C, DVI and LC single/dual-fiber optical modules plus fiber-optic extenders carrying IR and RS-232 control, aimed at ultra-high-definition and 8K video transport, split TVs, mobile handsets, projectors, VR gaming rigs, industrial and medical imaging, and automotive electronics. The company is a Chinese national high-tech enterprise, a member of the World Ultra HD Video Industry Alliance (CUVA) and the Shenzhen 8K Ultra HD Video Industry Cooperation Alliance (SUVA), holds ISO 9001 / ISO 14001 / ISO 45001 and IECQ HSPM certification, and reports more than 60 patents, four PCT filings and a CNAS- accredited laboratory. It is a hardware supplier: it publishes no developer
  program, no public API, and no machine-readable API contract of any kind.'
image: https://www.afalight.com/static/aef/images/logo.png
layout: provider
modified: '2026-09-12'
name: Afalight
nav: Providers
network: true
overview: 'Afalight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hardware, Optoelectronics, Optical Modules, and Fiber Optics.


  Afalight''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 6.0
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afalight Domain Security
  slug: afalight-domain-security
  summary_line: HSTS · DMARC
slug: afalight
tags:
- Company
- Hardware
- Optoelectronics
- Optical Modules
- Fiber Optics
- Video
- Manufacturing
- Semiconductors
- Consumer Electronics
- China
website: https://www.afalight.com/
---
