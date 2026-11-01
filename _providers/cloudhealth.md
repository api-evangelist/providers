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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.2
  scored_at: '2026-10-31'
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
artifact_total: 28
collections:
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
- group: commercial
  href: https://artifacts.apis.io/cloudhealth/finops/cloudhealth-finops.yml
  title: ''
  type: FinOps
  url: finops/cloudhealth-finops.yml
- group: other
  href: https://artifacts.apis.io/cloudhealth/capabilities/cloudhealth-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cloudhealth-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/vmware/
- group: agent
  href: https://artifacts.apis.io/cloudhealth/agentic-access/cloudhealth-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudhealth-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cloudhealth/security/cloudhealth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudhealth-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cloudhealth/authentication/cloudhealth-authentication.yml
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
  href: https://artifacts.apis.io/cloudhealth/json-ld/cloudhealth-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudhealth-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudhealth/rules/cloudhealth-rules.yml
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
  href: https://artifacts.apis.io/cloudhealth/well-known/cloudhealth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudhealth-well-known.yml
- group: agent
  href: https://artifacts.apis.io/cloudhealth/mcp/cloudhealth-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cloudhealth-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cloudhealth/scopes/cloudhealth-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cloudhealth-scopes.yml
- group: design
  href: https://artifacts.apis.io/cloudhealth/conventions/cloudhealth-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloudhealth-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloudhealth/errors/cloudhealth-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudhealth-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cloudhealth/lifecycle/cloudhealth-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloudhealth-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cloudhealth/rate-limits/cloudhealth-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloudhealth-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cloudhealth/plans/cloudhealth-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudhealth-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/cloudhealth/packages/cloudhealth-packages.yml
  title: ''
  type: Packages
  url: packages/cloudhealth-packages.yml
- group: design
  href: https://artifacts.apis.io/cloudhealth/conformance/cloudhealth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudhealth-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cloudhealth/llms/cloudhealth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudhealth-llms.txt
- group: agent
  href: https://artifacts.apis.io/cloudhealth/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-03-16'
description: CloudHealth (now VMware Tanzu CloudHealth, owned by Broadcom) is a multi-cloud financial and operational management platform. It provides cost visibility, optimization recommendations, asset inventory, custom perspectives (groupings), policies, governance, and partner/MSP billing workflows across AWS, Azure, GCP, Oracle, and data center environments. The platform exposes both a REST API and a GraphQL API for programmatic access to reports, assets, accounts, perspectives, tags, metrics, and partner customer provisioning.
finops:
- has_sources: true
  method: derived
  name: Cloudhealth Finops
  primary_unit: contract
  service_category: ''
  slug: cloudhealth-finops
  template: false
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
- description: Remote MCP server at apps.cloudhealthtech.com over HTTP requiring OAuth.
  name: CloudHealth MCP Server
  slug: cloudhealth
modified: '2026-09-16'
name: CloudHealth
nav: Providers
network: true
overview: 'CloudHealth is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including AWS Accounts API, Perspectives API, Reports API, and 5 more. Tagged areas include Cloud Cost, Cloud Governance, Cloud Management, Cost Optimization, and FinOps.


  The CloudHealth catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CloudHealth''s developer surface includes authentication, documentation, engineering blog, API reference, support, pricing, and 28 more developer resources.'
plans:
- name: Cloudhealth Plans Pricing
  plan_count: 3
  slug: cloudhealth-plans-pricing
- name: Cloudhealth Price Estimates
  plan_count: 0
  slug: cloudhealth-price-estimates
random_paper: 13
rate_limits:
- limit_count: 4
  name: Cloudhealth Rate Limits
  slug: cloudhealth-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 51
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
  composite: 56.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 75.8
    catalog_earned_first_party: 24.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 84.2
    contract_governance: 29.5
    contract_quality: 54.8
    developer_ergonomics: 37.5
    discoverability: 70.0
    operational_transparency: 36.8
  previous_composite: 54.7
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cloudhealth/cloudhealth-2026-06-20T174608.png
security:
- kind: authentication
  name: Cloudhealth Authentication
  slug: cloudhealth-authentication
  summary_line: http/apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Cloudhealth Domain Security
  slug: cloudhealth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: cloudhealth-cost-history-report
  slug: cloudhealth-cost-history-report
- name: cloudhealth-enable-aws-account
  slug: cloudhealth-enable-aws-account
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
