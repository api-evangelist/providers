---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Amazon Amplify Agentic Access
  operation_count: 18
  slug: amazon-amplify-agentic-access
  summary_line: 18 operations · 10 acting
api_count: 1
apis:
- description: The Apps API from Amazon Amplify — 4 operation(s) for apps.
  name: Amazon Amplify Apps API
  slug: amazon-amplify-apps-api
artifact_total: 55
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Amplify REST Apps API
  slug: open-amazon-amplify-apps-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-amplify-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-amplify-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-amplify-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-amplify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-amplify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-amplify-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-amplify-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-amplify-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-amplify-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-amplify-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-amplify-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-amplify-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-amplify-lifecycle.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/amplify/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/amplify/
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
  url: https://aws.amazon.com/blogs/mobile/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws-amplify
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/amplify/
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: Status
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-amplify
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-amplify-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-amplify-vocabulary.yaml
created: '2024-01-15'
description: AWS Amplify is a set of tools and services for building secure, scalable full-stack applications powered by AWS. It provides frontend and mobile developers with a complete workflow for building, deploying, and hosting cloud-powered applications.
examples:
- key_count: 10
  name: Amazon Amplify App Example
  slug: amazon-amplify-app-example
- key_count: 6
  name: Amazon Amplify Branch Example
  slug: amazon-amplify-branch-example
- key_count: 5
  name: Amazon Amplify Createapprequest Example
  slug: amazon-amplify-createapprequest-example
- key_count: 1
  name: Amazon Amplify Createappresult Example
  slug: amazon-amplify-createappresult-example
- key_count: 3
  name: Amazon Amplify Createbranchrequest Example
  slug: amazon-amplify-createbranchrequest-example
- key_count: 2
  name: Amazon Amplify Createdomainassociationrequest Example
  slug: amazon-amplify-createdomainassociationrequest-example
- key_count: 1
  name: Amazon Amplify Getappresult Example
  slug: amazon-amplify-getappresult-example
- key_count: 2
  name: Amazon Amplify Listappsresult Example
  slug: amazon-amplify-listappsresult-example
- key_count: 3
  name: Amazon Amplify Productionbranch Example
  slug: amazon-amplify-productionbranch-example
- key_count: 2
  name: Amazon Amplify Updateapprequest Example
  slug: amazon-amplify-updateapprequest-example
features:
- description: Create, update, and delete Amplify apps connected to Git repositories with automated build and deployment settings.
  name: App Management
- description: Manage feature branches and environments with independent build configurations, environment variables, and preview URLs.
  name: Branch Management
- description: Trigger and monitor deployments across branches with build history, logs, and status tracking.
  name: Deployment Automation
- description: Associate custom domains with Amplify apps and manage SSL certificates and subdomain routing configurations.
  name: Domain Association
- description: Manage AWS backend environments linked to Amplify applications for full-stack cloud resource provisioning.
  name: Backend Environment Management
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-amplify.png
integrations:
- description: Connect Amplify apps to AWS CodeCommit repositories for source code hosting and automated deployments.
  name: AWS CodeCommit
- description: Link Amplify deployments to GitHub repositories with automatic builds triggered on pull requests and branch merges.
  name: GitHub
- description: Amplify hosting uses CloudFront for global CDN distribution of static assets and dynamic content.
  name: AWS CloudFront
- description: Configure custom domains for Amplify apps using Route 53 DNS management and SSL certificate provisioning.
  name: AWS Route 53
json_schemas:
- name: App
  property_count: 10
  slug: amazon-amplify-app
- name: Branch
  property_count: 6
  slug: amazon-amplify-branch
- name: CreateAppRequest
  property_count: 5
  slug: amazon-amplify-createapprequest
- name: CreateAppResult
  property_count: 1
  slug: amazon-amplify-createappresult
- name: CreateBranchRequest
  property_count: 3
  slug: amazon-amplify-createbranchrequest
- name: CreateDomainAssociationRequest
  property_count: 2
  slug: amazon-amplify-createdomainassociationrequest
- name: GetAppResult
  property_count: 1
  slug: amazon-amplify-getappresult
- name: ListAppsResult
  property_count: 2
  slug: amazon-amplify-listappsresult
- name: ProductionBranch
  property_count: 3
  slug: amazon-amplify-productionbranch
- name: UpdateAppRequest
  property_count: 2
  slug: amazon-amplify-updateapprequest
json_structures:
- name: Amazon Amplify App Structure
  property_count: 0
  slug: amazon-amplify-app-structure
- name: Amazon Amplify Branch Structure
  property_count: 0
  slug: amazon-amplify-branch-structure
- name: Amazon Amplify Createapprequest Structure
  property_count: 0
  slug: amazon-amplify-createapprequest-structure
- name: Amazon Amplify Createappresult Structure
  property_count: 0
  slug: amazon-amplify-createappresult-structure
- name: Amazon Amplify Createbranchrequest Structure
  property_count: 0
  slug: amazon-amplify-createbranchrequest-structure
- name: Amazon Amplify Createdomainassociationrequest Structure
  property_count: 0
  slug: amazon-amplify-createdomainassociationrequest-structure
- name: Amazon Amplify Getappresult Structure
  property_count: 0
  slug: amazon-amplify-getappresult-structure
- name: Amazon Amplify Listappsresult Structure
  property_count: 0
  slug: amazon-amplify-listappsresult-structure
- name: Amazon Amplify Productionbranch Structure
  property_count: 0
  slug: amazon-amplify-productionbranch-structure
- name: Amazon Amplify Updateapprequest Structure
  property_count: 0
  slug: amazon-amplify-updateapprequest-structure
jsonld:
- class_count: 0
  name: Amazon Amplify Context
  property_count: 10
  slug: amazon-amplify-context
layout: provider
mcp_servers:
- description: ''
  name: amazon-amplify-mcp.yml
  slug: amazon-amplify-mcpyml
modified: '2026-06-20'
name: Amazon Amplify
nav: Providers
network: true
overview: 'Amazon Amplify publishes 1 API on the [APIs.io](https://apis.io/) network: Apps API. Tagged areas include Frontend, Full Stack, Hosting, Mobile Development, and Web Applications.


  The Amazon Amplify catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Amplify''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 24 more developer resources.'
random_paper: 17
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Amplify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-amplify-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Amazon Amplify API Rules
  rule_count: 14
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 7
  slug: amazon-amplify-spectral-rules
score:
  band: developing
  composite: 50.0
  delta: -4.4
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 41.7
    contract_quality: 74.1
    developer_ergonomics: 45.2
    discoverability: 87.0
    governance: 41.7
    operational_transparency: 2.6
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-amplify/refs/heads/main/screenshots/amazon-amplify-2026-07-25T195912.png
security:
- kind: authentication
  name: Amazon Amplify Authentication
  slug: amazon-amplify-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Amplify Domain Security
  slug: amazon-amplify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Amplify Vulnerability Disclosure
  slug: amazon-amplify-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Amplify Trust Center
  slug: amazon-amplify-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-amplify
tags:
- Frontend
- Full Stack
- Hosting
- Mobile Development
- Web Applications
use_cases:
- description: Automate build and deployment workflows for frontend apps by programmatically managing Amplify apps and branch deployments.
  name: CI/CD Pipeline Automation
- description: Manage development, staging, and production environments as separate branches with independent configurations.
  name: Multi-Environment Management
- description: Provision and configure Amplify hosting environments as part of infrastructure-as-code pipelines using the REST API.
  name: Infrastructure as Code
- description: Integrate Amplify app management into internal developer portals for self-service application deployment and hosting.
  name: Developer Portal Integration
website: https://aws.amazon.com/amplify/
---
