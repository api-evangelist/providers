---
access_model:
  confidence: medium
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Engagespark Agentic Access
  operation_count: 23
  slug: engagespark-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.engagespark.com
  baseurl_source: declared
  description: The Balance API from engageSPARK — 1 operation(s) for balance.
  name: engageSPARK Balance API
  slug: engagespark-balance-api
- baseURL: https://api.engagespark.com
  baseurl_source: declared
  description: The Campaigns API from engageSPARK — 2 operation(s) for campaigns.
  name: engageSPARK Campaigns API
  slug: engagespark-campaigns-api
- baseURL: https://api.engagespark.com
  baseurl_source: declared
  description: The Contacts API from engageSPARK — 2 operation(s) for contacts.
  name: engageSPARK Contacts API
  slug: engagespark-contacts-api
- baseURL: https://api.engagespark.com
  baseurl_source: declared
  description: The Files API from engageSPARK — 2 operation(s) for files.
  name: engageSPARK Files API
  slug: engagespark-files-api
- baseURL: https://api.engagespark.com
  baseurl_source: declared
  description: The SMS API from engageSPARK — 4 operation(s) for sms.
  name: engageSPARK SMS API
  slug: engagespark-sms-api
- baseURL: https://api.engagespark.com
  baseurl_source: declared
  description: The Top-Up API from engageSPARK — 3 operation(s) for top-up.
  name: engageSPARK Top-Up API
  slug: engagespark-top-up-api
- baseURL: https://api.engagespark.com
  baseurl_source: declared
  description: The Whats App API from engageSPARK — 3 operation(s) for whats app.
  name: engageSPARK Whats App API
  slug: engagespark-whats-app-api
artifact_total: 25
asyncapis:
- description: ''
  name: Engagespark Webhooks
  slug: engagespark-webhooks
collections:
- collection_type: open
  name: engageSPARK Balance API
  slug: open-engagespark-balance-api
- collection_type: open
  name: engageSPARK Balance Campaigns API
  slug: open-engagespark-campaigns-api
- collection_type: open
  name: engageSPARK Balance Contacts API
  slug: open-engagespark-contacts-api
- collection_type: open
  name: engageSPARK Balance Files API
  slug: open-engagespark-files-api
- collection_type: open
  name: engageSPARK Balance SMS API
  slug: open-engagespark-sms-api
- collection_type: open
  name: engageSPARK Balance Top-Up API
  slug: open-engagespark-top-up-api
- collection_type: open
  name: engageSPARK Balance WhatsApp API
  slug: open-engagespark-whatsapp-api
common:
- group: commercial
  href: https://artifacts.apis.io/engagespark/plans/engagespark-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/engagespark-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/engagespark/capabilities/engagespark-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/engagespark-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/engagespark/mcp/engagespark-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/engagespark-mcp.yml
- group: other
  href: https://artifacts.apis.io/engagespark/overlays/engagespark-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/engagespark-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/engagespark/agentic-access/engagespark-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/engagespark-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/engagespark/security/engagespark-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/engagespark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://engagespark.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.engagespark.com/support/how-can-i-use-your-api/
- group: docs
  title: ''
  type: Documentation
  url: https://openapi.engagespark.com/
- group: docs
  title: ''
  type: APIReference
  url: https://openapi.engagespark.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.engagespark.com/support/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.engagespark.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.engagespark.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.engagespark.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.engagespark.com/register
- group: start
  title: ''
  type: Login
  url: https://app.engagespark.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.engagespark.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.engagespark.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/engagespark
- group: agent
  href: https://artifacts.apis.io/engagespark/llms/engagespark-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/engagespark-llms.txt
- group: agent
  href: https://artifacts.apis.io/engagespark/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: engageSPARK is a mobile messaging and engagement platform for reaching hard-to-reach populations in low- and middle-income countries at scale. It lets NGOs, researchers, microfinance institutions, and businesses run SMS, automated voice (IVR), WhatsApp, and pre-paid airtime top-up campaigns across 180+ countries without writing code, or programmatically through its HTTP API. The engageSPARK API (api.engagespark.com, v1) exposes token-authenticated endpoints for sending SMS, WhatsApp, and airtime top-ups, managing contacts and organizations, subscribing and unsubscribing contacts to voice and SMS campaigns, reading message and top-up history, checking organization balance, and managing files. Incoming-SMS and campaign-action webhooks let the platform push survey responses and inbound messages into external systems such as Salesforce or Qualtrics.
image: https://www.engagespark.com/wp-content/uploads/2017/03/engagespark_logo_small.png
layout: provider
modified: '2026-07-19'
name: engageSPARK
nav: Providers
network: true
overview: 'engageSPARK publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Balance API, Campaigns API, Contacts API, and 4 more. Tagged areas include Company, Messaging, SMS, Voice, and WhatsApp.


  The engageSPARK catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  engageSPARK''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Engagespark Plans Pricing
  plan_count: 10
  slug: engagespark-plans-pricing
- name: Engagespark Price Estimates
  plan_count: 0
  slug: engagespark-price-estimates
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: engageSPARK API Rules
  rule_count: 66
  severity_counts:
    error: 58
    hint: 0
    info: 2
    warn: 6
  slug: engagespark-rules
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.8
  facets:
    access_clarity: 59.2
    contract_governance: 18.2
    contract_quality: 58.0
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    conformance: derived
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
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/engagespark/engagespark-2026-07-25T213341.png
security:
- kind: authentication
  name: Engagespark Authentication
  slug: engagespark-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Engagespark Domain Security
  slug: engagespark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Subscribe a contact to a campaign
  slug: engagespark-campaign-subscription
- name: Manage contacts
  slug: engagespark-manage-contacts
- name: Send an airtime top-up
  slug: engagespark-send-airtime-topup
- name: Send and track an SMS
  slug: engagespark-send-sms
slug: engagespark
tags:
- Company
- Messaging
- SMS
- Voice
- WhatsApp
- Airtime
- Communications
- CPaaS
- Surveys
- International Development
website: https://engagespark.com
---
