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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.0
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 1098
  human_in_the_loop: 0
  name: Pipeliner Agentic Access
  operation_count: 1510
  slug: pipeliner-agentic-access
  summary_line: 1510 operations · 1098 acting
api_count: 1
apis:
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Account API from Pipeliner CRM — 68 operation(s) for account.
  name: Pipeliner CRM Account API
  slug: pipeliner-account-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Activity API from Pipeliner CRM — 79 operation(s) for activity.
  name: Pipeliner CRM Activity API
  slug: pipeliner-activity-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Approval API from Pipeliner CRM — 20 operation(s) for approval.
  name: Pipeliner CRM Approval API
  slug: pipeliner-approval-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Call API from Pipeliner CRM — 5 operation(s) for call.
  name: Pipeliner CRM Call API
  slug: pipeliner-call-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Chat API from Pipeliner CRM — 5 operation(s) for chat.
  name: Pipeliner CRM Chat API
  slug: pipeliner-chat-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Client API from Pipeliner CRM — 22 operation(s) for client.
  name: Pipeliner CRM Client API
  slug: pipeliner-client-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Company Email API from Pipeliner CRM — 2 operation(s) for company email.
  name: Pipeliner CRM Company Email API
  slug: pipeliner-company-email-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Contact API from Pipeliner CRM — 83 operation(s) for contact.
  name: Pipeliner CRM Contact API
  slug: pipeliner-contact-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Country API from Pipeliner CRM — 5 operation(s) for country.
  name: Pipeliner CRM Country API
  slug: pipeliner-country-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Currency API from Pipeliner CRM — 15 operation(s) for currency.
  name: Pipeliner CRM Currency API
  slug: pipeliner-currency-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Custom Entity API from Pipeliner CRM — 17 operation(s) for custom entity.
  name: Pipeliner CRM Custom Entity API
  slug: pipeliner-custom-entity-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Data API from Pipeliner CRM — 5 operation(s) for data.
  name: Pipeliner CRM Data API
  slug: pipeliner-data-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Document API from Pipeliner CRM — 25 operation(s) for document.
  name: Pipeliner CRM Document API
  slug: pipeliner-document-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Email API from Pipeliner CRM — 50 operation(s) for email.
  name: Pipeliner CRM Email API
  slug: pipeliner-email-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Email Sequence API from Pipeliner CRM — 20 operation(s) for email sequence.
  name: Pipeliner CRM Email Sequence API
  slug: pipeliner-email-sequence-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Entities API from Pipeliner CRM — 2 operation(s) for entities.
  name: Pipeliner CRM Entities API
  slug: pipeliner-entities-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Field API from Pipeliner CRM — 15 operation(s) for field.
  name: Pipeliner CRM Field API
  slug: pipeliner-field-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Forecast API from Pipeliner CRM — 5 operation(s) for forecast.
  name: Pipeliner CRM Forecast API
  slug: pipeliner-forecast-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Form API from Pipeliner CRM — 15 operation(s) for form.
  name: Pipeliner CRM Form API
  slug: pipeliner-form-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Import API from Pipeliner CRM — 5 operation(s) for import.
  name: Pipeliner CRM Import API
  slug: pipeliner-import-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Interface API from Pipeliner CRM — 5 operation(s) for interface.
  name: Pipeliner CRM Interface API
  slug: pipeliner-interface-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Lead API from Pipeliner CRM — 5 operation(s) for lead.
  name: Pipeliner CRM Lead API
  slug: pipeliner-lead-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Lead & Opportunity API from Pipeliner CRM — 104 operation(s) for lead & opportunity.
  name: Pipeliner CRM Lead & Opportunity API
  slug: pipeliner-lead-opportunity-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The MasterRight API from Pipeliner CRM — 40 operation(s) for masterright.
  name: Pipeliner CRM Master Right API
  slug: pipeliner-masterright-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Media API from Pipeliner CRM — 5 operation(s) for media.
  name: Pipeliner CRM Media API
  slug: pipeliner-media-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Memo API from Pipeliner CRM — 10 operation(s) for memo.
  name: Pipeliner CRM Memo API
  slug: pipeliner-memo-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Message API from Pipeliner CRM — 15 operation(s) for message.
  name: Pipeliner CRM Message API
  slug: pipeliner-message-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Note API from Pipeliner CRM — 5 operation(s) for note.
  name: Pipeliner CRM Note API
  slug: pipeliner-note-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Online API from Pipeliner CRM — 35 operation(s) for online.
  name: Pipeliner CRM Online API
  slug: pipeliner-online-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Opportunity API from Pipeliner CRM — 10 operation(s) for opportunity.
  name: Pipeliner CRM Opportunity API
  slug: pipeliner-opportunity-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Phone API from Pipeliner CRM — 5 operation(s) for phone.
  name: Pipeliner CRM Phone API
  slug: pipeliner-phone-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Pipeline API from Pipeliner CRM — 5 operation(s) for pipeline.
  name: Pipeliner CRM Pipeline API
  slug: pipeliner-pipeline-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Process API from Pipeliner CRM — 20 operation(s) for process.
  name: Pipeliner CRM Process API
  slug: pipeliner-process-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Product API from Pipeliner CRM — 32 operation(s) for product.
  name: Pipeliner CRM Product API
  slug: pipeliner-product-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Product Line Items API from Pipeliner CRM — 5 operation(s) for product line items.
  name: Pipeliner CRM Product Line Items API
  slug: pipeliner-product-line-items-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Profile API from Pipeliner CRM — 11 operation(s) for profile.
  name: Pipeliner CRM Profile API
  slug: pipeliner-profile-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Project API from Pipeliner CRM — 37 operation(s) for project.
  name: Pipeliner CRM Project API
  slug: pipeliner-project-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Quote API from Pipeliner CRM — 45 operation(s) for quote.
  name: Pipeliner CRM Quote API
  slug: pipeliner-quote-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Report API from Pipeliner CRM — 13 operation(s) for report.
  name: Pipeliner CRM Report API
  slug: pipeliner-report-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The SalesRole API from Pipeliner CRM — 5 operation(s) for salesrole.
  name: Pipeliner CRM Sales Role API
  slug: pipeliner-salesrole-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The SalesUnit API from Pipeliner CRM — 7 operation(s) for salesunit.
  name: Pipeliner CRM Sales Unit API
  slug: pipeliner-salesunit-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Step API from Pipeliner CRM — 15 operation(s) for step.
  name: Pipeliner CRM Step API
  slug: pipeliner-step-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Tag API from Pipeliner CRM — 10 operation(s) for tag.
  name: Pipeliner CRM Tag API
  slug: pipeliner-tag-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Target API from Pipeliner CRM — 10 operation(s) for target.
  name: Pipeliner CRM Target API
  slug: pipeliner-target-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Text API from Pipeliner CRM — 15 operation(s) for text.
  name: Pipeliner CRM Text API
  slug: pipeliner-text-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Timeframe API from Pipeliner CRM — 2 operation(s) for timeframe.
  name: Pipeliner CRM Timeframe API
  slug: pipeliner-timeframe-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Translation API from Pipeliner CRM — 5 operation(s) for translation.
  name: Pipeliner CRM Translation API
  slug: pipeliner-translation-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Type API from Pipeliner CRM — 2 operation(s) for type.
  name: Pipeliner CRM Type API
  slug: pipeliner-type-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Unsubscribed API from Pipeliner CRM — 5 operation(s) for unsubscribed.
  name: Pipeliner CRM Unsubscribed API
  slug: pipeliner-unsubscribed-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Webhook API from Pipeliner CRM — 10 operation(s) for webhook.
  name: Pipeliner CRM Webhook API
  slug: pipeliner-webhook-api
- baseURL: https://us-east.api.pipelinersales.com/api/v100/rest/spaces/{space_id}
  baseurl_source: declared
  description: The Webresource API from Pipeliner CRM — 5 operation(s) for webresource.
  name: Pipeliner CRM Webresource API
  slug: pipeliner-webresource-api
artifact_total: 65
asyncapis:
- description: ''
  name: Pipeliner Webhooks
  slug: pipeliner-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/llms/pipeliner-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pipeliner-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.coevera.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/agentic-access/pipeliner-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pipeliner-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/rules/pipeliner-rules.yml
  title: ''
  type: Spectral
  url: rules/pipeliner-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/json-ld/pipeliner-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pipeliner-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/vocabulary/pipeliner-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pipeliner-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/asyncapi/pipeliner-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pipeliner-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/data-model/pipeliner-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pipeliner-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/conventions/pipeliner-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pipeliner-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.coevera.com/security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/security/pipeliner-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pipeliner-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/security/pipeliner-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/pipeliner-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/security/pipeliner-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pipeliner-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/security/pipeliner-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pipeliner-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/authentication/pipeliner-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pipeliner-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/errors/pipeliner-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pipeliner-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/conformance/pipeliner-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pipeliner-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/well-known/pipeliner-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pipeliner-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/well-known/pipeliner-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pipeliner-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/hosts/pipeliner-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pipeliner-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pipeliner/refs/heads/main/vendors/pipeliner-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pipeliner-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.pipelinersales.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pipelinersales.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.pipelinersales.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.pipelinersales.com/api-docs
- group: operate
  title: ''
  type: Support
  url: https://help.pipelinersales.com
- group: company
  title: ''
  type: Blog
  url: https://www.coevera.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coevera.com/crm/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coevera.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coevera.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://www.coevera.com/sales-crm/sign-up-geolocation/
- group: start
  title: ''
  type: Login
  url: https://www.coevera.com/log-in/
created: '2026-09-22'
description: Pipeliner CRM provides a visual sales pipeline and customer relationship management platform that helps businesses track leads, manage contacts, and automate sales processes. The solution offers customizable pipelines, activity tracking, reporting, and integration capabilities, enabling teams to improve productivity and close deals more efficiently. It serves a range of industries with a focus on sales automation and pipeline visibility, delivering a cloud‑based CRM experience.
json_schemas:
- name: Appointment
  property_count: 57
  slug: pipeliner-appointment
- name: batchMasterRightInput
  property_count: 161
  slug: pipeliner-batch-master-right-input
- name: createMasterRightInput
  property_count: 162
  slug: pipeliner-create-master-right-input
- name: MasterRight
  property_count: 165
  slug: pipeliner-master-right
- name: Opportunity
  property_count: 67
  slug: pipeliner-opportunity
- name: updateMasterRightInput
  property_count: 160
  slug: pipeliner-update-master-right-input
jsonld:
- class_count: 120
  name: Pipeliner Context
  property_count: 255
  slug: pipeliner-context
layout: provider
modified: '2026-09-22'
name: Pipeliner CRM
nav: Providers
network: true
overview: 'Pipeliner CRM publishes 51 APIs on the [APIs.io](https://apis.io/) network, including Account API, Activity API, Approval API, and 48 more. Tagged areas include CRM, Sales, Automation, Pipelines, and Cloud.


  The Pipeliner CRM catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Pipeliner CRM''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 26 more developer resources.'
random_paper: 0
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Pipeliner CRM API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: pipeliner-rules
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 70.0
    developer_ergonomics: 58.9
    discoverability: 69.6
    operational_transparency: 18.4
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 51
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Pipeliner Authentication
  slug: pipeliner-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pipeliner Domain Security
  slug: pipeliner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pipeliner Vulnerability Disclosure
  slug: pipeliner-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Pipeliner Trust Center
  slug: pipeliner-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: pipeliner
tags:
- CRM
- Sales
- Automation
- Pipelines
- Cloud
website: https://www.coevera.com/
---
