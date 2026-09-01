---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: API for creating and managing CloudShell environments — browser-based terminal sessions for AWS resource management.
  name: Amazon CloudShell API
  slug: amazon-cloudshell-api
artifact_total: 19
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-cloudshell-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-cloudshell-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-cloudshell-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/cloudshell/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cloudshell/latest/userguide/
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
  url: https://aws.amazon.com/blogs/developer/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudshell/
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-cloudshell
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-cloudshell-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudshell-vocabulary.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-cloudshell-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-cloudshell-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-cloudshell-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-cloudshell-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-cloudshell-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-cloudshell-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-cloudshell-lifecycle.yml
created: '2026-03-16'
description: AWS CloudShell is a browser-based terminal that enables users to manage and explore AWS resources directly from the AWS Management Console. Pre-authenticated, pre-installed with AWS CLI and dev tools, with 1 GB of persistent storage per region.
features:
- description: Sign in with AWS Console credentials — no additional authentication required.
  name: Pre-Authenticated Access
- description: Amazon Linux 2 environment with AWS CLI, SDKs, and development tools pre-installed.
  name: Pre-Installed Tools
- description: Up to 1 GB of persistent storage per AWS region for scripts and configurations.
  name: Persistent Storage
- description: Running commands in CloudShell incurs no extra charges beyond standard AWS service fees.
  name: No Additional Cost
- description: Upload and download files directly from the browser.
  name: File Management
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-cloudshell.png
integrations:
- description: Launch directly from any AWS Console page with existing credentials.
  name: AWS Management Console
- description: Pre-installed and pre-configured AWS CLI for all service access.
  name: AWS CLI
- description: CloudShell inherits permissions from the signed-in IAM user or role.
  name: AWS IAM
- description: Upload files to and download files from S3 using CloudShell.
  name: Amazon S3
layout: provider
mcp_servers:
- description: ''
  name: Amazon CloudShell MCP Server
  slug: amazon-cloudshell-mcp-server
modified: '2026-06-20'
name: Amazon CloudShell
nav: Providers
network: true
overview: 'Amazon CloudShell publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CloudShell, Terminal, CLI, and Browser-Based.


  The Amazon CloudShell catalog on APIs.io includes 1 Spectral governance ruleset.


  Amazon CloudShell''s developer surface includes developer portal, documentation, support, engineering blog, developer console, signup flow, YouTube channel, and 20 more developer resources.'
random_paper: 19
rules:
- effective_rule_count: 19
  extends: []
  name: Amazon CloudShell API Rules
  rule_count: 19
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 6
  slug: amazon-cloudshell-spectral-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 65.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 59.1
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 66.7
    governance: 59.1
    operational_transparency: 18.4
  previous_composite: 36.4
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-cloudshell/refs/heads/main/screenshots/amazon-cloudshell-2026-07-25T195948.png
security:
- kind: domain-security
  name: Amazon Cloudshell Domain Security
  slug: amazon-cloudshell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Cloudshell Vulnerability Disclosure
  slug: amazon-cloudshell-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Cloudshell Trust Center
  slug: amazon-cloudshell-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-cloudshell
tags:
- CloudShell
- Terminal
- CLI
- Browser-Based
use_cases:
- description: Execute AWS CLI commands from any browser without local setup.
  name: Quick CLI Access
- description: Run existing scripts with integrated AWS CLI documentation and auto-completion.
  name: Script Execution
- description: Reduce incident response times with seamless console-authenticated terminal access.
  name: Security Operations
- description: Provide consistent, pre-configured AWS environments for training and demonstrations.
  name: Training and Demos
website: https://aws.amazon.com/cloudshell/
---
