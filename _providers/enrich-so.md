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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Enrich So Agentic Access
  operation_count: 64
  slug: enrich-so-agentic-access
  summary_line: 64 operations · 21 acting
api_count: 7
apis:
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: Find a professional email from a first name, last name and company domain, single or in batches of up to 500,000 leads.
  name: Enrich Email Finder API
  slug: enrich-so-email-finder-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: Search, count, reveal, enrich, unlock and export leads across people and organizations, with saved searches and asynchronous reveal and export jobs.
  name: Enrich Lead Finder API
  slug: enrich-so-lead-finder-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: Find phone and mobile numbers for a person from an email address or profile URL, single or in bulk.
  name: Enrich Phone Finder API
  slug: enrich-so-phone-finder-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: List team members and manage pending team invitations for the organization behind the API key.
  name: Enrich Teams API
  slug: enrich-so-teams-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: Find employees at a company and run cascading ICP (ideal customer profile) people searches.
  name: Enrich People Search API
  slug: enrich-so-people-search-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: The Authentication API from Enrich — 1 operation(s) for authentication.
  name: Enrich Authentication API
  slug: enrich-so-authentication-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: The Company Followers API from Enrich — 7 operation(s) for company followers.
  name: Enrich Company Followers API
  slug: enrich-so-company-followers-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: The Company Followers/Count Estimation API from Enrich — 2 operation(s) for company followers/count estimation.
  name: Enrich Company Followers/Count Estimation API
  slug: enrich-so-company-followers-count-estimation-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: The Email Validation API from Enrich — 4 operation(s) for email validation.
  name: Enrich Email Validation API
  slug: enrich-so-email-validation-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: The Enrich API from Enrich — 1 operation(s) for enrich.
  name: Enrich API
  slug: enrich-so-enrich-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: The IP to Company API from Enrich — 4 operation(s) for ip to company.
  name: Enrich IP to Company API
  slug: enrich-so-ip-to-company-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: The Reverse Email Lookup API from Enrich — 4 operation(s) for reverse email lookup.
  name: Enrich Reverse Email Lookup API
  slug: enrich-so-reverse-email-lookup-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: The Wallets API from Enrich — 2 operation(s) for wallets.
  name: Enrich Wallets API
  slug: enrich-so-wallets-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: Credit balance and transaction history.
  name: Enrich Account API
  slug: enrich-so-account-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: IP-to-company resolution and LinkedIn company-follower scraping.
  name: Enrich Company Intelligence API
  slug: enrich-so-company-intelligence-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: Validate email addresses for deliverability.
  name: Enrich Email Verification API
  slug: enrich-so-email-verification-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: Reverse email lookup returning a person's professional profile.
  name: Enrich Person Enrichment API
  slug: enrich-so-person-enrichment-api
- baseURL: https://dev.enrich.so/api/v3
  baseurl_source: declared
  description: The Webhooks API from Enrich — 0 operation(s) for webhooks.
  name: Enrich Webhooks API
  slug: enrich-so-webhooks-api
artifact_total: 42
asyncapis:
- description: ''
  name: Enrich So Webhooks
  slug: enrich-so-webhooks
collections:
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
- group: other
  href: https://artifacts.apis.io/enrich-so/capabilities/enrich-so-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/enrich-so-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/enrich-so/overlays/enrich-so-account-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/enrich-so-account-overlay.yaml
- group: other
  href: https://artifacts.apis.io/enrich-so/overlays/enrich-so-company-intelligence-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/enrich-so-company-intelligence-overlay.yaml
- group: other
  href: https://artifacts.apis.io/enrich-so/overlays/enrich-so-email-verification-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/enrich-so-email-verification-overlay.yaml
- group: other
  href: https://artifacts.apis.io/enrich-so/overlays/enrich-so-person-enrichment-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/enrich-so-person-enrichment-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/enrich-so/security/enrich-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enrich-so-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/enrich-so/agentic-access/enrich-so-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/enrich-so-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/enrich-so/authentication/enrich-so-authentication.yml
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
  href: https://artifacts.apis.io/enrich-so/plans/enrich-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/enrich-so-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/enrich-so/rate-limits/enrich-so-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/enrich-so-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/enrich-so/finops/enrich-so-finops.yml
  title: ''
  type: FinOps
  url: finops/enrich-so-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.enrich.so/blog
- group: build
  href: https://artifacts.apis.io/enrich-so/packages/enrich-so-packages.yml
  title: ''
  type: Packages
  url: packages/enrich-so-packages.yml
- group: build
  href: https://artifacts.apis.io/enrich-so/packages/enrich-so-packages.yml
  title: ''
  type: SDKs
  url: packages/enrich-so-packages.yml
- group: agent
  href: https://artifacts.apis.io/enrich-so/well-known/enrich-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/enrich-so-well-known.yml
- group: agent
  href: https://artifacts.apis.io/enrich-so/mcp/enrich-so-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/enrich-so-mcp.yml
- group: build
  href: https://artifacts.apis.io/enrich-so/mcp/enrich-so-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/enrich-so-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/enrich-so/llms/enrich-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/enrich-so-llms.txt
- group: design
  href: https://artifacts.apis.io/enrich-so/conformance/enrich-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/enrich-so-conformance.yml
- group: design
  href: https://artifacts.apis.io/enrich-so/errors/enrich-so-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/enrich-so-problem-types.yml
- group: design
  href: https://artifacts.apis.io/enrich-so/lifecycle/enrich-so-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/enrich-so-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.enrich.so
- group: auth
  href: https://artifacts.apis.io/enrich-so/scopes/enrich-so-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/enrich-so-scopes.yml
- group: design
  href: https://artifacts.apis.io/enrich-so/conventions/enrich-so-conventions.yml
  title: ''
  type: Conventions
  url: conventions/enrich-so-conventions.yml
- group: operate
  href: https://artifacts.apis.io/enrich-so/changelog/enrich-so-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/enrich-so-changelog.yml
- group: design
  href: https://artifacts.apis.io/enrich-so/data-model/enrich-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/enrich-so-data-model.yml
- group: design
  href: https://artifacts.apis.io/enrich-so/asyncapi/enrich-so-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/enrich-so-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/enrich-so/skills/_index.yml
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
  href: https://artifacts.apis.io/enrich-so/collections/enrich-so.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/enrich-so.postman_collection.json
- group: build
  href: https://artifacts.apis.io/enrich-so/collections/enrich-so.opencollection.json
  title: ''
  type: OpenCollection
  url: collections/enrich-so.opencollection.json
created: '2026-07-11'
description: Enrich (enrich.so), operated by Enrich Labs, is a person and company data enrichment API for B2B go-to-market, sales, and web intelligence teams. From a single REST interface at https://dev.enrich.so/api/v3 it resolves a professional profile from an email address (reverse email lookup), finds and verifies professional email addresses, finds mobile and phone numbers, resolves a company and geolocation from an IP address, searches a lead-finder database of people and organizations, finds employees at a company, and scrapes LinkedIn company followers. Fifty-one operations across nine products, every one of them metered against a single prepaid credit balance and refunded when a lookup finds nothing. Every bulk product follows one submit/poll/results shape with reserve-and-settle billing, ten typed webhook callbacks, RFC 9457 problem details on every error, and official TypeScript and Go SDKs. Enrich also operates a first-party remote MCP server at mcp.enrich.so with OAuth 2.0 and
  dynamic client registration.
finops:
- has_sources: true
  method: searched
  name: Enrich So Finops
  primary_unit: ''
  service_category: Data Enrichment and Intelligence
  slug: enrich-so-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enrich-so.png
layout: provider
mcp_servers:
- description: 'Enrich operates a first-party REMOTE MCP server at https://mcp.enrich.so/mcp. It is a Streamable-HTTP MCP endpoint (Express, CORS-open, mcp-session-id exposed) that an MCP client can POST to directly '
  name: Enrich MCP Server
  slug: enrich-so-mcp-yml
modified: '2026-09-16'
name: Enrich
nav: Providers
network: true
overview: 'Enrich publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Email Finder API, Lead Finder API, Phone Finder API, and 15 more. Tagged areas include Data Enrichment, Contact Discovery, Web Intelligence, B2B Data, and Lead Enrichment.


  The Enrich catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Enrich''s developer surface includes authentication, documentation, engineering blog, changelog, API reference, getting-started guide, pricing, and 35 more developer resources.'
plans:
- name: Enrich So Plans Pricing
  plan_count: 3
  slug: enrich-so-plans-pricing
- name: Enrich So Price Estimates
  plan_count: 0
  slug: enrich-so-price-estimates
random_paper: 16
rate_limits:
- limit_count: 18
  name: Enrich So Rate Limits
  slug: enrich-so-rate-limits
scopes:
- name: Enrich So Scopes
  scope_count: 1
  slug: enrich-so-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 50.0
    developer_ergonomics: 62.5
    discoverability: 70.0
    operational_transparency: 76.3
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
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
screenshot: https://apis.io/screenshots/enrich-so/enrich-so-2026-07-25T213424.png
security:
- kind: authentication
  name: Enrich So Authentication
  slug: enrich-so-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Enrich So Domain Security
  slug: enrich-so-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: build-a-lead-list-without-overspending
  slug: build-a-lead-list-without-overspending
- name: enrich-a-person-from-an-email
  slug: enrich-a-person-from-an-email
- name: find-and-verify-a-work-email
  slug: find-and-verify-a-work-email
- name: run-a-bulk-enrichment-job
  slug: run-a-bulk-enrichment-job
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
