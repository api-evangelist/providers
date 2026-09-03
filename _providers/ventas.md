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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ventas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ventasreit.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.ventasreit.com/overview/default.aspx
- group: other
  title: ''
  type: AnnualReport
  url: https://ir.ventasreit.com/financials/annual-reports/default.aspx
- group: operate
  title: ''
  type: PressReleases
  url: https://ir.ventasreit.com/press-releases/
- group: other
  title: ''
  type: SECFilings
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000740260&type=10-K&dateb=&owner=include&count=40
- group: operate
  title: ''
  type: Contact
  url: https://www.ventasreit.com/contact
- group: company
  title: ''
  type: About
  url: https://www.ventasreit.com/about-ventas
created: '2026-03-24'
description: Ventas, Inc. is an S&P 500 healthcare real estate investment trust (REIT) and one of the largest owners of senior housing communities, medical office buildings, life science research facilities, and health system facilities in the United States, Canada, and United Kingdom. Ventas operates the Ventas OI proprietary data platform for operational intelligence across its portfolio of approximately 1,400 properties. Ventas does not offer a public developer API; data access is available through financial data providers and SEC EDGAR filings.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ventas.png
json_schemas:
- name: Ventas Healthcare Property
  property_count: 11
  slug: ventas-property
json_structures:
- name: Ventas Property Structure
  property_count: 0
  slug: ventas-property-structure
jsonld:
- class_count: 31
  name: Ventas Context
  property_count: 2
  slug: ventas-context
layout: provider
modified: '2026-05-03'
name: Ventas
nav: Providers
network: true
overview: 'Ventas is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Real-Estate, REIT, Senior Housing, and Life Science.


  The Ventas catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
press:
- date: '2026-05-25'
  title: How Ventas is using AI for real estate & net zero
  url: https://www.mckinsey.com/industries/real-estate/our-insights/how-ventas-used-machine-learning-and-ai-to-create-a-net-zero-plan
- date: '2026-05-25'
  title: Financials - Quarterly Results - Ventas IR
  url: https://ir.ventasreit.com/financials/quarterly-results/default.aspx
- date: '2026-05-25'
  title: Performance Marketing Agency, Beeby Clark+Meyler ...
  url: https://www.prnewswire.com/news-releases/performance-marketing-agency-beeby-clarkmeyler-pushes-the-boundaries-of-ai-led-advertising-with-the-release-of-ventas-ai-an-ai-stack-delivering-more-measurable-and-rapid-creative-testing-and-optimization-302179293.html
- date: '2026-05-25'
  title: Creative Testing at Scale - Ventas AI
  url: https://www.beebyclarkmeyler.com/ventas-ai
- date: '2026-05-25'
  title: Ventas Reports Fourth Quarter and Full Year 2025 Results ...
  url: https://ir.ventasreit.com/news/news-details/2026/Ventas-Reports-Fourth-Quarter-and-Full-Year-2025-Results-Provides-2026-Outlook-and-Increases-Dividend/default.aspx
random_paper: 6
rules:
- effective_rule_count: 5
  extends: []
  name: Ventas API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ventas-jsonschema-spectral-rules
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 76.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 0.0
  previous_composite: 8.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ventas/refs/heads/main/screenshots/ventas-2026-06-20T200911.png
security:
- kind: domain-security
  name: Ventas Domain Security
  slug: ventas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ventas
tags:
- Healthcare
- Real-Estate
- REIT
- Senior Housing
- Life Science
- Fortune 500
website: https://www.ventasreit.com/
---
