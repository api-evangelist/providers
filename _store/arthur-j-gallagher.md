---
aid: arthur-j-gallagher
name: Arthur J. Gallagher
description: Arthur J. Gallagher & Co. is a global insurance brokerage, risk management, and consulting firm headquartered in Rolling Meadows, Illinois. The company provides insurance brokerage, risk management, employee benefits, and retirement services to clients worldwide. Its subsidiaries include Gallagher Security (which offers the Command Centre REST API for physical security integration) and Gallagher Bassett (which offers claims management APIs for third-party claims administration). Arthur J. Gallagher serves clients in over 130 countries through its international network of brokers and offices.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/arthur-j-gallagher/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-19'
specificationVersion: '0.19'
type: Index
tags:
  - Insurance
  - Brokerage
  - Risk Management
  - Claims Management
  - Security
  - Benefits
apis:
  - aid: arthur-j-gallagher:command-centre-api
    name: Gallagher Command Centre REST API
    description: REST API providing HTTP functions to query and integrate with the Gallagher Command Centre physical security platform. Enables third-party systems to interact with access control, alarm monitoring, visitor management, and site management features. Supports on-premise and cloud gateway connectivity since version 8.60.
    humanURL: https://gallaghersecurity.github.io/
    baseURL: https://localhost:8904/api
    tags:
      - Access Control
      - Security
      - Alarms
      - Integration
      - Physical Security
    properties:
      - type: Documentation
        url: https://gallaghersecurity.github.io/
      - type: OpenAPI
        url: openapi/gallagher-command-centre-api.yml
      - type: GitHubRepository
        url: https://github.com/GallagherSecurity/cc-rest-docs
  - aid: arthur-j-gallagher:gallagher-bassett-api
    name: Gallagher Bassett Claims Management API
    description: API for integrating with Gallagher Bassett claims management services. Gallagher Bassett is a global third-party claims administrator and subsidiary of Arthur J. Gallagher, providing workers compensation, liability, property, and disability claims management.
    humanURL: https://developer.gallagherbassett.com/
    baseURL: https://api.gallagherbassett.com
    tags:
      - Claims
      - Insurance
      - Risk Management
      - Workers Compensation
    properties:
      - type: Documentation
        url: https://developer.gallagherbassett.com/
common:
  - type: Portal
    url: https://www.ajg.com/
    title: Arthur J. Gallagher Website
  - type: Documentation
    url: https://gallaghersecurity.github.io/
    title: Gallagher Security Developer Docs
  - type: Portal
    url: https://developer.gallagherbassett.com/
    title: Gallagher Bassett Developer Portal
  - type: GitHubOrganization
    url: https://github.com/GallagherSecurity
    title: Gallagher Security GitHub
  - type: Features
    data:
      - name: Command Centre REST API
        description: Full REST API for integrating with Gallagher's Command Centre physical security system, enabling access control, alarm management, visitor tracking, and event monitoring from third-party applications.
      - name: Cloud API Gateway
        description: Internet-based secure connectivity to Command Centre servers, enabling remote integration without VPN through the Gallagher Cloud API Gateway.
      - name: Mobile Connect SDK
        description: SDK for developing mobile applications that connect to Gallagher Command Centre for access control, including code samples and technical guides.
      - name: Claims Management API
        description: Gallagher Bassett API for programmatic integration with third-party claims administration workflows including claim submission, status tracking, and reporting.
  - type: UseCases
    data:
      - name: Physical Security Integration
        description: Technology partners integrate Command Centre REST API to build visitor management systems, CCTV integrations, and security operations center dashboards.
      - name: Access Control Automation
        description: Corporate IT teams integrate access control with HR systems to automatically provision and deprovision employee badge access based on employment status changes.
      - name: Claims Processing Integration
        description: Enterprise clients integrate Gallagher Bassett's claims API with their ERP and HR systems to automate workers compensation and liability claims submission and tracking.
      - name: Incident Response
        description: Security operations teams use the Command Centre API to correlate access events with alarm triggers for automated incident response and reporting.
  - type: Integrations
    data:
      - name: Gallagher Security Technology Partner Program
        description: Formal partner program for companies integrating with Command Centre, providing access to proprietary technology resources, software licenses, and technical support.
      - name: Gallagher Bassett Claims Administration
        description: Third-party administrators and enterprise clients integrate with Gallagher Bassett for outsourced claims management workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
