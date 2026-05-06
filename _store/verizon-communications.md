---
aid: verizon-communications
name: Verizon Communications
description: Verizon Communications is one of the world's leading providers of technology and communications services, offering wireless, wireline, broadband, and global enterprise services to consumers, businesses, and government customers. Verizon exposes developer APIs for network capabilities including SIM swap detection, number verification, IoT device management via ThingSpace, 5G edge computing, contact center voice APIs, and TM Forum-certified service management APIs for enterprise customers.
url: https://raw.githubusercontent.com/api-evangelist/verizon-communications/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Telecommunications
  - Wireless
  - Network APIs
  - IoT
  - 5G
  - Enterprise
  - Identity
apis:
  - aid: verizon-communications:network-apis
    name: Verizon Network APIs
    description: Verizon Network APIs provide authentication, fraud prevention, and device intelligence capabilities leveraging Verizon's mobile network. Includes Number Verification API for seamless device authentication and SIM Swap API for detecting fraudulent account takeovers.
    humanURL: https://www.verizon.com/business/solutions/network-apis/
    tags:
      - Network APIs
      - Authentication
      - Fraud Prevention
      - Identity
      - SIM Swap
      - Number Verification
    properties:
      - type: Documentation
        url: https://www.verizon.com/business/solutions/network-apis/
      - type: Portal
        url: https://developers.verizon.com/
  - aid: verizon-communications:thingspace
    name: Verizon ThingSpace IoT API
    description: ThingSpace gives organizations of all sizes tools to build IoT solutions, manage connected devices, and solve business problems end-to-end. Provides device connectivity management, diagnostics, software management, and location services for IoT deployments.
    humanURL: https://thingspace.verizon.com
    tags:
      - IoT
      - Device Management
      - Connectivity
      - Wireless
    properties:
      - type: Documentation
        url: https://thingspace.verizon.com/resources/documentation/connectivity/API_Reference/
      - type: Portal
        url: https://thingspace.verizon.com
      - type: APIReference
        url: https://thingspace.verizon.com/resources/documentation/connectivity/API_Console/
  - aid: verizon-communications:5g-edge
    name: Verizon 5G Edge API
    description: Verizon 5G Edge API enables developers to build ultra-low-latency applications by leveraging Verizon's multi-access edge computing (MEC) infrastructure. Provides discovery, session management, and location services for 5G edge compute workloads.
    humanURL: https://www.verizon.com/business/5g-edge-portal/api-documentation.html
    tags:
      - 5G
      - Edge Computing
      - MEC
      - Ultra-Low Latency
    properties:
      - type: Documentation
        url: https://www.verizon.com/business/5g-edge-portal/api-documentation.html
      - type: APIReference
        url: https://www.verizon.com/business/5g-edge-portal/documentation/verizon-5g-edge-discovery-service/api-reference.html
      - type: Portal
        url: https://www.verizon.com/business/5g-edge-portal/index.html
  - aid: verizon-communications:service-management
    name: Verizon TM Forum Service Management APIs
    description: Verizon provides a suite of TM Forum certified service management APIs exposing ITIL functions for inventory management, incident management, change management, event management, problem management, order management, and billing management. APIs are bi-directional and keep Verizon and customer systems synchronized.
    humanURL: https://developers.verizon.com/
    tags:
      - TM Forum
      - ITIL
      - Service Management
      - Enterprise
      - B2B
    properties:
      - type: Documentation
        url: https://developers.verizon.com/
      - type: APIReference
        url: https://developers.verizon.com/
  - aid: verizon-communications:voice-api
    name: Verizon Voice API (CPaaS)
    description: Verizon Communications Platform as a Service (CPaaS) offering provides APIs for inbound and outbound IP interactive voice response (IPIVR) and call detail reporting. Available exclusively for IP Contact Center (IPCC) customers to build customized communication solutions.
    humanURL: https://www.verizon.com/business/products/contact-center-cx/voice-api/
    tags:
      - CPaaS
      - Voice
      - Contact Center
      - IVR
      - Communications
    properties:
      - type: Documentation
        url: https://www.verizon.com/business/products/contact-center-cx/voice-api/
common:
  - type: Website
    url: https://www.verizon-communications.com
  - type: Portal
    url: https://developers.verizon.com/
  - type: Documentation
    url: https://developers.verizon.com/
  - type: Support
    url: https://developers.verizon.com/#/apis/ns/documentation/help
  - type: FAQ
    url: https://developers.verizon.com/#/apis/ns/documentation/frequently-asked-questions
  - type: Login
    url: https://secure.verizon.com/signin?goto=https://developers.verizon.com/apis/sec/v1/login
  - type: SignUp
    url: https://secure.verizon.com/account/register/start?goto=https%3A%2F%2Fdevelopers.verizon.com%2Fapis%2Fsec%2Fv1%2Flogin
  - type: PrivacyPolicy
    url: https://www.verizon.com/about/privacy/
  - type: TermsOfService
    url: https://www.verizon.com/about/terms-conditions/
  - type: Features
    data:
      - name: Number Verification
        description: Seamless authentication of end-user mobile devices via network-based verification, eliminating passwords and one-time codes.
      - name: SIM Swap Detection
        description: Check if a SIM card associated with a phone number has been recently changed to detect account takeover fraud.
      - name: IoT Device Management
        description: Full lifecycle management of IoT devices including connectivity, diagnostics, software updates, and location tracking via ThingSpace.
      - name: 5G Edge Computing
        description: Multi-access edge computing APIs for deploying ultra-low-latency applications on Verizon's 5G MEC infrastructure.
      - name: TM Forum Open APIs
        description: TM Forum-certified ITIL APIs for enterprise service management including inventory, incident, change, order, and billing management.
      - name: Contact Center Voice APIs
        description: CPaaS APIs for customized IP interactive voice response (IPIVR) and call detail reporting for contact center operations.
  - type: UseCases
    data:
      - name: Fraud Prevention
        description: Use SIM Swap and Number Verification APIs to protect users from account takeover and SIM-swapping fraud.
      - name: Passwordless Authentication
        description: Authenticate users seamlessly via mobile network without passwords using Number Verification API.
      - name: IoT Fleet Management
        description: Manage large-scale IoT device fleets with connectivity monitoring, remote diagnostics, and over-the-air software updates.
      - name: 5G Application Development
        description: Build edge-native applications leveraging ultra-low latency of Verizon's 5G MEC infrastructure.
      - name: Enterprise Service Automation
        description: Automate IT service management workflows using TM Forum-certified APIs integrated with ITSM platforms.
      - name: Contact Center Modernization
        description: Build customized IVR and call routing solutions using Verizon's CPaaS Voice API.
  - type: Integrations
    data:
      - name: ITSM Platforms
        description: Integrate TM Forum service management APIs with ITSM platforms like ServiceNow for automated incident and change management.
      - name: Identity Providers
        description: Embed Number Verification and SIM Swap APIs into authentication flows and identity provider SDKs.
      - name: IoT Platforms
        description: Connect ThingSpace device management APIs to IoT platforms and enterprise data lakes.
      - name: Edge Cloud Providers
        description: Deploy 5G Edge applications across Verizon's MEC nodes in partnership with AWS Wavelength and Google Cloud.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
