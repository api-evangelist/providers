---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - http://www.451degrees.com/product/
  - http://www.451degrees.com/contact/
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
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/451-degrees-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/451-degrees-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/451-degrees-llms.txt
- group: company
  title: ''
  type: Website
  url: http://www.451degrees.com/
- group: other
  title: ''
  type: Product
  url: http://www.451degrees.com/product/
- group: company
  title: ''
  type: About
  url: http://www.451degrees.com/about/
- group: operate
  title: ''
  type: Support
  url: http://www.451degrees.com/contact/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/451degrees
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/451DegreesGraffiti
coverage:
  checked: '2026-08-12'
  detail: 451 Degrees markets Graffiti as integrating "with simple API construction to current Comment Platforms and Ad Delivery Networks" and its own investor one-sheet claims real-time APIs delivered to five ad networks, but the entire public surface is a four-page WordPress marketing site whose only developer call to action is "Contact Us for a Demo" — there is no reference, no portal, and api./developer./docs./dev./portal.451degrees.com are all NXDOMAIN.
  evidence:
  - status: 200
    url: http://www.451degrees.com/product/
  - status: 404
    url: http://www.451degrees.com/developers/
  - status: 404
    url: http://www.451degrees.com/openapi.json
  - status: 404
    url: http://www.451degrees.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: 451 Degrees is a marketing-technology and ad-tech company founded in 2006 that builds Graffiti, a patented AI content ecosystem for digital content and ad-tech businesses. Graffiti uses machine learning, artificial intelligence, and natural language processing to analyze user-generated comments and digital content in real time, converting comment "noise" into structured data that powers brand safety, contextual relevancy, content recommendation, and first-party data strategies. It is designed as a platform-agnostic tool that complements existing comment platforms, ad delivery networks, and content systems rather than replacing them, and markets itself as privacy-compliant with GDPR and CCPA while using no cookies, mobile IDs, or IDFA for targeting.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/451-degrees.png
layout: provider
modified: '2026-08-12'
name: 451 Degrees
nav: Providers
network: true
overview: '451 Degrees is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AdTech, Brand Safety, and Contextual Advertising.


  451 Degrees'' developer surface includes support and 8 more developer resources.'
plans:
- name: 451 Degrees Plans Pricing
  plan_count: 0
  slug: 451-degrees-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: 451 Degrees Rate Limits
  slug: 451-degrees-rate-limits
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/451-degrees/refs/heads/main/screenshots/451-degrees-2026-07-25T181204.png
security:
- kind: domain-security
  name: 451 Degrees Domain Security
  slug: 451-degrees-domain-security
  summary_line: DMARC
slug: 451-degrees
tags:
- Company
- Artificial Intelligence
- AdTech
- Brand Safety
- Contextual Advertising
- Content Moderation
- Natural Language Processing
- Machine-Learning
- Marketing Technology
- Privacy
website: http://www.451degrees.com/
---
