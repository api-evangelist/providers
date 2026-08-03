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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 88
  human_in_the_loop: 1
  name: University Of Basel Agentic Access
  operation_count: 169
  slug: university-of-basel-agentic-access
  summary_line: 169 operations · 88 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Public DSpace REST API for "edoc", the open-access institutional repository of the University of Basel, running DSpace-CRIS 7.6.2. The API root reports the repository name and server endpoints and exp
  name: edoc DSpace REST API
  slug: edoc-rest
- description: 'OAI-PMH 2.0 metadata harvesting interface for the University of Basel edoc repository. The Identify verb reports repositoryName "edoc: Open Access Repository University of Basel" and adminEmail openac'
  name: edoc OAI-PMH
  slug: edoc-oai
- description: The DaSCH Service Platform API (DSP-API, formerly Knora), an open-source HTTP API for long-term preservation, querying, annotation and linking of humanities research data as RDF graphs, with the Gravs
  name: DaSCH DSP-API
  slug: dsp-api
- description: Standards-based SRU (Search/Retrieve via URL) interface to the SLSP swisscovery / Alma discovery system for the University of Basel institution zone (41SLSP_UBS). Allows programmatic search and retrie
  name: swisscovery (SLSP Alma) SRU
  slug: swisscovery-sru
- description: The Admin API API from University of Basel — 66 operation(s) for admin api.
  name: University of Basel Admin API API
  slug: university-of-basel-admin-api-api
- description: The API v2 API from University of Basel — 56 operation(s) for api v2.
  name: University of Basel API v2 API
  slug: university-of-basel-api-v2-api
- description: The API v3 API from University of Basel — 10 operation(s) for api v3.
  name: University of Basel API v3 API
  slug: university-of-basel-api-v3-api
- description: The Management API API from University of Basel — 3 operation(s) for management api.
  name: University of Basel Management API API
  slug: university-of-basel-management-api-api
- description: The Ontology Mappings API from University of Basel — 2 operation(s) for ontology mappings.
  name: University of Basel Ontology Mappings API
  slug: university-of-basel-ontology-mappings-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-basel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-basel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-basel-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.unibas.ch/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dasch.swiss/latest/DSP-API/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ITS-Unibas
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/dasch-swiss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-basel/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-basel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-basel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-basel-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
description: 'The University of Basel (Universität Basel) is the oldest university in Switzerland, founded in 1460, and is ranked #85 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is concentrated in scholarly and research infrastructure rather than a single central developer portal. The university operates "edoc", its open-access institutional repository running DSpace-CRIS 7.6.2, which exposes a public DSpace REST API and an OAI-PMH 2.0 metadata interface. The Swiss National Data and Service Center for the Humanities (DaSCH), hosted at the University of Basel, develops and operates the DSP-API, an open-source RDF-based humanities research data API. Library discovery is delivered through the SLSP swisscovery (Alma/Primo) platform, which offers a standards-based SRU search interface for the Basel institution zone. Source code is published across multiple verified GitHub organizations including IT Services (ITS-Unibas) and DaSCH (dasch-swiss).'
examples:
- key_count: 2
  name: University Of Basel Gethealth Example
  slug: university-of-basel-getHealth-example
- key_count: 2
  name: University Of Basel Getprojectbyshortcode Example
  slug: university-of-basel-getProjectByShortcode-example
- key_count: 2
  name: University Of Basel Getprojects Example
  slug: university-of-basel-getProjects-example
- key_count: 2
  name: University Of Basel Getversion Example
  slug: university-of-basel-getVersion-example
finops:
- name: University Of Basel Finops
  service_category: Education
  slug: university-of-basel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-basel.png
json_schemas:
- name: Group
  property_count: 6
  slug: university-of-basel-group
- name: Project
  property_count: 12
  slug: university-of-basel-project
- name: UserDto
  property_count: 10
  slug: university-of-basel-user
json_structures:
- name: University Of Basel Group Structure
  property_count: 6
  slug: university-of-basel-group-structure
- name: University Of Basel Project Structure
  property_count: 12
  slug: university-of-basel-project-structure
jsonld:
- class_count: 20
  name: University Of Basel Context
  property_count: 8
  slug: university-of-basel-context
layout: provider
name: University of Basel
nav: Providers
network: true
overview: 'University of Basel publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Admin API API, API v2 API, API v3 API, and 2 more. Tagged areas include Education, Higher Education, University, Switzerland, and Research Data.


  The University of Basel catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Basel''s developer surface includes authentication, GitHub presence, and 10 more developer resources.'
plans:
- name: University Of Basel Plans Pricing
  plan_count: 2
  slug: university-of-basel-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 1
  name: University Of Basel Rate Limits
  slug: university-of-basel-rate-limits
rules:
- name: University of Basel API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: university-of-basel-jsonschema-spectral-rules
- name: University of Basel API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 3
  slug: university-of-basel-rules
score:
  band: developing
  composite: 43.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-basel/refs/heads/main/screenshots/university-of-basel-2026-06-20T200131.png
security:
- kind: authentication
  name: University Of Basel Authentication
  slug: university-of-basel-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: University Of Basel Domain Security
  slug: university-of-basel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-basel
tags:
- Education
- Higher Education
- University
- Switzerland
- Research Data
- Open Access
- Institutional Repository
- Library
- Digital Humanities
website: https://www.unibas.ch/en
---
