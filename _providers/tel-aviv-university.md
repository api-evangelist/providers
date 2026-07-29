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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: 'Tel Aviv University Libraries run ExLibris Primo for catalog/discovery (branded "DaTA Search"), institution code 972TAU_INST:TAU. The hosted Primo platform exposes the standard Primo Search REST API. '
  name: TAU Libraries Primo Discovery (DaTA Search)
  slug: primo-discovery
- description: The TAU Libraries Primo discovery layer is backed by the ExLibris Alma library services platform. Alma deployments expose the standard OAI-PMH metadata harvesting protocol and the Alma REST APIs. Endp
  name: TAU Libraries Alma / OAI-PMH Metadata Harvesting
  slug: alma-oai-pmh
- description: A community/student project (Arazim Project) that programmatically wraps several TAU web systems — including the Moodle LMS, the information-management (IMS) grade system, and course/study-plan data —
  name: Unofficial tau-tools (Moodle / IMS / course data)
  slug: unofficial-tau-tools
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tel-aviv-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://english.tau.ac.il/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/arazimproject
- group: company
  title: ''
  type: LinkedIn
  url: https://il.linkedin.com/school/tel-aviv-university/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/telavivuni
- group: commercial
  title: ''
  type: Plans
  url: plans/tel-aviv-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tel-aviv-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tel-aviv-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Tel Aviv University (TAU) is Israel''s largest public research university, located in Tel Aviv, and is ranked #209 in the QS World University Rankings 2025. TAU does not publish a centralized, public developer portal or open-data API program. Its confirmed machine-accessible surface is limited to standard third-party platform endpoints: an ExLibris Primo discovery interface (institution code 972TAU_INST:TAU) backed by an Alma library services platform that exposes the usual Primo Search REST API and Alma OAI-PMH harvesting endpoints. Student-built, unofficial tooling also scrapes/wraps TAU''s Moodle and information-management (IMS) systems. No officially documented, self-service public API was found.'
finops:
- name: Tel Aviv University Finops
  service_category: Education
  slug: tel-aviv-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tel-aviv-university.png
jsonld:
- class_count: 5
  name: Tel Aviv University Context
  property_count: 6
  slug: tel-aviv-university-context
layout: provider
modified: '2026-07-25'
name: Tel Aviv University
nav: Providers
network: true
overview: 'Tel Aviv University publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Israel, and Library.


  The Tel Aviv University catalog on APIs.io includes 1 JSON-LD context.


  Tel Aviv University''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Tel Aviv University Plans Pricing
  plan_count: 2
  slug: tel-aviv-university-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 1
  name: Tel Aviv University Rate Limits
  slug: tel-aviv-university-rate-limits
score:
  band: emerging
  composite: 18.9
  delta: -2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tel-aviv-university/refs/heads/main/screenshots/tel-aviv-university-2026-06-20T195022.png
security:
- kind: domain-security
  name: Tel Aviv University Domain Security
  slug: tel-aviv-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tel-aviv-university
tags:
- Education
- Higher Education
- University
- Israel
- Library
- Discovery
- Research
website: https://english.tau.ac.il/
---
