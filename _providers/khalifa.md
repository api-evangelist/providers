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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Public open-source repositories from the Khalifa University Center for Autonomous Robotic Systems (KUCARS), covering autonomous robotics topics such as coverage path planning, soft manipulator dynamic
  name: KUCARS Open-Source Robotics Research (GitHub)
  slug: kucars
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/khalifa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ku.ac.ae
- group: build
  title: ''
  type: Library
  url: https://library.ku.ac.ae
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kucars
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/khalifauniversity/
- group: commercial
  title: ''
  type: Plans
  url: plans/khalifa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/khalifa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/khalifa-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Khalifa University of Science and Technology is a research-intensive university in Abu Dhabi, United Arab Emirates, ranked #202 in the QS World University Rankings 2025. It operates colleges of Engineering and Physical Sciences, Computing and Mathematical Sciences, and Medicine and Health Sciences, along with multiple research centers. No central public, documented developer or API program was found; student and administrative systems (KU Connect portal, Banner registration, e-Learn, library discovery) are gated behind institutional authentication. The only confirmed public code footprint is the GitHub organization of its Center for Autonomous Robotic Systems (KUCARS), which publishes open-source robotics research repositories rather than a managed, documented API.'
finops:
- name: Khalifa Finops
  service_category: Education
  slug: khalifa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/khalifa.png
jsonld:
- class_count: 14
  name: Khalifa Context
  property_count: 2
  slug: khalifa-context
layout: provider
modified: '2026-06-03'
name: Khalifa University
nav: Providers
network: true
overview: 'Khalifa University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Robotics.


  The Khalifa University catalog on APIs.io includes 1 JSON-LD context.


  Khalifa University''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Khalifa Plans Pricing
  plan_count: 2
  slug: khalifa-plans-pricing
random_paper: 124
rate_limits:
- limit_count: 1
  name: Khalifa Rate Limits
  slug: khalifa-rate-limits
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/khalifa/refs/heads/main/screenshots/khalifa-2026-06-20T184031.png
security:
- kind: domain-security
  name: Khalifa Domain Security
  slug: khalifa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: khalifa
tags:
- Education
- Higher Education
- University
- Research
- Robotics
- United Arab Emirates
- Abu Dhabi
website: https://www.ku.ac.ae
---
