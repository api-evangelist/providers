---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/vela-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vela-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryvela.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryvela.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryvela.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:contact@tryvela.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TryVela
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vela-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.tryvela.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tryvela.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vela-llms.txt
created: '2026-07-17'
description: Vela is an AI scheduling assistant from Y Combinator's Winter 2026 batch that handles the ambiguity that breaks scheduling. Added to any email thread or messaging conversation, it negotiates on the user's behalf — reading context, proposing meeting times across timezones, following up with participants, detecting calendar conflicts, rescheduling, and sending invites once scheduling is finalized. It works across Gmail, Outlook, Slack, Teams, WhatsApp, SMS, and phone, and is used by enterprise recruiters coordinating thousands of multi-party interviews a week as well as executives who need white-glove coordination at scale.
image: https://tryvela.ai/favicon.png
layout: provider
modified: '2026-07-21'
name: Vela
nav: Providers
network: true
overview: 'Vela is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Scheduling, Artificial Intelligence, AI Agents, and Meetings.


  Vela''s developer surface includes support and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 11.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vela/refs/heads/main/screenshots/vela-2026-09-02T165628.png
security:
- kind: domain-security
  name: Vela Domain Security
  slug: vela-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vela Vulnerability Disclosure
  slug: vela-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Vela Trust Center
  slug: vela-trust-center
  summary_line: SOC 2 Type 2, GDPR, CCPA, NIST CSF, NIST AI RMF
slug: vela
tags:
- Company
- Scheduling
- Artificial Intelligence
- AI Agents
- Meetings
- Calendar
- Recruiting
- Productivity
website: https://tryvela.ai
---
