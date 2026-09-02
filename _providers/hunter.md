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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Hunter Agentic Access
  operation_count: 25
  slug: hunter-agentic-access
  summary_line: 25 operations · 11 acting
api_count: 1
apis:
- description: Retrieve account information and usage statistics.
  name: Hunter Account API
  slug: hunter-account-api
- description: Manage email sequences and recipients.
  name: Hunter Campaigns API
  slug: hunter-campaigns-api
- description: Merge person and company enrichment for a single email address.
  name: Hunter Combined Enrichment API
  slug: hunter-combined-enrichment-api
- description: Enrich company information linked to a domain name.
  name: Hunter Company Enrichment API
  slug: hunter-company-enrichment-api
- description: Find companies matching criteria using natural language or filters.
  name: Hunter Discover API
  slug: hunter-discover-api
- description: Search for email addresses associated with a domain.
  name: Hunter Domain Search API
  slug: hunter-domain-search-api
- description: Count email addresses found for a domain.
  name: Hunter Email Count API
  slug: hunter-email-count-api
- description: Enrich personal information linked to an email or LinkedIn profile.
  name: Hunter Email Enrichment API
  slug: hunter-email-enrichment-api
- description: Find the most likely email address for a person at a company.
  name: Hunter Email Finder API
  slug: hunter-email-finder-api
- description: Verify the deliverability of an email address.
  name: Hunter Email Verifier API
  slug: hunter-email-verifier-api
- description: Manage leads stored in Hunter.
  name: Hunter Leads API
  slug: hunter-leads-api
- description: Manage leads list collections in Hunter.
  name: Hunter Leads Lists API
  slug: hunter-leads-lists-api
arazzos:
- description: Check remaining search quota before running a domain search.
  name: Hunter Account-Guarded Domain Search
  slug: hunter-account-guarded-domain-search-workflow
- description: Combine person and company enrichment for an email, then upsert it as a lead.
  name: Hunter Combined Enrich and Upsert Lead
  slug: hunter-combined-enrich-upsert-lead-workflow
- description: Create a new leads list and upsert a lead into it in one flow.
  name: Hunter Create List and Add Lead
  slug: hunter-create-list-add-lead-workflow
- description: Discover a target company, search its domain, and count its emails.
  name: Hunter Discover, Search, and Count
  slug: hunter-discover-search-count-workflow
- description: Search a domain, create a list, verify the top email, and upsert it as a lead.
  name: Hunter Domain Search to Build a Verified List
  slug: hunter-domain-search-build-list-workflow
- description: Search a domain for emails, find a named person's address, then verify it.
  name: Hunter Domain Search, Find, and Verify
  slug: hunter-domain-search-find-verify-workflow
- description: Enrich a person from an email, verify the address, and save a verified lead.
  name: Hunter Enrich, Verify, and Create Lead
  slug: hunter-enrich-verify-create-lead-workflow
- description: Find a person's email, verify it, and add it to a campaign when valid.
  name: Hunter Find, Verify, and Add Campaign Recipient
  slug: hunter-find-verify-add-recipient-workflow
- description: Find a person's email, verify it, and only save a lead when it is valid.
  name: Hunter Find, Verify, and Create Lead
  slug: hunter-find-verify-create-lead-workflow
- description: Verify an email, add it to a campaign when valid, then start the campaign.
  name: Hunter Verify and Add to Campaign
  slug: hunter-verify-add-to-campaign-workflow
artifact_total: 157
asyncapis:
- description: ''
  name: Hunter Webhooks
  slug: hunter-webhooks
collections:
- collection_type: postman
  name: Hunter API
  slug: postman-hunter-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hunter Account API
  slug: open-hunter-account-api
- collection_type: open
  name: Hunter API
  slug: open-hunter-api
- collection_type: open
  name: Hunter Account Campaigns API
  slug: open-hunter-campaigns-api
- collection_type: open
  name: Hunter Account Combined Enrichment API
  slug: open-hunter-combined-enrichment-api
- collection_type: open
  name: Hunter Account Company Enrichment API
  slug: open-hunter-company-enrichment-api
- collection_type: open
  name: Hunter Account Discover API
  slug: open-hunter-discover-api
- collection_type: open
  name: Hunter Account Domain Search API
  slug: open-hunter-domain-search-api
- collection_type: open
  name: Hunter Account Email Count API
  slug: open-hunter-email-count-api
- collection_type: open
  name: Hunter Account Email Enrichment API
  slug: open-hunter-email-enrichment-api
- collection_type: open
  name: Hunter Account Email Finder API
  slug: open-hunter-email-finder-api
- collection_type: open
  name: Hunter Account Email Verifier API
  slug: open-hunter-email-verifier-api
- collection_type: open
  name: Hunter Account Leads API
  slug: open-hunter-leads-api
- collection_type: open
  name: Hunter Account Leads Lists API
  slug: open-hunter-leads-lists-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hunter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hunter-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hunter-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hunter/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-account-guarded-domain-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-combined-enrich-upsert-lead-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-create-list-add-lead-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-discover-search-count-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-domain-search-build-list-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-domain-search-find-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-enrich-verify-create-lead-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-find-verify-add-recipient-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-find-verify-create-lead-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-verify-add-to-campaign-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hunterny
- group: start
  title: ''
  type: Portal
  url: https://hunter.io/api
- group: docs
  title: ''
  type: Documentation
  url: https://hunter.io/api-documentation/v2
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/hunter-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hunter-full-overlay.yaml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hunter-lead-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hunter-context.jsonld
- group: auth
  title: ''
  type: Authentication
  url: https://hunter.io/api-documentation/v2#authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://hunter.io/api-documentation/v2#rate-limiting
- group: commercial
  title: ''
  type: Pricing
  url: https://hunter.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hunter.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hunter.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hunter.io
- group: company
  title: ''
  type: Blog
  url: https://hunter.io/blog
- group: start
  title: ''
  type: Login
  url: https://hunter.io/users/sign_in
- group: start
  title: ''
  type: Signup
  url: https://hunter.io/users/sign_up
- group: operate
  title: ''
  type: ChangeLog
  url: https://hunter.io/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hunter-io
- group: operate
  title: ''
  type: Contact
  url: https://hunter.io/contact
- group: operate
  title: ''
  type: Support
  url: https://help.hunter.io
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hunter-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.hunter.io/mcp
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hunter-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hunter-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hunter-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/hunter-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hunter-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/hunter-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hunter-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hunter-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hunter-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hunter-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hunter-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://help.hunter.io/en/articles/1890029-gdpr-compliance
- group: design
  title: ''
  type: DataModel
  url: data-model/hunter-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hunter-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hunter-changelog.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hunter-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hunter.io/security-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/hunter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hunter-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hunter-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hunter-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/hunter-spectral-rules.yml
- group: build
  title: ''
  type: Postman
  url: postman/hunter-api.postman_collection.json
- group: docs
  title: ''
  type: APIReference
  url: https://hunter.io/api-documentation/v2
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hunter.io/api
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://hunter.io/data-processing-agreement
created: '2024-01-01'
description: Hunter is an email finding, verification and B2B prospecting platform. Its v2 API finds the professional email addresses associated with a company domain, predicts an address for a named person, verifies deliverability, enriches people and companies, discovers target accounts by natural-language query or structured filter, and manages the leads, lead lists and outreach sequences built from those results. Hunter also operates a first-party remote MCP server at https://mcp.hunter.io/mcp exposing roughly 100 tools, and publishes its own packaged Agent Skills, making it one of the few providers whose agent surface is wider than its documented REST contract.
examples:
- key_count: 9
  name: Hunter Account Result Example
  slug: hunter-account-result-example
- key_count: 9
  name: Hunter Campaign Example
  slug: hunter-campaign-example
- key_count: 3
  name: Hunter Campaign Recipient Example
  slug: hunter-campaign-recipient-example
- key_count: 30
  name: Hunter Company Enrichment Example
  slug: hunter-company-enrichment-example
- key_count: 12
  name: Hunter Company Geo Location Example
  slug: hunter-company-geo-location-example
- key_count: 12
  name: Hunter Discover Request Example
  slug: hunter-discover-request-example
- key_count: 3
  name: Hunter Discover Result Example
  slug: hunter-discover-result-example
- key_count: 12
  name: Hunter Domain Email Example
  slug: hunter-domain-email-example
- key_count: 7
  name: Hunter Domain Search Result Example
  slug: hunter-domain-search-result-example
- key_count: 5
  name: Hunter Email Count Result Example
  slug: hunter-email-count-result-example
- key_count: 11
  name: Hunter Email Finder Result Example
  slug: hunter-email-finder-result-example
- key_count: 14
  name: Hunter Email Verifier Result Example
  slug: hunter-email-verifier-result-example
- key_count: 1
  name: Hunter Error Example
  slug: hunter-error-example
- key_count: 7
  name: Hunter Geo Location Example
  slug: hunter-geo-location-example
- key_count: 21
  name: Hunter Lead Example
  slug: hunter-lead-example
- key_count: 15
  name: Hunter Lead Input Example
  slug: hunter-lead-input-example
- key_count: 4
  name: Hunter Leads List Example
  slug: hunter-leads-list-example
- key_count: 1
  name: Hunter Meta Example
  slug: hunter-meta-example
- key_count: 3
  name: Hunter Pagination Meta Example
  slug: hunter-pagination-meta-example
- key_count: 20
  name: Hunter Person Enrichment Example
  slug: hunter-person-enrichment-example
- key_count: 5
  name: Hunter Source Example
  slug: hunter-source-example
- key_count: 2
  name: Hunter Usage Counter Example
  slug: hunter-usage-counter-example
- key_count: 2
  name: Hunter Verification Status Example
  slug: hunter-verification-status-example
features:
- description: Find all email addresses associated with a domain name along with confidence scores and sources.
  name: Domain Search
- description: Generate the most likely email address for a person given their name and company domain.
  name: Email Finder
- description: Verify the deliverability and validity of email addresses with detailed status reporting.
  name: Email Verification
- description: Store, organize, and manage prospect leads with lists, tags, and CRM-like contact management.
  name: Lead Management
- description: Create and manage automated email outreach sequences with recipient tracking and scheduling.
  name: Email Campaigns
- description: Enrich email addresses and domains with personal, company, and firmographic data points.
  name: Data Enrichment
- description: Find companies matching ideal customer profiles using natural language queries and advanced filters.
  name: Company Discovery
finops:
- name: Hunter Finops
  service_category: Sales Intelligence
  slug: hunter-finops
image: https://hunter.io/images/hunter-logo.png
integrations:
- description: Push verified leads and enriched contacts directly to Salesforce CRM for pipeline management.
  name: Salesforce
- description: Sync leads and contact data with HubSpot CRM for unified sales and marketing workflows.
  name: HubSpot
- description: Export leads to Pipedrive CRM with enriched contact and company information.
  name: Pipedrive
- description: Connect Hunter with thousands of apps through Zapier for automated lead processing workflows.
  name: Zapier
- description: Export domain search results and verified emails directly to Google Sheets for analysis.
  name: Google Sheets
- description: Integrate lead data with Zoho CRM for end-to-end sales pipeline management.
  name: Zoho CRM
json_schemas:
- name: AccountResult
  property_count: 9
  slug: hunter-account-result
- name: AccountResult
  property_count: 9
  slug: hunter-accountresult
- name: CampaignRecipient
  property_count: 3
  slug: hunter-campaign-recipient
- name: Campaign
  property_count: 9
  slug: hunter-campaign
- name: CampaignRecipient
  property_count: 3
  slug: hunter-campaignrecipient
- name: CompanyEnrichment
  property_count: 30
  slug: hunter-company-enrichment
- name: CompanyGeoLocation
  property_count: 12
  slug: hunter-company-geo-location
- name: CompanyEnrichment
  property_count: 31
  slug: hunter-companyenrichment
- name: CompanyGeoLocation
  property_count: 12
  slug: hunter-companygeolocation
- name: DiscoverRequest
  property_count: 12
  slug: hunter-discover-request
- name: DiscoverResult
  property_count: 3
  slug: hunter-discover-result
- name: DiscoverRequest
  property_count: 12
  slug: hunter-discoverrequest
- name: DiscoverResult
  property_count: 3
  slug: hunter-discoverresult
- name: DomainEmail
  property_count: 12
  slug: hunter-domain-email
- name: DomainSearchResult
  property_count: 7
  slug: hunter-domain-search-result
- name: DomainEmail
  property_count: 13
  slug: hunter-domainemail
- name: DomainSearchResult
  property_count: 7
  slug: hunter-domainsearchresult
- name: EmailCountResult
  property_count: 5
  slug: hunter-email-count-result
- name: EmailFinderResult
  property_count: 11
  slug: hunter-email-finder-result
- name: EmailVerifierResult
  property_count: 14
  slug: hunter-email-verifier-result
- name: EmailCountResult
  property_count: 5
  slug: hunter-emailcountresult
- name: EmailFinderResult
  property_count: 12
  slug: hunter-emailfinderresult
- name: EmailVerifierResult
  property_count: 14
  slug: hunter-emailverifierresult
- name: Error
  property_count: 1
  slug: hunter-error
- name: GeoLocation
  property_count: 7
  slug: hunter-geo-location
- name: GeoLocation
  property_count: 7
  slug: hunter-geolocation
- name: LeadInput
  property_count: 15
  slug: hunter-lead-input
- name: Lead
  property_count: 21
  slug: hunter-lead
- name: LeadInput
  property_count: 15
  slug: hunter-leadinput
- name: LeadsList
  property_count: 4
  slug: hunter-leads-list
- name: LeadsList
  property_count: 4
  slug: hunter-leadslist
- name: Meta
  property_count: 1
  slug: hunter-meta
- name: PaginationMeta
  property_count: 3
  slug: hunter-pagination-meta
- name: PaginationMeta
  property_count: 3
  slug: hunter-paginationmeta
- name: PersonEnrichment
  property_count: 20
  slug: hunter-person-enrichment
- name: PersonEnrichment
  property_count: 21
  slug: hunter-personenrichment
- name: Source
  property_count: 5
  slug: hunter-source
- name: UsageCounter
  property_count: 2
  slug: hunter-usage-counter
- name: UsageCounter
  property_count: 2
  slug: hunter-usagecounter
- name: VerificationStatus
  property_count: 2
  slug: hunter-verification-status
- name: VerificationStatus
  property_count: 2
  slug: hunter-verificationstatus
json_structures:
- name: Hunter Account Result Structure
  property_count: 9
  slug: hunter-account-result-structure
- name: Hunter Campaign Recipient Structure
  property_count: 3
  slug: hunter-campaign-recipient-structure
- name: Hunter Campaign Structure
  property_count: 9
  slug: hunter-campaign-structure
- name: Hunter Company Enrichment Structure
  property_count: 30
  slug: hunter-company-enrichment-structure
- name: Hunter Company Geo Location Structure
  property_count: 12
  slug: hunter-company-geo-location-structure
- name: Hunter Discover Request Structure
  property_count: 12
  slug: hunter-discover-request-structure
- name: Hunter Discover Result Structure
  property_count: 3
  slug: hunter-discover-result-structure
- name: Hunter Domain Email Structure
  property_count: 12
  slug: hunter-domain-email-structure
- name: Hunter Domain Search Result Structure
  property_count: 7
  slug: hunter-domain-search-result-structure
- name: Hunter Email Count Result Structure
  property_count: 5
  slug: hunter-email-count-result-structure
- name: Hunter Email Finder Result Structure
  property_count: 11
  slug: hunter-email-finder-result-structure
- name: Hunter Email Verifier Result Structure
  property_count: 14
  slug: hunter-email-verifier-result-structure
- name: Hunter Error Structure
  property_count: 1
  slug: hunter-error-structure
- name: Hunter Geo Location Structure
  property_count: 7
  slug: hunter-geo-location-structure
- name: Hunter Lead Input Structure
  property_count: 15
  slug: hunter-lead-input-structure
- name: Hunter Lead Structure
  property_count: 21
  slug: hunter-lead-structure
- name: Hunter Leads List Structure
  property_count: 4
  slug: hunter-leads-list-structure
- name: Hunter Meta Structure
  property_count: 1
  slug: hunter-meta-structure
- name: Hunter Pagination Meta Structure
  property_count: 3
  slug: hunter-pagination-meta-structure
- name: Hunter Person Enrichment Structure
  property_count: 20
  slug: hunter-person-enrichment-structure
- name: Hunter Source Structure
  property_count: 5
  slug: hunter-source-structure
- name: Hunter Structure
  property_count: 0
  slug: hunter-structure
- name: Hunter Usage Counter Structure
  property_count: 2
  slug: hunter-usage-counter-structure
- name: Hunter Verification Status Structure
  property_count: 2
  slug: hunter-verification-status-structure
jsonld:
- class_count: 0
  name: Hunter Context
  property_count: 0
  slug: hunter-context
layout: provider
mcp_servers:
- description: Hunter operates a first-party REMOTE MCP server at https://mcp.hunter.io/mcp using the Streamable HTTP transport. It is documented in Hunter's own API reference ("Model Context Protocol (MCP)" section
  name: Hunter Remote MCP Server
  slug: hunter-remote-mcp-server
- description: ''
  name: Hunter Remote MCP Endpoint
  slug: hunter-remote-mcp-endpoint
modified: '2026-08-13'
name: Hunter
nav: Providers
network: true
overview: 'Hunter publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account API, Campaigns API, Combined Enrichment API, and 9 more. Tagged areas include Contact Discovery, Email, Email Verification, Lead Generation, and Prospecting.


  The Hunter catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Hunter''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, signup flow, changelog, and 56 more developer resources.'
plans:
- name: Hunter Plans Pricing
  plan_count: 6
  slug: hunter-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 15
  name: Hunter Rate Limits
  slug: hunter-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Hunter API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: hunter-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Hunter API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 8
  slug: hunter-spectral-rules
scopes:
- name: Hunter Scopes
  scope_count: 2
  slug: hunter-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: exemplar
  composite: 68.0
  coverage:
    artifact_dirs: 33
    catalog_gap: 30.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 47.0
    contract_quality: 74.9
    developer_ergonomics: 64.3
    discoverability: 68.5
    governance: 47.0
    operational_transparency: 68.4
  previous_composite: 68.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hunter/refs/heads/main/screenshots/hunter-2026-06-20T182943.png
security:
- kind: authentication
  name: Hunter Authentication
  slug: hunter-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Hunter Domain Security
  slug: hunter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hunter Vulnerability Disclosure
  slug: hunter-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: hunter
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
use_cases:
- description: Find and verify email addresses for sales outreach by searching company domains and building prospect lists.
  name: Sales Prospecting
- description: Enrich leads with company and personal data to qualify prospects and prioritize outreach efforts.
  name: Lead Qualification
- description: Verify large email lists to reduce bounce rates and improve email deliverability.
  name: Email List Cleaning
- description: Discover key contacts at target accounts using domain search and build targeted outreach campaigns.
  name: Account-Based Marketing
- description: Find professional email addresses for passive candidates at target companies for recruitment campaigns.
  name: Recruitment Outreach
website: https://hunter.io/api
---
