---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Netflix Open Connect is the purpose-built content delivery network that delivers Netflix streaming traffic. The Open Connect program provides partner ISPs with embedded appliances and peering arrangem
  name: Netflix Open Connect
  slug: netflix-open-connect
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/netflix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netflix-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netflix
- group: company
  title: ''
  type: Website
  url: https://www.netflix.com
- group: other
  title: ''
  type: Open Connect
  url: https://openconnect.netflix.com/
- group: company
  title: ''
  type: TechBlog
  url: https://netflixtechblog.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Netflix
- group: operate
  title: ''
  type: Partner Help Center
  url: https://partnerhelp.netflixstudios.com/
- group: company
  title: ''
  type: Jobs
  url: https://jobs.netflix.com/
- group: company
  title: ''
  type: About
  url: https://about.netflix.com/
created: '2026-03-21'
description: Netflix is a streaming entertainment service operating one of the world's largest content delivery networks. While Netflix does not publish a general public consumer API, it operates partner programs including Open Connect for ISP CDN integration and device certification programs for manufacturers embedding the Netflix application.
finops:
- name: Netflix Finops
  service_category: Media + CDN
  slug: netflix-finops
graphqls:
- description: Netflix does not publish a general-purpose public GraphQL API. This schema is a conceptual representation of the Netflix data model derived from publicly available information, including the Netflix T
  name: Netflix GraphQL Schema
  slug: netflix-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netflix.png
layout: provider
modified: '2026-07-25'
name: Netflix
nav: Providers
network: true
overview: Netflix publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CDN, Content Delivery, Device Certification, Entertainment, and Media.
plans:
- name: Netflix Plans Pricing
  plan_count: 2
  slug: netflix-plans-pricing
press:
- date: '2026-05-25'
  title: Netflix goes 'all in' on generative AI as entertainment ...
  url: https://www.reddit.com/r/technology/comments/1od4h2j/netflix_goes_all_in_on_generative_ai_as/
- date: '2026-05-25'
  title: Netflix 'all in' on leveraging AI in its streaming platform
  url: https://www.cnbc.com/2025/10/22/netflix-all-in-on-leveraging-ai-in-its-streaming-platform.html
- date: '2026-05-25'
  title: Using Generative AI in Content Production
  url: https://partnerhelp.netflixstudios.com/hc/en-us/articles/43393929218323-Using-Generative-AI-in-Content-Production
- date: '2026-05-25'
  title: Machine Learning
  url: https://research.netflix.com/research-area/machine-learning
- date: '2026-05-25'
  title: Netflix aims to be an innovator in using AI in the creative ...
  url: https://www.instagram.com/reel/DXNX3-8DBcV/?hl=en
random_paper: 14
rate_limits:
- limit_count: 2
  name: Netflix Rate Limits
  slug: netflix-rate-limits
score:
  band: emerging
  composite: 17.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 17.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netflix/refs/heads/main/screenshots/netflix-2026-06-20T190152.png
security:
- kind: domain-security
  name: Netflix Domain Security
  slug: netflix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Netflix Vulnerability Disclosure
  slug: netflix-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: netflix
tags:
- CDN
- Content Delivery
- Device Certification
- Entertainment
- Media
- Netflix
- Open Connect
- Streaming
- Fortune 500
website: https://www.netflix.com
---
