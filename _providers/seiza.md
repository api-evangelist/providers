---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.seiza.co/
coverage:
  checked: '2026-08-17'
  detail: Seiza was acquired by Adzuna on 2024-11-18 and has now been fully decommissioned rather than redirected — seiza.co holds a live registration to 2027 but its GoDaddy delegation answers REFUSED, so the apex, www, api, docs and app hosts all return SERVFAIL and no HTTP connection can be opened; the profile's inherited seiza.fr URL is an unrelated GoDaddy Website Builder page ("Find Your Zen") whose only machine-readable file is a GoDaddy-generated llms.txt, and while the real site was live it published 23 pre-built ATS connectors with bespoke integrations routed through sales but never a public API, developer portal or specification of any kind.
  evidence:
  - status: 0
    url: https://www.seiza.co/
  - status: 0
    url: https://api.seiza.co/
  - status: 404
    url: https://seiza.fr/openapi.json
  - status: 404
    url: https://seiza.fr/.well-known/agent-card.json
  - status: 200
    url: https://web.archive.org/web/20251112014053/https://www.seiza.co/produit/integrations/
  reason: defunct
  state: none
created: '2026-08-17'
description: 'Seiza was a French social-recruitment advertising and recruitment-automation SaaS platform dedicated to frontline hiring — hospitality and restaurants, transport and logistics, agri-food, industry, retail, temp staffing, healthcare and construction. Founded in Paris in 2010 as Work4 Labs by Stephane Le Viet, Gautier Machelon and Matt Brown, it built its early business on sourcing candidates through non-professional social networks rather than job boards or LinkedIn, later rebranding from Work4 to Seiza. It raised roughly $22.8M in venture capital (Serena, among others) and served about 400 clients across Europe and the US, including McDonald''s, Sysco, Ecolab and Veolia. The product was a recruiter web application — social sourcing campaigns, profile enrichment, one-click calling, a compatibility index, automated interview scheduling, SMS/messaging and reporting — plus a fixed catalog of 23 named ATS connectors (Bullhorn, Workday, Greenhouse, SmartRecruiters, iCIMS, Cornerstone,
  Recruitee, Talensoft, DigitalRecruiters, Beetween, Fountain, Paychex, CareerBuilder, Avionte, Acquity, Idibu, PivotCX, Talemetry, Gestmax, Scoptalent, Eolia Software, MyCVtheque, Hubspot), with anything outside that list handled as a bespoke integration through sales. No public API, developer portal, API reference, OpenAPI/AsyncAPI specification, webhook catalog, SDK or CLI was ever published: a 557-URL census of the archived seiza.co site shows only marketing, blog, FAQ and legal pages, and every /.well-known/ path returned 404 while the site was live. Seiza was acquired by UK job-search engine Adzuna on 2024-11-18 and folded into Adzuna''s social recruitment advertising line; Adzuna''s own developer program is profiled separately in this network. The company domain seiza.co was still serving in May 2026 but no longer resolves at all as of 2026-08-17. This profile is retained as a historical company record; there is no API surface to enrich.'
layout: provider
modified: '2026-08-17'
name: Seiza
nav: Providers
network: true
overview: Seiza is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Human Resources, HR Tech, and Recruitment.
random_paper: 15
score:
  band: minimal
  composite: 4.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
slug: seiza
tags:
- Company
- Software-as-a-Service
- Human Resources
- HR Tech
- Recruitment
- Recruitment Automation
- Applicant Tracking
- Frontline Workers
- Social Recruiting
- France
- Acquired
- Defunct
website: https://www.seiza.co/
---
