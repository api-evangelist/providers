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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 63.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Politicalcomms Com Agentic Access
  operation_count: 61
  slug: politicalcomms-com-agentic-access
  summary_line: 61 operations · 22 acting
api_count: 1
apis:
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: List 10DLC campaigns (carrier registrations) across your organization hierarchy.
  name: politicalcomms-com 10DLC Campaigns API
  slug: politicalcomms-com-10dlc-campaigns-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: Message statistics and delivery performance.
  name: politicalcomms-com Analytics API
  slug: politicalcomms-com-analytics-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: Usage and billing data across your organization.
  name: politicalcomms-com Billing API
  slug: politicalcomms-com-billing-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: List brands across your organization hierarchy.
  name: politicalcomms-com Brands API
  slug: politicalcomms-com-brands-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: List, import, and analyze contact lists.
  name: politicalcomms-com Contact Lists API
  slug: politicalcomms-com-contact-lists-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: Read inbound threads and reply inside them from the same number. Conversations are created by project sends; the API never starts one.
  name: politicalcomms-com Conversations API
  slug: politicalcomms-com-conversations-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: Create, schedule, and report on email campaigns. Pause, resume, and test sends are deliverability decisions a human makes while watching a send, and live in the dashboard.
  name: politicalcomms-com Email Campaigns API
  slug: politicalcomms-com-email-campaigns-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: Create email lists, read their contacts, and bulk-upsert or import addresses. To stop mailing someone use Email Suppressions, which survives a re-import.
  name: politicalcomms-com Email Lists API
  slug: politicalcomms-com-email-lists-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: Read the sender identities (From addresses) on your verified domains. Identities carry the physical mailing address and paid-for-by disclaimer, so they are created and edited in the dashboard.
  name: politicalcomms-com Email Senders API
  slug: politicalcomms-com-email-senders-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: Read, add, and lift suppressions in bulk. This is the primitive for keeping your own opt-out record in sync with ours.
  name: politicalcomms-com Email Suppressions API
  slug: politicalcomms-com-email-suppressions-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: Create and read saved email templates.
  name: politicalcomms-com Email Templates API
  slug: politicalcomms-com-email-templates-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: List, import, and fetch media files.
  name: politicalcomms-com Media Files API
  slug: politicalcomms-com-media-files-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: List descendant organizations and hierarchy.
  name: politicalcomms-com Organizations API
  slug: politicalcomms-com-organizations-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: List phone numbers across 10DLC campaigns and toll-free verifications.
  name: politicalcomms-com Phone Numbers API
  slug: politicalcomms-com-phone-numbers-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: Create, edit, test, schedule, and inspect projects.
  name: politicalcomms-com Projects API
  slug: politicalcomms-com-projects-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: 'Read the sending domains in your organization and the DNS records to publish. Domains are added in the dashboard: DNS is published by hand, so creation is not part of the API.'
  name: politicalcomms-com Sending Domains API
  slug: politicalcomms-com-sending-domains-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: List toll-free verifications (carrier registrations) across your organization hierarchy.
  name: politicalcomms-com Toll-Free Verifications API
  slug: politicalcomms-com-toll-free-verifications-api
- baseURL: https://api.politicalcomms.com/v1
  baseurl_source: declared
  description: List active link-tracking domains. Use the returned ids as `link_tracking_domain_id` on project create/update.
  name: politicalcomms-com Tracking Domains API
  slug: politicalcomms-com-tracking-domains-api
artifact_total: 38
common:
- group: agent
  href: https://artifacts.apis.io/politicalcomms-com/agentic-access/politicalcomms-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/politicalcomms-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/politicalcomms-com/rate-limits/politicalcomms-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/politicalcomms-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/politicalcomms-com/plans/politicalcomms-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/politicalcomms-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/politicalcomms-com/rules/politicalcomms-com-rules.yml
  title: ''
  type: Spectral
  url: rules/politicalcomms-com-rules.yml
- group: design
  href: https://artifacts.apis.io/politicalcomms-com/json-ld/politicalcomms-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/politicalcomms-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/politicalcomms-com/vocabulary/politicalcomms-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/politicalcomms-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/politicalcomms-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/politicalcomms-com/data-model/politicalcomms-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/politicalcomms-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/politicalcomms-com/cli/politicalcomms-com-cli.yml
  title: ''
  type: CLI
  url: cli/politicalcomms-com-cli.yml
- group: design
  href: https://artifacts.apis.io/politicalcomms-com/conventions/politicalcomms-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/politicalcomms-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/politicalcomms-com/conventions/politicalcomms-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/politicalcomms-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://politicalcomms.com/security
- group: auth
  href: https://artifacts.apis.io/politicalcomms-com/authentication/politicalcomms-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/politicalcomms-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/politicalcomms-com/errors/politicalcomms-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/politicalcomms-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/politicalcomms-com/conformance/politicalcomms-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/politicalcomms-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/politicalcomms-com/llms/politicalcomms-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/politicalcomms-com-llms.txt
- group: other
  href: https://artifacts.apis.io/politicalcomms-com/a2a/politicalcomms-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/politicalcomms-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/politicalcomms-com/mcp/politicalcomms-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/politicalcomms-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/politicalcomms-com/well-known/politicalcomms-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/politicalcomms-com-security.txt
- group: agent
  href: https://artifacts.apis.io/politicalcomms-com/well-known/politicalcomms-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/politicalcomms-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/politicalcomms-com/hosts/politicalcomms-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/politicalcomms-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/politicalcomms-com/vendors/politicalcomms-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/politicalcomms-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/politicalcomms-com/packages/politicalcomms-com-packages.yml
  title: ''
  type: SDKs
  url: packages/politicalcomms-com-packages.yml
- group: build
  href: https://artifacts.apis.io/politicalcomms-com/packages/politicalcomms-com-packages.yml
  title: ''
  type: Packages
  url: packages/politicalcomms-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.politicalcomms.com
- group: auth
  title: ''
  type: Security
  url: https://politicalcomms.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://politicalcomms.com/press/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://politicalcomms.com/developers/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.politicalcomms.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.politicalcomms.com/api-reference/introduction
- group: auth
  href: https://artifacts.apis.io/politicalcomms-com/security/politicalcomms-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/politicalcomms-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/politicalcomms-com/security/politicalcomms-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/politicalcomms-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/politicalcomms-com/security/politicalcomms-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/politicalcomms-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://politicalcomms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.politicalcomms.com/
- group: company
  title: ''
  type: Blog
  url: https://politicalcomms.com/blog
- group: operate
  title: ''
  type: Support
  url: https://politicalcomms.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://politicalcomms.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://politicalcomms.com/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://politicalcomms.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.politicalcomms.com/introduction
- group: start
  title: ''
  type: SignUp
  url: https://app.politicalcomms.com/
created: '2026-10-30'
description: Political Comms provides a direct-to-carrier political texting platform that enables compliant, large‑scale SMS, MMS, and RCS messaging for campaigns, PACs, advocacy groups, fundraisers, and elected officials across the United States. Founded in 2019, the service offers fast delivery, high throughput, and tools for voter outreach, fundraising, and volunteer coordination.
image: https://politicalcomms.com/images/brand/pcomms-logo-left-of-text.png
json_schemas:
- name: ConversationMessage
  property_count: 10
  slug: politicalcomms-com-conversation-message
- name: Conversation
  property_count: 14
  slug: politicalcomms-com-conversation
- name: EmailCampaign
  property_count: 23
  slug: politicalcomms-com-email-campaign
- name: EmailDomain
  property_count: 9
  slug: politicalcomms-com-email-domain
- name: EmailListImport
  property_count: 13
  slug: politicalcomms-com-email-list-import
- name: EmailSenderIdentity
  property_count: 14
  slug: politicalcomms-com-email-sender-identity
jsonld:
- class_count: 23
  name: Politicalcomms Com Context
  property_count: 135
  slug: politicalcomms-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at politicalcomms.com requiring an API key.
  name: politicalcomms-com MCP Server
  slug: politicalcomms-com-mcp-yml
modified: '2026-10-30'
name: politicalcomms-com
nav: Providers
network: true
overview: 'politicalcomms-com publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including 10DLC Campaigns API, Analytics API, Billing API, and 15 more. Tagged areas include Company, Political, Messaging, SMS, and RCS.


  The politicalcomms-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  politicalcomms-com''s developer surface includes CLI, authentication, changelog, API reference, documentation, engineering blog, support, and 35 more developer resources.'
plans:
- name: Politicalcomms Com Plans Pricing
  plan_count: 4
  slug: politicalcomms-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Politicalcomms Com Rate Limits
  slug: politicalcomms-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 116
  extends:
  - spectral:oas
  name: politicalcomms-com API Rules
  rule_count: 75
  severity_counts:
    error: 66
    hint: 0
    info: 1
    warn: 8
  slug: politicalcomms-com-rules
scopes:
- name: Politicalcomms Com Scopes
  scope_count: 0
  slug: politicalcomms-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 36
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.4
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 67.3
    developer_ergonomics: 55.2
    discoverability: 75.8
    operational_transparency: 42.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 73.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 38.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/politicalcomms-com/politicalcomms-com-2026-11-03T141343.png
security:
- kind: authentication
  name: Politicalcomms Com Authentication
  slug: politicalcomms-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Politicalcomms Com Domain Security
  slug: politicalcomms-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Politicalcomms Com Vulnerability Disclosure
  slug: politicalcomms-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Politicalcomms Com Trust Center
  slug: politicalcomms-com-trust-center
  summary_line: SOC 2, GDPR
skill_count: 3
skills:
- name: create-email-campaign
  slug: politicalcomms-com-create-email-campaign
- name: create-project
  slug: politicalcomms-com-create-project
- name: list-organizations
  slug: politicalcomms-com-list-organizations
slug: politicalcomms-com
tags:
- Company
- Political
- Messaging
- SMS
- RCS
- Campaigns
website: https://politicalcomms.com/
---
