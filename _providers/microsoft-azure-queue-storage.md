---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Azure Queue Storage Agentic Access
  operation_count: 7
  slug: microsoft-azure-queue-storage-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- baseURL: https://{account}.queue.core.windows.net/
  baseurl_source: declared
  description: Queues operations
  name: Azure Queue Storage Queues API
  slug: microsoft-azure-queue-storage-queues-api
- baseURL: https://{account}.queue.core.windows.net/
  baseurl_source: declared
  description: The message API from Azure Queue Storage — 2 operation(s) for message.
  name: Azure Queue Storage Message API
  slug: microsoft-azure-queue-storage-message-api
- baseURL: https://{account}.queue.core.windows.net/
  baseurl_source: declared
  description: The messageId API from Azure Queue Storage — 1 operation(s) for messageid.
  name: Azure Queue Storage Message ID API
  slug: microsoft-azure-queue-storage-messageid-api
- baseURL: https://{account}.queue.core.windows.net/
  baseurl_source: declared
  description: The queue API from Azure Queue Storage — 3 operation(s) for queue.
  name: Azure Queue Storage Queue API
  slug: microsoft-azure-queue-storage-queue-api
- baseURL: https://{account}.queue.core.windows.net/
  baseurl_source: declared
  description: The service API from Azure Queue Storage — 5 operation(s) for service.
  name: Azure Queue Storage Service API
  slug: microsoft-azure-queue-storage-service-api
artifact_total: 25
collections:
- collection_type: open
  name: Azure Queue Storage REST Queues API
  slug: open-microsoft-azure-queue-storage-queues-api
- collection_type: open
  name: Azure Queue Storage REST API
  slug: open-microsoft-azure-queue-storage
common:
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/analyticsonazure
- group: design
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/rules/microsoft-azure-queue-storage-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-queue-storage-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/json-ld/microsoft-azure-queue-storage-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-queue-storage-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/vocabulary/microsoft-azure-queue-storage-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-queue-storage-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/data-model/microsoft-azure-queue-storage-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-queue-storage-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/cli/microsoft-azure-queue-storage-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-queue-storage-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/conventions/microsoft-azure-queue-storage-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-queue-storage-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/rest/api/storageservices/previous-azure-storage-service-versions
- group: design
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/lifecycle/microsoft-azure-queue-storage-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-queue-storage-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/errors/microsoft-azure-queue-storage-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-queue-storage-error-codes.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/errors/microsoft-azure-queue-storage-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-queue-storage-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/conformance/microsoft-azure-queue-storage-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-queue-storage-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/llms/microsoft-azure-queue-storage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-queue-storage-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/well-known/microsoft-azure-queue-storage-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-queue-storage-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/well-known/microsoft-azure-queue-storage-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-queue-storage-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/hosts/microsoft-azure-queue-storage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-queue-storage-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/vendors/microsoft-azure-queue-storage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-queue-storage-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/packages/microsoft-azure-queue-storage-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-queue-storage-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/security/microsoft-azure-queue-storage-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-queue-storage-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/security/microsoft-azure-queue-storage-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-queue-storage-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/plans/microsoft-azure-queue-storage-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-queue-storage-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/rate-limits/microsoft-azure-queue-storage-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-queue-storage-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/finops/microsoft-azure-queue-storage-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-queue-storage-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/agentic-access/microsoft-azure-queue-storage-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-queue-storage-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/security/microsoft-azure-queue-storage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-queue-storage-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-queue-storage/authentication/microsoft-azure-queue-storage-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-queue-storage-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/storage/queues/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/storage/queues/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/storage/queues/storage-quickstart-queues-portal
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
created: '2026-03-13'
description: Azure Queue Storage is a Microsoft cloud service for storing large numbers of messages, enabling decoupled and asynchronous communication between application components. Messages can be accessed via authenticated HTTP/HTTPS calls and support visibility timeouts, peeking, and metadata for reliable processing.
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Queue Storage Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-queue-storage-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-queue-storage.png
json_schemas:
- name: DequeuedMessagesList
  property_count: 0
  slug: microsoft-azure-queue-storage-dequeued-messages-list
- name: KeyInfo
  property_count: 3
  slug: microsoft-azure-queue-storage-key-info
- name: ListQueuesSegmentResponse
  property_count: 6
  slug: microsoft-azure-queue-storage-list-queues-segment-response
- name: PeekedMessagesList
  property_count: 0
  slug: microsoft-azure-queue-storage-peeked-messages-list
- name: StorageServiceProperties
  property_count: 4
  slug: microsoft-azure-queue-storage-storage-service-properties
- name: UserDelegationKey
  property_count: 8
  slug: microsoft-azure-queue-storage-user-delegation-key
jsonld:
- class_count: 18
  name: Microsoft Azure Queue Storage Context
  property_count: 46
  slug: microsoft-azure-queue-storage-context
layout: provider
modified: '2026-05-19'
name: Azure Queue Storage
nav: Providers
network: true
overview: 'Azure Queue Storage publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Queues API, Message API, Message ID API, and 2 more. Tagged areas include Asynchronous Processing, Cloud Storage, Messaging, Queues, and Storage.


  The Azure Queue Storage catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azure Queue Storage''s developer surface includes engineering blog, CLI, changelog, authentication, developer portal, pricing, documentation, and 35 more developer resources.'
plans:
- name: Microsoft Azure Queue Storage Plans Pricing
  plan_count: 0
  slug: microsoft-azure-queue-storage-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 2
  name: Microsoft Azure Queue Storage Rate Limits
  slug: microsoft-azure-queue-storage-rate-limits
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Azure Queue Storage API Rules
  rule_count: 40
  severity_counts:
    error: 35
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-azure-queue-storage-rules
score:
  band: strong
  composite: 58.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.5
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 56.0
    developer_ergonomics: 63.7
    discoverability: 75.0
    operational_transparency: 73.7
  previous_composite: 42.8
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-azure-queue-storage/microsoft-azure-queue-storage-2026-06-20T185432.png
security:
- kind: authentication
  name: Microsoft Azure Queue Storage Authentication
  slug: microsoft-azure-queue-storage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Microsoft Azure Queue Storage Domain Security
  slug: microsoft-azure-queue-storage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Queue Storage Vulnerability Disclosure
  slug: microsoft-azure-queue-storage-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Queue Storage Trust Center
  slug: microsoft-azure-queue-storage-trust-center
  summary_line: GDPR
skill_count: 2
skills:
- name: manage-queues
  slug: microsoft-azure-queue-storage-manage-queues
- name: send-and-process-messages
  slug: microsoft-azure-queue-storage-send-and-process-messages
slug: microsoft-azure-queue-storage
tags:
- Asynchronous Processing
- Cloud Storage
- Messaging
- Queues
- Storage
website: https://www.microsoft.com/
---
