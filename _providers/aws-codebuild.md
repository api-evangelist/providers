---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 38
  human_in_the_loop: 3
  name: Aws Codebuild Agentic Access
  operation_count: 52
  slug: aws-codebuild-agentic-access
  summary_line: 52 operations · 38 acting · 3 human-in-the-loop
api_count: 48
apis:
- baseURL: https://codebuild.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The AWS CodeBuild API API from AWS CodeBuild — 1 operation(s) for aws codebuild api.
  name: AWS CodeBuild AWS CodeBuild API
  slug: aws-codebuild-aws-codebuild-api-api
- baseURL: https://codebuild.us-east-1.amazonaws.com
  baseurl_source: declared
  description: 'The AWS CodeBuild #X Amz Target=CodeBuild 20161006.DeleteReport… API from AWS CodeBuild — 1 operation(s) for aws codebuild #x amz target=codebuild 20161006.deletereport….'
  name: 'AWS CodeBuild AWS CodeBuild #X Amz Target=CodeBuild 20161006.DeleteReport… API'
  slug: aws-codebuild-aws-codebuild-x-amz-target-codebuild-20161006-deletereport-api
- baseURL: https://codebuild.us-east-1.amazonaws.com
  baseurl_source: declared
  description: 'The AWS CodeBuild #X Amz Target=CodeBuild 20161006.ListBuilds… API from AWS CodeBuild — 1 operation(s) for aws codebuild #x amz target=codebuild 20161006.listbuilds….'
  name: 'AWS CodeBuild AWS CodeBuild #X Amz Target=CodeBuild 20161006.ListBuilds… API'
  slug: aws-codebuild-aws-codebuild-x-amz-target-codebuild-20161006-listbuilds-api
- baseURL: https://codebuild.us-east-1.amazonaws.com
  baseurl_source: declared
  description: 'The AWS CodeBuild #X Amz Target=CodeBuild 20161006.ListProjects… API from AWS CodeBuild — 1 operation(s) for aws codebuild #x amz target=codebuild 20161006.listprojects….'
  name: 'AWS CodeBuild AWS CodeBuild #X Amz Target=CodeBuild 20161006.ListProjects… API'
  slug: aws-codebuild-aws-codebuild-x-amz-target-codebuild-20161006-listprojects-api
- baseURL: https://codebuild.us-east-1.amazonaws.com
  baseurl_source: declared
  description: 'The AWS CodeBuild #X Amz Target=CodeBuild 20161006.ListReports… API from AWS CodeBuild — 1 operation(s) for aws codebuild #x amz target=codebuild 20161006.listreports….'
  name: 'AWS CodeBuild AWS CodeBuild #X Amz Target=CodeBuild 20161006.ListReports… API'
  slug: aws-codebuild-aws-codebuild-x-amz-target-codebuild-20161006-listreports-api
- baseURL: https://codebuild.us-east-1.amazonaws.com
  baseurl_source: declared
  description: 'The AWS CodeBuild #X Amz Target=CodeBuild 20161006.RetryBuild… API from AWS CodeBuild — 1 operation(s) for aws codebuild #x amz target=codebuild 20161006.retrybuild….'
  name: 'AWS CodeBuild AWS CodeBuild #X Amz Target=CodeBuild 20161006.RetryBuild… API'
  slug: aws-codebuild-aws-codebuild-x-amz-target-codebuild-20161006-retrybuild-api
- baseURL: https://codebuild.us-east-1.amazonaws.com
  baseurl_source: declared
  description: 'The AWS CodeBuild #X Amz Target=CodeBuild 20161006.StartBuild… API from AWS CodeBuild — 1 operation(s) for aws codebuild #x amz target=codebuild 20161006.startbuild….'
  name: 'AWS CodeBuild AWS CodeBuild #X Amz Target=CodeBuild 20161006.StartBuild… API'
  slug: aws-codebuild-aws-codebuild-x-amz-target-codebuild-20161006-startbuild-api
- baseURL: https://codebuild.us-east-1.amazonaws.com
  baseurl_source: declared
  description: 'The AWS CodeBuild #X Amz Target=CodeBuild 20161006.StopBuild API API from AWS CodeBuild — 1 operation(s) for aws codebuild #x amz target=codebuild 20161006.stopbuild api.'
  name: 'AWS CodeBuild AWS CodeBuild #X Amz Target=CodeBuild 20161006.StopBuild API'
  slug: aws-codebuild-aws-codebuild-x-amz-target-codebuild-20161006-stopbuild-api-api
- baseURL: https://codebuild.us-east-1.amazonaws.com
  baseurl_source: declared
  description: 'The AWS CodeBuild #X Amz Target=CodeBuild… API from AWS CodeBuild — 38 operation(s) for aws codebuild #x amz target=codebuild….'
  name: 'AWS CodeBuild AWS CodeBuild #X Amz Target=CodeBuild… API'
  slug: aws-codebuild-aws-codebuild-x-amz-target-codebuild-api
- baseURL: https://codebuild.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for starting, stopping, and viewing builds
  name: AWS CodeBuild Builds API
  slug: aws-codebuild-builds-api
- baseURL: https://codebuild.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for creating and managing build projects
  name: AWS CodeBuild Projects API
  slug: aws-codebuild-projects-api
artifact_total: 19
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
  href: https://raw.githubusercontent.com/api-evangelist/aws-codebuild/refs/heads/main/agentic-access/aws-codebuild-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-codebuild-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aws-codebuild/refs/heads/main/security/aws-codebuild-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aws-codebuild-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aws-codebuild/refs/heads/main/security/aws-codebuild-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-codebuild-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aws-codebuild/refs/heads/main/security/aws-codebuild-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aws-codebuild-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aws-codebuild/refs/heads/main/authentication/aws-codebuild-authentication.yml
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
modified: '2026-09-16'
name: AWS CodeBuild
nav: Providers
network: true
overview: 'AWS CodeBuild publishes 11 APIs on the [APIs.io](https://apis.io/) network, including AWS CodeBuild API, AWS CodeBuild #X Amz Target=CodeBuild 20161006.DeleteReport… API, AWS CodeBuild #X Amz Target=CodeBuild 20161006.ListBuilds… API, and 8 more. Tagged areas include Builds, CI/CD, Continuous Integration, Developer Tools, and DevOps.


  AWS CodeBuild''s developer surface includes authentication, documentation, API reference, pricing, CLI, support, and 10 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 57.2
    developer_ergonomics: 59.5
    discoverability: 71.4
    operational_transparency: 18.4
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
