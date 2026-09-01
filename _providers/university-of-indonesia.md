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
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH 2.0) interface for UI Scholars Hub, the University of Indonesia institutional research repository running on the Digital Commons (bep
  name: UI Scholars Hub OAI-PMH
  slug: scholarhub-oai
- description: Sistem Akun UI, the university-wide Single Sign-On service, implemented using the CAS (Central Authentication Service) protocol at sso.ui.ac.id. It authenticates UI civitas academica across integrated
  name: SSO UI (CAS Authentication)
  slug: sso-cas
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-indonesia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ui.ac.id/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-indonesia/
- group: auth
  title: ''
  type: Authentication
  url: https://sso.ui.ac.id/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-indonesia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-indonesia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-indonesia-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/university-of-indonesia-context.jsonld
- group: company
  title: ''
  type: x-blog
  url: blogs/blogs.json
created: '2026-06-03'
description: 'University of Indonesia (Universitas Indonesia, UI) is a public research university based in Depok and Salemba, Jakarta, ranked #206 in the QS World University Rankings 2025 and the highest-ranked university in Indonesia. Its public, machine-readable developer footprint is limited: UI Scholars Hub, the institutional research repository hosted on the Digital Commons (bepress) platform, exposes a live OAI-PMH 2.0 metadata interface for harvesting scholarly works, and the campus-wide Single Sign-On runs on CAS (Central Authentication Service). No public, self-service developer portal with documented REST endpoints or API keys was found; academic, library, and identity systems are gated behind institutional credentials.'
finops:
- name: University Of Indonesia Finops
  service_category: Education
  slug: university-of-indonesia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-indonesia.png
jsonld:
- class_count: 25
  name: University Of Indonesia Context
  property_count: 4
  slug: university-of-indonesia-context
layout: provider
modified: '2026-06-03'
name: University of Indonesia
nav: Providers
network: true
overview: 'University of Indonesia publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Indonesia, and Research.


  The University of Indonesia catalog on APIs.io includes 1 JSON-LD context.


  University of Indonesia''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: University Of Indonesia Plans Pricing
  plan_count: 2
  slug: university-of-indonesia-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: University Of Indonesia Rate Limits
  slug: university-of-indonesia-rate-limits
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: University Of Indonesia Domain Security
  slug: university-of-indonesia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-indonesia
tags:
- Education
- Higher Education
- University
- Indonesia
- Research
- Repository
- OAI-PMH
- Authentication
website: https://www.ui.ac.id/
---
