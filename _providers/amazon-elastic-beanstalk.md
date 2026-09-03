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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amazon Elastic Beanstalk Agentic Access
  operation_count: 5
  slug: amazon-elastic-beanstalk-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://elasticbeanstalk.amazonaws.com
  baseurl_source: declared
  description: The Amazon Elastic Beanstalk AWS Elastic Beanstalk API API from Amazon Elastic Beanstalk — 1 operation(s) for amazon elastic beanstalk aws elastic beanstalk api.
  name: Amazon Elastic Beanstalk Amazon Elastic Beanstalk AWS Elastic Beanstalk API API
  slug: amazon-elastic-beanstalk-amazon-elastic-beanstalk-aws-elastic-beanstalk-api-api
- baseURL: https://elasticbeanstalk.amazonaws.com
  baseurl_source: declared
  description: 'The #CreateEnvironment API from Amazon Elastic Beanstalk — 1 operation(s) for #createenvironment.'
  name: 'Amazon Elastic Beanstalk #CreateEnvironment API'
  slug: amazon-elastic-beanstalk-createenvironment-api
- baseURL: https://elasticbeanstalk.amazonaws.com
  baseurl_source: declared
  description: 'The #DescribeEnvironments API from Amazon Elastic Beanstalk — 1 operation(s) for #describeenvironments.'
  name: 'Amazon Elastic Beanstalk #DescribeEnvironments API'
  slug: amazon-elastic-beanstalk-describeenvironments-api
- baseURL: https://elasticbeanstalk.amazonaws.com
  baseurl_source: declared
  description: 'The #UpdateEnvironment API from Amazon Elastic Beanstalk — 1 operation(s) for #updateenvironment.'
  name: 'Amazon Elastic Beanstalk #UpdateEnvironment API'
  slug: amazon-elastic-beanstalk-updateenvironment-api
arazzos:
- description: Confirm an existing application, launch an additional environment for it, and poll until Ready.
  name: Amazon Elastic Beanstalk Add Environment To Application
  slug: amazon-elastic-beanstalk-add-environment-to-application-workflow
- description: Resolve an application and inventory all of its environments with their status and health.
  name: Amazon Elastic Beanstalk Audit Application Environments
  slug: amazon-elastic-beanstalk-audit-application-environments-workflow
- description: Deploy an application version to a running environment and poll until the update completes.
  name: Amazon Elastic Beanstalk Deploy Version To Environment
  slug: amazon-elastic-beanstalk-deploy-version-to-environment-workflow
- description: Deploy a new version, poll the rollout, and roll back to the previous version if it fails.
  name: Amazon Elastic Beanstalk Deploy Version With Rollback
  slug: amazon-elastic-beanstalk-deploy-version-with-rollback-workflow
- description: Create an application, launch an environment for it, and poll until the environment is Ready.
  name: Amazon Elastic Beanstalk Provision Application And Environment
  slug: amazon-elastic-beanstalk-provision-application-environment-workflow
- description: Apply configuration option settings to a running environment and poll until the change settles.
  name: Amazon Elastic Beanstalk Update Environment Configuration
  slug: amazon-elastic-beanstalk-update-environment-configuration-workflow
artifact_total: 52
collections:
- collection_type: postman
  name: Amazon Elastic Beanstalk AWS Elastic Beanstalk API
  slug: postman-amazon-elastic-beanstalk
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Elastic Beanstalk AWS Elastic Beanstalk Amazon Elastic Beanstalk AWS Elastic Beanstalk API API
  slug: open-amazon-elastic-beanstalk-amazon-elastic-beanstalk-aws-elastic-beanstalk-api-api
- collection_type: open
  name: 'Amazon Elastic Beanstalk AWS Elastic Beanstalk Amazon Elastic Beanstalk AWS Elastic Beanstalk API #CreateEnvironment API'
  slug: open-amazon-elastic-beanstalk-createenvironment-api
- collection_type: open
  name: 'Amazon Elastic Beanstalk AWS Elastic Beanstalk Amazon Elastic Beanstalk AWS Elastic Beanstalk API #DescribeEnvironments API'
  slug: open-amazon-elastic-beanstalk-describeenvironments-api
- collection_type: open
  name: 'Amazon Elastic Beanstalk AWS Elastic Beanstalk Amazon Elastic Beanstalk AWS Elastic Beanstalk API #UpdateEnvironment API'
  slug: open-amazon-elastic-beanstalk-updateenvironment-api
- collection_type: open
  name: Amazon Elastic Beanstalk AWS Elastic Beanstalk API
  slug: open-amazon-elastic-beanstalk
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-elastic-beanstalk-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-elastic-beanstalk-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-elastic-beanstalk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-elastic-beanstalk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-elastic-beanstalk-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-elastic-beanstalk/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-beanstalk-add-environment-to-application-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-beanstalk-audit-application-environments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-beanstalk-deploy-version-to-environment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-beanstalk-deploy-version-with-rollback-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-beanstalk-provision-application-environment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-beanstalk-update-environment-configuration-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/elasticbeanstalk/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/elasticbeanstalk/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/elasticbeanstalk/
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
  type: Support
  url: https://aws.amazon.com/support/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/elasticbeanstalk/faqs/
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
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/elasticbeanstalk
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-elastic-beanstalk-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-elastic-beanstalk-vocabulary.yaml
created: '2024-01-15'
description: AWS Elastic Beanstalk is a platform-as-a-service (PaaS) that makes it easy to deploy, manage, and scale web applications and services. You simply upload your code and Elastic Beanstalk automatically handles the deployment, capacity provisioning, load balancing, auto-scaling, and application health monitoring.
examples:
- key_count: 8
  name: Amazon Elastic Beanstalk Application Description Example
  slug: amazon-elastic-beanstalk-application-description-example
- key_count: 1
  name: Amazon Elastic Beanstalk Application Description Message Example
  slug: amazon-elastic-beanstalk-application-description-message-example
- key_count: 1
  name: Amazon Elastic Beanstalk Application Descriptions Message Example
  slug: amazon-elastic-beanstalk-application-descriptions-message-example
- key_count: 2
  name: Amazon Elastic Beanstalk Environment Descriptions Message Example
  slug: amazon-elastic-beanstalk-environment-descriptions-message-example
- key_count: 10
  name: Amazon Elastic Beanstalk Environment Example
  slug: amazon-elastic-beanstalk-environment-example
features:
- description: Upload code and Elastic Beanstalk handles deployment automatically
  name: Automatic Deployment
- description: Automatically scale capacity up and down based on application needs
  name: Auto Scaling
- description: Monitor application health and performance with built-in dashboards
  name: Health Monitoring
- description: Support for Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker
  name: Multi-Language Support
- description: Manage multiple deployment environments (development, staging, production)
  name: Environment Management
finops:
- name: Amazon Elastic Beanstalk Finops
  service_category: API
  slug: amazon-elastic-beanstalk-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: ApplicationDescriptionMessage
  property_count: 1
  slug: amazon-elastic-beanstalk-application-description-message
- name: ApplicationDescription
  property_count: 8
  slug: amazon-elastic-beanstalk-application-description
- name: ApplicationDescriptionsMessage
  property_count: 1
  slug: amazon-elastic-beanstalk-application-descriptions-message
- name: EnvironmentDescriptionsMessage
  property_count: 2
  slug: amazon-elastic-beanstalk-environment-descriptions-message
- name: AWS Elastic Beanstalk Environment
  property_count: 21
  slug: amazon-elastic-beanstalk-environment
json_structures:
- name: Amazon Elastic Beanstalk Application Description Message Structure
  property_count: 1
  slug: amazon-elastic-beanstalk-application-description-message-structure
- name: Amazon Elastic Beanstalk Application Description Structure
  property_count: 8
  slug: amazon-elastic-beanstalk-application-description-structure
- name: Amazon Elastic Beanstalk Application Descriptions Message Structure
  property_count: 1
  slug: amazon-elastic-beanstalk-application-descriptions-message-structure
- name: Amazon Elastic Beanstalk Environment Descriptions Message Structure
  property_count: 2
  slug: amazon-elastic-beanstalk-environment-descriptions-message-structure
- name: Amazon Elastic Beanstalk Environment Structure
  property_count: 21
  slug: amazon-elastic-beanstalk-environment-structure
jsonld:
- class_count: 0
  name: Amazon Elastic Beanstalk Context
  property_count: 3
  slug: amazon-elastic-beanstalk-context
layout: provider
modified: '2026-05-19'
name: Amazon Elastic Beanstalk
nav: Providers
network: true
overview: 'Amazon Elastic Beanstalk publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Amazon Elastic Beanstalk AWS Elastic Beanstalk API API, #CreateEnvironment API, #DescribeEnvironments API, and 1 more. Tagged areas include Amazon Web Services, Auto-Scaling, Deployment, Elastic Beanstalk, and Platform-as-a-Service.


  The Amazon Elastic Beanstalk catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Elastic Beanstalk''s developer surface includes authentication, developer portal, documentation, engineering blog, developer console, signup flow, support, and 26 more developer resources.'
plans:
- name: Amazon Elastic Beanstalk Plans Pricing
  plan_count: 3
  slug: amazon-elastic-beanstalk-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Amazon Elastic Beanstalk Rate Limits
  slug: amazon-elastic-beanstalk-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Elastic Beanstalk API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-elastic-beanstalk-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon Elastic Beanstalk API Rules
  rule_count: 24
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 13
  slug: amazon-elastic-beanstalk-spectral-rules
score:
  band: strong
  composite: 59.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 44.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-elastic-beanstalk/refs/heads/main/screenshots/amazon-elastic-beanstalk-2026-06-20T171638.png
security:
- kind: authentication
  name: Amazon Elastic Beanstalk Authentication
  slug: amazon-elastic-beanstalk-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Elastic Beanstalk Domain Security
  slug: amazon-elastic-beanstalk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Elastic Beanstalk Vulnerability Disclosure
  slug: amazon-elastic-beanstalk-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Elastic Beanstalk Trust Center
  slug: amazon-elastic-beanstalk-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-elastic-beanstalk
tags:
- Amazon Web Services
- Auto-Scaling
- Deployment
- Elastic Beanstalk
- Platform-as-a-Service
- Web Applications
use_cases:
- description: Deploy and host web applications without managing infrastructure
  name: Web Application Hosting
- description: Deploy REST API backends with automatic scaling and load balancing
  name: API Backend Deployment
- description: Deploy containerized microservices using Docker or multi-container configurations
  name: Microservices Deployment
- description: Perform zero-downtime deployments using environment URL swapping
  name: Blue-Green Deployments
website: https://aws.amazon.com/elasticbeanstalk/
---
