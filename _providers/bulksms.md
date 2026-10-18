---
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Bulksms Agentic Access
  operation_count: 15
  slug: bulksms-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.bulksms.com/v1
  baseurl_source: declared
  description: Operations related to SMS attachments
  name: BulkSMS Attachments API
  slug: bulksms-attachments-api
- baseURL: https://api.bulksms.com/v1
  baseurl_source: declared
  description: Blocked number management operations
  name: BulkSMS Blocked Numbers API
  slug: bulksms-blocked-numbers-api
- baseURL: https://api.bulksms.com/v1
  baseurl_source: declared
  description: Credit management operations
  name: BulkSMS Credits API
  slug: bulksms-credits-api
- baseURL: https://api.bulksms.com/v1
  baseurl_source: declared
  description: A message record represents an SMS that has been sent or received. To send messages, create a `SubmissionEntry` and submit it to the Send Messages Operation. You can retrieve sent and received message
  name: BulkSMS Message API
  slug: bulksms-message-api
- baseURL: https://api.bulksms.com/v1
  baseurl_source: declared
  description: Operations related to the profile of the user
  name: BulkSMS Profile API
  slug: bulksms-profile-api
- baseURL: https://api.bulksms.com/v1
  baseurl_source: declared
  description: 'Manage webhooks that notify your server when messages are sent or received. For full details on implementing your webhook — including event types, request headers, payload structure, retry logic, and '
  name: BulkSMS Webhooks API
  slug: bulksms-webhooks-api
artifact_total: 18
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/agentic-access/bulksms-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bulksms-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/rules/bulksms-rules.yml
  title: ''
  type: Spectral
  url: rules/bulksms-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/json-ld/bulksms-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bulksms-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/vocabulary/bulksms-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bulksms-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/data-model/bulksms-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bulksms-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/conventions/bulksms-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bulksms-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/conventions/bulksms-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bulksms-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/errors/bulksms-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bulksms-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/conformance/bulksms-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bulksms-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/llms/bulksms-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bulksms-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/hosts/bulksms-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bulksms-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/vendors/bulksms-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bulksms-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/packages/bulksms-packages.yml
  title: ''
  type: SDKs
  url: packages/bulksms-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/packages/bulksms-packages.yml
  title: ''
  type: Packages
  url: packages/bulksms-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bulksms.com/company/terms-and-conditions.htm
- group: company
  title: ''
  type: Newsroom
  url: https://www.bulksms.com/resources/news/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bulksms.com/developer/eapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BulkSMS
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/authentication/bulksms-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bulksms-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bulksms/refs/heads/main/security/bulksms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bulksms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bulksms.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bulksms.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bulksms.com/developer/
- group: docs
  title: ''
  type: APIReference
  url: https://www.bulksms.com/developer/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bulksms.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.bulksms.com/support/
- group: start
  title: ''
  type: SignUp
  url: https://www1.bulksms.com/register/
- group: start
  title: ''
  type: Login
  url: https://www.bulksms.com/account/
created: '2026-10-13'
description: BulkSMS provides a business SMS platform enabling companies to send, receive and manage text messages globally. With over 25 years in business messaging, they support 180+ countries, 800+ local networks, and offer features like web-to-SMS, shortcodes, long numbers, RCS messaging, and integrations via REST, legacy EAPI, and SMPP. Their API allows developers to automate notifications, alerts, and marketing campaigns, backed by robust pricing, compliance, and support resources.
image: https://www.bulksms.com/images/share/bulksms-social-share-2026.jpg
json_schemas:
- name: Message
  property_count: 14
  slug: bulksms-message
- name: PreSignInfo
  property_count: 3
  slug: bulksms-pre-sign-info
- name: Profile
  property_count: 8
  slug: bulksms-profile
- name: SubmissionEntry
  property_count: 10
  slug: bulksms-submission-entry
- name: TransferEntry
  property_count: 5
  slug: bulksms-transfer-entry
- name: WebhookEntry
  property_count: 7
  slug: bulksms-webhook-entry
jsonld:
- class_count: 11
  name: Bulksms Context
  property_count: 45
  slug: bulksms-context
layout: provider
modified: '2026-10-13'
name: BulkSMS
nav: Providers
network: true
overview: 'BulkSMS publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attachments API, Blocked Numbers API, Credits API, and 3 more. Tagged areas include SMS, Messaging, Communications, Business, and BulkSMS.


  The BulkSMS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BulkSMS''s developer surface includes getting-started guide, authentication, documentation, API reference, pricing, support, signup flow, and 22 more developer resources.'
plans:
- name: Bulksms Plans Pricing
  plan_count: 0
  slug: bulksms-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: BulkSMS API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: bulksms-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 63.0
    developer_ergonomics: 63.7
    discoverability: 75.0
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 17.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Bulksms Authentication
  slug: bulksms-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bulksms Domain Security
  slug: bulksms-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bulksms
tags:
- SMS
- Messaging
- Communications
- Business
- BulkSMS
website: https://www.bulksms.com
---
