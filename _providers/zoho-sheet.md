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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 30.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Zoho Sheet Agentic Access
  operation_count: 1
  slug: zoho-sheet-agentic-access
  summary_line: 1 operation · 1 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://sheet.zoho.com/api/v2
  baseurl_source: declared
  description: Operations on Zoho Sheet workbooks (spreadsheet files)
  name: Zoho Sheet Workbook API
  slug: zoho-sheet-workbook-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zoho Sheet Data Workbook API
  slug: open-zoho-sheet-workbook-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoho-sheet-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-sheet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-sheet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoho-sheet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoho-sheet-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/sheet/
- group: docs
  title: ''
  type: Documentation
  url: https://sheet.zoho.com/help/api/v2/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zoho-corporation/
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/blog/sheet
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/workplace/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://us.zohostatus.com/
- group: other
  title: ''
  type: X
  url: https://x.com/zoho
- group: commercial
  title: ''
  type: Plans
  url: plans/zoho-sheet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoho-sheet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zoho-sheet-finops.yml
created: '2026-06-13'
description: Online spreadsheet application with a REST API for reading, writing, and manipulating spreadsheet data, cells, formulas, and exporting to various formats. The Zoho Sheet Data API v2 supports workbook management, worksheet operations, cell content manipulation, chart management, tabular data operations, pivot tables, and merge templates. Authentication uses OAuth 2.0 with scopes for read and update access.
examples:
- key_count: 4
  name: Add Worksheet
  slug: add-worksheet
- key_count: 4
  name: Oauth Token
  slug: oauth-token
- key_count: 4
  name: Read Worksheet Records
  slug: read-worksheet-records
- key_count: 4
  name: Write Worksheet Records
  slug: write-worksheet-records
finops:
- name: Zoho Sheet Finops
  service_category: ''
  slug: zoho-sheet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-sheet.png
json_schemas:
- name: Zoho Sheet API Response
  property_count: 9
  slug: api-response
- name: Zoho Sheet Cell Record
  property_count: 0
  slug: cell-record
- name: Zoho Sheet Workbook
  property_count: 5
  slug: workbook
layout: provider
modified: '2026-06-13'
name: Zoho Sheet
nav: Providers
network: true
overview: 'Zoho Sheet publishes 1 API on the [APIs.io](https://apis.io/) network: Workbook API. Tagged areas include Spreadsheets, Productivity, Collaboration, Data, and Office.


  The Zoho Sheet catalog on APIs.io includes 1 Spectral governance ruleset.


  Zoho Sheet''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Zoho Sheet Plans Pricing
  plan_count: 4
  slug: zoho-sheet-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Zoho Sheet Rate Limits
  slug: zoho-sheet-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Zoho Sheet API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zoho-sheet-jsonschema-spectral-rules
scopes:
- name: Zoho Sheet Scopes
  scope_count: 2
  slug: zoho-sheet-scopes
  summary_line: 2 scopes · authorizationCode/implicit/clientCredentials
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 55.1
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-sheet/refs/heads/main/screenshots/zoho-sheet-2026-06-20T201949.png
security:
- kind: authentication
  name: Zoho Sheet Authentication
  slug: zoho-sheet-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zoho Sheet Domain Security
  slug: zoho-sheet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Sheet Vulnerability Disclosure
  slug: zoho-sheet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-sheet
tags:
- Spreadsheets
- Productivity
- Collaboration
- Data
- Office
- Zoho
website: https://www.zoho.com/sheet/
---
