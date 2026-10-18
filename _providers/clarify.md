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
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 56
  human_in_the_loop: 6
  name: Clarify Agentic Access
  operation_count: 85
  slug: clarify-agentic-access
  summary_line: 85 operations · 56 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Activities API from Clarify — 1 operation(s) for activities.
  name: Clarify Activities API
  slug: clarify-activities-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Campaigns API from Clarify — 1 operation(s) for campaigns.
  name: Clarify Campaigns API
  slug: clarify-campaigns-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Comments API from Clarify — 2 operation(s) for comments.
  name: Clarify Comments API
  slug: clarify-comments-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Invitations API from Clarify — 3 operation(s) for invitations.
  name: Clarify Invitations API
  slug: clarify-invitations-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Layouts API from Clarify — 2 operation(s) for layouts.
  name: Clarify Layouts API
  slug: clarify-layouts-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The ListRows API from Clarify — 1 operation(s) for listrows.
  name: Clarify List Rows API
  slug: clarify-listrows-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Lists API from Clarify — 5 operation(s) for lists.
  name: Clarify Lists API
  slug: clarify-lists-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The MeetingRecordings API from Clarify — 6 operation(s) for meetingrecordings.
  name: Clarify Meeting Recordings API
  slug: clarify-meetingrecordings-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The ObjectAccess API from Clarify — 2 operation(s) for objectaccess.
  name: Clarify Object Access API
  slug: clarify-objectaccess-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The RecordAccess API from Clarify — 3 operation(s) for recordaccess.
  name: Clarify Record Access API
  slug: clarify-recordaccess-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The RecordAttachments API from Clarify — 2 operation(s) for recordattachments.
  name: Clarify Record Attachments API
  slug: clarify-recordattachments-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The RecordRelationships API from Clarify — 1 operation(s) for recordrelationships.
  name: Clarify Record Relationships API
  slug: clarify-recordrelationships-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Records API from Clarify — 4 operation(s) for records.
  name: Clarify Records API
  slug: clarify-records-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Resources API from Clarify — 4 operation(s) for resources.
  name: Clarify Resources API
  slug: clarify-resources-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Schemas API from Clarify — 9 operation(s) for schemas.
  name: Clarify Schemas API
  slug: clarify-schemas-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Users API from Clarify — 3 operation(s) for users.
  name: Clarify Users API
  slug: clarify-users-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Workflows API from Clarify — 2 operation(s) for workflows.
  name: Clarify Workflows API
  slug: clarify-workflows-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The WorkspaceSettings API from Clarify — 2 operation(s) for workspacesettings.
  name: Clarify Workspace Settings API
  slug: clarify-workspacesettings-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The API Keys API from Clarify — 2 operation(s) for api keys.
  name: Clarify API Keys API
  slug: clarify-api-keys-api
artifact_total: 34
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/well-known/clarify-clarify-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clarify-clarify-security.txt
- group: start
  title: ''
  type: SignUp
  url: https://auth1.clarify.ai/sign-up
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.clarify.ai/docs/getting-started/authentication
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/agentic-access/clarify-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clarify-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/rate-limits/clarify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clarify-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/plans/clarify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clarify-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/rules/clarify-rules.yml
  title: ''
  type: Spectral
  url: rules/clarify-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/json-ld/clarify-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clarify-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/vocabulary/clarify-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clarify-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/data-model/clarify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clarify-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/changelog/clarify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clarify-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/conventions/clarify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clarify-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.clarify.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/authentication/clarify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clarify-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/errors/clarify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clarify-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/conformance/clarify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clarify-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/llms/clarify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clarify-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/well-known/clarify-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clarify-www-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/well-known/clarify-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clarify-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/well-known/clarify-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clarify-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/well-known/clarify-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clarify-docs-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/well-known/clarify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clarify-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/hosts/clarify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clarify-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/vendors/clarify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clarify-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.clarify.ai/integrations/webhook
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clarify.ai
- group: auth
  title: ''
  type: Security
  url: https://www.clarify.ai/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clarifyhq
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.clarify.ai/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/security/clarify-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clarify-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/security/clarify-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clarify-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarify/refs/heads/main/security/clarify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clarify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clarify.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clarify.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clarify.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.clarify.ai/docs/api-reference
- group: operate
  title: ''
  type: Support
  url: https://developer.clarify.ai/docs/resources/support
- group: company
  title: ''
  type: Blog
  url: https://blog.clarify.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://clarify.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clarify.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clarify.ai/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/clarifyhq/workspace
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://clarify.ai/openapi.json
  - status: null
    url: https://www.clarify.ai/openapi.json
  - status: 401
    url: https://api.clarify.ai/mcp
  - status: 200
    url: https://www.clarify.ai
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: partner-login
  state: gated
created: '2026-10-08'
description: Clarify is an AI-native CRM platform that automates sales workflows, integrates with email, calendar, and various tools, and provides a conversational AI assistant to manage contacts, deals, and pipelines. It offers a JSON:API‑compliant API for programmatic access to CRM data, enabling custom integrations, automation, and AI‑driven insights for sales teams.
image: https://cdn.sanity.io/images/aa2wo756/production/0407fea58502918f464731d985ee3dec3a0007cc-1200x630.jpg?w=1200&h=630&auto=format
json_schemas:
- name: CreateRelationshipDto
  property_count: 1
  slug: clarify-create-relationship-dto
- name: ListOfActivitiesResponse
  property_count: 3
  slug: clarify-list-of-activities-response
- name: ListOfWorkflowsResponse
  property_count: 3
  slug: clarify-list-of-workflows-response
- name: UpdateLayoutBodyDto
  property_count: 2
  slug: clarify-update-layout-body-dto
- name: WorkflowResponse
  property_count: 1
  slug: clarify-workflow-response
- name: WorkspaceSettingsDto
  property_count: 46
  slug: clarify-workspace-settings-dto
jsonld:
- class_count: 71
  name: Clarify Context
  property_count: 85
  slug: clarify-context
layout: provider
modified: '2026-10-08'
name: Clarify
nav: Providers
network: true
overview: 'Clarify publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Campaigns API, Comments API, and 16 more. Tagged areas include Company, CRM, Artificial Intelligence, Automation, and Sales.


  The Clarify catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clarify''s developer surface includes signup flow, getting-started guide, changelog, authentication, documentation, API reference, support, and 36 more developer resources.'
plans:
- name: Clarify Plans Pricing
  plan_count: 4
  slug: clarify-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Clarify Rate Limits
  slug: clarify-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Clarify API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: clarify-rules
score:
  band: exemplar
  composite: 72.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 62.6
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 76.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 38.9
security:
- kind: authentication
  name: Clarify Authentication
  slug: clarify-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Clarify Domain Security
  slug: clarify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clarify Vulnerability Disclosure
  slug: clarify-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Clarify Trust Center
  slug: clarify-trust-center
  summary_line: SOC 2, GDPR
slug: clarify
tags:
- Company
- CRM
- Artificial Intelligence
- Automation
- Sales
website: https://www.clarify.ai
---
