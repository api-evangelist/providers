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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 11
  human_in_the_loop: 2
  name: Cloudfront Agentic Access
  operation_count: 23
  slug: cloudfront-agentic-access
  summary_line: 23 operations · 11 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The AWS CloudFront REST API exposes operations for managing distributions (CreateDistribution, GetDistribution, UpdateDistribution, DeleteDistribution, ListDistributions), origins, cache policies, inv
  name: AWS CloudFront API (canonical)
  slug: canonical
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The CachePolicies API from CloudFront — 2 operation(s) for cachepolicies.
  name: CloudFront CachePolicies API
  slug: cloudfront-cachepolicies-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Distributions API from CloudFront — 3 operation(s) for distributions.
  name: CloudFront Distributions API
  slug: cloudfront-distributions-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Functions API from CloudFront — 2 operation(s) for functions.
  name: CloudFront Functions API
  slug: cloudfront-functions-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Invalidations API from CloudFront — 2 operation(s) for invalidations.
  name: CloudFront Invalidations API
  slug: cloudfront-invalidations-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The OriginAccessControl API from CloudFront — 2 operation(s) for originaccesscontrol.
  name: CloudFront OriginAccessControl API
  slug: cloudfront-originaccesscontrol-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The PublicKeys API from CloudFront — 1 operation(s) for publickeys.
  name: CloudFront PublicKeys API
  slug: cloudfront-publickeys-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon CloudFront CachePolicies API
  slug: open-cloudfront-cachepolicies-api
- collection_type: open
  name: Amazon CloudFront CachePolicies Distributions API
  slug: open-cloudfront-distributions-api
- collection_type: open
  name: Amazon CloudFront CachePolicies Functions API
  slug: open-cloudfront-functions-api
- collection_type: open
  name: Amazon CloudFront CachePolicies Invalidations API
  slug: open-cloudfront-invalidations-api
- collection_type: open
  name: Amazon CloudFront CachePolicies OriginAccessControl API
  slug: open-cloudfront-originaccesscontrol-api
- collection_type: open
  name: Amazon CloudFront CachePolicies PublicKeys API
  slug: open-cloudfront-publickeys-api
- collection_type: open
  name: Amazon CloudFront API
  slug: open-cloudfront
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cloudfront-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudfront-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudfront-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudfront-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudfront-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudfront-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/cloudfront/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cloudfront/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/cloudfront/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: Canonical
  url: https://github.com/api-evangelist/amazon-cloudfront
- group: build
  title: ''
  type: Packages
  url: packages/cloudfront-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cloudfront-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cloudfront-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://aws.amazon.com/.well-known/security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cloudfront-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cloudfront-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudfront-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudfront-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/programs/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudfront-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudfront-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudfront-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cloudfront-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cloudfront-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/cloudfront-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloudfront-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudfront-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudfront-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/vulnerability-reporting/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/developer/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/Welcome.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/networking-and-content-delivery/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
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
  type: SLA
  url: https://aws.amazon.com/cloudfront/sla/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/cloudfront/faqs/
created: '2024-01-01'
description: CloudFront is Amazon Web Services' content delivery network (CDN) for delivering data, video, applications, and APIs globally with low latency. This repository is the short-form profile for AWS CloudFront; the canonical AWS service profile lives at amazon-cloudfront in the API Evangelist Network. CloudFront's API is part of the AWS Service Reference and exposes operations for distributions, origins, cache behaviors, invalidations, origin access identities, functions, and Lambda@Edge.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudfront.png
layout: provider
mcp_servers:
- description: ''
  name: CloudFront MCP Server
  slug: cloudfront-mcp-server
modified: '2026-09-05'
name: CloudFront
nav: Providers
network: true
overview: 'CloudFront publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CachePolicies API, Distributions API, Functions API, and 3 more. Tagged areas include Alias, CDN, Caching, Content Delivery, and Edge Computing.


  CloudFront''s developer surface includes authentication, documentation, pricing, changelog, CLI, API reference, getting-started guide, and 35 more developer resources.'
plans:
- name: Cloudfront Plans Pricing
  plan_count: 5
  slug: cloudfront-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 12
  name: Cloudfront Rate Limits
  slug: cloudfront-rate-limits
score:
  band: strong
  composite: 66.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 37.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 50.3
    developer_ergonomics: 73.2
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 29.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudfront/refs/heads/main/screenshots/cloudfront-2026-06-20T174603.png
security:
- kind: authentication
  name: Cloudfront Authentication
  slug: cloudfront-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cloudfront Domain Security
  slug: cloudfront-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cloudfront Vulnerability Disclosure
  slug: cloudfront-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cloudfront Trust Center
  slug: cloudfront-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: cloudfront
tags:
- Alias
- CDN
- Caching
- Content Delivery
- Edge Computing
- Lambda@Edge
- Network
website: https://aws.amazon.com/cloudfront/
---
