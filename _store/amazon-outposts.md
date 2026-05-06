---
aid: amazon-outposts
name: Amazon Outposts
description: AWS Outposts is a family of fully managed solutions delivering AWS infrastructure and services to virtually any on-premises or edge location for a truly consistent hybrid experience. It allows you to extend AWS infrastructure, AWS services, APIs, and tools to virtually any data center, co-location space, or on-premises facility.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Edge Computing
  - Hybrid Cloud
  - Infrastructure
  - On-Premises
url: https://raw.githubusercontent.com/api-evangelist/amazon-outposts/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-outposts:aws-outposts-api
    name: AWS Outposts API
    description: The AWS Outposts API provides programmatic access to create and manage Outposts, sites, orders, catalog items, assets, and local gateway routes for deploying AWS infrastructure on-premises.
    humanURL: https://aws.amazon.com/outposts/
    baseURL: https://outposts.amazonaws.com
    tags:
      - Edge Computing
      - Hybrid Cloud
      - On-Premises
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/outposts/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-outposts-openapi.yml
      - type: Getting Started
        url: https://aws.amazon.com/outposts/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/outposts/pricing/
      - type: FAQ
        url: https://aws.amazon.com/outposts/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/outposts/
  - type: Website
    url: https://aws.amazon.com/outposts/
  - type: Documentation
    url: https://docs.aws.amazon.com/outposts/
  - type: Terms of Service
    url: https://aws.amazon.com/service-terms/
  - type: Privacy Policy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/tag/aws-outposts/
  - type: GitHub Organization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/outposts/
  - type: Sign Up
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-outposts-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-outposts-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-outposts-workflow.yaml
  - type: JSON-LD
    url: json-ld/amazon-outposts-openapi-context.jsonld
  - type: JSONSchema
    url: json-schema/openapi-access-denied-exception-schema.json
    title: Openapi Access Denied Exception
  - type: JSONSchema
    url: json-schema/openapi-account-id-schema.json
    title: Openapi Account Id
  - type: JSONSchema
    url: json-schema/openapi-address-line1-schema.json
    title: Openapi Address Line1
  - type: JSONSchema
    url: json-schema/openapi-address-line2-schema.json
    title: Openapi Address Line2
  - type: JSONSchema
    url: json-schema/openapi-address-line3-schema.json
    title: Openapi Address Line3
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
