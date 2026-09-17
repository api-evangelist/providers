---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 63
  human_in_the_loop: 50
  name: Configure8 Agentic Access
  operation_count: 89
  slug: configure8-agentic-access
  summary_line: 89 operations · 63 acting · 50 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Catalog Entities API from Configure8 — 7 operation(s) for catalog entities.
  name: Configure8 Catalog Entities API
  slug: configure8-catalog-entities-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Catalog Relations API from Configure8 — 2 operation(s) for catalog relations.
  name: Configure8 Catalog Relations API
  slug: configure8-catalog-relations-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Deployments API from Configure8 — 1 operation(s) for deployments.
  name: Configure8 Deployments API
  slug: configure8-deployments-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Scorecards API from Configure8 — 2 operation(s) for scorecards.
  name: Configure8 Scorecards API
  slug: configure8-scorecards-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Users API from Configure8 — 2 operation(s) for users.
  name: Configure8 Users API
  slug: configure8-users-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Catalog Entity API from Configure8 — 22 operation(s) for catalog entity.
  name: Configure8 Catalog Entity API
  slug: configure8-catalog-entity-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Catalog Entity Batch API from Configure8 — 2 operation(s) for catalog entity batch.
  name: Configure8 Catalog Entity Batch API
  slug: configure8-catalog-entity-batch-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Catalog Entity Metadata API from Configure8 — 1 operation(s) for catalog entity metadata.
  name: Configure8 Catalog Entity Metadata API
  slug: configure8-catalog-entity-metadata-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Catalog Relation API from Configure8 — 1 operation(s) for catalog relation.
  name: Configure8 Catalog Relation API
  slug: configure8-catalog-relation-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Credential API from Configure8 — 2 operation(s) for credential.
  name: Configure8 Credential API
  slug: configure8-credential-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Deployment API from Configure8 — 2 operation(s) for deployment.
  name: Configure8 Deployment API
  slug: configure8-deployment-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Module Settings API from Configure8 — 2 operation(s) for module settings.
  name: Configure8 Module Settings API
  slug: configure8-module-settings-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Private SCIM API from Configure8 — 1 operation(s) for private scim.
  name: Configure8 Private SCIM API
  slug: configure8-private-scim-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The SCIM API from Configure8 — 8 operation(s) for scim.
  name: Configure8 SCIM API
  slug: configure8-scim-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Scorecard API from Configure8 — 5 operation(s) for scorecard.
  name: Configure8 Scorecard API
  slug: configure8-scorecard-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Sync API from Configure8 — 2 operation(s) for sync.
  name: Configure8 Sync API
  slug: configure8-sync-api
- baseURL: https://app.configure8.io/public/v1
  baseurl_source: declared
  description: The Templates API from Configure8 — 1 operation(s) for templates.
  name: Configure8 Templates API
  slug: configure8-templates-api
artifact_total: 34
asyncapis:
- description: ''
  name: Configure8 Self Service Actions Webhooks
  slug: configure8-self-service-actions-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Configure8 Public REST Catalog Entities API
  slug: open-configure8-catalog-entities-api
- collection_type: open
  name: Configure8 Public REST Catalog Entities Catalog Relations API
  slug: open-configure8-catalog-relations-api
- collection_type: open
  name: Configure8 Public REST Catalog Entities Deployments API
  slug: open-configure8-deployments-api
- collection_type: open
  name: Configure8 Public REST Catalog Entities Scorecards API
  slug: open-configure8-scorecards-api
- collection_type: open
  name: Configure8 Public REST Catalog Entities Users API
  slug: open-configure8-users-api
- collection_type: open
  name: Configure8 Public REST API
  slug: open-configure8
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/overlays/configure8-c8-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/configure8-c8-public-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/agentic-access/configure8-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/configure8-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/security/configure8-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/configure8-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/security/configure8-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/configure8-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/security/configure8-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/configure8-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/security/configure8-trust-center.yml
  title: ''
  type: Compliance
  url: security/configure8-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/security/configure8-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/configure8-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/authentication/configure8-authentication.yml
  title: ''
  type: Authentication
  url: authentication/configure8-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/conventions/configure8-conventions.yml
  title: ''
  type: Conventions
  url: conventions/configure8-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/conformance/configure8-conformance.yml
  title: ''
  type: Conformance
  url: conformance/configure8-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/errors/configure8-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/configure8-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/lifecycle/configure8-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/configure8-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/data-model/configure8-data-model.yml
  title: ''
  type: DataModel
  url: data-model/configure8-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/plans/configure8-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/configure8-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/rate-limits/configure8-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/configure8-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/well-known/configure8-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/configure8-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/llms/configure8-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/configure8-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/mcp/configure8-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/configure8-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/asyncapi/configure8-self-service-actions-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/configure8-self-service-actions-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/changelog/configure8-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/configure8-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://configure8.io/docs-sub/configure8-product-docs/extras/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Configure8inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/configure8
- group: company
  title: ''
  type: Website
  url: https://www.configure8.io/
- group: docs
  title: ''
  type: Documentation
  url: https://configure8.io/docs-sub/configure8-product-docs
- group: docs
  title: ''
  type: APIReference
  url: https://configure8.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://configure8.io/docs-sub/configure8-product-docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.configure8.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.configure8.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://configure8.io/try-now
- group: operate
  title: ''
  type: Support
  url: https://configure8.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://configure8.io/tos.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://configure8.io/privacy/policy
- group: other
  title: ''
  type: Platform Engineering
  url: https://platformengineering.org/tools/configur8
created: '2026-03-16'
description: Configure8 is a commercial Internal Developer Portal (IDP) that gives engineering organizations a unified catalog of services, environments, and resources, with dependency mapping across cloud and on-premises infrastructure. It pairs that catalog with scorecards for software health and golden-path compliance, no-code self-service actions for developers, and FinOps-style cloud cost visibility. Configure8 supports SaaS and self-hosted deployments and ships with enterprise features such as RBAC, SCIM, SSO, audit logging, and a public REST API.
finops:
- name: Configure8 Finops
  service_category: API
  slug: configure8-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/configure8.png
layout: provider
mcp_servers:
- description: 'configure8''s ReadMe-hosted API reference exposes a Model Context Protocol endpoint at https://configure8.readme.io/mcp. A POST of {"jsonrpc":"2.0","id":1,"method":"tools/list"} with Accept: applicatio'
  name: configure8 documentation MCP server
  slug: configure8-documentation-mcp-server
modified: '2026-09-05'
name: Configure8
nav: Providers
network: true
overview: 'Configure8 publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Catalog Entities API, Catalog Relations API, Deployments API, and 14 more. Tagged areas include Catalog, Cloud Cost, Developer Experience, DevOps, and Internal Developer Portal.


  The Configure8 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Configure8''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 28 more developer resources.'
plans:
- name: Configure8 Plans Pricing
  plan_count: 2
  slug: configure8-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Configure8 Rate Limits
  slug: configure8-rate-limits
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 44.9
    developer_ergonomics: 49.4
    discoverability: 75.9
    operational_transparency: 36.8
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 29.4
      derived: 5
      marker_coverage: 29.4
      total: 17
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/configure8/refs/heads/main/screenshots/configure8-2026-06-20T174854.png
security:
- kind: authentication
  name: Configure8 Authentication
  slug: configure8-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Configure8 Domain Security
  slug: configure8-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Configure8 Vulnerability Disclosure
  slug: configure8-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Configure8 Trust Center
  slug: configure8-trust-center
  summary_line: SOC 2
slug: configure8
tags:
- Catalog
- Cloud Cost
- Developer Experience
- DevOps
- Internal Developer Portal
- Platform Engineering
- Scorecards
- Self-Service
- Service Catalog
- SRE
website: https://www.configure8.io/
---
