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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Fudan University Dataverse is a research data repository built on the Dataverse open-source platform, hosting survey, census, and social-science datasets contributed by Fudan researchers. The Datavers
  name: Fudan University Dataverse (Research Data Repository)
  slug: dataverse
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fudan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fudan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fudan.edu.cn
- group: company
  title: ''
  type: Website
  url: https://www.fudan.edu.cn/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/FudanUniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/fudan-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/fudan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fudan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fudan-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Fudan University is a major public research university in Shanghai, China, ranked #84 in the QS World University Rankings 2025. It operates a Dataverse research data repository (Fudan University Dataverse, launched in 2014) hosting tens of thousands of files across social science, demography, and economics datasets, and maintains the China Open Data Index via its Digital and Mobile Governance Laboratory. As of this review, Fudan exposes no openly documented, publicly reachable developer API program: its Dataverse host (which by the Dataverse software design provides a native REST API and OAI-PMH) returns an access-forbidden page to requests originating outside mainland China, and the official GitHub organization carries no public repositories.'
finops:
- name: Fudan Finops
  service_category: Education
  slug: fudan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fudan.png
jsonld:
- class_count: 15
  name: Fudan Context
  property_count: 0
  slug: fudan-context
layout: provider
modified: '2026-06-03'
name: Fudan University
nav: Providers
network: true
overview: 'Fudan University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The Fudan University catalog on APIs.io includes 1 JSON-LD context.


  Fudan University''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Fudan Plans Pricing
  plan_count: 2
  slug: fudan-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 1
  name: Fudan Rate Limits
  slug: fudan-rate-limits
score:
  band: emerging
  composite: 20.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fudan/refs/heads/main/screenshots/fudan-2026-06-20T181623.png
security:
- kind: domain-security
  name: Fudan Domain Security
  slug: fudan-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Fudan Vulnerability Disclosure
  slug: fudan-vulnerability-disclosure
  summary_line: disclosure policy published
slug: fudan
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- China
- Shanghai
website: https://www.fudan.edu.cn
---
