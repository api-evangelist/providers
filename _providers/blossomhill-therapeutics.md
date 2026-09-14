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
  url: security/blossomhill-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bhtherapeutics.com/
- group: company
  title: ''
  type: About
  url: https://bhtherapeutics.com/about-us/
- group: other
  title: ''
  type: Pipeline
  url: https://bhtherapeutics.com/pipeline/
- group: company
  title: ''
  type: Investors
  url: https://bhtherapeutics.com/investors/
- group: company
  title: ''
  type: Blog
  url: https://bhtherapeutics.com/news/
- group: operate
  title: ''
  type: PressReleases
  url: https://bhtherapeutics.com/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://bhtherapeutics.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://bhtherapeutics.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://bhtherapeutics.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bhtherapeutics.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bhtherapeutics.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://bhtherapeutics.com/cookie-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blossomhill-therapeutics-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blossomhill-therapeutics-inc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/bhtherapeutics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/blossomhill-therapeutics_stock/
coverage:
  checked: '2026-08-07'
  detail: BlossomHill is a clinical-stage oncology drug-discovery company with no developer site and no API product; every OpenAPI, GraphQL, MCP and agent-card path on bhtherapeutics.com returns 404, api./docs./developer.bhtherapeutics.com do not resolve, and the only machine-readable surface on the domain is the default WordPress /wp-json REST root its marketing CMS exposes.
  evidence:
  - status: 404
    url: https://bhtherapeutics.com/openapi.json
  - status: 404
    url: https://bhtherapeutics.com/.well-known/agent-card.json
  - status: 404
    url: https://bhtherapeutics.com/graphql
  - status: 200
    url: https://bhtherapeutics.com/wp-json/
  - status: 401
    url: https://stg-blossomhill-build.kinsta.cloud/
  reason: not-a-software-company
  state: none
created: '2026-08-07'
description: 'BlossomHill Therapeutics is a privately held, clinical-stage biopharmaceutical company headquartered in San Diego, California, founded in 2020 by drug designer J. Jean Cui, Ph.D. and biotech operator Y. Peter Li, Ph.D., M.B.A. It develops intelligently designed small-molecule medicines for oncology and autoimmune disease, led by BH-30643, a first-in-class macrocyclic non-covalent mutant-selective OMNI-EGFR inhibitor for EGFR- and HER2-mutated non-small cell lung cancer, and BH-30236, a macrocyclic CLK inhibitor for relapsed or refractory acute myeloid leukemia and higher-risk myelodysplastic syndrome. The company is a drug discovery business, not a software vendor: it publishes no public API, SDK, developer portal or machine-readable specification.'
image: https://bhtherapeutics.com/wp-content/uploads/logo-stacked.svg
layout: provider
modified: '2026-08-07'
name: BlossomHill Therapeutics
nav: Providers
network: true
overview: 'BlossomHill Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Drug Discovery.


  BlossomHill Therapeutics'' developer surface includes engineering blog and 16 more developer resources.'
random_paper: 14
screenshot: https://raw.githubusercontent.com/api-evangelist/blossomhill-therapeutics/refs/heads/main/screenshots/blossomhill-therapeutics-2026-08-07T162640.png
security:
- kind: domain-security
  name: Blossomhill Therapeutics Domain Security
  slug: blossomhill-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blossomhill-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Drug Discovery
- Clinical Trials
- Life Sciences
- Precision Medicine
website: https://bhtherapeutics.com/
---
