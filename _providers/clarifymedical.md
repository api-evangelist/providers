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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 58
  human_in_the_loop: 6
  name: Clarifymedical Agentic Access
  operation_count: 91
  slug: clarifymedical-agentic-access
  summary_line: 91 operations · 58 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Activities API from Clarifymedical — 1 operation(s) for activities.
  name: Clarifymedical Activities API
  slug: clarifymedical-activities-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Auth API from Clarifymedical — 1 operation(s) for auth.
  name: Clarifymedical Auth API
  slug: clarifymedical-auth-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Campaigns API from Clarifymedical — 1 operation(s) for campaigns.
  name: Clarifymedical Campaigns API
  slug: clarifymedical-campaigns-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Comments API from Clarifymedical — 2 operation(s) for comments.
  name: Clarifymedical Comments API
  slug: clarifymedical-comments-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Invitations API from Clarifymedical — 3 operation(s) for invitations.
  name: Clarifymedical Invitations API
  slug: clarifymedical-invitations-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Layouts API from Clarifymedical — 2 operation(s) for layouts.
  name: Clarifymedical Layouts API
  slug: clarifymedical-layouts-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The ListRows API from Clarifymedical — 1 operation(s) for listrows.
  name: Clarifymedical List Rows API
  slug: clarifymedical-listrows-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Lists API from Clarifymedical — 5 operation(s) for lists.
  name: Clarifymedical Lists API
  slug: clarifymedical-lists-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The MeetingRecordings API from Clarifymedical — 6 operation(s) for meetingrecordings.
  name: Clarifymedical Meeting Recordings API
  slug: clarifymedical-meetingrecordings-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The ObjectAccess API from Clarifymedical — 2 operation(s) for objectaccess.
  name: Clarifymedical Object Access API
  slug: clarifymedical-objectaccess-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The RecordAccess API from Clarifymedical — 3 operation(s) for recordaccess.
  name: Clarifymedical Record Access API
  slug: clarifymedical-recordaccess-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The RecordAttachments API from Clarifymedical — 2 operation(s) for recordattachments.
  name: Clarifymedical Record Attachments API
  slug: clarifymedical-recordattachments-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The RecordRelationships API from Clarifymedical — 1 operation(s) for recordrelationships.
  name: Clarifymedical Record Relationships API
  slug: clarifymedical-recordrelationships-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Records API from Clarifymedical — 4 operation(s) for records.
  name: Clarifymedical Records API
  slug: clarifymedical-records-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Resources API from Clarifymedical — 4 operation(s) for resources.
  name: Clarifymedical Resources API
  slug: clarifymedical-resources-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Schemas API from Clarifymedical — 9 operation(s) for schemas.
  name: Clarifymedical Schemas API
  slug: clarifymedical-schemas-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Users API from Clarifymedical — 4 operation(s) for users.
  name: Clarifymedical Users API
  slug: clarifymedical-users-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Workflows API from Clarifymedical — 2 operation(s) for workflows.
  name: Clarifymedical Workflows API
  slug: clarifymedical-workflows-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The Workspaces API from Clarifymedical — 2 operation(s) for workspaces.
  name: Clarifymedical Workspaces API
  slug: clarifymedical-workspaces-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The WorkspaceSettings API from Clarifymedical — 2 operation(s) for workspacesettings.
  name: Clarifymedical Workspace Settings API
  slug: clarifymedical-workspacesettings-api
- baseURL: https://api.clarify.ai/v1
  baseurl_source: declared
  description: The API Keys API from Clarifymedical — 2 operation(s) for api keys.
  name: Clarifymedical API Keys API
  slug: clarifymedical-api-keys-api
artifact_total: 35
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/agentic-access/clarifymedical-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clarifymedical-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/plans/clarifymedical-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clarifymedical-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/rules/clarifymedical-rules.yml
  title: ''
  type: Spectral
  url: rules/clarifymedical-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/json-ld/clarifymedical-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clarifymedical-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/vocabulary/clarifymedical-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clarifymedical-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/data-model/clarifymedical-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clarifymedical-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/changelog/clarifymedical-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clarifymedical-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.clarify.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/authentication/clarifymedical-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clarifymedical-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/errors/clarifymedical-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clarifymedical-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/conformance/clarifymedical-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clarifymedical-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/llms/clarifymedical-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clarifymedical-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/well-known/clarifymedical-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clarifymedical-www-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/well-known/clarifymedical-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clarifymedical-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/well-known/clarifymedical-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clarifymedical-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/well-known/clarifymedical-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clarifymedical-docs-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/well-known/clarifymedical-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clarifymedical-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/hosts/clarifymedical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clarifymedical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/vendors/clarifymedical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clarifymedical-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.clarify.ai/integrations/webhook
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clarify.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://www.clarify.ai/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clarify.ai
- group: start
  title: ''
  type: SignUp
  url: https://auth1.clarify.ai/sign-up
- group: auth
  title: ''
  type: Security
  url: https://www.clarify.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clarify.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clarify.ai/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clarifyhq
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.clarify.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.clarify.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.clarify.ai/docs/getting-started/authentication
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clarify.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://www.clarify.ai/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/security/clarifymedical-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clarifymedical-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/security/clarifymedical-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clarifymedical-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarifymedical/refs/heads/main/security/clarifymedical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clarifymedical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clarify.ai
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://clarify.ai/openapi.json
  - status: 401
    url: https://api.clarify.ai/mcp
  - status: 200
    url: https://clarify.ai
  reason: partner-login
  state: gated
created: '2026-10-08'
description: Clarifymedical is a healthcare data analytics company that provides APIs for patient activation, growth intelligence, and health system orchestration. It offers services such as Meridian and Arrival to help health systems understand and improve care delivery, leveraging comprehensive health economics data. The company focuses on integrating patient data, provider contracts, and network analytics to drive better health outcomes and operational efficiency.
image: https://cdn.sanity.io/images/aa2wo756/production/0407fea58502918f464731d985ee3dec3a0007cc-1200x630.jpg?w=1200&h=630&auto=format
json_schemas:
- name: CreateRelationshipDto
  property_count: 1
  slug: clarifymedical-create-relationship-dto
- name: ListOfActivitiesResponse
  property_count: 3
  slug: clarifymedical-list-of-activities-response
- name: ListOfWorkflowsResponse
  property_count: 3
  slug: clarifymedical-list-of-workflows-response
- name: UpdateLayoutBodyDto
  property_count: 2
  slug: clarifymedical-update-layout-body-dto
- name: WorkflowResponse
  property_count: 1
  slug: clarifymedical-workflow-response
- name: WorkspaceSettingsDto
  property_count: 46
  slug: clarifymedical-workspace-settings-dto
jsonld:
- class_count: 77
  name: Clarifymedical Context
  property_count: 88
  slug: clarifymedical-context
layout: provider
modified: '2026-10-08'
name: Clarifymedical
nav: Providers
network: true
overview: 'Clarifymedical publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Auth API, Campaigns API, and 18 more. Tagged areas include Company, Healthcare, Data Analytics, and Health Tech.


  The Clarifymedical catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clarifymedical''s developer surface includes changelog, authentication, support, signup flow, pricing, engineering blog, getting-started guide, and 31 more developer resources.'
plans:
- name: Clarifymedical Plans Pricing
  plan_count: 4
  slug: clarifymedical-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Clarifymedical API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: clarifymedical-rules
score:
  band: strong
  composite: 65.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 62.7
    developer_ergonomics: 49.4
    discoverability: 64.3
    operational_transparency: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 38.9
security:
- kind: authentication
  name: Clarifymedical Authentication
  slug: clarifymedical-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Clarifymedical Domain Security
  slug: clarifymedical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clarifymedical Vulnerability Disclosure
  slug: clarifymedical-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Clarifymedical Trust Center
  slug: clarifymedical-trust-center
  summary_line: SOC 2, GDPR
slug: clarifymedical
tags:
- Company
- Healthcare
- Data Analytics
- Health Tech
website: https://clarify.ai
---
