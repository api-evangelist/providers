---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Cloudfront Agentic Access
  operation_count: 9
  slug: amazon-cloudfront-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: Operations for managing CloudFront distributions
  name: Amazon CloudFront Distributions API
  slug: amazon-cloudfront-distributions-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: Operations for managing CloudFront functions
  name: Amazon CloudFront Functions API
  slug: amazon-cloudfront-functions-api
- baseURL: https://cloudfront.amazonaws.com
  baseurl_source: declared
  description: Operations for managing cache invalidations
  name: Amazon CloudFront Invalidations API
  slug: amazon-cloudfront-invalidations-api
artifact_total: 60
collections:
- collection_type: postman
  name: Amazon CloudFront Distributions API
  slug: postman-amazon-cloudfront-distributions-api
- collection_type: postman
  name: Amazon CloudFront Distributions Functions API
  slug: postman-amazon-cloudfront-functions-api
- collection_type: postman
  name: Amazon CloudFront Distributions Invalidations API
  slug: postman-amazon-cloudfront-invalidations-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon CloudFront Distributions API
  slug: open-amazon-cloudfront-distributions-api
- collection_type: open
  name: Amazon CloudFront Distributions Functions API
  slug: open-amazon-cloudfront-functions-api
- collection_type: open
  name: Amazon CloudFront Distributions Invalidations API
  slug: open-amazon-cloudfront-invalidations-api
- collection_type: open
  name: Amazon CloudFront API
  slug: open-amazon-cloudfront
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-cloudfront-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-cloudfront/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-cloudfront-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-cloudfront-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-cloudfront-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-cloudfront-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/cloudfront/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/
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
  url: https://aws.amazon.com/blogs/networking-and-content-delivery/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudfront/
- group: start
  title: ''
  type: Signup
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
  url: https://stackoverflow.com/questions/tagged/amazon-cloudfront
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
  url: rules/amazon-cloudfront-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudfront-vocabulary.yaml
created: '2026-05-11'
description: Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds across 750+ globally dispersed Points of Presence.
examples:
- key_count: 9
  name: Cloudfront Cache Behavior Example
  slug: cloudfront-cache-behavior-example
- key_count: 13
  name: Cloudfront Distribution Config Example
  slug: cloudfront-distribution-config-example
- key_count: 6
  name: Cloudfront Distribution Example
  slug: cloudfront-distribution-example
- key_count: 6
  name: Cloudfront Distribution List Example
  slug: cloudfront-distribution-list-example
- key_count: 2
  name: Cloudfront Invalidation Batch Example
  slug: cloudfront-invalidation-batch-example
- key_count: 4
  name: Cloudfront Invalidation Example
  slug: cloudfront-invalidation-example
- key_count: 6
  name: Cloudfront Invalidation List Example
  slug: cloudfront-invalidation-list-example
- key_count: 5
  name: Cloudfront Origin Example
  slug: cloudfront-origin-example
features:
- description: Deliver content from 750+ globally distributed Points of Presence for low latency.
  name: Global Edge Network
- description: Built-in AWS Shield Standard protection for all CloudFront distributions at no extra cost.
  name: DDoS Protection
- description: Deploy serverless code at edge locations with CloudFront Functions and Lambda@Edge.
  name: Edge Functions
- description: Secure content delivery with HTTPS and field-level encryption capabilities.
  name: HTTPS Encryption
- description: Additional caching layer to reduce load on origins and improve cache hit rates.
  name: Origin Shield
finops:
- name: Amazon Cloudfront Finops
  service_category: API
  slug: amazon-cloudfront-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-cloudfront.png
integrations:
- description: Serve static content from S3 buckets through CloudFront distributions.
  name: Amazon S3
- description: Run Lambda functions at CloudFront edge locations for request customization.
  name: AWS Lambda@Edge
- description: Filter malicious traffic with WAF rules applied at the CloudFront edge.
  name: AWS WAF
- description: Use ACM SSL/TLS certificates with CloudFront distributions.
  name: AWS ACM
- description: Route traffic to CloudFront distributions using Route 53 aliases.
  name: Amazon Route 53
json_schemas:
- name: Amazon CloudFront Distribution
  property_count: 6
  slug: amazon-cloudfront-distribution
- name: CacheBehavior
  property_count: 9
  slug: cloudfront-cache-behavior
- name: DistributionConfig
  property_count: 13
  slug: cloudfront-distribution-config
- name: DistributionList
  property_count: 6
  slug: cloudfront-distribution-list
- name: Distribution
  property_count: 6
  slug: cloudfront-distribution
- name: InvalidationBatch
  property_count: 2
  slug: cloudfront-invalidation-batch
- name: InvalidationList
  property_count: 6
  slug: cloudfront-invalidation-list
- name: Invalidation
  property_count: 4
  slug: cloudfront-invalidation
- name: Origin
  property_count: 5
  slug: cloudfront-origin
json_structures:
- name: Cloudfront Cache Behavior Structure
  property_count: 9
  slug: cloudfront-cache-behavior-structure
- name: Cloudfront Distribution Config Structure
  property_count: 13
  slug: cloudfront-distribution-config-structure
- name: Cloudfront Distribution List Structure
  property_count: 6
  slug: cloudfront-distribution-list-structure
- name: Cloudfront Distribution Structure
  property_count: 6
  slug: cloudfront-distribution-structure
- name: Cloudfront Invalidation Batch Structure
  property_count: 2
  slug: cloudfront-invalidation-batch-structure
- name: Cloudfront Invalidation List Structure
  property_count: 6
  slug: cloudfront-invalidation-list-structure
- name: Cloudfront Invalidation Structure
  property_count: 4
  slug: cloudfront-invalidation-structure
- name: Cloudfront Origin Structure
  property_count: 5
  slug: cloudfront-origin-structure
jsonld:
- class_count: 8
  name: Amazon Cloudfront Context
  property_count: 40
  slug: amazon-cloudfront-context
layout: provider
modified: '2026-05-19'
name: Amazon CloudFront
nav: Providers
network: true
overview: 'Amazon CloudFront publishes 3 APIs on the [APIs.io](https://apis.io/) network: Distributions API, Functions API, and Invalidations API. Tagged areas include CloudFront, CDN, Content Delivery, and Edge.


  The Amazon CloudFront catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon CloudFront''s developer surface includes developer portal, documentation, support, engineering blog, developer console, signup flow, YouTube channel, and 16 more developer resources.'
plans:
- name: Amazon Cloudfront Plans Pricing
  plan_count: 1
  slug: amazon-cloudfront-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Amazon Cloudfront Rate Limits
  slug: amazon-cloudfront-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon CloudFront API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-cloudfront-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon CloudFront API Rules
  rule_count: 24
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 11
  slug: amazon-cloudfront-spectral-rules
score:
  band: strong
  composite: 61.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 81.5
    catalog_earned_first_party: 0.0
    catalog_gap: 33.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 28.8
    contract_quality: 67.3
    developer_ergonomics: 60.7
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 39.5
  previous_composite: 62.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-cloudfront/refs/heads/main/screenshots/amazon-cloudfront-2026-06-20T171615.png
security:
- kind: domain-security
  name: Amazon Cloudfront Domain Security
  slug: amazon-cloudfront-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Cloudfront Vulnerability Disclosure
  slug: amazon-cloudfront-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Cloudfront Trust Center
  slug: amazon-cloudfront-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-cloudfront
tags:
- CloudFront
- CDN
- Content Delivery
- Edge
use_cases:
- description: Fast, secure global content delivery for web applications.
  name: Website Acceleration
- description: Live and on-demand video streaming with Media Services integration.
  name: Video Streaming
- description: Low-latency API delivery with edge termination and WebSocket support.
  name: API Acceleration
- description: Scale patch and software update delivery globally to millions of endpoints.
  name: Software Distribution
website: https://aws.amazon.com/cloudfront/
---
