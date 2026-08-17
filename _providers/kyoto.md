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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kyoto Agentic Access
  operation_count: 6
  slug: kyoto-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- description: The Institute for Information Management and Communication (IIMC) operates a Shibboleth-based SAML identity provider for university-wide accounts (SPS-ID / ECS-ID) with multi-factor authentication. Fe
  name: Kyoto University Integrated Authentication (Shibboleth/SAML)
  slug: sso
- description: OAI-PMH 2.0 metadata harvesting interface
  name: Kyoto University OAI-PMH API
  slug: kyoto-oai-pmh-api
- description: DSpace 7.6 HAL+JSON REST API
  name: Kyoto University REST API
  slug: kyoto-rest-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KURENAI Repository API (DSpace 7.6 REST + ) OAI-PMH API
  slug: open-kyoto-oai-pmh-api
- collection_type: open
  name: KURENAI Repository API (DSpace 7.6 + ) OAI-PMH REST API
  slug: open-kyoto-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kyoto-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kyoto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kyoto-u.ac.jp/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kyoto-u
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/kyoto-university/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Kyoto_Univ_PR
- group: auth
  title: ''
  type: Authentication
  url: https://www.iimc.kyoto-u.ac.jp/en/services/account/auth-system
- group: commercial
  title: ''
  type: Plans
  url: plans/kyoto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kyoto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kyoto-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Kyoto University is a national research university in Kyoto, Japan, ranked #37 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is centered on scholarly and open-source infrastructure rather than a centralized developer portal. Confirmed public surfaces include the KURENAI research information repository (DSpace) with a live OAI-PMH metadata endpoint, the kyoto-u "Kyoto University Open Source Project" GitHub organization, and a Shibboleth/SAML integrated authentication system operated by the Institute for Information Management and Communication (IIMC). Student information, course, and timetable systems are gated behind campus accounts and are not publicly documented APIs.'
examples:
- key_count: 6
  name: Kyoto Getroot Example
  slug: kyoto-getRoot-example
- key_count: 2
  name: Kyoto Listcommunities Example
  slug: kyoto-listCommunities-example
- key_count: 3
  name: Kyoto Oaiidentify Example
  slug: kyoto-oaiIdentify-example
finops:
- name: Kyoto Finops
  service_category: Education
  slug: kyoto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kyoto.png
json_schemas:
- name: KURENAI Collection
  property_count: 6
  slug: kyoto-collection
- name: KURENAI Community
  property_count: 9
  slug: kyoto-community
json_structures:
- name: Kyoto Collection Structure
  property_count: 5
  slug: kyoto-collection-structure
- name: Kyoto Community Structure
  property_count: 7
  slug: kyoto-community-structure
jsonld:
- class_count: 9
  name: Kyoto Context
  property_count: 6
  slug: kyoto-context
layout: provider
modified: '2026-06-03'
name: Kyoto University
nav: Providers
network: true
overview: 'Kyoto University publishes 2 APIs on the [APIs.io](https://apis.io/) network: OAI-PMH API and REST API. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Kyoto University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Kyoto University''s developer surface includes GitHub presence, authentication, and 9 more developer resources.'
plans:
- name: Kyoto Plans Pricing
  plan_count: 2
  slug: kyoto-plans-pricing
random_paper: 119
rate_limits:
- limit_count: 1
  name: Kyoto Rate Limits
  slug: kyoto-rate-limits
rules:
- name: Kyoto University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: kyoto-jsonschema-spectral-rules
- name: Kyoto University API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: kyoto-rules
score:
  band: thin
  composite: 37.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 37.5
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
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kyoto/refs/heads/main/screenshots/kyoto-2026-06-20T184226.png
security:
- kind: domain-security
  name: Kyoto Domain Security
  slug: kyoto-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kyoto
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Scholarly
- Repository
- Japan
website: https://www.kyoto-u.ac.jp/en
---
