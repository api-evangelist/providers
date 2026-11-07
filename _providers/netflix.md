---
access_model:
  confidence: low
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Netflix Open Connect is the purpose-built content delivery network that delivers Netflix streaming traffic. The Open Connect program provides partner ISPs with embedded appliances and peering arrangem
  name: Netflix Open Connect
  slug: netflix-open-connect
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/netflix/plans/netflix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/netflix-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/netflix/rate-limits/netflix-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/netflix-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/netflix/finops/netflix-finops.yml
  title: ''
  type: FinOps
  url: finops/netflix-finops.yml
- group: auth
  href: https://artifacts.apis.io/netflix/security/netflix-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/netflix-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/netflix/security/netflix-domain-security.yml
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
- has_sources: true
  method: generated
  name: Netflix Finops
  primary_unit: ''
  service_category: Media + CDN
  slug: netflix-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netflix.png
layout: provider
modified: '2026-07-25'
name: Netflix
nav: Providers
network: true
overview: Netflix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CDN, Content Delivery, Device Certification, Entertainment, and Media.
plans:
- name: Netflix Plans Pricing
  plan_count: 2
  slug: netflix-plans-pricing
press:
- date: ''
  title: Netflix goes 'all in' on generative AI as entertainment ...
  url: https://www.reddit.com/r/technology/comments/1od4h2j/netflix_goes_all_in_on_generative_ai_as/
- date: ''
  title: Netflix 'all in' on leveraging AI in its streaming platform
  url: https://www.cnbc.com/2025/10/22/netflix-all-in-on-leveraging-ai-in-its-streaming-platform.html
- date: ''
  title: Using Generative AI in Content Production
  url: https://partnerhelp.netflixstudios.com/hc/en-us/articles/43393929218323-Using-Generative-AI-in-Content-Production
- date: ''
  title: Machine Learning
  url: https://research.netflix.com/research-area/machine-learning
- date: ''
  title: Netflix aims to be an innovator in using AI in the creative ...
  url: https://www.instagram.com/reel/DXNX3-8DBcV/?hl=en
random_paper: 18
rate_limits:
- limit_count: 2
  name: Netflix Rate Limits
  slug: netflix-rate-limits
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/netflix/netflix-2026-06-20T190152.png
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
