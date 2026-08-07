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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 2
  name: Cloudfront Agentic Access
  operation_count: 23
  slug: cloudfront-agentic-access
  summary_line: 23 operations · 11 acting · 2 human-in-the-loop
api_count: 7
apis:
- description: The AWS CloudFront REST API exposes operations for managing distributions (CreateDistribution, GetDistribution, UpdateDistribution, DeleteDistribution, ListDistributions), origins, cache policies, inv
  name: AWS CloudFront API (canonical)
  slug: canonical
- description: The CachePolicies API from CloudFront — 2 operation(s) for cachepolicies.
  name: CloudFront CachePolicies API
  slug: cloudfront-cachepolicies-api
- description: The Distributions API from CloudFront — 3 operation(s) for distributions.
  name: CloudFront Distributions API
  slug: cloudfront-distributions-api
- description: The Functions API from CloudFront — 2 operation(s) for functions.
  name: CloudFront Functions API
  slug: cloudfront-functions-api
- description: The Invalidations API from CloudFront — 2 operation(s) for invalidations.
  name: CloudFront Invalidations API
  slug: cloudfront-invalidations-api
- description: The OriginAccessControl API from CloudFront — 2 operation(s) for originaccesscontrol.
  name: CloudFront OriginAccessControl API
  slug: cloudfront-originaccesscontrol-api
- description: The PublicKeys API from CloudFront — 1 operation(s) for publickeys.
  name: CloudFront PublicKeys API
  slug: cloudfront-publickeys-api
artifact_total: 13
collections:
- collection_type: open
  name: Amazon CloudFront API
  slug: open-cloudfront
common:
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
created: '2024-01-01'
description: CloudFront is Amazon Web Services' content delivery network (CDN) for delivering data, video, applications, and APIs globally with low latency. This repository is the short-form profile for AWS CloudFront; the canonical AWS service profile lives at amazon-cloudfront in the API Evangelist Network. CloudFront's API is part of the AWS Service Reference and exposes operations for distributions, origins, cache behaviors, invalidations, origin access identities, functions, and Lambda@Edge.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudfront.png
layout: provider
modified: '2026-04-25'
name: CloudFront
nav: Providers
network: true
overview: 'CloudFront publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CachePolicies API, Distributions API, Functions API, and 3 more. Tagged areas include Alias, CDN, Caching, Content Delivery, and Edge Computing.


  CloudFront''s developer surface includes authentication, documentation, pricing, and 7 more developer resources.'
random_paper: 71
score:
  band: thin
  composite: 31.4
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 57.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
