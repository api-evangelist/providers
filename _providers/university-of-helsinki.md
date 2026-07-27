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
api_count: 3
apis:
- description: Public REST API for Helda, the open institutional repository of the University of Helsinki, powered by DSpace 7.6.2. Provides programmatic access to research publications, dissertations, theses, and o
  name: Helda DSpace REST API
  slug: helda-rest
- description: OAI-PMH metadata-harvesting endpoint for Helda, enabling third parties to harvest Dublin Core and other metadata formats describing the university's open-access publications. Confirmed live, returning
  name: Helda OAI-PMH Metadata Interface
  slug: helda-oai
- description: The University of Helsinki runs the Funidata Sisu student information system for academic administration (study plans, course registration, curricula, organizations). Sisu exposes GraphQL and REST API
  name: Sisu (Kori) Student Information System API
  slug: sisu-kori
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-helsinki-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-helsinki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.helsinki.fi/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UniversityofHelsinki
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-helsinki/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-helsinki-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-helsinki-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-helsinki-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Helsinki is Finland''s oldest and largest multidisciplinary research university, founded in 1640, and is ranked #68 in the QS World University Rankings 2025. Its public developer and API footprint centers on open scholarly infrastructure: Helda, the university''s institutional repository, runs on DSpace 7 and exposes both a public REST API and an OAI-PMH metadata-harvesting interface. The university also maintains official GitHub organizations for its IT, computer science, student services, and language technology groups. Student-facing academic data flows through the Funidata Sisu student information system (Kori GraphQL/REST APIs), which is used institutionally but is not publicly documented or self-service.'
finops:
- name: University Of Helsinki Finops
  service_category: Education
  slug: university-of-helsinki-finops
graphqls:
- description: The University of Helsinki runs the Funidata Sisu student information system for academic administration (study plans, course registration, curricula, organizations). Sisu exposes GraphQL and REST API
  name: University of Helsinki GraphQL API
  slug: university-of-helsinki-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-helsinki.png
jsonld:
- class_count: 25
  name: University Of Helsinki Context
  property_count: 1
  slug: university-of-helsinki-context
layout: provider
modified: '2026-06-03'
name: University of Helsinki
nav: Providers
network: true
overview: 'University of Helsinki publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Finland, and Research.


  The University of Helsinki catalog on APIs.io includes 1 JSON-LD context.


  University of Helsinki''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: University Of Helsinki Plans Pricing
  plan_count: 2
  slug: university-of-helsinki-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: University Of Helsinki Rate Limits
  slug: university-of-helsinki-rate-limits
score:
  band: emerging
  composite: 24.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 0.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.0
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/screenshots/university-of-helsinki-2026-06-20T200155.png
security:
- kind: domain-security
  name: University Of Helsinki Domain Security
  slug: university-of-helsinki-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Helsinki Vulnerability Disclosure
  slug: university-of-helsinki-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-helsinki
tags:
- Education
- Higher Education
- University
- Finland
- Research
- Open Data
- Institutional Repository
- OAI-PMH
website: https://www.helsinki.fi/en
---
