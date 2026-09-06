---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'White-label AI travel agent that travel companies can embed on their own site, customized with brand voice, colors, and inventory. Marketed as a low-code / no-code deployment with commission share on '
  name: Layla for Brands (White Label)
  slug: layla-for-brands
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/layla-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/layla-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://layla.ai/
- group: company
  title: ''
  type: About
  url: https://layla.ai/about
- group: company
  title: ''
  type: Partners
  url: https://layla.ai/partners
- group: company
  title: ''
  type: Newsletter
  url: https://justasklayla.substack.com/
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/layla-7376
- group: commercial
  title: ''
  type: Plans
  url: plans/layla-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/layla-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/layla-ai-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://layla.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://justasklayla.substack.com/feed
created: '2026-05-23'
description: Layla is an AI travel agent that plans trips conversationally, generating itineraries with flights, hotels, activities, and restaurants wired into real booking inventory from partners such as Booking.com and Skyscanner. The consumer product is at layla.ai; a Layla for Brands white-label offering lets travel companies embed an AI travel agent into their own site with their own branding and inventory.
finops:
- name: Layla Ai Finops
  service_category: API
  slug: layla-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/layla-ai.png
layout: provider
modified: '2026-07-25'
name: Layla AI
nav: Providers
network: true
overview: 'Layla AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Travel, Itinerary Planning, Conversational AI, and White Label.


  Layla AI''s developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Layla Ai Plans Pricing
  plan_count: 1
  slug: layla-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Layla Ai Rate Limits
  slug: layla-ai-rate-limits
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/layla-ai/refs/heads/main/screenshots/layla-ai-2026-06-20T184413.png
security:
- kind: domain-security
  name: Layla Ai Domain Security
  slug: layla-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Layla Ai Vulnerability Disclosure
  slug: layla-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: layla-ai
tags:
- Artificial Intelligence
- Travel
- Itinerary Planning
- Conversational AI
- White Label
- Booking
- Consumer
website: https://layla.ai/
---
