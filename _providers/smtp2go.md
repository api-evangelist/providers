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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Smtp2Go Agentic Access
  operation_count: 52
  slug: smtp2go-agentic-access
  summary_line: 52 operations · 52 acting
api_count: 1
apis:
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Email activity search
  name: SMTP2GO Activity API
  slug: smtp2go-activity-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: API key management
  name: SMTP2GO API Keys API
  slug: smtp2go-api-keys-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Send and receive SMS messages
  name: SMTP2GO SMS API
  slug: smtp2go-sms-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: SMTP user account management
  name: SMTP2GO SMTP Users API
  slug: smtp2go-smtp-users-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Subaccount management
  name: SMTP2GO Subaccounts API
  slug: smtp2go-subaccounts-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Suppression list management
  name: SMTP2GO Suppressions API
  slug: smtp2go-suppressions-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Email template management
  name: SMTP2GO Templates API
  slug: smtp2go-templates-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Webhook configuration
  name: SMTP2GO Webhooks API
  slug: smtp2go-webhooks-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Manage the allowed recipients list
  name: SMTP2GO ALLOWED RECIPIENTS API
  slug: smtp2go-allowed-recipients-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Manage the allowed/restricted senders list
  name: SMTP2GO ALLOWED SENDERS API
  slug: smtp2go-allowed-senders-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: View dedicated IP addresses on the account
  name: SMTP2GO DEDICATED IPS API
  slug: smtp2go-dedicated-ips-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Search and retrieve archived email content
  name: SMTP2GO EMAIL ARCHIVE API
  slug: smtp2go-email-archive-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Send standard, MIME and batch email; manage scheduled sends
  name: SMTP2GO EMAILS API
  slug: smtp2go-emails-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Manage the account IP allow list for SMTP and API access
  name: SMTP2GO IP Allow List API
  slug: smtp2go-ip-allow-list-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Manage IP-authenticated sending entries
  name: SMTP2GO IP AUTH API
  slug: smtp2go-ip-auth-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Add, verify and manage sender domains, tracking and return-path subdomains
  name: SMTP2GO SENDER DOMAINS API
  slug: smtp2go-sender-domains-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Verify individual From addresses
  name: SMTP2GO SINGLE SENDER EMAILS API
  slug: smtp2go-single-sender-emails-api
- baseURL: https://api.smtp2go.com/v3
  baseurl_source: declared
  description: Delivery, bounce, spam, unsubscribe and cycle statistics
  name: SMTP2GO STATISTICS API
  slug: smtp2go-statistics-api
artifact_total: 45
asyncapis:
- description: ''
  name: Smtp2Go Webhooks
  slug: smtp2go-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SMTP2GO Email Activity API
  slug: open-smtp2go-activity-api
- collection_type: open
  name: SMTP2GO Email Activity API Keys API
  slug: open-smtp2go-api-keys-api
- collection_type: open
  name: SMTP2GO Email Activity Domains API
  slug: open-smtp2go-domains-api
- collection_type: open
  name: SMTP2GO Activity Email API
  slug: open-smtp2go-email-api
- collection_type: open
  name: SMTP2GO Email Activity SMS API
  slug: open-smtp2go-sms-api
- collection_type: open
  name: SMTP2GO Email Activity SMTP Users API
  slug: open-smtp2go-smtp-users-api
- collection_type: open
  name: SMTP2GO Email Activity Stats API
  slug: open-smtp2go-stats-api
- collection_type: open
  name: SMTP2GO Email Activity Subaccounts API
  slug: open-smtp2go-subaccounts-api
- collection_type: open
  name: SMTP2GO Email Activity Suppressions API
  slug: open-smtp2go-suppressions-api
- collection_type: open
  name: SMTP2GO Email Activity Templates API
  slug: open-smtp2go-templates-api
- collection_type: open
  name: SMTP2GO Email Activity Webhooks API
  slug: open-smtp2go-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/smtp2go-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smtp2go-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smtp2go-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smtp2go-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.smtp2go.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.smtp2go.com/docs/introduction-guide
- group: docs
  title: ''
  type: APIReference
  url: https://developers.smtp2go.com/reference/general-api-resources
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/smtp2go-oss
- group: company
  title: ''
  type: Blog
  url: https://www.smtp2go.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smtp2go.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://smtp2gostatus.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smtp2go
- group: other
  title: ''
  type: X
  url: https://x.com/smtp2go
- group: operate
  title: ''
  type: Support
  url: https://support.smtp2go.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/smtp2go-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smtp2go-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smtp2go-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/smtp2go-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/smtp2go-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/smtp2go-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/smtp2go-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smtp2go-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/smtp2go-api-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/smtp2go-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/smtp2go-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/smtp2go-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/smtp2go-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.smtp2go.com/reference/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/smtp2go-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.smtp2go.com/blog/security-and-privacy-at-smtp2go/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/smtp2go-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/smtp2go-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/smtp2go-data-model.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.smtp2go.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.smtp2go.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.smtp2go.com/pricing/signup/
- group: start
  title: ''
  type: Login
  url: https://app.smtp2go.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smtp2go.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smtp2go.com/privacy/
created: '2026-06-13'
description: SMTP2GO is a New Zealand-founded email and SMS delivery platform, running since 2006, that sends and tracks transactional and marketing messages over SMTP relay or a JSON REST API from data centres in the United States, the European Union and Australia. The v3 API covers sending standard, MIME, batch and scheduled email, sending and receiving SMS, verifying sender domains and single sender addresses, managing SMTP users, API keys, IP allow lists and IP authentication, templates, webhooks, suppressions, subaccounts, dedicated IPs and the email archive, plus activity search and delivery statistics. It also ships a remote MCP server and a published Agent Skill for AI agents.
examples:
- key_count: 4
  name: Add Suppression Example
  slug: add-suppression-example
- key_count: 4
  name: Send Email Example
  slug: send-email-example
- key_count: 4
  name: Send Sms Example
  slug: send-sms-example
finops:
- name: Smtp2Go Finops
  service_category: ''
  slug: smtp2go-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smtp2go.png
json_schemas:
- name: SMTP2GO Send Email Request
  property_count: 15
  slug: smtp2go-send-email
- name: SMTP2GO Suppression
  property_count: 6
  slug: smtp2go-suppression
jsonld:
- class_count: 9
  name: Smtp2Go Context
  property_count: 66
  slug: smtp2go-context
layout: provider
mcp_servers:
- description: ''
  name: SMTP2GO remote MCP server
  slug: smtp2go-remote-mcp-server
modified: '2026-08-13'
name: SMTP2GO
nav: Providers
network: true
overview: 'SMTP2GO publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Activity API, API Keys API, SMS API, and 15 more. Tagged areas include Email, Email Delivery, Transactional Email, SMTP, and SMS.


  The SMTP2GO catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SMTP2GO''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, support, changelog, and 33 more developer resources.'
plans:
- name: Smtp2Go Plans Pricing
  plan_count: 4
  slug: smtp2go-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 9
  name: Smtp2Go Rate Limits
  slug: smtp2go-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SMTP2GO API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: smtp2go-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 72.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 78.3
    catalog_earned_first_party: 24.0
    catalog_gap: 36.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 28.0
    contract_quality: 74.5
    developer_ergonomics: 63.1
    discoverability: 75.9
    governance: 28.0
    operational_transparency: 76.3
  previous_composite: 72.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smtp2go/refs/heads/main/screenshots/smtp2go-2026-06-20T194102.png
security:
- kind: authentication
  name: Smtp2Go Authentication
  slug: smtp2go-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Smtp2Go Domain Security
  slug: smtp2go-domain-security
  summary_line: TLSv1.3 · DMARC
slug: smtp2go
tags:
- Email
- Email Delivery
- Transactional Email
- SMTP
- SMS
- Email API
- Deliverability
- Webhook
- Messaging
- Communications
- MCP
- Agent Skills
website: https://www.smtp2go.com/
---
