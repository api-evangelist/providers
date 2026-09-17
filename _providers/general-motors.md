---
access_model:
  confidence: high
  label: Enterprise — approved customers and partners only
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - https://developer.gm.com/explore-apis
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: You can reach customers in their cars using GMs powerful, in-vehicle platform. Our tools can provide access to close to 200 data points, allowing you to monitor vehicle data in real-time to deliver th
  name: General Motors
  slug: general-motors
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/general-motors/refs/heads/main/security/general-motors-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/general-motors-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/generalmotors
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/general-motors
- group: company
  title: ''
  type: Website
  url: https://www.gm.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gm.com/docs/api-data-services
- group: docs
  title: ''
  type: APIReference
  url: https://developer.gm.com/explore-apis
- group: operate
  title: ''
  type: Support
  url: https://developer.gm.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://news.gm.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gm.com/privacy-statement
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/general-motors/refs/heads/main/security/general-motors-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/general-motors-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/general-motors/refs/heads/main/security/general-motors-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/general-motors-vulnerability-disclosure.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/general-motors/refs/heads/main/packages/general-motors-packages.yml
  title: ''
  type: Packages
  url: packages/general-motors-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/general-motors/refs/heads/main/llms/general-motors-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/general-motors-llms.txt
coverage:
  checked: '2026-09-12'
  detail: The GM Developer Portal is a single-page app whose own router guards every /docs/* route with requireCommercialAPIAccess and whose backend at https://developer.gm.com/v1 returns 403 to every anonymous request except GET /v1/csrf-token, so the API reference and any machine-readable contract are released only to customers GM has already approved for commercial API access.
  evidence:
  - status: 403
    url: https://developer.gm.com/v1/apis
  - status: 200
    url: https://developer.gm.com/v1/csrf-token
  - status: 404
    url: https://api.gm.com/openapi.json
  - status: 404
    url: https://api.onstarfleetintelligence.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2025-02-08'
description: You can reach customers in their cars using GMs powerful, in-vehicle platform. Our tools can provide access to close to 200 data points, allowing you to monitor vehicle data in real-time to deliver the content that matters, when it matters. Create an account now to start developing amazing in-vehicle experiences for your customers.
finops:
- name: General Motors Finops
  service_category: Automotive & Connected Services
  slug: general-motors-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/general-motors.png
layout: provider
modified: '2026-09-12'
name: General Motors
nav: Providers
network: true
overview: 'General Motors publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automobiles, Cars, Vehicles, Connected Vehicles, and Telematics.


  General Motors'' developer surface includes documentation, API reference, support, engineering blog, and 10 more developer resources.'
plans:
- name: General Motors Plans Pricing
  plan_count: 0
  slug: general-motors-plans-pricing
press:
- date: '2026-05-25'
  title: General Motors is using artificial intelligence to speed up ...
  url: https://www.facebook.com/AutoNews/posts/general-motors-is-using-artificial-intelligence-to-speed-up-vehicle-design-and-t/1587922703193457/
- date: '2026-05-25'
  title: GM's path to the future gets an AI infusion from NVIDIA
  url: https://investor.gm.com/news-releases/news-release-details/gms-path-future-gets-ai-infusion-nvidia
- date: '2026-05-25'
  title: GM, Nvidia to partner on AI tech for factories and next-gen ...
  url: https://www.wardsauto.com/news/archive-auto-gm-partner-with-nvidia-ai-technology-drive-agx-omniverse/742977/
- date: '2026-05-25'
  title: General Motors and NVIDIA Collaborate on AI for Next- ...
  url: https://investor.nvidia.com/news/press-release-details/2025/General-Motors-and-NVIDIA-Collaborate-on-AI-for-Next-Generation-Vehicle-Experience-and-Manufacturing/default.aspx
- date: '2026-05-25'
  title: Using AI to advance manufacturing at General Motors
  url: https://news.gm.com/home.detail.html/Pages/topic/us/en/2025/mar/0311-ai.html
random_paper: 3
rate_limits:
- limit_count: 0
  name: General Motors Rate Limits
  slug: general-motors-rate-limits
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 59.3
    operational_transparency: 13.2
  previous_composite: 18.0
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/general-motors/refs/heads/main/screenshots/general-motors-2026-06-20T181729.png
security:
- kind: authentication
  name: General Motors Authentication
  slug: general-motors-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: General Motors Domain Security
  slug: general-motors-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: General Motors Vulnerability Disclosure
  slug: general-motors-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: general-motors
tags:
- Automobiles
- Cars
- Vehicles
- Connected Vehicles
- Telematics
- Fortune 100
website: https://www.gm.com/
---
