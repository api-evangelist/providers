---
aid: amazon-network-firewall
name: Amazon Network Firewall
description: AWS Network Firewall is a stateful, managed, network firewall and intrusion detection and prevention service for your virtual private cloud (VPC). It enables you to filter traffic at the perimeter of your VPC with a flexible rules engine with support for thousands of custom rules.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Firewall
  - Intrusion Detection
  - Network Security
  - VPC
url: https://raw.githubusercontent.com/api-evangelist/amazon-network-firewall/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-network-firewall:aws-network-firewall-api
    name: AWS Network Firewall API
    description: The AWS Network Firewall API provides programmatic access to create and manage firewalls, firewall policies, rule groups, and TLS inspection configurations for network traffic filtering in VPCs.
    humanURL: https://aws.amazon.com/network-firewall/
    baseURL: https://network-firewall.amazonaws.com
    tags:
      - Firewall
      - Network Security
      - VPC
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-network-firewall-openapi.yml
      - type: Getting Started
        url: https://aws.amazon.com/network-firewall/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/network-firewall/pricing/
      - type: FAQ
        url: https://aws.amazon.com/network-firewall/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/network-firewall/
  - type: Website
    url: https://aws.amazon.com/network-firewall/
  - type: Documentation
    url: https://docs.aws.amazon.com/network-firewall/
  - type: Terms of Service
    url: https://aws.amazon.com/service-terms/
  - type: Privacy Policy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/networking-and-content-delivery/tag/aws-network-firewall/
  - type: GitHub Organization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/vpc/network-firewall/
  - type: Sign Up
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-network-firewall-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-network-firewall-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-network-firewall-workflow.yaml
  - type: JSON-LD
    url: json-ld/amazon-network-firewall-openapi-context.jsonld
  - type: JSONSchema
    url: json-schema/openapi-action-definition-schema.json
    title: Openapi Action Definition
  - type: JSONSchema
    url: json-schema/openapi-action-name-schema.json
    title: Openapi Action Name
  - type: JSONSchema
    url: json-schema/openapi-address-definition-schema.json
    title: Openapi Address Definition
  - type: JSONSchema
    url: json-schema/openapi-address-schema.json
    title: Openapi Address
  - type: JSONSchema
    url: json-schema/openapi-addresses-schema.json
    title: Openapi Addresses
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
