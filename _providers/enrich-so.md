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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Enrich So Agentic Access
  operation_count: 53
  slug: enrich-so-agentic-access
  summary_line: 53 operations · 23 acting
api_count: 10
apis:
- description: Credit balance and transaction history for the organization behind the API key.
  name: Enrich Account API
  slug: enrich-so-account-api
- description: IP-to-company resolution (single and batch) and LinkedIn company-follower scraping with audience count estimation. The company-follower endpoints are restricted to approved accounts.
  name: Enrich Company Intelligence API
  slug: enrich-so-company-intelligence-api
- description: Find a professional email from a first name, last name and company domain, single or in batches of up to 500,000 leads.
  name: Enrich Email Finder API
  slug: enrich-so-email-finder-api
- description: Validate email addresses for deliverability, single or in batches of up to 500,000 emails.
  name: Enrich Email Verification API
  slug: enrich-so-email-verification-api
- description: Search, count, reveal, enrich, unlock and export leads across people and organizations, with saved searches and asynchronous reveal and export jobs.
  name: Enrich Lead Finder API
  slug: enrich-so-lead-finder-api
- description: Reverse email lookup returning a person's professional profile, single or in bulk.
  name: Enrich Person Enrichment API
  slug: enrich-so-person-enrichment-api
- description: Find phone and mobile numbers for a person from an email address or profile URL, single or in bulk.
  name: Enrich Phone Finder API
  slug: enrich-so-phone-finder-api
- description: List team members and manage pending team invitations for the organization behind the API key.
  name: Enrich Teams API
  slug: enrich-so-teams-api
- description: Find employees at a company and run cascading ICP (ideal customer profile) people searches.
  name: Enrich People Search API
  slug: enrich-so-people-search-api
- description: 'The prior major version of the Enrich API, still live at api.enrich.so and still serving its own Swagger UI at https://api.enrich.so/docs. Two operations: GET /v1/api/auth returns the account/credit c'
  name: Enrich Labs Legacy API (v1/v2)
  slug: enrich-so-legacy-api
artifact_total: 30
asyncapis:
- description: ''
  name: Enrich So Webhooks
  slug: enrich-so-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Enrich Account API
  slug: open-enrich-so-account-api
- collection_type: open
  name: Enrich Company Intelligence API
  slug: open-enrich-so-company-intelligence-api
- collection_type: open
  name: Enrich Email Finder API
  slug: open-enrich-so-email-finder-api
- collection_type: open
  name: Enrich Email Verification API
  slug: open-enrich-so-email-verification-api
- collection_type: open
  name: Enrich Lead Finder API
  slug: open-enrich-so-lead-finder-api
- collection_type: open
  name: Enrich People Search API
  slug: open-enrich-so-people-search-api
- collection_type: open
  name: Enrich Person Enrichment API
  slug: open-enrich-so-person-enrichment-api
- collection_type: open
  name: Enrich Phone Finder API
  slug: open-enrich-so-phone-finder-api
- collection_type: open
  name: Enrich Teams API
  slug: open-enrich-so-teams-api
- collection_type: open
  name: Enrich API
  slug: open-enrich-so
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enrich-so-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/enrich-so-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/enrich-so-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/enrich-so
- group: company
  title: ''
  type: Website
  url: https://www.enrich.so
- group: docs
  title: ''
  type: Documentation
  url: https://doc.enrich.so/introduction-1951028m0
- group: commercial
  title: ''
  type: Plans
  url: plans/enrich-so-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enrich-so-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/enrich-so-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.enrich.so/blog
- group: build
  title: ''
  type: Packages
  url: packages/enrich-so-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/enrich-so-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/enrich-so-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/enrich-so-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/enrich-so-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enrich-so-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/enrich-so-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/enrich-so-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/enrich-so-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.enrich.so
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/enrich-so-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/enrich-so-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/enrich-so-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/enrich-so-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/enrich-so-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://doc.enrich.so/api-reference-1951025m0
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.enrich.so/introduction-1951028m0
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.enrich.so/quickstart-1951029m0
- group: commercial
  title: ''
  type: Pricing
  url: https://doc.enrich.so/credits-pricing-1951027m0
- group: start
  title: ''
  type: SignUp
  url: https://dash.enrich.so
- group: start
  title: ''
  type: Login
  url: https://dash.enrich.so/dashboard/api-keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enrich.so/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enrich.so/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maximiseai
- group: build
  title: ''
  type: PostmanCollection
  url: collections/enrich-so.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/enrich-so.opencollection.json
created: '2026-07-11'
description: Enrich (enrich.so), operated by Enrich Labs, is a person and company data enrichment API for B2B go-to-market, sales, and web intelligence teams. From a single REST interface at https://dev.enrich.so/api/v3 it resolves a professional profile from an email address (reverse email lookup), finds and verifies professional email addresses, finds mobile and phone numbers, resolves a company and geolocation from an IP address, searches a lead-finder database of people and organizations, finds employees at a company, and scrapes LinkedIn company followers. Fifty-one operations across nine products, every one of them metered against a single prepaid credit balance and refunded when a lookup finds nothing. Every bulk product follows one submit/poll/results shape with reserve-and-settle billing, ten typed webhook callbacks, RFC 9457 problem details on every error, and official TypeScript and Go SDKs. Enrich also operates a first-party remote MCP server at mcp.enrich.so with OAuth 2.0 and
  dynamic client registration.
finops:
- name: Enrich So Finops
  service_category: Data Enrichment and Intelligence
  slug: enrich-so-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enrich-so.png
layout: provider
mcp_servers:
- description: ''
  name: enrich-so-mcp.yml
  slug: enrich-so-mcpyml
modified: '2026-08-14'
name: Enrich
nav: Providers
network: true
overview: 'Enrich publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account API, Company Intelligence API, Email Finder API, and 7 more. Tagged areas include Data Enrichment, Contact Discovery, Web Intelligence, B2B Data, and Lead Enrichment.


  The Enrich catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Enrich''s developer surface includes authentication, documentation, engineering blog, changelog, API reference, getting-started guide, pricing, and 30 more developer resources.'
plans:
- name: Enrich So Plans Pricing
  plan_count: 5
  slug: enrich-so-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 18
  name: Enrich So Rate Limits
  slug: enrich-so-rate-limits
scopes:
- name: Enrich So Scopes
  scope_count: 0
  slug: enrich-so-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.4
  delta: -3.6
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 30.3
    contract_quality: 72.2
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 73.7
  previous_composite: 71.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enrich-so/refs/heads/main/screenshots/enrich-so-2026-07-25T213424.png
security:
- kind: authentication
  name: Enrich So Authentication
  slug: enrich-so-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Enrich So Domain Security
  slug: enrich-so-domain-security
  summary_line: TLSv1.3 · DMARC
slug: enrich-so
tags:
- Data Enrichment
- Contact Discovery
- Web Intelligence
- B2B Data
- Lead Enrichment
- Email Finder
- Email Verification
- Phone Numbers
- People Search
- IP Intelligence
- LinkedIn
- Reference Data
- MCP
website: https://www.enrich.so
---
