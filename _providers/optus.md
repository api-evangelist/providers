---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Optus Agentic Access
  operation_count: 15
  slug: optus-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 4
apis:
- description: Hosted two-factor authentication API that creates an SMS one-time-code challenge for a mobile handset with POST /challenges and validates the user's entry with POST /responses, with customisable messa
  name: Optus SMS Suite 2FA REST API
  slug: optus-sms-suite-2fa-rest-api
- description: Companion REST API to the SMS gateway for scheduling and sending plain-text transactional email over a separate endpoint, returning a 64-bit message ID for later retrieval and firing DLR callbacks whe
  name: Optus SMS Suite REST Email API
  slug: optus-sms-suite-rest-email-api
- description: Legacy GET-based HTTPS interface for SMS integration, covering message sending, delivery receipts, and inbound (mobile-originated) message callbacks for systems that cannot build a JSON REST client. N
  name: Optus SMS Suite HTTPS API
  slug: optus-sms-suite-https-api
- description: WSDL-described SOAP interface for SMS integration supporting custom source addressing, message classification, and structured error handling, published for legacy enterprise middleware. The WSDL is se
  name: Optus SMS Suite SOAP API
  slug: optus-sms-suite-soap-api
- description: Implementation of the 3GPP MM7 SOAP protocol for sending and receiving MMS, carrying text, image, audio, video, and SMIL content in multipart MIME requests to /mm7, with MO message and delivery-report
  name: Optus SMS Suite MMS MM7 API
  slug: optus-sms-suite-mms-mm7-api
- description: Direct SMSC connectivity over SMPP 3.3 and 3.4 with mandatory TLS, offering high-throughput binary messaging, custom character encoding, and detailed delivery reporting. A wire protocol rather than an
  name: Optus SMS Suite SMPP API
  slug: optus-sms-suite-smpp-api
- baseURL: https://api.sms.optus.com.au/rest/campaign_manager/v1
  baseurl_source: declared
  description: The Delete Multiple Lists API from Optus — 1 operation(s) for delete multiple lists.
  name: Optus Delete Multiple Lists API
  slug: optus-delete-multiple-lists-api
- baseURL: https://api.sms.optus.com.au/rest/sms/v2
  baseurl_source: declared
  description: The documentation API from Optus — 1 operation(s) for documentation.
  name: Optus Documentation API
  slug: optus-documentation-api
- baseURL: https://api.sms.optus.com.au/rest/campaign_manager/v1
  baseurl_source: declared
  description: The Lists API from Optus — 2 operation(s) for lists.
  name: Optus Lists API
  slug: optus-lists-api
- baseURL: https://api.sms.optus.com.au/rest/gateway
  baseurl_source: declared
  description: The Messages API from Optus — 3 operation(s) for messages.
  name: Optus Messages API
  slug: optus-messages-api
- baseURL: https://api.sms.optus.com.au/rest/campaign_manager/v1
  baseurl_source: declared
  description: The Report API from Optus — 1 operation(s) for report.
  name: Optus Report API
  slug: optus-report-api
- baseURL: https://api.sms.optus.com.au/rest/campaign_manager/v1
  baseurl_source: declared
  description: The Scheduled Campaigns API from Optus — 1 operation(s) for scheduled campaigns.
  name: Optus Scheduled Campaigns API
  slug: optus-scheduled-campaigns-api
- baseURL: https://api.sms.optus.com.au/rest/services/v1
  baseurl_source: declared
  description: The Services API from Optus — 1 operation(s) for services.
  name: Optus Services API
  slug: optus-services-api
- baseURL: https://api.sms.optus.com.au/rest/services/v1
  baseurl_source: declared
  description: The Status API from Optus — 1 operation(s) for status.
  name: Optus Status API
  slug: optus-status-api
- baseURL: https://api.sms.optus.com.au/rest/campaign_manager/v1
  baseurl_source: declared
  description: The Templates API from Optus — 1 operation(s) for templates.
  name: Optus Templates API
  slug: optus-templates-api
- baseURL: https://api.sms.optus.com.au/rest/2fa
  baseurl_source: declared
  description: The Healthz API from Optus — 1 operation(s) for healthz.
  name: Optus Healthz API
  slug: optus-healthz-api
artifact_total: 47
asyncapis:
- description: Derived event description for the callbacks The Optus SMS Suite POSTs to subscriber-hosted URLs. Optus publishes NO AsyncAPI document; this file was derived by API Evangelist from two sources that are
  name: The Optus SMS Suite Callback Surface
  slug: optus-sms-suite-asyncapi
collections:
- collection_type: open
  name: Campaign Manager
  slug: open-optus-sms-suite-campaign-manager
- collection_type: open
  name: The Optus SMS Suite REST API
  slug: open-optus-sms-suite-rest-v1
- collection_type: open
  name: SMS Gateway REST APIv2
  slug: open-optus-sms-suite-rest-v2
- collection_type: open
  name: Omni Status API
  slug: open-optus-sms-suite-status
common:
- group: operate
  href: https://artifacts.apis.io/optus/rate-limits/optus-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/optus-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/optus/plans/optus-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/optus-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/optus/rules/optus-rules.yml
  title: ''
  type: Spectral
  url: rules/optus-rules.yml
- group: design
  href: https://artifacts.apis.io/optus/json-ld/optus-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/optus-context.jsonld
- group: design
  href: https://artifacts.apis.io/optus/vocabulary/optus-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/optus-vocabulary.yml
- group: start
  href: https://artifacts.apis.io/optus/sandbox/optus-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/optus-sandbox.yml
- group: design
  href: https://artifacts.apis.io/optus/errors/optus-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/optus-problem-types.yml
- group: other
  href: https://artifacts.apis.io/optus/overlays/optus-delete-multiple-lists-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optus-delete-multiple-lists-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optus/hosts/optus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/optus-hosts.yml
- group: build
  href: https://artifacts.apis.io/optus/integrations/optus-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/optus-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/optus/vendors/optus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/optus-vendors.yml
- group: other
  href: https://artifacts.apis.io/optus/capabilities/optus-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/optus-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/optus/skills/optus-send-and-reconcile-sms.md
  title: ''
  type: AgentSkill
  url: skills/optus-send-and-reconcile-sms.md
- group: agent
  href: https://artifacts.apis.io/optus/skills/optus-run-sms-campaign.md
  title: ''
  type: AgentSkill
  url: skills/optus-run-sms-campaign.md
- group: agent
  href: https://artifacts.apis.io/optus/skills/optus-check-service-health.md
  title: ''
  type: AgentSkill
  url: skills/optus-check-service-health.md
- group: company
  title: ''
  type: Website
  url: https://www.optus.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sms.optus.com.au/docs/en/developer-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://sms.optus.com.au/docs/en/developer-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://sms.optus.com.au/docs/en/integrations/messaging-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://sms.optus.com.au/docs/en/developer-getting-started/
- group: start
  title: ''
  type: SignUp
  url: https://sms.optus.com.au/customer/online_signup
- group: start
  title: ''
  type: Login
  url: https://sms.optus.com.au/login
- group: operate
  title: ''
  type: Support
  url: https://www.optus.com.au/business/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://sms.optus.com.au/docs/en/support-centre/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optus.com.au/about/legal/standard-forms-agreement/business
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optus.com.au/about/legal/privacy
- group: auth
  href: https://artifacts.apis.io/optus/authentication/optus-authentication.yml
  title: ''
  type: Authentication
  url: authentication/optus-authentication.yml
- group: design
  href: https://artifacts.apis.io/optus/conventions/optus-conventions.yml
  title: ''
  type: Conventions
  url: conventions/optus-conventions.yml
- group: design
  href: https://artifacts.apis.io/optus/errors/optus-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/optus-error-codes.yml
- group: design
  href: https://artifacts.apis.io/optus/lifecycle/optus-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/optus-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sms.optus.com.au/
- group: operate
  href: https://artifacts.apis.io/optus/lifecycle/optus-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/optus-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/optus/changelog/optus-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/optus-changelog.yml
- group: design
  href: https://artifacts.apis.io/optus/conformance/optus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/optus-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://sms.optus.com.au/docs/en/solution-sheets/safe-secure/
- group: auth
  href: https://artifacts.apis.io/optus/security/optus-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/optus-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/optus-vdp-pro
- group: auth
  href: https://artifacts.apis.io/optus/security/optus-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/optus-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/optus/security/optus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/optus-domain-security.yml
- group: docs
  href: https://artifacts.apis.io/optus/asyncapi/optus-sms-suite-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/optus-sms-suite-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/optus/asyncapi/optus-sms-suite-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/optus-sms-suite-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/optus/data-model/optus-data-model.yml
  title: ''
  type: DataModel
  url: data-model/optus-data-model.yml
- group: agent
  href: https://artifacts.apis.io/optus/mcp/optus-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/optus-mcp.yml
- group: agent
  href: https://artifacts.apis.io/optus/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/optus/agentic-access/optus-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/optus-agentic-access.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/optus
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Optus
created: '2026-07-25'
description: 'Optus (Singtel Optus Pty Limited) is Australia''s second-largest telecommunications carrier, wholly owned by Singapore''s Singtel and headquartered in Macquarie Park, Sydney. It runs a national mobile network reaching over 99% of the Australian population, alongside NBN and cable broadband, satellite capacity inherited from AUSSAT, enterprise and government connectivity, IoT/M2M services, and consumer media. Its API posture is split in two. The only genuinely public, self-serve developer surface Optus operates is The Optus SMS Suite — an enterprise messaging platform white-labelled from New Zealand''s Modica Group at sms.optus.com.au, which publishes open documentation, downloadable OpenAPI/Swagger definitions, a WSDL, delivery-receipt callbacks, and a free-trial signup. Everything else is partner-gated: the IoT Control Centre is a Cisco/Jasper platform behind a referral-coded starter kit, and Optus has no first-party network-API portal — developer.optus.com.au and api.optus.com.au
  resolve on Akamai but return HTTP 403 Access Denied. On network APIs Optus is a stated GSMA Open Gateway participant and an endorser of the Bridge Alliance API Exchange (BAEx), but as of this review no CAMARA API is callable from Optus directly; its route to developers runs through its parent Singtel''s Paragon-powered BAEx and Aduna, not through anything Optus publishes itself.'
finops:
- has_sources: true
  method: derived
  name: Optus Finops
  primary_unit: ''
  service_category: ''
  slug: optus-finops
  template: true
image: https://www.optus.com.au/content/dam/optus/cloud/images/shop/mobile/og-image/og-optus.version-1727925929257.png
json_schemas:
- name: BroadcastRestResponse
  property_count: 0
  slug: optus-broadcast-rest-response
- name: CampaignReport
  property_count: 0
  slug: optus-campaign-report
- name: DeleteMultipleListsRequest
  property_count: 1
  slug: optus-delete-multiple-lists-request
- name: ListCreateResponse
  property_count: 2
  slug: optus-list-create-response
- name: ListGetResponse
  property_count: 0
  slug: optus-list-get-response
- name: ListRequest
  property_count: 6
  slug: optus-list-request
- name: MessageBroadcast
  property_count: 0
  slug: optus-message-broadcast
- name: Message
  property_count: 0
  slug: optus-message
- name: RestResponse
  property_count: 0
  slug: optus-rest-response
- name: ScheduleCampaignRequest
  property_count: 12
  slug: optus-schedule-campaign-request
- name: ScheduleCampaignResponse
  property_count: 2
  slug: optus-schedule-campaign-response
- name: TemplateGetResponse
  property_count: 0
  slug: optus-template-get-response
jsonld:
- class_count: 12
  name: Optus Context
  property_count: 34
  slug: optus-context
layout: provider
modified: '2026-10-21'
name: Optus
nav: Providers
network: true
overview: 'Optus publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Delete Multiple Lists API, Documentation API, Lists API, and 13 more. Tagged areas include Telecommunications, Australia, Mobile Network Operator, Messaging, and SMS.


  The Optus catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Optus'' developer surface includes sandbox, documentation, API reference, getting-started guide, signup flow, support, authentication, and 40 more developer resources.'
plans:
- name: Optus Plans Pricing
  plan_count: 2
  slug: optus-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Optus Rate Limits
  slug: optus-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Optus API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: optus-rules
score:
  band: exemplar
  composite: 67.3
  coverage:
    artifact_dirs: 34
    catalog_earned: 76.8
    catalog_earned_first_party: 16.0
    catalog_gap: 38.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 35.6
    contract_quality: 65.9
    developer_ergonomics: 63.7
    discoverability: 62.5
    operational_transparency: 78.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 67.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 40.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/optus/optus-2026-08-07T190818.png
security:
- kind: authentication
  name: Optus Authentication
  slug: optus-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Optus Domain Security
  slug: optus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Optus Vulnerability Disclosure
  slug: optus-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Optus Trust Center
  slug: optus-trust-center
  summary_line: ISO 27001, SOC 2, IRAP
skill_count: 4
skills:
- name: optus-check-service-health
  slug: optus-check-service-health
- name: optus-run-sms-campaign
  slug: optus-run-sms-campaign
- name: optus-send-and-reconcile-sms
  slug: optus-send-and-reconcile-sms
- name: optus-two-factor-authentication
  slug: optus-two-factor-authentication
slug: optus
tags:
- Telecommunications
- Australia
- Mobile Network Operator
- Messaging
- SMS
- MMS
- Two-Factor Authentication
- Network APIs
- CAMARA
- Open Gateway
- IoT
- 5G
- Broadband
- Satellite
- Enterprise
website: https://www.optus.com.au/
---
