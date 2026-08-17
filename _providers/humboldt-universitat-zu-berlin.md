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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Humboldt Universitat Zu Berlin Agentic Access
  operation_count: 8
  slug: humboldt-universitat-zu-berlin-agentic-access
  summary_line: 8 operations
api_count: 6
apis:
- description: 'Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH 2.0) endpoint for the edoc institutional repository, allowing public harvesting of metadata for theses, dissertations, articles, and '
  name: edoc-Server OAI-PMH Interface
  slug: edoc-oai
- description: The University Library's central search portal, Primus, is built on the Ex Libris Primo discovery service backed by Alma. Primo/Alma provide open REST APIs for discovery and resource management; API a
  name: University Library Primus Discovery (Ex Libris Primo/Alma)
  slug: primo-discovery
- description: 'Identity and access management at Humboldt-Universität zu Berlin uses Shibboleth/SAML single sign-on, operated by the Computer- und Medienservice (CMS). Service-provider integration is documented for '
  name: HU-IAM Shibboleth Single Sign-On (SAML)
  slug: shibboleth-sso
- description: Core repository resources (communities, collections, items)
  name: Humboldt-Universität zu Berlin Core API
  slug: humboldt-universitat-zu-berlin-core-api
- description: Search and discovery over indexed repository objects
  name: Humboldt-Universität zu Berlin Discovery API
  slug: humboldt-universitat-zu-berlin-discovery-api
- description: API root and capability discovery
  name: Humboldt-Universität zu Berlin Root API
  slug: humboldt-universitat-zu-berlin-root-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: edoc-Server DSpace REST API (Humboldt-Universität zu Berlin) Core API
  slug: open-humboldt-universitat-zu-berlin-core-api
- collection_type: open
  name: edoc-Server DSpace REST API (Humboldt-Universität zu Berlin) Core Discovery API
  slug: open-humboldt-universitat-zu-berlin-discovery-api
- collection_type: open
  name: edoc-Server DSpace REST API (Humboldt-Universität zu Berlin) Core Root API
  slug: open-humboldt-universitat-zu-berlin-root-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/humboldt-universitat-zu-berlin-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/humboldt-universitat-zu-berlin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/humboldt-universitat-zu-berlin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hu-berlin.de/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UB-HU-Berlin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/humboldt-universitat-zu-berlin/
- group: auth
  title: ''
  type: Authentication
  url: https://www.cms.hu-berlin.de/de/dl/hu-iam/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/humboldt-universitat-zu-berlin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/humboldt-universitat-zu-berlin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/humboldt-universitat-zu-berlin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Humboldt-Universität zu Berlin (HU Berlin) is a public research university in Berlin, Germany, ranked #126 in the QS World University Rankings 2025. Its public developer/API footprint is centered on scholarly and library infrastructure rather than a unified developer portal: the edoc Open Access publication server runs on DSpace 7 and exposes a public REST API and an OAI-PMH metadata interface, the University Library''s Primus discovery service is built on Ex Libris Primo/Alma (which provides open APIs), and access management uses Shibboleth/SAML single sign-on. The University Library IT department also maintains a public GitHub organization (UB-HU-Berlin). No consolidated, self-service public API developer portal was confirmed.'
examples:
- key_count: 8
  name: Humboldt Universitat Zu Berlin Get Collection Example
  slug: humboldt-universitat-zu-berlin-get-collection-example
- key_count: 2
  name: Humboldt Universitat Zu Berlin List Communities Example
  slug: humboldt-universitat-zu-berlin-list-communities-example
- key_count: 1
  name: Humboldt Universitat Zu Berlin Search Objects Example
  slug: humboldt-universitat-zu-berlin-search-objects-example
finops:
- name: Humboldt Universitat Zu Berlin Finops
  service_category: Education
  slug: humboldt-universitat-zu-berlin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/humboldt-universitat-zu-berlin.png
json_schemas:
- name: DSpace Collection
  property_count: 8
  slug: humboldt-universitat-zu-berlin-collection
- name: DSpace Community
  property_count: 8
  slug: humboldt-universitat-zu-berlin-community
- name: DSpace Item
  property_count: 12
  slug: humboldt-universitat-zu-berlin-item
json_structures:
- name: Humboldt Universitat Zu Berlin Community Structure
  property_count: 7
  slug: humboldt-universitat-zu-berlin-community-structure
- name: Humboldt Universitat Zu Berlin Item Structure
  property_count: 11
  slug: humboldt-universitat-zu-berlin-item-structure
jsonld:
- class_count: 15
  name: Humboldt Universitat Zu Berlin Context
  property_count: 8
  slug: humboldt-universitat-zu-berlin-context
layout: provider
modified: '2026-06-03'
name: Humboldt-Universität zu Berlin
nav: Providers
network: true
overview: 'Humboldt-Universität zu Berlin publishes 3 APIs on the [APIs.io](https://apis.io/) network: Core API, Discovery API, and Root API. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Humboldt-Universität zu Berlin catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Humboldt-Universität zu Berlin''s developer surface includes GitHub presence, authentication, and 9 more developer resources.'
plans:
- name: Humboldt Universitat Zu Berlin Plans Pricing
  plan_count: 2
  slug: humboldt-universitat-zu-berlin-plans-pricing
random_paper: 107
rate_limits:
- limit_count: 1
  name: Humboldt Universitat Zu Berlin Rate Limits
  slug: humboldt-universitat-zu-berlin-rate-limits
rules:
- name: Humboldt-Universität zu Berlin API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: humboldt-universitat-zu-berlin-jsonschema-spectral-rules
- name: Humboldt-Universität zu Berlin API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 3
  slug: humboldt-universitat-zu-berlin-rules
score:
  band: thin
  composite: 39.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 59.5
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/humboldt-universitat-zu-berlin/refs/heads/main/screenshots/humboldt-universitat-zu-berlin-2026-06-20T182937.png
security:
- kind: domain-security
  name: Humboldt Universitat Zu Berlin Domain Security
  slug: humboldt-universitat-zu-berlin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Humboldt Universitat Zu Berlin Vulnerability Disclosure
  slug: humboldt-universitat-zu-berlin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: humboldt-universitat-zu-berlin
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Library
- Germany
website: https://www.hu-berlin.de/en
---
