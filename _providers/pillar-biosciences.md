---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pillar-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pillarbiosci.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pillarbiosci.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://www.pillarbiosci.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.pillarbiosci.com/company/pillar-news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pillarbiosci.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pillar-Biosciences-Inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pillar-biosciences
- group: build
  title: ''
  type: Packages
  url: packages/pillar-biosciences-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pillar-biosciences-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/pillar-biosciences-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pillar-biosciences-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pillar-biosciences-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pillar-biosciences-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pillar-biosciences-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Pillar sells NGS panels and the PiVAT analysis app, and PiVAT's own product page names its integration surface as bioinformatics FILE formats (FASTQ, BAM, VCF, PDF) rather than an API; the PiVAT app host answers HTTP 200 with the same 1,535-byte React SPA shell for /openapi.json and every other unknown path, and 403 for the whole /.well-known/ space, so there is no developer portal, contract or reference to read anywhere.
  evidence:
  - status: 200
    url: https://pivat.pillarbiosci.com/openapi.json
  - status: 403
    url: https://pivat.pillarbiosci.com/.well-known/agent-card.json
  - status: 404
    url: https://www.pillarbiosci.com/openapi.json
  - status: 404
    url: https://www.pillarbiosci.com/llms.txt
  - status: 200
    url: https://www.pillarbiosci.com/wp-sitemap-posts-page-1.xml
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Pillar Biosciences is a Natick, Massachusetts molecular diagnostics company, founded in 2014, that develops targeted next-generation sequencing (NGS) solutions for precision oncology. Its proprietary SLIMamp (Stem-Loop Inhibition Mediated amplification) chemistry enables highly multiplexed, single-tube PCR library preparation from as little as 2.5 ng of DNA, and its oncoReveal panel portfolio covers solid tumour tissue, liquid biopsy, haematologic malignancy, BRCA/HRD/methylation and inherited disease testing, alongside an InheritReveal line and a VersaTile machine-learning panel-design platform. Sequencing data is processed by PiVAT (Pillar Variant Analysis Toolkit), a secondary-analysis pipeline available as a local install or a HIPAA-scoped cloud deployment, with optional OncoKB-powered tertiary reporting. Pillar ships both research-use-only kits and an IVD product line, and raised a $34.5M round led by Illumina in 2025. Pillar publishes no public API, SDK or developer program;
  PiVAT's integration surface is bioinformatics file formats (FASTQ, BAM, VCF, PDF) behind a customer login.
image: https://www.pillarbiosci.com/wp-content/uploads/elementor/thumbs/Pillar_biosciences_logo-scaled-rsdcx7op9xcoyh7jq90gxuj6f8dx4edt9do6jp6ees.png
layout: provider
modified: '2026-08-26'
name: Pillar Biosciences
nav: Providers
network: true
overview: 'Pillar Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Genomics, Molecular Diagnostics, and Next-Generation Sequencing.


  Pillar Biosciences'' developer surface includes documentation, support, engineering blog, changelog, and 11 more developer resources.'
plans:
- name: Pillar Biosciences Plans Pricing
  plan_count: 0
  slug: pillar-biosciences-plans-pricing
random_paper: 0
screenshot: https://raw.githubusercontent.com/api-evangelist/pillar-biosciences/refs/heads/main/screenshots/pillar-biosciences-2026-09-02T151246.png
security:
- kind: domain-security
  name: Pillar Biosciences Domain Security
  slug: pillar-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pillar-biosciences
tags:
- Company
- Life Sciences
- Genomics
- Molecular Diagnostics
- Next-Generation Sequencing
- Precision Oncology
- Bioinformatics
- Healthcare
- Laboratory Software
website: https://www.pillarbiosci.com/
---
