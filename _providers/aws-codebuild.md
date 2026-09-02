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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aws Codebuild Agentic Access
  operation_count: 1
  slug: aws-codebuild-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The AWS CodeBuild API API from AWS CodeBuild — 1 operation(s) for aws codebuild api.
  name: AWS CodeBuild AWS CodeBuild API API
  slug: aws-codebuild-aws-codebuild-api-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS CodeBuild AWS CodeBuild API API
  slug: open-aws-codebuild-aws-codebuild-api-api
- collection_type: open
  name: AWS CodeBuild API
  slug: open-aws-codebuild
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-codebuild-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-codebuild-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-codebuild-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-codebuild-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-codebuild-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/codebuild/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/codebuild/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/codebuild/latest/APIReference/Welcome.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/codebuild/pricing/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html
- group: other
  title: ''
  type: Endpoints
  url: https://docs.aws.amazon.com/general/latest/gr/codebuild.html
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/codebuild/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
created: '2026-05-11'
description: AWS CodeBuild is a fully managed continuous integration build service that compiles source code, runs unit tests, and produces deployable artifacts. It eliminates the need to provision, manage, and scale build servers by providing prepackaged build environments for popular languages and tools, and scales automatically to meet peak build requests. The CodeBuild API uses AWS Signature Version 4 (SigV4) authentication and is accessed via SDKs, the AWS CLI, or direct HTTPS calls to regional service endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-codebuild.png
layout: provider
modified: '2026-05-11'
name: AWS CodeBuild
nav: Providers
network: true
overview: 'AWS CodeBuild publishes 1 API on the [APIs.io](https://apis.io/) network: AWS CodeBuild API API. Tagged areas include Builds, CI/CD, Continuous Integration, Developer Tools, and DevOps.


  AWS CodeBuild''s developer surface includes authentication, documentation, API reference, pricing, CLI, support, and 10 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 59.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 38.4
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
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-codebuild/refs/heads/main/screenshots/aws-codebuild-2026-06-20T172754.png
security:
- kind: authentication
  name: Aws Codebuild Authentication
  slug: aws-codebuild-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws Codebuild Domain Security
  slug: aws-codebuild-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Codebuild Vulnerability Disclosure
  slug: aws-codebuild-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Codebuild Trust Center
  slug: aws-codebuild-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-codebuild
tags:
- Builds
- CI/CD
- Continuous Integration
- Developer Tools
- DevOps
website: https://aws.amazon.com/codebuild/
---
