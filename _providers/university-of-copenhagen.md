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
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: The University of Copenhagen Research Portal (researchprofiles.ku.dk) is built on the Elsevier Pure research information system, locally branded CURIS. Pure platforms conventionally expose research me
  name: University of Copenhagen Research Portal (CURIS / Pure)
  slug: research-portal
- description: 'The ku-kom GitHub organization publishes the open-source TYPO3 CMS extensions and Bootstrap-based styleguide that power the ku.dk web platform. These are reusable source-code components rather than a '
  name: University of Copenhagen Web Platform (ku-kom GitHub)
  slug: ku-kom-github
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-copenhagen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ku.dk/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ku-kom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-copenhagen/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-copenhagen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-copenhagen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-copenhagen-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Copenhagen (Københavns Universitet, UCPH), founded in 1479, is Denmark''s oldest and largest university and one of the leading research institutions in the Nordic region, ranked #53 in the QS World University Rankings 2025. It has no centralized public developer portal or documented open-data API program. Its public technical footprint consists of the ku-kom GitHub organization (TYPO3 CMS extensions and front-end styleguide used to build the ku.dk web platform) and the CURIS research information system on researchprofiles.ku.dk, an Elsevier Pure platform that conventionally supports OAI-PMH metadata harvesting and the Pure web service though these endpoints could not be confirmed reachable from the public internet at review time.'
finops:
- name: University Of Copenhagen Finops
  service_category: Education
  slug: university-of-copenhagen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-copenhagen.png
jsonld:
- class_count: 9
  name: University Of Copenhagen Context
  property_count: 6
  slug: university-of-copenhagen-context
layout: provider
modified: '2026-06-03'
name: University of Copenhagen
nav: Providers
network: true
overview: 'University of Copenhagen publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Denmark.


  The University of Copenhagen catalog on APIs.io includes 1 JSON-LD context.


  University of Copenhagen''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: University Of Copenhagen Plans Pricing
  plan_count: 2
  slug: university-of-copenhagen-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 1
  name: University Of Copenhagen Rate Limits
  slug: university-of-copenhagen-rate-limits
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
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-copenhagen/refs/heads/main/screenshots/university-of-copenhagen-2026-06-20T200145.png
security:
- kind: domain-security
  name: University Of Copenhagen Domain Security
  slug: university-of-copenhagen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-copenhagen
tags:
- Education
- Higher Education
- University
- Research
- Denmark
- Nordic
- Open Source
website: https://www.ku.dk/en
---
