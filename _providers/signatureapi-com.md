---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Signatureapi Com Agentic Access
  operation_count: 23
  slug: signatureapi-com-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.signatureapi.com/v1
  baseurl_source: declared
  description: A **deliverable** is the final signed PDF generated after an envelope completes. It contains the signed documents and an audit trail.
  name: signatureapi-com Deliverables API
  slug: signatureapi-com-deliverables-api
- baseURL: https://api.signatureapi.com/v1
  baseurl_source: declared
  description: An **envelope** holds documents and recipients, and manages the signing process from start to finish. Create an envelope to send documents for signature.
  name: signatureapi-com Envelopes API
  slug: signatureapi-com-envelopes-api
- baseURL: https://api.signatureapi.com/v1
  baseurl_source: declared
  description: An **event** records a change or action in your account. Events are delivered via webhooks and available through the API.
  name: signatureapi-com Events API
  slug: signatureapi-com-events-api
- baseURL: https://api.signatureapi.com/v1
  baseurl_source: declared
  description: A **recipient** is a person who receives an envelope. Recipients can be signers, approvers, or preparers.
  name: signatureapi-com Recipients API
  slug: signatureapi-com-recipients-api
- baseURL: https://api.signatureapi.com/v1
  baseurl_source: declared
  description: The Senders API from signatureapi-com — 2 operation(s) for senders.
  name: signatureapi-com Senders API
  slug: signatureapi-com-senders-api
- baseURL: https://api.signatureapi.com/v1
  baseurl_source: declared
  description: An **upload** is a file stored in SignatureAPI for use as a document source in envelopes. Supports PDF, DOCX, and image files.
  name: signatureapi-com Uploads API
  slug: signatureapi-com-uploads-api
- baseURL: https://api.signatureapi.com/v1
  baseurl_source: declared
  description: The Webhooks API from signatureapi-com — 0 operation(s) for webhooks.
  name: signatureapi-com Webhooks API
  slug: signatureapi-com-webhooks-api
artifact_total: 26
asyncapis:
- description: ''
  name: Signatureapi Com Webhooks
  slug: signatureapi-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/signatureapi-com/agentic-access/signatureapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/signatureapi-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/signatureapi-com/rate-limits/signatureapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/signatureapi-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/signatureapi-com/plans/signatureapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/signatureapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/signatureapi-com/rules/signatureapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/signatureapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/signatureapi-com/json-ld/signatureapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/signatureapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/signatureapi-com/vocabulary/signatureapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/signatureapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/signatureapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/signatureapi-com/asyncapi/signatureapi-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/signatureapi-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/signatureapi-com/data-model/signatureapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/signatureapi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/signatureapi-com/conventions/signatureapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/signatureapi-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/signatureapi-com/authentication/signatureapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/signatureapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/signatureapi-com/errors/signatureapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/signatureapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/signatureapi-com/conformance/signatureapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/signatureapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/signatureapi-com/llms/signatureapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/signatureapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/signatureapi-com/well-known/signatureapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/signatureapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/signatureapi-com/hosts/signatureapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/signatureapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/signatureapi-com/vendors/signatureapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/signatureapi-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/signatureapi-com/packages/signatureapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/signatureapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/signatureapi-com/packages/signatureapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/signatureapi-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://signatureapi.com/terms
- group: operate
  title: ''
  type: Support
  url: https://signatureapi.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://signatureapi.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://signatureapi.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://signatureapi.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://signatureapi.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://signatureapi.com/docs/api/guides/overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://signatureapi.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://signatureapi.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://signatureapi.com/docs/api/guides/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.signatureapi.com</code
- group: docs
  title: ''
  type: APIReference
  url: https://signatureapi.com/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/signatureapi-com/security/signatureapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/signatureapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://signatureapi.com/
created: '2026-10-31'
description: SignatureAPI provides a modern electronic signature API that enables developers to integrate e‑signatures into applications and workflows at scale. The platform offers API endpoints for document creation, template management, envelope handling, and compliance features such as HIPAA, SOC2, GDPR, and CCPA. It includes AI Toolkit integrations, low‑cost pricing, and extensive documentation, making it suitable for businesses seeking automated signing solutions.
image: https://signatureapi.com/og-image.jpg
json_schemas:
- name: Envelope
  property_count: 15
  slug: signatureapi-com-envelope-envelope-input
- name: Envelope
  property_count: 22
  slug: signatureapi-com-envelope-envelope
- name: Envelope Event
  property_count: 0
  slug: signatureapi-com-event-envelope-context-event
- name: Event
  property_count: 0
  slug: signatureapi-com-event-event
- name: Event.RecipientEvent
  property_count: 0
  slug: signatureapi-com-event-recipient-event
- name: Recipient
  property_count: 0
  slug: signatureapi-com-recipient-recipient
jsonld:
- class_count: 116
  name: Signatureapi Com Context
  property_count: 107
  slug: signatureapi-com-context
layout: provider
modified: '2026-10-31'
name: signatureapi-com
nav: Providers
network: true
overview: 'signatureapi-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Deliverables API, Envelopes API, Events API, and 4 more. Tagged areas include Company, E-Signature, Software-as-a-Service, Compliance, and Automation.


  The signatureapi-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  signatureapi-com''s developer surface includes authentication, support, pricing, documentation, changelog, engineering blog, getting-started guide, and 26 more developer resources.'
plans:
- name: Signatureapi Com Plans Pricing
  plan_count: 3
  slug: signatureapi-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Signatureapi Com Rate Limits
  slug: signatureapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: signatureapi-com API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: signatureapi-com-rules
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 74.5
    developer_ergonomics: 43.5
    discoverability: 67.0
    operational_transparency: 44.7
  previous_composite: 64.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/signatureapi-com/signatureapi-com-2026-11-03T143158.png
security:
- kind: authentication
  name: Signatureapi Com Authentication
  slug: signatureapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Signatureapi Com Domain Security
  slug: signatureapi-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: signatureapi-com-create-and-retrieve-deliverable
  slug: signatureapi-com-create-and-retrieve-deliverable
- name: signatureapi-com-envelope-workflow
  slug: signatureapi-com-envelope-workflow
- name: signatureapi-com-resend-recipient-request
  slug: signatureapi-com-resend-recipient-request
- name: signatureapi-com-send-sender-lifecycle
  slug: signatureapi-com-send-sender-lifecycle
- name: signatureapi-com-upload-file
  slug: signatureapi-com-upload-file
slug: signatureapi-com
tags:
- Company
- E-Signature
- Software-as-a-Service
- Compliance
- Automation
website: https://signatureapi.com/
---
