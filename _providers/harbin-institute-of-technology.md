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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Harbin Institute Of Technology Agentic Access
  operation_count: 16
  slug: harbin-institute-of-technology-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 1
apis:
- description: RSS 2.0 feeds (with Dublin Core extensions) from the HIT Elsevier Pure research portal. The research output feed returns the latest publications; a persons feed lists researcher profiles. Verified liv
  name: HIT Research Portal RSS Feeds
  slug: pure-rss
- description: The person API from Harbin Institute of Technology — 5 operation(s) for person.
  name: Harbin Institute of Technology person API
  slug: harbin-institute-of-technology-person-api
- description: The researchOutput API from Harbin Institute of Technology — 5 operation(s) for researchoutput.
  name: Harbin Institute of Technology researchOutput API
  slug: harbin-institute-of-technology-researchoutput-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HIT Research Portal (Pure) person API
  slug: open-harbin-institute-of-technology-person-api
- collection_type: open
  name: HIT Research Portal (Pure) person researchOutput API
  slug: open-harbin-institute-of-technology-researchoutput-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/harbin-institute-of-technology-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harbin-institute-of-technology-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/harbin-institute-of-technology-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harbin-institute-of-technology-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harbin-institute-of-technology-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://en.hit.edu.cn/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://scholar.hit.edu.cn/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/HITSZ-HLT
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/harbin-institute-of-technology/
- group: commercial
  title: ''
  type: Plans
  url: plans/harbin-institute-of-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/harbin-institute-of-technology-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/harbin-institute-of-technology-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Harbin Institute of Technology (HIT) is a public research university in Harbin, Heilongjiang, China, founded in 1920 and overseen by the Ministry of Industry and Information Technology, with additional campuses in Weihai and Shenzhen. It is ranked #252 in the QS World University Rankings 2025. HIT does not operate a formal public developer portal, but its Elsevier Pure research portal (scholar.hit.edu.cn) exposes standard machine-readable interfaces: an OAI-PMH endpoint (verified live, OpenAIRE CERIF 1.2 profile) and RSS feeds of research outputs and researcher profiles. Most other institutional systems (library OPAC, institutional repository, student/SSO systems) are gated and do not publish open, documented APIs.'
examples:
- key_count: 8
  name: Harbin Institute Of Technology Person Get Example
  slug: harbin-institute-of-technology-person-get-example
- key_count: 3
  name: Harbin Institute Of Technology Research Outputs List Example
  slug: harbin-institute-of-technology-research-outputs-list-example
- key_count: 7
  name: Harbin Institute Of Technology Research Outputs Search Example
  slug: harbin-institute-of-technology-research-outputs-search-example
finops:
- name: Harbin Institute Of Technology Finops
  service_category: Education
  slug: harbin-institute-of-technology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harbin-institute-of-technology.png
json_schemas:
- name: HIT Person
  property_count: 51
  slug: harbin-institute-of-technology-person
- name: HIT Research Output
  property_count: 53
  slug: harbin-institute-of-technology-research-output
json_structures:
- name: Harbin Institute Of Technology Person Structure
  property_count: 51
  slug: harbin-institute-of-technology-person-structure
- name: Harbin Institute Of Technology Research Output Structure
  property_count: 53
  slug: harbin-institute-of-technology-research-output-structure
jsonld:
- class_count: 11
  name: Harbin Institute Of Technology Context
  property_count: 4
  slug: harbin-institute-of-technology-context
layout: provider
modified: '2026-06-03'
name: Harbin Institute of Technology
nav: Providers
network: true
overview: 'Harbin Institute of Technology publishes 2 APIs on the [APIs.io](https://apis.io/) network: person API and researchOutput API. Tagged areas include Education, Higher Education, University, Research, and Scholarly.


  The Harbin Institute of Technology catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Harbin Institute of Technology''s developer surface includes authentication, GitHub presence, and 11 more developer resources.'
plans:
- name: Harbin Institute Of Technology Plans Pricing
  plan_count: 2
  slug: harbin-institute-of-technology-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Harbin Institute Of Technology Rate Limits
  slug: harbin-institute-of-technology-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Harbin Institute of Technology API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: harbin-institute-of-technology-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Harbin Institute of Technology API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: harbin-institute-of-technology-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 41.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 65.3
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harbin-institute-of-technology/refs/heads/main/screenshots/harbin-institute-of-technology-2026-06-20T182524.png
security:
- kind: authentication
  name: Harbin Institute Of Technology Authentication
  slug: harbin-institute-of-technology-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Harbin Institute Of Technology Domain Security
  slug: harbin-institute-of-technology-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Harbin Institute Of Technology Vulnerability Disclosure
  slug: harbin-institute-of-technology-vulnerability-disclosure
  summary_line: disclosure policy published
slug: harbin-institute-of-technology
tags:
- Education
- Higher Education
- University
- Research
- Scholarly
- OAI-PMH
- China
website: https://en.hit.edu.cn/
---
