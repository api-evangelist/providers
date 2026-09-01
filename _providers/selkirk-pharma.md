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
  url: security/selkirk-pharma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.selkirkpharma.com/
- group: company
  title: ''
  type: Careers
  url: https://www.selkirkpharma.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.selkirkpharma.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/selkirk-pharma
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/selkirk-pharma_stock/
coverage:
  checked: '2026-08-26'
  detail: 'Selkirk Pharma is a sterile fill/finish CDMO in Spokane, Washington whose product is aseptic manufacturing capacity for injectable drugs, not software — there is no developer program, no API, no SDK on npm or PyPI, no GitHub organization, and every developer-shaped hostname (api./docs./developer./portal./app./login./status..selkirkpharma.com) is NXDOMAIN rather than a wildcard; the archived 2026-05-08 home page links 17 pages and all 17 are contract-manufacturing marketing. Separately worth recording for a re-run: the live Webflow edge refused the TLS handshake (alert 40) to curl, python ssl and openssl at both TLSv1.2 and TLSv1.3, so the site itself could only be read from the Wayback Machine — but that obstruction is not why this profile is thin.'
  evidence:
  - status: 0
    url: https://www.selkirkpharma.com/
  - status: 301
    url: http://www.selkirkpharma.com/openapi.json
  - status: 200
    url: http://web.archive.org/web/20260508082831/https://www.selkirkpharma.com/
  - status: 200
    url: https://api.github.com/search/users?q=selkirk+pharma
  - status: 404
    url: https://pypi.org/pypi/selkirk-pharma/json
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Selkirk Pharma, Inc. is a privately held U.S. contract development and manufacturing organization (CDMO) in Spokane, Washington, specializing in the aseptic fill/finish of sterile injectable drug products — vaccines, biologics and small molecules — for clinical and commercial supply. Founded in 2018, it operates a purpose-built aseptic campus at 9110 W Granite Avenue in the Pacific Northwest Technology Park, roughly half a mile from Spokane International Airport, running unidirectional personnel and material flow, single-use systems, SKAN isolator technology and Bausch+Strobel VarioSys dose-filling lines rated to about 3,600 vials per hour under EU GMP Annex 1. Services span aseptic filling, in-house analytical chemistry and microbiology, sterility testing, finished-product inspection, regulatory support and supply-chain services, plus a ClinFAST program that compresses fill/finish timelines for clinical-trial material. The build-out drew roughly $150M led by Spokane''s Cowles
  Company with other Washington State investors, and Colleen Dixon was named chief executive in July 2024. Selkirk Pharma sells contract manufacturing capacity, not software: it operates no developer program, publishes no web API, SDK or machine-readable specification, and maintains no public source-code organization. (In this sector "API" ordinarily means active pharmaceutical ingredient; Selkirk fills and finishes drug product and publishes no web API.)'
layout: provider
modified: '2026-08-26'
name: Selkirk Pharma
nav: Providers
network: true
overview: Selkirk Pharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Contract Manufacturing, CDMO, and Sterile Injectables.
random_paper: 7
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Selkirk Pharma Domain Security
  slug: selkirk-pharma-domain-security
  summary_line: DMARC
slug: selkirk-pharma
tags:
- Company
- Pharmaceuticals
- Contract Manufacturing
- CDMO
- Sterile Injectables
- Aseptic Fill Finish
- Biologics
- Life Sciences
- Clinical Trials
- Manufacturing
website: https://www.selkirkpharma.com/
---
