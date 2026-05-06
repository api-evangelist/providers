---
aid: rackspace-technology
url: https://raw.githubusercontent.com/api-evangelist/rackspace-technology/refs/heads/main/apis.yml
name: Rackspace Technology
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud
  - Managed Services
  - Multicloud
  - Infrastructure
  - DevOps
description: Rackspace Technology is a multicloud solutions provider offering managed services, professional services, and consulting across cloud infrastructure, applications, data, AI, and cybersecurity. The company operates as a trusted operator of the full stack from governed private cloud to AI in production, with offerings spanning private, public, and hybrid cloud, VMware, OpenStack, Kubernetes, Microsoft 365, ERP/CRM, and security services. Rackspace exposes a broad set of public APIs covering ticketing, DNS, load balancing, monitoring, metrics, cloud orchestration, billing, identity, and customer service.
created: '2026-05-04'
modified: '2026-05-05'
specificationVersion: '0.19'
apis:
  - aid: rackspace-technology:ticketing-api
    name: Rackspace Ticketing API
    humanURL: https://docs.rackspace.com/reference/ticketing-rackspace-ticketing-api
    tags:
      - Ticketing
      - Support
    properties:
      - type: APIReference
        url: https://docs.rackspace.com/reference/ticketing-rackspace-ticketing-api
    description: The Rackspace Ticketing API (v2.0) lets customers and partners create, read, and manage support tickets programmatically.
  - aid: rackspace-technology:cloud-dns-api
    name: Rackspace Cloud DNS API
    humanURL: https://docs.rackspace.com/reference/rackspace-cloud-dns-api-10
    tags:
      - DNS
      - Networking
    properties:
      - type: APIReference
        url: https://docs.rackspace.com/reference/rackspace-cloud-dns-api-10
      - type: OpenAPI
        url: openapi/rackspace-cloud-dns.yaml
      - type: Documentation
        url: https://github.com/rackerlabs/docs-cloud-dns
      - type: JSONSchema
        url: json-schema/rackspace-cloud-dns-domain-schema.json
        title: Domain Schema
      - type: JSONSchema
        url: json-schema/rackspace-cloud-dns-record-schema.json
        title: Record Schema
      - type: JSONStructure
        url: json-structure/rackspace-cloud-dns-domain-structure.json
        title: Domain Structure
      - type: Examples
        url: examples/rackspace-cloud-dns-list-domains-example.json
        title: List Domains Example
      - type: Examples
        url: examples/rackspace-cloud-dns-create-domain-example.json
        title: Create Domain Example
    description: The Rackspace Cloud DNS API (1.0) provides programmatic management of DNS zones and records hosted on the Rackspace Cloud.
  - aid: rackspace-technology:load-balancers-api
    name: Rackspace Dedicated Load Balancer API
    humanURL: https://docs.rackspace.com/reference/load-balancers-api-30-dlbv3
    tags:
      - Load Balancing
      - Networking
    properties:
      - type: APIReference
        url: https://docs.rackspace.com/reference/load-balancers-api-30-dlbv3
      - type: Documentation
        url: https://github.com/rackerlabs/docs-dedicated-load-balancer-v3
      - type: RAML
        url: raml/rackspace-bpi-load-balancer-v2.raml
        title: BPI Load Balancer v2 RAML
      - type: RAML
        url: raml/rackspace-f5-load-balancer.raml
        title: F5 Load Balancer RAML
    description: The Dedicated Load Balancer V3 (dlbv3) API provisions and manages dedicated load balancers for Rackspace customers. Internal BPI and F5 load-balancer RAML specifications are also included for reference.
  - aid: rackspace-technology:metrics-api
    name: Rackspace Metrics API
    humanURL: https://docs.rackspace.com/reference/metrics-getting-started
    tags:
      - Metrics
      - Monitoring
    properties:
      - type: APIReference
        url: https://docs.rackspace.com/reference/metrics-getting-started
    description: The Rackspace Metrics API (2.0) ingests and queries time-series metric data for monitoring infrastructure and applications.
  - aid: rackspace-technology:monitoring-api
    name: Rackspace Monitoring API
    humanURL: https://docs.rackspace.com/reference/getting-started-monitoring
    tags:
      - Monitoring
      - Operations
    properties:
      - type: APIReference
        url: https://docs.rackspace.com/reference/getting-started-monitoring
      - type: Documentation
        url: https://github.com/rackerlabs/docs-cloud-monitoring
    description: The Rackspace Monitoring API (1.0) configures monitoring checks, alarms, and notification plans for cloud and dedicated infrastructure.
  - aid: rackspace-technology:cloud-orchestration-api
    name: Rackspace Cloud Orchestration API
    humanURL: https://docs.rackspace.com/reference/rackspace-cloud-orchestration-api-10
    tags:
      - Orchestration
      - Cloud
    properties:
      - type: APIReference
        url: https://docs.rackspace.com/reference/rackspace-cloud-orchestration-api-10
      - type: Documentation
        url: https://github.com/rackerlabs/docs-cloud-orchestration
    description: The Rackspace Cloud Orchestration API (1.0) deploys multi-resource cloud stacks via templates.
  - aid: rackspace-technology:cloud-feeds-api
    name: Rackspace Cloud Feeds API
    humanURL: https://docs.rackspace.com/reference/rackspace-cloud-feedstm-api-10
    tags:
      - Events
      - Feeds
    properties:
      - type: APIReference
        url: https://docs.rackspace.com/reference/rackspace-cloud-feedstm-api-10
      - type: SourceCode
        url: https://github.com/rackerlabs/cloudfeeds-catalog
        title: Cloud Feeds Catalog Service
      - type: XSD
        url: xsd/rackspace-cloud-feeds-catalog.xsd
        title: Feeds Catalog XSD
    description: The Rackspace Cloud Feeds API (1.0) provides Atom-style event feeds for cloud product activity and notifications.
  - aid: rackspace-technology:billing-api
    name: Rackspace Billing API
    humanURL: https://docs.rackspace.com/reference/billing-apiguide-v2
    tags:
      - Billing
      - Account
    properties:
      - type: APIReference
        url: https://docs.rackspace.com/reference/billing-apiguide-v2
    description: The Rackspace Billing API (V2) returns invoices, transactions, and account billing data programmatically.
  - aid: rackspace-technology:customer-service-api
    name: Rackspace Customer Service API
    humanURL: https://docs.rackspace.com/reference/customer-service-v1
    tags:
      - Customer
      - Account
    properties:
      - type: APIReference
        url: https://docs.rackspace.com/reference/customer-service-v1
      - type: OpenAPI
        url: openapi/rackspace-customer-service.yaml
      - type: Documentation
        url: https://github.com/rackerlabs/docs-customer-service
      - type: JSONSchema
        url: json-schema/rackspace-customer-service-customer-account-schema.json
        title: Customer Account Schema
      - type: Examples
        url: examples/rackspace-customer-service-list-accounts-example.json
        title: List Customer Accounts Example
    description: The Rackspace Customer Service API (4.24.0) manages customer accounts, contacts, and service relationships keyed by Rackspace Customer Number (RCN).
  - aid: rackspace-technology:customer-identity-api
    name: Rackspace Customer Identity API
    humanURL: https://docs.rackspace.com/reference/cloud-identity-v2-getting-started
    tags:
      - Identity
      - Authentication
    properties:
      - type: APIReference
        url: https://docs.rackspace.com/reference/cloud-identity-v2-getting-started
      - type: OpenAPI
        url: openapi/rackspace-cloud-identity.yaml
      - type: Documentation
        url: https://github.com/rackerlabs/docs-cloud-identity
      - type: JSONSchema
        url: json-schema/rackspace-cloud-identity-token-schema.json
        title: Token Schema
      - type: JSONSchema
        url: json-schema/rackspace-cloud-identity-user-schema.json
        title: User Schema
      - type: JSONStructure
        url: json-structure/rackspace-cloud-identity-token-structure.json
        title: Token Structure
      - type: Examples
        url: examples/rackspace-cloud-identity-authenticate-example.json
        title: Authenticate Example
      - type: SDK
        url: https://github.com/rackspace/gophercloud
        title: Go SDK (gophercloud)
      - type: SDK
        url: https://github.com/rackspace/php-opencloud
        title: PHP SDK (php-opencloud)
      - type: SDK
        url: https://github.com/rackspace/openstack.net
        title: .NET SDK
    description: The Rackspace Customer Identity API (Cloud Identity v2) issues authentication tokens and manages users, roles, and tenants for accessing Rackspace cloud APIs.
  - aid: rackspace-technology:offer-api
    name: Rackspace Offer API
    humanURL: https://docs.rackspace.com/reference/rackspace-offer-api-20
    tags:
      - Offers
      - Catalog
    properties:
      - type: APIReference
        url: https://docs.rackspace.com/reference/rackspace-offer-api-20
      - type: OpenAPI
        url: openapi/rackspace-offer.yaml
      - type: Documentation
        url: https://github.com/rackerlabs/docs-offerings
      - type: JSONSchema
        url: json-schema/rackspace-offer-offering-schema.json
        title: Offering Schema
      - type: Examples
        url: examples/rackspace-offer-get-offerings-example.json
        title: Get Offerings Example
    description: The Rackspace Offer API (2.0) exposes the catalog of product offers and their metadata.
common:
  - type: Website
    url: https://www.rackspace.com/
  - type: Documentation
    url: https://docs.rackspace.com/
  - type: APIReference
    url: https://docs.rackspace.com/reference/
  - type: Support
    url: https://support.rackspace.com/
  - type: GitHubOrganization
    url: https://github.com/rackspace
    title: Rackspace GitHub Org
  - type: GitHubOrganization
    url: https://github.com/rackerlabs
    title: RackerLabs GitHub Org
  - type: SDK
    url: https://github.com/rackspace/gophercloud
    title: Go SDK (gophercloud, archived)
  - type: SDK
    url: https://github.com/rackspace/php-opencloud
    title: PHP SDK (php-opencloud)
  - type: SDK
    url: https://github.com/rackspace/openstack.net
    title: .NET SDK (openstack.net)
  - type: SDK
    url: https://github.com/rackspace/jclouds
    title: Java SDK (jclouds, archived)
  - type: SDK
    url: https://github.com/rackspace/fog
    title: Ruby SDK (fog, archived)
  - type: CLI
    url: https://github.com/rackspace/rack
    title: Rack CLI (unmaintained)
  - type: Tools
    url: https://github.com/rackerlabs/repose
    title: Repose API Middleware Platform
  - type: Tools
    url: https://github.com/rackerlabs/api-checker
    title: API Checker (WADL contract validator)
  - type: Tools
    url: https://github.com/rackerlabs/mimic
    title: Mimic API Mock Service
  - type: Tools
    url: https://github.com/rackerlabs/atom-hopper
    title: Atom Hopper (Java ATOMpub Server, powers Cloud Feeds)
  - type: Tools
    url: https://github.com/rackerlabs/auter
    title: Auter Auto-Update Tool
  - type: Tools
    url: https://github.com/rackerlabs/scantron
    title: Scantron Distributed Scanner
  - type: Tools
    url: https://github.com/rackerlabs/configsnap
    title: Configsnap Linux State Tool
  - type: Tools
    url: https://github.com/rackerlabs/genestack
    title: Genestack Flex Cloud Platform
  - type: Tools
    url: https://github.com/rackerlabs/understack
    title: Understack Bare-Metal Stack
  - type: Tools
    url: https://github.com/rackerlabs/keystone-rxt
    title: Keystone RXT (Federated Keystone with Rackspace Global Auth)
  - type: Tools
    url: https://github.com/rackerlabs/external-dns-rackspace-webhook
    title: External-DNS Rackspace Cloud DNS Webhook
  - type: Tools
    url: https://github.com/rackerlabs/cert-manager-webhook-rackspace
    title: cert-manager Webhook for Rackspace Cloud DNS
  - type: Tools
    url: https://github.com/rackerlabs/terraform-provider-raxclouddns
    title: Terraform Provider for Rackspace Cloud DNS
  - type: Tools
    url: https://github.com/rackerlabs/terraform-provider-spot
    title: Terraform Provider for Rackspace Spot
  - type: Tools
    url: https://github.com/rackerlabs/spot-sdk
    title: Rackspace Spot SDK
  - type: SpectralRules
    url: rules/rackspace-technology-rules.yml
    title: Rackspace Technology Spectral Ruleset
  - type: NaftikoCapabilities
    url: capabilities/cloud-account-operations.yaml
    title: Cloud Account Operations Capability
  - type: JSONLD
    url: json-ld/rackspace-technology-context.jsonld
    title: Rackspace Technology JSON-LD Context
  - type: Vocabulary
    url: vocabulary/rackspace-technology-vocabulary.yml
    title: Rackspace Technology Vocabulary
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
---
