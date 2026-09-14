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
  url: security/slalom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slalom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.slalom.com/us/en
- group: company
  title: ''
  type: Blog
  url: https://www.slalom.com/us/en/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/slalombuild
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.slalom.com/us/en/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.slalom.com/us/en/legal/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/slalom-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/slalom-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/slalom-security.txt
- group: auth
  title: ''
  type: Security
  url: security/slalom-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/slalom-packages.yml
coverage:
  checked: '2026-08-28'
  detail: 'Slalom is a consulting firm that sells engagements, not software products: its 705-page US sitemap contains no developer, API, or documentation section, and no OpenAPI, GraphQL, MCP or agent-card probe hit on either www.slalom.com or www.slalombuild.com.'
  evidence:
  - status: 404
    url: https://www.slalom.com/openapi.json
  - status: 404
    url: https://www.slalom.com/.well-known/api-catalog
  - status: 404
    url: https://www.slalombuild.com/openapi.json
  - status: 200
    url: https://www.slalom.com/content/slalom.sitemap.us-sitemap.xml
  - status: 200
    url: https://www.slalom.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-28'
description: Slalom is a global business and technology consulting firm headquartered in Seattle, Washington, founded in 2001 and privately held, with roughly 12,000 employees across dozens of markets in North America, Europe, Asia and Australia. The firm delivers strategy, artificial intelligence, data, cloud and engineering, customer experience, legacy modernization, digital product building, and privacy and security consulting, and operates the Slalom Build brand for custom software, data platform and product engineering work. Slalom is a delivery partner for Microsoft, AWS, Salesforce, Google Cloud, Adobe and NVIDIA. It sells consulting engagements rather than software, and publishes no public developer program, API reference or machine-readable API contract; the machine-readable surface it does publish is an llms.txt at its marketing root and a security.txt on the Slalom Build site.
image: https://www.slalom.com/content/dam/slalom/global-assets/Slalom_OG_Image.png
layout: provider
modified: '2026-08-28'
name: Slalom
nav: Providers
network: true
overview: 'Slalom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consulting, Professional Services, Technology Consulting, and Artificial Intelligence.


  Slalom''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 18
screenshot: https://raw.githubusercontent.com/api-evangelist/slalom/refs/heads/main/screenshots/slalom-2026-09-02T155829.png
security:
- kind: domain-security
  name: Slalom Domain Security
  slug: slalom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Slalom Vulnerability Disclosure
  slug: slalom-vulnerability-disclosure
  summary_line: contact published
slug: slalom
tags:
- Company
- Consulting
- Professional Services
- Technology Consulting
- Artificial Intelligence
- Cloud
- Data
- Digital Transformation
- Systems Integration
website: https://www.slalom.com/us/en
---
