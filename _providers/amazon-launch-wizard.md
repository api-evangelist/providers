---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Amazon Launch Wizard Agentic Access
  operation_count: 5
  slug: amazon-launch-wizard-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://launchwizard.amazonaws.com
  baseurl_source: declared
  description: Launch Wizard deployment management
  name: Amazon Launch Wizard Deployments API
  slug: amazon-launch-wizard-deployments-api
artifact_total: 31
collections:
- collection_type: postman
  name: Amazon Launch Wizard Deployments API
  slug: postman-amazon-launch-wizard-deployments-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Launch Wizard Deployments API
  slug: open-amazon-launch-wizard-deployments-api
- collection_type: open
  name: Amazon Launch Wizard API
  slug: open-amazon-launch-wizard
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-launch-wizard/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-launch-wizard-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-launch-wizard-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-launch-wizard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-launch-wizard-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-launch-wizard-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/launchwizard/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/launchwizard/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/launchwizard/
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
  url: https://aws.amazon.com/blogs/apn/tag/aws-launch-wizard/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/launchwizard/
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
  url: rules/amazon-launch-wizard-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-launch-wizard-vocabulary.yaml
created: '2026-03-16'
description: AWS Launch Wizard is a service that guides you through the sizing, configuration, and deployment of enterprise applications on AWS, such as Microsoft SQL Server Always On and HANA-based SAP systems, without the need to manually identify and provision individual AWS resources.
examples:
- key_count: 6
  name: Amazon Launch Wizard Deployment Example
  slug: amazon-launch-wizard-deployment-example
features:
- description: Step-by-step guidance to size, configure, and deploy enterprise applications on AWS.
  name: Guided Deployment
- description: Deploy SAP HANA and SAP NetWeaver on AWS with automated infrastructure sizing and setup.
  name: SAP Support
- description: Deploy Microsoft SQL Server on AWS with Always On availability groups and best practices.
  name: SQL Server Support
- description: Deploy Microsoft Active Directory on AWS with recommended configurations.
  name: Active Directory Support
- description: Estimate the cost of your deployment before provisioning resources.
  name: Cost Estimation
finops:
- name: Amazon Launch Wizard Finops
  service_category: API
  slug: amazon-launch-wizard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-launch-wizard.png
integrations:
- description: Launch Wizard generates CloudFormation templates for repeatable infrastructure deployments.
  name: AWS CloudFormation
- description: Provisions and configures EC2 instances with recommended sizes for enterprise workloads.
  name: Amazon EC2
- description: Attaches appropriately sized EBS volumes optimized for enterprise application performance.
  name: Amazon EBS
- description: Uses Systems Manager for configuration management and post-deployment tasks.
  name: AWS Systems Manager
json_schemas:
- name: Deployment
  property_count: 6
  slug: amazon-launch-wizard-deployment
json_structures:
- name: Amazon Launch Wizard Deployment Structure
  property_count: 6
  slug: amazon-launch-wizard-deployment-structure
jsonld:
- class_count: 1
  name: Amazon Launch Wizard Context
  property_count: 7
  slug: amazon-launch-wizard-context
layout: provider
modified: '2026-05-19'
name: Amazon Launch Wizard
nav: Providers
network: true
overview: 'Amazon Launch Wizard publishes 1 API on the [APIs.io](https://apis.io/) network: Deployments API. Tagged areas include Deployment, Enterprise Applications, SAP, and SQL Server.


  The Amazon Launch Wizard catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Launch Wizard''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 14 more developer resources.'
plans:
- name: Amazon Launch Wizard Plans Pricing
  plan_count: 3
  slug: amazon-launch-wizard-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Amazon Launch Wizard Rate Limits
  slug: amazon-launch-wizard-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Amazon Launch Wizard API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-launch-wizard-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: Amazon Launch Wizard API Rules
  rule_count: 22
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 13
  slug: amazon-launch-wizard-spectral-rules
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 28.8
    contract_quality: 64.6
    developer_ergonomics: 46.4
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-launch-wizard/refs/heads/main/screenshots/amazon-launch-wizard-2026-06-20T171723.png
security:
- kind: authentication
  name: Amazon Launch Wizard Authentication
  slug: amazon-launch-wizard-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Launch Wizard Domain Security
  slug: amazon-launch-wizard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Launch Wizard Vulnerability Disclosure
  slug: amazon-launch-wizard-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Launch Wizard Trust Center
  slug: amazon-launch-wizard-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-launch-wizard
tags:
- Deployment
- Enterprise Applications
- SAP
- SQL Server
use_cases:
- description: Migrate SAP workloads to AWS with guided deployment and AWS best practices.
  name: SAP Migration
- description: Deploy highly available SQL Server with Always On availability groups.
  name: SQL Server HA
- description: Deploy and configure Active Directory on AWS for enterprise identity management.
  name: Active Directory Setup
website: https://aws.amazon.com/launchwizard/
---
