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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Hunter Io Agentic Access
  operation_count: 15
  slug: hunter-io-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 8
apis:
- description: Account metadata and usage counters.
  name: Hunter Account API
  slug: hunter-io-account-api
- description: Company discovery and prospecting.
  name: Hunter Discover API
  slug: hunter-io-discover-api
- description: Discover all emails for a domain or company.
  name: Hunter Domain Search API
  slug: hunter-io-domain-search-api
- description: Count emails for a domain.
  name: Hunter Email Count API
  slug: hunter-io-email-count-api
- description: Find the email address of a person at a company.
  name: Hunter Email Finder API
  slug: hunter-io-email-finder-api
- description: Verify the deliverability of an email address.
  name: Hunter Email Verifier API
  slug: hunter-io-email-verifier-api
- description: Person, company, and combined enrichment.
  name: Hunter Enrichment API
  slug: hunter-io-enrichment-api
- description: Lead management.
  name: Hunter Leads API
  slug: hunter-io-leads-api
arazzos:
- description: Verify an email, upsert it as a lead, then assign the lead to a target leads list.
  name: Hunter Add Verified Lead To List
  slug: hunter-io-add-verified-lead-to-list-workflow
- description: Resolve an author's email from their name and publication domain, verify it, then enrich their profile.
  name: Hunter Author Finder
  slug: hunter-io-author-finder-workflow
- description: Find a contact, verify it, and seed a campaign by creating a verified lead in a target list.
  name: Hunter Campaign Lead Builder
  slug: hunter-io-campaign-lead-builder-workflow
- description: Use the free Email Count to confirm coverage before spending a credit on Domain Search.
  name: Hunter Count Gated Domain Search
  slug: hunter-io-count-gated-domain-search-workflow
- description: Check account search credits first and run a Domain Search only when credits remain.
  name: Hunter Credit Guarded Domain Search
  slug: hunter-io-credit-guarded-domain-search-workflow
- description: Discover companies matching a target profile, then pull the email list for the top match's domain.
  name: Hunter Discover To Domain Emails
  slug: hunter-io-discover-to-domain-emails-workflow
- description: Discover a domain's email pattern, find a specific person's email, then verify its deliverability.
  name: Hunter Domain To Verified Email
  slug: hunter-io-domain-to-verified-email-workflow
- description: Combined-enrich an email into person and company data, then upsert a fully populated lead.
  name: Hunter Enrich Email To Lead
  slug: hunter-io-enrich-email-to-lead-workflow
- description: Find a person's email, verify it, and create a lead only when the address is deliverable.
  name: Hunter Find Verify Create Lead
  slug: hunter-io-find-verify-create-lead-workflow
- description: Retrieve a stored lead, re-verify its email, and update or delete it based on the result.
  name: Hunter Reverify Lead
  slug: hunter-io-reverify-lead-workflow
- description: Verify a known email and upsert it into Hunter as a lead with its verification status.
  name: Hunter Verify Existing Email
  slug: hunter-io-verify-existing-email-workflow
artifact_total: 78
collections:
- collection_type: postman
  name: Hunter Account API
  slug: postman-hunter-account-api
- collection_type: postman
  name: Hunter Discover API
  slug: postman-hunter-discover-api
- collection_type: postman
  name: Hunter Domain Search API
  slug: postman-hunter-domain-search-api
- collection_type: postman
  name: Hunter Email Count API
  slug: postman-hunter-email-count-api
- collection_type: postman
  name: Hunter Email Finder API
  slug: postman-hunter-email-finder-api
- collection_type: postman
  name: Hunter Email Verifier API
  slug: postman-hunter-email-verifier-api
- collection_type: postman
  name: Hunter Enrichment API
  slug: postman-hunter-enrichment-api
- collection_type: postman
  name: Hunter Leads API
  slug: postman-hunter-leads-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hunter Account API
  slug: open-hunter-account-api
- collection_type: open
  name: Hunter Discover API
  slug: open-hunter-discover-api
- collection_type: open
  name: Hunter Domain Search API
  slug: open-hunter-domain-search-api
- collection_type: open
  name: Hunter Email Count API
  slug: open-hunter-email-count-api
- collection_type: open
  name: Hunter Email Finder API
  slug: open-hunter-email-finder-api
- collection_type: open
  name: Hunter Email Verifier API
  slug: open-hunter-email-verifier-api
- collection_type: open
  name: Hunter Enrichment API
  slug: open-hunter-enrichment-api
- collection_type: open
  name: Hunter Account API
  slug: open-hunter-io-account-api
- collection_type: open
  name: Hunter Account Discover API
  slug: open-hunter-io-discover-api
- collection_type: open
  name: Hunter Account Domain Search API
  slug: open-hunter-io-domain-search-api
- collection_type: open
  name: Hunter Account Email Count API
  slug: open-hunter-io-email-count-api
- collection_type: open
  name: Hunter Account Email Finder API
  slug: open-hunter-io-email-finder-api
- collection_type: open
  name: Hunter Account Email Verifier API
  slug: open-hunter-io-email-verifier-api
- collection_type: open
  name: Hunter Account Enrichment API
  slug: open-hunter-io-enrichment-api
- collection_type: open
  name: Hunter Account Leads API
  slug: open-hunter-io-leads-api
- collection_type: open
  name: Hunter Leads API
  slug: open-hunter-leads-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hunter-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hunter-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hunter-io-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hunter/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-io-add-verified-lead-to-list-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-io-author-finder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-io-campaign-lead-builder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-io-count-gated-domain-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-io-credit-guarded-domain-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-io-discover-to-domain-emails-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-io-domain-to-verified-email-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-io-enrich-email-to-lead-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-io-find-verify-create-lead-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-io-reverify-lead-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hunter-io-verify-existing-email-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://hunter.io
- group: docs
  title: ''
  type: Documentation
  url: https://hunter.io/api-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://hunter.io/api-documentation/v2
- group: start
  title: ''
  type: GettingStarted
  url: https://hunter.io/api-documentation/v2#introduction
- group: auth
  title: ''
  type: Authentication
  url: https://hunter.io/api-documentation/v2#authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://hunter.io/api-documentation/v2#rate-limiting
- group: design
  title: ''
  type: ErrorCodes
  url: https://hunter.io/api-documentation/v2#errors
- group: operate
  title: ''
  type: ChangeLog
  url: https://hunter.io/api-documentation/v2#changelog
- group: company
  title: ''
  type: Blog
  url: https://hunter.io/blog
- group: start
  title: ''
  type: Signup
  url: https://hunter.io/users/sign_up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hunter.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hunter.io/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hunter.io
- group: operate
  title: ''
  type: Support
  url: https://hunter.io/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hunter-io
- group: build
  title: ''
  type: Plugin
  url: https://chrome.google.com/webstore/detail/hunter-find-email-address/hgmhmanijnjhaffoampdlllchpolkdnj
- group: build
  title: ''
  type: Plugin
  url: https://addons.mozilla.org/en-US/firefox/addon/hunterio/
- group: build
  title: ''
  type: Tools
  url: https://hunter.io/email-pattern
- group: build
  title: ''
  type: Tools
  url: https://hunter.io/email-verifier
- group: build
  title: ''
  type: Tools
  url: https://hunter.io/email-finder
- group: build
  title: ''
  type: Tools
  url: https://hunter.io/bulks
- group: build
  title: ''
  type: Tools
  url: https://hunter.io/companies
- group: other
  title: ''
  type: Resource
  url: https://hunter.io/templates
- group: other
  title: ''
  type: Glossary
  url: https://hunter.io/email-marketing-glossary
- group: build
  title: ''
  type: Plugin
  url: https://github.com/hunter-io/claude-plugin
- group: build
  title: ''
  type: Tools
  url: https://github.com/hunter-io/chatgpt-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/hunter-io/hunter-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/hunter-io/mcp-oauth-proxy
- group: build
  title: ''
  type: Tools
  url: https://github.com/hunter-io/baseimage-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/hunter-io/sentry-ruby
- group: commercial
  title: ''
  type: Plans
  url: plans/hunter-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hunter-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hunter-io-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hunter-io-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/hunter-io-rules.yml
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/hunter-io-structure.json
created: '2026-05-25T00:00:00.000Z'
description: Hunter.io is an email-intelligence and outbound platform that finds, verifies, and enriches professional email addresses at scale. Its public APIs cover Domain Search, Email Finder, Email Verifier, Email Count, Discover (company prospecting), Person/Company/Combined Enrichment, Leads management, and Account/usage inspection. Credit-based metering, plan-tiered monthly allowances, and per-endpoint rate limits make it a reference example of a usage-based B2B data API.
examples:
- key_count: 2
  name: Hunter Domain Search Example
  slug: hunter-domain-search-example
- key_count: 2
  name: Hunter Email Finder Example
  slug: hunter-email-finder-example
- key_count: 2
  name: Hunter Email Verifier Example
  slug: hunter-email-verifier-example
features:
- Domain Search returns all emails for a domain with sources, confidence, department, and seniority
- Email Finder predicts the most likely address for a person at a company with 0-100 confidence
- Email Verifier runs MX, SMTP, regex, disposable, webmail, accept-all, and block checks plus database lookup
- Email Count is free and unauthenticated for pre-flight sizing of a domain's email footprint
- Discover API for company prospecting via natural language or structured filters
- Person, company, and combined enrichment with optional Clearbit-shape response for drop-in migration
- Leads API with CRUD, upsert, filtered list, custom attributes, and lead-list scoping
- Campaigns API for outbound sequences, recipients, opens, clicks, replies, and unsubscribes
- Account API returns plan, reset date, and per-meter usage counters for FinOps
- Three auth modes: api_key query, X-API-KEY header, or Authorization Bearer
- Token-bucket-style per-endpoint rate limits with 429 responses (5-15 rps, 50-500 rpm)
- Monthly credit allowances per plan with reset_date semantics
- Chrome and Firefox browser extensions, Google Sheets add-on, and Bulk Tasks UI
- Native integrations with Salesforce, HubSpot, Zapier, Pipedrive, Zoho CRM, and many outbound tools
- Hunter MCP server and ChatGPT MCP server for agentic email-finder workflows
- Hunter Claude Plugin for find, verify, and enrich workflows inside Claude
- GDPR-aligned data handling with 451 responses on restricted personal data
finops:
- name: Hunter Io Finops
  service_category: Marketing and Sales
  slug: hunter-io-finops
graphqls:
- description: Conceptual GraphQL schema for the Hunter.io email intelligence and outbound platform, derived from the Hunter.io REST API (https://hunter.io/api-documentation/v2).
  name: Hunter.io GraphQL Schema
  slug: hunter-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hunter-io.png
json_schemas:
- name: Hunter Email
  property_count: 13
  slug: hunter-email
- name: Hunter Lead
  property_count: 24
  slug: hunter-lead
- name: Hunter Email Verification Result
  property_count: 14
  slug: hunter-verification
json_structures:
- name: Hunter Io Structure
  property_count: 0
  slug: hunter-io-structure
jsonld:
- class_count: 0
  name: Hunter Io Context
  property_count: 4
  slug: hunter-io-context
layout: provider
modified: '2026-05-25'
name: Hunter
nav: Providers
network: true
overview: 'Hunter publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Discover API, Domain Search API, and 5 more. Tagged areas include Email Finder, Email Verifier, Lead Generation, Outreach, and Prospecting.


  The Hunter catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Hunter''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, engineering blog, signup flow, and 44 more developer resources.'
plans:
- name: Hunter Io Plans Pricing
  plan_count: 5
  slug: hunter-io-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 8
  name: Hunter Io Rate Limits
  slug: hunter-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Hunter API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hunter-io-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Hunter API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 4
  slug: hunter-io-rules
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 28.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 28.8
    contract_quality: 72.8
    developer_ergonomics: 61.9
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 50.0
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hunter-io/refs/heads/main/screenshots/hunter-io-2026-06-20T182944.png
security:
- kind: authentication
  name: Hunter Io Authentication
  slug: hunter-io-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Hunter Io Domain Security
  slug: hunter-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hunter-io
tags:
- Email Finder
- Email Verifier
- Lead Generation
- Outreach
- Prospecting
- Enrichment
- Sales
- Marketing
website: https://hunter.io
---
