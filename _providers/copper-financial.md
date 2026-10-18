---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Copper Financial Agentic Access
  operation_count: 27
  slug: copper-financial-agentic-access
  summary_line: 27 operations
api_count: 1
apis:
- baseURL: https://api.copper.com/developer_api/v1
  baseurl_source: declared
  description: Account and user information operations
  name: Copper Financial Account API
  slug: copper-financial-account-api
- baseURL: https://api.copper.com/developer_api/v1
  baseurl_source: declared
  description: Activity tracking operations
  name: Copper Financial Activities API
  slug: copper-financial-activities-api
- baseURL: https://api.copper.com/developer_api/v1
  baseurl_source: declared
  description: Company management operations
  name: Copper Financial Companies API
  slug: copper-financial-companies-api
- baseURL: https://api.copper.com/developer_api/v1
  baseurl_source: declared
  description: Custom field definitions and operations
  name: Copper Financial Custom Fields API
  slug: copper-financial-custom-fields-api
- baseURL: https://api.copper.com/developer_api/v1
  baseurl_source: declared
  description: Field layout configuration for entity types
  name: Copper Financial Field Layouts API
  slug: copper-financial-field-layouts-api
- baseURL: https://api.copper.com/developer_api/v1
  baseurl_source: declared
  description: Lead management operations
  name: Copper Financial Leads API
  slug: copper-financial-leads-api
- baseURL: https://api.copper.com/developer_api/v1
  baseurl_source: declared
  description: Sales opportunity operations
  name: Copper Financial Opportunities API
  slug: copper-financial-opportunities-api
- baseURL: https://api.copper.com/developer_api/v1
  baseurl_source: declared
  description: People/contact management operations
  name: Copper Financial People API
  slug: copper-financial-people-api
- baseURL: https://api.copper.com/developer_api/v1
  baseurl_source: declared
  description: Related items and relationship operations
  name: Copper Financial Related Items API
  slug: copper-financial-related-items-api
- baseURL: https://api.copper.com/developer_api/v1
  baseurl_source: declared
  description: Tag management operations
  name: Copper Financial Tags API
  slug: copper-financial-tags-api
- baseURL: https://api.copper.com/developer_api/v1
  baseurl_source: declared
  description: Task management operations
  name: Copper Financial Tasks API
  slug: copper-financial-tasks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Copper Financial Webhooks
  slug: copper-financial-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/agentic-access/copper-financial-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/copper-financial-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/plans/copper-financial-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/copper-financial-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/rules/copper-financial-rules.yml
  title: ''
  type: Spectral
  url: rules/copper-financial-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/json-ld/copper-financial-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/copper-financial-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/vocabulary/copper-financial-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/copper-financial-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/asyncapi/copper-financial-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/copper-financial-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/data-model/copper-financial-data-model.yml
  title: ''
  type: DataModel
  url: data-model/copper-financial-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/changelog/copper-financial-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/copper-financial-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/conventions/copper-financial-conventions.yml
  title: ''
  type: Conventions
  url: conventions/copper-financial-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.copper.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/authentication/copper-financial-authentication.yml
  title: ''
  type: Authentication
  url: authentication/copper-financial-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/errors/copper-financial-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/copper-financial-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/conformance/copper-financial-conformance.yml
  title: ''
  type: Conformance
  url: conformance/copper-financial-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/llms/copper-financial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/copper-financial-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/well-known/copper-financial-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/copper-financial-support-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/well-known/copper-financial-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/copper-financial-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/well-known/copper-financial-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/copper-financial-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/hosts/copper-financial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/copper-financial-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/vendors/copper-financial-vendors.yml
  title: ''
  type: Vendors
  url: vendors/copper-financial-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.copper.com/
- group: auth
  title: ''
  type: Security
  url: https://www.copper.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.copper.com/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/security/copper-financial-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/copper-financial-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copper-financial/refs/heads/main/security/copper-financial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/copper-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.copper.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.copper.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.copper.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.copper.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.copper.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.copper.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.copper.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.copper.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.copper.com/introduction/oauth/quickstart.html
- group: start
  title: ''
  type: SignUp
  url: https://www.copper.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.copper.com/users/sign_in
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://developer.copper.com/v1/openapi.json
  - status: 401
    url: https://api.copper.com/mcp
  - status: 401
    url: https://app.copper.com/mcp
  - status: 403
    url: https://developer.copper.com/mcp
  - status: 403
    url: https://support.copper.com/mcp
  - status: 200
    url: https://www.copper.com/
  reason: partner-login
  state: gated
created: '2026-10-10'
description: Copper Financial provides a CRM platform for service‑based businesses, offering tools to organize contacts, track deals, manage projects, automate workflows, and generate custom reports. The solution integrates with popular apps such as Google Workspace and supports mobile access, aiming to streamline sales and customer relationship processes for agencies, consulting firms, and other service industries.
json_schemas:
- name: Activity
  property_count: 10
  slug: copper-financial-activity
- name: Company
  property_count: 16
  slug: copper-financial-company
- name: Lead
  property_count: 25
  slug: copper-financial-lead
- name: Opportunity
  property_count: 23
  slug: copper-financial-opportunity
- name: Person
  property_count: 26
  slug: copper-financial-person
- name: Task
  property_count: 15
  slug: copper-financial-task
jsonld:
- class_count: 15
  name: Copper Financial Context
  property_count: 77
  slug: copper-financial-context
layout: provider
modified: '2026-10-10'
name: Copper Financial
nav: Providers
network: true
overview: 'Copper Financial publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Activities API, Companies API, and 8 more. Tagged areas include Company, CRM, Software-as-a-Service, Sales, and Marketing.


  The Copper Financial catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Copper Financial''s developer surface includes changelog, authentication, documentation, API reference, pricing, support, engineering blog, and 29 more developer resources.'
plans:
- name: Copper Financial Plans Pricing
  plan_count: 3
  slug: copper-financial-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Copper Financial API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: copper-financial-rules
score:
  band: strong
  composite: 64.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 73.6
    developer_ergonomics: 49.4
    discoverability: 71.4
    operational_transparency: 50.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Copper Financial Authentication
  slug: copper-financial-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Copper Financial Domain Security
  slug: copper-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Copper Financial Trust Center
  slug: copper-financial-trust-center
  summary_line: GDPR
slug: copper-financial
tags:
- Company
- CRM
- Software-as-a-Service
- Sales
- Marketing
website: https://www.copper.com/
---
