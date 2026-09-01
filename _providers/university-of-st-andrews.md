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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of St Andrews Agentic Access
  operation_count: 4
  slug: university-of-st-andrews-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: OAI-PMH (Open Archives Initiative Protocol for Metadata Harvesting) endpoint for the University of St Andrews Pure research information system, which underpins the public St Andrews Research Portal. A
  name: Pure Research Portal OAI-PMH
  slug: pure-oai
- description: OAI-PMH endpoint for the DSpace-based St Andrews Research Repository, the institution's open-access repository of theses, articles, and other research outputs. Supports metadata harvesting via standar
  name: St Andrews Research Repository OAI-PMH
  slug: repository-oai
- description: System components and their hierarchy.
  name: University of St Andrews Components API
  slug: university-of-st-andrews-components-api
- description: Incidents and maintenance notices.
  name: University of St Andrews Notices API
  slug: university-of-st-andrews-notices-api
- description: Overall page status.
  name: University of St Andrews Status API
  slug: university-of-st-andrews-status-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: University of St Andrews Service Status Components API
  slug: open-university-of-st-andrews-components-api
- collection_type: open
  name: University of St Andrews Service Status Components Notices API
  slug: open-university-of-st-andrews-notices-api
- collection_type: open
  name: University of St Andrews Service Components Status API
  slug: open-university-of-st-andrews-status-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-st-andrews-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-st-andrews-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-st-andrews-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.st-andrews.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/StAResComp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-st-andrews/
- group: operate
  title: ''
  type: Status
  url: https://status.st-andrews.ac.uk/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-st-andrews-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-st-andrews-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-st-andrews-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of St Andrews is Scotland''s first university (founded 1413) and ranked #90 in the QS World University Rankings 2025. Its public developer and API footprint is modest and oriented toward research-data interoperability and operational transparency rather than a centralized developer portal. Confirmed public, machine-readable interfaces include a JSON service-status API, an OAI-PMH endpoint for the Pure research information system behind the St Andrews Research Portal, and an OAI-PMH interface for the DSpace-based St Andrews Research Repository. The university also maintains a Research Computing GitHub organization for software produced for and by its researchers.'
examples:
- key_count: 1
  name: University Of St Andrews Getnotice Example
  slug: university-of-st-andrews-getNotice-example
- key_count: 1
  name: University Of St Andrews Getstatus Example
  slug: university-of-st-andrews-getStatus-example
- key_count: 2
  name: University Of St Andrews Listcomponents Example
  slug: university-of-st-andrews-listComponents-example
- key_count: 2
  name: University Of St Andrews Listnotices Example
  slug: university-of-st-andrews-listNotices-example
finops:
- name: University Of St Andrews Finops
  service_category: Education
  slug: university-of-st-andrews-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-st-andrews.png
json_schemas:
- name: Component
  property_count: 9
  slug: university-of-st-andrews-component
- name: Notice
  property_count: 17
  slug: university-of-st-andrews-notice
- name: Page
  property_count: 8
  slug: university-of-st-andrews-page
json_structures:
- name: University Of St Andrews Component Structure
  property_count: 9
  slug: university-of-st-andrews-component-structure
- name: University Of St Andrews Notice Structure
  property_count: 15
  slug: university-of-st-andrews-notice-structure
jsonld:
- class_count: 28
  name: University Of St Andrews Context
  property_count: 2
  slug: university-of-st-andrews-context
layout: provider
modified: '2026-06-03'
name: University of St Andrews
nav: Providers
network: true
overview: 'University of St Andrews publishes 3 APIs on the [APIs.io](https://apis.io/) network: Components API, Notices API, and Status API. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The University of St Andrews catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of St Andrews'' developer surface includes GitHub presence, status page, and 9 more developer resources.'
plans:
- name: University Of St Andrews Plans Pricing
  plan_count: 2
  slug: university-of-st-andrews-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: University Of St Andrews Rate Limits
  slug: university-of-st-andrews-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of St Andrews API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-st-andrews-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: University of St Andrews API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: university-of-st-andrews-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 54.4
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-st-andrews/refs/heads/main/screenshots/university-of-st-andrews-2026-06-20T200233.png
security:
- kind: domain-security
  name: University Of St Andrews Domain Security
  slug: university-of-st-andrews-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of St Andrews Vulnerability Disclosure
  slug: university-of-st-andrews-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-st-andrews
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- OAI-PMH
- Scotland
- United Kingdom
website: https://www.st-andrews.ac.uk/
---
