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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: OAI-PMH metadata-harvesting interface for the DSpace-based institutional repository of electronic dissertations and habilitations of Universität Hamburg, operated by the Staats- und Universitätsbiblio
  name: E-Dissertationen (ediss.sub.hamburg) OAI-PMH
  slug: ediss-oai
- description: Open Access discovery portal aggregating freely available publications, research data, teaching materials, and scientific collections of Universität Hamburg. Underlying IT services (repositories and m
  name: Open-Access-Portal Universität Hamburg
  slug: open-access-portal
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/universitat-hamburg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uni-hamburg.de/en.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Uni-Hamburg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universitaet-hamburg/
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.rrz.uni-hamburg.de/
- group: auth
  title: ''
  type: Authentication
  url: https://www.rrz.uni-hamburg.de/services/weitere/authentifizierung/shibboleth/configure.html
- group: commercial
  title: ''
  type: Plans
  url: plans/universitat-hamburg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/universitat-hamburg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/universitat-hamburg-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universität Hamburg is a public research university in Hamburg, Germany, ranked #191 in the QS World University Rankings 2025. Its public developer and machine-readable footprint is concentrated in library and open-access infrastructure operated by the Staats- und Universitätsbibliothek (SUB) and the Regionales Rechenzentrum (RRZ), rather than a single branded developer portal. Confirmed public interfaces include a DSpace-based institutional dissertation repository (ediss.sub.hamburg) exposing an OAI-PMH metadata endpoint, and an official Universität Hamburg open-source presence on GitHub. Campus systems such as the STiNE campus-management platform and Shibboleth/SAML single sign-on are gated and not openly documented as public APIs.'
finops:
- name: Universitat Hamburg Finops
  service_category: Education
  slug: universitat-hamburg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/universitat-hamburg.png
jsonld:
- class_count: 8
  name: Universitat Hamburg Context
  property_count: 2
  slug: universitat-hamburg-context
layout: provider
modified: '2026-06-03'
name: Universität Hamburg
nav: Providers
network: true
overview: 'Universität Hamburg publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Germany, and Open Access.


  The Universität Hamburg catalog on APIs.io includes 1 JSON-LD context.


  Universität Hamburg''s developer surface includes GitHub presence, authentication, and 8 more developer resources.'
plans:
- name: Universitat Hamburg Plans Pricing
  plan_count: 2
  slug: universitat-hamburg-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 1
  name: Universitat Hamburg Rate Limits
  slug: universitat-hamburg-rate-limits
score:
  band: emerging
  composite: 23.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 10.9
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/universitat-hamburg/refs/heads/main/screenshots/universitat-hamburg-2026-06-20T200115.png
security:
- kind: domain-security
  name: Universitat Hamburg Domain Security
  slug: universitat-hamburg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: universitat-hamburg
tags:
- Education
- Higher Education
- University
- Germany
- Open Access
- Library
- Metadata
- OAI-PMH
website: https://www.uni-hamburg.de/en.html
---
