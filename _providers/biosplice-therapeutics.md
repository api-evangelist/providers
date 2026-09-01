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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/biosplice-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/biosplice-therapeutics-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/biosplice-therapeutics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.biosplice.com/
- group: company
  title: ''
  type: About
  url: https://www.biosplice.com/mission/default.aspx
- group: other
  title: ''
  type: Pipeline
  url: https://www.biosplice.com/our-programs/detail.aspx?id=20
- group: other
  title: ''
  type: Team
  url: https://www.biosplice.com/management/default.aspx
- group: other
  title: ''
  type: Publications
  url: https://www.biosplice.com/publications/default.aspx
- group: company
  title: ''
  type: News
  url: https://www.biosplice.com/news/default.aspx
- group: company
  title: ''
  type: Blog
  url: https://www.biosplice.com/news/default.aspx
- group: company
  title: ''
  type: Careers
  url: https://www.biosplice.com/careers/default.aspx
- group: operate
  title: ''
  type: Contact
  url: https://www.biosplice.com/contact-us/default.aspx
- group: operate
  title: ''
  type: Support
  url: https://www.biosplice.com/contact-us/default.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.biosplice.com/privacy/default.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.biosplice.com/terms/default.aspx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/biospliceinc
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/biosplice-therapeutics_stock/
coverage:
  checked: '2026-08-07'
  detail: Biosplice is a clinical-stage drug developer whose product is an injectable small molecule, not software; www.biosplice.com is a 13KB ASP.NET brochure site with no robots.txt and no sitemap.xml, every spec and /.well-known/ path is rewritten to the CMS 404 page, and api./developer./docs./portal./status./graphql./mcp.biosplice.com have no DNS record at all.
  evidence:
  - status: 404
    url: https://www.biosplice.com/openapi.json
  - status: 404
    url: https://www.biosplice.com/.well-known/agent-card.json
  - status: 404
    url: https://www.biosplice.com/.well-known/agent.json
  - status: 404
    url: https://www.biosplice.com/llms.txt
  - status: 404
    url: https://www.biosplice.com/sitemap.xml
  - status: 404
    url: https://api.github.com/orgs/biosplice
  reason: not-a-software-company
  state: none
created: '2026-08-07'
description: 'Biosplice Therapeutics, Inc. is a privately held, clinical-stage biopharmaceutical company headquartered in San Diego, California, founded in 2008 by Osman Kibar and known until its 2020 rename as Samumed, LLC (samumed.com still redirects to biosplice.com). The company develops first-in-class small-molecule therapeutics that act on novel components of the Wnt signaling pathway and on the regulation of alternative pre-mRNA splicing. Its lead program is lorecivivint, an investigational intra-articular knee injection for osteoarthritis, positioned against a stated unmet need of "over 50 million US patients suffer from osteoarthritis, with no drugs available to arrest the disease"; the candidate has completed Phase 3 study and a New Drug Application has been submitted to the U.S. Food and Drug Administration. Programs outside lorecivivint — neurology, diabetes and oncology — are developed by the company''s affiliate TenaRx, Inc. The company is led by Erich Horsley (Chief Executive
  Officer) with Osman Kibar as Founder and Executive Chairman, Yusuf Yazici as Chief Medical Officer, Phil Wilson as Chief Financial Officer and Scott W. Bulcao as Chief Legal Officer. Biosplice is a drug-discovery and clinical-development organization, not a software vendor: biosplice.com is a small ASP.NET corporate site covering mission, board, management, advisors, programs, publications, news and careers, and the company publishes no developer program of any kind — no API, no SDK, no developer portal, no GitHub organization and no machine-readable API contract.'
layout: provider
modified: '2026-08-07'
name: Biosplice Therapeutics
nav: Providers
network: true
overview: 'Biosplice Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Drug Development.


  Biosplice Therapeutics'' developer surface includes product news, engineering blog, support, and 14 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/biosplice-therapeutics/refs/heads/main/screenshots/biosplice-therapeutics-2026-08-07T162507.png
security:
- kind: domain-security
  name: Biosplice Therapeutics Domain Security
  slug: biosplice-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biosplice-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Drug Development
- Clinical Trials
- Osteoarthritis
- Small Molecule Therapeutics
- Healthcare
- San Diego
website: https://www.biosplice.com/
---
