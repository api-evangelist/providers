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
api_count: 3
apis:
- description: BORIS Portal is the institutional repository and research information system of the University of Bern, running DSpace 7.6.1 with the DSpace-CRIS extension. Its REST API (HAL/JSON) exposes communities
  name: BORIS Portal DSpace REST API
  slug: boris-rest
- description: OAI-PMH 2.0 harvesting endpoint for BORIS Portal, allowing metadata harvesting of the University of Bern's research outputs. Confirmed live (verb=Identify returns repository name "BORIS Portal", proto
  name: BORIS Portal OAI-PMH Endpoint
  slug: boris-oai
- description: The University of Bern Library publishes curated guidance on Application Programming Interfaces for text and data mining, covering freely accessible and licensed third-party data services (OpenAlex, C
  name: University Library Data-Mining APIs Guide
  slug: library-tdm-apis
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-bern-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-bern-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unibe.ch/index_eng.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/id-unibe-ch
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ub-unibe-ch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-bern/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-bern-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-bern-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-bern-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Bern (Universität Bern), founded in 1834, is a comprehensive public research university in the Swiss capital with around 16,000 students across eight faculties, ranked #91 in the QS World University Rankings 2025. Its public, machine-readable footprint centers on BORIS Portal, the institutional repository and research information system, which runs DSpace 7.6.1 and exposes both a REST API and an OAI-PMH endpoint. The University Library also publishes guidance on data-mining APIs and maintains open-source tools on GitHub. There is no single unified, self-service developer portal; administrative, course, and identity systems are gated behind institutional affiliation and Swiss federated identity (SWITCH edu-ID / Shibboleth).'
finops:
- name: University Of Bern Finops
  service_category: Education
  slug: university-of-bern-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-bern.png
jsonld:
- class_count: 13
  name: University Of Bern Context
  property_count: 5
  slug: university-of-bern-context
layout: provider
modified: '2026-06-03'
name: University of Bern
nav: Providers
network: true
overview: 'University of Bern publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Switzerland, and Research.


  The University of Bern catalog on APIs.io includes 1 JSON-LD context.


  University of Bern''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: University Of Bern Plans Pricing
  plan_count: 2
  slug: university-of-bern-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: University Of Bern Rate Limits
  slug: university-of-bern-rate-limits
score:
  band: emerging
  composite: 20.8
  delta: 1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-bern/refs/heads/main/screenshots/university-of-bern-2026-06-20T200135.png
security:
- kind: domain-security
  name: University Of Bern Domain Security
  slug: university-of-bern-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: University Of Bern Vulnerability Disclosure
  slug: university-of-bern-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-bern
tags:
- Education
- Higher Education
- University
- Switzerland
- Research
- Open Access
- Institutional Repository
- Library
website: https://www.unibe.ch/index_eng.html
---
