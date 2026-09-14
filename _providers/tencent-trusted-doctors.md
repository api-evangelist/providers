---
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.doctorwork.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doctorwork
- group: build
  title: ''
  type: Packages
  url: packages/tencent-trusted-doctors-packages.yml
coverage:
  checked: '2026-08-30'
  detail: The company was absorbed into Medlinker on 2021-01-01 and its brand retired in April 2021; its own primary domain www.xingren.com now returns a blanket HTTP 301 to www.medlinker.com, and the only surviving "开发者中心" at developer.doctorwork.com is internal employee tooling behind the company's own SSO (the page loads /_/sso/internal/user and an app bundle named "oa-dev-tools"), not a public developer portal.
  evidence:
  - status: 301
    url: https://www.xingren.com/
  - status: 200
    url: https://developer.doctorwork.com/
  - status: 404
    url: https://api.xingren.com/openapi.json
  - status: 301
    url: https://www.doctorwork.com/openapi.json
  - status: 404
    url: https://developer.doctorwork.com/.well-known/agent-card.json
  - status: 200
    url: https://github.com/doctorwork
  reason: defunct
  state: none
created: '2026-08-30'
description: Tencent Trusted Doctors (企鹅杏仁) was a Chinese digital-health group formed in August 2018 by merging Tencent's medical unit Tencent Doctorwork (企鹅医生) with the Shanghai doctor platform Trusted Doctors (杏仁医生). It combined an online consultation and doctor-social platform with a network of bricks-and-mortar clinics, connecting roughly 440,000 verified physicians to more than 10 million patients, and reached unicorn valuation on a USD 250M round in April 2019 backed by Tencent and Country Garden Ventures. The company was acquired by Medlinker (医联) with the deal completing 2021-01-01, and the 企鹅杏仁 brand was retired in April 2021 in favour of 未来医生 (Future Doctor). It never published a public developer program, API reference, or machine-readable contract, and its primary domain xingren.com now redirects wholesale to the acquirer.
layout: provider
modified: '2026-08-30'
name: Tencent Trusted Doctors
nav: Providers
network: true
overview: Tencent Trusted Doctors is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Telemedicine, and Digital Health.
random_paper: 15
slug: tencent-trusted-doctors
tags:
- Company
- Health
- Healthcare
- Telemedicine
- Digital Health
- Clinics
- China
- Acquired
website: https://www.doctorwork.com/
---
