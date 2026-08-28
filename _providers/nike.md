---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Nike provides APIs for product catalog access, inventory, store locations, and e-commerce integration. The platform supports partners and developers building experiences around Nike products.
  name: Nike Developer API
  slug: nike-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nike-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://about.nike.com/en/newsroom
description: Nike is the world's largest supplier of athletic shoes and apparel and a major manufacturer of sports equipment, designing, developing, and marketing products under the Nike, Jordan, and Converse brands.
finops:
- name: Nike Finops
  service_category: Retail + E-Commerce
  slug: nike-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nike.png
layout: provider
modified: '2026-04-28'
name: nike
nav: Providers
network: true
overview: 'nike publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500.


  nike''s developer surface includes engineering blog and 1 more developer resources.'
plans:
- name: Nike Plans Pricing
  plan_count: 1
  slug: nike-plans-pricing
press:
- date: '2026-05-25'
  title: Nike Unveils Project Amplify, the World's First Powered ...
  url: https://about.nike.com/en/newsroom/releases/nike-project-amplify-official-images
- date: '2026-05-25'
  title: 'Nike on Instagram: "There is no finish line when it comes to ...'
  url: https://www.instagram.com/reel/DQJxDm9joWp/?hl=en
- date: '2026-05-25'
  title: Nike uses AI for personalized retail, boosts digital sales
  url: https://www.linkedin.com/posts/adrian-pearson-jr-474089239_nike-ai-retailinnovation-activity-7380664867831283713-Hh9H
- date: '2026-05-25'
  title: Nike Debuts its First Neuroscience-Based Footwear to ...
  url: https://about.nike.com/en/newsroom/releases/nike-mind-001-mind-002-official-images
- date: '2026-05-25'
  title: Nike Creates New Innovation Engine to Power Athletes ...
  url: https://about.nike.com/en/newsroom/releases/nike-new-innovation-engine-announcement
random_paper: 3
rate_limits:
- limit_count: 1
  name: Nike Rate Limits
  slug: nike-rate-limits
score:
  band: emerging
  composite: 11.1
  delta: 1.9
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 9.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nike/refs/heads/main/screenshots/nike-2026-06-20T190340.png
security:
- kind: domain-security
  name: Nike Domain Security
  slug: nike-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nike
tags:
- Fortune 500
---
