---
aid: symantec
name: Symantec
description: Symantec (now part of Broadcom) is a leading enterprise cybersecurity company providing endpoint security, threat detection, data loss prevention, identity security, and network protection products. Symantec offers REST APIs for Endpoint Protection Manager (SEPM), Endpoint Security Cloud (SES), Endpoint Detection and Response (EDR), Data Loss Prevention (DLP), and the Integrated Cyber Defense Manager (ICDm) platform.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Broadcom
  - Cybersecurity
  - DLP
  - EDR
  - Endpoint Protection
  - Endpoint Security
  - Security
  - Symantec
url: https://raw.githubusercontent.com/api-evangelist/symantec/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: symantec:sepm-api
    name: Symantec Endpoint Protection Manager API
    description: The SEPM REST API enables programmatic access to Symantec Endpoint Protection Manager for managing computers, groups, policies, and server configuration. Requires OAuth 2.0 authentication via the SEPM identity endpoint. Base URL is https://{sepm-host}:8446/sepm/api/v1.
    humanURL: https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-protection/all/APIsSEP/Symantec-Endpoint-Security-API-commands1.html
    baseURL: https://{sepm-host}:8446/sepm/api/v1
    properties:
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-protection/all/APIsSEP/Symantec-Endpoint-Security-API-commands1.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/symantec/refs/heads/main/openapi/symantec-sepm-api-openapi.yml
      - type: Documentation
        url: https://apidocs.symantec.com/home/SAEP
    tags:
      - Computers
      - Endpoint Protection
      - Groups
      - Policies
      - Security Management
      - SEPM
  - aid: symantec:ses-api
    name: Symantec Endpoint Security API
    description: The Symantec Endpoint Security (SES) REST API provides access to cloud-based endpoint security management including device inventory, threat events, incident management, and behavioral analytics. Requires OAuth 2.0 authentication. Documentation at apidocs.securitycloud.symantec.com.
    humanURL: https://apidocs.securitycloud.symantec.com/
    tags:
      - Behavioral Analytics
      - Cloud Security
      - Devices
      - Endpoint Security
      - Events
      - Incidents
      - SES
    properties:
      - type: Documentation
        url: https://apidocs.securitycloud.symantec.com/
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-security/sescloud/APIs/accessing-the-api-reference-v125094769-d4155e11.html
  - aid: symantec:symantec-edr-api
    name: Symantec Endpoint Detection and Response API
    description: The Symantec EDR REST API enables programmatic access to endpoint detection and response capabilities including incident management, threat hunting, forensics, and entity queries. Uses OAuth 2.0 with client credentials grant type.
    humanURL: https://apidocs.symantec.com/home/SymantecEDR_4.2
    tags:
      - EDR
      - Endpoint Security
      - Forensics
      - Incidents
      - Threat Hunting
    properties:
      - type: Documentation
        url: https://apidocs.symantec.com/home/SymantecEDR_4.2
  - aid: symantec:symantec-dlp-api
    name: Symantec Data Loss Prevention API
    description: The Symantec DLP REST API enables integration with the DLP Enforce platform for incident management, policy management, and data discovery. Supports retrieving incidents, updating remediation status, and managing DLP policies.
    humanURL: https://apidocs.symantec.com/home/DLP15.7
    tags:
      - Compliance
      - DLP
      - Data Loss Prevention
      - Incidents
      - Policy Management
    properties:
      - type: Documentation
        url: https://apidocs.symantec.com/home/DLP15.7
common:
  - type: Website
    url: https://www.broadcom.com/products/cybersecurity/endpoint
  - type: APIDocumentation
    url: https://apidocs.securitycloud.symantec.com/
  - type: APIDocumentation
    url: https://apidocs.symantec.com/
  - type: Documentation
    url: https://techdocs.broadcom.com/us/en/symantec-security-software
  - type: Support
    url: https://support.broadcom.com
  - type: Community
    url: https://community.broadcom.com/symantecenterprise
  - type: GitHub
    url: https://github.com/Symantec
  - type: Login
    url: https://sep.securitycloud.symantec.com
  - type: TermsOfService
    url: https://www.broadcom.com/company/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://www.broadcom.com/company/legal/privacy
  - type: Status
    url: https://status.broadcom.com/services/symantec-endpoint-security-enterprise/
  - type: Blog
    url: https://www.broadcom.com/blog/category/cybersecurity
  - type: TechDocs
    url: https://techdocs.broadcom.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
