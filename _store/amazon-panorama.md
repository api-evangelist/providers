---
aid: amazon-panorama
name: Amazon Panorama
description: AWS Panorama is a machine learning appliance and software development kit (SDK) that brings computer vision to on-premises cameras. It allows organizations to automate visual inspection tasks, such as gauging production line efficiency or identifying bottlenecks in industrial operations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Cameras
  - Computer Vision
  - Edge ML
  - Industrial IoT
url: https://raw.githubusercontent.com/api-evangelist/amazon-panorama/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-panorama:aws-panorama-api
    name: AWS Panorama API
    description: The AWS Panorama API provides programmatic access to create and manage appliances, application instances, packages, nodes, and device jobs for deploying computer vision applications to edge cameras.
    humanURL: https://aws.amazon.com/panorama/
    baseURL: https://panorama.amazonaws.com
    tags:
      - Computer Vision
      - Edge ML
      - Industrial IoT
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/panorama/latest/api/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-panorama-openapi.yml
      - type: Getting Started
        url: https://aws.amazon.com/panorama/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/panorama/pricing/
      - type: FAQ
        url: https://aws.amazon.com/panorama/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/panorama/
  - type: Website
    url: https://aws.amazon.com/panorama/
  - type: Documentation
    url: https://docs.aws.amazon.com/panorama/
  - type: Terms of Service
    url: https://aws.amazon.com/service-terms/
  - type: Privacy Policy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/machine-learning/tag/aws-panorama/
  - type: GitHub Organization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/panorama/
  - type: Sign Up
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-panorama-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-panorama-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-panorama-workflow.yaml
  - type: JSON-LD
    url: json-ld/amazon-panorama-openapi-context.jsonld
  - type: JSONSchema
    url: json-schema/openapi-access-denied-exception-schema.json
    title: Openapi Access Denied Exception
  - type: JSONSchema
    url: json-schema/openapi-alternate-software-metadata-schema.json
    title: Openapi Alternate Software Metadata
  - type: JSONSchema
    url: json-schema/openapi-alternate-softwares-schema.json
    title: Openapi Alternate Softwares
  - type: JSONSchema
    url: json-schema/openapi-application-instance-arn-schema.json
    title: Openapi Application Instance Arn
  - type: JSONSchema
    url: json-schema/openapi-application-instance-health-status-schema.json
    title: Openapi Application Instance Health Status
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
