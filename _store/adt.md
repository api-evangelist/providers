---
aid: adt
url: https://raw.githubusercontent.com/api-evangelist/adt/refs/heads/main/apis.yml
modified: '2026-04-19'
apis:
  - name: ADT+ Platform API
    description: The ADT+ Platform API provides programmatic access to ADT's smart home security platform, enabling management of security devices, sensors, cameras, locks, and automation rules. Supports real-time status monitoring, arming and disarming, video clip retrieval, and alert management for residential and commercial security systems.
    humanURL: https://www.adt.com/smart-home
    baseURL: https://api.adt.com/v1
    tags:
      - Automation
      - Monitoring
      - Security
      - Smart Home
    properties:
      - type: Documentation
        url: https://www.adt.com/smart-home
      - type: OpenAPI
        url: openapi/adt-platform-api-openapi.yml
      - type: JSONSchema
        url: json-schema/
      - type: JSONStructure
        url: json-structure/
      - type: JSONLD
        url: json-ld/adt-platform-api-context.jsonld
      - type: SpectralRules
        url: rules/adt-spectral-rules.yml
      - type: NaftikoCapability
        url: capabilities/shared/platform-api.yaml
      - type: Vocabulary
        url: vocabulary/adt-vocabulary.yaml
  - name: ADT Business API
    description: The ADT Business API provides commercial security management capabilities including multi-site access control, commercial alarm management, video surveillance integration, and security event monitoring for small to enterprise business customers.
    humanURL: https://www.adt.com/business
    baseURL: https://api.adt.com/business/v1
    tags:
      - Access Control
      - Business Security
      - Commercial
      - Video Surveillance
    properties:
      - type: Documentation
        url: https://www.adt.com/business
      - type: OpenAPI
        url: openapi/adt-business-api-openapi.yml
      - type: JSONSchema
        url: json-schema/
      - type: JSONStructure
        url: json-structure/
      - type: JSONLD
        url: json-ld/adt-business-api-context.jsonld
      - type: SpectralRules
        url: rules/adt-spectral-rules.yml
      - type: NaftikoCapability
        url: capabilities/home-security-management.yaml
      - type: Vocabulary
        url: vocabulary/adt-vocabulary.yaml
common:
  - type: Website
    url: https://www.adt.com
  - type: Portal
    url: https://www.adt.com/smart-home
  - type: Support
    url: https://www.adt.com/support
  - type: Blog
    url: https://www.adt.com/about-adt/news
  - type: TermsOfService
    url: https://www.adt.com/terms-of-service
  - type: PrivacyPolicy
    url: https://www.adt.com/privacy-policy
  - type: Login
    url: https://www.adt.com/login
  - type: SignUp
    url: https://www.adt.com/get-a-quote
  - type: Features
    data:
      - name: Professional Security Monitoring
        description: 24/7 professional monitoring center that responds to alarms, contacts emergency services, and alerts homeowners.
      - name: Smart Home Automation
        description: Programmatic control of lights, locks, thermostats, and smart plugs integrated with the ADT+ security platform.
      - name: Video Surveillance and Clips
        description: Access and retrieve recorded video clips from indoor, outdoor, and doorbell cameras via API.
      - name: Remote Arm and Disarm
        description: Remotely arm and disarm security systems and zones through authenticated API calls.
      - name: Sensor and Device Status
        description: Real-time status monitoring of door sensors, motion detectors, smoke detectors, and flood sensors.
      - name: Access Control Management
        description: Manage smart locks, access codes, and entry permissions for residential and commercial properties.
      - name: Alarm Event Notifications
        description: Receive real-time webhook notifications for alarm events, zone violations, and system status changes.
      - name: Multi-Site Management
        description: Manage multiple properties and security systems from a single API integration for commercial customers.
  - type: UseCases
    data:
      - name: Home Automation Integration
        description: Integrate ADT security with third-party home automation platforms like Google Home, Amazon Alexa, and Apple HomeKit.
      - name: Property Management
        description: Manage access codes and security schedules for rental properties, vacation homes, and commercial buildings.
      - name: Insurance Integration
        description: Share security monitoring data with insurance providers for smart home insurance discount programs.
      - name: Emergency Response Automation
        description: Trigger automated emergency responses, notifications, and camera recordings when alarms are triggered.
      - name: Business Intelligence
        description: Analyze security events, access patterns, and alarm history for business operational insights.
      - name: Contractor Access Management
        description: Issue temporary access codes for service contractors with time-limited entry permissions.
  - type: Integrations
    data:
      - name: Google Nest
        description: Integration with Google Nest thermostats, cameras, and smart displays through ADT+ with Google partnership.
      - name: Amazon Alexa
        description: Voice control of ADT security system including arm, disarm, and status queries via Amazon Alexa.
      - name: Google Assistant
        description: Voice control and smart home automation via Google Assistant and Nest Hub displays.
      - name: Z-Wave
        description: Z-Wave wireless protocol support for smart locks, lights, thermostats, and other smart home devices.
      - name: Apple HomeKit
        description: HomeKit-compatible devices that integrate with ADT security ecosystem.
      - name: Ring
        description: Integration with Ring video doorbells and cameras as complementary security devices.
      - name: Lutron
        description: Smart lighting control integration with Lutron Caseta and RadioRA systems.
description: ADT is a provider of monitored security, interactive home and business automation, and related monitoring services for residential and small business customers across the United States and Canada. ADT offers smart home security systems, professional monitoring, video surveillance, access control, and automation integrations with Google Nest, Amazon Alexa, and Z-Wave smart home devices through the ADT+ platform.
name: ADT
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
created: '2024-01-01'
specificationVersion: '0.19'
tags:
  - Access Control
  - Automation
  - Home Security
  - IoT
  - Monitoring
  - Security
  - Smart Home
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
