---
aid: cloudguard
url: https://raw.githubusercontent.com/api-evangelist/cloudguard/refs/heads/main/apis.yml
name: CloudGuard
tags:
  - Check Point
  - CNAPP
  - Cloud Security
  - Compliance
  - CSPM
  - CWPP
  - Posture Management
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-01-01'
modified: '2026-04-26'
position: Consumer
x-type: company
x-company: Check Point Software Technologies
description: Check Point CloudGuard is a Cloud Native Application Protection Platform (CNAPP) that delivers cloud security posture management (CSPM), cloud workload protection (CWPP), code security, network security, and intelligence/CDR capabilities across AWS, Azure, GCP, Alibaba, Oracle, Kubernetes, and on-premises environments. The CloudGuard public REST API (originally Dome9) is used to onboard cloud accounts, run posture assessments, manage compliance bundles, retrieve findings, and configure policies and alerts.
apis:
  - aid: cloudguard:cloudguard-cnapp-api
    name: CloudGuard CNAPP REST API
    tags:
      - CNAPP
      - Cloud Security
      - Compliance
      - Posture
    humanURL: https://docs.cgn.portal.checkpoint.com/reference
    properties:
      - url: https://docs.cgn.portal.checkpoint.com/reference
        type: Documentation
      - url: https://api.dome9.com/v2/swagger.json
        type: OpenAPI
      - url: https://sc1.checkpoint.com/documents/CloudGuard_Dome9/Documentation/API-Authentication.html
        type: Authentication
      - url: https://registry.terraform.io/providers/dome9/dome9/latest/docs
        type: Terraform Provider
    description: The CloudGuard CNAPP REST API (formerly Dome9 v2) is used to onboard AWS, Azure, GCP, Kubernetes, and on-premises accounts; create and run compliance/posture rulesets; retrieve security findings and alerts; manage IAM safety, network policies, and exclusions; and configure notifications and integrations. Authentication is via API key and secret over HTTP Basic.
  - aid: cloudguard:cloudguard-workload-api
    name: CloudGuard Workload Protection (CWPP) API
    tags:
      - Container Security
      - CWPP
      - Image Assurance
      - Kubernetes
    humanURL: https://sc1.checkpoint.com/documents/CloudGuard_Dome9/Documentation/Workload/Overview.htm
    properties:
      - url: https://sc1.checkpoint.com/documents/CloudGuard_Dome9/Documentation/Workload/Overview.htm
        type: Documentation
    description: Workload protection capabilities exposed through the CloudGuard platform for Kubernetes admission control, image assurance/CI scanning, runtime protection, and serverless function security.
  - aid: cloudguard:cloudguard-code-security-api
    name: CloudGuard Code Security (Spectral) API
    tags:
      - Code Security
      - Secrets Detection
      - SAST
    humanURL: https://docs.spectralops.io/
    properties:
      - url: https://docs.spectralops.io/
        type: Documentation
    description: CloudGuard Code Security (formerly Spectral) provides developer-first SAST, infrastructure-as-code scanning, secrets detection, and SCA via CLI and API integrations into CI/CD pipelines.
  - aid: cloudguard:cloudguard-waf-api
    name: CloudGuard WAF API
    tags:
      - API Security
      - WAF
      - Web Application Firewall
    humanURL: https://sc1.checkpoint.com/documents/CloudGuard_AppSec/Documentation/Default.htm
    properties:
      - url: https://sc1.checkpoint.com/documents/CloudGuard_AppSec/Documentation/Default.htm
        type: Documentation
    description: CloudGuard WAF (CloudGuard AppSec) protects web applications and APIs with contextual machine-learning-based threat prevention; the platform exposes management APIs for policy, asset, and event configuration.
  - aid: cloudguard:cloudguard-network-security-api
    name: CloudGuard Network Security API
    tags:
      - Cloud Firewall
      - Network Security
    humanURL: https://www.checkpoint.com/cloudguard/cloud-network-security/
    properties:
      - url: https://www.checkpoint.com/cloudguard/cloud-network-security/
        type: Documentation
    description: CloudGuard Network Security delivers cloud-native firewalling and threat prevention with management APIs for gateway provisioning, rule management, and integrations with CI/CD pipelines.
common:
  - type: Website
    url: https://www.checkpoint.com/cloudguard/
  - type: Documentation
    url: https://docs.cgn.portal.checkpoint.com/
  - type: Developer Portal
    url: https://docs.cgn.portal.checkpoint.com/reference
  - type: Getting Started
    url: https://sc1.checkpoint.com/documents/CloudGuard_Dome9/Documentation/Getting-Started/Getting-started-with-CloudGuard.htm
  - type: Authentication
    url: https://sc1.checkpoint.com/documents/CloudGuard_Dome9/Documentation/API-Authentication.html
  - type: Support
    url: https://support.checkpoint.com/
  - type: Community
    url: https://community.checkpoint.com/
  - type: Status
    url: https://status.dome9.com/
  - type: Privacy Policy
    url: https://www.checkpoint.com/privacy/
  - type: Terraform Provider
    url: https://registry.terraform.io/providers/dome9/dome9/latest/docs
  - type: JSON-LD
    url: json-ld/cloudguard-context.jsonld
  - type: Spectral
    url: rules/cloudguard-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cloudguard-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
