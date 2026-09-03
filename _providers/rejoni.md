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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://rejoni.com/
- group: company
  title: ''
  type: About
  url: https://rejoni.com/about
- group: other
  title: ''
  type: Team
  url: https://rejoni.com/team
- group: other
  title: ''
  type: Technology
  url: https://rejoni.com/technology
- group: company
  title: ''
  type: News
  url: https://rejoni.com/news
- group: operate
  title: ''
  type: Contact
  url: https://rejoni.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rejoni.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rejoni
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/rejoni_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rejoni-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rejoni-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Rejoni's product is a resorbable hydrogel implant and a transcervical delivery catheter pending FDA premarket approval, not software; its whole web presence is a seven-page Webflow marketing site with an empty robots.txt, where /openapi.json, /graphql, /mcp, /llms.txt and every /.well-known/ path 404 against a verified real-404 control, and api./developer./docs.rejoni.com resolve only to a wildcard A record that never answers a TCP connect.
  evidence:
  - status: 404
    url: https://rejoni.com/openapi.json
  - status: 404
    url: https://rejoni.com/llms.txt
  - status: 404
    url: https://rejoni.com/.well-known/agent-card.json
  - status: 404
    url: https://rejoni.com/graphql
  - status: 404
    url: https://rejoni.com/zzz-control-path-check
  - status: 0
    url: https://api.rejoni.com/
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Rejoni, Inc. is a privately held, clinical-stage women''s health medical device company founded in June 2020 by serial entrepreneur Amar Sawhney, PhD and Pramand LLC, and headquartered at 201 Burlington Road in Bedford, Massachusetts. It develops proprietary hydrogel-based biomaterial therapies for gynecological surgery, with a stated mission of protecting, preserving and healing the uterus. Its lead product, the Juveena Hydrogel System, is designed to prevent the formation and reformation of intrauterine adhesions (IUAs) — the scar tissue that forms after transcervical procedures such as dilation and curettage, myomectomy or treatment of heavy bleeding, and a leading cause of infertility and abnormal uterine bleeding. The system pairs a low-profile proprietary transcervical catheter with two liquid precursors that cross-link on delivery into a soft, temporary hydrogel implant that mechanically separates the uterine walls during healing and then resorbs on its own in roughly
  two to three weeks, about one menstrual cycle, so no removal procedure is required. Juveena is investigational only and pending FDA approval; the FDA filed Rejoni''s premarket approval (PMA) application in January 2026, and the company completed patient enrollment in its US IDE pivotal study. Rejoni closed a $25 million financing in June 2026 with ClavystBio, Amed Ventures, Ascension Ventures, Catalyst Health Ventures, Delos Capital, FemHealth Ventures, Iyengar Capital and Sparta Group, and appointed women''s health MedTech leader John Nealon as chief executive officer in May 2026. Rejoni runs no developer program and publishes no public API: its entire web presence is a small Webflow marketing site, and probes for OpenAPI, Swagger, GraphQL, MCP, llms.txt and every /.well-known/ discovery path returned HTTP 404 against a verified real-404 origin, while api./developer./docs./app./portal.rejoni.com resolve only to a wildcard A record with no listener answering on either port 80 or 443.'
image: https://cdn.prod.website-files.com/68a338214a8d0f9a68a471b5/68a360063a1179d6ecb188ec_Rejoni_tag_logo_White.svg
layout: provider
modified: '2026-08-05'
name: Rejoni
nav: Providers
network: true
overview: 'Rejoni is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Women''s Health, Healthcare, and Biomaterials.


  Rejoni''s developer surface includes product news and 10 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rejoni/refs/heads/main/screenshots/rejoni-2026-09-02T153258.png
security:
- kind: domain-security
  name: Rejoni Domain Security
  slug: rejoni-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rejoni
tags:
- Company
- Medical Devices
- Women's Health
- Healthcare
- Biomaterials
- Life Sciences
- Surgery
- Clinical Trials
- MedTech
website: https://rejoni.com/
---
