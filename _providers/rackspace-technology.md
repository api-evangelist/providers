---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 27
  human_in_the_loop: 2
  name: Rackspace Technology Agentic Access
  operation_count: 77
  slug: rackspace-technology-agentic-access
  summary_line: 77 operations · 27 acting · 2 human-in-the-loop
api_count: 26
apis:
- description: The Rackspace Ticketing API (v2.0) lets customers and partners create, read, and manage support tickets programmatically.
  name: Rackspace Ticketing API
  slug: ticketing-api
- description: The Dedicated Load Balancer V3 (dlbv3) API provisions and manages dedicated load balancers for Rackspace customers. Internal BPI and F5 load-balancer RAML specifications are also included for referenc
  name: Rackspace Dedicated Load Balancer API
  slug: load-balancers-api
- description: The Rackspace Metrics API (2.0) ingests and queries time-series metric data for monitoring infrastructure and applications.
  name: Rackspace Metrics API
  slug: metrics-api
- description: The Rackspace Monitoring API (1.0) configures monitoring checks, alarms, and notification plans for cloud and dedicated infrastructure.
  name: Rackspace Monitoring API
  slug: monitoring-api
- description: The Rackspace Cloud Orchestration API (1.0) deploys multi-resource cloud stacks via templates.
  name: Rackspace Cloud Orchestration API
  slug: cloud-orchestration-api
- description: The Rackspace Cloud Feeds API (1.0) provides Atom-style event feeds for cloud product activity and notifications.
  name: Rackspace Cloud Feeds API
  slug: cloud-feeds-api
- description: The Rackspace Billing API (V2) returns invoices, transactions, and account billing data programmatically.
  name: Rackspace Billing API
  slug: billing-api
- description: Customer contact operations.
  name: Rackspace Technology Contacts API
  slug: rackspace-technology-contacts-api
- description: Currency lookup.
  name: Rackspace Technology Currency API
  slug: rackspace-technology-currency-api
- description: Customer-account lookup and history operations.
  name: Rackspace Technology CustomerAccounts API
  slug: rackspace-technology-customeraccounts-api
- description: DNS domain (zone) operations.
  name: Rackspace Technology Domains API
  slug: rackspace-technology-domains-api
- description: Per-account usage limits and rate caps.
  name: Rackspace Technology Limits API
  slug: rackspace-technology-limits-api
- description: Resource-level customer metadata.
  name: Rackspace Technology Metadata API
  slug: rackspace-technology-metadata-api
- description: Multi-factor authentication setup and operations.
  name: Rackspace Technology MultiFactor API
  slug: rackspace-technology-multifactor-api
- description: Offering catalog operations.
  name: Rackspace Technology Offerings API
  slug: rackspace-technology-offerings-api
- description: Phone PIN operations for verbal account verification.
  name: Rackspace Technology PhonePin API
  slug: rackspace-technology-phonepin-api
- description: Commit and volume pricing grid operations.
  name: Rackspace Technology Pricing API
  slug: rackspace-technology-pricing-api
- description: Product catalog operations.
  name: Rackspace Technology Products API
  slug: rackspace-technology-products-api
- description: DNS record operations within a domain.
  name: Rackspace Technology Records API
  slug: rackspace-technology-records-api
- description: Reverse DNS (PTR) record operations.
  name: Rackspace Technology ReverseDNS API
  slug: rackspace-technology-reversedns-api
- description: Global and tenant role assignments.
  name: Rackspace Technology Roles API
  slug: rackspace-technology-roles-api
- description: Secret question and answer operations.
  name: Rackspace Technology SecretQA API
  slug: rackspace-technology-secretqa-api
- description: Tenant (account) operations.
  name: Rackspace Technology Tenants API
  slug: rackspace-technology-tenants-api
- description: Authentication and token validation operations.
  name: Rackspace Technology Tokens API
  slug: rackspace-technology-tokens-api
- description: User account operations.
  name: Rackspace Technology Users API
  slug: rackspace-technology-users-api
- description: Service version metadata.
  name: Rackspace Technology Versions API
  slug: rackspace-technology-versions-api
artifact_total: 50
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rackspace-technology-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rackspace-technology-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rackspace-technology-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rackspace-technology-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rackspace-technology-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rackspace-technology
- group: company
  title: ''
  type: Website
  url: https://www.rackspace.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rackspace.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rackspace.com/reference/
- group: operate
  title: ''
  type: Support
  url: https://support.rackspace.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rackspace.com/blog/feed
- group: build
  title: Rackspace GitHub Org
  type: GitHubOrganization
  url: https://github.com/rackspace
- group: build
  title: RackerLabs GitHub Org
  type: GitHubOrganization
  url: https://github.com/rackerlabs
- group: build
  title: Go SDK (gophercloud, archived)
  type: SDKs
  url: https://github.com/rackspace/gophercloud
- group: build
  title: PHP SDK (php-opencloud)
  type: SDKs
  url: https://github.com/rackspace/php-opencloud
- group: build
  title: .NET SDK (openstack.net)
  type: SDKs
  url: https://github.com/rackspace/openstack.net
- group: build
  title: Java SDK (jclouds, archived)
  type: SDKs
  url: https://github.com/rackspace/jclouds
- group: build
  title: Ruby SDK (fog, archived)
  type: SDKs
  url: https://github.com/rackspace/fog
- group: build
  title: Rack CLI (unmaintained)
  type: CLI
  url: https://github.com/rackspace/rack
- group: build
  title: Repose API Middleware Platform
  type: Tools
  url: https://github.com/rackerlabs/repose
- group: build
  title: API Checker (WADL contract validator)
  type: Tools
  url: https://github.com/rackerlabs/api-checker
- group: build
  title: Mimic API Mock Service
  type: Tools
  url: https://github.com/rackerlabs/mimic
- group: build
  title: Atom Hopper (Java ATOMpub Server, powers Cloud Feeds)
  type: Tools
  url: https://github.com/rackerlabs/atom-hopper
- group: build
  title: Auter Auto-Update Tool
  type: Tools
  url: https://github.com/rackerlabs/auter
- group: build
  title: Scantron Distributed Scanner
  type: Tools
  url: https://github.com/rackerlabs/scantron
- group: build
  title: Configsnap Linux State Tool
  type: Tools
  url: https://github.com/rackerlabs/configsnap
- group: build
  title: Genestack Flex Cloud Platform
  type: Tools
  url: https://github.com/rackerlabs/genestack
- group: build
  title: Understack Bare-Metal Stack
  type: Tools
  url: https://github.com/rackerlabs/understack
- group: build
  title: Keystone RXT (Federated Keystone with Rackspace Global Auth)
  type: Tools
  url: https://github.com/rackerlabs/keystone-rxt
- group: build
  title: External-DNS Rackspace Cloud DNS Webhook
  type: Tools
  url: https://github.com/rackerlabs/external-dns-rackspace-webhook
- group: build
  title: cert-manager Webhook for Rackspace Cloud DNS
  type: Tools
  url: https://github.com/rackerlabs/cert-manager-webhook-rackspace
- group: build
  title: Terraform Provider for Rackspace Cloud DNS
  type: Tools
  url: https://github.com/rackerlabs/terraform-provider-raxclouddns
- group: build
  title: Terraform Provider for Rackspace Spot
  type: Tools
  url: https://github.com/rackerlabs/terraform-provider-spot
- group: build
  title: Rackspace Spot SDK
  type: Tools
  url: https://github.com/rackerlabs/spot-sdk
- group: design
  title: Rackspace Technology Spectral Ruleset
  type: SpectralRules
  url: rules/rackspace-technology-rules.yml
- group: design
  title: Rackspace Technology JSON-LD Context
  type: JSONLD
  url: json-ld/rackspace-technology-context.jsonld
- group: design
  title: Rackspace Technology Vocabulary
  type: Vocabulary
  url: vocabulary/rackspace-technology-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.rackspace.com/llms.txt
created: '2026-05-04'
description: Rackspace Technology is a multicloud solutions provider offering managed services, professional services, and consulting across cloud infrastructure, applications, data, AI, and cybersecurity. The company operates as a trusted operator of the full stack from governed private cloud to AI in production, with offerings spanning private, public, and hybrid cloud, VMware, OpenStack, Kubernetes, Microsoft 365, ERP/CRM, and security services. Rackspace exposes a broad set of public APIs covering ticketing, DNS, load balancing, monitoring, metrics, cloud orchestration, billing, identity, and customer service.
examples:
- key_count: 2
  name: Rackspace Cloud Dns Create Domain Example
  slug: rackspace-cloud-dns-create-domain-example
- key_count: 2
  name: Rackspace Cloud Dns List Domains Example
  slug: rackspace-cloud-dns-list-domains-example
- key_count: 2
  name: Rackspace Cloud Identity Authenticate Example
  slug: rackspace-cloud-identity-authenticate-example
- key_count: 2
  name: Rackspace Customer Service List Accounts Example
  slug: rackspace-customer-service-list-accounts-example
- key_count: 2
  name: Rackspace Offer Get Offerings Example
  slug: rackspace-offer-get-offerings-example
finops:
- name: Rackspace Technology Finops
  service_category: API
  slug: rackspace-technology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rackspace-technology.png
json_schemas:
- name: Domain
  property_count: 9
  slug: rackspace-cloud-dns-domain
- name: Record
  property_count: 9
  slug: rackspace-cloud-dns-record
- name: Token
  property_count: 3
  slug: rackspace-cloud-identity-token
- name: User
  property_count: 7
  slug: rackspace-cloud-identity-user
- name: CustomerAccount
  property_count: 7
  slug: rackspace-customer-service-customer-account
- name: Offering
  property_count: 8
  slug: rackspace-offer-offering
json_structures:
- name: Rackspace Cloud Dns Domain Structure
  property_count: 0
  slug: rackspace-cloud-dns-domain-structure
- name: Rackspace Cloud Identity Token Structure
  property_count: 0
  slug: rackspace-cloud-identity-token-structure
jsonld:
- class_count: 42
  name: Rackspace Technology Context
  property_count: 9
  slug: rackspace-technology-context
layout: provider
modified: '2026-05-19'
name: Rackspace Technology
nav: Providers
network: true
overview: 'Rackspace Technology publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Currency API, CustomerAccounts API, and 16 more. Tagged areas include Cloud, Managed Services, Multicloud, Infrastructure, and DevOps.


  The Rackspace Technology catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Rackspace Technology''s developer surface includes authentication, documentation, API reference, support, engineering blog, CLI, tooling, and 31 more developer resources.'
plans:
- name: Rackspace Technology Plans Pricing
  plan_count: 1
  slug: rackspace-technology-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 2
  name: Rackspace Technology Rate Limits
  slug: rackspace-technology-rate-limits
rules:
- name: Rackspace Technology API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rackspace-technology-jsonschema-spectral-rules
- name: Rackspace Technology API Rules
  rule_count: 34
  severity_counts:
    error: 16
    hint: 2
    info: 0
    warn: 16
  slug: rackspace-technology-rules
score:
  band: developing
  composite: 43.0
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 28.8
    developer_ergonomics: 54.3
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 19
      marker_coverage: 100.0
      total: 19
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rackspace-technology/refs/heads/main/screenshots/rackspace-technology-2026-06-20T192513.png
security:
- kind: authentication
  name: Rackspace Technology Authentication
  slug: rackspace-technology-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rackspace Technology Domain Security
  slug: rackspace-technology-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rackspace Technology Vulnerability Disclosure
  slug: rackspace-technology-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Rackspace Technology Trust Center
  slug: rackspace-technology-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: rackspace-technology
tags:
- Cloud
- Managed Services
- Multicloud
- Infrastructure
- DevOps
website: https://www.rackspace.com/
---
