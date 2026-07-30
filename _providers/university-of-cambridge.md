---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Cambridge Agentic Access
  operation_count: 39
  slug: university-of-cambridge-agentic-access
  summary_line: 39 operations
api_count: 7
apis:
- description: The University's central web authentication service. Raven OAuth2 conforms to OpenID Connect; applications register client credentials to authenticate Cambridge users. An identity/SSO interface rather
  name: Raven Authentication (OAuth2 / OpenID Connect)
  slug: raven
- description: UIS API Gateway (ALPHA) publishing read-oriented REST APIs — University Card, University Student (CamSIS-sourced), and University Human Resources (CHRIS-sourced). Interactive "try this API" docs on th
  name: Cambridge API Gateway (Card / Student / HR)
  slug: gateway
- description: Cambridge's open-access research repository (Apollo) on the DSpace platform, exposing OAI-PMH metadata harvesting and a DSpace REST API. Managed by Cambridge University Library Open Research Systems.
  name: Apollo Institutional Repository API (DSpace)
  slug: apollo
- description: 'Methods for querying and manipulating groups. #### The fetch parameter for groups All methods that return groups also accept an optional `fetch` parameter that may be used to request additional inform'
  name: University of Cambridge group API
  slug: university-of-cambridge-group-api
- description: Common methods for searching for objects in the Lookup/Ibis database.
  name: University of Cambridge ibis API
  slug: university-of-cambridge-ibis-api
- description: 'Methods for querying and manipulating institutions. #### The fetch parameter for institutions All methods that return institutions also accept an optional `fetch` parameter that may be used to request'
  name: University of Cambridge institution API
  slug: university-of-cambridge-institution-api
- description: 'Methods for querying and manipulating people. #### Notes on the fetch parameter All methods that return people, institutions or groups also accept an optional `fetch` parameter that may be used to req'
  name: University of Cambridge person API
  slug: university-of-cambridge-person-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-cambridge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-cambridge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-cambridge-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cam.ac.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.api.apps.cam.ac.uk/
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.developers.cam.ac.uk/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Cambridge_Uni
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-cambridge/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-cambridge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-cambridge-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-cambridge-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cam.ac.uk/rss/
created: '2026-06-03'
description: 'The University of Cambridge (founded 1209; QS World 2025 #5) is a public collegiate research university with a real, documented developer footprint operated mainly by University Information Services (UIS): a central API Gateway / developer portal (developer.api.apps.cam.ac.uk) fronting identity-oriented REST APIs, the long-standing Lookup/Ibis directory web service, the Raven central authentication service (OAuth2 / OpenID Connect), and the Apollo institutional repository (DSpace REST + OAI-PMH). UIS open-source code is published on a self-hosted GitLab.'
examples:
- key_count: 1
  name: University Of Cambridge Group Example
  slug: university-of-cambridge-group-example
- key_count: 1
  name: University Of Cambridge Institution Example
  slug: university-of-cambridge-institution-example
- key_count: 1
  name: University Of Cambridge Person Example
  slug: university-of-cambridge-person-example
finops:
- name: University Of Cambridge Finops
  service_category: Education
  slug: university-of-cambridge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-cambridge.png
json_schemas:
- name: Group
  property_count: 7
  slug: university-of-cambridge-group
- name: Institution
  property_count: 6
  slug: university-of-cambridge-institution
- name: Person
  property_count: 9
  slug: university-of-cambridge-person
json_structures:
- name: University Of Cambridge Group Structure
  property_count: 6
  slug: university-of-cambridge-group-structure
- name: University Of Cambridge Institution Structure
  property_count: 4
  slug: university-of-cambridge-institution-structure
- name: University Of Cambridge Person Structure
  property_count: 8
  slug: university-of-cambridge-person-structure
jsonld:
- class_count: 22
  name: University Of Cambridge Context
  property_count: 2
  slug: university-of-cambridge-context
layout: provider
modified: '2026-06-03'
name: University of Cambridge
nav: Providers
network: true
overview: 'University of Cambridge publishes 4 APIs on the [APIs.io](https://apis.io/) network, including group API, ibis API, institution API, and 1 more. Tagged areas include Education, Higher Education, University, Research, and United Kingdom.


  The University of Cambridge catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Cambridge''s developer surface includes authentication, engineering blog, and 11 more developer resources.'
plans:
- name: University Of Cambridge Plans Pricing
  plan_count: 2
  slug: university-of-cambridge-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 1
  name: University Of Cambridge Rate Limits
  slug: university-of-cambridge-rate-limits
rules:
- name: University of Cambridge API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-cambridge-jsonschema-spectral-rules
- name: University of Cambridge API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: university-of-cambridge-rules
score:
  band: developing
  composite: 42.1
  delta: -3.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 63.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-cambridge/refs/heads/main/screenshots/university-of-cambridge-2026-06-20T200140.png
security:
- kind: authentication
  name: University Of Cambridge Authentication
  slug: university-of-cambridge-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: University Of Cambridge Domain Security
  slug: university-of-cambridge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-cambridge
tags:
- Education
- Higher Education
- University
- Research
- United Kingdom
- Identity
- API Gateway
- Developer Portal
website: https://www.cam.ac.uk/
---
