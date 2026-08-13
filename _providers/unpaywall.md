---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
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
  score: 35.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Unpaywall Agentic Access
  operation_count: 2
  slug: unpaywall-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Look up open access status by DOI
  name: Unpaywall DOI Lookup API
  slug: unpaywall-doi-lookup-api
- description: Search articles by title
  name: Unpaywall Search API
  slug: unpaywall-search-api
artifact_total: 15
collections:
- collection_type: open
  name: Unpaywall API
  slug: open-unpaywall
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unpaywall-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unpaywall-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ourresearch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/impactstory
- group: company
  title: ''
  type: Website
  url: https://unpaywall.org
- group: docs
  title: ''
  type: Documentation
  url: https://unpaywall.org/products/api
- group: other
  title: ''
  type: DataFormat
  url: https://unpaywall.org/data-format
- group: operate
  title: ''
  type: Support
  url: https://support.unpaywall.org
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/unpaywall/refs/heads/main/vocabulary/unpaywall-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/unpaywall/refs/heads/main/json-ld/unpaywall-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://unpaywall.org/llms.txt
created: '2025-02-06'
description: The Unpaywall REST API gives anyone free, programmatic access to the Unpaywall database of open access scholarly articles. The database covers over 120 million articles with Crossref DOIs and provides free, legal full-text links where available, with metadata on OA status (gold, hybrid, bronze, green), host type (publisher, repository), version (published, accepted, submitted), and license information.
examples:
- key_count: 2
  name: Unpaywall Get Doi Example
  slug: unpaywall-get-doi-example
- key_count: 2
  name: Unpaywall Search Example
  slug: unpaywall-search-example
finops:
- name: Unpaywall Finops
  service_category: API
  slug: unpaywall-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unpaywall.png
json_schemas:
- name: Unpaywall Article Object
  property_count: 23
  slug: unpaywall-article
json_structures:
- name: Unpaywall Article Structure
  property_count: 0
  slug: unpaywall-article-structure
jsonld:
- class_count: 8
  name: Unpaywall Context
  property_count: 37
  slug: unpaywall-context
layout: provider
modified: '2026-05-19'
name: Unpaywall
nav: Providers
network: true
overview: 'Unpaywall publishes 2 APIs on the [APIs.io](https://apis.io/) network: DOI Lookup API and Search API. Tagged areas include Open Access, Scholarly Articles, Research, Academic, and Libraries.


  The Unpaywall catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Unpaywall''s developer surface includes documentation, support, and 9 more developer resources.'
plans:
- name: Unpaywall Plans Pricing
  plan_count: 3
  slug: unpaywall-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Unpaywall Rate Limits
  slug: unpaywall-rate-limits
rules:
- name: Unpaywall API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: unpaywall-jsonschema-spectral-rules
- name: Unpaywall API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: unpaywall-rules
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 71.6
    developer_ergonomics: 13.0
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unpaywall/refs/heads/main/screenshots/unpaywall-2026-06-20T200345.png
security:
- kind: domain-security
  name: Unpaywall Domain Security
  slug: unpaywall-domain-security
  summary_line: TLSv1.3
slug: unpaywall
tags:
- Open Access
- Scholarly Articles
- Research
- Academic
- Libraries
- DOI
- Science
website: https://unpaywall.org
---
