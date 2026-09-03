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
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Stannp Agentic Access
  operation_count: 32
  slug: stannp-agentic-access
  summary_line: 32 operations · 23 acting
api_count: 1
apis:
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Account balance and user information
  name: Stannp Account API
  slug: stannp-account-api
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Manage batch direct mail campaigns
  name: Stannp Campaigns API
  slug: stannp-campaigns-api
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Record recipient engagement and conversion events
  name: Stannp Events API
  slug: stannp-events-api
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Manage recipient groups
  name: Stannp Groups API
  slug: stannp-groups-api
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Create, post, retrieve, and cancel letter mailpieces
  name: Stannp Letters API
  slug: stannp-letters-api
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Create, retrieve, and cancel postcard mailpieces
  name: Stannp Postcards API
  slug: stannp-postcards-api
- baseURL: https://api-eu1.stannp.com/v1/
  baseurl_source: declared
  description: Manage individual recipients and bulk imports
  name: Stannp Recipients API
  slug: stannp-recipients-api
artifact_total: 33
asyncapis:
- description: ''
  name: Stannp Webhooks
  slug: stannp-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stannp Direct Mail Account API
  slug: open-stannp-account-api
- collection_type: open
  name: Stannp Direct Mail Account Campaigns API
  slug: open-stannp-campaigns-api
- collection_type: open
  name: Stannp Direct Mail Account Events API
  slug: open-stannp-events-api
- collection_type: open
  name: Stannp Direct Mail Account Groups API
  slug: open-stannp-groups-api
- collection_type: open
  name: Stannp Direct Mail Account Letters API
  slug: open-stannp-letters-api
- collection_type: open
  name: Stannp Direct Mail Account Postcards API
  slug: open-stannp-postcards-api
- collection_type: open
  name: Stannp Direct Mail Account Recipients API
  slug: open-stannp-recipients-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/stannp-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stannp-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stannp-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.stannp.com/us/accreditations
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stannp-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stannp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.stannp.com/us/trust
- group: auth
  title: ''
  type: Authentication
  url: authentication/stannp-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stannp-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/stannp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stannp-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stannp-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stannp-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stannp-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stannp.com/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/stannp-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/stannp-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/stannp-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stannp-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stannp-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stannp-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.stannp.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.stannp.com/us/developer-tools
- group: docs
  title: ''
  type: Documentation
  url: https://www.stannp.com/us/direct-mail-api/guide
- group: docs
  title: ''
  type: APIReference
  url: https://www.stannp.com/us/direct-mail-api/postcards
- group: start
  title: ''
  type: GettingStarted
  url: https://www.stannp.com/us/direct-mail-api/guide#introduction
- group: operate
  title: ''
  type: Support
  url: https://www.stannp.com/us/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.stannp.com/us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stannp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stannp-com-postcard-bulk-mailer
- group: other
  title: ''
  type: X
  url: https://twitter.com/stannpdm
- group: company
  title: ''
  type: Blog
  url: https://go.stannp.com/en-us/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stannp.com/us/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/stannp-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://app-us1.stannp.com/register
- group: start
  title: ''
  type: Login
  url: https://app-us1.stannp.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stannp.com/us/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stannp.com/us/privacy-policy
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stannp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stannp-finops.yml
created: '2026-06-12'
description: Stannp is a direct mail platform that enables businesses to send physical postcards and letters programmatically via a REST API. The platform lets developers create campaigns, upload recipient lists, trigger individual mail pieces in real time, and track print and delivery status through webhooks and event endpoints. Authentication uses API key-based HTTP Basic Auth over HTTPS, and the API follows a simple JSON response envelope with success/data or success/error fields. Stannp serves businesses across the UK, US, and Canada with per-item pricing for letters and postcards at scale, and supports no-code integrations through Zapier and Make as well as official SDKs for PHP, Go, and C#.
examples:
- key_count: 8
  name: Create Postcard Request
  slug: create-postcard-request
- key_count: 2
  name: Create Postcard Response
  slug: create-postcard-response
- key_count: 5
  name: Webhook Payload
  slug: webhook-payload
finops:
- name: Stannp Finops
  service_category: ''
  slug: stannp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stannp.png
json_schemas:
- name: Campaign
  property_count: 8
  slug: campaign
- name: Mailpiece
  property_count: 8
  slug: mailpiece
- name: Recipient
  property_count: 22
  slug: recipient
jsonld:
- class_count: 45
  name: Stannp Context
  property_count: 9
  slug: stannp-context
layout: provider
mcp_servers:
- description: ''
  name: Stannp MCP Server
  slug: stannp-mcp-server
modified: '2026-08-13'
name: Stannp
nav: Providers
network: true
overview: 'Stannp publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Campaigns API, Events API, and 4 more. Tagged areas include Direct Mail, Postcards, Letters, Print, and Physical Mail.


  The Stannp catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Stannp''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 34 more developer resources.'
plans:
- name: Stannp Plans Pricing
  plan_count: 5
  slug: stannp-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Stannp Rate Limits
  slug: stannp-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Stannp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stannp-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 78.0
  coverage:
    artifact_dirs: 29
    catalog_gap: 24.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 43.2
    contract_quality: 75.8
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 43.2
    operational_transparency: 68.4
  previous_composite: 78.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 56.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/screenshots/stannp-2026-06-20T194506.png
security:
- kind: authentication
  name: Stannp Authentication
  slug: stannp-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Stannp Domain Security
  slug: stannp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stannp Vulnerability Disclosure
  slug: stannp-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Stannp Trust Center
  slug: stannp-trust-center
  summary_line: HIPAA, ISO 27001, ISO 9001, GDPR, ICO registration ZA134992 (UK Data Processor), USPS CASS certification, Royal Mail PAF accreditation, Royal Mail Mail Made Easy partner, SecurityScorecard A rating
slug: stannp
tags:
- Direct Mail
- Postcards
- Letters
- Print
- Physical Mail
- Marketing Automation
- Campaigns
- Address Verification
- SMS
- Webhook
- Mailing Lists
- Fulfillment
website: https://www.stannp.com
---
