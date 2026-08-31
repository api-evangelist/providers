---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Justcall Agentic Access
  operation_count: 3
  slug: justcall-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: REST API for placing calls, sending SMS and MMS messages, managing contacts, phone numbers, users, and call dispositions in JustCall. Authentication uses an API key and API secret passed in the Author
  name: JustCall REST API
  slug: rest-api
- description: Manage and query voice calls handled through JustCall.
  name: JustCall Calls API
  slug: justcall-calls-api
- description: Create and manage contacts in the JustCall directory.
  name: JustCall Contacts API
  slug: justcall-contacts-api
- description: Send and manage SMS/MMS messages.
  name: JustCall SMS API
  slug: justcall-sms-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: JustCall REST Calls API
  slug: open-justcall-calls-api
- collection_type: open
  name: JustCall REST Calls Contacts API
  slug: open-justcall-contacts-api
- collection_type: open
  name: JustCall REST Calls SMS API
  slug: open-justcall-sms-api
- collection_type: open
  name: JustCall REST API
  slug: open-justcall
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/justcall-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/justcall-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/justcall-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/justcall-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/justcall-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/justcall-io
- group: company
  title: ''
  type: Website
  url: https://justcall.io
- group: docs
  title: ''
  type: Documentation
  url: https://developer.justcall.io/docs/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://justcall.io/developer-docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://justcall.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://justcall.io/signup
- group: operate
  title: ''
  type: Support
  url: https://help.justcall.io
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.justcall.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://justcall.io/blog/
created: '2026-05-11'
description: JustCall is a cloud-based phone system and contact center platform that provides voice calling, SMS/MMS messaging, IVR, call analytics, and contact management for small and mid-sized businesses. The platform integrates with CRMs, helpdesks, and automation tools. JustCall exposes REST APIs and webhooks for programmatically managing calls, SMS, contacts, phone numbers, and call dispositions, authenticated via API key plus API secret in headers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/justcall.png
layout: provider
modified: '2026-05-11'
name: JustCall
nav: Providers
network: true
overview: 'JustCall publishes 3 APIs on the [APIs.io](https://apis.io/) network: Calls API, Contacts API, and SMS API. Tagged areas include Voice, SMS, Cloud Phone, Contact Center, and Telephony.


  JustCall''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/justcall/refs/heads/main/screenshots/justcall-2026-06-20T183845.png
security:
- kind: authentication
  name: Justcall Authentication
  slug: justcall-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Justcall Domain Security
  slug: justcall-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Justcall Trust Center
  slug: justcall-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, CSA STAR
slug: justcall
tags:
- Voice
- SMS
- Cloud Phone
- Contact Center
- Telephony
- Communications
website: https://justcall.io
---
