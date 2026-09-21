---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Cloudhealth Agentic Access
  operation_count: 10
  slug: cloudhealth-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 8
apis:
- description: GraphQL API at a single endpoint (https://apps.cloudhealthtech.com/graphql) covering budgets, FlexReports, FlexOrgs, saved reports, savings plan and commitment recommendations, cost reallocation and G
  name: CloudHealth GraphQL API
  slug: cloudhealth-graphql-api
- description: Partner-specific REST endpoints for MSPs to provision customers, assign AWS/Azure accounts, manage custom price books, billing rules, and customer statements at scale.
  name: CloudHealth Partner API
  slug: cloudhealth-partner-api
- baseURL: https://chapi.cloudhealthtech.com
  baseurl_source: declared
  description: AWS account configuration management.
  name: CloudHealth AWS Accounts API
  slug: cloudhealth-aws-accounts-api
- baseURL: https://chapi.cloudhealthtech.com
  baseurl_source: declared
  description: Perspective (grouping) management.
  name: CloudHealth Perspectives API
  slug: cloudhealth-perspectives-api
- baseURL: https://chapi.cloudhealthtech.com
  baseurl_source: declared
  description: OLAP cost and usage reports.
  name: CloudHealth Reports API
  slug: cloudhealth-reports-api
- baseURL: https://chapi.cloudhealthtech.com
  baseurl_source: declared
  description: Asset search.
  name: CloudHealth Search API
  slug: cloudhealth-search-api
- baseURL: https://chapi.cloudhealthtech.com
  baseurl_source: declared
  description: Single sign-on configuration.
  name: CloudHealth SSO API
  slug: cloudhealth-sso-api
- description: The CloudHealth Platform REST API programmatically retrieves and manages data from the CloudHealth Platform — AWS/Azure/GCP accounts, assets, perspectives, billing rules, metrics, OLAP reports, polici
  name: CloudHealth Platform API
  slug: cloudhealth-platform-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CloudHealth REST AWS Accounts API
  slug: open-cloudhealth-aws-accounts-api
- collection_type: open
  name: CloudHealth REST AWS Accounts Perspectives API
  slug: open-cloudhealth-perspectives-api
- collection_type: open
  name: CloudHealth REST AWS Accounts Reports API
  slug: open-cloudhealth-reports-api
- collection_type: open
  name: CloudHealth REST AWS Accounts Search API
  slug: open-cloudhealth-search-api
- collection_type: open
  name: CloudHealth REST AWS Accounts SSO API
  slug: open-cloudhealth-sso-api
- collection_type: open
  name: CloudHealth REST API
  slug: open-cloudhealth
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/vmware/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/agentic-access/cloudhealth-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudhealth-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/security/cloudhealth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudhealth-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/authentication/cloudhealth-authentication.yml
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
  url: https://www.broadcom.com/products/software/finops/cloudhealth
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.cloudhealthtech.com/
- group: docs
  title: ''
  type: Product Documentation
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/cloudhealth/saas/index.html
- group: auth
  title: ''
  type: Authentication
  url: https://apidocs.cloudhealthtech.com/#documentation_getting-your-api-key
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.broadcom.com/company/legal/privacy/policy
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/json-ld/cloudhealth-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudhealth-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/rules/cloudhealth-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudhealth-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://blogs.vmware.com/feed/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.cloudhealthtech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.cloudhealthtech.com/graphql-api/
- group: start
  title: ''
  type: Login
  url: https://apps.cloudhealthtech.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.broadcom.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.broadcom.com/company/legal/terms-of-use
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/marketplace/pp/prodview-btyciyjmdewhm
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/well-known/cloudhealth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudhealth-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/mcp/cloudhealth-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cloudhealth-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/scopes/cloudhealth-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cloudhealth-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/conventions/cloudhealth-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloudhealth-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/errors/cloudhealth-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudhealth-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/lifecycle/cloudhealth-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloudhealth-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/rate-limits/cloudhealth-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloudhealth-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/plans/cloudhealth-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudhealth-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/packages/cloudhealth-packages.yml
  title: ''
  type: Packages
  url: packages/cloudhealth-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/conformance/cloudhealth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudhealth-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/llms/cloudhealth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudhealth-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
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
mcp_servers:
- description: ''
  name: CloudHealth MCP Server
  slug: cloudhealth-mcp-server
modified: '2026-09-16'
name: CloudHealth
nav: Providers
network: true
overview: 'CloudHealth publishes 5 APIs on the [APIs.io](https://apis.io/) network, including AWS Accounts API, Perspectives API, Reports API, and 2 more. Tagged areas include Cloud Cost, Cloud Governance, Cloud Management, Cost Optimization, and FinOps.


  The CloudHealth catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CloudHealth''s developer surface includes authentication, documentation, engineering blog, API reference, support, pricing, and 26 more developer resources.'
plans:
- name: Cloudhealth Plans Pricing
  plan_count: 3
  slug: cloudhealth-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Cloudhealth Rate Limits
  slug: cloudhealth-rate-limits
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: CloudHealth API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: cloudhealth-rules
scopes:
- name: Cloudhealth Scopes
  scope_count: 4
  slug: cloudhealth-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 87.0
    catalog_earned_first_party: 24.0
    catalog_gap: 28.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 63.6
    contract_quality: 62.7
    developer_ergonomics: 31.5
    discoverability: 74.1
    operational_transparency: 34.2
  previous_composite: 56.3
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
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudhealth/refs/heads/main/screenshots/cloudhealth-2026-06-20T174608.png
security:
- kind: authentication
  name: Cloudhealth Authentication
  slug: cloudhealth-authentication
  summary_line: http/apiKey/oauth2 · 4 schemes
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
website: https://www.broadcom.com/products/software/finops/cloudhealth
---
