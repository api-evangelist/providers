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
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Tu Dresden Agentic Access
  operation_count: 18
  slug: tu-dresden-agentic-access
  summary_line: 18 operations · 1 acting
api_count: 9
apis:
- description: 'Gated JSON API providing automated access to public data from the TU Dresden lecture directory (Vorlesungsverzeichnis): courses, seminars, instructors, buildings, semesters, institutes and degree prog'
  name: TU Dresden Lecture Catalog API
  slug: lecture-catalog
- description: SAML 2.0 Shibboleth Identity Provider operated by the ZIH for authentication and authorization of TU Dresden services, and usable by external services for federated login (DFN-AAI). OIDC support is pl
  name: TU Dresden Shibboleth Single Sign-On (SAML IdP)
  slug: sso-shibboleth
- description: OAI-PMH 2.0 metadata harvesting interface for Qucosa, the document and publication server used by TU Dresden (tud.qucosa.de) for theses, dissertations and open-access publications. Supports standard O
  name: Qucosa OAI-PMH (TU Dresden Document Server)
  slug: qucosa-oai
- description: OpARA (Open Access Repository and Archive) is the research-data repository for researchers of TU Dresden and TU Bergakademie Freiberg, operated by the ZIH. It supports long-term archiving and open-acc
  name: OpARA Research Data Repository
  slug: opara
- description: Authority Provider Identifier Search
  name: TU Dresden authority_search API
  slug: tu-dresden-authority-search-api
- description: API endpoint to be use with the explorative search webapp
  name: TU Dresden explorative search API
  slug: tu-dresden-explorative-search-api
- description: Openrefine Reconcilation and Data Extension Operations
  name: TU Dresden reconcile API
  slug: tu-dresden-reconcile-api
- description: Search and Access Operations
  name: TU Dresden search and access API
  slug: tu-dresden-search-and-access-api
- description: Source data access operation
  name: TU Dresden source API
  slug: tu-dresden-source-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LOD authority_search API
  slug: open-tu-dresden-authority-search-api
- collection_type: open
  name: LOD authority_search explorative search API
  slug: open-tu-dresden-explorative-search-api
- collection_type: open
  name: LOD authority_search reconcile API
  slug: open-tu-dresden-reconcile-api
- collection_type: open
  name: LOD authority_search search and access API
  slug: open-tu-dresden-search-and-access-api
- collection_type: open
  name: LOD authority_search source API
  slug: open-tu-dresden-source-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tu-dresden-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tu-dresden-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tu-dresden-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tu-dresden.de/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tu-dresden
- group: company
  title: ''
  type: LinkedIn
  url: https://de.linkedin.com/school/tu-dresden/
- group: commercial
  title: ''
  type: Plans
  url: plans/tu-dresden-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tu-dresden-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tu-dresden-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Technische Universität Dresden (TU Dresden) is one of Germany''s leading research universities and a member of the German Universities Excellence Initiative, located in Dresden, Saxony. It ranks #234 in the QS World University Rankings 2025. Its public developer/API footprint is modest and largely tied to academic infrastructure: a gated lecture-catalog (course directory) JSON API, the Shibboleth SAML-based single sign-on identity provider operated by the Center for Information Services and High Performance Computing (ZIH), the OpARA research-data repository, and the Qucosa document server which exposes an OAI-PMH interface. The Saxony State and University Library (SLUB Dresden), which serves the university, additionally publishes a documented Linked Open Data API for bibliographic and authority data.'
examples:
- key_count: 2
  name: Tu Dresden Entity Example
  slug: tu-dresden-entity-example
- key_count: 2
  name: Tu Dresden Search Example
  slug: tu-dresden-search-example
finops:
- name: Tu Dresden Finops
  service_category: Education
  slug: tu-dresden-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tu-dresden.png
json_schemas:
- name: SLUB LOD Entity
  property_count: 8
  slug: tu-dresden-entity
json_structures:
- name: Tu Dresden Entity Structure
  property_count: 7
  slug: tu-dresden-entity-structure
jsonld:
- class_count: 15
  name: Tu Dresden Context
  property_count: 4
  slug: tu-dresden-context
layout: provider
modified: '2026-06-03'
name: TU Dresden
nav: Providers
network: true
overview: 'TU Dresden publishes 5 APIs on the [APIs.io](https://apis.io/) network, including authority_search API, explorative search API, reconcile API, and 2 more. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The TU Dresden catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TU Dresden''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Tu Dresden Plans Pricing
  plan_count: 2
  slug: tu-dresden-plans-pricing
random_paper: 125
rate_limits:
- limit_count: 1
  name: Tu Dresden Rate Limits
  slug: tu-dresden-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TU Dresden API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tu-dresden-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: TU Dresden API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 2
  slug: tu-dresden-rules
score:
  band: thin
  composite: 32.2
  delta: -5.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 55.2
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tu-dresden/refs/heads/main/screenshots/tu-dresden-2026-06-20T195822.png
security:
- kind: domain-security
  name: Tu Dresden Domain Security
  slug: tu-dresden-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tu Dresden Vulnerability Disclosure
  slug: tu-dresden-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tu-dresden
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Library
- Germany
website: https://tu-dresden.de/
---
