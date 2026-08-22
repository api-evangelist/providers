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
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Security Hub Agentic Access
  operation_count: 6
  slug: amazon-security-hub-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 5
apis:
- description: Operations for enabling and configuring Security Hub.
  name: Amazon Security Hub Administration API
  slug: amazon-security-hub-administration-api
- description: Operations for managing security findings.
  name: Amazon Security Hub Findings API
  slug: amazon-security-hub-findings-api
- description: Operations for managing security insights.
  name: Amazon Security Hub Insights API
  slug: amazon-security-hub-insights-api
- description: Operations for managing product integrations.
  name: Amazon Security Hub Integrations API
  slug: amazon-security-hub-integrations-api
- description: Operations for managing security standards.
  name: Amazon Security Hub Standards API
  slug: amazon-security-hub-standards-api
arazzos:
- description: Enable Security Hub, confirm its standards, and capture an initial findings baseline.
  name: Amazon Security Hub Bootstrap Posture Baseline
  slug: amazon-security-hub-bootstrap-posture-baseline-workflow
- description: Enable Security Hub for the account and review which security standards are now available.
  name: Amazon Security Hub Enable Hub and Review Standards
  slug: amazon-security-hub-enable-hub-and-review-standards-workflow
- description: Enable a partner product integration and verify its findings flow into Security Hub.
  name: Amazon Security Hub Onboard Product Integration
  slug: amazon-security-hub-onboard-product-integration-workflow
- description: List a saved insight and drill into the findings behind it.
  name: Amazon Security Hub Review Insight Findings
  slug: amazon-security-hub-review-insight-findings-workflow
- description: List the enabled security standards and pull the failing compliance findings behind them.
  name: Amazon Security Hub Standards Compliance Audit
  slug: amazon-security-hub-standards-compliance-audit-workflow
- description: Retrieve high-severity findings and update them by re-importing the modified records.
  name: Amazon Security Hub Triage and Update Findings
  slug: amazon-security-hub-triage-and-update-findings-workflow
artifact_total: 46
collections:
- collection_type: postman
  name: Amazon Security Hub
  slug: postman-amazon-security-hub
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Security Hub Administration API
  slug: open-amazon-security-hub-administration-api
- collection_type: open
  name: Amazon Security Hub Administration Findings API
  slug: open-amazon-security-hub-findings-api
- collection_type: open
  name: Amazon Security Hub Administration Insights API
  slug: open-amazon-security-hub-insights-api
- collection_type: open
  name: Amazon Security Hub Administration Integrations API
  slug: open-amazon-security-hub-integrations-api
- collection_type: open
  name: Amazon Security Hub Administration Standards API
  slug: open-amazon-security-hub-standards-api
- collection_type: open
  name: Amazon Security Hub
  slug: open-amazon-security-hub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-security-hub-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-security-hub-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-security-hub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-security-hub-domain-security.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-security-hub/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-hub-bootstrap-posture-baseline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-hub-enable-hub-and-review-standards-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-hub-onboard-product-integration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-hub-review-insight-findings-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-hub-standards-compliance-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-security-hub-triage-and-update-findings-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/security-hub/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/securityhub/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/securityhub/latest/APIReference/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/securityhub/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/security-hub/pricing/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/security-hub/faqs/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-security-hub
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-security-hub-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-security-hub-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-security-hub-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-security-hub-finding-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-security-hub-finding-example.json
created: '2024-01-15'
description: AWS Security Hub is a cloud security posture management service that provides a comprehensive view of your security state across AWS accounts. It aggregates, organizes, and prioritizes security findings from multiple AWS services and third-party tools, enabling centralized security monitoring, compliance checking, and automated remediation workflows.
examples:
- key_count: 15
  name: Amazon Security Hub Finding Example
  slug: amazon-security-hub-finding-example
features:
- description: Aggregate security findings from across multiple AWS accounts and regions into a single pane of glass.
  name: Multi-Account Findings Aggregation
- description: Standardized JSON format for all security findings enabling consistent analysis and automation.
  name: AWS Security Finding Format (ASFF)
- description: Automated compliance checks against CIS AWS Foundations, PCI DSS, NIST, SOC 2, and AWS Foundational Security Best Practices.
  name: Built-in Compliance Standards
- description: Ingest findings from 80+ third-party security partners including CrowdStrike, Palo Alto Networks, and Splunk.
  name: Third-Party Integrations
- description: Trigger automated remediation via Amazon EventBridge and AWS Security Hub automated response and remediation.
  name: Automated Remediation
- description: Correlated views of security findings to highlight areas needing attention.
  name: Security Insights
- description: Create custom actions to send findings to ticketing, chat, and SOAR platforms.
  name: Custom Actions
- description: Aggregate findings across multiple AWS regions into a designated aggregation region.
  name: Cross-Region Aggregation
finops:
- name: Amazon Security Hub Finops
  service_category: API
  slug: amazon-security-hub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-security-hub.png
json_schemas:
- name: Finding
  property_count: 15
  slug: amazon-security-hub-finding
json_structures:
- name: Amazon Security Hub Finding Structure
  property_count: 15
  slug: amazon-security-hub-finding-structure
jsonld:
- class_count: 1
  name: Amazon Security Hub Context
  property_count: 15
  slug: amazon-security-hub-context
layout: provider
modified: '2026-05-19'
name: Amazon Security Hub
nav: Providers
network: true
overview: 'Amazon Security Hub publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Administration API, Findings API, Insights API, and 2 more. Tagged areas include Compliance, Monitoring, and Security.


  The Amazon Security Hub catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Security Hub''s developer surface includes developer portal, getting-started guide, documentation, API reference, developer console, signup flow, pricing, and 27 more developer resources.'
plans:
- name: Amazon Security Hub Plans Pricing
  plan_count: 3
  slug: amazon-security-hub-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Amazon Security Hub Rate Limits
  slug: amazon-security-hub-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Security Hub API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-security-hub-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: Amazon Security Hub API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 12
  slug: amazon-security-hub-spectral-rules
score:
  band: strong
  composite: 54.3
  delta: -7.1
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 25.0
    contract_quality: 61.7
    developer_ergonomics: 50.0
    discoverability: 72.2
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-security-hub/refs/heads/main/screenshots/amazon-security-hub-2026-06-20T171826.png
security:
- kind: domain-security
  name: Amazon Security Hub Domain Security
  slug: amazon-security-hub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Security Hub Vulnerability Disclosure
  slug: amazon-security-hub-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Security Hub Trust Center
  slug: amazon-security-hub-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-security-hub
tags:
- Compliance
- Monitoring
- Security
use_cases:
- description: Continuously monitor your AWS environment for security misconfigurations and compliance gaps.
  name: Cloud Security Posture Management
- description: Automate compliance checks and generate reports for CIS, PCI DSS, NIST, and other frameworks.
  name: Compliance Reporting
- description: Centralize security monitoring across dozens or hundreds of AWS accounts in an organization.
  name: Multi-Account Security Operations
- description: Aggregate findings from GuardDuty, Inspector, Macie, and third-party tools in one place.
  name: Threat Detection Aggregation
- description: Trigger automated remediation workflows when critical findings are detected.
  name: Automated Incident Response
- description: Replace multiple point solutions with centralized finding aggregation and normalized data.
  name: Security Tool Consolidation
website: https://aws.amazon.com/
---
