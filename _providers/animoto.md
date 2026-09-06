---
access_model:
  confidence: medium
  label: Public self-service product; API access closed
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://animoto.com/pricing
  - https://animoto.com/sign-up
  - https://api.animoto.com/jobs/
  trial: true
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Animoto API is a partner-facing RESTful web service for programmatically directing and rendering videos from images, video clips, music and text. The host is live and authenticating (HTTP Basic, r
  name: Animoto API
  slug: api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://animoto.com/
- group: company
  title: ''
  type: Blog
  url: https://animoto.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://animoto.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.animoto.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://animoto.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://animoto.com/log_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://animoto.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://animoto.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/animoto
- group: auth
  title: ''
  type: Compliance
  url: https://help.animoto.com/hc/en-us/articles/360004421634-General-Data-Protection-Regulation-GDPR-and-Animoto
- group: auth
  title: ''
  type: DomainSecurity
  url: security/animoto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/animoto-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/animoto-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/animoto-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/animoto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/animoto-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/animoto-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/animoto-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/animoto-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/animoto-llms.txt
coverage:
  checked: '2026-08-13'
  detail: 'Animoto''s API host api.animoto.com is live and answers every path with HTTP 401 and WWW-Authenticate: Basic realm="Application", while the public developer surface has been withdrawn — animoto.com/developer returns 200 but serves the marketing homepage byte-for-byte and the help center''s "Developer Resources" section (id 200768337) contains zero published articles.'
  evidence:
  - status: 401
    url: https://api.animoto.com/jobs/
  - status: 200
    url: https://animoto.com/developer
  - status: 0
    url: https://developer.animoto.com/
  - status: 404
    url: https://animoto.com/.well-known/agent-card.json
  - status: 200
    url: https://rubygems.org/api/v1/gems/animoto.json
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: 'Animoto is a cloud-based video creation platform, founded in 2006 and headquartered in New York City, that lets anyone turn photos, video clips, screen recordings and music into professional-looking videos through a drag-and-drop web editor and a large library of customizable templates. It is widely used for marketing and social-media videos, e-commerce and product promos, slideshows, real-estate tours, training and internal communications, and personal celebration videos, and is sold as subscription SaaS across free, Basic, Professional and Professional Plus tiers. Animoto is part of the Redbrick family of brands. It was surfaced as a portfolio company of kindred-ventures. Animoto formerly ran a partner-facing REST API for programmatic video directing and rendering: the API host api.animoto.com is still live and answers every request with an HTTP Basic challenge, but the developer program around it has been retired — animoto.com/developer now serves the marketing homepage,
  developer.animoto.com and the documented partner sandbox hosts no longer resolve, the help center Developer Resources section is empty, and the official Animoto API Ruby client has not been released since 2013.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/animoto.png
layout: provider
modified: '2026-08-13'
name: Animoto
nav: Providers
network: true
overview: 'Animoto publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Video, Video Creation, and Video Editing.


  Animoto''s developer surface includes engineering blog, pricing, support, signup flow, authentication, changelog, and 14 more developer resources.'
plans:
- name: Animoto Plans Pricing
  plan_count: 4
  slug: animoto-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Animoto Rate Limits
  slug: animoto-rate-limits
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 32.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Animoto Authentication
  slug: animoto-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Animoto Domain Security
  slug: animoto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: animoto
tags:
- Company
- Consumer
- Video
- Video Creation
- Video Editing
- Slideshow
- Marketing
- Social-Media
- Content Creation
- Software-as-a-Service
website: https://animoto.com/
---
