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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: 'Open JSON API from the CTSI-operated UCSF Profiles research-networking platform, providing data on 8,000+ UCSF researchers, faculty, and postdocs: name, school, department, title, ORCID, education, re'
  name: UCSF Profiles JSON API
  slug: profiles-json
- description: UCSF's institutional API catalog and developer portal, operated by ITS Integration Services on the MuleSoft Anypoint Platform. It documents APIs such as SIS Course Enrollment, Building Metadata (Archi
  name: Developer@UCSF API Portal (internal)
  slug: developer-portal
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucsf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucsf.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UCSF
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ucsf/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ucsf.edu/
- group: commercial
  title: ''
  type: Plans
  url: plans/ucsf-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucsf-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucsf-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ucsf-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-03'
description: 'The University of California, San Francisco (UCSF) is a public health-sciences university and the only UC campus dedicated exclusively to graduate and health professions education, biomedical research, and patient care. It is ranked #39 in the QS World University Rankings 2025. UCSF maintains a public developer presence centered on the CTSI-operated UCSF Profiles research-networking platform, which exposes an open JSON API covering 8,000+ researchers, faculty, and postdocs. UCSF also runs an internal developer portal (developer.ucsf.edu) and a MuleSoft Anypoint API platform managed by ITS Integration Services that catalogs SIS course enrollment, building metadata, ServiceNow, and CV APIs, but those are gated behind MyAccess SSO and the campus network and are not publicly consumable.'
finops:
- name: Ucsf Finops
  service_category: Education
  slug: ucsf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucsf.png
jsonld:
- class_count: 42
  name: Ucsf Context
  property_count: 3
  slug: ucsf-context
layout: provider
modified: '2026-06-03'
name: University of California, San Francisco
nav: Providers
network: true
overview: 'University of California, San Francisco publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Health Sciences, and Research.


  The University of California, San Francisco catalog on APIs.io includes 1 JSON-LD context.


  University of California, San Francisco''s developer surface includes GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Ucsf Plans Pricing
  plan_count: 2
  slug: ucsf-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 1
  name: Ucsf Rate Limits
  slug: ucsf-rate-limits
score:
  band: emerging
  composite: 23.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 10.9
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.3
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Ucsf Domain Security
  slug: ucsf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ucsf
tags:
- Education
- Higher Education
- University
- Health Sciences
- Research
- Researcher Profiles
- Open Data
- United States
website: https://www.ucsf.edu/
---
