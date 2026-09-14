---
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.advexai.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdvexAI
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advex-ai-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/advex-ai-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advex-ai-llms.txt
coverage:
  checked: '2026-09-09'
  detail: Advex sells Composer as an on-premises visual-inspection appliance (the "Advex box") driven by a no-code UI and explicitly designed to run on-device without network connectivity, so it has never published an API, developer portal, SDK or machine-readable spec — its own site's entire navigation was Use Cases, Benefits, Pricing, FAQ, Blog and Book A Demo — and as of this check even that site is unpublished, answering HTTP 404 from an empty Framer origin on every host and path.
  evidence:
  - status: 404
    url: https://www.advexai.com/
  - status: 301
    url: https://advex.ai/
  - status: 404
    url: https://www.advexai.com/openapi.json
  - status: 404
    url: https://www.advexai.com/.well-known/security.txt
  - status: 200
    url: https://api.github.com/orgs/AdvexAI
  - status: 200
    url: http://web.archive.org/web/20260612174810/https://www.advexai.com/
  reason: no-developer-program
  state: none
created: '2026-09-09'
description: Advex AI (Advex AI, Inc., San Francisco / Pleasanton, California; founded 2022 by Pedro Pachuca and Qasim Wani) builds generative-AI synthetic data and self-healing computer vision for industrial quality inspection. Its flagship product, Composer, is a no-code AI vision system that lets manufacturing and logistics teams train, deploy and manage visual inspection tasks — defect and anomaly detection, pick-and-place, kitting and assembly verification, counting — from a handful of real images, using diffusion models to synthesize the missing training data and VLMs to run the inspection. Composer is sold as an on-premises appliance (the "Advex box") paired with plant cameras and is explicitly designed to run entirely on-device without network connectivity. The company raised a $3.5M seed round in November 2024 led by Construct Capital with Pear VC and Emerson Collective. As of this profile Advex publishes no public API, developer portal, SDK or machine-readable specification of
  any kind, and its own website is currently unpublished.
image: https://avatars.githubusercontent.com/u/119636653?v=4
layout: provider
modified: '2026-09-09'
name: Advex AI
nav: Providers
network: true
overview: Advex AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Computer Vision, Synthetic Data, and Manufacturing.
plans:
- name: Advex Ai Plans Pricing
  plan_count: 0
  slug: advex-ai-plans-pricing
random_paper: 6
security:
- kind: domain-security
  name: Advex Ai Domain Security
  slug: advex-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: advex-ai
tags:
- Company
- Artificial Intelligence
- Computer Vision
- Synthetic Data
- Manufacturing
- Machine Learning
- Quality Inspection
- Industrial Automation
website: https://www.advexai.com/
---
