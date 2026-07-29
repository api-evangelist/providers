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
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Imperial College London Agentic Access
  operation_count: 8
  slug: imperial-college-london-agentic-access
  summary_line: 8 operations
api_count: 4
apis:
- description: Imperial's SAML 2.0 federated identity provider participates in the UK Access Management Federation. It is a standards-based single sign-on integration interface rather than a REST API; access require
  name: Imperial Shibboleth Identity Provider (SAML 2.0)
  slug: shibboleth
- description: Communities, collections, and items.
  name: Imperial College London Core API
  slug: imperial-college-london-core-api
- description: Search and browse over indexed objects.
  name: Imperial College London Discover API
  slug: imperial-college-london-discover-api
- description: API entry point and link index.
  name: Imperial College London Root API
  slug: imperial-college-london-root-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/imperial-college-london-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imperial-college-london-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.imperial.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ImperialCollegeLondon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/imperial-college-london/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/imperialcollege
- group: commercial
  title: ''
  type: Plans
  url: plans/imperial-college-london-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/imperial-college-london-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/imperial-college-london-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Imperial College London is a UK public research university (QS World 2025 #2) specializing in science, engineering, medicine, and business. Its public developer footprint is infrastructure-oriented rather than a published API program: the institution operates a large GitHub organization for staff and student code, the Spiral open-access research repository (DSpace-CRIS), an Ex Libris Primo/Alma library discovery system, and Shibboleth/SAML federated identity. Imperial does not publish a first-party, self-service developer portal with open REST endpoints; most machine-accessible interfaces are protocol-standard (OAI-PMH, SAML), vendor-hosted, or require institutional authentication.'
examples:
- key_count: 8
  name: Imperial College London Getcommunity Example
  slug: imperial-college-london-getCommunity-example
- key_count: 9
  name: Imperial College London Searchobjects Example
  slug: imperial-college-london-searchObjects-example
finops:
- name: Imperial College London Finops
  service_category: Education
  slug: imperial-college-london-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imperial-college-london.png
json_schemas:
- name: Spiral DSpace Community
  property_count: 8
  slug: imperial-college-london-community
- name: Spiral DSpace Item
  property_count: 12
  slug: imperial-college-london-item
json_structures:
- name: Imperial College London Community Structure
  property_count: 7
  slug: imperial-college-london-community-structure
- name: Imperial College London Item Structure
  property_count: 11
  slug: imperial-college-london-item-structure
jsonld:
- class_count: 20
  name: Imperial College London Context
  property_count: 0
  slug: imperial-college-london-context
layout: provider
modified: '2026-06-03'
name: Imperial College London
nav: Providers
network: true
overview: 'Imperial College London publishes 3 APIs on the [APIs.io](https://apis.io/) network: Core API, Discover API, and Root API. Tagged areas include Education, Higher Education, University, Research, and United Kingdom.


  The Imperial College London catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Imperial College London''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Imperial College London Plans Pricing
  plan_count: 2
  slug: imperial-college-london-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 1
  name: Imperial College London Rate Limits
  slug: imperial-college-london-rate-limits
rules:
- name: Imperial College London API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: imperial-college-london-jsonschema-spectral-rules
- name: Imperial College London API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 2
  slug: imperial-college-london-rules
score:
  band: thin
  composite: 37.0
  delta: -4.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 57.1
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imperial-college-london/refs/heads/main/screenshots/imperial-college-london-2026-06-20T183255.png
security:
- kind: domain-security
  name: Imperial College London Domain Security
  slug: imperial-college-london-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: imperial-college-london
tags:
- Education
- Higher Education
- University
- Research
- United Kingdom
- Open Access
- Repository
- Identity
website: https://www.imperial.ac.uk/
---
