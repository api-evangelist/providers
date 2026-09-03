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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Amazon Ses Agentic Access
  operation_count: 6
  slug: amazon-ses-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 2
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
- baseURL: https://email.{region}.amazonaws.com
  baseurl_source: declared
  description: Operations for managing contact lists.
  name: Amazon SES Contact Lists API
  slug: amazon-ses-contact-lists-api
- baseURL: https://email.{region}.amazonaws.com
  baseurl_source: declared
  description: Operations for sending email messages.
  name: Amazon SES Email Sending API
  slug: amazon-ses-email-sending-api
- baseURL: https://email.{region}.amazonaws.com
  baseurl_source: declared
  description: Operations for managing email identities.
  name: Amazon SES Identities API
  slug: amazon-ses-identities-api
- baseURL: https://email.{region}.amazonaws.com
  baseurl_source: declared
  description: Operations for managing email templates.
  name: Amazon SES Templates API
  slug: amazon-ses-templates-api
- baseURL: https://email.{region}.amazonaws.com
  baseurl_source: declared
  description: The Email API from Amazon SES — 60 operation(s) for email.
  name: Amazon SES Email API
  slug: amazon-ses-email-api
artifact_total: 47
asyncapis:
- description: ''
  name: Amazon Ses Events
  slug: amazon-ses-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon SES Amazon Simple Email Service (SES) Contact Lists API
  slug: open-amazon-ses-contact-lists-api
- collection_type: open
  name: Amazon SES Amazon Simple Email Service (SES) Contact Lists Email Sending API
  slug: open-amazon-ses-email-sending-api
- collection_type: open
  name: Amazon SES Amazon Simple Email Service (SES) Contact Lists Identities API
  slug: open-amazon-ses-identities-api
- collection_type: open
  name: Amazon SES Amazon Simple Email Service (SES) Contact Lists Templates API
  slug: open-amazon-ses-templates-api
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
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://github.com/amazon-ses/skills
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aws.amazon.com/ses/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/ses/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/ses/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/Welcome.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/ses/latest/dg/send-email-getting-started.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/ses/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
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
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/ses/
- group: start
  title: ''
  type: SignUp
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
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/amazon-ses-sesv2-openapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-ses-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/amazon-ses-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/amazon-ses-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-ses-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amazon-ses-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-ses-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amazon-ses-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-ses-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amazon-ses-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-ses-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/amazon-ses-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/amazon-ses-events.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-ses-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/amazon-ses-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-ses-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-ses-api-reference-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-ses-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-ses-security.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/amazon-ses-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amazon-ses-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/amazon-ses-finops.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-ses-sesv2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-ses-email-sending-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-ses-identities-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-ses-contact-lists-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-ses-templates-api-overlay.yaml
- group: build
  title: ''
  type: PostmanCollection
  url: collections/amazon-ses.postman_collection.json
created: '2024-01-15'
description: Amazon Simple Email Service (SES) is AWS's cloud email platform for sending and receiving mail at scale — marketing, notification and transactional. The current contract is the SES v2 API (version 2019-09-27), an 86-operation REST-JSON service authenticated with AWS Signature Version 4 and reached at a regional endpoint, alongside an SMTP submission interface on ports 25/465/587/2465/2587. It covers email sending and templated bulk sends, domain and address identity verification with DKIM, SPF and DMARC alignment, configuration sets and event publishing to SNS, EventBridge, CloudWatch and Firehose, contact lists and subscription topics, account and configuration-set suppression lists, dedicated IP pools both managed and standard, tenants for per-workload reputation isolation, and Virtual Deliverability Manager for inbox placement and reputation reporting. Mail Manager adds inbound processing with ingress points, traffic policies, rule sets, relays and archives. Every new account
  starts in the SES sandbox, and a published mailbox simulator forces delivery, bounce, complaint and out-of-office outcomes on demand.
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
mcp_servers:
- description: ''
  name: Amazon SES MCP Server
  slug: amazon-ses-mcp-server
modified: '2026-08-13'
name: Amazon SES
nav: Providers
network: true
overview: 'Amazon SES publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Contact Lists API, Email Sending API, Identities API, and 2 more. Tagged areas include Email, Email Deliverability, Email Service, Marketing Email, and Notification.


  The Amazon SES catalog on APIs.io includes 1 event-driven AsyncAPI specification, 3 JSON-LD contexts, and 2 Spectral governance rulesets.


  Amazon SES''s developer surface includes developer portal, documentation, API reference, getting-started guide, pricing, support, engineering blog, and 61 more developer resources.'
plans:
- name: Amazon Ses Plans Pricing
  plan_count: 4
  slug: amazon-ses-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 24
  name: Amazon Ses Rate Limits
  slug: amazon-ses-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Amazon SES API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-ses-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: Amazon SES API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 13
  slug: amazon-ses-spectral-rules
score:
  band: exemplar
  composite: 76.7
  coverage:
    artifact_dirs: 31
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.6
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 47.0
    contract_quality: 64.9
    developer_ergonomics: 90.5
    discoverability: 57.4
    governance: 47.0
    operational_transparency: 84.2
  previous_composite: 76.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 20.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-ses/refs/heads/main/screenshots/amazon-ses-2026-06-20T171820.png
security:
- kind: authentication
  name: Amazon Ses Authentication
  slug: amazon-ses-authentication
  summary_line: apiKey/sigv4/smtp-credentials · 1 scheme
- kind: domain-security
  name: Amazon Ses Domain Security
  slug: amazon-ses-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Ses Vulnerability Disclosure
  slug: amazon-ses-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
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
- Notification
- SMTP
- Transactional Email
- Bulk Email
- Email Receiving
- DKIM
- Messaging
- Cloud Infrastructure
website: https://aws.amazon.com/ses/
---
