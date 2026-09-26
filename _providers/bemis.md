---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 0
artifact_total: 9
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bemis/refs/heads/main/security/bemis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bemis-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bemis-company-inc-
- group: other
  title: Amcor
  type: Successor
  url: https://www.amcor.com
coverage:
  checked: '2026-09-19'
  detail: Bemis Company was fully absorbed into Amcor on 11 June 2019 and its own domain bemis.com 301s every path, including /.well-known/* and /developers, to the Amcor homepage, while the only site still trading under the Bemis name, www.bemisus.com, is an unrelated domain registered 2025-12-22 that is not wired here.
  evidence:
  - status: 301
    url: https://www.bemis.com/
  - status: 301
    url: https://www.bemis.com/developers
  - status: 404
    url: https://www.amcor.com/.well-known/api-catalog
  - status: 404
    url: https://www.amcor.com/openapi.json
  - status: 404
    url: https://www.bemisus.com/openapi.json
  reason: defunct
  state: none
created: '2026-03-23'
description: 'Bemis Company, Inc. was a global manufacturer of flexible packaging for food, beverage, personal care and healthcare markets. Founded in 1858 and headquartered in Neenah, Wisconsin, it completed a $6.8 billion all-stock merger with Amcor Limited on 11 June 2019 and was fully absorbed into Amcor: bemis.com now 301s to www.amcor.com and the Bemis businesses, including its healthcare packaging unit, operate as Amcor Flexibles. Bemis never ran a developer program, and no public API surface exists to profile; www.bemisus.com, which presents itself as Bemis, is an unrelated domain registered in December 2025.'
features:
- description: Bemis/Amcor manufactures flexible packaging solutions for food, beverage, personal care, and pharmaceutical markets, including pouches, films, bags, and lidding materials.
  name: Flexible Packaging Manufacturing
- description: FDA-compliant packaging solutions for medical devices, pharmaceuticals, and diagnostics, manufactured under ISO 13485 and ISO 9001 quality management systems.
  name: Healthcare and Pharmaceutical Packaging
- description: Bemis and Amcor invest in recyclable, compostable, and reduced-material packaging innovations as part of the combined company's sustainability commitments.
  name: Sustainable Packaging
- description: The combined Bemis/Amcor manufacturing network spans 40+ countries with hundreds of manufacturing facilities serving consumer goods companies, retailers, and pharmaceutical manufacturers worldwide.
  name: Global Manufacturing Network
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bemis.png
integrations:
- description: Bemis Company completed its merger with Amcor Limited in June 2019 in a $6.8 billion all-stock transaction, creating a single global packaging leader operating under the Amcor brand.
  name: Amcor
layout: provider
modified: '2026-09-19'
name: Bemis
nav: Providers
network: true
overview: Bemis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Amcor, Consumer Packaging, Flexible Packaging, Food Packaging, and Healthcare Packaging.
press:
- date: ''
  title: Bemis Company in $6.8 Billion Merger With Amcor
  url: https://www.clearygottlieb.com/news-and-insights/news-listing/bemis-company-in-6-8-billion-merger-with-amcor
- date: ''
  title: Bemis Co. receives silver award from FTA
  url: https://www.packworld.com/home/press-release/13377625/bemis-co-receives-silver-award-from-fta
- date: ''
  title: Bemis Associates, Inc. (“Bemis”), one of the global leaders in ...
  url: https://www.facebook.com/100090941572524/posts/bemis-associates-inc-bemis-one-of-the-global-leaders-in-bonding-and-material-inn/911655875209123/
- date: ''
  title: Amcor Completes Acquisition of Bemis, Creating the ...
  url: https://www.prnewswire.com/news-releases/amcor-completes-acquisition-of-bemis-creating-the-global-leader-in-consumer-packaging-300865415.html
- date: ''
  title: /C O R R E C T I O N -- Bemis Associates Inc/
  url: https://www.newswire.ca/news-releases/bemis-associates-appoints-christina-chen-as-president-and-chief-operating-officer-885168229.html
random_paper: 0
screenshot: https://raw.githubusercontent.com/api-evangelist/bemis/refs/heads/main/screenshots/bemis-2026-06-20T173134.png
security:
- kind: domain-security
  name: Bemis Domain Security
  slug: bemis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bemis
tags:
- Amcor
- Consumer Packaging
- Flexible Packaging
- Food Packaging
- Healthcare Packaging
- Manufacturing
- Packaging
- Pharmaceutical Packaging
use_cases:
- description: Flexible packaging for snack foods, dairy, frozen foods, beverages, and other consumer food products requiring barrier properties, shelf-life extension, and retail presentation.
  name: Food and Beverage Packaging
- description: FDA-registered, ISO-certified flexible packaging for pharmaceuticals, medical devices, and diagnostic products requiring sterile barrier protection and regulatory compliance.
  name: Pharmaceutical and Medical Device Packaging
- description: Flexible packaging and films for cosmetics, personal care, and household product brands requiring printability, material compatibility, and supply chain efficiency.
  name: Personal Care Packaging
---
