---
aid: digicert
url: https://raw.githubusercontent.com/api-evangelist/digicert/refs/heads/main/apis.yml
apis:
  - aid: digicert:digicert-services-api
    name: DigiCert Services API
    tags:
      - Certificates
      - Encryption
      - PKI
      - SSL
      - TLS
    humanURL: https://dev.digicert.com/en/certcentral-apis/services-api.html
    baseURL: https://www.digicert.com/services/v2
    properties:
      - url: https://dev.digicert.com/en/certcentral-apis/services-api.html
        type: Documentation
    description: The DigiCert Services API automates certificate processes to save time and streamline certificate management across the CertCentral platform. Use this API to manage all aspects of your CertCentral account including order, issue, reissue, renew, and revoke for SSL/TLS, code signing, client, and document signing certificates, as well as user, organization, domain, and product management.
  - aid: digicert:digicert-report-library-api
    name: DigiCert Report Library API
    tags:
      - Certificates
      - Encryption
      - Reporting
    humanURL: https://dev.digicert.com/en/certcentral-apis/report-library-api.html
    properties:
      - url: https://dev.digicert.com/en/certcentral-apis/report-library-api.html
        type: Documentation
    description: The DigiCert Report Library API allows users to create and manage custom reports for CertCentral certificate orders, domains, organizations, and account activity. Programmatically schedule, retrieve, and export reports to streamline visibility and auditing of certificate inventories.
  - aid: digicert:digicert-discovery-api
    name: DigiCert Discovery API
    tags:
      - Certificates
      - Discovery
      - Encryption
      - Scanning
    humanURL: https://dev.digicert.com/en/certcentral-apis/discovery-api.html
    properties:
      - url: https://dev.digicert.com/en/certcentral-apis/discovery-api.html
        type: Documentation
    description: The DigiCert Discovery API enables scanning of internal and public-facing networks using sensors to find SSL/TLS certificates regardless of the issuing Certificate Authority. Use the API to manage scan configurations, sensors, divisions, and the certificates that have been discovered to reduce risk from unknown or expired certificates.
  - aid: digicert:digicert-automation-api
    name: DigiCert Automation API
    tags:
      - Automation
      - Certificates
      - Encryption
    humanURL: https://dev.digicert.com/en/certcentral-apis/automation-api.html
    properties:
      - url: https://dev.digicert.com/en/certcentral-apis/automation-api.html
        type: Documentation
    description: The DigiCert Automation API allows configuration of automation profiles and management of automation activities for certificate lifecycle operations. Access all automation features available in CertCentral programmatically without needing to log in to the platform.
  - aid: digicert:digicert-custom-reports-api
    name: DigiCert Custom Reports API
    tags:
      - Certificates
      - Encryption
      - GraphQL
      - Reporting
    humanURL: https://dev.digicert.com/en/certcentral-apis/custom-reports-api.html
    properties:
      - url: https://dev.digicert.com/en/certcentral-apis/custom-reports-api.html
        type: Documentation
    description: The DigiCert Custom Reports API allows generation of customizable and comprehensive data sets by leveraging the powerful GraphQL query language. Build tailored reporting against CertCentral data sources with flexible filtering, sorting, and field selection.
name: Digicert
tags:
  - Certificates
  - Encryption
  - PKI
  - SSL
  - TLS
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - name: DigiCert Developer Portal
    url: https://dev.digicert.com/
    type: Developer
  - name: DigiCert Documentation
    url: https://docs.digicert.com/
    type: Documentation
  - name: DigiCert Knowledge Base
    url: https://knowledge.digicert.com/
    type: Support
  - name: DigiCert
    url: https://www.digicert.com/
    type: Website
  - name: DigiCert Blog
    url: https://www.digicert.com/blog/
    type: Blog
  - name: DigiCert Pricing
    url: https://www.digicert.com/tls-ssl/compare-certificates
    type: Pricing
  - name: DigiCert Trust Center
    url: https://www.digicert.com/trust/
    type: Security
  - name: DigiCert Status
    url: https://status.digicert.com/
    type: Status
  - name: DigiCert Privacy Policy
    url: https://www.digicert.com/legal-repository/privacy-policy
    type: PrivacyPolicy
  - name: DigiCert Master Services Agreement
    url: https://www.digicert.com/legal-repository/master-services-agreement
    type: TermsOfService
  - name: DigiCert GitHub
    url: https://github.com/digicert
    type: GitHub
  - name: DigiCert Changelog
    url: https://dev.digicert.com/en/changelog.html
    type: ChangeLog
created: '2025-01-08'
modified: '2026-04-28'
position: Consumer
description: Digicert is a leading provider of digital security solutions, specializing in SSL/TLS certificates, PKI solutions, and website security. They help organizations of all sizes protect their websites, data, and communications from cyber threats by providing secure encryption and authentication services. Digicert's CertCentral platform exposes a suite of REST and GraphQL APIs for certificate lifecycle management, discovery, automation, and reporting.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
