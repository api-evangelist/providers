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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Regulations Gov Agentic Access
  operation_count: 7
  slug: regulations-gov-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://api.regulations.gov
  baseurl_source: declared
  description: Utilities to support submitting public comments
  name: Regulations.gov comment submission utilities API
  slug: regulations-gov-comment-submission-utilities-api
- baseURL: https://api.regulations.gov
  baseurl_source: declared
  description: Public comments submitted on regulatory documents
  name: Regulations.gov comments API
  slug: regulations-gov-comments-api
- baseURL: https://api.regulations.gov
  baseurl_source: declared
  description: Regulatory dockets grouping related documents
  name: Regulations.gov dockets API
  slug: regulations-gov-dockets-api
- baseURL: https://api.regulations.gov
  baseurl_source: declared
  description: Federal regulatory documents including notices, rules, and proposed rules
  name: Regulations.gov documents API
  slug: regulations-gov-documents-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Regulations.gov comment submission utilities API
  slug: open-regulations-gov-comment-submission-utilities-api
- collection_type: open
  name: Regulations.gov comment submission utilities comments API
  slug: open-regulations-gov-comments-api
- collection_type: open
  name: Regulations.gov comment submission utilities dockets API
  slug: open-regulations-gov-dockets-api
- collection_type: open
  name: Regulations.gov comment submission utilities documents API
  slug: open-regulations-gov-documents-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/regulations-gov-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/regulations-gov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/regulations-gov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/regulations-gov-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.regulations.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://open.gsa.gov/api/regulationsgov/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/GSA
- group: company
  title: ''
  type: Blog
  url: https://www.gsa.gov/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://api.data.gov/docs/rate-limits/
- group: commercial
  title: ''
  type: Plans
  url: plans/regulations-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/regulations-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/regulations-gov-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://www.regulations.gov/support
created: '2026-06-13'
description: Regulations.gov is the US federal government's central portal for public participation in the rulemaking process, operated by the General Services Administration. Its REST API enables programmatic access to regulatory dockets, proposed rules, final rules, supporting documents, and public comments submitted to federal agencies. Developers can search and filter content across all federal agencies, retrieve full document and comment details with attachments, and submit public comments programmatically. The API is managed through api.data.gov and uses API key authentication.
examples:
- key_count: 2
  name: Comment List Response
  slug: comment-list-response
- key_count: 1
  name: Comment Submission Request
  slug: comment-submission-request
- key_count: 1
  name: Docket Detail Response
  slug: docket-detail-response
- key_count: 2
  name: Document List Response
  slug: document-list-response
finops:
- name: Regulations Gov Finops
  service_category: ''
  slug: regulations-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/regulations-gov.png
json_schemas:
- name: Comment
  property_count: 3
  slug: comment
- name: Docket
  property_count: 3
  slug: docket
- name: Document
  property_count: 3
  slug: document
jsonld:
- class_count: 5
  name: Regulations Gov Context
  property_count: 99
  slug: regulations-gov-context
layout: provider
modified: '2026-06-13'
name: Regulations.gov
nav: Providers
network: true
overview: 'Regulations.gov publishes 4 APIs on the [APIs.io](https://apis.io/) network, including comment submission utilities API, comments API, dockets API, and 1 more. Tagged areas include Government, Federal Rulemaking, Public Comments, Regulatory, and Dockets.


  The Regulations.gov catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Regulations.gov''s developer surface includes authentication, documentation, engineering blog, pricing, support, and 8 more developer resources.'
plans:
- name: Regulations Gov Plans Pricing
  plan_count: 2
  slug: regulations-gov-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Regulations Gov Rate Limits
  slug: regulations-gov-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Regulations.gov API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: regulations-gov-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 62.8
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/regulations-gov/refs/heads/main/screenshots/regulations-gov-2026-06-20T192801.png
security:
- kind: authentication
  name: Regulations Gov Authentication
  slug: regulations-gov-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Regulations Gov Domain Security
  slug: regulations-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: regulations-gov
tags:
- Government
- Federal Rulemaking
- Public Comments
- Regulatory
- Dockets
- GSA
- Open Data
website: https://www.regulations.gov/
---
