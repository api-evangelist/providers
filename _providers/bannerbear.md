---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Bannerbear Agentic Access
  operation_count: 29
  slug: bannerbear-agentic-access
  summary_line: 29 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.bannerbear.com/v2
  baseurl_source: declared
  description: Build animated GIFs from template frames.
  name: Bannerbear Animated GIFs API
  slug: bannerbear-animated-gifs-api
- baseURL: https://api.bannerbear.com/v2
  baseurl_source: declared
  description: API key verification and account status.
  name: Bannerbear Auth API
  slug: bannerbear-auth-api
- baseURL: https://api.bannerbear.com/v2
  baseurl_source: declared
  description: Generate multiple images from a template set.
  name: Bannerbear Collections API
  slug: bannerbear-collections-api
- baseURL: https://api.bannerbear.com/v2
  baseurl_source: declared
  description: Reference fonts and effects.
  name: Bannerbear Fonts API
  slug: bannerbear-fonts-api
- baseURL: https://api.bannerbear.com/v2
  baseurl_source: declared
  description: Auto-generate images from templates.
  name: Bannerbear Images API
  slug: bannerbear-images-api
- baseURL: https://api.bannerbear.com/v2
  baseurl_source: declared
  description: Capture web page screenshots by URL.
  name: Bannerbear Screenshots API
  slug: bannerbear-screenshots-api
- baseURL: https://api.bannerbear.com/v2
  baseurl_source: declared
  description: Manage templates and template sets.
  name: Bannerbear Templates API
  slug: bannerbear-templates-api
- baseURL: https://api.bannerbear.com/v2
  baseurl_source: declared
  description: Render videos from video templates.
  name: Bannerbear Videos API
  slug: bannerbear-videos-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bannerbear Animated GIFs API
  slug: open-bannerbear-animated-gifs-api
- collection_type: open
  name: Bannerbear Animated GIFs Auth API
  slug: open-bannerbear-auth-api
- collection_type: open
  name: Bannerbear Animated GIFs Collections API
  slug: open-bannerbear-collections-api
- collection_type: open
  name: Bannerbear Animated GIFs Fonts API
  slug: open-bannerbear-fonts-api
- collection_type: open
  name: Bannerbear Animated GIFs Images API
  slug: open-bannerbear-images-api
- collection_type: open
  name: Bannerbear Animated GIFs Screenshots API
  slug: open-bannerbear-screenshots-api
- collection_type: open
  name: Bannerbear Animated GIFs Templates API
  slug: open-bannerbear-templates-api
- collection_type: open
  name: Bannerbear Animated GIFs Videos API
  slug: open-bannerbear-videos-api
- collection_type: open
  name: Bannerbear API
  slug: open-bannerbear
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bannerbear-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bannerbear-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bannerbear-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.bannerbear.com/blog/feed.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yongfook
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bannerbear
- group: company
  title: ''
  type: Website
  url: https://www.bannerbear.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bannerbear.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/bannerbear-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bannerbear-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bannerbear-finops.yml
created: '2026-06-20'
description: Bannerbear is an API-first platform for auto-generating images and videos from reusable templates. A single REST API call applies text, image, and color modifications to a template and renders branded marketing visuals, social media graphics, animated GIFs, screenshots, and videos at scale, with asynchronous webhook and polling delivery.
finops:
- name: Bannerbear Finops
  service_category: Media and Content
  slug: bannerbear-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bannerbear.png
layout: provider
modified: '2026-06-20'
name: Bannerbear
nav: Providers
network: true
overview: 'Bannerbear publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Animated GIFs API, Auth API, Collections API, and 5 more. Tagged areas include Image-Generation, Video Generation, Templates, Media, and Automation.


  Bannerbear''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Bannerbear Plans Pricing
  plan_count: 4
  slug: bannerbear-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Bannerbear Rate Limits
  slug: bannerbear-rate-limits
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 50.5
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bannerbear/refs/heads/main/screenshots/bannerbear-2026-06-20T172954.png
security:
- kind: authentication
  name: Bannerbear Authentication
  slug: bannerbear-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bannerbear Domain Security
  slug: bannerbear-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bannerbear
tags:
- Image-Generation
- Video Generation
- Templates
- Media
- Automation
website: https://www.bannerbear.com
---
