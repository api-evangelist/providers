---
aid: amazon-workspaces-web
name: Amazon WorkSpaces Web
description: Amazon WorkSpaces Web is a purpose-built, low-cost, fully managed service that enables secure browser access to internal websites and SaaS applications. It provides persistent browser sessions with built-in security controls, preventing users from downloading content to local devices while maintaining a seamless browsing experience. The service offers 58 API operations for managing portals, user settings, browser policies, network settings, trust stores, and IP access controls.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - End User Computing
  - Secure Browser
  - Virtual Desktop
  - Zero Trust
url: https://raw.githubusercontent.com/api-evangelist/amazon-workspaces-web/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-workspaces-web:amazon-workspaces-web-api
    name: Amazon WorkSpaces Web API
    description: The Amazon WorkSpaces Web API provides programmatic access to create and manage web portals, network settings, user access logging, user settings, browser settings, and trust store configurations for secure browser deployments. 58 operations covering portals, user settings, browser policies, network settings, trust stores, and IP access controls.
    humanURL: https://aws.amazon.com/workspaces/web/
    baseURL: https://workspaces-web.amazonaws.com
    tags:
      - AWS
      - End User Computing
      - Secure Browser
      - Zero Trust
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/
      - type: APIReference
        url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/
      - type: GettingStarted
        url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/workspaces/web/pricing/
      - type: FAQ
        url: https://aws.amazon.com/workspaces/web/faqs/
      - type: OpenAPI
        url: openapi/amazon-workspaces-web-openapi-original.yaml
      - type: JSONSchema
        url: json-schema/workspaces-web-portal-schema.json
      - type: JSONLD
        url: json-ld/amazon-workspaces-web-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/workspaces/web/
  - type: Documentation
    url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/
  - type: Console
    url: https://console.aws.amazon.com/workspaces-web/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: SpectralRules
    url: rules/amazon-workspaces-web-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-workspaces-web-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/secure-browser-management.yaml
  - type: Features
    data:
      - name: Secure Browser Portals
        description: Purpose-built browser portals that provide secure access to internal websites and SaaS applications without VPN requirements.
      - name: Data Loss Prevention Controls
        description: Built-in controls to prevent users from downloading, uploading, printing, or copying content to local devices.
      - name: Browser Policy Management
        description: Configurable browser policies to control features like clipboard access, printing, and file transfers at the organizational level.
      - name: Network Isolation
        description: VPC-based network settings to isolate browser sessions within enterprise network boundaries with security group controls.
      - name: Trust Store Management
        description: SSL certificate trust stores for validating internal website certificates in secure browser sessions.
      - name: IP Access Controls
        description: IP-based access rules to restrict portal access to specific corporate IP ranges or geographic locations.
      - name: User Access Logging
        description: Detailed session logging for audit and compliance purposes with integration to Kinesis data streams.
      - name: Identity Integration
        description: SAML-based identity provider integration for single sign-on to secure browser portal sessions.
  - type: UseCases
    data:
      - name: Secure Third-Party Access
        description: Provide contractors and third-party vendors secure access to internal tools without requiring VPN or device enrollment.
      - name: BYOD Security
        description: Enable bring-your-own-device policies while maintaining security controls over corporate application access.
      - name: Compliance-Driven Browsing
        description: Enforce data handling compliance requirements through browser-level controls for regulated industries.
      - name: SaaS Application Security
        description: Provide secure, controlled access to SaaS applications with session recording and data exfiltration prevention.
      - name: Developer Sandbox Environments
        description: Create isolated browser environments for development and testing of internal web applications.
  - type: Integrations
    data:
      - name: AWS IAM Identity Center
        description: Single sign-on integration for WorkSpaces Web portal authentication.
      - name: Amazon Kinesis
        description: User access logging integration to stream session data for analysis.
      - name: AWS KMS
        description: Encryption key management for browser settings and data at rest.
      - name: Amazon VPC
        description: VPC integration for network isolation of browser sessions.
      - name: AWS Certificate Manager
        description: Certificate management for trust store and SSL configurations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
