---
access_model:
  confidence: high
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
  - rate-limits
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
    idempotency: documented
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-11-06'
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
  phrasing_intents:
  - id: listCachePolicies
    intent: List cache policies
    question: Which cache policies are available to attach to my distributions?
  - id: createCachePolicy
    intent: Create a cache policy
    question: How do I define my own caching rules, like TTLs and cache keys?
  - id: getCachePolicy
    intent: Get a cache policy
    question: What TTLs and cache key settings does a specific cache policy use?
  - id: deleteCachePolicy
    intent: Delete a cache policy
    question: How do I remove a custom cache policy I don't use anymore?
  phrasing_ops: 4
  slug: cloudfront-cachepolicies-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Distributions API from CloudFront — 3 operation(s) for distributions.
  name: CloudFront Distributions API
  phrasing_intents:
  - id: CreateDistribution
    intent: Create a CloudFront distribution
    question: How do I set up a new CloudFront distribution in front of my origin?
  - id: ListDistributions
    intent: List CloudFront distributions
    question: Which CloudFront distributions exist in my AWS account?
  - id: DeleteDistribution
    intent: Delete a CloudFront distribution
    question: How do I permanently remove a CloudFront distribution I no longer need?
  - id: GetDistribution
    intent: Get a distribution's details and status
    question: Has my distribution finished deploying, or is it still in progress?
  - id: GetDistributionConfig
    intent: Get a distribution's configuration
    question: Where do I read just the configuration settings of a distribution before editing them?
  - id: UpdateDistribution
    intent: Update a distribution's configuration
    question: How do I change the settings of an existing CloudFront distribution?
  phrasing_ops: 6
  slug: cloudfront-distributions-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Functions API from CloudFront — 2 operation(s) for functions.
  name: CloudFront Functions API
  phrasing_intents:
  - id: CreateFunction
    intent: Create a CloudFront Function
    question: How do I write a new lightweight function that runs at the edge?
  - id: ListFunctions
    intent: List CloudFront Functions
    question: Which CloudFront Functions have I written in this account?
  - id: DeleteFunction
    intent: Delete a CloudFront Function
    question: How do I remove a CloudFront Function I no longer need?
  - id: GetFunction
    intent: Describe a CloudFront Function
    question: What stage and status is a particular CloudFront Function in?
  phrasing_ops: 4
  slug: cloudfront-functions-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Invalidations API from CloudFront — 2 operation(s) for invalidations.
  name: CloudFront Invalidations API
  phrasing_intents:
  - id: listInvalidations
    intent: List a distribution's cache invalidations
    question: Which cache invalidations have been run on my distribution?
  - id: createInvalidation
    intent: Invalidate cached content on a distribution
    question: How do I clear cached files from CloudFront after deploying new content?
  - id: getInvalidation
    intent: Check the status of a cache invalidation
    question: Has my cache invalidation finished yet?
  phrasing_ops: 3
  slug: cloudfront-invalidations-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The OriginAccessControl API from CloudFront — 2 operation(s) for originaccesscontrol.
  name: CloudFront OriginAccessControl API
  phrasing_intents:
  - id: CreateOriginAccessControl
    intent: Create an origin access control
    question: How do I lock down my S3 bucket so only CloudFront can read it?
  - id: ListOriginAccessControls
    intent: List origin access controls
    question: Which origin access controls have I set up for my S3 origins?
  - id: DeleteOriginAccessControl
    intent: Delete an origin access control
    question: How do I remove an origin access control I'm no longer using?
  - id: GetOriginAccessControl
    intent: Get an origin access control
    question: What signing behavior does a specific origin access control use?
  phrasing_ops: 4
  slug: cloudfront-originaccesscontrol-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Public Keys API from CloudFront — 1 operation(s) for public keys.
  name: CloudFront Public Keys API
  phrasing_intents:
  - id: CreatePublicKey
    intent: Upload a public key for signed URLs
    question: How do I upload a public key so CloudFront can verify signed URLs?
  - id: ListPublicKeys
    intent: List public keys for signed URLs
    question: Which public keys have I uploaded for signed URLs and cookies?
  phrasing_ops: 2
  slug: cloudfront-public-keys-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Anycast Ip List API from CloudFront — 2 operation(s) for anycast ip list.
  name: CloudFront Anycast Ip List API
  slug: cloudfront-anycast-ip-list-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Cache Policy API from CloudFront — 3 operation(s) for cache policy.
  name: CloudFront Cache Policy API
  slug: cloudfront-cache-policy-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Conflicting Alias API from CloudFront — 1 operation(s) for conflicting alias.
  name: CloudFront Conflicting Alias API
  slug: cloudfront-conflicting-alias-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Connection Function API from CloudFront — 7 operation(s) for connection function.
  name: CloudFront Connection Function API
  slug: cloudfront-connection-function-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Connection Group API from CloudFront — 4 operation(s) for connection group.
  name: CloudFront Connection Group API
  slug: cloudfront-connection-group-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Continuous Deployment Policy API from CloudFront — 3 operation(s) for continuous deployment policy.
  name: CloudFront Continuous Deployment Policy API
  slug: cloudfront-continuous-deployment-policy-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Delete Resource Policy API from CloudFront — 1 operation(s) for delete resource policy.
  name: CloudFront Delete Resource Policy API
  slug: cloudfront-delete-resource-policy-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Distribution Tenant API from CloudFront — 9 operation(s) for distribution tenant.
  name: CloudFront Distribution Tenant API
  slug: cloudfront-distribution-tenant-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Domain Association API from CloudFront — 1 operation(s) for domain association.
  name: CloudFront Domain Association API
  slug: cloudfront-domain-association-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Domain Conflicts API from CloudFront — 1 operation(s) for domain conflicts.
  name: CloudFront Domain Conflicts API
  slug: cloudfront-domain-conflicts-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Field Level Encryption API from CloudFront — 3 operation(s) for field level encryption.
  name: CloudFront Field Level Encryption API
  slug: cloudfront-field-level-encryption-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Field Level Encryption Profile API from CloudFront — 3 operation(s) for field level encryption profile.
  name: CloudFront Field Level Encryption Profile API
  slug: cloudfront-field-level-encryption-profile-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Get Resource Policy API from CloudFront — 1 operation(s) for get resource policy.
  name: CloudFront Get Resource Policy API
  slug: cloudfront-get-resource-policy-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Key Group API from CloudFront — 3 operation(s) for key group.
  name: CloudFront Key Group API
  slug: cloudfront-key-group-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Key Value Store API from CloudFront — 2 operation(s) for key value store.
  name: CloudFront Key Value Store API
  slug: cloudfront-key-value-store-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Managed Certificate API from CloudFront — 1 operation(s) for managed certificate.
  name: CloudFront Managed Certificate API
  slug: cloudfront-managed-certificate-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Origin Access Identity API from CloudFront — 3 operation(s) for origin access identity.
  name: CloudFront Origin Access Identity API
  slug: cloudfront-origin-access-identity-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Origin Request Policy API from CloudFront — 3 operation(s) for origin request policy.
  name: CloudFront Origin Request Policy API
  slug: cloudfront-origin-request-policy-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Put Resource Policy API from CloudFront — 1 operation(s) for put resource policy.
  name: CloudFront Put Resource Policy API
  slug: cloudfront-put-resource-policy-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Realtime Log Config API from CloudFront — 3 operation(s) for realtime log config.
  name: CloudFront Realtime Log Config API
  slug: cloudfront-realtime-log-config-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Response Headers Policy API from CloudFront — 3 operation(s) for response headers policy.
  name: CloudFront Response Headers Policy API
  slug: cloudfront-response-headers-policy-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Streaming Distribution API from CloudFront — 3 operation(s) for streaming distribution.
  name: CloudFront Streaming Distribution API
  slug: cloudfront-streaming-distribution-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Tagging API from CloudFront — 1 operation(s) for tagging.
  name: CloudFront Tagging API
  slug: cloudfront-tagging-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Trust Store API from CloudFront — 4 operation(s) for trust store.
  name: CloudFront Trust Store API
  slug: cloudfront-trust-store-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Verify Dns Configuration API from CloudFront — 1 operation(s) for verify dns configuration.
  name: CloudFront Verify Dns Configuration API
  slug: cloudfront-verify-dns-configuration-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: The Vpc Origin API from CloudFront — 2 operation(s) for vpc origin.
  name: CloudFront Vpc Origin API
  slug: cloudfront-vpc-origin-api
artifact_total: 54
collections:
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
  href: https://artifacts.apis.io/cloudfront/vendor-facets/cloudfront-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/cloudfront-vendor-facets.yml
- group: other
  href: https://artifacts.apis.io/cloudfront/overlays/cloudfront-publickeys-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudfront-publickeys-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudfront/capabilities/cloudfront-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cloudfront-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/cloudfront/agentic-access/cloudfront-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudfront-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cloudfront/security/cloudfront-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cloudfront-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cloudfront/security/cloudfront-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudfront-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cloudfront/security/cloudfront-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudfront-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cloudfront/authentication/cloudfront-authentication.yml
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
  href: https://artifacts.apis.io/cloudfront/packages/cloudfront-packages.yml
  title: ''
  type: Packages
  url: packages/cloudfront-packages.yml
- group: build
  href: https://artifacts.apis.io/cloudfront/packages/cloudfront-packages.yml
  title: ''
  type: SDKs
  url: packages/cloudfront-packages.yml
- group: agent
  href: https://artifacts.apis.io/cloudfront/well-known/cloudfront-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudfront-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://aws.amazon.com/.well-known/security.txt
- group: agent
  href: https://artifacts.apis.io/cloudfront/mcp/cloudfront-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cloudfront-mcp.yml
- group: build
  href: https://artifacts.apis.io/cloudfront/mcp/cloudfront-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cloudfront-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cloudfront/llms/cloudfront-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudfront-llms.txt
- group: design
  href: https://artifacts.apis.io/cloudfront/conformance/cloudfront-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudfront-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/programs/
- group: design
  href: https://artifacts.apis.io/cloudfront/errors/cloudfront-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudfront-error-codes.yml
- group: design
  href: https://artifacts.apis.io/cloudfront/lifecycle/cloudfront-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloudfront-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cloudfront/conventions/cloudfront-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloudfront-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloudfront/conventions/cloudfront-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cloudfront-conventions.yml
- group: operate
  href: https://artifacts.apis.io/cloudfront/changelog/cloudfront-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloudfront-changelog.yml
- group: build
  href: https://artifacts.apis.io/cloudfront/cli/cloudfront-cli.yml
  title: ''
  type: CLI
  url: cli/cloudfront-cli.yml
- group: design
  href: https://artifacts.apis.io/cloudfront/data-model/cloudfront-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudfront-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/cloudfront/plans/cloudfront-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudfront-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cloudfront/rate-limits/cloudfront-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloudfront-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/cloudfront/skills/_index.yml
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
finops:
- has_sources: true
  method: derived
  name: Cloudfront Finops
  primary_unit: distribution
  service_category: ''
  slug: cloudfront-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudfront.png
layout: provider
mcp_servers:
- description: Remote MCP server at aws-mcp.us-east-1.api.aws requiring an API key; 8 tools listed.
  name: CloudFront MCP Server
  slug: cloudfront-mcp-yml
modified: '2026-09-16'
name: CloudFront
nav: Providers
network: true
overview: 'CloudFront publishes 33 API contracts indexed on the [APIs.io](https://apis.io/) network, including CachePolicies API, Distributions API, Functions API, and 30 more. Tagged areas include Amazon Web Services, CDN, Caching, Content Delivery, and Edge Computing.


  The CloudFront catalog on APIs.io includes 1 Spectral governance ruleset.


  CloudFront''s developer surface includes authentication, documentation, pricing, changelog, CLI, API reference, getting-started guide, and 37 more developer resources.'
plans:
- name: Cloudfront Plans Pricing
  plan_count: 5
  slug: cloudfront-plans-pricing
- name: Cloudfront Price Estimates
  plan_count: 0
  slug: cloudfront-price-estimates
random_paper: 8
rate_limits:
- limit_count: 12
  name: Cloudfront Rate Limits
  slug: cloudfront-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: CloudFront API Rules
  rule_count: 60
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 13
  slug: cloudfront-rules
score:
  band: exemplar
  composite: 74.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 62.4
    developer_ergonomics: 73.2
    discoverability: 85.0
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 73.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 93.8
      total: 32
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cloudfront/cloudfront-2026-06-20T174603.png
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
skill_count: 3
skills:
- name: Invalidate cached CloudFront content
  slug: cloudfront-invalidate-cached-content
- name: Lock a CloudFront origin down with origin access control
  slug: cloudfront-lock-origin-with-oac
- name: Update a CloudFront distribution safely
  slug: cloudfront-update-distribution-safely
slug: cloudfront
tags:
- Amazon Web Services
- CDN
- Caching
- Content Delivery
- Edge Computing
- Lambda@Edge
- Networks
website: https://aws.amazon.com/cloudfront/
---
