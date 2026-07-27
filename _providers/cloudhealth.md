---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Cloudhealth Agentic Access
  operation_count: 10
  slug: cloudhealth-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 7
apis:
- description: GraphQL API exposed in the CloudHealth UI under Setup > Admin > GraphQL Explorer for programmatic interaction with the platform's reporting and asset data model.
  name: CloudHealth GraphQL API
  slug: cloudhealth-graphql-api
- description: Partner-specific REST endpoints for MSPs to provision customers, assign AWS/Azure accounts, manage custom price books, billing rules, and customer statements at scale.
  name: CloudHealth Partner API
  slug: cloudhealth-partner-api
- description: AWS account configuration management.
  name: CloudHealth AWS Accounts API
  slug: cloudhealth-aws-accounts-api
- description: Perspective (grouping) management.
  name: CloudHealth Perspectives API
  slug: cloudhealth-perspectives-api
- description: OLAP cost and usage reports.
  name: CloudHealth Reports API
  slug: cloudhealth-reports-api
- description: Asset search.
  name: CloudHealth Search API
  slug: cloudhealth-search-api
- description: Single sign-on configuration.
  name: CloudHealth SSO API
  slug: cloudhealth-sso-api
artifact_total: 17
collections:
- collection_type: open
  name: CloudHealth REST API
  slug: open-cloudhealth
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudhealth-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudhealth-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudhealth-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CloudHealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudhealthtech
- group: company
  title: ''
  type: Website
  url: https://www.vmware.com/products/cloud-infrastructure/tanzu-cloudhealth
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.cloudhealthtech.com/
- group: docs
  title: ''
  type: Product Documentation
  url: https://techdocs.broadcom.com/us/en/vmware-tanzu/cloudhealth/tanzu-cloudhealth/saas/tnz-cloudhealth/index.html
- group: auth
  title: ''
  type: Authentication
  url: https://apidocs.cloudhealthtech.com/#documentation_authenticating-api-requests
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.broadcom.com/company/legal/privacy/policy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudhealth-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudhealth-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://blogs.vmware.com/feed/
created: '2026-03-16'
description: CloudHealth (now VMware Tanzu CloudHealth, owned by Broadcom) is a multi-cloud financial and operational management platform. It provides cost visibility, optimization recommendations, asset inventory, custom perspectives (groupings), policies, governance, and partner/MSP billing workflows across AWS, Azure, GCP, Oracle, and data center environments. The platform exposes both a REST API and a GraphQL API for programmatic access to reports, assets, accounts, perspectives, tags, metrics, and partner customer provisioning.
finops:
- name: Cloudhealth Finops
  service_category: API
  slug: cloudhealth-finops
graphqls:
- description: GraphQL API exposed in the CloudHealth UI under Setup > Admin > GraphQL Explorer for programmatic interaction with the platform's reporting and asset data model.
  name: CloudHealth GraphQL API
  slug: cloudhealth-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudhealth.png
jsonld:
- class_count: 0
  name: Cloudhealth Context
  property_count: 5
  slug: cloudhealth-context
layout: provider
modified: '2026-05-19'
name: CloudHealth
nav: Providers
network: true
overview: 'CloudHealth publishes 5 APIs on the [APIs.io](https://apis.io/) network, including AWS Accounts API, Perspectives API, Reports API, and 2 more. Tagged areas include Cloud Cost, Cloud Governance, Cloud Management, Cost Optimization, and FinOps.


  The CloudHealth catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CloudHealth''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Cloudhealth Plans Pricing
  plan_count: 3
  slug: cloudhealth-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Cloudhealth Rate Limits
  slug: cloudhealth-rate-limits
rules:
- name: CloudHealth API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: cloudhealth-rules
score:
  band: developing
  composite: 46.3
  delta: 2.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.1
    developer_ergonomics: 21.7
    discoverability: 87.5
    governance: 26.3
    operational_transparency: 36.8
  previous_composite: 44.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/screenshots/cloudhealth-2026-06-20T174608.png
security:
- kind: authentication
  name: Cloudhealth Authentication
  slug: cloudhealth-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cloudhealth Domain Security
  slug: cloudhealth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudhealth
tags:
- Cloud Cost
- Cloud Governance
- Cloud Management
- Cost Optimization
- FinOps
- Multi-Cloud
website: https://www.vmware.com/products/cloud-infrastructure/tanzu-cloudhealth
---
