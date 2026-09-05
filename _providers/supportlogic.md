---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.supportlogic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.supportlogic.com/resources/techguides/
- group: operate
  title: ''
  type: Support
  url: https://support.supportlogic.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.supportlogic.com/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.supportlogic.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.supportlogic.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.supportlogic.com/master-service-agreement/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/supportlogic-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/supportlogic-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/supportlogic-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.supportlogic.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/supportlogic-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/supportlogic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.supportlogic.com/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supportlogic-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supportlogic-llms.txt
created: '2026-07-17'
description: SupportLogic is an enterprise AI infrastructure company for customer experience and support operations. Its Service Experience Data Cloud normalizes support data across cases, chat, and voice and enriches it with AI-driven sentiment and predictive signals, while ambient AI agents predict and prevent escalations, detect sentiment, automate case routing, draft replies and knowledge-base articles, and coach support teams. SupportLogic layers on top of existing ticketing/CRM stacks (Salesforce, Zendesk, Freshdesk, ServiceNow, Jira) and exposes its intelligence to AI clients through a first-party hosted MCP server that works with Claude, ChatGPT, and enterprise applications. Surfaced as a portfolio company of General Catalyst and Sierra Ventures and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/supportlogic.png
layout: provider
mcp_servers:
- description: ''
  name: Supportlogic MCP Server
  slug: supportlogic-mcp-server
modified: '2026-07-21'
name: Supportlogic
nav: Providers
network: true
overview: 'Supportlogic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer-Support, Customer Experience, Artificial Intelligence, and Service Experience.


  Supportlogic''s developer surface includes documentation, support, engineering blog, pricing, authentication, and 11 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 24.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/supportlogic/refs/heads/main/screenshots/supportlogic-2026-09-02T161307.png
security:
- kind: authentication
  name: Supportlogic Authentication
  slug: supportlogic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Supportlogic Domain Security
  slug: supportlogic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Supportlogic Vulnerability Disclosure
  slug: supportlogic-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Supportlogic Trust Center
  slug: supportlogic-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, HIPAA, GDPR, CCPA, FIPS 140-2
slug: supportlogic
tags:
- Company
- Customer-Support
- Customer Experience
- Artificial Intelligence
- Service Experience
- Sentiment Analysis
- Escalation Management
- MCP
- Software-as-a-Service
website: https://www.supportlogic.com/
---
