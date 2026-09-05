---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://developers.marketo.com/'', ''status'': 301, ''note'': ''declared website redirects to https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/home — a different registrable domain (marketo.com -> adobe.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 98
  human_in_the_loop: 0
  name: Marketo Agentic Access
  operation_count: 166
  slug: marketo-agentic-access
  summary_line: 166 operations · 98 acting
api_count: 6
apis:
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: The Campaigns API from Marketo — 7 operation(s) for campaigns.
  name: Marketo Campaigns API
  slug: marketo-campaigns-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Channel Controller
  name: Marketo Channels API
  slug: marketo-channels-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: The Email Templates API from Marketo — 10 operation(s) for email templates.
  name: Marketo Email  Templates API
  slug: marketo-email-templates-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Email Controller
  name: Marketo Emails API
  slug: marketo-emails-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: The File Contents API from Marketo — 1 operation(s) for file contents.
  name: Marketo File  Contents API
  slug: marketo-file-contents-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: File Controller
  name: Marketo Files API
  slug: marketo-files-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Folder Controller
  name: Marketo Folders API
  slug: marketo-folders-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: The Form Fields API from Marketo — 9 operation(s) for form fields.
  name: Marketo Form  Fields API
  slug: marketo-form-fields-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Form Controller
  name: Marketo Forms API
  slug: marketo-forms-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: The Landing Page Content API from Marketo — 4 operation(s) for landing page content.
  name: Marketo Landing  Page  Content API
  slug: marketo-landing-page-content-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: The Landing Page Redirect Rules API from Marketo — 4 operation(s) for landing page redirect rules.
  name: Marketo Landing  Page  Redirect  Rules API
  slug: marketo-landing-page-redirect-rules-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: The Landing Page Templates API from Marketo — 9 operation(s) for landing page templates.
  name: Marketo Landing  Page  Templates API
  slug: marketo-landing-page-templates-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: The Landing Pages API from Marketo — 11 operation(s) for landing pages.
  name: Marketo Landing  Pages API
  slug: marketo-landing-pages-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Program Controller
  name: Marketo Programs API
  slug: marketo-programs-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Segment Controller
  name: Marketo Segments API
  slug: marketo-segments-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: The Smart Campaigns API from Marketo — 8 operation(s) for smart campaigns.
  name: Marketo Smart  Campaigns API
  slug: marketo-smart-campaigns-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: The Smart Lists API from Marketo — 4 operation(s) for smart lists.
  name: Marketo Smart  Lists API
  slug: marketo-smart-lists-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Snippet Controller
  name: Marketo Snippets API
  slug: marketo-snippets-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: The Static Lists API from Marketo — 3 operation(s) for static lists.
  name: Marketo Static  Lists API
  slug: marketo-static-lists-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Token Controller
  name: Marketo Tokens API
  slug: marketo-tokens-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Activities Controller
  name: Marketo Activities API
  slug: marketo-activities-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Bulk Export Activities Controller
  name: Marketo Bulk Export Activities API
  slug: marketo-bulk-export-activities-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Bulk Export Custom Objects Controller
  name: Marketo Bulk Export Custom Objects API
  slug: marketo-bulk-export-custom-objects-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Bulk Export Leads Controller
  name: Marketo Bulk Export Leads API
  slug: marketo-bulk-export-leads-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Bulk Export Program Members Controller
  name: Marketo Bulk Export Program Members API
  slug: marketo-bulk-export-program-members-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Bulk Import Custom Objects Controller
  name: Marketo Bulk Import Custom Objects API
  slug: marketo-bulk-import-custom-objects-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Bulk Import Leads Controller
  name: Marketo Bulk Import Leads API
  slug: marketo-bulk-import-leads-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Bulk Import Program Members Controller
  name: Marketo Bulk Import Program Members API
  slug: marketo-bulk-import-program-members-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Sync company records (createOnly, updateOnly, or createOrUpdate)
  name: Marketo Companies API
  slug: marketo-companies-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Upsert (insert or update) custom object records
  name: Marketo Custom Objects API
  slug: marketo-custom-objects-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: API endpoints for managing email templates created with the new Email Designer in Marketo Engage.
  name: Marketo Email Templates (New) API
  slug: marketo-email-templates-new-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: API endpoints for managing emails created with the new Email Designer in Marketo Engage.
  name: Marketo Emails (New) API
  slug: marketo-emails-new-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: API endpoints for managing fragments created with the new Email Designer in Marketo Engage.
  name: Marketo Fragments (New) API
  slug: marketo-fragments-new-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Identity Controller
  name: Marketo Identity API
  slug: marketo-identity-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Leads Controller
  name: Marketo Leads API
  slug: marketo-leads-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Add leads to or remove leads from static lists
  name: Marketo Lists API
  slug: marketo-lists-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Named Account Lists Controller
  name: Marketo Named Account Lists API
  slug: marketo-named-account-lists-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Named Accounts Controller
  name: Marketo Named Accounts API
  slug: marketo-named-accounts-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Opportunities Controller
  name: Marketo Opportunities API
  slug: marketo-opportunities-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Upsert (insert or update) person/lead records
  name: Marketo Persons API
  slug: marketo-persons-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Sync program member status or delete (remove) members from programs
  name: Marketo Program Members API
  slug: marketo-program-members-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Sales Persons Controller
  name: Marketo Sales Persons API
  slug: marketo-sales-persons-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Tag Controller
  name: Marketo Tags API
  slug: marketo-tags-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Stats Controller
  name: Marketo Usage API
  slug: marketo-usage-api
- baseURL: https://{munchkinId}.mktorest.com/rest
  baseurl_source: declared
  description: Marketo Engage provides a set of User Management endpoints allow you to perform CRUD operations on user records in Marketo.
  name: Marketo User Management API
  slug: marketo-user-management-api
artifact_total: 122
asyncapis:
- description: 'AsyncAPI 2.6 description of the two event-shaped surfaces Marketo Engage (Adobe) exposes to integrators: 1. Outbound Webhooks fired from Smart Campaign "Call Webhook" flow steps. Marketo issues an HTT'
  name: Marketo Engage Events
  slug: marketo-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Marketo Engage Rest Approve API
  slug: open-marketo-approve-api
- collection_type: open
  name: Marketo Engage Rest Approve Assets API
  slug: open-marketo-assets-api
- collection_type: open
  name: Marketo Engage Rest Approve Campaigns API
  slug: open-marketo-campaigns-api
- collection_type: open
  name: Marketo Engage Rest Approve Cc API
  slug: open-marketo-cc-api
- collection_type: open
  name: Marketo Engage Rest Approve Channel API
  slug: open-marketo-channel-api
- collection_type: open
  name: Marketo Engage Rest Approve Channels API
  slug: open-marketo-channels-api
- collection_type: open
  name: Marketo Engage Rest Approve Clone.json API
  slug: open-marketo-clone-json-api
- collection_type: open
  name: Marketo Engage Rest Approve Content API
  slug: open-marketo-content-api
- collection_type: open
  name: Marketo Engage Rest Approve Content.json API
  slug: open-marketo-content-json-api
- collection_type: open
  name: Marketo Engage Rest Approve Delete.json API
  slug: open-marketo-delete-json-api
- collection_type: open
  name: Marketo Engage Rest Approve Discard API
  slug: open-marketo-discard-api
- collection_type: open
  name: Marketo Engage Rest Approve Dynamic API
  slug: open-marketo-dynamic-api
- collection_type: open
  name: Marketo Engage Rest Approve Email API
  slug: open-marketo-email-api
- collection_type: open
  name: Marketo Engage Rest Approve Email  Templates API
  slug: open-marketo-email-templates-api
- collection_type: open
  name: Marketo Engage Rest Approve Emails API
  slug: open-marketo-emails-api
- collection_type: open
  name: Marketo Engage Rest API
  slug: open-marketo-engage-rest-api
- collection_type: open
  name: Marketo Engage Rest Approve Field API
  slug: open-marketo-field-api
- collection_type: open
  name: Marketo Engage Rest Approve Fields API
  slug: open-marketo-fields-api
- collection_type: open
  name: Marketo Engage Rest Approve File API
  slug: open-marketo-file-api
- collection_type: open
  name: Marketo Engage Rest Approve File  Contents API
  slug: open-marketo-file-contents-api
- collection_type: open
  name: Marketo Engage Rest Approve Files API
  slug: open-marketo-files-api
- collection_type: open
  name: Marketo Engage Rest Approve Folder API
  slug: open-marketo-folder-api
- collection_type: open
  name: Marketo Engage Rest Approve Folders API
  slug: open-marketo-folders-api
- collection_type: open
  name: Marketo Engage Rest Approve Form API
  slug: open-marketo-form-api
- collection_type: open
  name: Marketo Engage Rest Approve Form  Fields API
  slug: open-marketo-form-fields-api
- collection_type: open
  name: Marketo Engage Rest Approve Forms API
  slug: open-marketo-forms-api
- collection_type: open
  name: Marketo Engage Rest Approve Full API
  slug: open-marketo-full-api
- collection_type: open
  name: Marketo Engage Rest Approve Id API
  slug: open-marketo-id-api
- collection_type: open
  name: Marketo Engage Rest Approve .Json API
  slug: open-marketo-json-api
- collection_type: open
  name: Marketo Engage Rest Approve Landing API
  slug: open-marketo-landing-api
- collection_type: open
  name: Marketo Engage Rest Approve Landing  Page  Content API
  slug: open-marketo-landing-page-content-api
- collection_type: open
  name: Marketo Engage Rest Approve Landing  Page  Redirect  Rules API
  slug: open-marketo-landing-page-redirect-rules-api
- collection_type: open
  name: Marketo Engage Rest Approve Landing  Page  Templates API
  slug: open-marketo-landing-page-templates-api
- collection_type: open
  name: Marketo Engage Rest Approve Landing  Pages API
  slug: open-marketo-landing-pages-api
- collection_type: open
  name: Marketo Engage Rest Approve Member API
  slug: open-marketo-member-api
- collection_type: open
  name: Marketo Engage Rest Approve Modules API
  slug: open-marketo-modules-api
- collection_type: open
  name: Marketo Engage Rest Approve Name API
  slug: open-marketo-name-api
- collection_type: open
  name: Marketo Engage Rest Approve Name.json API
  slug: open-marketo-name-json-api
- collection_type: open
  name: Marketo Engage Rest Approve Page API
  slug: open-marketo-page-api
- collection_type: open
  name: Marketo Engage Rest Approve Program API
  slug: open-marketo-program-api
- collection_type: open
  name: Marketo Engage Rest Approve Programs API
  slug: open-marketo-programs-api
- collection_type: open
  name: Marketo Engage Rest Approve Redirect API
  slug: open-marketo-redirect-api
- collection_type: open
  name: Marketo Engage Approve Rest API
  slug: open-marketo-rest-api
- collection_type: open
  name: Marketo Engage Rest Approve Rules API
  slug: open-marketo-rules-api
- collection_type: open
  name: Marketo Engage Rest Approve Segments API
  slug: open-marketo-segments-api
- collection_type: open
  name: Marketo Engage Rest Approve Segments.json API
  slug: open-marketo-segments-json-api
- collection_type: open
  name: Marketo Engage Rest Approve Send API
  slug: open-marketo-send-api
- collection_type: open
  name: Marketo Engage Rest Approve Set API
  slug: open-marketo-set-api
- collection_type: open
  name: Marketo Engage Rest Approve Smart API
  slug: open-marketo-smart-api
- collection_type: open
  name: Marketo Engage Rest Approve Smart  Campaigns API
  slug: open-marketo-smart-campaigns-api
- collection_type: open
  name: Marketo Engage Rest Approve Smart  Lists API
  slug: open-marketo-smart-lists-api
- collection_type: open
  name: Marketo Engage Rest Approve Snippets API
  slug: open-marketo-snippets-api
- collection_type: open
  name: Marketo Engage Rest Approve Static API
  slug: open-marketo-static-api
- collection_type: open
  name: Marketo Engage Rest Approve Static  Lists API
  slug: open-marketo-static-lists-api
- collection_type: open
  name: Marketo Engage Rest Approve Submit API
  slug: open-marketo-submit-api
- collection_type: open
  name: Marketo Engage Rest Approve Template API
  slug: open-marketo-template-api
- collection_type: open
  name: Marketo Engage Rest Approve Templates API
  slug: open-marketo-templates-api
- collection_type: open
  name: Marketo Engage Rest Approve Text.json API
  slug: open-marketo-text-json-api
- collection_type: open
  name: Marketo Engage Rest Approve Thank API
  slug: open-marketo-thank-api
- collection_type: open
  name: Marketo Engage Rest Approve Tokens API
  slug: open-marketo-tokens-api
- collection_type: open
  name: Marketo Engage Rest Approve Type API
  slug: open-marketo-type-api
- collection_type: open
  name: Marketo Engage Rest Approve Unapprove.json API
  slug: open-marketo-unapprove-json-api
- collection_type: open
  name: Marketo Engage Rest Approve Used API
  slug: open-marketo-used-api
- collection_type: open
  name: Marketo Engage Rest Approve Variable API
  slug: open-marketo-variable-api
- collection_type: open
  name: Marketo Engage Rest Approve Variables API
  slug: open-marketo-variables-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/marketo-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/marketo-asset-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/marketo-lead-database-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/marketo-user-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/marketo-identity-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/marketo-data-ingestion-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marketo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marketo-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adobemarketoengage
- group: start
  title: ''
  type: DeveloperPortal
  url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/home
- group: start
  title: ''
  type: Portal
  url: https://developers.marketo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/rest-api
- group: docs
  title: ''
  type: APIReference
  url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/endpoint-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/getting-started
- group: operate
  title: ''
  type: Support
  url: https://experienceleaguecommunities.adobe.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Marketo
- group: design
  title: ''
  type: Webhooks
  url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/webhooks/webhooks
- group: build
  title: ''
  type: Libraries
  url: https://github.com/Marketo/Community-Supported-Client-Libraries
- group: build
  title: ''
  type: Packages
  url: packages/marketo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/marketo-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marketo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/marketo-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/marketo-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/marketo-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marketo-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/marketo-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/marketo-finops.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/marketo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://experienceleague.adobe.com/en/docs/marketo/using/release-notes/current
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/marketo-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/marketo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/marketo-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/marketo-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/marketo-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/marketo-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/marketo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/marketo-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/marketo-security.txt
- group: auth
  title: ''
  type: Security
  url: security/marketo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/marketo-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Rules
  url: rules/marketo-asyncapi-spectral-rules.yml
- group: operate
  title: ''
  type: Contact
  url: https://experienceleaguecommunities.adobe.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy/policy.html
- group: commercial
  title: ''
  type: License
  url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/api-license
created: '2023-11-23'
description: Marketo, an Adobe company, develops and sells B2B marketing automation software for account-based marketing, lead management, email marketing and campaign execution. Adobe Marketo Engage publishes five machine-readable specifications covering 367 REST operations across five surfaces — a Lead Database API for person records, activity and change feeds, companies, opportunities, custom objects, static lists, smart campaigns and bulk import/export; an Asset API for emails, landing pages, forms, templates, snippets and segments; a User Management API for users, roles and workspaces; an Identity endpoint issuing two-legged OAuth 2.0 client-credentials tokens; and an asynchronous Data Ingestion API on a separate Adobe-hosted domain. The base URL is per-subscription (https://{munchkinId}.mktorest.com), authorization is role-permission rather than OAuth-scope based, and most failures — including rate-limit and quota exhaustion — are returned inside an HTTP 200 body.
finops:
- name: Marketo Finops
  service_category: API
  slug: marketo-finops
graphqls:
- description: Marketo Engage is Adobe's marketing automation platform offering programmatic access to leads, programs, campaigns, assets, lists, and bulk import/export via a REST API. This conceptual GraphQL schema
  name: Marketo (Adobe) GraphQL Schema
  slug: marketo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marketo.png
layout: provider
modified: '2026-08-13'
name: Marketo
nav: Providers
network: true
overview: 'Marketo publishes 45 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Channels API, Email  Templates API, and 42 more. Tagged areas include Adobe, Automation, Marketing, Marketing Automation, and Email Marketing.


  The Marketo catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Marketo''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, authentication, changelog, and 40 more developer resources.'
plans:
- name: Marketo Plans Pricing
  plan_count: 0
  slug: marketo-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 6
  name: Marketo Rate Limits
  slug: marketo-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Marketo API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: marketo-asyncapi-spectral-rules
scopes:
- name: Marketo Scopes
  scope_count: 24
  slug: marketo-scopes
  summary_line: 24 scopes
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 58.6
    developer_ergonomics: 63.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 45
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marketo/refs/heads/main/screenshots/marketo-2026-06-20T184954.png
security:
- kind: authentication
  name: Marketo Authentication
  slug: marketo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Marketo Domain Security
  slug: marketo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Marketo Vulnerability Disclosure
  slug: marketo-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: marketo
tags:
- Adobe
- Automation
- Marketing
- Marketing Automation
- Email Marketing
- Lead Management
- Campaign Management
- CRM
- Customer Engagement
- B2B
website: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/home
---
