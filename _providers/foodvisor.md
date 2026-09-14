---
access_model:
  confidence: medium
  label: Unknown — no API is offered
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - lifecycle
  trial: false
  try_now: false
api_count: 1
apis:
- description: RETIRED. A commercial computer-vision API that detected food items in a photograph and returned nutritional facts including calories and macronutrients. Endpoint and authentication details were issued
  name: Foodvisor Vision API (retired)
  slug: vision
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.foodvisor.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Foodvisor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/foodvisor
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.foodvisor.io/en/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.foodvisor.io/en/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.foodvisor.io/en/signup/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foodvisor-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/foodvisor-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/foodvisor-llms.txt
coverage:
  checked: '2026-09-10'
  detail: 'Foodvisor retired its Vision API: the product page /en/vision/ now returns HTTP 404, the documentation host vision.foodvisor.io is NXDOMAIN from three resolvers, and the live marketing SPA''s router declares no /vision/, /api/ or /developers/ route at all — the company ships only the consumer app now.'
  evidence:
  - status: 404
    url: https://www.foodvisor.io/en/vision/
  - status: 0
    url: https://vision.foodvisor.io/docs/
  - status: 404
    url: https://api.foodvisor.io/openapi.json
  - status: 404
    url: https://www.foodvisor.io/.well-known/api-catalog
  - status: 404
    url: https://www.foodvisor.io/llms.txt
  reason: no-developer-program
  state: none
created: '2025-03-01'
description: 'Foodvisor is a French mobile nutrition platform whose app identifies food items from a photograph using computer vision and returns nutritional information — calories, macronutrients and portion estimates. Between 2023 and 2025 Foodvisor also sold that capability to developers as the Foodvisor Vision API, a commercial image-recognition and nutrition-analysis service documented at vision.foodvisor.io. That developer product has since been withdrawn: the Vision product page now returns HTTP 404, the documentation host no longer resolves in DNS, and the live site carries no API, developer or enterprise content. Foodvisor today publishes no machine-readable contract, no SDK, no MCP server and no /.well-known document, and operates as a consumer subscription app.'
finops:
- name: Foodvisor Finops
  service_category: ''
  slug: foodvisor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/foodvisor.png
layout: provider
modified: '2026-09-10'
name: Foodvisor
nav: Providers
network: true
overview: 'Foodvisor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Computer-Vision, Food, Health, and Nutrition.


  Foodvisor''s developer surface includes signup flow and 8 more developer resources.'
plans:
- name: Foodvisor Plans Pricing
  plan_count: 0
  slug: foodvisor-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Foodvisor Rate Limits
  slug: foodvisor-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/foodvisor/refs/heads/main/screenshots/foodvisor-2026-06-20T181405.png
security:
- kind: domain-security
  name: Foodvisor Domain Security
  slug: foodvisor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: foodvisor
tags:
- Artificial Intelligence
- Computer-Vision
- Food
- Health
- Nutrition
- Mobile
website: https://www.foodvisor.io/
---
