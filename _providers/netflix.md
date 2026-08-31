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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-30'
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
random_paper: 6
rate_limits:
- limit_count: 2
  name: Netflix Rate Limits
  slug: netflix-rate-limits
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 20.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
