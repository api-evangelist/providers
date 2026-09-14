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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/quaise-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quaise-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quaise.com/
- group: company
  title: ''
  type: Blog
  url: https://www.quaise.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quaise.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quaise.com/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/quaise-energy-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/quaise-energy-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quaise-energy-llms.txt
coverage:
  checked: '2026-08-26'
  detail: 'Quaise Energy sells millimeter-wave drilling hardware and geothermal power, not software: contract discovery found no OpenAPI/GraphQL/MCP/A2A surface on any host, and the only web application (an LCOE calculator) is a client-side React app behind an AWS Cognito login whose shipped bundle still carries a DEV config pointing at a backend host that 404s at every path.'
  evidence:
  - status: 404
    url: https://www.quaise.com/openapi.json
  - status: 404
    url: https://www.quaise.com/.well-known/api-catalog
  - status: 404
    url: https://www.quaise.com/.well-known/agent-card.json
  - status: 404
    url: https://www.quaise.com/developers
  - status: 200
    url: https://www.quaise.com/.well-known/security.txt
  - status: 404
    url: https://quaise-play-research.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Quaise Energy is a deep-geothermal energy company and MIT spinout, founded in 2018 by Carlos Araque and Matthew Houde out of a decade of millimeter-wave research by Paul Woskov at the MIT Plasma Science and Fusion Center. Quaise is developing millimeter-wave (MMW) drilling — using a gyrotron to vaporize rather than grind rock — to reach supercritical conditions several kilometers down, where temperatures approach 500 degrees C, and to convert existing fossil-fuel power stations to superhot geothermal baseload. The company drilled 100 meters with the technique at its Central Texas field site in 2025. Quaise is an energy and hardware company: it publishes no developer program, no public API, and no machine-readable API contract. Its only public web application is a levelized-cost-of-energy (LCOE) calculator whose full functionality sits behind an AWS Cognito login.'
image: https://d19xrwp2bu8dt3.cloudfront.net/general/Quaise-link-img1.png
layout: provider
modified: '2026-08-26'
name: Quaise Energy
nav: Providers
network: true
overview: 'Quaise Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Geothermal, Clean Energy, and Drilling.


  Quaise Energy''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 20
screenshot: https://raw.githubusercontent.com/api-evangelist/quaise-energy/refs/heads/main/screenshots/quaise-energy-2026-09-02T152553.png
security:
- kind: domain-security
  name: Quaise Energy Domain Security
  slug: quaise-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Quaise Energy Vulnerability Disclosure
  slug: quaise-energy-vulnerability-disclosure
  summary_line: disclosure policy published
slug: quaise-energy
tags:
- Company
- Energy
- Geothermal
- Clean Energy
- Drilling
- Deep Tech
- Climate Tech
- Hardware
website: https://www.quaise.com/
---
