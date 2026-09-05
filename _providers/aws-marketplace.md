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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Aws Marketplace Agentic Access
  operation_count: 13
  slug: aws-marketplace-agentic-access
  summary_line: 13 operations · 10 acting
api_count: 1
apis:
- description: REST API for AWS Marketplace sellers to programmatically view and update their product entities and change sets in the marketplace catalog.
  name: AWS Marketplace Catalog API
  slug: catalog-api
- description: API used by AWS Marketplace sellers of SaaS and container products to report customer usage and entitlements for billing.
  name: AWS Marketplace Metering Service API
  slug: metering-service
- description: API for AWS Marketplace sellers to determine the entitlement that a customer has to a paid AWS Marketplace product.
  name: AWS Marketplace Entitlement Service API
  slug: entitlement-service
- description: API for AWS Marketplace sellers to request and retrieve reports about sales, customer subscriptions, and disbursements.
  name: AWS Marketplace Commerce Analytics Service API
  slug: commerce-analytics-service
- baseURL: https://catalog.marketplace.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Change Sets API from AWS Marketplace — 4 operation(s) for change sets.
  name: AWS Marketplace Change Sets API
  slug: aws-marketplace-change-sets-api
- baseURL: https://catalog.marketplace.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Entities API from AWS Marketplace — 3 operation(s) for entities.
  name: AWS Marketplace Entities API
  slug: aws-marketplace-entities-api
- baseURL: https://catalog.marketplace.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Resource Policies API from AWS Marketplace — 3 operation(s) for resource policies.
  name: AWS Marketplace Resource Policies API
  slug: aws-marketplace-resource-policies-api
- baseURL: https://catalog.marketplace.us-east-1.amazonaws.com
  baseurl_source: declared
  description: The Tags API from AWS Marketplace — 3 operation(s) for tags.
  name: AWS Marketplace Tags API
  slug: aws-marketplace-tags-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Marketplace Catalog Change Sets API
  slug: open-aws-marketplace-change-sets-api
- collection_type: open
  name: AWS Marketplace Catalog Change Sets Entities API
  slug: open-aws-marketplace-entities-api
- collection_type: open
  name: AWS Marketplace Catalog Change Sets Resource Policies API
  slug: open-aws-marketplace-resource-policies-api
- collection_type: open
  name: AWS Marketplace Catalog Change Sets Tags API
  slug: open-aws-marketplace-tags-api
- collection_type: open
  name: AWS Marketplace Catalog API
  slug: open-aws-marketplace
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/aws-marketplace-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-marketplace-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-marketplace-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-marketplace-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-marketplace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-marketplace-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/marketplace/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/marketplace/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/marketplace/latest/APIReference/welcome.html
- group: docs
  title: ''
  type: Buyer Guide
  url: https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html
- group: docs
  title: ''
  type: Seller Guide
  url: https://docs.aws.amazon.com/marketplace/latest/userguide/what-is-marketplace.html
- group: build
  title: ''
  type: GitHub Samples
  url: https://github.com/aws-samples/aws-marketplace-api-samples
- group: start
  title: ''
  type: Signup
  url: https://aws.amazon.com/marketplace/management/signin
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/awsmarketplace/feed/
created: '2026-05-11'
description: AWS Marketplace is a curated digital catalog from Amazon Web Services that lets customers find, buy, deploy, and manage third-party software, SaaS, containers, machine images (AMIs), data products, and professional services that run on AWS. The AWS Marketplace Catalog API enables approved sellers to programmatically manage their products, change sets, and entities, while buyers can integrate procurement workflows with AWS billing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-marketplace.png
layout: provider
modified: '2026-05-11'
name: AWS Marketplace
nav: Providers
network: true
overview: 'AWS Marketplace publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Change Sets API, Entities API, Resource Policies API, and 1 more. Tagged areas include Cloud Marketplace, Procurement, Software-as-a-Service, Software Distribution, and Catalog.


  AWS Marketplace''s developer surface includes authentication, documentation, API reference, signup flow, engineering blog, and 9 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-marketplace/refs/heads/main/screenshots/aws-marketplace-2026-06-20T172754.png
security:
- kind: authentication
  name: Aws Marketplace Authentication
  slug: aws-marketplace-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws Marketplace Domain Security
  slug: aws-marketplace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Marketplace Vulnerability Disclosure
  slug: aws-marketplace-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Marketplace Trust Center
  slug: aws-marketplace-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-marketplace
tags:
- Cloud Marketplace
- Procurement
- Software-as-a-Service
- Software Distribution
- Catalog
website: https://aws.amazon.com/marketplace/
---
