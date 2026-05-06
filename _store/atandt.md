---
aid: atandt
name: AT&T
description: AT&T Inc. is a multinational telecommunications conglomerate providing wireless and wireline communications, broadband internet, digital TV, and business services. As a Fortune 100 company, AT&T operates one of the largest telecommunications networks in the United States and globally. This profile covers AT&T's full API ecosystem including consumer telecommunications APIs, enterprise connectivity APIs, and business service management APIs available through AT&T's developer programs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Telecommunications
  - Fortune 100
  - Wireless
  - Wireline
  - Broadband
  - Enterprise
  - 5G
  - Network
url: https://raw.githubusercontent.com/api-evangelist/atandt/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: atandt:att-wireless-apis
    name: AT&T Wireless APIs
    description: Developer APIs for AT&T's wireless network capabilities including SMS messaging, MMS messaging, OAuth authentication, speech-to-text, text-to-speech, in-app messaging, and advertising APIs for consumer and business applications.
    humanURL: https://developer.att.com/s/
    baseURL: https://api.att.com
    tags:
      - Wireless
      - SMS
      - MMS
      - Speech
      - Advertising
      - OAuth
    properties:
      - type: Documentation
        url: https://developer.att.com/s/
      - type: Portal
        url: https://developer.att.com/s/
      - type: Authentication
        url: https://developer.att.com/oauth-2/docs
      - type: GettingStarted
        url: https://developer.att.com/s/
      - type: OpenAPI
        url: openapi/atandt-wireless-apis.yaml
  - aid: atandt:att-network-apis
    name: AT&T 5G Network APIs
    description: CAMARA-standard 5G network APIs available through the AT&T Developer Hub and Network API Accelerator Program. Includes SIM Swap detection, Device Status, Number Verification, Quality on Demand, Network Insights, and Mobility Threat and Anomaly Detection APIs.
    humanURL: https://devex-web.att.com/developer-hub/
    baseURL: https://api.att.com
    tags:
      - 5G
      - CAMARA
      - Network
      - Device Status
      - SIM Swap
      - Quality of Service
    properties:
      - type: Documentation
        url: https://devex-web.att.com/developer-hub/
      - type: GettingStarted
        url: https://devex-web.att.com/developer-hub/docs/network-api-accelerator-program
      - type: OpenAPI
        url: openapi/atandt-network-apis.yaml
  - aid: atandt:att-enterprise-connectivity-apis
    name: AT&T Enterprise Connectivity APIs
    description: Enterprise-grade APIs for AT&T wireline business services including service qualification, quoting, ordering, and provisioning. The Alliance API suite supports automated ordering of AVPN, IPBB, ATTPhone, ASE, and AT&T Internet Air for Business services.
    humanURL: https://devex-web.att.com/alliance
    baseURL: https://devex-web.att.com
    tags:
      - Enterprise
      - Wireline
      - AVPN
      - Service Ordering
      - Service Qualification
    properties:
      - type: Documentation
        url: https://devex-web.att.com/alliance
      - type: GettingStarted
        url: https://devex-web.att.com/order/docs/get-started-with-ordering-api
      - type: OpenAPI
        url: openapi/atandt-enterprise-connectivity-apis.yaml
  - aid: atandt:att-mvno-apis
    name: AT&T MVNO APIs
    description: TM Forum-aligned APIs for mobile virtual network operators (MVNOs) on the AT&T network. The MVNX API suite covers subscriber activation, number portability, device management, service lifecycle management, and balance management following TMF open standards.
    humanURL: https://devex-web.att.com/mvnx
    baseURL: https://devex-web.att.com
    tags:
      - MVNO
      - TM Forum
      - Subscriber Management
      - Porting
    properties:
      - type: Documentation
        url: https://devex-web.att.com/mvnx/docs/mvnx-quickstart
      - type: GettingStarted
        url: https://devex-web.att.com/mvnx/docs/mvnx-quickstart
  - aid: atandt:att-cloud-voice-apis
    name: AT&T Cloud Voice APIs
    description: REST APIs for AT&T Business Voice and Cloud Voice services enabling partners to manage service ordering, provisioning, and administration for AT&T's enterprise voice and cloud communication products.
    humanURL: https://devex-web.att.com/business-voice-cloud-voice
    baseURL: https://devex-web.att.com
    tags:
      - Voice
      - Cloud
      - Business
      - UCaaS
    properties:
      - type: Documentation
        url: https://devex-web.att.com/business-voice-cloud-voice
  - aid: atandt:att-ebonding-apis
    name: AT&T eBonding APIs
    description: Seamless API integration with AT&T's wireless and wireline IT and ordering systems. eBonding APIs enable enterprise partners and resellers to integrate their BSS/OSS systems directly with AT&T's backend systems for automated order management and status updates.
    humanURL: https://devex-web.att.com/ebonding-common
    baseURL: https://devex-web.att.com
    tags:
      - eBonding
      - Enterprise
      - BSS
      - OSS
      - Integration
    properties:
      - type: Documentation
        url: https://devex-web.att.com/ebonding-common
common:
  - type: SpectralRules
    url: rules/atandt-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/atandt-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/wireless-messaging.yaml
  - type: NaftikoCapability
    url: capabilities/network-security.yaml
  - type: Website
    url: https://www.att.com
  - type: Portal
    url: https://developer.att.com/s/
  - type: DeveloperPortal
    url: https://devex-web.att.com/
  - type: Documentation
    url: https://developer.att.com/s/
  - type: Authentication
    url: https://developer.att.com/oauth-2/docs
  - type: Support
    url: https://developer.att.com/support
  - type: TermsOfService
    url: https://www.att.com/gen/general?pid=11561
  - type: PrivacyPolicy
    url: https://www.att.com/gen/privacy-policy?pid=2506
  - type: Blog
    url: https://about.att.com/blogs
  - type: StatusPage
    url: https://www.att.com/support/article/wireless/KM1000428
  - type: GitHubOrganization
    url: https://github.com/attdevsupport
  - type: GitHubOrganization
    url: https://github.com/att
  - type: X
    url: https://x.com/att
  - type: LinkedIn
    url: https://www.linkedin.com/company/att
  - type: YouTube
    url: https://www.youtube.com/att
  - type: Features
    data:
      - 'AT&T: API access via partner / B2B contracts only'
      - No public API pricing published — contact enterprise sales
      - AT&T Business APIs are sold via partner program with custom contracts.
    sources:
      - https://developer.att.com/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Enterprise Digital Transformation
        description: Automate wireline service ordering, qualification, and provisioning for enterprise customers through API integration.
      - name: Mobile App Authentication
        description: Use AT&T network signals for frictionless authentication and fraud prevention in consumer and business mobile applications.
      - name: IoT and Edge Computing
        description: Connect and manage IoT devices using AT&T's 5G and LTE networks with quality of service guarantees for mission-critical applications.
      - name: MVNO Launch and Operations
        description: Launch and operate mobile virtual network services on AT&T's infrastructure using TM Forum-standard management APIs.
      - name: Workforce Communication
        description: Integrate AT&T voice and messaging APIs into business workflows for employee and customer communication automation.
  - type: Integrations
    data:
      - name: Microsoft Azure
        description: AT&T and Microsoft partnership for 5G and Azure-powered edge computing solutions for enterprise applications.
      - name: Cisco
        description: Integration with Cisco enterprise networking and collaboration solutions through AT&T's business services.
      - name: IBM
        description: AT&T and IBM partnership for AI-powered network management and cloud services integration.
      - name: TM Forum Open APIs
        description: MVNX and enterprise APIs follow TM Forum Open API standards for telecom BSS/OSS interoperability.
      - name: GSMA CAMARA
        description: AT&T implements CAMARA open-source standard network APIs for cross-carrier developer platform interoperability.
  - type: Solutions
    data:
      - name: AT&T Business
        description: Comprehensive connectivity, cloud, cybersecurity, and collaboration solutions for small, medium, and enterprise businesses.
      - name: FirstNet
        description: Dedicated broadband network for America's first responders including priority access, preemption, and dedicated coverage expansion.
      - name: AT&T Wholesale
        description: Network services for carriers, MVNOs, and resellers including voice, data, and roaming services on AT&T's infrastructure.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
