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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The Aberdeen University Research Archive (AURA) runs DSpace 8.1 and exposes a public HATEOAS REST API for discovering communities, collections, items, bitstreams, and related metadata in the open-acce
  name: AURA DSpace REST API
  slug: aura-dspace-rest
- description: AURA provides an OAI-PMH 2.0 endpoint (repository name "Aura") for harvesting Dublin Core and other metadata formats describing the University of Aberdeen's open-access research outputs. Standard verb
  name: AURA OAI-PMH Metadata Harvesting
  slug: aura-oai-pmh
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-aberdeen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-aberdeen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.abdn.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uofa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-aberdeen/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-aberdeen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-aberdeen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-aberdeen-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Aberdeen is a public research university in Aberdeen, Scotland, United Kingdom, founded in 1495 and ranked #236 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is centred on the Aberdeen University Research Archive (AURA), an open-access institutional repository running DSpace 8 that exposes both a DSpace REST API and an OAI-PMH 2.0 metadata-harvesting endpoint. The university also operates an Elsevier Pure research portal and maintains a verified GitHub organization. No general-purpose public developer portal with course, timetable, or student-information-system APIs was found; integration-style APIs appear to be internal/gated.'
finops:
- name: University Of Aberdeen Finops
  service_category: Education
  slug: university-of-aberdeen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-aberdeen.png
jsonld:
- class_count: 22
  name: University Of Aberdeen Context
  property_count: 3
  slug: university-of-aberdeen-context
layout: provider
modified: '2026-06-03'
name: University of Aberdeen
nav: Providers
network: true
overview: 'University of Aberdeen publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The University of Aberdeen catalog on APIs.io includes 1 JSON-LD context.


  University of Aberdeen''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: University Of Aberdeen Plans Pricing
  plan_count: 2
  slug: university-of-aberdeen-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: University Of Aberdeen Rate Limits
  slug: university-of-aberdeen-rate-limits
score:
  band: emerging
  composite: 19.5
  delta: 0.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-aberdeen/refs/heads/main/screenshots/university-of-aberdeen-2026-06-20T200131.png
security:
- kind: domain-security
  name: University Of Aberdeen Domain Security
  slug: university-of-aberdeen-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Aberdeen Vulnerability Disclosure
  slug: university-of-aberdeen-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: university-of-aberdeen
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Institutional Repository
- DSpace
- OAI-PMH
- United Kingdom
- Scotland
website: https://www.abdn.ac.uk/
---
