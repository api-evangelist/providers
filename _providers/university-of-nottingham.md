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
- description: Publicly accessible OAI-PMH (Open Archives Initiative Protocol for Metadata Harvesting) interface for Repository@Nottingham, the university's institutional research repository powered by Worktribe. Su
  name: Repository@Nottingham OAI-PMH
  slug: repository-oai
- description: Legacy EPrints repositories (Nottingham ePrints, Nottingham eTheses, Nottingham eDissertations) historically exposed OAI-PMH endpoints at /perl/oai2. As of verification these endpoints are protected b
  name: Nottingham ePrints / eTheses OAI-PMH (gated)
  slug: eprints-oai
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-nottingham-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nottingham.ac.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.nottingham.ac.uk/dts/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UniversityOfNottingham
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Health-Informatics-UoN
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-nottingham/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/UniofNottingham
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-nottingham-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-nottingham-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-nottingham-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Nottingham is a public research university in Nottingham, United Kingdom, ranked #71 in the QS World University Rankings 2025. As a research-intensive institution it operates Repository@Nottingham (powered by Worktribe) which exposes a publicly accessible OAI-PMH metadata-harvesting interface for its research outputs, alongside legacy EPrints repositories (Nottingham ePrints, eTheses). Most institutional systems (student records, timetabling, library discovery, identity) are gated behind SSO and are not publicly documented developer APIs. The university maintains several official GitHub organizations publishing open-source code.'
finops:
- name: University Of Nottingham Finops
  service_category: Education
  slug: university-of-nottingham-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-nottingham.png
jsonld:
- class_count: 8
  name: University Of Nottingham Context
  property_count: 4
  slug: university-of-nottingham-context
layout: provider
modified: '2026-06-03'
name: University of Nottingham
nav: Providers
network: true
overview: 'University of Nottingham publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The University of Nottingham catalog on APIs.io includes 1 JSON-LD context.


  University of Nottingham''s developer surface includes GitHub presence and 10 more developer resources.'
plans:
- name: University Of Nottingham Plans Pricing
  plan_count: 2
  slug: university-of-nottingham-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: University Of Nottingham Rate Limits
  slug: university-of-nottingham-rate-limits
score:
  band: emerging
  composite: 18.8
  delta: -1.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-nottingham/refs/heads/main/screenshots/university-of-nottingham-2026-06-20T200211.png
security:
- kind: domain-security
  name: University Of Nottingham Domain Security
  slug: university-of-nottingham-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: university-of-nottingham
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- OAI-PMH
- United Kingdom
website: https://www.nottingham.ac.uk/
---
