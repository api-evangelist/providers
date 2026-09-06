---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Telstra Agentic Access
  operation_count: 13
  slug: telstra-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 2
apis:
- baseURL: https://tapi.telstra.com/v2
  baseurl_source: declared
  description: OAuth 2.0 client credentials token issuance.
  name: Telstra Authentication API
  slug: telstra-authentication-api
- baseURL: https://tapi.telstra.com/v2
  baseurl_source: declared
  description: Service health checks for SMS and MMS messaging surfaces.
  name: Telstra HealthCheck API
  slug: telstra-healthcheck-api
- baseURL: https://tapi.telstra.com/v2
  baseurl_source: declared
  description: Send, retrieve, and check status of MMS messages.
  name: Telstra MMS API
  slug: telstra-mms-api
- baseURL: https://tapi.telstra.com/v2
  baseurl_source: declared
  description: Create, retrieve, and delete dedicated number subscriptions.
  name: Telstra Provisioning API
  slug: telstra-provisioning-api
- baseURL: https://tapi.telstra.com/v2
  baseurl_source: declared
  description: Send, retrieve, and check status of SMS messages.
  name: Telstra SMS API
  slug: telstra-sms-api
- baseURL: https://tapi.telstra.com/v2
  baseurl_source: declared
  description: Mobile number verification operations.
  name: Telstra Verification API
  slug: telstra-verification-api
artifact_total: 51
collections:
- collection_type: postman
  name: Telstra Messaging Authentication API
  slug: postman-telstra-authentication-api
- collection_type: postman
  name: Telstra Messaging Authentication HealthCheck API
  slug: postman-telstra-healthcheck-api
- collection_type: postman
  name: Telstra Messaging Authentication MMS API
  slug: postman-telstra-mms-api
- collection_type: postman
  name: Telstra Messaging Authentication Provisioning API
  slug: postman-telstra-provisioning-api
- collection_type: postman
  name: Telstra Messaging Authentication SMS API
  slug: postman-telstra-sms-api
- collection_type: postman
  name: Telstra Messaging Authentication Verification API
  slug: postman-telstra-verification-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Telstra Messaging Authentication API
  slug: open-telstra-authentication-api
- collection_type: open
  name: Telstra Messaging Authentication HealthCheck API
  slug: open-telstra-healthcheck-api
- collection_type: open
  name: Telstra Messaging API
  slug: open-telstra-messaging-api
- collection_type: open
  name: Telstra Messaging Authentication MMS API
  slug: open-telstra-mms-api
- collection_type: open
  name: Telstra Mobile Number Verification API
  slug: open-telstra-mobile-number-verification-api
- collection_type: open
  name: Telstra Messaging Authentication Provisioning API
  slug: open-telstra-provisioning-api
- collection_type: open
  name: Telstra Messaging Authentication SMS API
  slug: open-telstra-sms-api
- collection_type: open
  name: Telstra Messaging Authentication Verification API
  slug: open-telstra-verification-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/telstra/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telstra-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telstra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telstra-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/telstra-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://dev.telstra.com
- group: start
  title: ''
  type: Portal
  url: https://www.telstra.com.au
- group: docs
  title: ''
  type: Documentation
  url: https://dev.telstra.com
- group: start
  title: ''
  type: Signup
  url: https://dev.telstra.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/telstra
- group: operate
  title: ''
  type: StatusPage
  url: https://crowdsupport.telstra.com.au/t5/network-coverage/ct-p/Networkcoverage
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telstra.com.au/business-enterprise/legal/messaging-api-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telstra.com.au/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telstra
- group: company
  title: ''
  type: Blog
  url: https://exchange.telstra.com.au
- group: operate
  title: ''
  type: Support
  url: https://www.telstra.com.au/support
- group: operate
  title: ''
  type: Forums
  url: https://crowdsupport.telstra.com.au
- group: build
  title: ''
  type: GitHub
  url: https://github.com/telstra
- group: build
  title: ''
  type: SDKs
  url: https://github.com/telstra/MessagingAPI-SDK-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/telstra/MessagingAPI-SDK-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/telstra/MessagingAPI-SDK-Java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/telstra/MessagingAPI-SDK-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/telstra/MessagingAPI-SDK-Go
- group: commercial
  title: ''
  type: License
  url: https://github.com/telstra/tdev-doc-license
- group: build
  title: ''
  type: Tools
  url: https://github.com/telstra/Cat-1-Development-Kit
- group: build
  title: ''
  type: Tools
  url: https://github.com/telstra/Cat-M1-Dev-Board
- group: commercial
  title: ''
  type: Plans
  url: plans/telstra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/telstra-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/telstra-finops.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/telstra-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/telstra-vocabulary.yml
created: '2026-05-25T00:00:00.000Z'
description: Telstra is Australia's largest telecommunications and mobile network operator, providing fixed broadband, mobile voice and data, enterprise networking, and IoT connectivity across Australia and into Asia. Telstra exposes a developer programme at dev.telstra.com fronting carrier-grade Messaging (SMS / MMS) and Mobile Number Verification APIs, with official SDKs in Python, Node.js, Java, .NET, and Go, and Arduino libraries for the Telstra Cat-1 and Cat-M1 IoT development kits. APIs are reached at tapi.telstra.com behind OAuth 2.0 client credentials with the NSMS or MNV scopes.
examples:
- key_count: 2
  name: Telstra Create Subscription Example
  slug: telstra-create-subscription-example
- key_count: 2
  name: Telstra Oauth Token Example
  slug: telstra-oauth-token-example
- key_count: 2
  name: Telstra Send Sms Example
  slug: telstra-send-sms-example
features:
- SMS messaging (single, multi-recipient) over the Telstra mobile network
- MMS messaging with multipart payloads (image, audio, video, SMIL, vCard)
- Inbound replies on Telstra-provisioned dedicated virtual numbers
- Delivery status notifications via push callbacks (notifyURL) and pull status endpoint
- Scheduled delivery and validity-period controls
- Priority message flag and per-message user reference
- OAuth 2.0 client credentials grant with NSMS scope (3599 second bearer tokens)
- Free Trial tier with Telstra-supplied trial numbers and whitelisted recipients
- Commercial Paid tier with negotiated per-message pricing and SLA
- International SMS reach beyond Australia
- Official SDKs in Python, Node.js, Java, .NET, and Go
- Service healthchecks for SMS and MMS surfaces
- Mobile Number Verification — silent MSISDN match on the Telstra data network (separate API)
- Arduino development kits for Cat-1 and Cat-M1 IoT modules on the Telstra network
finops:
- name: Telstra Finops
  service_category: ''
  slug: telstra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telstra.png
json_schemas:
- name: Telstra Message
  property_count: 15
  slug: telstra-message
- name: Telstra Subscription
  property_count: 5
  slug: telstra-subscription
json_structures:
- name: Telstra Message Structure
  property_count: 0
  slug: telstra-message-structure
jsonld:
- class_count: 0
  name: Telstra Context
  property_count: 5
  slug: telstra-context
layout: provider
modified: '2026-05-25'
name: Telstra
nav: Providers
network: true
overview: 'Telstra publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, HealthCheck API, MMS API, and 3 more. Tagged areas include Telecommunications, Telco, Mobile, Messaging, and SMS.


  The Telstra catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Telstra''s developer surface includes authentication, developer portal, documentation, signup flow, engineering blog, support, GitHub presence, and 24 more developer resources.'
plans:
- name: Telstra Plans Pricing
  plan_count: 2
  slug: telstra-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Telstra Rate Limits
  slug: telstra-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Telstra API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: telstra-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Telstra API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: telstra-rules
scopes:
- name: Telstra Scopes
  scope_count: 2
  slug: telstra-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 84.5
    catalog_earned_first_party: 0.0
    catalog_gap: 30.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 28.8
    contract_quality: 71.0
    developer_ergonomics: 46.4
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 52.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telstra/refs/heads/main/screenshots/telstra-2026-06-20T195052.png
security:
- kind: authentication
  name: Telstra Authentication
  slug: telstra-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Telstra Domain Security
  slug: telstra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telstra
tags:
- Telecommunications
- Telco
- Mobile
- Messaging
- SMS
- MMS
- Networks
- Australia
- Verification
website: https://dev.telstra.com
---
