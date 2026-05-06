---
aid: verizon
url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/apis.yml
apis:
  - aid: verizon:verizon-5g-edge
    name: Verizon 5G Edge
    tags:
      - Wireless
    humanURL: https://www.verizon.com/business/5g-edge-portal/api-documentation.html
    properties:
      - url: https://www.verizon.com/business/5g-edge-portal/api-documentation.html
        type: Documentation
      - url: https://www.verizon.com/business/5g-edge-portal/index.html
        name: Portal
        type: Portal
      - url: https://www.verizon.com/business/5g-edge-portal/partners.html
        name: Partners
        type: Partners
      - url: https://www.verizon.com/business/5g-edge-portal/faq.html
        name: FAQ
        type: FAQ
      - url: https://www.verizon.com/business/solutions/5g/edge-computing/developer-form/
        name: Developer Form | Verizon
        type: Newsletter
      - url: https://www.verizon.com/business/5g-edge-portal/legal.html
        name: Legal
        type: TermsOfService
      - url: https://www.verizon.com/about/privacy/
        name: Privacy Policy Home Page | About Verizon
        type: PrivacyPolicy
      - url: https://mblogin.verizonwireless.com/account/business/login?appGroup=TSD&goto=https%3A%2F%2Fmblogin.verizonwireless.com%2Fvzauth%2Foauth2%2Fauthorize%3Fscope%3Dopenid%26response_type%3Did_token%26realm%3D%2Fvzwmb%26redirect_uri%3Dhttps%3A%2F%2Fwww.verizon.com%2Fbusiness%2F5g-edge-portal%2Fredirect%26nonce%3DYmMyOWFhNjItZDU0ZS00Mzg1LTg2NzYtYTYyMjYzYWU4ZWFiLTIxNTA0MCxodHRwczovL3d3dy52ZXJpem9uLmNvbS9idXNpbmVzcy81Zy1lZGdlLXBvcnRhbC9hY2NvdW50L2xvZ2luP2E9MC41NTIyNzE1NDg0MTc3OTk4%26client_id%3Dmdp_agent%26response_mode%3Dform_post&realm=%2Fvzwmb
        name: Verizon Business Account Login
        type: Login
      - url: https://www.verizon.com/business/5g-edge-portal/sign-up.html?adobe_mc=MCMID%3D30667738221820930504169506415661990520%7CMCORGID%3D7ED836675AB3A4860A495CAD%2540AdobeOrg%7CTS%3D1732034957&_gl=1*t9c1hx*_ga*MTYxNzc2Mjc2MS4xNzMyMDM0OTU3*_ga_12R1DX1LX7*MTczMjAzNDk1Ny4xLjAuMTczMjAzNDk1Ny42MC4wLjA.
        name: Sign up
        type: SignUp
      - url: https://www.verizon.com/business/products/contact-center-cx/voice-api/
        name: 'Voice APIs: Communication Platform as a Service | Verizon'
        type: Documentation
    description: Software Management Services API lets customers manage, schedule and distribute software updates to eligible 4G and 5G Internet of Things devices.
  - aid: verizon:thingspace
    name: Verizon ThingSpace
    tags:
      - IoT
      - Device Management
      - Connectivity
      - Wireless
    humanURL: https://thingspace.verizon.com
    properties:
      - url: https://thingspace.verizon.com
        name: Verizon ThingSpace
        type: Documentation
      - type: APIReference
        url: https://thingspace.verizon.com/resources/documentation/connectivity/API_Reference/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/openapi/verizon-thingspace-connectivity-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-schema/thingspace-connectivity-account-information-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-schema/thingspace-connectivity-device-information-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-schema/thingspace-connectivity-device-id-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-schema/thingspace-connectivity-device-list-request-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-schema/thingspace-connectivity-device-list-response-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-schema/thingspace-connectivity-activate-devices-request-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-schema/thingspace-connectivity-deactivate-devices-request-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-schema/thingspace-connectivity-send-sms-request-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-schema/thingspace-connectivity-callback-summary-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-schema/thingspace-connectivity-device-request-response-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-structure/thingspace-connectivity-account-information-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-structure/thingspace-connectivity-device-information-structure.json
      - type: JSON-LD
        url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/json-ld/verizon-thingspace-connectivity-context.jsonld
      - type: SDK
        url: https://github.com/sdks-io/verizon-apis-python-sdk
        title: Python SDK
      - type: SDK
        url: https://packagist.org/packages/sdksio/verizon-apis-sdk
        title: PHP SDK
    description: ThingSpace gives organizations of all sizes all the tools to build IoT solutions or use end-to-end solutions to solve business problems.
  - aid: verizon:communications-platform-as-a-service
    name: Verizon Communications Platform as a Service (CPaaS)
    tags: []
    humanURL: https://www.verizon.com/business/en-gb/products/contact-center-cx-solutions/communications-platform-as-a-service/
    properties: []
    description: Available exclusively for IP Contact Center (IPCC) customers, our Communications Platform as a Service (CPaaS) offering provides a set of APIs that you can leverage to build customized solutions for inbound and outbound IP interactive voice response (IPIVR) and call detail reporting.
  - aid: undefined:verizon-inventory-management
    name: Verizon Inventory Management
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/service-management-apis/dep-inventory-management-tmf
    properties:
      - type: Documentation
        url: https://developers.verizon.com/#/apis/ns/products/service-management-apis/dep-inventory-management-tmf
    description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These APIs are bi-directional, helping to keep the information accessed from both Verizon and customer systems synchronized.
  - aid: undefined:verizon-incident-management
    name: Verizon Incident Management
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/service-management-apis/dep-incident-management-tmf
    properties: []
    description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These APIs are bi-directional, helping to keep the information accessed from both Verizon and customer systems synchronized.
  - aid: undefined:verizon-change-management
    name: Verizon Change Management
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/service-management-apis/dep-change-management-tmf
    properties: []
    description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These APIs are bi-directional, helping to keep the information accessed from both Verizon and customer systems synchronized.
  - aid: undefined:verizon-event-management
    name: Verizon Event Management
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/service-management-apis/dep-event-management-tmf
    properties: []
    description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These APIs are bi-directional, helping to keep the information accessed from both Verizon and customer systems synchronized.
  - aid: undefined:verizon-problem-management
    name: Verizon Problem Management
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/service-management-apis/dep-problem-management-tmf
    properties: []
    description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These APIs are bi-directional, helping to keep the information accessed from both Verizon and customer systems synchronized.
  - aid: undefined:verizon-order-management
    name: Verizon Order Management
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/service-management-apis/dep-order-management-tmf
    properties: []
    description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These APIs are bi-directional, helping to keep the information accessed from both Verizon and customer systems synchronized.
  - aid: undefined:verizon-billing-management
    name: Verizon Billing Management
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/service-management-apis/dep-billing-management-tmf
    properties: []
    description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These APIs are bi-directional, helping to keep the information accessed from both Verizon and customer systems synchronized.
  - aid: undefined:verizon-dynamic-bandwidth-apis
    name: Verizon Dynamic Bandwidth APIs
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/private-ip-apis/dynamic-bandwidth-apis
    properties: []
    description: These innovative network provisioning API solutions can be deployed in the enterprises network eco-system to drive real-time network adjustments according to their changing business needs. Taking an agile approach to network provisioning, it can aid in dynamically allocating/de-allocating and scaling the bandwidth requirements as the need arises.
  - aid: undefined:dynamic-network-manager-dnm-standardized-apis
    name: Dynamic Network Manager (DNM) Standardized APIs
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/private-ip-apis/dynamic-network-manager-mef-1
    properties: []
    description: MEF API Standards distinguish between Envelope APIs and related Payload schemas. The Envelope APIs can work with multiple Payload Schemas, in this case the Private IP Payload Schema. The MEF-76 Specification describes APIs for service control functions (e.g. inventory, parameter change requests, notifications etc.).
  - aid: undefined:secure-cloud-interconnect-apis-utilization
    name: Secure Cloud Interconnect APIs Utilization
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/secure-cloud-interconnect-apis/SCI-Utilization-API
    properties: []
    description: SCI supports APIs to fetch data consumption and bandwidth utilization measurements for the SCI connection to the cloud.
  - aid: undefined:secure-cloud-interconnect-apis-billing-usage
    name: Secure Cloud Interconnect APIs Billing Usage
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/secure-cloud-interconnect-apis/SCI-Billing-Usage-API
    properties: []
    description: SCI supports APIs to fetch data consumption and bandwidth utilization measurements for the SCI connection to the cloud.
  - aid: undefined:dynamic-network-manager-dnm-standardized-apis
    name: Dynamic Network Manager (DNM) Standardized APIs
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/internet-dedicated-services-apis/dynamic-network-manager-mef-2
    properties: []
    description: MEF API Standards distinguish between Envelope APIs and related Payload schemas. The Envelope APIs can work with multiple Payload Schemas, in this case the DNM APIs to support IDS. The MEF-76 Specification describes APIs for service control functions (e.g. inventory, parameter change requests, notifications etc.).
  - aid: undefined:dynamic-network-manager-dnm-standardized-apis
    name: Dynamic Network Manager (DNM) Standardized APIs
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/e-line-services-apis/dynamic-network-manager-mef-3
    properties: []
    description: MEF API Standards distinguish between Envelope APIs and related Payload schemas. The Envelope APIs can work with multiple Payload Schemas, in this case the DNM APIs to support E-Line. The MEF-76 Specification describes APIs for service control functions (e.g. inventory, parameter change requests, notifications etc.).
  - aid: undefined:dynamic-network-manager-dnm-standardized-apis
    name: Dynamic Network Manager (DNM) Standardized APIs
    tags: []
    humanURL: https://developers.verizon.com/#/apis/ns/products/e-lan-services-apis/dynamic-network-manager-mef-4
    properties: []
    description: MEF API Standards distinguish between Envelope APIs and related Payload schemas. The Envelope APIs can work with multiple Payload Schemas, in this case the DNM APIs to support E-LAN . The MEF-76 Specification describes APIs for service control functions (e.g. inventory, parameter change requests, notifications etc.).
name: Verizon
tags:
  - Wireless
  - Telecommunications
  - IoT
  - 5G
  - Enterprise
  - Network APIs
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://www.verizon.com
    type: Website
  - url: https://developers.verizon.com/
    name: Portal
    type: Portal
  - url: https://developers.verizon.com/#/apis/ns/documentation/help
    name: Help - Verizon API Marketplace
    type: Support
  - url: https://developers.verizon.com/#/apis/ns/documentation/frequently-asked-questions
    name: FAQ - Verizon API Marketplace
    type: FAQ
  - url: https://secure.verizon.com/signin?goto=https://developers.verizon.com/apis/sec/v1/login
    name: My Verizon login. Sign in to your Verizon Wireless or Fios Account
    type: Login
  - url: https://secure.verizon.com/account/register/start?goto=https%3A%2F%2Fdevelopers.verizon.com%2Fapis%2Fsec%2Fv1%2Flogin
    name: Register a service
    type: SignUp
  - url: https://www.verizon.com/about/privacy/
    type: PrivacyPolicy
  - url: https://www.verizon.com/about/terms-conditions/
    type: TermsOfService
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/rules/verizon-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/vocabulary/verizon-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/capabilities/iot-device-management.yaml
  - type: Features
    data:
      - 'Verizon: API access via partner / B2B contracts only'
      - No public API pricing published — contact enterprise sales
      - Verizon Network APIs (5G, location, identity) sold via the Verizon Open Innovation API portal with custom enterprise contracts.
    sources:
      - https://thingspace.verizon.com/
      - https://www.verizon.com/business/products/internet-of-things/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: IoT Fleet Management
        description: Manage large-scale IoT device fleets with activation, deactivation, and status monitoring.
      - name: Remote Device Management
        description: Remotely diagnose, configure, and update IoT devices over Verizon's wireless network.
      - name: Enterprise Network Automation
        description: Automate network bandwidth provisioning and IT service management with TM Forum APIs.
      - name: 5G Edge Applications
        description: Build ultra-low-latency applications on Verizon's 5G edge computing infrastructure.
      - name: Contact Center Modernization
        description: Build customized IVR and call routing solutions with Verizon's CPaaS Voice API.
  - type: Integrations
    data:
      - name: AWS Wavelength
        description: Deploy 5G Edge applications on Verizon MEC nodes through AWS Wavelength partnership.
      - name: Google Cloud MEC
        description: Build edge-native applications through Verizon and Google Cloud edge computing integration.
      - name: ITSM Platforms
        description: Connect TM Forum service management APIs to ServiceNow and other ITSM platforms.
      - name: IoT Platforms
        description: Integrate ThingSpace device management with enterprise IoT platforms and data lakes.
created: '2024-11-19'
modified: '2026-05-04'
description: Verizon is a leading telecommunications company providing wireless, wireline, broadband, and global enterprise services. Verizon offers developer APIs for IoT device management via ThingSpace, 5G edge computing, TM Forum service management, dynamic network bandwidth, and communications platform APIs for contact center and SMS solutions.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
