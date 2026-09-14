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
  url: security/sionna-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sionna-therapeutics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.sionnatx.com/
- group: company
  title: ''
  type: About
  url: https://www.sionnatx.com/about-us/
- group: other
  title: ''
  type: Science
  url: https://www.sionnatx.com/our-science/
- group: other
  title: ''
  type: Pipeline
  url: https://www.sionnatx.com/pipeline/
- group: company
  title: ''
  type: Careers
  url: https://www.sionnatx.com/join-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.sionnatx.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sionnatx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sionnatx.com/terms-of-use/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.sionnatx.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/sionna-therapeutics_stock/
coverage:
  checked: '2026-08-27'
  detail: Sionna Therapeutics is a clinical-stage biopharmaceutical company whose product is a small-molecule CFTR modulator, not software — its entire public surface is a nine-page WordPress marketing site (home, about, science, pipeline, careers, contact, legal) whose Yoast sitemap lists no developer, API or documentation page, and the only machine-readable endpoint on the host is the default WordPress /wp-json/ CMS route table (343 core/plugin routes, no product API).
  evidence:
  - status: 404
    url: https://www.sionnatx.com/openapi.json
  - status: 404
    url: https://www.sionnatx.com/developers
  - status: 404
    url: https://www.sionnatx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.sionnatx.com/.well-known/security.txt
  - status: 200
    url: https://www.sionnatx.com/page-sitemap.xml
  - status: 404
    url: https://api.github.com/orgs/sionna-therapeutics
  - status: 0
    url: https://investors.sionnatx.com/
  reason: not-a-software-company
  state: none
created: '2026-08-27'
description: 'Sionna Therapeutics, Inc. (Nasdaq: SION) is a clinical-stage biopharmaceutical company headquartered at 21 Hickory Drive, Waltham, Massachusetts, working to revolutionize the treatment paradigm for cystic fibrosis (CF) by developing novel small molecules that normalize the function of the cystic fibrosis transmembrane conductance regulator (CFTR) protein. Building on more than a decade of its co-founders'' research, the company advances a pipeline of first-in-class stabilizers of CFTR''s nucleotide-binding domain 1 (NBD1) — the domain that carries F508del, the most common CF-causing mutation — including SION-719 and SION-451, alongside a portfolio of complementary CFTR modulators such as SION-2222 (galicaftor) and SION-109 designed to work synergistically with the NBD1 stabilizers. Sionna operates purely as a drug-development organization: its public web presence is a nine-page WordPress marketing site covering science, pipeline, careers, contact and legal material, plus a
  hosted investor-relations portal. It publishes no developer program, public API, SDK, webhook surface, or machine-readable specification of any kind.'
image: https://www.sionnatx.com/wp-content/uploads/share_news-from-sionna.jpg
layout: provider
modified: '2026-08-27'
name: Sionna Therapeutics
nav: Providers
network: true
overview: Sionna Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.
random_paper: 16
screenshot: https://raw.githubusercontent.com/api-evangelist/sionna-therapeutics/refs/heads/main/screenshots/sionna-therapeutics-2026-09-02T155640.png
security:
- kind: domain-security
  name: Sionna Therapeutics Domain Security
  slug: sionna-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sionna-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Drug Development
- Rare Disease
- Cystic Fibrosis
- Small Molecule
website: https://www.sionnatx.com/
---
