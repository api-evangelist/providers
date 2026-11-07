---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Smartsheet Agentic Access
  operation_count: 10
  slug: smartsheet-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- description: 'REST API v2.0 for managing sheets, rows, columns, cells, reports, workspaces, folders, users, groups, attachments, discussions, automation rules, and webhooks. Authentication uses OAuth 2.0 or Bearer '
  name: Smartsheet REST API
  slug: rest-api
- baseURL: https://api.smartsheet.com/2.0
  baseurl_source: declared
  description: Manage columns within sheets.
  name: Smartsheet Columns API
  slug: smartsheet-columns-api
- baseURL: https://api.smartsheet.com/2.0
  baseurl_source: declared
  description: Retrieve report data.
  name: Smartsheet Reports API
  slug: smartsheet-reports-api
- baseURL: https://api.smartsheet.com/2.0
  baseurl_source: declared
  description: Manage rows within sheets.
  name: Smartsheet Rows API
  slug: smartsheet-rows-api
- baseURL: https://api.smartsheet.com/2.0
  baseurl_source: declared
  description: Manage Smartsheet sheets.
  name: Smartsheet Sheets API
  slug: smartsheet-sheets-api
- baseURL: https://api.smartsheet.com/2.0
  baseurl_source: declared
  description: Manage webhook subscriptions.
  name: Smartsheet Webhooks API
  slug: smartsheet-webhooks-api
artifact_total: 19
collections:
- collection_type: open
  name: Smartsheet Columns API
  slug: open-smartsheet-columns-api
- collection_type: open
  name: Smartsheet Columns Reports API
  slug: open-smartsheet-reports-api
- collection_type: open
  name: Smartsheet Columns Rows API
  slug: open-smartsheet-rows-api
- collection_type: open
  name: Smartsheet Columns Sheets API
  slug: open-smartsheet-sheets-api
- collection_type: open
  name: Smartsheet Columns Webhooks API
  slug: open-smartsheet-webhooks-api
- collection_type: open
  name: Smartsheet API
  slug: open-smartsheet
common:
- group: other
  href: https://artifacts.apis.io/smartsheet/capabilities/smartsheet-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/smartsheet-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/smartsheet/agentic-access/smartsheet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/smartsheet-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/smartsheet/security/smartsheet-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/smartsheet-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/smartsheet/security/smartsheet-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/smartsheet-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/smartsheet/security/smartsheet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smartsheet-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/smartsheet/authentication/smartsheet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smartsheet-authentication.yml
- group: auth
  href: https://artifacts.apis.io/smartsheet/scopes/smartsheet-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/smartsheet-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smartsheet-com
- group: company
  title: ''
  type: Website
  url: https://www.smartsheet.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.smartsheet.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.smartsheet.com/
- group: start
  title: ''
  type: Signup
  url: https://www.smartsheet.com/try-it
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smartsheet.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smartsheet-platform
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.smartsheet.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.smartsheet.com/blog
created: '2026-05-11'
description: Smartsheet is a SaaS work management and collaboration platform that combines spreadsheet-style sheets, project plans, Gantt charts, dashboards, forms, and workflow automation for teams and enterprises. The Smartsheet REST API provides programmatic access to sheets, rows, columns, reports, workspaces, users, attachments, and webhooks using OAuth 2.0 or API access tokens.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartsheet.png
layout: provider
modified: '2026-05-11'
name: Smartsheet
nav: Providers
network: true
overview: 'Smartsheet publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Columns API, Reports API, Rows API, and 3 more. Tagged areas include Work Management, Project Management, Collaboration, Productivity, and Workflow Automation.


  The Smartsheet catalog on APIs.io includes 1 Spectral governance ruleset.


  Smartsheet''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, and 11 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Smartsheet API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: smartsheet-rules
scopes:
- name: Smartsheet Scopes
  scope_count: 10
  slug: smartsheet-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 49.0
    developer_ergonomics: 52.4
    discoverability: 73.2
    operational_transparency: 13.2
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/smartsheet/smartsheet-2026-06-20T194052.png
security:
- kind: authentication
  name: Smartsheet Authentication
  slug: smartsheet-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Smartsheet Domain Security
  slug: smartsheet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Smartsheet Vulnerability Disclosure
  slug: smartsheet-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Smartsheet Trust Center
  slug: smartsheet-trust-center
  summary_line: HIPAA, FedRAMP
slug: smartsheet
tags:
- Work Management
- Project Management
- Collaboration
- Productivity
- Workflow Automation
- Spreadsheets
website: https://www.smartsheet.com
---
