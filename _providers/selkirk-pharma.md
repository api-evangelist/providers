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
