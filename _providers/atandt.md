---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Atandt Agentic Access
  operation_count: 15
  slug: atandt-agentic-access
  summary_line: 15 operations · 11 acting
api_count: 6
apis:
- baseURL: https://api.att.com
  baseurl_source: declared
  description: Developer APIs for AT&T's wireless network capabilities including SMS messaging, MMS messaging, OAuth authentication, speech-to-text, text-to-speech, in-app messaging, and advertising APIs for consume
  name: AT&T Wireless APIs
  slug: att-wireless-apis
- description: CAMARA-standard 5G network APIs available through the AT&T Developer Hub and Network API Accelerator Program. Includes SIM Swap detection, Device Status, Number Verification, Quality on Demand, Networ
  name: AT&T 5G Network APIs
  slug: att-network-apis
- description: Enterprise-grade APIs for AT&T wireline business services including service qualification, quoting, ordering, and provisioning. The Alliance API suite supports automated ordering of AVPN, IPBB, ATTPho
  name: AT&T Enterprise Connectivity APIs
  slug: att-enterprise-connectivity-apis
- description: TM Forum-aligned APIs for mobile virtual network operators (MVNOs) on the AT&T network. The MVNX API suite covers subscriber activation, number portability, device management, service lifecycle manage
  name: AT&T MVNO APIs
  slug: att-mvno-apis
- description: REST APIs for AT&T Business Voice and Cloud Voice services enabling partners to manage service ordering, provisioning, and administration for AT&T's enterprise voice and cloud communication products.
  name: AT&T Cloud Voice APIs
  slug: att-cloud-voice-apis
- description: Seamless API integration with AT&T's wireless and wireline IT and ordering systems. eBonding APIs enable enterprise partners and resellers to integrate their BSS/OSS systems directly with AT&T's backe
  name: AT&T eBonding APIs
  slug: att-ebonding-apis
artifact_total: 94
common:
- group: agent
  href: https://artifacts.apis.io/atandt/agentic-access/atandt-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/atandt-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/atandt/security/atandt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atandt-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/atandt/authentication/atandt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/atandt-authentication.yml
- group: auth
  href: https://artifacts.apis.io/atandt/scopes/atandt-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/atandt-scopes.yml
- group: design
  href: https://artifacts.apis.io/atandt/rules/atandt-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/atandt-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/atandt/vocabulary/atandt-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/atandt-vocabulary.yaml
- group: company
  title: ''
  type: Website
  url: https://www.att.com
- group: start
  title: ''
  type: Portal
  url: https://developer.att.com/s/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devex-web.att.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.att.com/s/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.att.com/oauth-2/docs
- group: operate
  title: ''
  type: Support
  url: https://developer.att.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.att.com/gen/general?pid=11561
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.att.com/gen/privacy-policy?pid=2506
- group: company
  title: ''
  type: Blog
  url: https://about.att.com/blogs
- group: operate
  title: ''
  type: StatusPage
  url: https://www.att.com/support/article/wireless/KM1000428
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/attdevsupport
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/att
- group: other
  title: ''
  type: X
  url: https://x.com/att
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/att
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/att
created: '2026-03-23'
description: AT&T Inc. is a multinational telecommunications conglomerate providing wireless and wireline communications, broadband internet, digital TV, and business services. As a Fortune 100 company, AT&T operates one of the largest telecommunications networks in the United States and globally. This profile covers AT&T's full API ecosystem including consumer telecommunications APIs, enterprise connectivity APIs, and business service management APIs available through AT&T's developer programs.
examples:
- key_count: 5
  name: Enterprise Apis Product Order Example
  slug: enterprise-apis-product-order-example
- key_count: 4
  name: Enterprise Apis Product Order Request Example
  slug: enterprise-apis-product-order-request-example
- key_count: 1
  name: Enterprise Apis Service Qualification Request Example
  slug: enterprise-apis-service-qualification-request-example
- key_count: 3
  name: Enterprise Apis Service Qualification Response Example
  slug: enterprise-apis-service-qualification-response-example
- key_count: 3
  name: Network Apis Create Session Request Example
  slug: network-apis-create-session-request-example
- key_count: 3
  name: Network Apis Device Connectivity Status Example
  slug: network-apis-device-connectivity-status-example
- key_count: 3
  name: Network Apis Device Roaming Status Example
  slug: network-apis-device-roaming-status-example
- key_count: 5
  name: Network Apis Network Metrics Example
  slug: network-apis-network-metrics-example
- key_count: 1
  name: Network Apis Number Verification Request Example
  slug: network-apis-number-verification-request-example
- key_count: 1
  name: Network Apis Number Verification Response Example
  slug: network-apis-number-verification-response-example
- key_count: 4
  name: Network Apis Session Info Example
  slug: network-apis-session-info-example
- key_count: 2
  name: Network Apis Sim Swap Check Request Example
  slug: network-apis-sim-swap-check-request-example
- key_count: 1
  name: Network Apis Sim Swap Check Response Example
  slug: network-apis-sim-swap-check-response-example
- key_count: 3
  name: Network Apis Threat Assessment Example
  slug: network-apis-threat-assessment-example
- key_count: 2
  name: Wireless Apis Delivery Info Example
  slug: wireless-apis-delivery-info-example
- key_count: 5
  name: Wireless Apis Inbound Sms Message Example
  slug: wireless-apis-inbound-sms-message-example
- key_count: 1
  name: Wireless Apis Send Sms Request Example
  slug: wireless-apis-send-sms-request-example
- key_count: 1
  name: Wireless Apis Send Sms Response Example
  slug: wireless-apis-send-sms-response-example
- key_count: 6
  name: Wireless Apis Token Request Example
  slug: wireless-apis-token-request-example
- key_count: 5
  name: Wireless Apis Token Response Example
  slug: wireless-apis-token-response-example
features:
- 'AT&T: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- AT&T Business APIs are sold via partner program with custom contracts.
finops:
- has_sources: true
  method: unmarked
  name: Atandt Finops
  primary_unit: ''
  service_category: Telecommunications
  slug: atandt-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: AT&T and Microsoft partnership for 5G and Azure-powered edge computing solutions for enterprise applications.
  name: Microsoft Azure
- description: Integration with Cisco enterprise networking and collaboration solutions through AT&T's business services.
  name: Cisco
- description: AT&T and IBM partnership for AI-powered network management and cloud services integration.
  name: IBM
- description: MVNX and enterprise APIs follow TM Forum Open API standards for telecom BSS/OSS interoperability.
  name: TM Forum Open APIs
- description: AT&T implements CAMARA open-source standard network APIs for cross-carrier developer platform interoperability.
  name: GSMA CAMARA
json_schemas:
- name: Product Order Request
  property_count: 4
  slug: enterprise-apis-product-order-request
- name: Product Order
  property_count: 5
  slug: enterprise-apis-product-order
- name: Service Qualification Request
  property_count: 1
  slug: enterprise-apis-service-qualification-request
- name: Service Qualification Response
  property_count: 3
  slug: enterprise-apis-service-qualification-response
- name: Create QoD Session Request
  property_count: 3
  slug: network-apis-create-session-request
- name: Device Connectivity Status
  property_count: 3
  slug: network-apis-device-connectivity-status
- name: Device Roaming Status
  property_count: 3
  slug: network-apis-device-roaming-status
- name: Network Metrics
  property_count: 5
  slug: network-apis-network-metrics
- name: Number Verification Request
  property_count: 1
  slug: network-apis-number-verification-request
- name: Number Verification Response
  property_count: 1
  slug: network-apis-number-verification-response
- name: QoD Session Info
  property_count: 4
  slug: network-apis-session-info
- name: SIM Swap Check Request
  property_count: 2
  slug: network-apis-sim-swap-check-request
- name: SIM Swap Check Response
  property_count: 1
  slug: network-apis-sim-swap-check-response
- name: Threat Assessment
  property_count: 3
  slug: network-apis-threat-assessment
- name: Delivery Info
  property_count: 2
  slug: wireless-apis-delivery-info
- name: Inbound SMS Message
  property_count: 5
  slug: wireless-apis-inbound-sms-message
- name: Send SMS Request
  property_count: 1
  slug: wireless-apis-send-sms-request
- name: Send SMS Response
  property_count: 1
  slug: wireless-apis-send-sms-response
- name: Token Request
  property_count: 6
  slug: wireless-apis-token-request
- name: Token Response
  property_count: 5
  slug: wireless-apis-token-response
json_structures:
- name: Enterprise Apis Product Order Request Structure
  property_count: 4
  slug: enterprise-apis-product-order-request-structure
- name: Enterprise Apis Product Order Structure
  property_count: 5
  slug: enterprise-apis-product-order-structure
- name: Enterprise Apis Service Qualification Request Structure
  property_count: 1
  slug: enterprise-apis-service-qualification-request-structure
- name: Enterprise Apis Service Qualification Response Structure
  property_count: 3
  slug: enterprise-apis-service-qualification-response-structure
- name: Network Apis Create Session Request Structure
  property_count: 3
  slug: network-apis-create-session-request-structure
- name: Network Apis Device Connectivity Status Structure
  property_count: 3
  slug: network-apis-device-connectivity-status-structure
- name: Network Apis Device Roaming Status Structure
  property_count: 3
  slug: network-apis-device-roaming-status-structure
- name: Network Apis Network Metrics Structure
  property_count: 5
  slug: network-apis-network-metrics-structure
- name: Network Apis Number Verification Request Structure
  property_count: 1
  slug: network-apis-number-verification-request-structure
- name: Network Apis Number Verification Response Structure
  property_count: 1
  slug: network-apis-number-verification-response-structure
- name: Network Apis Session Info Structure
  property_count: 4
  slug: network-apis-session-info-structure
- name: Network Apis Sim Swap Check Request Structure
  property_count: 2
  slug: network-apis-sim-swap-check-request-structure
- name: Network Apis Sim Swap Check Response Structure
  property_count: 1
  slug: network-apis-sim-swap-check-response-structure
- name: Network Apis Threat Assessment Structure
  property_count: 3
  slug: network-apis-threat-assessment-structure
- name: Wireless Apis Delivery Info Structure
  property_count: 2
  slug: wireless-apis-delivery-info-structure
- name: Wireless Apis Inbound Sms Message Structure
  property_count: 5
  slug: wireless-apis-inbound-sms-message-structure
- name: Wireless Apis Send Sms Request Structure
  property_count: 1
  slug: wireless-apis-send-sms-request-structure
- name: Wireless Apis Send Sms Response Structure
  property_count: 1
  slug: wireless-apis-send-sms-response-structure
- name: Wireless Apis Token Request Structure
  property_count: 6
  slug: wireless-apis-token-request-structure
- name: Wireless Apis Token Response Structure
  property_count: 5
  slug: wireless-apis-token-response-structure
jsonld:
- class_count: 0
  name: Enterprise Apis Context
  property_count: 1
  slug: enterprise-apis-context
- class_count: 0
  name: Network Apis Context
  property_count: 9
  slug: network-apis-context
- class_count: 0
  name: Wireless Apis Context
  property_count: 2
  slug: wireless-apis-context
layout: provider
modified: '2026-05-19'
name: AT&T
nav: Providers
network: true
overview: 'AT&T is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Wireless APIs, 5G Network APIs, Enterprise Connectivity APIs, and 3 more. Tagged areas include Fortune 100, Telecommunications, Fortune 100, Wireless, and Wireline.


  The AT&T catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  AT&T''s developer surface includes authentication, developer portal, documentation, support, engineering blog, YouTube channel, and 15 more developer resources.'
plans:
- name: Atandt Plans Pricing
  plan_count: 1
  slug: atandt-plans-pricing
press:
- date: '2026-05-25'
  title: Enhancing Network Optimization and Planning with AI
  url: https://about.att.com/blogs/2025/geo-modeler.html
- date: '2026-05-25'
  title: 'AI for small business: How to get started'
  url: https://www.business.att.com/learn/articles/ai-for-small-business-how-to-get-started.html
- date: '2026-05-25'
  title: AT&T Transformed into an AI Company with H2O.ai
  url: https://h2o.ai/case-studies/att-transformed-into-an-ai-company-with-h2o-ai/
- date: '2026-05-25'
  title: AT&T and H2O.ai Launch Co-Developed Artificial ...
  url: https://www.prnewswire.com/news-releases/att-and-h2oai-launch-co-developed-artificial-intelligence-feature-store-with-industry-first-capabilities-301410998.html
- date: '2026-05-25'
  title: AT&T Tests New AI Digital Receptionist
  url: https://about.att.com/blogs/2025/ai-digital-receptionist.html
random_paper: 12
rate_limits:
- limit_count: 1
  name: Atandt Rate Limits
  slug: atandt-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 5
  extends: []
  name: AT&T — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: atandt-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: AT&T API Rules
  rule_count: 33
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 19
  slug: atandt-spectral-rules
scopes:
- name: Atandt Scopes
  scope_count: 2
  slug: atandt-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 68.4
    catalog_earned_first_party: 0.0
    catalog_gap: 46.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 40.0
    contract_governance: 27.3
    contract_quality: 36.7
    developer_ergonomics: 50.0
    discoverability: 71.4
    operational_transparency: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 35.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atandt Authentication
  slug: atandt-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Atandt Domain Security
  slug: atandt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atandt
solutions:
- description: Comprehensive connectivity, cloud, cybersecurity, and collaboration solutions for small, medium, and enterprise businesses.
  name: AT&T Business
- description: Dedicated broadband network for America's first responders including priority access, preemption, and dedicated coverage expansion.
  name: FirstNet
- description: Network services for carriers, MVNOs, and resellers including voice, data, and roaming services on AT&T's infrastructure.
  name: AT&T Wholesale
tags:
- Fortune 100
- Telecommunications
- Fortune 100
- Wireless
- Wireline
- Broadband
- Enterprise
- 5G
- Network
use_cases:
- description: Automate wireline service ordering, qualification, and provisioning for enterprise customers through API integration.
  name: Enterprise Digital Transformation
- description: Use AT&T network signals for frictionless authentication and fraud prevention in consumer and business mobile applications.
  name: Mobile App Authentication
- description: Connect and manage IoT devices using AT&T's 5G and LTE networks with quality of service guarantees for mission-critical applications.
  name: IoT and Edge Computing
- description: Launch and operate mobile virtual network services on AT&T's infrastructure using TM Forum-standard management APIs.
  name: MVNO Launch and Operations
- description: Integrate AT&T voice and messaging APIs into business workflows for employee and customer communication automation.
  name: Workforce Communication
website: https://www.att.com
---
