---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 304
  human_in_the_loop: 8
  name: Imperva Agentic Access
  operation_count: 414
  slug: imperva-agentic-access
  summary_line: 414 operations · 304 acting · 8 human-in-the-loop
api_count: 15
apis:
- description: 'API for managing Imperva''s API security product, providing visibility into API traffic, detection of API vulnerabilities and threats, and enforcement of API access policies. Integrates with cloud WAF '
  name: Imperva API Security
  slug: api-security
- description: API for managing Imperva's Data Security Fabric (DSF) product, enabling automated deployment and configuration of data security monitoring, auditing, and analytics across cloud and on-premises data re
  name: Imperva Data Security Fabric API
  slug: data-security-fabric-api
- description: Add, delete, and modify accounts. Get account details.
  name: Imperva Account Management API
  slug: imperva-account-management-api
- description: The Administration API from Imperva — 8 operation(s) for administration.
  name: Imperva Administration API
  slug: imperva-administration-api
- description: The Auth API from Imperva — 2 operation(s) for auth.
  name: Imperva Auth API
  slug: imperva-auth-api
- description: The Conf API from Imperva — 126 operation(s) for conf.
  name: Imperva Conf API
  slug: imperva-conf-api
- description: Generate dummy notifications to test system alerts.
  name: Imperva DDoS for Networks Test Alerts API
  slug: imperva-ddos-for-networks-test-alerts-api
- description: Manage IP Protection over TCP/IP settings.
  name: Imperva DDoS Protection for Individual IPs API
  slug: imperva-ddos-protection-for-individual-ips-api
- description: The Experimental API from Imperva — 24 operation(s) for experimental.
  name: Imperva Experimental API
  slug: imperva-experimental-api
- description: Implement integrations with the Imperva service.
  name: Imperva Integrations API
  slug: imperva-integrations-api
- description: Provision Login Protect users and configure protected pages.
  name: Imperva Login Protect API
  slug: imperva-login-protect-api
- description: The Management API from Imperva — 2 operation(s) for management.
  name: Imperva Management API
  slug: imperva-management-api
- description: Add, remove, and update sites.
  name: Imperva Site Management API
  slug: imperva-site-management-api
- description: The Status API from Imperva — 1 operation(s) for status.
  name: Imperva Status API
  slug: imperva-status-api
- description: Retrieve traffic statistics and logs for sites or accounts.
  name: Imperva Traffic Statistics and Logs API
  slug: imperva-traffic-statistics-and-logs-api
artifact_total: 32
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/imperva-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imperva-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/imperva-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.imperva.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.imperva.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/imperva
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/imperva
- group: other
  title: ''
  type: X
  url: https://x.com/imperva
- group: company
  title: ''
  type: Blog
  url: https://www.imperva.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.imperva.com/products/plans/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.imperva.com
- group: commercial
  title: ''
  type: Plans
  url: plans/imperva-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/imperva-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/imperva-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/imperva-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/imperva-context.jsonld
created: '2026-06-12'
description: Imperva (a Thales company) is a cybersecurity company providing cloud-based and on-premises application security, data security, and network security solutions. Their developer APIs cover cloud WAF management, DDoS protection, API security, advanced bot protection, and data security fabric for enterprises. Developers can manage sites, policies, configurations, and analytics programmatically via REST APIs authenticated with API keys. Imperva also provides a Python SDK (imperva-sdk) for the SecureSphere on-premises MX platform, a Terraform provider for infrastructure-as-code provisioning, and a CLI for orchestration and automation workflows.
examples:
- key_count: 8
  name: Imperva Account Example
  slug: imperva-account-example
- key_count: 3
  name: Imperva Api Result Example
  slug: imperva-api-result-example
- key_count: 8
  name: Imperva Site Add Example
  slug: imperva-site-add-example
finops:
- name: Imperva Finops
  service_category: Security
  slug: imperva-finops
graphqls:
- description: Imperva Cloud Application Security GraphQL Schema
  name: Imperva GraphQL
  slug: imperva-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imperva.png
json_schemas:
- name: account
  property_count: 13
  slug: imperva-account
- name: accounts
  property_count: 13
  slug: imperva-accounts
- name: ApiResult
  property_count: 3
  slug: imperva-apiresult
- name: ApiResultAccountStatus
  property_count: 4
  slug: imperva-apiresultaccountstatus
- name: ApiResultListUsers
  property_count: 4
  slug: imperva-apiresultlistusers
jsonld:
- class_count: 15
  name: Imperva Context
  property_count: 25
  slug: imperva-context
layout: provider
modified: '2026-06-12'
name: Imperva
nav: Providers
network: true
overview: 'Imperva publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Account Management API, Administration API, Auth API, and 10 more. Tagged areas include Security, Cybersecurity, WAF, DDoS Protection, and API Security.


  The Imperva catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Imperva''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Imperva Plans Pricing
  plan_count: 7
  slug: imperva-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Imperva Rate Limits
  slug: imperva-rate-limits
rules:
- name: Imperva API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: imperva-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.7
  delta: -3.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.1
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imperva/refs/heads/main/screenshots/imperva-2026-06-20T183300.png
security:
- kind: authentication
  name: Imperva Authentication
  slug: imperva-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Imperva Domain Security
  slug: imperva-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: imperva
tags:
- Security
- Cybersecurity
- WAF
- DDoS Protection
- API Security
- Bot Management
- Data Security
- Cloud Security
website: https://www.imperva.com
---
