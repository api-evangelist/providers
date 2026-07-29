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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Amazon Lightsail Agentic Access
  operation_count: 6
  slug: amazon-lightsail-agentic-access
  summary_line: 6 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Lightsail virtual server instance management
  name: Amazon Lightsail Instances API
  slug: amazon-lightsail-instances-api
artifact_total: 30
collections:
- collection_type: postman
  name: Amazon Lightsail Instances API
  slug: postman-amazon-lightsail-instances-api
- collection_type: open
  name: Amazon Lightsail API
  slug: open-amazon-lightsail
- collection_type: open
  name: Amazon Lightsail API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-lightsail/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-lightsail-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-lightsail-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-lightsail-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-lightsail-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-lightsail-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/lightsail/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/lightsail/
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
  url: https://aws.amazon.com/blogs/compute/
- group: build
  title: ''
  type: github
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://lightsail.aws.amazon.com/
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
  url: https://stackoverflow.com/questions/tagged/amazon-lightsail
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
  type: SpectralRules
  url: rules/amazon-lightsail-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-lightsail-vocabulary.yaml
created: '2024-01-15'
description: Amazon Lightsail is a virtual private server (VPS) provider and is the easiest way to get started with AWS for developers, small businesses, students, and other users who need a solution to build and host their applications on cloud. Lightsail provides developers compute, storage, and networking capacity and capabilities to deploy and manage websites and web applications in the cloud.
examples:
- key_count: 7
  name: Amazon Lightsail Instance Example
  slug: amazon-lightsail-instance-example
features:
- description: Launch virtual servers with pre-configured Linux/Windows environments in minutes.
  name: Simple Virtual Servers
- description: Deploy managed databases (MySQL, PostgreSQL) without server management.
  name: Managed Databases
- description: Deploy containerized applications using Lightsail container services.
  name: Containers
- description: Create CloudFront-powered CDN distributions for faster content delivery.
  name: CDN Distributions
- description: Fixed monthly pricing with no surprise bills including compute, storage, and data transfer.
  name: Predictable Pricing
finops:
- name: Amazon Lightsail Finops
  service_category: API
  slug: amazon-lightsail-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Connect Lightsail instances to S3 buckets for object storage.
  name: Amazon S3
- description: Distribute Lightsail content globally via CloudFront CDN distributions.
  name: AWS CloudFront
- description: Manage DNS for Lightsail resources using Route 53.
  name: Amazon Route 53
- description: Migrate Lightsail instances to EC2 when you need more control.
  name: Amazon EC2
json_schemas:
- name: Instance
  property_count: 7
  slug: amazon-lightsail-instance
json_structures:
- name: Amazon Lightsail Instance Structure
  property_count: 7
  slug: amazon-lightsail-instance-structure
jsonld:
- class_count: 1
  name: Amazon Lightsail Context
  property_count: 7
  slug: amazon-lightsail-context
layout: provider
modified: '2026-05-19'
name: Amazon Lightsail
nav: Providers
network: true
overview: 'Amazon Lightsail publishes 1 API on the [APIs.io](https://apis.io/) network: Instances API.


  The Amazon Lightsail catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Lightsail''s developer surface includes authentication, developer portal, documentation, support, engineering blog, GitHub presence, developer console, and 19 more developer resources.'
plans:
- name: Amazon Lightsail Plans Pricing
  plan_count: 3
  slug: amazon-lightsail-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 5
  name: Amazon Lightsail Rate Limits
  slug: amazon-lightsail-rate-limits
rules:
- name: Amazon Lightsail API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 2
  slug: amazon-lightsail-jsonschema-spectral-rules
- name: Amazon Lightsail API Rules
  rule_count: 23
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 14
  slug: amazon-lightsail-spectral-rules
score:
  band: strong
  composite: 65.9
  delta: -2.6
  facets:
    commercial_clarity: 89.5
    contract_quality: 74.6
    developer_ergonomics: 45.7
    discoverability: 44.4
    governance: 68.8
    operational_transparency: 57.9
  previous_composite: 68.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/screenshots/amazon-lightsail-2026-06-20T171728.png
security:
- kind: authentication
  name: Amazon Lightsail Authentication
  slug: amazon-lightsail-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Lightsail Domain Security
  slug: amazon-lightsail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Lightsail Vulnerability Disclosure
  slug: amazon-lightsail-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Lightsail Trust Center
  slug: amazon-lightsail-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-lightsail
use_cases:
- description: Host WordPress sites with pre-configured LAMP stacks at low, predictable cost.
  name: WordPress Hosting
- description: Develop and test web applications on simple cloud infrastructure.
  name: Web Application Development
- description: Power small business websites with affordable, managed cloud hosting.
  name: Small Business Websites
website: https://aws.amazon.com/lightsail/
---
