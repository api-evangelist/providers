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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The Universiti Teknologi Malaysia Institutional Repository (UTM-IR) is built on EPrints and exposes an OAI-PMH 2.0 metadata harvesting endpoint at /cgi/oai2, as registered with ROAR, OpenDOAR, and She
  name: UTM Institutional Repository (UTM-IR) OAI-PMH
  slug: eprints-oai
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/utm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.utm.my/
- group: build
  title: ''
  type: Library
  url: https://library.utm.my/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://digital.utm.my/
- group: auth
  title: ''
  type: Authentication
  url: https://my.utm.my/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universiti-teknologi-malaysia/
- group: commercial
  title: ''
  type: Plans
  url: plans/utm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/utm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/utm-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universiti Teknologi Malaysia (UTM) is a public research university in Johor Bahru and Kuala Lumpur, Malaysia, ranked #181 in the QS World University Rankings 2025. UTM operates a broad set of institutional web properties including its main portal (utm.my), the UTM Library, UTMDigital services, the myUTM single sign-on portal, and the UTM Institutional Repository (UTM-IR) running EPrints. UTM does not publish a dedicated public developer portal or documented REST APIs; the most machine-consumable public interface is the EPrints OAI-PMH metadata feed for its institutional repository.'
finops:
- name: Utm Finops
  service_category: Education
  slug: utm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/utm.png
jsonld:
- class_count: 10
  name: Utm Context
  property_count: 1
  slug: utm-context
layout: provider
modified: '2026-06-03'
name: Universiti Teknologi Malaysia
nav: Providers
network: true
overview: 'Universiti Teknologi Malaysia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Universiti Teknologi Malaysia catalog on APIs.io includes 1 JSON-LD context.


  Universiti Teknologi Malaysia''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Utm Plans Pricing
  plan_count: 2
  slug: utm-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Utm Rate Limits
  slug: utm-rate-limits
score:
  band: emerging
  composite: 23.1
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/utm/refs/heads/main/screenshots/utm-2026-06-20T200738.png
security:
- kind: domain-security
  name: Utm Domain Security
  slug: utm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: utm
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Institutional Repository
- OAI-PMH
- Malaysia
website: https://www.utm.my/
---
