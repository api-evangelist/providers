---
aid: amazon-service-catalog
name: Amazon Service Catalog
description: AWS Service Catalog enables organizations to create and manage catalogs of IT services that are approved for use on AWS. IT administrators can create and manage a portfolio of products (services, applications, and others) and control which users have access to which products.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Cloud Governance
  - Compliance
  - IT Governance
  - Service Catalog
url: https://raw.githubusercontent.com/api-evangelist/amazon-service-catalog/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-service-catalog:aws-service-catalog-api
    name: AWS Service Catalog API
    description: The AWS Service Catalog API provides programmatic access to create and manage portfolios, products, provisioning artifacts, constraints, and service actions for IT service governance and self-service provisioning.
    humanURL: https://aws.amazon.com/servicecatalog/
    baseURL: https://servicecatalog.amazonaws.com
    tags:
      - Cloud Governance
      - IT Governance
      - Service Catalog
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Reference.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/servicecatalog/2015-12-10/openapi.yaml
      - type: Getting Started
        url: https://aws.amazon.com/servicecatalog/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/servicecatalog/pricing/
      - type: FAQ
        url: https://aws.amazon.com/servicecatalog/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/servicecatalog/
  - type: Website
    url: https://aws.amazon.com/servicecatalog/
  - type: Documentation
    url: https://docs.aws.amazon.com/servicecatalog/
  - type: Terms of Service
    url: https://aws.amazon.com/service-terms/
  - type: Privacy Policy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/mt/tag/aws-service-catalog/
  - type: GitHub Organization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/servicecatalog/
  - type: Sign Up
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: JSON-LD
    url: json-ld/amazon-service-catalog-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-service-catalog-portfolio-schema.json
  - type: JSONSchema
    url: json-schema/amazon-service-catalog-product-view-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-service-catalog-provisioned-product-schema.json
  - type: JSONStructure
    url: json-structure/amazon-service-catalog-portfolio-structure.json
  - type: JSONStructure
    url: json-structure/amazon-service-catalog-product-view-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-service-catalog-provisioned-product-structure.json
  - type: Example
    url: examples/amazon-service-catalog-portfolio-example.json
  - type: Example
    url: examples/amazon-service-catalog-product-view-summary-example.json
  - type: Example
    url: examples/amazon-service-catalog-provisioned-product-example.json
  - type: NaftikoCapability
    url: capabilities/it-service-governance.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-service-catalog.yaml
  - type: SpectralRules
    url: rules/amazon-service-catalog-spectral-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
