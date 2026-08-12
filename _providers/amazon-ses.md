---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Amazon Ses Agentic Access
  operation_count: 6
  slug: amazon-ses-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 16
apis:
- description: Official AWS documentation for Amazon Simple Email Service, providing comprehensive guides, API references, and tutorials for email sending and management.
  name: Amazon SES Documentation
  slug: amazon-ses-documentation
- description: The OpenAPI definition for the Amazon SES API, describing all available operations for sending emails, managing identities, contact lists, and email templates.
  name: Amazon SES OpenAPI
  slug: amazon-ses-openapi
- description: The APIs.guru maintained OpenAPI definition for the Amazon SES API.
  name: Amazon SES OpenAPI (APIs.guru)
  slug: amazon-ses-openapi-apisguru
- description: JSON Schema definitions for the Amazon SES API request and response objects.
  name: Amazon SES JSON Schema
  slug: amazon-ses-json-schema
- description: JSON-LD context document for Amazon SES API resources providing semantic linked data mappings.
  name: Amazon SES JSON-LD Context
  slug: amazon-ses-json-ld-context
- description: Pricing details for Amazon SES including email sending, receiving, and additional features.
  name: Amazon SES Pricing
  slug: amazon-ses-pricing
- description: Getting started guide for Amazon SES, helping new users set up and begin sending emails.
  name: Amazon SES Getting Started
  slug: amazon-ses-getting-started
- description: Frequently asked questions about Amazon SES covering features, pricing, deliverability, and compliance.
  name: Amazon SES FAQ
  slug: amazon-ses-faq
- description: Comprehensive user guide for Amazon SES covering all features and best practices for email communication.
  name: Amazon SES User Guide
  slug: amazon-ses-user-guide
- description: Complete API reference documentation for Amazon SES with detailed descriptions of all operations, parameters, and data types.
  name: Amazon SES API Reference
  slug: amazon-ses-api-reference
- description: AWS CLI reference for Amazon SES, providing command-line access to all SES operations.
  name: Amazon SES CLI Reference
  slug: amazon-ses-cli-reference
- description: Security documentation for Amazon SES covering authentication, authorization, and encryption.
  name: Amazon SES Security
  slug: amazon-ses-security
- description: Operations for managing contact lists.
  name: Amazon SES Contact Lists API
  slug: amazon-ses-contact-lists-api
- description: Operations for sending email messages.
  name: Amazon SES Email Sending API
  slug: amazon-ses-email-sending-api
- description: Operations for managing email identities.
  name: Amazon SES Identities API
  slug: amazon-ses-identities-api
- description: Operations for managing email templates.
  name: Amazon SES Templates API
  slug: amazon-ses-templates-api
artifact_total: 38
collections:
- collection_type: open
  name: Amazon SES Amazon Simple Email Service (SES)
  slug: open-amazon-ses
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-ses-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-ses-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-ses-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-ses-domain-security.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/amazon-ses/skills
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/ses/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/ses/
- group: commercial
  title: ''
  type: terms
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: privacy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/messaging-and-targeting/
- group: build
  title: ''
  type: github
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/ses/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: knowledge-center
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-ses
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-ses-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-ses-emailmessage-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-ses-openapi-email-message-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-ses-emailmessage-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-ses-openapi-email-message-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-ses-emailmessage-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-ses-openapi-email-message-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-ses-emailmessage-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-ses-openapi-email-message-example.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-ses-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-ses-vocabulary.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/amazon-ses-openapi.yml
created: '2024-01-15'
description: Amazon Simple Email Service (SES) is a cloud-based email sending service designed to help digital marketers and application developers send marketing, notification, and transactional emails, providing a reliable and scalable infrastructure for email communication.
examples:
- key_count: 7
  name: Amazon Ses Emailmessage Example
  slug: amazon-ses-emailmessage-example
- key_count: 3
  name: Amazon Ses Openapi Email Message Example
  slug: amazon-ses-openapi-email-message-example
finops:
- name: Amazon Ses Finops
  service_category: Communication / Email
  slug: amazon-ses-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: EmailMessage
  property_count: 7
  slug: amazon-ses-emailmessage
- name: EmailMessage
  property_count: 3
  slug: amazon-ses-openapi-email-message
json_structures:
- name: Amazon Ses Emailmessage Structure
  property_count: 7
  slug: amazon-ses-emailmessage-structure
- name: Amazon Ses Openapi Email Message Structure
  property_count: 3
  slug: amazon-ses-openapi-email-message-structure
- name: Amazon Ses Structure
  property_count: 0
  slug: amazon-ses-structure
jsonld:
- class_count: 0
  name: Amazon Ses Context
  property_count: 6
  slug: amazon-ses-context
- class_count: 1
  name: Amazon Ses Emailmessage Context
  property_count: 19
  slug: amazon-ses-emailmessage-context
- class_count: 1
  name: Amazon Ses Openapi Email Message Context
  property_count: 12
  slug: amazon-ses-openapi-email-message-context
layout: provider
modified: '2026-05-19'
name: Amazon SES
nav: Providers
network: true
overview: 'Amazon SES publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Contact Lists API, Email Sending API, Identities API, and 1 more. Tagged areas include Email, Email Deliverability, Email Service, Marketing Email, and Notifications.


  The Amazon SES catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon SES''s developer surface includes developer portal, documentation, terms of service, privacy policy, support, engineering blog, GitHub presence, and 28 more developer resources.'
plans:
- name: Amazon Ses Plans Pricing
  plan_count: 4
  slug: amazon-ses-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 5
  name: Amazon Ses Rate Limits
  slug: amazon-ses-rate-limits
rules:
- name: Amazon SES API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-ses-jsonschema-spectral-rules
- name: Amazon SES API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 13
  slug: amazon-ses-spectral-rules
score:
  band: developing
  composite: 48.8
  delta: -7.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 59.0
    developer_ergonomics: 37.0
    discoverability: 50.0
    governance: 68.8
    operational_transparency: 34.2
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-ses/refs/heads/main/screenshots/amazon-ses-2026-06-20T171820.png
security:
- kind: domain-security
  name: Amazon Ses Domain Security
  slug: amazon-ses-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Ses Vulnerability Disclosure
  slug: amazon-ses-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Ses Trust Center
  slug: amazon-ses-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
skill_count: 2
skills:
- name: aws-mail-manager
  slug: aws-mail-manager
- name: aws-ses
  slug: aws-ses
slug: amazon-ses
tags:
- Email
- Email Deliverability
- Email Service
- Marketing Email
- Notifications
- SMTP
- Transactional Email
website: https://aws.amazon.com/ses/
---
