---
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aavantgardebio-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.aavantgarde.com/en/
- group: company
  title: ''
  type: About
  url: https://www.aavantgarde.com/en/about/
- group: company
  title: ''
  type: Blog
  url: https://www.aavantgarde.com/en/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aavantgarde.com/en/privacy-notice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aavantgarde-bio
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aavantgardebio-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/aavantgardebio-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/aavantgardebio-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aavantgardebio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aavantgardebio-llms.txt
coverage:
  checked: '2026-09-05'
  detail: AAVantgarde Bio is a clinical-stage gene therapy company whose product is an investigational AAV vector, not software — the corporate site has no developer section at all (nav is About / Innovation / Clinical Trials / For Patients / News / Careers / Contact), api., developer., docs., status. and trust. subdomains are all NXDOMAIN, there is no GitHub organization, and the only machine-readable documents the site serves are the OpenID discovery and JWKS files its Umbraco CMS emits for website-member sign-in.
  evidence:
  - status: 200
    url: https://www.aavantgarde.com/en/
  - status: 404
    url: https://www.aavantgarde.com/llms.txt
  - status: 404
    url: https://www.aavantgarde.com/.well-known/api-catalog
  - status: 404
    url: https://www.aavantgarde.com/.well-known/agent-card.json
  - status: 200
    url: https://www.aavantgarde.com/.well-known/openid-configuration
  - status: 404
    url: https://api.github.com/orgs/aavantgarde-bio
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: AAVantgarde Bio is a clinical-stage biotechnology company headquartered in Milan, Italy, developing next-generation adeno-associated virus (AAV) gene therapies for inherited retinal diseases with high unmet need. Founded in 2021 by Prof. Alberto Auricchio, the company has built two proprietary vector platforms — dual hybrid and dual intein — that overcome the DNA cargo capacity limit of a single AAV vector by splitting a large expression cassette across two AAV8 vectors that recombine inside the target cell. Its lead programs are AAVB-081 for retinitis pigmentosa due to Usher syndrome type 1B (LUCE-1 Phase 1/2, the first dual AAV gene therapy tested clinically in an ocular indication) and AAVB-039 for ABCA4-associated Stargardt disease (CELESTE Phase 1/2), which holds FDA Fast Track and Orphan Drug designation. The company raised a EUR 61 million Series A and closed a USD 141 million Series B. AAVantgarde publishes no public API, developer program or machine-readable contract;
  this profile records what its public web surface actually serves.
image: https://www.aavantgarde.com/assets/img/AavantgardeBio-logo.svg
layout: provider
modified: '2026-09-05'
name: AAVantgarde Bio
nav: Providers
network: true
overview: 'AAVantgarde Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Gene Therapy, Life Sciences, and Pharmaceuticals.


  AAVantgarde Bio''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 15
security:
- kind: domain-security
  name: Aavantgardebio Domain Security
  slug: aavantgardebio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aavantgardebio Vulnerability Disclosure
  slug: aavantgardebio-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: aavantgardebio
tags:
- Company
- Biotechnology
- Gene Therapy
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Ophthalmology
- Rare Disease
- Healthcare
- Italy
website: https://www.aavantgarde.com/en/
---
