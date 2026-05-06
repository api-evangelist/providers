---
aid: unisys
url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/apis.yml
apis:
  - aid: unisys:unisys-stealth-ecoapi
    name: Unisys Stealth EcoAPI
    tags:
      - Security
      - Zero Trust
      - Network Security
      - Endpoint Isolation
      - Cybersecurity
    humanURL: https://stealthsecurity.unisys.com
    baseURL: https://stealth-server:8448
    properties:
      - url: https://stealthsecurity.unisys.com/resources/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/openapi/unisys-stealth-ecoapi-openapi.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/rules/unisys-stealth-spectral-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/capabilities/shared/unisys-stealth-ecoapi.yaml
        type: NaftikoCapability
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/capabilities/zero-trust-security.yaml
        type: NaftikoCapability
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/vocabulary/unisys-vocabulary.yaml
        type: Vocabulary
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/json-ld/unisys-context.jsonld
        type: JSONLDContext
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/json-schema/unisys-stealth-role-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/json-schema/unisys-isolation-request-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/json-schema/unisys-unisolation-request-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/json-schema/unisys-action-response-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/json-structure/unisys-stealth-role-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/json-structure/unisys-isolation-request-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/json-structure/unisys-action-response-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/examples/unisys-stealth-isolate-endpoint-example.json
        type: Example
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/examples/unisys-stealth-isolate-user-example.json
        type: Example
      - url: https://raw.githubusercontent.com/api-evangelist/unisys/refs/heads/main/examples/unisys-stealth-get-roles-example.json
        type: Example
    description: The Unisys Stealth EcoAPI enables security teams and automation platforms to integrate with Unisys Stealth zero trust network segmentation. Using the EcoAPI, teams can programmatically isolate and un-isolate endpoints and users from the Stealth network in response to security events, retrieve Stealth role configurations, and manage dynamic endpoint isolation workflows. The API uses HTTP Basic authentication against a configurable Stealth server endpoint.
    data:
      - name: Features
        data:
          - name: Dynamic Endpoint Isolation
            description: Programmatically isolate compromised endpoints from the Stealth zero trust network in real time
          - name: Dynamic User Isolation
            description: Isolate specific users from network access without disrupting other endpoints or users
          - name: Combined Isolation
            description: Simultaneously isolate both an endpoint and associated user in a single API call
          - name: Role-Based Isolation Policies
            description: Apply specific Stealth isolation role policies during isolation for granular containment
          - name: Un-Isolation and Restoration
            description: Restore isolated endpoints and users to normal Stealth network access after incident resolution
          - name: Stealth Role Retrieval
            description: Retrieve available Stealth isolation role configurations for policy selection
          - name: SOAR/SIEM Integration
            description: Integrate with security orchestration platforms for automated incident response workflows
      - name: UseCases
        data:
          - name: Incident Response Containment
            description: Security operations teams isolate compromised endpoints immediately upon alert detection
          - name: SOAR Automation
            description: SOAR platforms trigger Stealth isolation automatically based on SIEM threat detection rules
          - name: Insider Threat Containment
            description: Isolate specific users when suspicious activity is detected while preserving investigation access
          - name: Ransomware Containment
            description: Rapidly isolate infected endpoints to prevent lateral movement and ransomware spread
          - name: Compliance-Driven Isolation
            description: Enforce regulatory compliance by isolating non-compliant endpoints from sensitive network segments
      - name: Integrations
        data:
          - name: SIEM Platforms
            description: Integrate with Splunk, IBM QRadar, and Microsoft Sentinel for automated threat-triggered isolation
          - name: SOAR Platforms
            description: Connect with Palo Alto XSOAR, Splunk SOAR, and other orchestration platforms
          - name: Vulnerability Management
            description: Trigger isolation based on critical vulnerability scan results
          - name: Endpoint Detection and Response
            description: Integrate with EDR solutions to trigger Stealth isolation for confirmed threats
name: Unisys
tags:
  - Security
  - Zero Trust
  - Network Security
  - IT Services
  - Cybersecurity
  - Enterprise Technology
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-06'
modified: '2026-05-03'
position: Consumer
description: Unisys is a global information technology company that provides specialized solutions integrated with leading-edge security. Unisys delivers digital workplace services, cloud and infrastructure services, and enterprise computing solutions including the ClearPath mainframe platform and the Unisys Stealth zero trust security suite. Unisys serves clients across industries including financial services, government, healthcare, and transportation.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
