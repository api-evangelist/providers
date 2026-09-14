---
api_count: 0
artifact_total: 1
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adicet-bio-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adicet-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adicetbio.com/
- group: company
  title: ''
  type: About
  url: https://www.adicetbio.com/about/
- group: operate
  title: ''
  type: Support
  url: https://www.adicetbio.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adicetbio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adicetbio.com/privacy/
- group: company
  title: ''
  type: Careers
  url: https://www.adicetbio.com/careers/openings/
coverage:
  checked: '2026-09-07'
  detail: Adicet Bio is a clinical-stage cell-therapy biotech — its products are investigational gamma delta CAR T cell therapies, not software — and its entire public surface is a nine-page corporate marketing site plus a vendor-hosted investor relations portal; every OpenAPI, Swagger, GraphQL, MCP, agent-card and /.well-known/ path probed on adicetbio.com, www.adicetbio.com and investor.adicetbio.com returned 404, 301 or 403, and the site contains no developer, API, docs or integrations link anywhere in its navigation.
  evidence:
  - status: 404
    url: https://www.adicetbio.com/openapi.json
  - status: 404
    url: https://www.adicetbio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.adicetbio.com/llms.txt
  - status: 404
    url: https://www.adicetbio.com/graphql
  - status: 200
    url: https://www.adicetbio.com/
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: 'Adicet Bio, Inc. (Nasdaq: ACET) is a clinical-stage biotechnology company with offices in Redwood City, California and Boston, Massachusetts, discovering and developing allogeneic "off-the-shelf" gamma delta T cell therapies engineered with chimeric antigen receptors (CARs) for autoimmune disease and cancer. Its lead candidate, prulacabtagene leucel (prula-cel), is an anti-CD20 gamma delta CAR T cell therapy in development for B cell-mediated autoimmune diseases, alongside ADI-212 for metastatic castration-resistant prostate cancer. Adicet publishes a corporate website covering its science platform, clinical pipeline, leadership and careers, plus a vendor-hosted investor relations portal. It operates no public developer program, API, SDK, or machine-readable interface of any kind; this profile records that absence rather than an API surface.'
image: https://www.adicetbio.com/themes/default/images/logo.svg
layout: provider
modified: '2026-09-07'
name: Adicet Bio
nav: Providers
network: true
overview: 'Adicet Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Cell Therapy, and Immunotherapy.


  Adicet Bio''s developer surface includes support and 7 more developer resources.'
random_paper: 11
security:
- kind: domain-security
  name: Adicet Bio Domain Security
  slug: adicet-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adicet-bio
tags:
- Company
- Biotechnology
- Life Sciences
- Cell Therapy
- Immunotherapy
- Oncology
- Autoimmune
- Clinical Trials
- Pharmaceuticals
website: https://www.adicetbio.com/
---
