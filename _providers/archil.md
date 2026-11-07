---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://control.green.us-east-1.aws.prod.archil.com
  baseurl_source: declared
  description: Manage API keys (also called API tokens) used to authenticate Control Plane API requests. Distinct from disk tokens.
  name: Archil API Tokens API
  slug: archil-api-tokens-api
- baseURL: https://control.green.us-east-1.aws.prod.archil.com
  baseurl_source: declared
  description: Manage authorized users on disks
  name: Archil Disk Users API
  slug: archil-disk-users-api
- baseURL: https://control.green.us-east-1.aws.prod.archil.com
  baseurl_source: declared
  description: Create, read, update, and delete disks
  name: Archil Disks API
  slug: archil-disks-api
- baseURL: https://control.green.us-east-1.aws.prod.archil.com
  baseurl_source: declared
  description: Run commands on a disk without provisioning compute
  name: Archil Serverless Execution API
  slug: archil-serverless-execution-api
artifact_total: 23
collections:
- collection_type: postman
  name: Archil Control Plane API Tokens API
  slug: postman-archil-api-tokens-api
- collection_type: postman
  name: Archil Control Plane API Tokens Disk Users API
  slug: postman-archil-disk-users-api
- collection_type: postman
  name: Archil Control Plane API Tokens Disks API
  slug: postman-archil-disks-api
- collection_type: postman
  name: Archil Control Plane API Tokens Serverless Execution API
  slug: postman-archil-serverless-execution-api
- collection_type: open
  name: Archil Control Plane API Tokens API
  slug: open-archil-api-tokens-api
- collection_type: open
  name: Archil Control Plane API Tokens Disk Users API
  slug: open-archil-disk-users-api
- collection_type: open
  name: Archil Control Plane API Tokens Disks API
  slug: open-archil-disks-api
- collection_type: open
  name: Archil Control Plane API Tokens Serverless Execution API
  slug: open-archil-serverless-execution-api
common:
- group: commercial
  href: https://artifacts.apis.io/archil/plans/archil-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/archil-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/archil/capabilities/archil-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/archil-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/archil/overlays/archil-controlplane-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/archil-controlplane-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/archil/overview
- group: auth
  href: https://artifacts.apis.io/archil/security/archil-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/archil-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://archil.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.archil.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.archil.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.archil.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.archil.com/getting-started/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://console.archil.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@archil.com
- group: company
  title: ''
  type: Blog
  url: https://archil.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://archil.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://archil.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://archil.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/archil-data
- group: operate
  title: ''
  type: StatusPage
  url: https://status.archil.com
- group: auth
  title: ''
  type: Compliance
  url: https://docs.archil.com/details/security
- group: auth
  title: ''
  type: Security
  url: https://docs.archil.com/details/security
- group: agent
  href: https://artifacts.apis.io/archil/llms/archil-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/archil-llms.txt
- group: build
  href: https://artifacts.apis.io/archil/packages/archil-packages.yml
  title: ''
  type: Packages
  url: packages/archil-packages.yml
- group: build
  href: https://artifacts.apis.io/archil/packages/archil-packages.yml
  title: ''
  type: SDKs
  url: packages/archil-packages.yml
- group: build
  href: https://artifacts.apis.io/archil/cli/archil-cli.yml
  title: ''
  type: CLI
  url: cli/archil-cli.yml
- group: agent
  href: https://artifacts.apis.io/archil/mcp/archil-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/archil-mcp.yml
- group: operate
  href: https://artifacts.apis.io/archil/changelog/archil-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/archil-changelog.yml
- group: design
  href: https://artifacts.apis.io/archil/lifecycle/archil-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/archil-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/archil/conformance/archil-conformance.yml
  title: ''
  type: Conformance
  url: conformance/archil-conformance.yml
- group: auth
  href: https://artifacts.apis.io/archil/authentication/archil-authentication.yml
  title: ''
  type: Authentication
  url: authentication/archil-authentication.yml
- group: auth
  href: https://artifacts.apis.io/archil/security/archil-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/archil-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/archil/security/archil-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/archil-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/archil/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Archil is the cloud filesystem for AI. It turns an existing object-storage bucket (Amazon S3, Google Cloud Storage, Cloudflare R2, Azure Blob, MinIO, Wasabi, Backblaze B2, DigitalOcean Spaces) into an unlimited, POSIX-compatible local disk that thousands of machines can mount at once — live, in place, and faster than local disk. A single multi-tenant "disk" caches active data in a high-speed layer, supports copy-on-write branches and checkpoints for isolated agent and CI fan-out, and can run serverless bash and parallel grep directly against the data with no separate sandbox. Archil exposes a REST Control Plane API for managing disks, disk users, API tokens, and serverless execution, plus first-party TypeScript and Python SDKs, a `disk` CLI, a Linux `archil` mount CLI, a Kubernetes CSI driver, a Terraform provider, and an S3-compatible HTTP API. Founded 2024, backed by Felicis, Y Combinator, General Catalyst, Peak XV, and Standard Capital. Added to the API Evangelist network
  from the Felicis portfolio and enriched by the pipeline.
finops:
- has_sources: true
  method: derived
  name: Archil Finops
  primary_unit: gb-mo
  service_category: ''
  slug: archil-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/archil.png
layout: provider
modified: '2026-07-18'
name: Archil
nav: Providers
network: true
overview: 'Archil publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Tokens API, Disk Users API, Disks API, and 1 more. Tagged areas include Company, Cloud Storage, Filesystem, Object Storage, and Artificial Intelligence.


  The Archil catalog on APIs.io includes 1 Spectral governance ruleset.


  Archil''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Archil Plans Pricing
  plan_count: 5
  slug: archil-plans-pricing
- name: Archil Price Estimates
  plan_count: 0
  slug: archil-price-estimates
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Archil API Rules
  rule_count: 64
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 2
  slug: archil-rules
score:
  band: strong
  composite: 66.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 53.3
    developer_ergonomics: 74.4
    discoverability: 73.2
    operational_transparency: 36.8
  previous_composite: 66.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/archil/archil-2026-07-25T201028.png
security:
- kind: authentication
  name: Archil Authentication
  slug: archil-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Archil Domain Security
  slug: archil-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Archil Vulnerability Disclosure
  slug: archil-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Archil Trust Center
  slug: archil-trust-center
  summary_line: SOC 2 Type II
skill_count: 3
skills:
- name: Create an S3-backed disk and authorize a client
  slug: archil-create-and-mount-disk
- name: Manage Control Plane API tokens
  slug: archil-manage-api-tokens
- name: Run a command and search files on a disk (serverless)
  slug: archil-serverless-exec
slug: archil
tags:
- Company
- Cloud Storage
- Filesystem
- Object Storage
- Artificial Intelligence
- Infrastructure
- Developer Tools
- Serverless
- Data
- S3
website: https://archil.com
---
