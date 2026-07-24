---
access_model:
  confidence: high
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: At T Developer Hub Agentic Access
  operation_count: 12
  slug: at-t-developer-hub-agentic-access
  summary_line: 12 operations · 10 acting
api_count: 8
apis:
- description: The Device Connectivity API from AT&T Developer Hub — 1 operation(s) for device connectivity.
  name: AT&T Developer Hub Device Connectivity API
  slug: at-t-developer-hub-device-connectivity-api
- description: The Device Roaming API from AT&T Developer Hub — 1 operation(s) for device roaming.
  name: AT&T Developer Hub Device Roaming API
  slug: at-t-developer-hub-device-roaming-api
- description: The Network Metrics API from AT&T Developer Hub — 1 operation(s) for network metrics.
  name: AT&T Developer Hub Network Metrics API
  slug: at-t-developer-hub-network-metrics-api
- description: The Number Verification API from AT&T Developer Hub — 1 operation(s) for number verification.
  name: AT&T Developer Hub Number Verification API
  slug: at-t-developer-hub-number-verification-api
- description: The QoD Sessions API from AT&T Developer Hub — 2 operation(s) for qod sessions.
  name: AT&T Developer Hub QoD Sessions API
  slug: at-t-developer-hub-qod-sessions-api
- description: The SIM Swap API from AT&T Developer Hub — 2 operation(s) for sim swap.
  name: AT&T Developer Hub SIM Swap API
  slug: at-t-developer-hub-sim-swap-api
- description: The Threat Detection API from AT&T Developer Hub — 1 operation(s) for threat detection.
  name: AT&T Developer Hub Threat Detection API
  slug: at-t-developer-hub-threat-detection-api
- description: The Threat Subscriptions API from AT&T Developer Hub — 1 operation(s) for threat subscriptions.
  name: AT&T Developer Hub Threat Subscriptions API
  slug: at-t-developer-hub-threat-subscriptions-api
artifact_total: 137
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/at-t-developer-hub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/at-t-developer-hub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/at-t-developer-hub-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/at-t-developer-hub-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.att.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.att.com/s/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devex-web.att.com/developer-hub/
- group: docs
  title: ''
  type: Documentation
  url: https://devex-web.att.com/developer-hub/
- group: start
  title: ''
  type: GettingStarted
  url: https://devex-web.att.com/developer-hub/docs/network-api-accelerator-program
- group: start
  title: ''
  type: Signup
  url: https://devex-web.att.com/developer-hub/docs/network-api-accelerator-program
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.att.com/gen/general?pid=11561
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.att.com/gen/privacy-policy?pid=2506
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/attdevsupport
- group: design
  title: ''
  type: SpectralRules
  url: rules/at-t-developer-hub-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/at-t-developer-hub-vocabulary.yaml
created: '2025-05-02'
description: The AT&T Developer Hub provides access to cutting-edge network APIs including 5G, edge computing, and CAMARA industry-standard APIs. The Network API Accelerator Program offers early adopters pre-release, invite-only access to network capabilities spanning device status, SIM swap detection, number verification, quality of service on demand, network insights, and mobility threat detection. AT&T's network APIs enable developers to build advanced applications leveraging the U.S. mobile network for authentication, fraud prevention, performance optimization, and security.
examples:
- key_count: 6
  name: At T Developer Hub Checksimswap Example
  slug: at-t-developer-hub-checksimswap-example
- key_count: 6
  name: At T Developer Hub Createqodsession Example
  slug: at-t-developer-hub-createqodsession-example
- key_count: 6
  name: At T Developer Hub Getdeviceconnectivitystatus Example
  slug: at-t-developer-hub-getdeviceconnectivitystatus-example
- key_count: 6
  name: At T Developer Hub Getdeviceroamingstatus Example
  slug: at-t-developer-hub-getdeviceroamingstatus-example
- key_count: 6
  name: At T Developer Hub Getdevicethreats Example
  slug: at-t-developer-hub-getdevicethreats-example
- key_count: 6
  name: At T Developer Hub Getnetworkmetrics Example
  slug: at-t-developer-hub-getnetworkmetrics-example
- key_count: 6
  name: At T Developer Hub Getqodsession Example
  slug: at-t-developer-hub-getqodsession-example
- key_count: 6
  name: At T Developer Hub Listqodsessions Example
  slug: at-t-developer-hub-listqodsessions-example
- key_count: 6
  name: At T Developer Hub Retrievesimswapdate Example
  slug: at-t-developer-hub-retrievesimswapdate-example
- key_count: 6
  name: At T Developer Hub Subscribetothreatalerts Example
  slug: at-t-developer-hub-subscribetothreatalerts-example
- key_count: 6
  name: At T Developer Hub Verifyphonenumber Example
  slug: at-t-developer-hub-verifyphonenumber-example
- key_count: 1
  name: Device Status Api Device Connectivity Request Example
  slug: device-status-api-device-connectivity-request-example
- key_count: 2
  name: Device Status Api Device Connectivity Status Example
  slug: device-status-api-device-connectivity-status-example
- key_count: 3
  name: Device Status Api Device Example
  slug: device-status-api-device-example
- key_count: 1
  name: Device Status Api Device Roaming Request Example
  slug: device-status-api-device-roaming-request-example
- key_count: 3
  name: Device Status Api Device Roaming Status Example
  slug: device-status-api-device-roaming-status-example
- key_count: 1
  name: Mobility Threat Anomaly Detection Api Device Example
  slug: mobility-threat-anomaly-detection-api-device-example
- key_count: 4
  name: Mobility Threat Anomaly Detection Api Threat Assessment Example
  slug: mobility-threat-anomaly-detection-api-threat-assessment-example
- key_count: 1
  name: Mobility Threat Anomaly Detection Api Threat Assessment Request Example
  slug: mobility-threat-anomaly-detection-api-threat-assessment-request-example
- key_count: 4
  name: Mobility Threat Anomaly Detection Api Threat Indicator Example
  slug: mobility-threat-anomaly-detection-api-threat-indicator-example
- key_count: 4
  name: Mobility Threat Anomaly Detection Api Threat Subscription Example
  slug: mobility-threat-anomaly-detection-api-threat-subscription-example
- key_count: 4
  name: Mobility Threat Anomaly Detection Api Threat Subscription Request Example
  slug: mobility-threat-anomaly-detection-api-threat-subscription-request-example
- key_count: 2
  name: Network Insights Api Device Example
  slug: network-insights-api-device-example
- key_count: 6
  name: Network Insights Api Network Metrics Example
  slug: network-insights-api-network-metrics-example
- key_count: 1
  name: Network Insights Api Network Metrics Request Example
  slug: network-insights-api-network-metrics-request-example
- key_count: 1
  name: Number Verification Api Number Verification Request Example
  slug: number-verification-api-number-verification-request-example
- key_count: 1
  name: Number Verification Api Number Verification Response Example
  slug: number-verification-api-number-verification-response-example
- key_count: 5
  name: Quality On Demand Api Create Session Request Example
  slug: quality-on-demand-api-create-session-request-example
- key_count: 2
  name: Quality On Demand Api Device Example
  slug: quality-on-demand-api-device-example
- key_count: 7
  name: Quality On Demand Api Session Info Example
  slug: quality-on-demand-api-session-info-example
- key_count: 2
  name: Sim Swap Api Sim Swap Check Request Example
  slug: sim-swap-api-sim-swap-check-request-example
- key_count: 1
  name: Sim Swap Api Sim Swap Check Response Example
  slug: sim-swap-api-sim-swap-check-response-example
- key_count: 1
  name: Sim Swap Api Sim Swap Date Request Example
  slug: sim-swap-api-sim-swap-date-request-example
- key_count: 1
  name: Sim Swap Api Sim Swap Date Response Example
  slug: sim-swap-api-sim-swap-date-response-example
features:
- description: Implements GSMA CAMARA open-source standard APIs including SIM Swap, Device Status, Number Verification, and Quality on Demand for cross-carrier interoperability.
  name: CAMARA Industry-Standard APIs
- description: Invite-only early access program for developers to trial pre-release 5G network APIs and influence future network capability development.
  name: Network API Accelerator Program
- description: Exposes AT&T's 5G network intelligence including QoS on demand, network performance insights, and device connectivity status.
  name: 5G Network Capabilities
- description: Network-based fraud signals including SIM swap detection, number verification, and mobility threat detection to strengthen app security.
  name: Fraud Prevention Network Signals
finops:
- name: At T Developer Hub Finops
  service_category: Telecommunications / Network APIs
  slug: at-t-developer-hub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/at-t-developer-hub.png
integrations:
- description: AT&T's partnership with Aduna provides standardized access to AT&T 5G Network APIs with cross-carrier interoperability for all three major U.S. carriers.
  name: Aduna Network API Platform
- description: Collaboration with Vonage to bring AT&T CAMARA network APIs to communications platform developers.
  name: Vonage (Ericsson)
- description: Member of GSMA's CAMARA open-source project defining standardized telco network APIs for cross-operator portability.
  name: GSMA CAMARA
json_schemas:
- name: CreateSessionRequest
  property_count: 5
  slug: at-t-developer-hub-createsessionrequest
- name: Device
  property_count: 3
  slug: at-t-developer-hub-device
- name: DeviceConnectivityRequest
  property_count: 1
  slug: at-t-developer-hub-deviceconnectivityrequest
- name: DeviceConnectivityStatus
  property_count: 2
  slug: at-t-developer-hub-deviceconnectivitystatus
- name: DeviceRoamingRequest
  property_count: 1
  slug: at-t-developer-hub-deviceroamingrequest
- name: DeviceRoamingStatus
  property_count: 3
  slug: at-t-developer-hub-deviceroamingstatus
- name: ErrorInfo
  property_count: 3
  slug: at-t-developer-hub-errorinfo
- name: NetworkMetrics
  property_count: 6
  slug: at-t-developer-hub-networkmetrics
- name: NetworkMetricsRequest
  property_count: 1
  slug: at-t-developer-hub-networkmetricsrequest
- name: NumberVerificationRequest
  property_count: 1
  slug: at-t-developer-hub-numberverificationrequest
- name: NumberVerificationResponse
  property_count: 1
  slug: at-t-developer-hub-numberverificationresponse
- name: SessionInfo
  property_count: 7
  slug: at-t-developer-hub-sessioninfo
- name: SimSwapCheckRequest
  property_count: 2
  slug: at-t-developer-hub-simswapcheckrequest
- name: SimSwapCheckResponse
  property_count: 1
  slug: at-t-developer-hub-simswapcheckresponse
- name: SimSwapDateRequest
  property_count: 1
  slug: at-t-developer-hub-simswapdaterequest
- name: SimSwapDateResponse
  property_count: 1
  slug: at-t-developer-hub-simswapdateresponse
- name: ThreatAssessment
  property_count: 4
  slug: at-t-developer-hub-threatassessment
- name: ThreatAssessmentRequest
  property_count: 1
  slug: at-t-developer-hub-threatassessmentrequest
- name: ThreatIndicator
  property_count: 4
  slug: at-t-developer-hub-threatindicator
- name: ThreatSubscription
  property_count: 4
  slug: at-t-developer-hub-threatsubscription
- name: ThreatSubscriptionRequest
  property_count: 4
  slug: at-t-developer-hub-threatsubscriptionrequest
- name: DeviceConnectivityRequest
  property_count: 1
  slug: device-status-api-device-connectivity-request
- name: DeviceConnectivityStatus
  property_count: 2
  slug: device-status-api-device-connectivity-status
- name: DeviceRoamingRequest
  property_count: 1
  slug: device-status-api-device-roaming-request
- name: DeviceRoamingStatus
  property_count: 3
  slug: device-status-api-device-roaming-status
- name: Device
  property_count: 3
  slug: device-status-api-device
- name: Device
  property_count: 1
  slug: mobility-threat-anomaly-detection-api-device
- name: ThreatAssessmentRequest
  property_count: 1
  slug: mobility-threat-anomaly-detection-api-threat-assessment-request
- name: ThreatAssessment
  property_count: 4
  slug: mobility-threat-anomaly-detection-api-threat-assessment
- name: ThreatIndicator
  property_count: 4
  slug: mobility-threat-anomaly-detection-api-threat-indicator
- name: ThreatSubscriptionRequest
  property_count: 4
  slug: mobility-threat-anomaly-detection-api-threat-subscription-request
- name: ThreatSubscription
  property_count: 4
  slug: mobility-threat-anomaly-detection-api-threat-subscription
- name: Device
  property_count: 2
  slug: network-insights-api-device
- name: NetworkMetricsRequest
  property_count: 1
  slug: network-insights-api-network-metrics-request
- name: NetworkMetrics
  property_count: 6
  slug: network-insights-api-network-metrics
- name: NumberVerificationRequest
  property_count: 1
  slug: number-verification-api-number-verification-request
- name: NumberVerificationResponse
  property_count: 1
  slug: number-verification-api-number-verification-response
- name: CreateSessionRequest
  property_count: 5
  slug: quality-on-demand-api-create-session-request
- name: Device
  property_count: 2
  slug: quality-on-demand-api-device
- name: SessionInfo
  property_count: 7
  slug: quality-on-demand-api-session-info
- name: SimSwapCheckRequest
  property_count: 2
  slug: sim-swap-api-sim-swap-check-request
- name: SimSwapCheckResponse
  property_count: 1
  slug: sim-swap-api-sim-swap-check-response
- name: SimSwapDateRequest
  property_count: 1
  slug: sim-swap-api-sim-swap-date-request
- name: SimSwapDateResponse
  property_count: 1
  slug: sim-swap-api-sim-swap-date-response
json_structures:
- name: At T Developer Hub Structure
  property_count: 0
  slug: at-t-developer-hub-structure
- name: Device Status Api Device Connectivity Request Structure
  property_count: 1
  slug: device-status-api-device-connectivity-request-structure
- name: Device Status Api Device Connectivity Status Structure
  property_count: 2
  slug: device-status-api-device-connectivity-status-structure
- name: Device Status Api Device Roaming Request Structure
  property_count: 1
  slug: device-status-api-device-roaming-request-structure
- name: Device Status Api Device Roaming Status Structure
  property_count: 3
  slug: device-status-api-device-roaming-status-structure
- name: Device Status Api Device Structure
  property_count: 3
  slug: device-status-api-device-structure
- name: Mobility Threat Anomaly Detection Api Device Structure
  property_count: 1
  slug: mobility-threat-anomaly-detection-api-device-structure
- name: Mobility Threat Anomaly Detection Api Threat Assessment Request Structure
  property_count: 1
  slug: mobility-threat-anomaly-detection-api-threat-assessment-request-structure
- name: Mobility Threat Anomaly Detection Api Threat Assessment Structure
  property_count: 4
  slug: mobility-threat-anomaly-detection-api-threat-assessment-structure
- name: Mobility Threat Anomaly Detection Api Threat Indicator Structure
  property_count: 4
  slug: mobility-threat-anomaly-detection-api-threat-indicator-structure
- name: Mobility Threat Anomaly Detection Api Threat Subscription Request Structure
  property_count: 4
  slug: mobility-threat-anomaly-detection-api-threat-subscription-request-structure
- name: Mobility Threat Anomaly Detection Api Threat Subscription Structure
  property_count: 4
  slug: mobility-threat-anomaly-detection-api-threat-subscription-structure
- name: Network Insights Api Device Structure
  property_count: 2
  slug: network-insights-api-device-structure
- name: Network Insights Api Network Metrics Request Structure
  property_count: 1
  slug: network-insights-api-network-metrics-request-structure
- name: Network Insights Api Network Metrics Structure
  property_count: 6
  slug: network-insights-api-network-metrics-structure
- name: Number Verification Api Number Verification Request Structure
  property_count: 1
  slug: number-verification-api-number-verification-request-structure
- name: Number Verification Api Number Verification Response Structure
  property_count: 1
  slug: number-verification-api-number-verification-response-structure
- name: Quality On Demand Api Create Session Request Structure
  property_count: 5
  slug: quality-on-demand-api-create-session-request-structure
- name: Quality On Demand Api Device Structure
  property_count: 2
  slug: quality-on-demand-api-device-structure
- name: Quality On Demand Api Session Info Structure
  property_count: 7
  slug: quality-on-demand-api-session-info-structure
- name: Sim Swap Api Sim Swap Check Request Structure
  property_count: 2
  slug: sim-swap-api-sim-swap-check-request-structure
- name: Sim Swap Api Sim Swap Check Response Structure
  property_count: 1
  slug: sim-swap-api-sim-swap-check-response-structure
- name: Sim Swap Api Sim Swap Date Request Structure
  property_count: 1
  slug: sim-swap-api-sim-swap-date-request-structure
- name: Sim Swap Api Sim Swap Date Response Structure
  property_count: 1
  slug: sim-swap-api-sim-swap-date-response-structure
jsonld:
- class_count: 5
  name: At T Developer Hub Device Status Api Context
  property_count: 11
  slug: at-t-developer-hub-device-status-api-context
- class_count: 7
  name: At T Developer Hub Mobility Threat Anomaly Detection Api Context
  property_count: 14
  slug: at-t-developer-hub-mobility-threat-anomaly-detection-api-context
- class_count: 3
  name: At T Developer Hub Network Insights Api Context
  property_count: 10
  slug: at-t-developer-hub-network-insights-api-context
- class_count: 2
  name: At T Developer Hub Number Verification Api Context
  property_count: 2
  slug: at-t-developer-hub-number-verification-api-context
- class_count: 3
  name: At T Developer Hub Quality On Demand Api Context
  property_count: 13
  slug: at-t-developer-hub-quality-on-demand-api-context
- class_count: 4
  name: At T Developer Hub Sim Swap Api Context
  property_count: 4
  slug: at-t-developer-hub-sim-swap-api-context
layout: provider
modified: '2026-05-19'
name: AT&T Developer Hub
nav: Providers
network: true
overview: 'AT&T Developer Hub publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Device Connectivity API, Device Roaming API, Network Metrics API, and 5 more. Tagged areas include Fortune 100, 5G, Network APIs, CAMARA, and Connectivity.


  The AT&T Developer Hub catalog on APIs.io includes 6 JSON-LD contexts and 2 Spectral governance rulesets.


  AT&T Developer Hub''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, and 10 more developer resources.'
plans:
- name: At T Developer Hub Plans Pricing
  plan_count: 1
  slug: at-t-developer-hub-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: At T Developer Hub Rate Limits
  slug: at-t-developer-hub-rate-limits
rules:
- name: AT&T Developer Hub API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: at-t-developer-hub-jsonschema-spectral-rules
- name: AT&T Developer Hub API Rules
  rule_count: 32
  severity_counts:
    error: 14
    hint: 0
    info: 4
    warn: 14
  slug: at-t-developer-hub-spectral-rules
scopes:
- name: At T Developer Hub Scopes
  scope_count: 0
  slug: at-t-developer-hub-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 59.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 71.7
    developer_ergonomics: 39.1
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 26.3
  previous_composite: 59.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: At T Developer Hub Authentication
  slug: at-t-developer-hub-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: At T Developer Hub Domain Security
  slug: at-t-developer-hub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: at-t-developer-hub
tags:
- Fortune 100
- 5G
- Network APIs
- CAMARA
- Connectivity
- Telecommunications
- Edge Computing
- Device Status
- SIM Swap
use_cases:
- description: Detect recent SIM card changes to prevent account takeover attacks and strengthen multi-factor authentication flows.
  name: SIM Swap Fraud Prevention
- description: Verify device phone numbers silently via the network without OTP codes, reducing authentication friction in mobile apps.
  name: Frictionless Mobile Authentication
- description: Request guaranteed bandwidth or low latency for real-time applications like video conferencing, AR/VR, and industrial IoT.
  name: 5G Quality of Service Optimization
- description: Monitor device connectivity and roaming status to trigger location-aware application behaviors.
  name: Device Connectivity Monitoring
- description: Leverage AT&T network ML-based threat signals to detect anomalous device behavior and security incidents.
  name: Threat Detection and Security
website: https://www.att.com/
---
