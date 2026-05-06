---
aid: cisco-secure-client
name: Cisco Secure Client
url: https://raw.githubusercontent.com/api-evangelist/cisco-secure-client/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
tags:
  - Endpoint Security
  - Remote Access
  - Security
  - VPN
  - Zero Trust
description: Cisco Secure Client (formerly AnyConnect) is the unified endpoint agent for Cisco security and connectivity, delivering VPN, Zero Trust Network Access, endpoint posture, network visibility, and secure web access from a single installer. Programmatic interfaces are exposed indirectly through Cisco Secure Firewall (ASA, FTD), Cisco Identity Services Engine (ISE), Cisco Secure Access, Umbrella, and Duo. There is no single public REST surface for the client itself; integration is achieved through profile XML packages, MDM-deployed configuration, and the management plane APIs exposed by these adjacent Cisco services.
apis:
  - aid: cisco-secure-client:secure-firewall-management-api
    name: Cisco Secure Firewall Management Center API
    tags:
      - ASA
      - Firewall
      - FTD
      - Management
      - VPN
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cisco.com/docs/secure-firewall-management-center-api/
    properties:
      - url: https://developer.cisco.com/docs/secure-firewall-management-center-api/
        type: Documentation
    description: The Cisco Secure Firewall Management Center API configures remote-access VPN gateways, group policies, and Secure Client profiles distributed to endpoints. Authentication uses a token generated via the generatetoken endpoint and passed as the X-auth-access-token header on subsequent calls.
  - aid: cisco-secure-client:ise-ers-api
    name: Cisco ISE ERS API
    tags:
      - ERS
      - Identity
      - ISE
      - NAC
      - Posture
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cisco.com/docs/identity-services-engine/
    properties:
      - url: https://developer.cisco.com/docs/identity-services-engine/
        type: Documentation
    description: The Cisco Identity Services Engine External RESTful Services (ERS) API manages the network access control plane that Secure Client integrates with for posture assessment and policy enforcement. Endpoints cover endpoint identity groups, posture conditions, and authorization policies.
  - aid: cisco-secure-client:umbrella-api
    name: Cisco Umbrella API
    tags:
      - DNS
      - Roaming
      - Secure Web Gateway
      - Umbrella
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.umbrella.com
    humanURL: https://developer.cisco.com/docs/cloud-security/
    properties:
      - url: https://developer.cisco.com/docs/cloud-security/
        type: Documentation
    description: The Cisco Umbrella API exposes the cloud-delivered DNS, secure web gateway, and roaming protection services that integrate with the Secure Client Umbrella module. Authentication uses OAuth 2.0 client credentials and endpoints cover deployments, policies, reports, and destination lists.
  - aid: cisco-secure-client:duo-admin-api
    name: Cisco Duo Admin API
    tags:
      - Authentication
      - Duo
      - MFA
      - Zero Trust
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://duo.com/docs/adminapi
    properties:
      - url: https://duo.com/docs/adminapi
        type: Documentation
    description: The Duo Admin API configures multi-factor authentication policies, users, groups, and integrations used by Secure Client deployments for ZTNA and adaptive authentication. Authentication uses an HMAC signature scheme over the request and integration keys.
  - aid: cisco-secure-client:secure-access-api
    name: Cisco Secure Access API
    tags:
      - SASE
      - Secure Access
      - SSE
      - ZTNA
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cisco.com/docs/cloud-security/secure-access/
    properties:
      - url: https://developer.cisco.com/docs/cloud-security/secure-access/
        type: Documentation
    description: The Cisco Secure Access API is the management interface for Cisco's converged SSE platform that Secure Client connects to as a SASE endpoint agent. Endpoints cover network tunnels, ZTNA application definitions, posture profiles, and reporting.
common:
  - type: Portal
    url: https://developer.cisco.com/
  - type: Documentation
    url: https://www.cisco.com/c/en/us/support/security/secure-client-5/series.html
  - type: Getting Started
    url: https://developer.cisco.com/docs/secure-client/getting-started/
  - type: Change Log
    url: https://www.cisco.com/c/en/us/td/docs/security/vpn_client/anyconnect/Cisco-Secure-Client-5/release/notes/release-notes-cisco-secure-client-5.html
  - type: Support
    url: https://www.cisco.com/c/en/us/support/index.html
  - type: Status
    url: https://status.cisco.com/
  - type: Community
    url: https://community.cisco.com/
  - type: Terms of Service
    url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/end-user-license-agreement.html
  - type: Privacy Policy
    url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
  - type: JSON-LD
    url: json-ld/cisco-secure-client-context.jsonld
  - type: Spectral
    url: rules/cisco-secure-client-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cisco-secure-client-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
