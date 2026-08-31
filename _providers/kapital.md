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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kapital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kapital.com/
- group: company
  title: ''
  type: Blog
  url: https://kapital.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://kapital.com/recursos/costos-y-comisiones
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kapital.com/recursos/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kapital.com/recursos/aviso-de-privacidad
- group: start
  title: ''
  type: SignUp
  url: https://onboarding.kapital.com/registro-inicial
- group: start
  title: ''
  type: Login
  url: https://app.kapital.com/
- group: operate
  title: ''
  type: Support
  url: https://kapital.com/recursos/aclaraciones
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KapitalMx
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kapital-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/kapital-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/kapital-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kapital-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kapital-rate-limits.yml
coverage:
  checked: '2026-08-23'
  detail: Kapital Bank ships regulated banking only as an end-user product - its whole 58-URL sitemap contains no developer, API, integration or documentation page, robots.txt disallows /api/*, and the only two API hosts that resolve are private app backends (api.kapital.com answers "404 page not found" on every path behind Imperva, and api.kapital.mx is an AWS ALB catch-all returning the same 50-byte {"code":200,"message":"Exito","response":false} for every path including a nonexistent control path).
  evidence:
  - status: 200
    url: https://kapital.com/sitemaps/sitemap-pages.xml
  - status: 200
    url: https://kapital.com/robots.txt
  - status: 404
    url: https://api.kapital.com/openapi.json
  - status: 200
    url: https://api.kapital.mx/.well-known/this-path-does-not-exist-ae-probe
  - status: 0
    url: https://developers.kapital.com/
  - status: 200
    url: https://kapital.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: Kapital (KPTL MEXICO BANK, S.A., Institucion de Banca Multiple, Kapital Mexico Grupo Financiero) is a licensed Mexican bank and AI-native financial platform for SMEs and corporates, founded in 2019 and headquartered in Mexico City. Its ecosystem combines business and personal deposit accounts, corporate cards, SPEI and SPID transfers, FX cash/transfers/cheques and derivatives (forwards, interest rates), working-capital and revolving credit (Credito Empresarial, Credito PyME, Credito FLEX), factoring, and fixed-income investments (Pagare, CEDES) with Kapital IA, a native artificial-intelligence layer that reconciles cash flow, projects sales, validates supplier pricing and flags anomalous costs. It is supervised by the CNBV and Banco de Mexico, with deposits protected by IPAB, and it also operates in Colombia as Kapital Colombia. Kapital publishes no public developer portal, OpenAPI, SDK or webhook surface; the banking surface is delivered through its own web and mobile applications.
image: https://images.ctfassets.net/vr3zuj968faf/4ukUDPhZ4HcU709aDP2z4W/672ff99991179687f553c2de8c41dbd4/Kapital__1_.webp
layout: provider
modified: '2026-08-23'
name: Kapital
nav: Providers
network: true
overview: 'Kapital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial-Services, Fintech, Small and Medium Businesses, and Payments.


  Kapital''s developer surface includes engineering blog, pricing, signup flow, support, and 11 more developer resources.'
plans:
- name: Kapital Plans Pricing
  plan_count: 0
  slug: kapital-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Kapital Rate Limits
  slug: kapital-rate-limits
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 30.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Kapital Domain Security
  slug: kapital-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kapital
tags:
- Banking
- Financial-Services
- Fintech
- Small and Medium Businesses
- Payments
- Foreign Exchange
- Lending
- Treasury
- Artificial Intelligence
- Mexico
- Latin America
website: https://kapital.com/
---
