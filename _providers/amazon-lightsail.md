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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 151
  human_in_the_loop: 13
  name: Amazon Lightsail Agentic Access
  operation_count: 162
  slug: amazon-lightsail-agentic-access
  summary_line: 162 operations · 151 acting · 13 human-in-the-loop
api_count: 2
apis:
- baseURL: https://lightsail.us-east-1.amazonaws.com
  baseurl_source: declared
  description: 'The Amazon Lightsail API — 162 operations covering instances (virtual private servers), container services, object storage buckets, managed MySQL and PostgreSQL databases, block storage disks, static '
  name: Amazon Lightsail API
  slug: amazon-lightsail-instances-api
artifact_total: 33
collections:
- collection_type: postman
  name: Amazon Lightsail Instances API
  slug: postman-amazon-lightsail-instances-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Lightsail Instances API
  slug: open-amazon-lightsail-instances-api
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
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/agentic-access/amazon-lightsail-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-lightsail-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/security/amazon-lightsail-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-lightsail-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/security/amazon-lightsail-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-lightsail-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/security/amazon-lightsail-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-lightsail-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/authentication/amazon-lightsail-authentication.yml
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
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://lightsail.aws.amazon.com/
- group: start
  title: ''
  type: SignUp
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
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/security/amazon-lightsail-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/amazon-lightsail-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/rules/amazon-lightsail-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-lightsail-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/vocabulary/amazon-lightsail-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-lightsail-vocabulary.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/lightsail/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/Welcome.html
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/lightsail/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/lightsail/pricing/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/smithy/amazon-lightsail-2016-11-28.json
  title: ''
  type: Smithy
  url: smithy/amazon-lightsail-2016-11-28.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/packages/amazon-lightsail-packages.yml
  title: ''
  type: Packages
  url: packages/amazon-lightsail-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/packages/amazon-lightsail-packages.yml
  title: ''
  type: SDKs
  url: packages/amazon-lightsail-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/cli/amazon-lightsail-cli.yml
  title: ''
  type: CLI
  url: cli/amazon-lightsail-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/well-known/amazon-lightsail-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-lightsail-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/well-known/amazon-lightsail-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-lightsail-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/mcp/amazon-lightsail-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/amazon-lightsail-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/mcp/amazon-lightsail-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/amazon-lightsail-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/llms/amazon-lightsail-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-lightsail-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/conformance/amazon-lightsail-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amazon-lightsail-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/errors/amazon-lightsail-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amazon-lightsail-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/lifecycle/amazon-lightsail-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-lightsail-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/conventions/amazon-lightsail-conventions.yml
  title: ''
  type: Conventions
  url: conventions/amazon-lightsail-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/changelog/amazon-lightsail-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/amazon-lightsail-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/data-model/amazon-lightsail-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amazon-lightsail-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/plans/amazon-lightsail-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-lightsail-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/rate-limits/amazon-lightsail-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-lightsail-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/finops/amazon-lightsail-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-lightsail-finops.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/examples/amazon-lightsail-instance-example.json
  title: ''
  type: Examples
  url: examples/amazon-lightsail-instance-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/postman/amazon-lightsail-instances-api.postman_collection.json
  title: ''
  type: Postman
  url: postman/amazon-lightsail-instances-api.postman_collection.json
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://aws.amazon.com/security/
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
mcp_servers:
- description: ''
  name: Amazon Lightsail MCP Server
  slug: amazon-lightsail-mcp-server
modified: '2026-09-17'
name: Amazon Lightsail
nav: Providers
network: true
overview: 'Amazon Lightsail publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Compute, Virtual Private Server, Hosting, and Containers.


  The Amazon Lightsail catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Lightsail''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 45 more developer resources.'
plans:
- name: Amazon Lightsail Plans Pricing
  plan_count: 100
  slug: amazon-lightsail-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Amazon Lightsail Rate Limits
  slug: amazon-lightsail-rate-limits
rules:
- effective_rule_count: 3
  extends: []
  name: Amazon Lightsail API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 2
  slug: amazon-lightsail-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Amazon Lightsail API Rules
  rule_count: 23
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 14
  slug: amazon-lightsail-spectral-rules
score:
  band: exemplar
  composite: 72.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 72.5
    catalog_earned_first_party: 12.0
    catalog_gap: 42.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 17.7
  facets:
    access_clarity: 93.4
    contract_governance: 47.0
    contract_quality: 70.1
    developer_ergonomics: 81.5
    discoverability: 75.9
    operational_transparency: 47.4
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-lightsail/refs/heads/main/screenshots/amazon-lightsail-2026-06-20T171728.png
security:
- kind: authentication
  name: Amazon Lightsail Authentication
  slug: amazon-lightsail-authentication
  summary_line: sigv4 · 1 scheme
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
tags:
- Cloud
- Compute
- Virtual Private Server
- Hosting
- Containers
- Database
- Storage
- CDN
- Networking
- Infrastructure
- DevOps
use_cases:
- description: Host WordPress sites with pre-configured LAMP stacks at low, predictable cost.
  name: WordPress Hosting
- description: Develop and test web applications on simple cloud infrastructure.
  name: Web Application Development
- description: Power small business websites with affordable, managed cloud hosting.
  name: Small Business Websites
website: https://aws.amazon.com/lightsail/
---
