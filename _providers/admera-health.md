---
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/admera-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.admerahealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.admerahealth.com/blog
- group: operate
  title: ''
  type: Support
  url: https://admerahealth.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: ContactUs
  url: https://www.admerahealth.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.admerahealth.com/faqs
- group: start
  title: ''
  type: Login
  url: https://www.admerahealth.com/eratrack-customer-portal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.admerahealth.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.admerahealth.com/privacy-policy
- group: auth
  title: ''
  type: Certification
  url: https://www.admerahealth.com/certifications
- group: auth
  title: ''
  type: Compliance
  url: https://www.admerahealth.com/certifications
- group: company
  title: ''
  type: Careers
  url: https://www.admerahealth.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/admera-health/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/AdmeraHealth
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/admera-health-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/admera-health-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/admera-health-plans-pricing.yml
coverage:
  checked: '2026-09-07'
  detail: Admera Health is a genomics sequencing and bioinformatics CRO whose only software product is EraTrack, a login-only customer project-tracking portal; the ASP.NET backend behind it at api.admerahealth.com answers 404 to every spec, swagger, docs and .well-known path, and the marketing site has no /developer, /developers, /docs or /api-docs page at all.
  evidence:
  - status: 404
    url: https://www.admerahealth.com/developers
  - status: 404
    url: https://api.admerahealth.com/swagger/v1/swagger.json
  - status: 404
    url: https://api.admerahealth.com/openapi.json
  - status: 200
    url: https://www.admerahealth.com/eratrack-customer-portal
  - status: 200
    url: https://www.admerahealth.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: Admera Health is a CLIA-certified and CAP-accredited genomics service provider and contract research organization headquartered in South Plainfield, New Jersey, established in 2014 as a spinout of GENEWIZ. It runs 100% US-based next-generation sequencing, library preparation and bioinformatics operations for academic, biotech and biopharma customers, spanning whole genome and whole exome sequencing, metagenomics and amplicon sequencing, bulk and small RNA-seq, single-cell sequencing on 10x Genomics, Parse Biosciences and Takara Bio platforms, spatial transcriptomics on Visium HD and STOmics Stereo-seq, epigenomics, proteomics and metabolomics, plus BioEcho nucleic acid purification products. Customers submit and track projects through EraTrack, a login-only web portal. Admera Health publishes no public developer program, API reference, SDK or machine-readable specification of any kind.
image: https://static1.squarespace.com/static/62fd3ea4903b393b1c2b91c4/t/6a9202d1ee934c04baae347f/1787953873973/admera_health_final_logo_final_transparent_500px.png?format=1500w
layout: provider
modified: '2026-09-07'
name: Admera Health
nav: Providers
network: true
overview: 'Admera Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genomics, Sequencing, Bioinformatics, and Life Sciences.


  Admera Health''s developer surface includes engineering blog, support, FAQ, and 14 more developer resources.'
plans:
- name: Admera Health Plans Pricing
  plan_count: 0
  slug: admera-health-plans-pricing
random_paper: 12
security:
- kind: domain-security
  name: Admera Health Domain Security
  slug: admera-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: admera-health
tags:
- Company
- Genomics
- Sequencing
- Bioinformatics
- Life Sciences
- Healthcare
- Laboratory Services
- Biotechnology
- Multi-Omics
- Contract Research
website: https://www.admerahealth.com/
---
