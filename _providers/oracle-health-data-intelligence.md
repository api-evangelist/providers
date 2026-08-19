---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Oracle Health Data Intelligence Agentic Access
  operation_count: 2
  slug: oracle-health-data-intelligence-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: 'Oracle Health Data Intelligence is a comprehensive platform that leverages advanced analytics and artificial intelligence to collect and analyze health data from various sources, including electronic '
  name: Oracle Health Data Intelligence
  slug: oracle-health-data-intelligence
- description: The Populations API from Oracle Health Data Intelligence — 2 operation(s) for populations.
  name: Oracle Health Data Intelligence Populations API
  slug: oracle-health-data-intelligence-populations-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle Health Data Intelligence - Allergy Populations API
  slug: open-oracle-health-data-intelligence-populations-api
- collection_type: open
  name: Oracle Health Data Intelligence - Allergy API
  slug: open-oracle-health-data-intelligence
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-health-data-intelligence-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-health-data-intelligence-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-health-data-intelligence-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
created: '2025-01-07'
description: Oracle Health Data Intelligence is a comprehensive platform that leverages advanced analytics and artificial intelligence to provide actionable insights and support informed decision-making in healthcare. By integrating data from multiple sources, such as electronic health records, claims data, and genomic information, Oracle Health Data Intelligence enables healthcare organizations to gain a holistic view of patient populations, identify trends and patterns, and improve care delivery.
finops:
- name: Oracle Health Data Intelligence Finops
  service_category: API
  slug: oracle-health-data-intelligence-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-health-data-intelligence.png
layout: provider
modified: '2026-03-16'
name: Oracle Health Data Intelligence
nav: Providers
network: true
overview: 'Oracle Health Data Intelligence publishes 1 API on the [APIs.io](https://apis.io/) network: Populations API. Tagged areas include Genomic, Health Records, and Healthcare.


  Oracle Health Data Intelligence''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Oracle Health Data Intelligence Plans Pricing
  plan_count: 3
  slug: oracle-health-data-intelligence-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 5
  name: Oracle Health Data Intelligence Rate Limits
  slug: oracle-health-data-intelligence-rate-limits
score:
  band: emerging
  composite: 25.0
  delta: 0.1
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 54.5
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 24.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-health-data-intelligence/refs/heads/main/screenshots/oracle-health-data-intelligence-2026-06-20T191145.png
security:
- kind: authentication
  name: Oracle Health Data Intelligence Authentication
  slug: oracle-health-data-intelligence-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Oracle Health Data Intelligence Domain Security
  slug: oracle-health-data-intelligence-domain-security
  summary_line: TLSv1.3
slug: oracle-health-data-intelligence
tags:
- Genomic
- Health Records
- Healthcare
---
