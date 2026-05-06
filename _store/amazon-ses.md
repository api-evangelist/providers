---
name: Amazon SES
description: Amazon Simple Email Service (SES) is a cloud-based email sending service designed to help digital marketers and application developers send marketing, notification, and transactional emails, providing a reliable and scalable infrastructure for email communication.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/amazon-ses/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon SES Documentation
    description: Official AWS documentation for Amazon Simple Email Service, providing comprehensive guides, API references, and tutorials for email sending and management.
    url: https://docs.aws.amazon.com/ses/
    type: documentation
  - name: Amazon SES OpenAPI
    description: The OpenAPI definition for the Amazon SES API, describing all available operations for sending emails, managing identities, contact lists, and email templates.
    url: openapi/amazon-ses-openapi.yml
    type: openapi
  - name: Amazon SES OpenAPI (APIs.guru)
    description: The APIs.guru maintained OpenAPI definition for the Amazon SES API.
    url: https://api.apis.guru/v2/specs/amazonaws.com/sesv2/2019-09-27/openapi.yaml
    type: openapi
  - name: Amazon SES JSON Schema
    description: JSON Schema definitions for the Amazon SES API request and response objects.
    url: json-schema/amazon-ses-emailmessage-schema.json
    type: json-schema
  - name: Amazon SES JSON-LD Context
    description: JSON-LD context document for Amazon SES API resources providing semantic linked data mappings.
    url: json-ld/amazon-ses-context.jsonld
    type: json-ld
  - name: Amazon SES Pricing
    description: Pricing details for Amazon SES including email sending, receiving, and additional features.
    url: https://aws.amazon.com/ses/pricing/
    type: pricing
  - name: Amazon SES Getting Started
    description: Getting started guide for Amazon SES, helping new users set up and begin sending emails.
    url: https://docs.aws.amazon.com/ses/latest/dg/send-email-getting-started.html
    type: getting-started
  - name: Amazon SES FAQ
    description: Frequently asked questions about Amazon SES covering features, pricing, deliverability, and compliance.
    url: https://aws.amazon.com/ses/faqs/
    type: faq
  - name: Amazon SES User Guide
    description: Comprehensive user guide for Amazon SES covering all features and best practices for email communication.
    url: https://docs.aws.amazon.com/ses/latest/dg/Welcome.html
    type: user-guide
  - name: Amazon SES API Reference
    description: Complete API reference documentation for Amazon SES with detailed descriptions of all operations, parameters, and data types.
    url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/Welcome.html
    type: api-reference
  - name: Amazon SES CLI Reference
    description: AWS CLI reference for Amazon SES, providing command-line access to all SES operations.
    url: https://docs.aws.amazon.com/cli/latest/reference/sesv2/
    type: cli-reference
  - name: Amazon SES Security
    description: Security documentation for Amazon SES covering authentication, authorization, and encryption.
    url: https://docs.aws.amazon.com/ses/latest/dg/security.html
    type: security
common:
  - type: portal
    url: https://aws.amazon.com/
  - type: website
    url: https://aws.amazon.com/ses/
  - type: docs
    url: https://docs.aws.amazon.com/ses/
  - type: terms
    url: https://aws.amazon.com/service-terms/
  - type: privacy
    url: https://aws.amazon.com/privacy/
  - type: support
    url: https://aws.amazon.com/support/
  - type: blog
    url: https://aws.amazon.com/blogs/messaging-and-targeting/
  - type: github
    url: https://github.com/aws
  - type: console
    url: https://console.aws.amazon.com/ses/
  - type: signup
    url: https://portal.aws.amazon.com/billing/signup
  - type: login
    url: https://signin.aws.amazon.com/
  - type: status
    url: https://health.aws.amazon.com/health/status
  - type: knowledge-center
    url: https://repost.aws/knowledge-center
  - type: youtube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: stack-overflow
    url: https://stackoverflow.com/questions/tagged/amazon-ses
  - type: contact
    url: https://aws.amazon.com/contact-us/
  - type: security
    url: https://aws.amazon.com/security/
  - type: compliance
    url: https://aws.amazon.com/compliance/
  - type: JSON-LD
    url: json-ld/amazon-ses-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-ses-emailmessage-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-ses-openapi-email-message-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-ses-emailmessage-schema.json
  - type: JSONSchema
    url: json-schema/amazon-ses-openapi-email-message-schema.json
  - type: JSONStructure
    url: json-structure/amazon-ses-emailmessage-structure.json
  - type: JSONStructure
    url: json-structure/amazon-ses-openapi-email-message-structure.json
  - type: Example
    url: examples/amazon-ses-emailmessage-example.json
  - type: Example
    url: examples/amazon-ses-openapi-email-message-example.json
  - type: NaftikoCapability
    url: capabilities/amazon-ses.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-ses.yaml
  - type: SpectralRules
    url: rules/amazon-ses-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-ses-vocabulary.yaml
  - type: OpenAPI
    url: openapi/amazon-ses-openapi.yml
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
tags:
  - AWS
  - Email
  - Email Deliverability
  - Email Service
  - Marketing Email
  - Notifications
  - SMTP
  - Transactional Email
---
