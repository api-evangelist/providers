---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amazon License Manager Agentic Access
  operation_count: 5
  slug: amazon-license-manager-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://license-manager.amazonaws.com
  baseurl_source: declared
  description: License configuration management
  name: Amazon License Manager License Configurations API
  slug: amazon-license-manager-license-configurations-api
- baseURL: https://license-manager.amazonaws.com
  baseurl_source: declared
  description: The License Manager Grant API from Amazon License Manager — 5 operation(s) for license manager grant.
  name: Amazon License Manager License Manager Grant API
  slug: amazon-license-manager-grant-api
- baseURL: https://license-manager.amazonaws.com
  baseurl_source: declared
  description: The License Manager License API from Amazon License Manager — 4 operation(s) for license manager license.
  name: Amazon License Manager License Manager License API
  slug: amazon-license-manager-license-api
- baseURL: https://license-manager.amazonaws.com
  baseurl_source: declared
  description: The License Manager License Asset Group API from Amazon License Manager — 5 operation(s) for license manager license asset group.
  name: Amazon License Manager License Manager License Asset Group API
  slug: amazon-license-manager-license-asset-group-api
- baseURL: https://license-manager.amazonaws.com
  baseurl_source: declared
  description: The License Manager License Asset Ruleset API from Amazon License Manager — 5 operation(s) for license manager license asset ruleset.
  name: Amazon License Manager License Manager License Asset Ruleset API
  slug: amazon-license-manager-license-asset-ruleset-api
- baseURL: https://license-manager.amazonaws.com
  baseurl_source: declared
  description: The License Manager License Conversion Task API from Amazon License Manager — 3 operation(s) for license manager license conversion task.
  name: Amazon License Manager License Manager License Conversion Task API
  slug: amazon-license-manager-license-conversion-task-api
- baseURL: https://license-manager.amazonaws.com
  baseurl_source: declared
  description: The License Manager License Manager Report Generator API from Amazon License Manager — 5 operation(s) for license manager license manager report generator.
  name: Amazon License Manager License Manager License Manager Report Generator API
  slug: amazon-license-manager-license-manager-report-generator-api
- baseURL: https://license-manager.amazonaws.com
  baseurl_source: declared
  description: The License Manager Operations API from Amazon License Manager — 26 operation(s) for license manager operations.
  name: Amazon License Manager License Manager Operations API
  slug: amazon-license-manager-operations-api
- baseURL: https://license-manager.amazonaws.com
  baseurl_source: declared
  description: The License Manager Token API from Amazon License Manager — 3 operation(s) for license manager token.
  name: Amazon License Manager License Manager Token API
  slug: amazon-license-manager-token-api
artifact_total: 34
collections:
- collection_type: postman
  name: Amazon License Manager License Configurations API
  slug: postman-amazon-license-manager-license-configurations-api
- collection_type: open
  name: Amazon License Manager License Configurations API
  slug: open-amazon-license-manager-license-configurations-api
- collection_type: open
  name: Amazon License Manager API
  slug: open-amazon-license-manager
common:
- group: commercial
  href: https://artifacts.apis.io/amazon-license-manager/plans/amazon-license-manager-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-license-manager-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-license-manager/rate-limits/amazon-license-manager-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-license-manager-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-license-manager/finops/amazon-license-manager-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-license-manager-finops.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/license-manager/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-license-manager/overview
- group: agent
  href: https://artifacts.apis.io/amazon-license-manager/agentic-access/amazon-license-manager-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-license-manager-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-license-manager/security/amazon-license-manager-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-license-manager-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-license-manager/security/amazon-license-manager-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-license-manager-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-license-manager/security/amazon-license-manager-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-license-manager-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-license-manager/authentication/amazon-license-manager-authentication.yml
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
  href: https://artifacts.apis.io/amazon-license-manager/rules/amazon-license-manager-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-license-manager-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-license-manager/vocabulary/amazon-license-manager-vocabulary.yaml
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
- has_sources: true
  method: derived
  name: Amazon License Manager Finops
  primary_unit: ''
  service_category: ''
  slug: amazon-license-manager-finops
  template: true
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
modified: '2026-09-16'
name: Amazon License Manager
nav: Providers
network: true
overview: 'Amazon License Manager publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including License Configurations API, License Manager Grant API, License Manager License API, and 6 more. Tagged areas include Amazon Web Services, Compliance, Cost Management, License Management, and Software Licensing.


  The Amazon License Manager catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon License Manager''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 18 more developer resources.'
plans:
- name: Amazon License Manager Plans Pricing
  plan_count: 1
  slug: amazon-license-manager-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Amazon License Manager Rate Limits
  slug: amazon-license-manager-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon License Manager — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-license-manager-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 65
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
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 67.4
    catalog_earned_first_party: 8.0
    catalog_gap: 47.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.2
  facets:
    access_clarity: 67.1
    contract_governance: 27.3
    contract_quality: 65.5
    developer_ergonomics: 46.4
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 88.9
      total: 9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/amazon-license-manager/amazon-license-manager-2026-06-20T171724.png
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
- Amazon Web Services
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
