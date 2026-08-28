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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iit-madras-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iitm.ac.in/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/IIT-Madras
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/school/reachiitm/
- group: commercial
  title: ''
  type: Plans
  url: plans/iit-madras-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iit-madras-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/iit-madras-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/iit-madras-context.jsonld
- group: other
  title: ''
  type: ProductPage
  url: https://www.iitm.ac.in/sso
created: '2026-06-03'
description: 'Indian Institute of Technology Madras (IIT Madras) is a public technical and research university in Chennai, India, ranked #227 in the QS World University Rankings 2025. It operates an institutional website (iitm.ac.in), a central library with electronic databases, a large online BS degree program in Data Science and Applications, and SSO/OAuth2-based identity endpoints. As of this review IIT Madras does not publish a public, documented developer portal or open API program. Its official GitHub organization exists but currently exposes no public repositories. The properties cataloged below reflect only publicly confirmed institutional web properties and identity endpoints, not documented third-party APIs.'
finops:
- name: Iit Madras Finops
  service_category: Education
  slug: iit-madras-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iit-madras.png
jsonld:
- class_count: 15
  name: Iit Madras Context
  property_count: 4
  slug: iit-madras-context
layout: provider
modified: '2026-07-25'
name: Indian Institute of Technology Madras
nav: Providers
network: true
overview: 'Indian Institute of Technology Madras is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and India.


  The Indian Institute of Technology Madras catalog on APIs.io includes 1 JSON-LD context.


  Indian Institute of Technology Madras'' developer surface includes GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Iit Madras Plans Pricing
  plan_count: 2
  slug: iit-madras-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Iit Madras Rate Limits
  slug: iit-madras-rate-limits
score:
  band: emerging
  composite: 16.3
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 16.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iit-madras/refs/heads/main/screenshots/iit-madras-2026-06-20T183233.png
security:
- kind: domain-security
  name: Iit Madras Domain Security
  slug: iit-madras-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iit-madras
tags:
- Education
- Higher Education
- University
- Research
- India
- IIT
website: https://www.iitm.ac.in/
---
