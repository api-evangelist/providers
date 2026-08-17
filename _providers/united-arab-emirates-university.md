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
api_count: 2
apis:
- description: OAI-PMH 2.0 metadata harvesting endpoint for Scholarworks@UAEU, the university's open-access institutional repository built on the bepress Digital Commons platform. The endpoint supports standard OAI-
  name: Scholarworks@UAEU OAI-PMH Repository API
  slug: scholarworks-oai-pmh
- description: 'UAEU publishes open datasets (e.g. UAEU granted patents and digital transaction reports) as an organization on the UAE national open data portal operated by the Federal Competitiveness and Statistics '
  name: UAEU Open Data on UAE National Portal (CKAN)
  slug: fcsc-open-data
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-arab-emirates-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uaeu.ac.ae/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uitsws
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/united-arab-emirates-university/
- group: build
  title: ''
  type: Library
  url: https://www.uaeu.ac.ae/en/library/
- group: other
  title: ''
  type: Research
  url: https://research.uaeu.ac.ae/
- group: commercial
  title: ''
  type: Plans
  url: plans/united-arab-emirates-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/united-arab-emirates-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/united-arab-emirates-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'United Arab Emirates University (UAEU) is a public research university in Al Ain, United Arab Emirates, ranked #262 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is limited and oriented toward research and open data rather than a formal developer program: the UAEU Library operates Scholarworks@UAEU, a bepress Digital Commons institutional repository that exposes a standards-based OAI-PMH 2.0 metadata harvesting endpoint, and UAEU publishes open datasets through the UAE national open data portal (FCSC), which is built on CKAN and offers a CKAN Action API. UAEU''s Division of Information Technology maintains a GitHub organization (uitsws / UAEU-DOIT), but it currently has no public repositories. No general-purpose, self-service public developer portal or documented student-information / catalog API was found.'
finops:
- name: United Arab Emirates University Finops
  service_category: Education
  slug: united-arab-emirates-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-arab-emirates-university.png
jsonld:
- class_count: 13
  name: United Arab Emirates University Context
  property_count: 6
  slug: united-arab-emirates-university-context
layout: provider
modified: '2026-06-03'
name: United Arab Emirates University
nav: Providers
network: true
overview: 'United Arab Emirates University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The United Arab Emirates University catalog on APIs.io includes 1 JSON-LD context.


  United Arab Emirates University''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: United Arab Emirates University Plans Pricing
  plan_count: 2
  slug: united-arab-emirates-university-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 1
  name: United Arab Emirates University Rate Limits
  slug: united-arab-emirates-university-rate-limits
score:
  band: emerging
  composite: 19.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/united-arab-emirates-university/refs/heads/main/screenshots/united-arab-emirates-university-2026-06-20T200041.png
security:
- kind: domain-security
  name: United Arab Emirates University Domain Security
  slug: united-arab-emirates-university-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: united-arab-emirates-university
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Institutional Repository
- OAI-PMH
- CKAN
- United Arab Emirates
- Middle East
website: https://www.uaeu.ac.ae/en/
---
