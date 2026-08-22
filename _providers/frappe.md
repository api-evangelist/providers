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
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Frappe Agentic Access
  operation_count: 10
  slug: frappe-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 2
apis:
- description: The Method API from Frappe — 4 operation(s) for method.
  name: Frappe Method API
  slug: frappe-method-api
- description: The Resource API from Frappe — 2 operation(s) for resource.
  name: Frappe Resource API
  slug: frappe-resource-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Frappe Framework REST Method API
  slug: open-frappe-method-api
- collection_type: open
  name: Frappe Framework REST Method Resource API
  slug: open-frappe-resource-api
- collection_type: open
  name: Frappe Framework REST API
  slug: open-frappe
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/frappe/frappe/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/frappe/frappe/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/frappe/frappe/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/frappe/frappe/blob/develop/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/frappe/frappe/blob/develop/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/frappe/frappe/blob/develop/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/frappe-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/frappe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/frappe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/frappe-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/frappe-technologies
- group: company
  title: ''
  type: Website
  url: https://frappe.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.frappe.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/frappe
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/frappe/frappe
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/frappe/erpnext
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/frappe/mcp
- group: company
  title: ''
  type: Blog
  url: https://frappe.io/rss.xml
created: '2025-02-06'
description: Frappe is a fully featured, low-code web framework written in Python and JavaScript that powers ERPNext, the open-source ERP for accounting, inventory, payroll, and operations. The Frappe REST API auto-exposes every DocType for CRUD plus whitelisted Python method calls.
finops:
- name: Frappe Finops
  service_category: API
  slug: frappe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/frappe.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Frappe
nav: Providers
network: true
overview: 'Frappe publishes 2 APIs on the [APIs.io](https://apis.io/) network: Method API and Resource API. Tagged areas include Open Source, ERP, Accounting, Inventory, and Payroll.


  The Frappe catalog on APIs.io includes 1 Spectral governance ruleset.


  Frappe''s developer surface includes authentication, documentation, engineering blog, and 15 more developer resources.'
plans:
- name: Frappe Plans Pricing
  plan_count: 3
  slug: frappe-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Frappe Rate Limits
  slug: frappe-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Frappe API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: frappe-rest-rules
score:
  band: thin
  composite: 30.0
  delta: -3.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 45.5
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/frappe/refs/heads/main/screenshots/frappe-2026-06-20T181510.png
security:
- kind: authentication
  name: Frappe Authentication
  slug: frappe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Frappe Domain Security
  slug: frappe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Frappe Vulnerability Disclosure
  slug: frappe-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: frappe
tags:
- Open Source
- ERP
- Accounting
- Inventory
- Payroll
- Low Code
website: https://frappe.io/
---
