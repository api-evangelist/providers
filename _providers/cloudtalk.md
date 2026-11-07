---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Cloudtalk Agentic Access
  operation_count: 56
  slug: cloudtalk-agentic-access
  summary_line: 56 operations · 33 acting
api_count: 1
apis:
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: All data you can get about your agents.
  name: CloudTalk Agents API
  slug: cloudtalk-agents-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: Bulk actions.
  name: CloudTalk Bulks API
  slug: cloudtalk-bulks-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: All data you can get about your calls.
  name: CloudTalk Calls API
  slug: cloudtalk-calls-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: All data you can get about your campaigns.
  name: CloudTalk Campaigns API
  slug: cloudtalk-campaigns-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: All data you can get about your contacts.
  name: CloudTalk Contacts API
  slug: cloudtalk-contacts-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: Conversation Intelligence data about your calls.
  name: CloudTalk Conversation Intelligence API
  slug: cloudtalk-conversation-intelligence-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: CueCards API ver. 1.0.2
  name: CloudTalk CueCard API
  slug: cloudtalk-cuecard-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: The Groups API from CloudTalk — 3 operation(s) for groups.
  name: CloudTalk Groups API
  slug: cloudtalk-groups-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: All data you can get about your numbers.
  name: CloudTalk Numbers API
  slug: cloudtalk-numbers-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: Sms handling.
  name: CloudTalk Sms API
  slug: cloudtalk-sms-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: VoiceAgent API ver. 1.0.0
  name: CloudTalk VoiceAgent API
  slug: cloudtalk-voiceagent-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: The tags you create and assign to your contacts.
  name: CloudTalk Contact tags API
  slug: cloudtalk-contact-tags-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: 'Partner API for the CloudTalk sales dialer — campaigns, campaign contacts, call scripts, surveys, disposition buttons, statistics and data exports. The Dialer is a newly released product surface: depe'
  name: CloudTalk Dialer API
  slug: cloudtalk-dialer-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: All other helper endpoints.
  name: CloudTalk Utilities API
  slug: cloudtalk-utilities-api
- baseURL: https://my.cloudtalk.io/api
  baseurl_source: declared
  description: 'Manage webhook endpoints: subscriptions, signing secrets, test events and the delivery log. Endpoints created here and in the Dashboard are the same endpoints.'
  name: CloudTalk Webhooks API
  slug: cloudtalk-webhooks-api
artifact_total: 42
asyncapis:
- description: ''
  name: Cloudtalk Webhooks
  slug: cloudtalk-webhooks
collections:
- collection_type: open
  name: CloudTalk Agents API
  slug: open-cloudtalk-agents-api
- collection_type: open
  name: CloudTalk Agents Bulks API
  slug: open-cloudtalk-bulks-api
- collection_type: open
  name: CloudTalk Agents Calls API
  slug: open-cloudtalk-calls-api
- collection_type: open
  name: CloudTalk Agents Campaigns API
  slug: open-cloudtalk-campaigns-api
- collection_type: open
  name: CloudTalk Agents Contacts API
  slug: open-cloudtalk-contacts-api
- collection_type: open
  name: CloudTalk Agents Conversation Intelligence API
  slug: open-cloudtalk-conversation-intelligence-api
- collection_type: open
  name: CloudTalk Agents CueCard API
  slug: open-cloudtalk-cuecard-api
- collection_type: open
  name: CloudTalk Agents Groups API
  slug: open-cloudtalk-groups-api
- collection_type: open
  name: CloudTalk Agents Numbers API
  slug: open-cloudtalk-numbers-api
- collection_type: open
  name: CloudTalk Agents Other API
  slug: open-cloudtalk-other-api
- collection_type: open
  name: CloudTalk Agents Sms API
  slug: open-cloudtalk-sms-api
- collection_type: open
  name: CloudTalk Agents Tags API
  slug: open-cloudtalk-tags-api
- collection_type: open
  name: CloudTalk Agents VoiceAgent API
  slug: open-cloudtalk-voiceagent-api
common:
- group: other
  href: https://artifacts.apis.io/cloudtalk/capabilities/cloudtalk-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cloudtalk-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cloudtalk.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudtalk.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cloudtalk.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cloudtalk.io/en/collections/441737-getting-started-with-cloudtalk
- group: operate
  title: ''
  type: Support
  url: https://help.cloudtalk.io/en/
- group: company
  title: ''
  type: Blog
  url: https://www.cloudtalk.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CloudTalk-io
- group: operate
  title: ''
  type: Roadmap
  url: https://releases.cloudtalk.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudtalk.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudtalk.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.cloudtalk.io/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudtalk.io/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudtalk.io/privacy-notice/
- group: auth
  href: https://artifacts.apis.io/cloudtalk/authentication/cloudtalk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudtalk-authentication.yml
- group: design
  href: https://artifacts.apis.io/cloudtalk/conventions/cloudtalk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloudtalk-conventions.yml
- group: operate
  href: https://artifacts.apis.io/cloudtalk/rate-limits/cloudtalk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloudtalk-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cloudtalk/plans/cloudtalk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudtalk-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cloudtalk/changelog/cloudtalk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloudtalk-changelog.yml
- group: build
  href: https://artifacts.apis.io/cloudtalk/packages/cloudtalk-packages.yml
  title: ''
  type: Packages
  url: packages/cloudtalk-packages.yml
- group: design
  href: https://artifacts.apis.io/cloudtalk/errors/cloudtalk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudtalk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cloudtalk/lifecycle/cloudtalk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloudtalk-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cloudtalk/conformance/cloudtalk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudtalk-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cloudtalk.io/
- group: auth
  href: https://artifacts.apis.io/cloudtalk/security/cloudtalk-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cloudtalk-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.cloudtalk.io/
- group: auth
  href: https://artifacts.apis.io/cloudtalk/security/cloudtalk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudtalk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cloudtalk/security/cloudtalk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudtalk-domain-security.yml
- group: design
  href: https://artifacts.apis.io/cloudtalk/data-model/cloudtalk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudtalk-data-model.yml
- group: design
  href: https://artifacts.apis.io/cloudtalk/asyncapi/cloudtalk-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cloudtalk-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/cloudtalk/mcp/cloudtalk-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cloudtalk-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cloudtalk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cloudtalk/llms/cloudtalk-help-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudtalk-help-llms.txt
- group: agent
  href: https://artifacts.apis.io/cloudtalk/llms/cloudtalk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudtalk-llms.txt
- group: other
  href: https://artifacts.apis.io/cloudtalk/overlays/cloudtalk-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudtalk-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cloudtalk/agentic-access/cloudtalk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudtalk-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudtalk.io
created: '2026-07-17'
description: CloudTalk is an AI-powered cloud call center and business phone system (CCaaS) for sales and customer support teams, backed by Point Nine. Its public REST API (served at https://my.cloudtalk.io/api, published as OpenAPI 3.0.1 version 1.7) lets developers automate calls, contacts, agents, groups, phone numbers, campaigns, tags, SMS, blacklists and notes, and read Conversation Intelligence data — transcription, sentiment, topics, talk-listen ratio and smart notes — plus initiate VoiceAgent calls. Authentication is HTTPS-only HTTP Basic Auth using an API Access Key ID and Secret; responses are JSON, paginated with a Collections Envelope, and rate limited to 60 requests per minute per company. Events are delivered through Workflow Automation triggers (native and virtual webhooks) rather than the REST API.
finops:
- has_sources: true
  method: derived
  name: Cloudtalk Finops
  primary_unit: user
  service_category: ''
  slug: cloudtalk-finops
  template: false
image: https://www.cloudtalk.sk/files/social/1/Share-Img.png
layout: provider
modified: '2026-08-14'
name: CloudTalk
nav: Providers
network: true
overview: 'CloudTalk publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Bulks API, Calls API, and 12 more. Tagged areas include Company, Communications, Voice, VoIP, and Call Center.


  The CloudTalk catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  CloudTalk''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Cloudtalk Plans Pricing
  plan_count: 15
  slug: cloudtalk-plans-pricing
- name: Cloudtalk Price Estimates
  plan_count: 0
  slug: cloudtalk-price-estimates
random_paper: 3
rate_limits:
- limit_count: 1
  name: Cloudtalk Rate Limits
  slug: cloudtalk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: CloudTalk API Rules
  rule_count: 64
  severity_counts:
    error: 46
    hint: 0
    info: 5
    warn: 13
  slug: cloudtalk-rules
score:
  band: exemplar
  composite: 68.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 67.1
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 68.4
  previous_composite: 62.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 51.7
      total: 29
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/cloudtalk/cloudtalk-2026-07-25T205712.png
security:
- kind: authentication
  name: Cloudtalk Authentication
  slug: cloudtalk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cloudtalk Domain Security
  slug: cloudtalk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloudtalk Vulnerability Disclosure
  slug: cloudtalk-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Cloudtalk Trust Center
  slug: cloudtalk-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 3
skills:
- name: Get CloudTalk Conversation Intelligence for a call
  slug: cloudtalk-conversation-intelligence
- name: Make an outbound CloudTalk call
  slug: cloudtalk-make-outbound-call
- name: Manage CloudTalk contacts
  slug: cloudtalk-manage-contacts
slug: cloudtalk
tags:
- Company
- Communications
- Voice
- VoIP
- Call Center
- Contact Center
- CCaaS
- Telephony
- SMS
- Conversation Intelligence
website: https://www.cloudtalk.io
---
