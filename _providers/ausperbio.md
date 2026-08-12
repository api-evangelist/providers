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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ausperbio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ausperbio.com/
- group: company
  title: ''
  type: About
  url: https://www.ausperbio.com/company.html
- group: other
  title: ''
  type: Team
  url: https://www.ausperbio.com/leadership.html
- group: other
  title: ''
  type: Product
  url: https://www.ausperbio.com/platform.html
- group: other
  title: ''
  type: Research
  url: https://www.ausperbio.com/pipeline.html
- group: company
  title: ''
  type: Blog
  url: https://www.ausperbio.com/news.html
- group: company
  title: ''
  type: News
  url: https://www.ausperbio.com/news.html
- group: operate
  title: ''
  type: Support
  url: https://www.ausperbio.com/contact-us.html
- group: operate
  title: ''
  type: Contact
  url: https://www.ausperbio.com/contact-us.html
- group: company
  title: ''
  type: Careers
  url: https://www.ausperbio.com/careers.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ausperbio.com/term.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ausperbio.com/privacy.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ausperbio
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ausperbio-llms.txt
coverage:
  checked: '2026-08-06'
  detail: AusperBio develops antisense-oligonucleotide and siRNA drugs for chronic hepatitis B, so there is no software product to expose; ausperbio.com is a Vue single-page app that returns an identical 2,601-byte shell (md5 519d85ce…) for every path including invented ones, and the only machine-readable API description on the estate is the springdoc description of the private Spring Boot CMS at cms.ausperbio.com/jzy-admin/, which is correctly 401-gated and is site infrastructure rather than a product surface.
  evidence:
  - note: Soft 404 — byte-identical to the SPA shell returned for a nonexistent control path.
    status: 200
    url: https://www.ausperbio.com/openapi.json
  - note: Control path proving every 200 on this host is the SPA catch-all.
    status: 200
    url: https://www.ausperbio.com/definitely-not-a-real-path-zzz999
  - note: Soft 404 — SPA shell, not an llms.txt.
    status: 200
    url: https://www.ausperbio.com/llms.txt
  - note: Soft 404 — SPA shell, not an agent card. No A2A card published.
    status: 200
    url: https://www.ausperbio.com/.well-known/agent-card.json
  - note: Returns {"code":401,"msg":""} — springdoc API description exists but is authentication-gated.
    status: 200
    url: https://cms.ausperbio.com/jzy-admin/v3/api-docs
  - status: 401
    url: https://cms.ausperbio.com/jzy-admin/doc.html
  - note: No such host in DNS. Same for developer. and docs. subdomains.
    status: 0
    url: https://api.ausperbio.com/
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'AusperBio — AusperBio Therapeutics, Inc. in the United States and Ausper Biopharma Co., Ltd. (杭州浩博医药有限公司) in Hangzhou, China — is a clinical-stage biopharmaceutical company founded in 2019 that develops oligonucleotide and targeted delivery technologies, with an initial focus on achieving a functional cure for chronic hepatitis B infection. Its proprietary Med-Oligo antisense oligonucleotide (ASO) platform pairs novel ASO design and optimization with targeted delivery conjugation chemistry, and its Au-HALO hepatocyte-targeting delivery technology extends the same modular approach to siRNA. The lead candidate AHB-137 is an unconjugated ASO that completed enrollment in two Phase II trials and received China CDE clearance to enter Phase III; a second clinical candidate, AHB-171, is a hepatocyte-targeted siRNA. The company has raised more than $200M across Series B, B+ and B2 rounds from investors including Qiming Venture Partners, HanKang Capital, CDH Investments, Sherpa Capital,
  YuanBio Venture Capital and Genesis Capital. AusperBio sells therapeutics, not software: it publishes no developer program, no public API, no SDK and no machine-readable API contract. Its only machine-readable surface is the private Spring Boot CMS backend that renders ausperbio.com, whose springdoc API description is correctly locked behind authentication.'
image: https://www.ausperbio.com/favicon.ico
layout: provider
modified: '2026-08-06'
name: AusperBio
nav: Providers
network: true
overview: 'AusperBio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Biopharmaceutical, and Life Sciences.


  AusperBio''s developer surface includes engineering blog, product news, support, and 12 more developer resources.'
random_paper: 42
score:
  band: minimal
  composite: 12.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ausperbio/refs/heads/main/screenshots/ausperbio-2026-08-07T161949.png
security:
- kind: domain-security
  name: Ausperbio Domain Security
  slug: ausperbio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ausperbio
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Biopharmaceutical
- Life Sciences
- Therapeutics
- Oligonucleotide
- Antisense Oligonucleotide
- siRNA
- Clinical Trials
- Hepatitis B
- Drug Development
- Health
- China
website: https://www.ausperbio.com/
---
