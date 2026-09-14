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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conagra-foods-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conagra-foods-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.conagrabrands.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/conagra
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/conagra-brands
- group: other
  title: ''
  type: Active Profile
  url: https://raw.githubusercontent.com/api-evangelist/conagra-brands/refs/heads/main/apis.yml
- group: other
  title: ''
  type: Lamb Weston (spin-off)
  url: https://www.lambweston.com
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Conagra_Brands
coverage:
  checked: '2026-09-05'
  detail: The ConAgra Foods brand was retired in 2015 when the company renamed to Conagra Brands and spun off Lamb Weston; conagrafoods.com now 301s to conagrabrands.com, whose www host returns a clean 404 on every discovery path and whose GitHub organization publishes zero public repositories.
  evidence:
  - status: 301
    url: https://conagrafoods.com/
  - status: 404
    url: https://www.conagrabrands.com/.well-known/api-catalog
  - status: 404
    url: https://www.conagrabrands.com/openapi.json
  - status: 200
    url: https://api.github.com/orgs/conagra/repos
  reason: defunct
  state: none
created: '2025-03-23'
description: ConAgra Foods, Inc. was the prior corporate name of Conagra Brands. In 2015 the company spun off its foodservice ingredients business as Lamb Weston and renamed the remaining packaged-foods business to Conagra Brands, Inc. This profile is preserved as a historical alias; the active company profile lives at the conagra-brands repository. No public developer APIs were ever published under the ConAgra Foods brand.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/conagra-foods.png
layout: provider
modified: '2026-09-05'
name: ConAgra Foods
nav: Providers
network: true
overview: ConAgra Foods is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Alias, Branded Foods, CPG, Consumer Packaged Goods, and Historical.
press:
- date: '2026-05-25'
  title: News Releases
  url: https://www.conagrabrands.com/news-room?item=g7rqBLVLuv81UAmrh20MpxJ7whd2MIUrZeqRYSE1VVd0o0Mz97ZvF3kIoFPSkQSwCdLW/Q7F9G0BAX%20xuSO0vw%3D%3D&news-release-category=All&news-release-keyword=&news-release-year=All&t=2&page=6
- date: '2026-05-25'
  title: Company Leadership
  url: https://www.conagrabrands.com/our-company/corporate-leadership
- date: '2026-05-25'
  title: News Releases
  url: https://www.conagrabrands.com/news-room?c=202310&p=sustainable_energy&page=6
- date: '2026-05-25'
  title: Conagra Brands Strategic Audit - DigitalCommons@UNL
  url: https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1855&context=honorstheses
- date: '2026-05-25'
  title: Conagra Brands Enhances its Artificial Intelligence Capabilities ...
  url: https://www.stlamerican.com/online-features/press-releases/conagra-brands-enhances-its-artificial-intelligence-capabilities-with-human-centered-approach/
random_paper: 13
security:
- kind: domain-security
  name: Conagra Foods Domain Security
  slug: conagra-foods-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: conagra-foods
tags:
- Alias
- Branded Foods
- CPG
- Consumer Packaged Goods
- Historical
- Renamed
- Fortune 500
website: https://www.conagrabrands.com
---
