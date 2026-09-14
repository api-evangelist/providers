---
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ahara-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://foodhealthcollective.org/
- group: operate
  title: ''
  type: Support
  url: https://foodhealthcollective.org/partner
- group: company
  title: ''
  type: Blog
  url: https://foodhealthcollective.org/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://foodhealthcollective.org/privacy
- group: commercial
  title: ''
  type: Plans
  url: plans/ahara-plans-pricing.yml
coverage:
  checked: '2026-09-13'
  detail: AHARA rebranded to Food Health Collective in late 2024 and sells a dietitian-led personalized-nutrition program and a consumer iOS app (Food Health Rx) to employers, health plans and providers — its live Webflow site at foodhealthcollective.org has no developer, docs, API or integration section anywhere in its 15-URL sitemap, the legacy ahara.com domain is registrar-suspended (clientHold, NXDOMAIN on every label including the app/auth subdomains certificate transparency shows once existed), eatahara.com fails the TLS handshake, and there is no GitHub organization or first-party package on npm or PyPI.
  evidence:
  - status: 404
    url: https://foodhealthcollective.org/openapi.json
  - status: 404
    url: https://foodhealthcollective.org/.well-known/api-catalog
  - status: 404
    url: https://foodhealthcollective.org/llms.txt
  - status: 200
    url: https://foodhealthcollective.org/sitemap.xml
  - status: 404
    url: https://ahara.health/
  - status: 0
    url: https://www.ahara.com/
  - status: 0
    url: https://eatahara.com/
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: 'AHARA is a Los Angeles personalized-nutrition company founded in 2022 by physician nutritionist Dr. Melina Jampolis and The RealReal founder Julie Wainwright, funded with a $10.25M seed round led by Greycroft. It pairs a health questionnaire and at-home genetic, epigenetic and blood-biomarker testing with registered-dietitian guidance and a consumer app (Food Health Rx) that turns the results into a personalized food-as-medicine plan, sold direct to consumers and through employers, health plans and providers. In late 2024 the company rebranded as Food Health Collective and moved its web presence to foodhealthcollective.org; the original ahara.com domain is now registrar-suspended (clientHold, NXDOMAIN) and the ahara.health Squarespace site has expired. AHARA operates no developer program: there is no portal, no documentation, no API reference, no public package, no GitHub organization and no machine-readable contract on any host it controls.'
image: https://cdn.prod.website-files.com/653ab111bff5168524434e6f/674ce9a6714fc3b7bc89e07f_1.png
layout: provider
modified: '2026-09-13'
name: AHARA
nav: Providers
network: true
overview: 'AHARA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Nutrition, Personalized Nutrition, and Digital Health.


  AHARA''s developer surface includes support, engineering blog, and 4 more developer resources.'
plans:
- name: Ahara Plans Pricing
  plan_count: 0
  slug: ahara-plans-pricing
random_paper: 5
security:
- kind: domain-security
  name: Ahara Domain Security
  slug: ahara-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ahara
tags:
- Company
- Health
- Nutrition
- Personalized Nutrition
- Digital Health
- Food as Medicine
- Preventive Health
- Consumer Health
- Employer Benefits
- Health Plans
- Mobile App
- Wellness
website: https://foodhealthcollective.org/
---
