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
agentic_access:
- acting_count: 93
  human_in_the_loop: 0
  name: Department Of State Agentic Access
  operation_count: 158
  slug: department-of-state-agentic-access
  summary_line: 158 operations · 93 acting
api_count: 4
apis:
- baseURL: https://www.state.gov/wp-json
  baseurl_source: declared
  description: The Department of State runs www.state.gov on WordPress and exposes the WordPress REST API anonymously at https://www.state.gov/wp-json. Alongside the core WordPress resources the Department registers
  name: state.gov Content API
  slug: state-gov-content-api
- description: A RESTful, OPDS Catalog 1.1 feed of the Foreign Relations of the United States series — the official documentary record of major U.S. foreign policy decisions — published by the Office of the Historia
  name: Office of the Historian Ebook Catalog API
  slug: historian-ebook-catalog-api
- description: The Department's Project Open Data catalog, served as a single machine-readable DCAT-US 3.0 document at https://www.state.gov/data.json. 397 dataset entries covering Foreign Relations metadata, Humani
  name: Department of State Open Data Catalog
  slug: open-data-catalog
- description: Country-by-country travel advisories (Levels 1-4) issued by the Bureau of Consular Affairs, with RSS distribution.
  name: State Department Travel Advisories
  slug: travel-advisories
- description: Per-country pages covering entry/exit requirements, local laws, safety, health, and U.S. embassy contacts.
  name: Country Information Pages
  slug: country-information
- description: Voluntary enrollment system for U.S. citizens traveling or residing abroad to receive embassy alerts.
  name: Smart Traveler Enrollment Program (STEP)
  slug: smart-traveler-enrollment-program
- description: Reference information on nonimmigrant and immigrant visa categories, processing times, and reciprocity schedules.
  name: U.S. Visa Information
  slug: visa-information
- description: Public-facing passport application, renewal, and status-check resources from the Bureau of Consular Affairs.
  name: U.S. Passport Services
  slug: passport-services
- description: Department-wide policy and procedural manuals issued by the Office of Directives Management.
  name: Foreign Affairs Manual (FAM) and Handbook (FAH)
  slug: foreign-affairs-manual
- description: Government-internal name-check system used during visa and passport adjudication. Referenced here for completeness; no public API.
  name: ConsularLookout (CLASS)
  slug: consular-lookout-class
- description: State Department-wide enterprise case-management platform. Internal system; referenced here for organizational completeness.
  name: eCASE Enterprise Case Management
  slug: ecase
- description: Public datasets published by the State Department through the federal open-data catalog.
  name: State Department Open Data on data.gov
  slug: state-data-gov
artifact_total: 32
common:
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/USStateDept
- group: company
  title: ''
  type: Blog
  url: https://www.state.gov/blogs
- group: other
  title: ''
  type: X
  url: https://x.com/StateDept
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/department-of-state-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/department-of-state-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.state.gov/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-state-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usstatedept
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/statedept
- group: start
  title: ''
  type: Portal
  url: https://www.state.gov/
- group: start
  title: ''
  type: Portal
  url: https://travel.state.gov/
- group: docs
  title: ''
  type: Reference
  url: https://fam.state.gov/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/department-of-state-state-gov-content-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/department-of-state-state-gov-content-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/department-of-state-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/department-of-state-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/department-of-state-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/department-of-state-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/department-of-state-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/department-of-state-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/department-of-state-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/department-of-state-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/department-of-state-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/department-of-state-plans-pricing.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/department-of-state-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.state.gov/bureau-of-diplomatic-technology/vulnerability-disclosure-policy
- group: docs
  title: ''
  type: Documentation
  url: https://history.state.gov/developer/catalog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://history.state.gov/developer
- group: docs
  title: ''
  type: APIReference
  url: https://www.state.gov/wp-json/
- group: operate
  title: ''
  type: Support
  url: https://www.state.gov/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.state.gov/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.state.gov/copyright-information
- group: other
  title: ''
  type: OpenData
  url: https://www.state.gov/data.json
created: '2024-12-03'
description: 'The U.S. Department of State leads U.S. foreign policy, conducts diplomacy with foreign governments, issues U.S. passports and visas, supports U.S. citizens abroad, and publishes country-specific information and travel advisories. It operates no unified developer portal and issues no API keys, but it does serve several real, anonymous, machine-readable surfaces: the state.gov Content API at https://www.state.gov/wp-json, where 473 WordPress REST routes expose press releases, briefings, reports, biographies, bureaus and country and policy content as structured JSON with no credential; the Office of the Historian Ebook Catalog API, an OPDS Catalog 1.1 feed of the Foreign Relations of the United States series and the only surface the Department documents on a developer page of its own; a DCAT-US 3.0 open data catalog of 397 datasets at https://www.state.gov/data.json; and the Travel Advisories RSS feed. Discovery is the weak point rather than supply — none of the nine State hosts
  probed serves any /.well-known/ document, three of the four State APIs listed in the federal inventory have been retired without notice, and travel.state.gov and the Bureau of Consular Affairs data catalog refuse non-browser clients outright.'
finops:
- name: Department Of State Finops
  service_category: API
  slug: department-of-state-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/department-of-state.png
json_schemas:
- name: state_biography
  property_count: 28
  slug: department-of-state-state-biography
- name: state_briefing
  property_count: 28
  slug: department-of-state-state-briefing
- name: state_bureau
  property_count: 29
  slug: department-of-state-state-bureau
- name: state_country
  property_count: 27
  slug: department-of-state-state-country
- name: state_ext_content
  property_count: 27
  slug: department-of-state-state-ext-content
- name: state_people
  property_count: 26
  slug: department-of-state-state-people
- name: state_policy_issue
  property_count: 31
  slug: department-of-state-state-policy-issue
- name: state_press_release
  property_count: 30
  slug: department-of-state-state-press-release
- name: state_report
  property_count: 31
  slug: department-of-state-state-report
- name: state_trip_travel
  property_count: 27
  slug: department-of-state-state-trip-travel
jsonld:
- class_count: 0
  name: State Context
  property_count: 5
  slug: state-context
layout: provider
mcp_servers:
- description: ''
  name: Department of State MCP Server
  slug: department-of-state-mcp-server
modified: '2026-09-07'
name: Department of State
nav: Providers
network: true
overview: 'Department of State publishes 1 API on the [APIs.io](https://apis.io/) network: state.gov Content API. Tagged areas include Federal-Government, Foreign Affairs, Travel, Consular, and Visas.


  The Department of State catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Department of State''s developer surface includes engineering blog, authentication, developer portal, documentation, API reference, support, and 29 more developer resources.'
plans:
- name: Department Of State Plans Pricing
  plan_count: 0
  slug: department-of-state-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Department Of State Rate Limits
  slug: department-of-state-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Department of State API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: state-rules
security:
- kind: authentication
  name: Department Of State Authentication
  slug: department-of-state-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Department Of State Domain Security
  slug: department-of-state-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Department Of State Vulnerability Disclosure
  slug: department-of-state-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: department-of-state
tags:
- Federal-Government
- Foreign Affairs
- Travel
- Consular
- Visas
- Passports
website: https://www.state.gov/
---
