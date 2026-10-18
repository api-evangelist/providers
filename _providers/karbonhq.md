---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Karbonhq Agentic Access
  operation_count: 77
  slug: karbonhq-agentic-access
  summary_line: 77 operations · 34 acting
api_count: 2
apis:
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: List and view an Invoice and associated line items
  name: Karbon Billing API
  slug: karbonhq-billing-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: View or update the Business Card attached to a Contact and/or Organization
  name: Karbon Business Cards API
  slug: karbonhq-business-cards-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Create a client group to manage related contacts, create work for them, and see all related jobs in a single view. [Read more](https://help.karbonhq.com/en/articles/5880261-manage-a-client-group)
  name: Karbon Client Groups API
  slug: karbonhq-client-groups-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Use comments on tasks to add notes or bring a colleague into the conversation to collaborate on the task. [Read more](https://help.karbonhq.com/en/articles/2111192-comment-and-collaborate-on-a-task)
  name: Karbon Comments API
  slug: karbonhq-comments-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Manage your contacts and get the full overview over clients, whether they are individuals or organizations. [Read more](https://help.karbonhq.com/en/articles/5708609-overview-of-contacts)
  name: Karbon Contacts API
  slug: karbonhq-contacts-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Endpoints to manage Custom Fields on Contacts and Organizations in Karbon, refer to the Karbon help and support content for more information on [creating custom fields](https://help.karbonhq.com/en/ar
  name: Karbon Custom Fields API
  slug: karbonhq-custom-fields-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Estimate and track time to understand jobs that are on-budget, allocate resources, and uncover performance insights to transform your firm. [Read more](https://help.karbonhq.com/en/articles/4439115-ov
  name: Karbon Estimate Summaries API
  slug: karbonhq-estimate-summaries-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Handle files and attachments. [Read more](https://help.karbonhq.com/en/articles/5714089-files-and-attachments)
  name: Karbon Files API
  slug: karbonhq-files-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Endpoints that enable Karbon Integration Partners to manage integrated workflow tasks enabled for their integrations. Note that these endpoints cannot be used to access Tasks or Client Tasks. Access i
  name: Karbon Integrated Workflows API
  slug: karbonhq-integrated-workflows-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Hold a conversation internally within your company. Unlike an email, Notes are viewed only by members of your team. [Read more](https://help.karbonhq.com/en/s/articles/5919746-use-notes)
  name: Karbon Notes API
  slug: karbonhq-notes-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Create an organization to represent marriages and couples and client groups to represent families. [Read more](https://help.karbonhq.com/en/articles/5708609-overview-of-contacts#h_8ee87bfcc1)
  name: Karbon Organizations API
  slug: karbonhq-organizations-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Retrieve lists of valid Contact Types, Work Types and Work Statuses
  name: Karbon Tenant Settings API
  slug: karbonhq-tenant-settings-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Retrieve individual (non-aggregated) time entries, each record represents a single time entry for a specific day, user, and work item. [Read more](https://help.karbonhq.com/en/s/articles/6022358-manag
  name: Karbon Timesheets and Time Entries API
  slug: karbonhq-timesheets-and-time-entries-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Create and view the basics & defaults for colleagues, teams and job roles to customize Karbon to represent the way you and your team work. [Read more](https://help.karbonhq.com/en/articles/3731216-edi
  name: Karbon Users API
  slug: karbonhq-users-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Details of the different payloads sent for Karbon Webhook subscriptions
  name: Karbon Webhook Payloads API
  slug: karbonhq-webhook-payloads-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: 'Integrate your system with Karbon to receive changes made to your data in Karbon. Note: Webhook payloads take the following form: ```JSON { "ResourcePermaKey": "{EntityKey}", "ResourceType": "{EntityT'
  name: Karbon Webhook Subscriptions API
  slug: karbonhq-webhook-subscriptions-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Manage a Work Item to best fit your workflow, including timelines, tasks and work teams. [Read more](https://help.karbonhq.com/en/articles/6057036-managing-work-items-and-teams)
  name: Karbon Work Items API
  slug: karbonhq-work-items-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Set a Work Item to repeat on a defined schedule. [Read more](https://help.karbonhq.com/en/articles/6096234-setup-repeating-work-on-a-schedule)
  name: Karbon Work Schedules API
  slug: karbonhq-work-schedules-api
- baseURL: https://api.karbonhq.com
  baseurl_source: declared
  description: Find and review templates that you created to fit your firm's unique workflows. [Read more](https://help.karbonhq.com/en/articles/5325202-create-and-customize-work-templates)
  name: Karbon Work Templates API
  slug: karbonhq-work-templates-api
artifact_total: 36
asyncapis:
- description: ''
  name: Karbonhq Webhooks
  slug: karbonhq-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/capabilities/karbonhq-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/karbonhq-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/agentic-access/karbonhq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/karbonhq-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/rate-limits/karbonhq-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/karbonhq-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/plans/karbonhq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/karbonhq-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/rules/karbonhq-rules.yml
  title: ''
  type: Spectral
  url: rules/karbonhq-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/rules/karbonhq-karbon-api-reference-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/karbonhq-karbon-api-reference-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/json-ld/karbonhq-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/karbonhq-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/vocabulary/karbonhq-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/karbonhq-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/asyncapi/karbonhq-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/karbonhq-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/data-model/karbonhq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/karbonhq-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/changelog/karbonhq-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/karbonhq-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/conventions/karbonhq-conventions.yml
  title: ''
  type: Conventions
  url: conventions/karbonhq-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/lifecycle/karbonhq-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/karbonhq-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/lifecycle/karbonhq-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/karbonhq-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/errors/karbonhq-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/karbonhq-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/conformance/karbonhq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/karbonhq-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/overlays/karbonhq-karbon-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/karbonhq-karbon-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/llms/karbonhq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/karbonhq-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/well-known/karbonhq-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/karbonhq-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/well-known/karbonhq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/karbonhq-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/hosts/karbonhq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/karbonhq-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/vendors/karbonhq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/karbonhq-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/authentication/karbonhq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/karbonhq-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/security/karbonhq-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/karbonhq-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/security/karbonhq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/karbonhq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://karbonhq.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/karbonhq/karbon-api-reference/blob/57cc9814d7cc6bc697895d0bfe52b0c422684d3c/vacuum-rules.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.karbonhq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://karbonhq.github.io/karbon-api-reference/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.karbonhq.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.karbonhq.com/guides/authentication/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.karbonhq.com/release-notes/2026-09-23/
- group: operate
  title: ''
  type: Support
  url: https://help.karbonhq.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.karbonhq.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/karbonhq
- group: commercial
  title: ''
  type: Pricing
  url: https://karbonhq.com/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://karbonhq.com/get-started
- group: start
  title: ''
  type: Login
  url: https://app2.karbonhq.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://karbonhq.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://karbonhq.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://karbonhq.com/security/
- group: other
  title: ''
  type: Leadership
  url: https://karbonhq.com/leadership/
- group: company
  title: ''
  type: About
  url: https://karbonhq.com/about/
created: '2026-10-09'
description: Karbon is accounting practice management software for accounting firms, built to enhance visibility, efficiency, and connectivity for a firm no matter where its people are located. Through the Karbon Developer Center (developers.karbonhq.com) it publishes a public REST API reference plus guides covering authentication, pagination, rate limits, webhooks, work items, clients, custom fields, budgets and time, invoices and payments, and file uploads.
image: https://karbonhq.com/images/og-default-image.jpg
json_schemas:
- name: BusinessCardRequest
  property_count: 14
  slug: karbonhq-business-card-request
- name: BusinessCard
  property_count: 14
  slug: karbonhq-business-card
- name: GetWorkSchedule
  property_count: 26
  slug: karbonhq-get-work-schedule
- name: ResponseCreateClientGroup
  property_count: 13
  slug: karbonhq-response-create-client-group
- name: ResponseCreateContact
  property_count: 21
  slug: karbonhq-response-create-contact
- name: WorkScheduleRequest
  property_count: 19
  slug: karbonhq-work-schedule-request
jsonld:
- class_count: 88
  name: Karbonhq Context
  property_count: 272
  slug: karbonhq-context
layout: provider
mcp_servers:
- description: Karbon's official hosted MCP server. It lets AI agents connect to a user's Karbon account. Karbon's own llms.txt files announce it at https://mcp.karbonhq.com ("Karbon's MCP server, for AI agents to c
  name: Karbon MCP Server
  slug: karbonhq
modified: '2026-10-09'
name: Karbon
nav: Providers
network: true
overview: 'Karbon publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Business Cards API, Client Groups API, and 16 more. Tagged areas include Company, Accounting, Practice Management, Workflows, and Collaboration.


  The Karbon catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Karbon''s developer surface includes changelog, authentication, API reference, documentation, support, pricing, getting-started guide, and 37 more developer resources.'
plans:
- name: Karbonhq Plans Pricing
  plan_count: 3
  slug: karbonhq-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Karbonhq Rate Limits
  slug: karbonhq-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Karbon — karbon api reference rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: karbonhq-karbon-api-reference-spectral-rules
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Karbon API Rules
  rule_count: 18
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 4
  slug: karbonhq-rules
score:
  band: exemplar
  composite: 71.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 75.5
    developer_ergonomics: 56.5
    discoverability: 76.7
    operational_transparency: 84.2
  previous_composite: 74.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/karbonhq/refs/heads/main/screenshots/karbonhq-2026-10-11T110101.png
security:
- kind: authentication
  name: Karbonhq Authentication
  slug: karbonhq-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Karbonhq Domain Security
  slug: karbonhq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Karbonhq Vulnerability Disclosure
  slug: karbonhq-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: karbonhq
tags:
- Company
- Accounting
- Practice Management
- Workflows
- Collaboration
- Professional Services
- Software-as-a-Service
website: https://karbonhq.com/
---
