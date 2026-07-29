---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Truto Agentic Access
  operation_count: 30
  slug: truto-agentic-access
  summary_line: 30 operations · 9 acting
api_count: 18
apis:
- description: Account records representing companies or organizations
  name: Truto Accounts API
  slug: truto-accounts-api
- description: Job applications linking candidates to jobs
  name: Truto Applications API
  slug: truto-applications-api
- description: Candidate profiles and contact information
  name: Truto Candidates API
  slug: truto-candidates-api
- description: Company and organization records
  name: Truto Companies API
  slug: truto-companies-api
- description: Contact records representing individuals at companies
  name: Truto Contacts API
  slug: truto-contacts-api
- description: Organizational departments
  name: Truto Departments API
  slug: truto-departments-api
- description: Employee records and personal details
  name: Truto Employees API
  slug: truto-employees-api
- description: Employment terms, positions, and job history
  name: Truto Employments API
  slug: truto-employments-api
- description: Departments, teams, and organizational units
  name: Truto Groups API
  slug: truto-groups-api
- description: Manage connected third-party accounts
  name: Truto Integrated Accounts API
  slug: truto-integrated-accounts-api
- description: Job postings and open positions
  name: Truto Jobs API
  slug: truto-jobs-api
- description: Generate tokens for customer-initiated account connections
  name: Truto Link Tokens API
  slug: truto-link-tokens-api
- description: Provision Model Context Protocol servers for AI agent access
  name: Truto MCP Servers API
  slug: truto-mcp-servers-api
- description: Job offers extended to candidates
  name: Truto Offers API
  slug: truto-offers-api
- description: Sales opportunities and deals
  name: Truto Opportunities API
  slug: truto-opportunities-api
- description: Opportunity pipeline stages
  name: Truto Stages API
  slug: truto-stages-api
- description: Tasks and follow-up actions
  name: Truto Tasks API
  slug: truto-tasks-api
- description: Time off requests and leave management
  name: Truto Timeoff API
  slug: truto-timeoff-api
artifact_total: 42
collections:
- collection_type: open
  name: Truto Admin API
  slug: open-truto-admin
- collection_type: open
  name: Truto Unified ATS API
  slug: open-truto-unified-ats
- collection_type: open
  name: Truto Unified CRM API
  slug: open-truto-unified-crm
- collection_type: open
  name: Truto Unified HRIS API
  slug: open-truto-unified-hris
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/truto-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/truto-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truto-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gettruto
- group: company
  title: ''
  type: Website
  url: https://truto.one/
- group: docs
  title: ''
  type: Documentation
  url: https://truto.one/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://truto.one/docs/api-reference/overview/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://truto.one/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://truto.one/unified-apis/
- group: company
  title: ''
  type: Blog
  url: https://truto.one/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/trutohq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://truto.one/docs/api-reference/overview/introduction
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/truto/refs/heads/main/rules/truto-rules.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://truto.one/blog/announcing-truto-docs-mcp-stop-ai-hallucinations-in-api-integrations/
- group: agent
  title: ''
  type: AgentSkills
  url: https://truto.one/blog/truto-agent-skills-stop-ai-hallucinations-when-building-integrations/
- group: agent
  title: ''
  type: LlmsText
  url: https://truto.one/llms.txt
created: '2026-03-16'
description: Truto is a unified API and embedded integration platform that enables B2B SaaS companies to ship native integrations without writing integration-specific code. Founded in 2023, Truto uses a declarative, config-driven architecture where every connector is data, not code. The platform provides Unified APIs across four major categories — HRIS (41 providers, 20 resources), ATS (27 providers, 17 resources), CRM (27 providers, 17 resources), and an expanding set of additional categories — plus an Admin API for managing integrated accounts, generating link tokens, and programmatic MCP server provisioning. Truto supports real-time pass-through (no data stored in between), full schema customization via JSONata, and one-API-call MCP server generation for AI agent access. Authentication uses Bearer tokens. Truto supports over 250 integrations and is available as Truto Cloud or on-premise.
examples:
- key_count: 2
  name: Truto Admin Create Link Token Example
  slug: truto-admin-create-link-token-example
- key_count: 2
  name: Truto Admin List Integrated Accounts Example
  slug: truto-admin-list-integrated-accounts-example
- key_count: 2
  name: Truto Unified Crm List Contacts Example
  slug: truto-unified-crm-list-contacts-example
- key_count: 2
  name: Truto Unified Hris List Employees Example
  slug: truto-unified-hris-list-employees-example
finops:
- name: Truto Finops
  service_category: Unified API / Integration Platform
  slug: truto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truto.png
json_schemas:
- name: Candidate
  property_count: 11
  slug: truto-candidate
- name: Employee
  property_count: 19
  slug: truto-employee
- name: IntegratedAccount
  property_count: 8
  slug: truto-integrated-account
json_structures:
- name: Truto Employee Structure
  property_count: 0
  slug: truto-employee-structure
- name: Truto Integrated Account Structure
  property_count: 0
  slug: truto-integrated-account-structure
jsonld:
- class_count: 50
  name: Truto Context
  property_count: 16
  slug: truto-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Truto
nav: Providers
network: true
overview: 'Truto publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Applications API, Candidates API, and 15 more. Tagged areas include Unified API, Integration Platform, HRIS, ATS, and CRM.


  The Truto catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Truto''s developer surface includes authentication, documentation, getting-started guide, engineering blog, GitHub presence, and 12 more developer resources.'
plans:
- name: Truto Plans Pricing
  plan_count: 2
  slug: truto-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Truto Rate Limits
  slug: truto-rate-limits
rules:
- name: Truto API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: truto-jsonschema-spectral-rules
- name: Truto API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 3
    warn: 6
  slug: truto-rules
score:
  band: developing
  composite: 52.9
  delta: -4.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 69.5
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 57.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/truto/refs/heads/main/screenshots/truto-2026-06-20T195809.png
security:
- kind: authentication
  name: Truto Authentication
  slug: truto-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Truto Domain Security
  slug: truto-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Truto Trust Center
  slug: truto-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: truto
tags:
- Unified API
- Integration Platform
- HRIS
- ATS
- CRM
- Embedded Integrations
- MCP
- AI Agents
- SaaS
website: https://truto.one/
---
