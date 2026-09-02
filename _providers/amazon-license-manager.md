---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amazon License Manager Agentic Access
  operation_count: 5
  slug: amazon-license-manager-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: License configuration management
  name: Amazon License Manager License Configurations API
  slug: amazon-license-manager-license-configurations-api
artifact_total: 27
collections:
- collection_type: postman
  name: Amazon License Manager License Configurations API
  slug: postman-amazon-license-manager-license-configurations-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon License Manager License Configurations API
  slug: open-amazon-license-manager-license-configurations-api
- collection_type: open
  name: Amazon License Manager API
  slug: open-amazon-license-manager
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-license-manager/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-license-manager-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-license-manager-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-license-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-license-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-license-manager-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/license-manager/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/license-manager/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/license-manager/
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
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/mt/tag/aws-license-manager/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/license-manager/
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
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-license-manager-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-license-manager-vocabulary.yaml
created: '2026-03-16'
description: AWS License Manager makes it easier to manage licenses in AWS and on-premises servers from software vendors such as Microsoft, SAP, Oracle, and IBM. It helps you control your licensing costs by letting you create rules that emulate the terms of your licensing agreements.
examples:
- key_count: 8
  name: Amazon License Manager License Configuration Example
  slug: amazon-license-manager-license-configuration-example
features:
- description: Define licensing rules based on software attributes and enforce them during instance launches.
  name: License Rule Enforcement
- description: Track license usage across AWS and on-premises environments from a central dashboard.
  name: License Tracking
- description: Discover software inventory across multiple AWS accounts in an AWS Organization.
  name: Cross-Account Discovery
- description: Generate license compliance reports for auditors and software vendors.
  name: Automated Compliance Reports
- description: Use existing on-premises software licenses on EC2 with BYOL programs.
  name: Bring Your Own License (BYOL)
finops:
- name: Amazon License Manager Finops
  service_category: API
  slug: amazon-license-manager-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-license-manager.png
json_schemas:
- name: LicenseConfiguration
  property_count: 8
  slug: amazon-license-manager-license-configuration
json_structures:
- name: Amazon License Manager License Configuration Structure
  property_count: 8
  slug: amazon-license-manager-license-configuration-structure
jsonld:
- class_count: 1
  name: Amazon License Manager Context
  property_count: 7
  slug: amazon-license-manager-context
layout: provider
modified: '2026-05-19'
name: Amazon License Manager
nav: Providers
network: true
overview: 'Amazon License Manager publishes 1 API on the [APIs.io](https://apis.io/) network: License Configurations API. Tagged areas include Compliance, Cost Management, License Management, and Software Licensing.


  The Amazon License Manager catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon License Manager''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 14 more developer resources.'
plans:
- name: Amazon License Manager Plans Pricing
  plan_count: 3
  slug: amazon-license-manager-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Amazon License Manager Rate Limits
  slug: amazon-license-manager-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon License Manager API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-license-manager-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon License Manager API Rules
  rule_count: 24
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 15
  slug: amazon-license-manager-spectral-rules
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 68.0
    developer_ergonomics: 50.0
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-license-manager/refs/heads/main/screenshots/amazon-license-manager-2026-06-20T171724.png
security:
- kind: authentication
  name: Amazon License Manager Authentication
  slug: amazon-license-manager-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon License Manager Domain Security
  slug: amazon-license-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon License Manager Vulnerability Disclosure
  slug: amazon-license-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon License Manager Trust Center
  slug: amazon-license-manager-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-license-manager
tags:
- Compliance
- Cost Management
- License Management
- Software Licensing
use_cases:
- description: Ensure software deployments comply with license agreements across your AWS estate.
  name: License Compliance
- description: Track license usage to identify unused licenses and optimize software spend.
  name: Cost Optimization
- description: Generate detailed license reports for software vendor audits.
  name: Vendor Audit Preparation
website: https://aws.amazon.com/license-manager/
---
