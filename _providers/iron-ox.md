---
api_count: 0
artifact_total: 0
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iron-ox
- group: other
  title: ''
  type: CompanyProfile
  url: https://www.ycombinator.com/companies/iron-ox
- group: company
  title: ''
  type: Press
  url: https://techcrunch.com/2021/09/23/robotic-farming-firm-iron-ox-raises-53m/
- group: company
  title: ''
  type: Press
  url: https://www.cnbc.com/2022/04/18/iron-ox-is-disrupting-agriculture-with-robots-and-ai.html
- group: company
  title: ''
  type: Press
  url: https://techcrunch.com/2022/11/03/iron-ox-lays-off-50-amounting-to-nearly-half-its-staff/
- group: company
  title: ''
  type: Press
  url: https://www.therobotreport.com/reports-of-layoffs-at-iron-ox/
- group: company
  title: ''
  type: Press
  url: https://agfundernews.com/another-blow-for-indoor-farm-robotics-as-iron-ox-lays-off-nearly-half-its-staff
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/iron-ox-well-known.yml
coverage:
  checked: '2026-08-23'
  detail: Iron Ox ceased operations in mid-2023 and ironox.com is now a GoDaddy parking lander that answers HTTP 200 with the same 114-byte redirect to /lander for every path, including /openapi.json and every /.well-known/ document.
  evidence:
  - status: 200
    url: https://ironox.com/
  - status: 200
    url: https://ironox.com/openapi.json
  - status: 200
    url: https://ironox.com/.well-known/agent-card.json
  - status: 0
    url: https://api.ironox.com/
  - status: 404
    url: http://web.archive.org/web/20230812090055/https://ironox.com/
  - status: 200
    url: https://github.com/iron-ox
  reason: defunct
  state: none
created: '2026-08-23'
description: 'Iron Ox (legally Inevitable Tech, Inc.) was a San Carlos, California robotics company that built autonomous indoor farms — hydroponic greenhouses worked by mobile transport robots and a robotic arm that seeded, moved, imaged and harvested leafy greens and herbs, with machine learning used to spot pests and disease plant by plant. Founded in 2015 by Brandon Alexander and Jon Binney, it went through Y Combinator (W16), raised roughly $98 million in total including a $53 million Series C led by Breakthrough Energy Ventures in September 2021, and ran greenhouses in Gilroy, California and Lockhart, Texas. It cut about half its staff — roughly 50 people — in November 2022 and ceased operations in mid-2023. Iron Ox never ran a developer program: it sold produce, not software, and the only public code it ever shipped was internal ROS robotics tooling on GitHub. Its site, ironox.com, is now a GoDaddy parking lander and every developer subdomain has been removed from DNS, so there is
  no API, specification, SDK or documentation surface left to profile.'
image: https://avatars.githubusercontent.com/u/15058167?v=4
layout: provider
modified: '2026-08-23'
name: Iron Ox
nav: Providers
network: true
overview: Iron Ox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Robotics, and Automation.
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/iron-ox/refs/heads/main/screenshots/iron-ox-2026-09-02T145924.png
slug: iron-ox
tags:
- Company
- Agriculture
- AgTech
- Robotics
- Automation
- Indoor Farming
- Controlled Environment Agriculture
- Machine-Learning
- Climate Tech
- Defunct
---
