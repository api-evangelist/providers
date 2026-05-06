---
aid: at-t-developer-hub
name: AT&T Developer Hub
description: The AT&T Developer Hub provides access to cutting-edge network APIs including 5G, edge computing, and CAMARA industry-standard APIs. The Network API Accelerator Program offers early adopters pre-release, invite-only access to network capabilities spanning device status, SIM swap detection, number verification, quality of service on demand, network insights, and mobility threat detection. AT&T's network APIs enable developers to build advanced applications leveraging the U.S. mobile network for authentication, fraud prevention, performance optimization, and security.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - 5G
  - Network APIs
  - CAMARA
  - Connectivity
  - Telecommunications
  - Edge Computing
  - Device Status
  - SIM Swap
url: https://raw.githubusercontent.com/api-evangelist/at-t-developer-hub/refs/heads/main/apis.yml
created: '2025-05-02'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: at-t-developer-hub:att-network-insights-api
    name: AT&T Network Insights API
    description: Delivers performance metrics and device-level network data, providing developers with insights into network conditions, signal quality, and performance indicators for connected devices on the AT&T network.
    humanURL: https://devex-web.att.com/developer-hub/
    baseURL: https://api.att.com
    tags:
      - Network Performance
      - Metrics
      - 5G
      - Monitoring
    properties:
      - type: Documentation
        url: https://devex-web.att.com/developer-hub/
      - type: GettingStarted
        url: https://devex-web.att.com/developer-hub/docs/network-api-accelerator-program
      - type: OpenAPI
        url: openapi/at-t-developer-hub-network-insights-api.yaml
  - aid: at-t-developer-hub:att-mobility-threat-anomaly-detection-api
    name: AT&T Mobility Threat and Anomaly Detection API
    description: Uses machine learning to identify threats and unusual activity on mobile devices on the AT&T network. Provides real-time threat detection signals to applications for enhanced security, fraud prevention, and anomaly detection across subscriber devices.
    humanURL: https://devex-web.att.com/developer-hub/
    baseURL: https://api.att.com
    tags:
      - Security
      - Fraud Detection
      - Machine Learning
      - Anomaly Detection
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://devex-web.att.com/developer-hub/
      - type: GettingStarted
        url: https://devex-web.att.com/developer-hub/docs/network-api-accelerator-program
      - type: OpenAPI
        url: openapi/at-t-developer-hub-mobility-threat-anomaly-detection-api.yaml
  - aid: at-t-developer-hub:att-sim-swap-api
    name: AT&T SIM Swap API
    description: CAMARA-standard API that checks when SIM cards associated with mobile numbers have changed. Enables applications to strengthen authentication flows and detect SIM swap fraud by querying AT&T's network for recent SIM card changes on a subscriber's number.
    humanURL: https://devex-web.att.com/developer-hub/
    baseURL: https://api.att.com
    tags:
      - SIM Swap
      - Authentication
      - Fraud Prevention
      - CAMARA
      - Security
    properties:
      - type: Documentation
        url: https://devex-web.att.com/developer-hub/
      - type: GettingStarted
        url: https://devex-web.att.com/developer-hub/docs/network-api-accelerator-program
      - type: OpenAPI
        url: openapi/at-t-developer-hub-sim-swap-api.yaml
  - aid: at-t-developer-hub:att-device-status-api
    name: AT&T Device Status API
    description: CAMARA-standard API that checks the connectivity status of user equipment, including roaming information. Enables applications to determine if a device is reachable, connected, and whether it is roaming on a partner network, supporting location-aware and connectivity-sensitive application logic.
    humanURL: https://devex-web.att.com/developer-hub/
    baseURL: https://api.att.com
    tags:
      - Device Status
      - Connectivity
      - Roaming
      - CAMARA
      - 5G
    properties:
      - type: Documentation
        url: https://devex-web.att.com/developer-hub/
      - type: GettingStarted
        url: https://devex-web.att.com/developer-hub/docs/network-api-accelerator-program
      - type: OpenAPI
        url: openapi/at-t-developer-hub-device-status-api.yaml
  - aid: at-t-developer-hub:att-quality-on-demand-api
    name: AT&T Quality on Demand API
    description: CAMARA-standard Quality of Service on Demand (QoD) API that temporarily enhances Quality of Service on 5G PDU sessions. Enables applications to request prioritized network throughput, reduced latency, or guaranteed bandwidth for time-sensitive operations like video streaming, gaming, remote surgery, or industrial automation.
    humanURL: https://devex-web.att.com/developer-hub/
    baseURL: https://api.att.com
    tags:
      - Quality of Service
      - QoS
      - 5G
      - CAMARA
      - Network Slicing
      - Latency
    properties:
      - type: Documentation
        url: https://devex-web.att.com/developer-hub/
      - type: GettingStarted
        url: https://devex-web.att.com/developer-hub/docs/network-api-accelerator-program
      - type: OpenAPI
        url: openapi/at-t-developer-hub-quality-on-demand-api.yaml
  - aid: at-t-developer-hub:att-number-verification-api
    name: AT&T Number Verification API
    description: CAMARA-standard API enabling seamless device authentication via the mobile network. Verifies that a device is currently using a specific phone number without requiring the user to enter an OTP, leveraging the AT&T network signal for frictionless identity verification in mobile applications.
    humanURL: https://devex-web.att.com/developer-hub/
    baseURL: https://api.att.com
    tags:
      - Number Verification
      - Authentication
      - Identity
      - CAMARA
      - Mobile
    properties:
      - type: Documentation
        url: https://devex-web.att.com/developer-hub/
      - type: GettingStarted
        url: https://devex-web.att.com/developer-hub/docs/network-api-accelerator-program
      - type: OpenAPI
        url: openapi/at-t-developer-hub-number-verification-api.yaml
common:
  - type: Website
    url: https://www.att.com/
  - type: Portal
    url: https://developer.att.com/s/
  - type: DeveloperPortal
    url: https://devex-web.att.com/developer-hub/
  - type: Documentation
    url: https://devex-web.att.com/developer-hub/
  - type: GettingStarted
    url: https://devex-web.att.com/developer-hub/docs/network-api-accelerator-program
  - type: SignUp
    url: https://devex-web.att.com/developer-hub/docs/network-api-accelerator-program
  - type: TermsOfService
    url: https://www.att.com/gen/general?pid=11561
  - type: PrivacyPolicy
    url: https://www.att.com/gen/privacy-policy?pid=2506
  - type: GitHubOrganization
    url: https://github.com/attdevsupport
  - type: SpectralRules
    url: rules/at-t-developer-hub-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/at-t-developer-hub-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/network-security.yaml
  - type: NaftikoCapability
    url: capabilities/network-performance.yaml
  - type: Features
    data:
      - name: CAMARA Industry-Standard APIs
        description: Implements GSMA CAMARA open-source standard APIs including SIM Swap, Device Status, Number Verification, and Quality on Demand for cross-carrier interoperability.
      - name: Network API Accelerator Program
        description: Invite-only early access program for developers to trial pre-release 5G network APIs and influence future network capability development.
      - name: 5G Network Capabilities
        description: Exposes AT&T's 5G network intelligence including QoS on demand, network performance insights, and device connectivity status.
      - name: Fraud Prevention Network Signals
        description: Network-based fraud signals including SIM swap detection, number verification, and mobility threat detection to strengthen app security.
  - type: UseCases
    data:
      - name: SIM Swap Fraud Prevention
        description: Detect recent SIM card changes to prevent account takeover attacks and strengthen multi-factor authentication flows.
      - name: Frictionless Mobile Authentication
        description: Verify device phone numbers silently via the network without OTP codes, reducing authentication friction in mobile apps.
      - name: 5G Quality of Service Optimization
        description: Request guaranteed bandwidth or low latency for real-time applications like video conferencing, AR/VR, and industrial IoT.
      - name: Device Connectivity Monitoring
        description: Monitor device connectivity and roaming status to trigger location-aware application behaviors.
      - name: Threat Detection and Security
        description: Leverage AT&T network ML-based threat signals to detect anomalous device behavior and security incidents.
  - type: Integrations
    data:
      - name: Aduna Network API Platform
        description: AT&T's partnership with Aduna provides standardized access to AT&T 5G Network APIs with cross-carrier interoperability for all three major U.S. carriers.
      - name: Vonage (Ericsson)
        description: Collaboration with Vonage to bring AT&T CAMARA network APIs to communications platform developers.
      - name: GSMA CAMARA
        description: Member of GSMA's CAMARA open-source project defining standardized telco network APIs for cross-operator portability.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
