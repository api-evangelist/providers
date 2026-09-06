---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.people.ai/'', ''status'': 301, ''note'': ''declared website redirects to https://www.backstory.ai/ — a different registrable domain (people.ai -> backstory.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.people.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.people.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.people.ai/about-us/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.people.ai/terms-and-conditions-eusa-10-17-17
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.people.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://app.people.ai/login/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.people.ai/product/trust-security
- group: auth
  title: ''
  type: Compliance
  url: https://www.people.ai/product/trust-security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/peopleai-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/peopleai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peopleai-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/peopleai-well-known.yml
created: '2026-07-17'
description: People.ai is an AI-powered revenue intelligence platform for enterprise sales teams. It automatically captures sales activity and contact data from email, calendar, and meetings, matches it into CRM systems like Salesforce and Microsoft Dynamics 365, and delivers AI-driven forecasting, opportunity management, account execution, and engagement forensics to improve pipeline visibility and drive predictable revenue growth. People.ai integrates with Salesforce, Microsoft, Oracle, Slack, Zoom, Webex, 6sense, and ZoomInfo. It is delivered as an enterprise SaaS product and does not publish a public developer API; its trust and security posture is documented with SOC 2, ISO 27001, ISO 27017, GDPR, and CSA STAR. As of 2026 People.ai has rebranded to Backstory (www.people.ai now 301-redirects to www.backstory.ai); the product login remains at app.people.ai.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peopleai.png
layout: provider
modified: '2026-07-20'
name: People.ai
nav: Providers
network: true
overview: 'People.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Revenue Intelligence, Sales, Artificial Intelligence, and CRM.


  People.ai''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peopleai/refs/heads/main/screenshots/peopleai-2026-09-02T151010.png
security:
- kind: domain-security
  name: Peopleai Domain Security
  slug: peopleai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Peopleai Trust Center
  slug: peopleai-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, GDPR, CSA STAR
slug: peopleai
tags:
- Company
- Revenue Intelligence
- Sales
- Artificial Intelligence
- CRM
- Sales Automation
- Forecasting
- Enterprise
website: https://www.people.ai/
---
