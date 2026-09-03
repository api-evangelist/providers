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
    consent_identity: true
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
  score: 2.2
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silicon-box-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.silicon-box.com/
- group: company
  title: ''
  type: About
  url: https://www.silicon-box.com/about
- group: other
  title: ''
  type: Services
  url: https://www.silicon-box.com/services
- group: company
  title: ''
  type: Blog
  url: https://www.silicon-box.com/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.silicon-box.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.silicon-box.com/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.silicon-box.com/careers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/silicon-box-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: well-known/silicon-box-robots.txt
coverage:
  checked: '2026-08-27'
  detail: Silicon Box is a chiplet advanced-packaging foundry whose product is physically manufactured silicon — its entire 47-URL sitemap is corporate marketing (services, newsroom, careers, virtual factory) with no developer, docs or API section, and no api./developer./docs./portal. subdomain resolves at all.
  evidence:
  - status: 200
    url: https://www.silicon-box.com/sitemap.xml
  - status: 404
    url: https://www.silicon-box.com/openapi.json
  - status: 404
    url: https://www.silicon-box.com/api-docs
  - status: 404
    url: https://www.silicon-box.com/docs
  - status: 404
    url: https://www.silicon-box.com/graphql
  - status: 404
    url: https://www.silicon-box.com/.well-known/agent-card.json
  - status: 200
    url: https://www.silicon-box.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-27'
description: 'Silicon Box Pte Ltd is an independent advanced semiconductor packaging and chiplet integration company headquartered in Tampines, Singapore, founded in 2021 by Byung Joon Han, Sehat Sutardja and Weili Dai. It operates a $2B panel-level packaging foundry and provides the back-end interconnection infrastructure that makes chiplet adoption practical — from early design collaboration through final manufacture and test — functioning as an OSAT with an added design-consulting practice. It has shipped over 500 million units at high yield, joined the imec Automotive Chiplet Program, and is building a second €3.2B facility in Novara, Piedmont, Italy. Silicon Box is a semiconductor manufacturer, not a software vendor: it publishes no developer program, no API documentation and no machine-readable API contract. See x-coverage below for the measured basis of that statement.'
image: https://lirp.cdn-website.com/68ddebd6/dms3rep/multi/opt/ENG20230714_130004-1920w.jpg
layout: provider
modified: '2026-08-27'
name: Silicon Box
nav: Providers
network: true
overview: 'Silicon Box is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Semiconductors, Chiplets, Advanced Packaging, Manufacturing, and Hardware.


  Silicon Box''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/silicon-box/refs/heads/main/screenshots/silicon-box-2026-09-02T155456.png
security:
- kind: domain-security
  name: Silicon Box Domain Security
  slug: silicon-box-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: silicon-box
tags:
- Semiconductors
- Chiplets
- Advanced Packaging
- Manufacturing
- Hardware
- Foundry
- Singapore
- Company
website: https://www.silicon-box.com/
---
